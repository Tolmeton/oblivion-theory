#!/usr/bin/env python3
"""NumPy-only E1 direction probe for OQ-B02-004.

The recovery gates E0a/E0b test alpha=0/lambda=0. This E1 probe asks whether
nonzero alpha changes the representation trajectory while the Fisher radius is
kept comparable.

Scope:
  - model: small tanh MLP
  - data: deterministic 2D Gaussian classification
  - Fisher approximation: empirical diagonal Fisher
  - alpha implementation: toy connection-side direction shift, projected back
    to the same Fisher radius

This is a direction-control probe, not a full Amari alpha-connection
implementation and not a performance claim.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "results" / "fisher_alpha_sam_direction_probe.json"


def sigmoid(logits: np.ndarray) -> np.ndarray:
    positive = logits >= 0
    out = np.empty_like(logits, dtype=float)
    out[positive] = 1.0 / (1.0 + np.exp(-logits[positive]))
    exp_x = np.exp(logits[~positive])
    out[~positive] = exp_x / (1.0 + exp_x)
    return out


def make_dataset(seed: int, n_per_class: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    cov = np.array([[0.55, 0.18], [0.18, 0.45]], dtype=float)
    x0 = rng.multivariate_normal(mean=np.array([-1.0, -0.7]), cov=cov, size=n_per_class)
    x1 = rng.multivariate_normal(mean=np.array([1.0, 0.7]), cov=cov, size=n_per_class)
    x = np.vstack([x0, x1])
    y = np.concatenate([np.zeros(n_per_class), np.ones(n_per_class)])
    order = rng.permutation(x.shape[0])
    x = x[order]
    y = y[order]
    return standardize(x), y


def standardize(x: np.ndarray) -> np.ndarray:
    mean = x.mean(axis=0, keepdims=True)
    std = x.std(axis=0, keepdims=True) + 1e-12
    return (x - mean) / std


def dims(hidden_dim: int) -> dict[str, slice]:
    i0 = 0
    i1 = i0 + 2 * hidden_dim
    i2 = i1 + hidden_dim
    i3 = i2 + hidden_dim
    i4 = i3 + 1
    return {
        "W1": slice(i0, i1),
        "b1": slice(i1, i2),
        "W2": slice(i2, i3),
        "b2": slice(i3, i4),
    }


def param_size(hidden_dim: int) -> int:
    return 4 * hidden_dim + 1


def unpack(theta: np.ndarray, hidden_dim: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    sl = dims(hidden_dim)
    W1 = theta[sl["W1"]].reshape(2, hidden_dim)
    b1 = theta[sl["b1"]]
    W2 = theta[sl["W2"]]
    b2 = float(theta[sl["b2"]][0])
    return W1, b1, W2, b2


def forward(theta: np.ndarray, x: np.ndarray, hidden_dim: int) -> tuple[np.ndarray, np.ndarray]:
    W1, b1, W2, b2 = unpack(theta, hidden_dim)
    hidden = np.tanh(x @ W1 + b1)
    logit = hidden @ W2 + b2
    return hidden, logit


def loss_value(theta: np.ndarray, x: np.ndarray, y: np.ndarray, hidden_dim: int) -> float:
    _, z = forward(theta, x, hidden_dim)
    return float(np.mean(np.maximum(z, 0.0) - y * z + np.log1p(np.exp(-np.abs(z)))))


def accuracy(theta: np.ndarray, x: np.ndarray, y: np.ndarray, hidden_dim: int) -> float:
    _, z = forward(theta, x, hidden_dim)
    return float(np.mean((sigmoid(z) >= 0.5) == y))


def loss_grad(theta: np.ndarray, x: np.ndarray, y: np.ndarray, hidden_dim: int) -> np.ndarray:
    W1, b1, W2, _ = unpack(theta, hidden_dim)
    h = np.tanh(x @ W1 + b1)
    p = sigmoid(h @ W2 + unpack(theta, hidden_dim)[3])
    dz = (p - y) / x.shape[0]
    grad_W2 = h.T @ dz
    grad_b2 = np.array([np.sum(dz)])
    dh = dz[:, None] * W2[None, :]
    da = dh * (1.0 - h * h)
    grad_W1 = x.T @ da
    grad_b1 = da.sum(axis=0)
    return np.concatenate([grad_W1.ravel(), grad_b1, grad_W2, grad_b2]).astype(float)


def per_sample_grads(theta: np.ndarray, x: np.ndarray, y: np.ndarray, hidden_dim: int) -> np.ndarray:
    W1, b1, W2, b2 = unpack(theta, hidden_dim)
    grads = np.zeros((x.shape[0], theta.size), dtype=float)
    for i in range(x.shape[0]):
        xi = x[i : i + 1]
        yi = y[i]
        h = np.tanh(xi @ W1 + b1)[0]
        p = float(sigmoid(np.array([h @ W2 + b2]))[0])
        dz = p - yi
        grad_W2 = h * dz
        grad_b2 = np.array([dz])
        da = dz * W2 * (1.0 - h * h)
        grad_W1 = np.outer(xi[0], da)
        grad_b1 = da
        grads[i] = np.concatenate([grad_W1.ravel(), grad_b1, grad_W2, grad_b2])
    return grads


def empirical_fisher_diag(theta: np.ndarray, x: np.ndarray, y: np.ndarray, hidden_dim: int, damping: float) -> np.ndarray:
    grads = per_sample_grads(theta, x, y, hidden_dim)
    return np.mean(grads * grads, axis=0) + damping


def fisher_norm(diag: np.ndarray, vector: np.ndarray) -> float:
    return float(np.sqrt(max(np.sum(diag * vector * vector), 0.0)))


def project_to_fisher_radius(diag: np.ndarray, vector: np.ndarray, rho: float) -> np.ndarray:
    norm = fisher_norm(diag, vector)
    if norm < 1e-15:
        return np.zeros_like(vector, dtype=float)
    return vector * (rho / norm)


def fisher_sam_perturbation(
    theta: np.ndarray,
    x: np.ndarray,
    y: np.ndarray,
    hidden_dim: int,
    rho: float,
    damping: float,
) -> np.ndarray:
    grad = loss_grad(theta, x, y, hidden_dim)
    fisher_diag = empirical_fisher_diag(theta, x, y, hidden_dim, damping)
    natural_direction = grad / fisher_diag
    return project_to_fisher_radius(fisher_diag, natural_direction, rho)


def alpha_connection_correction(theta: np.ndarray, eps: np.ndarray, scale: float) -> np.ndarray:
    """Toy non-parallel direction shift used only for E1 probing."""
    gate = 1.0 + 0.1 * np.tanh(theta)
    rotated = np.roll(eps * gate, 1) - 0.25 * eps
    centered = rotated - np.mean(rotated)
    return scale * centered


def alpha_sam_perturbation(
    theta: np.ndarray,
    x: np.ndarray,
    y: np.ndarray,
    hidden_dim: int,
    rho: float,
    damping: float,
    alpha: float,
    correction_scale: float,
) -> np.ndarray:
    fisher_diag = empirical_fisher_diag(theta, x, y, hidden_dim, damping)
    eps = fisher_sam_perturbation(theta, x, y, hidden_dim, rho, damping)
    shifted = eps + alpha * alpha_connection_correction(theta, eps, correction_scale)
    return project_to_fisher_radius(fisher_diag, shifted, rho)


def linear_cka(X: np.ndarray, Y: np.ndarray) -> float:
    Xc = X - X.mean(axis=0, keepdims=True)
    Yc = Y - Y.mean(axis=0, keepdims=True)
    GX = Xc @ Xc.T
    GY = Yc @ Yc.T
    hsic_xy = float(np.sum(GX * GY))
    hsic_xx = float(np.sum(GX * GX))
    hsic_yy = float(np.sum(GY * GY))
    denom = np.sqrt(hsic_xx * hsic_yy)
    if denom < 1e-15:
        return 0.0
    return hsic_xy / denom


def diag_gaussian_kl(X: np.ndarray, Y: np.ndarray) -> float:
    """KL(N_X || N_Y) with diagonal Gaussian moments."""
    mx = X.mean(axis=0)
    my = Y.mean(axis=0)
    vx = X.var(axis=0) + 1e-8
    vy = Y.var(axis=0) + 1e-8
    return float(0.5 * np.sum(vx / vy + (my - mx) ** 2 / vy - 1.0 + np.log(vy / vx)))


def train(
    seed: int,
    alpha: float,
    args: argparse.Namespace,
) -> dict:
    x, y = make_dataset(seed=seed, n_per_class=args.n_per_class)
    rng = np.random.default_rng(20_000 + seed)
    theta = rng.normal(loc=0.0, scale=0.12, size=param_size(args.hidden_dim))
    history = []

    for epoch in range(args.epochs + 1):
        eps = alpha_sam_perturbation(
            theta,
            x,
            y,
            args.hidden_dim,
            args.rho,
            args.damping,
            alpha,
            args.correction_scale,
        )
        fisher_diag = empirical_fisher_diag(theta, x, y, args.hidden_dim, args.damping)
        hidden, _ = forward(theta, x, args.hidden_dim)
        if epoch % args.checkpoint_interval == 0 or epoch == args.epochs:
            history.append(
                {
                    "epoch": epoch,
                    "theta": theta.tolist(),
                    "loss": loss_value(theta, x, y, args.hidden_dim),
                    "accuracy": accuracy(theta, x, y, args.hidden_dim),
                    "fisher_radius": fisher_norm(fisher_diag, eps),
                    "surrogate_loss": loss_value(theta + eps, x, y, args.hidden_dim),
                    "hidden": hidden.tolist(),
                }
            )
        if epoch == args.epochs:
            break
        grad_surrogate = loss_grad(theta + eps, x, y, args.hidden_dim)
        theta = theta - args.lr * grad_surrogate

    return {
        "seed": seed,
        "alpha": alpha,
        "epochs": args.epochs,
        "history": history,
    }


def compare_to_alpha0(alpha_run: dict, zero_run: dict, rho: float) -> dict:
    rows = []
    max_radius_error = 0.0
    for a_step, z_step in zip(alpha_run["history"], zero_run["history"]):
        hidden_a = np.array(a_step["hidden"], dtype=float)
        hidden_z = np.array(z_step["hidden"], dtype=float)
        cka = linear_cka(hidden_a, hidden_z)
        kl = diag_gaussian_kl(hidden_a, hidden_z)
        theta_delta = float(np.linalg.norm(np.array(a_step["theta"]) - np.array(z_step["theta"])))
        radius_error = abs(float(a_step["fisher_radius"]) - rho)
        max_radius_error = max(max_radius_error, radius_error)
        rows.append(
            {
                "epoch": a_step["epoch"],
                "cka_vs_alpha0": cka,
                "phi_cka_vs_alpha0": 1.0 - cka,
                "diag_gaussian_kl_vs_alpha0": kl,
                "theta_delta_vs_alpha0": theta_delta,
                "loss_delta_vs_alpha0": abs(float(a_step["loss"] - z_step["loss"])),
                "accuracy_delta_vs_alpha0": abs(float(a_step["accuracy"] - z_step["accuracy"])),
                "fisher_radius_error": radius_error,
            }
        )
    final = rows[-1]
    return {
        "seed": alpha_run["seed"],
        "alpha": alpha_run["alpha"],
        "max_radius_error": max_radius_error,
        "max_phi_cka": max(row["phi_cka_vs_alpha0"] for row in rows),
        "max_diag_gaussian_kl": max(row["diag_gaussian_kl_vs_alpha0"] for row in rows),
        "max_theta_delta": max(row["theta_delta_vs_alpha0"] for row in rows),
        "final_phi_cka": final["phi_cka_vs_alpha0"],
        "final_diag_gaussian_kl": final["diag_gaussian_kl_vs_alpha0"],
        "final_theta_delta": final["theta_delta_vs_alpha0"],
        "rows": rows,
    }


def run_probe(args: argparse.Namespace) -> dict:
    alphas = [float(a) for a in args.alphas.split(",")]
    if 0.0 not in alphas:
        alphas.append(0.0)
    alphas = sorted(set(alphas))

    runs = []
    comparisons = []
    for seed in range(args.seeds):
        by_alpha = {alpha: train(seed, alpha, args) for alpha in alphas}
        zero_run = by_alpha[0.0]
        for alpha, run in by_alpha.items():
            runs.append(run)
            if alpha != 0.0:
                comparisons.append(compare_to_alpha0(run, zero_run, args.rho))

    max_radius_error = max(row["max_radius_error"] for row in comparisons)
    mean_final_phi = float(np.mean([row["final_phi_cka"] for row in comparisons]))
    mean_final_kl = float(np.mean([row["final_diag_gaussian_kl"] for row in comparisons]))
    min_final_phi = float(np.min([row["final_phi_cka"] for row in comparisons]))
    min_final_kl = float(np.min([row["final_diag_gaussian_kl"] for row in comparisons]))
    max_theta_delta = float(np.max([row["max_theta_delta"] for row in comparisons]))

    radius_pass = max_radius_error <= args.radius_tol
    representation_pass = mean_final_phi >= args.min_phi_cka and mean_final_kl >= args.min_kl
    status = "pass" if radius_pass and representation_pass else "fail"

    return {
        "case": "OQ-B02-004",
        "gate": "E1_direction_probe",
        "status": status,
        "setup": {
            "model": "numpy_tanh_mlp",
            "data": "deterministic_2d_gaussian_classification",
            "fisher_approximation": "empirical_diagonal_fisher",
            "alphas": alphas,
            "seeds": args.seeds,
            "epochs": args.epochs,
            "hidden_dim": args.hidden_dim,
            "n_per_class": args.n_per_class,
            "lr": args.lr,
            "rho": args.rho,
            "damping": args.damping,
            "correction_scale": args.correction_scale,
        },
        "thresholds": {
            "radius_tol": args.radius_tol,
            "min_phi_cka": args.min_phi_cka,
            "min_kl": args.min_kl,
        },
        "summary": {
            "radius_pass": radius_pass,
            "representation_pass": representation_pass,
            "max_fisher_radius_error": max_radius_error,
            "mean_final_phi_cka": mean_final_phi,
            "min_final_phi_cka": min_final_phi,
            "mean_final_diag_gaussian_kl": mean_final_kl,
            "min_final_diag_gaussian_kl": min_final_kl,
            "max_theta_delta": max_theta_delta,
        },
        "comparisons": comparisons,
        "runs": runs,
        "interpretation": (
            "E1 checks whether nonzero alpha changes hidden representations "
            "while each perturbation is projected to the same Fisher radius. "
            "This is a toy connection-side direction probe, not a full Amari "
            "alpha-connection implementation."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--alphas", default="-0.5,0.0,0.5")
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--epochs", type=int, default=160)
    parser.add_argument("--checkpoint-interval", type=int, default=20)
    parser.add_argument("--hidden-dim", type=int, default=6)
    parser.add_argument("--n-per-class", type=int, default=96)
    parser.add_argument("--lr", type=float, default=0.06)
    parser.add_argument("--rho", type=float, default=0.05)
    parser.add_argument("--damping", type=float, default=1e-3)
    parser.add_argument("--correction-scale", type=float, default=2.0)
    parser.add_argument("--radius-tol", type=float, default=1e-10)
    parser.add_argument("--min-phi-cka", type=float, default=1e-6)
    parser.add_argument("--min-kl", type=float, default=1e-6)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    result = run_probe(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    compact = {k: result[k] for k in ("case", "gate", "status", "setup", "thresholds", "summary")}
    print(json.dumps(compact, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
