#!/usr/bin/env python3
"""NumPy-only E2 lambda probe for OQ-B02-004.

E0a/E0b established alpha=0/lambda=0 recovery. E1 established that nonzero
alpha can change hidden representations while preserving Fisher radius. E2 asks
whether a forgetting-field lambda term can move the representation profile
without merely changing accuracy.

Scope:
  - model: small tanh MLP
  - data: deterministic 2D Gaussian classification
  - alpha: fixed nonzero direction-control value
  - lambda term: finite-difference gradient of R(theta) = Phi_CKA(theta)^2,
    where Phi_CKA = 1 - CKA(hidden(theta), hidden(theta_initial))

This is a toy operational probe for the theory case, not a full torch/CIFAR or
full Amari alpha-connection implementation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "results" / "fisher_alpha_sam_lambda_probe.json"


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
    mean = x.mean(axis=0, keepdims=True)
    std = x.std(axis=0, keepdims=True) + 1e-12
    return (x - mean) / std, y


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
    W1, b1, W2, b2 = unpack(theta, hidden_dim)
    h = np.tanh(x @ W1 + b1)
    p = sigmoid(h @ W2 + b2)
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
    mx = X.mean(axis=0)
    my = Y.mean(axis=0)
    vx = X.var(axis=0) + 1e-8
    vy = Y.var(axis=0) + 1e-8
    return float(0.5 * np.sum(vx / vy + (my - mx) ** 2 / vy - 1.0 + np.log(vy / vx)))


def phi_cka(theta: np.ndarray, x: np.ndarray, hidden_ref: np.ndarray, hidden_dim: int) -> float:
    hidden, _ = forward(theta, x, hidden_dim)
    return 1.0 - linear_cka(hidden, hidden_ref)


def forgetting_regularizer(theta: np.ndarray, x: np.ndarray, hidden_ref: np.ndarray, hidden_dim: int) -> float:
    phi = phi_cka(theta, x, hidden_ref, hidden_dim)
    return float(phi * phi)


def central_gradient_regularizer(
    theta: np.ndarray,
    x: np.ndarray,
    hidden_ref: np.ndarray,
    hidden_dim: int,
    h: float,
) -> np.ndarray:
    grad = np.zeros_like(theta, dtype=float)
    for idx in range(theta.size):
        step = np.zeros_like(theta, dtype=float)
        step[idx] = h
        plus = forgetting_regularizer(theta + step, x, hidden_ref, hidden_dim)
        minus = forgetting_regularizer(theta - step, x, hidden_ref, hidden_dim)
        grad[idx] = (plus - minus) / (2.0 * h)
    return grad


def train(seed: int, lam: float, args: argparse.Namespace) -> dict:
    x, y = make_dataset(seed=seed, n_per_class=args.n_per_class)
    rng = np.random.default_rng(30_000 + seed)
    theta = rng.normal(loc=0.0, scale=0.12, size=param_size(args.hidden_dim))
    hidden_ref, _ = forward(theta, x, args.hidden_dim)
    history = []

    for epoch in range(args.epochs + 1):
        eps = alpha_sam_perturbation(
            theta,
            x,
            y,
            args.hidden_dim,
            args.rho,
            args.damping,
            args.alpha,
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
                    "phi_vs_initial": 1.0 - linear_cka(hidden, hidden_ref),
                    "kl_vs_initial": diag_gaussian_kl(hidden, hidden_ref),
                    "fisher_radius": fisher_norm(fisher_diag, eps),
                    "surrogate_loss": loss_value(theta + eps, x, y, args.hidden_dim),
                }
            )
        if epoch == args.epochs:
            break

        grad_surrogate = loss_grad(theta + eps, x, y, args.hidden_dim)
        grad_reg = central_gradient_regularizer(
            theta,
            x,
            hidden_ref,
            args.hidden_dim,
            args.fd_step,
        )
        theta = theta - args.lr * (grad_surrogate + lam * grad_reg)

    return {
        "seed": seed,
        "lambda": lam,
        "alpha": args.alpha,
        "epochs": args.epochs,
        "history": history,
    }


def compare_to_lambda0(lambda_run: dict, zero_run: dict, rho: float) -> dict:
    rows = []
    max_radius_error = 0.0
    for l_step, z_step in zip(lambda_run["history"], zero_run["history"]):
        theta_delta = float(np.linalg.norm(np.array(l_step["theta"]) - np.array(z_step["theta"])))
        radius_error = abs(float(l_step["fisher_radius"]) - rho)
        max_radius_error = max(max_radius_error, radius_error)
        rows.append(
            {
                "epoch": l_step["epoch"],
                "phi_delta_vs_lambda0": float(l_step["phi_vs_initial"] - z_step["phi_vs_initial"]),
                "abs_phi_delta_vs_lambda0": abs(float(l_step["phi_vs_initial"] - z_step["phi_vs_initial"])),
                "kl_delta_vs_lambda0": float(l_step["kl_vs_initial"] - z_step["kl_vs_initial"]),
                "abs_kl_delta_vs_lambda0": abs(float(l_step["kl_vs_initial"] - z_step["kl_vs_initial"])),
                "theta_delta_vs_lambda0": theta_delta,
                "loss_delta_vs_lambda0": abs(float(l_step["loss"] - z_step["loss"])),
                "accuracy_delta_vs_lambda0": abs(float(l_step["accuracy"] - z_step["accuracy"])),
                "fisher_radius_error": radius_error,
            }
        )
    final = rows[-1]
    return {
        "seed": lambda_run["seed"],
        "lambda": lambda_run["lambda"],
        "max_radius_error": max_radius_error,
        "max_abs_phi_delta": max(row["abs_phi_delta_vs_lambda0"] for row in rows),
        "max_abs_kl_delta": max(row["abs_kl_delta_vs_lambda0"] for row in rows),
        "max_theta_delta": max(row["theta_delta_vs_lambda0"] for row in rows),
        "max_loss_delta": max(row["loss_delta_vs_lambda0"] for row in rows),
        "max_accuracy_delta": max(row["accuracy_delta_vs_lambda0"] for row in rows),
        "final_phi_delta": final["phi_delta_vs_lambda0"],
        "final_abs_phi_delta": final["abs_phi_delta_vs_lambda0"],
        "final_kl_delta": final["kl_delta_vs_lambda0"],
        "final_abs_kl_delta": final["abs_kl_delta_vs_lambda0"],
        "final_accuracy_delta": final["accuracy_delta_vs_lambda0"],
        "rows": rows,
    }


def run_probe(args: argparse.Namespace) -> dict:
    lambdas = [float(v) for v in args.lambdas.split(",")]
    if 0.0 not in lambdas:
        lambdas.append(0.0)
    lambdas = sorted(set(lambdas))

    runs = []
    comparisons = []
    for seed in range(args.seeds):
        by_lambda = {lam: train(seed, lam, args) for lam in lambdas}
        zero_run = by_lambda[0.0]
        for lam, run in by_lambda.items():
            runs.append(run)
            if lam != 0.0:
                comparisons.append(compare_to_lambda0(run, zero_run, args.rho))

    max_radius_error = max(row["max_radius_error"] for row in comparisons)
    max_accuracy_delta = max(row["max_accuracy_delta"] for row in comparisons)
    mean_final_abs_phi_delta = float(np.mean([row["final_abs_phi_delta"] for row in comparisons]))
    min_final_abs_phi_delta = float(np.min([row["final_abs_phi_delta"] for row in comparisons]))
    mean_final_abs_kl_delta = float(np.mean([row["final_abs_kl_delta"] for row in comparisons]))
    min_final_abs_kl_delta = float(np.min([row["final_abs_kl_delta"] for row in comparisons]))
    max_theta_delta = float(np.max([row["max_theta_delta"] for row in comparisons]))

    radius_pass = max_radius_error <= args.radius_tol
    accuracy_pass = max_accuracy_delta <= args.max_accuracy_delta
    profile_pass = (
        mean_final_abs_phi_delta >= args.min_mean_abs_phi_delta
        and mean_final_abs_kl_delta >= args.min_mean_abs_kl_delta
    )
    status = "pass" if radius_pass and accuracy_pass and profile_pass else "fail"

    return {
        "case": "OQ-B02-004",
        "gate": "E2_lambda_probe",
        "status": status,
        "setup": {
            "model": "numpy_tanh_mlp",
            "data": "deterministic_2d_gaussian_classification",
            "fisher_approximation": "empirical_diagonal_fisher",
            "alpha": args.alpha,
            "lambdas": lambdas,
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
            "max_accuracy_delta": args.max_accuracy_delta,
            "min_mean_abs_phi_delta": args.min_mean_abs_phi_delta,
            "min_mean_abs_kl_delta": args.min_mean_abs_kl_delta,
        },
        "summary": {
            "radius_pass": radius_pass,
            "accuracy_pass": accuracy_pass,
            "profile_pass": profile_pass,
            "max_fisher_radius_error": max_radius_error,
            "max_accuracy_delta": max_accuracy_delta,
            "mean_final_abs_phi_delta": mean_final_abs_phi_delta,
            "min_final_abs_phi_delta": min_final_abs_phi_delta,
            "mean_final_abs_kl_delta": mean_final_abs_kl_delta,
            "min_final_abs_kl_delta": min_final_abs_kl_delta,
            "max_theta_delta": max_theta_delta,
        },
        "comparisons": comparisons,
        "runs": runs,
        "interpretation": (
            "E2 checks whether a lambda-weighted CKA forgetting regularizer "
            "moves the representation profile while preserving Fisher radius "
            "and comparable accuracy. This is a toy operational probe."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambdas", default="-0.08,0.0,0.08")
    parser.add_argument("--alpha", type=float, default=0.5)
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--checkpoint-interval", type=int, default=20)
    parser.add_argument("--hidden-dim", type=int, default=6)
    parser.add_argument("--n-per-class", type=int, default=96)
    parser.add_argument("--lr", type=float, default=0.06)
    parser.add_argument("--rho", type=float, default=0.05)
    parser.add_argument("--damping", type=float, default=1e-3)
    parser.add_argument("--correction-scale", type=float, default=2.0)
    parser.add_argument("--fd-step", type=float, default=1e-4)
    parser.add_argument("--radius-tol", type=float, default=1e-10)
    parser.add_argument("--max-accuracy-delta", type=float, default=0.08)
    parser.add_argument("--min-mean-abs-phi-delta", type=float, default=1e-4)
    parser.add_argument("--min-mean-abs-kl-delta", type=float, default=1e-4)
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
