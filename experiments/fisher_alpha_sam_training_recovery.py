#!/usr/bin/env python3
"""NumPy-only E0b trainable recovery for OQ-B02-004.

This runner checks whether alpha-SAM(alpha=0, lambda=0) recovers the same
training trajectory as a Fisher SAM baseline on a small trainable model.

Scope:
  - model: binary logistic regression
  - data: deterministic 2D Gaussian classification
  - Fisher approximation: empirical diagonal Fisher
  - optimizer: Fisher-ball first-order SAM perturbation + gradient step

This is still a recovery gate, not evidence that alpha-SAM improves Fisher SAM.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "results" / "fisher_alpha_sam_training_recovery.json"


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


def unpack(theta: np.ndarray) -> tuple[np.ndarray, float]:
    return theta[:2], float(theta[2])


def logits(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    w, b = unpack(theta)
    return x @ w + b


def loss_value(theta: np.ndarray, x: np.ndarray, y: np.ndarray) -> float:
    z = logits(theta, x)
    return float(np.mean(np.maximum(z, 0.0) - y * z + np.log1p(np.exp(-np.abs(z)))))


def loss_grad(theta: np.ndarray, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    p = sigmoid(logits(theta, x))
    residual = p - y
    grad_w = x.T @ residual / x.shape[0]
    grad_b = float(np.mean(residual))
    return np.array([grad_w[0], grad_w[1], grad_b], dtype=float)


def accuracy(theta: np.ndarray, x: np.ndarray, y: np.ndarray) -> float:
    pred = sigmoid(logits(theta, x)) >= 0.5
    return float(np.mean(pred == y))


def empirical_fisher_diag(theta: np.ndarray, x: np.ndarray, y: np.ndarray, damping: float) -> np.ndarray:
    p = sigmoid(logits(theta, x))
    residual2 = (p - y) ** 2
    fisher_w = (x * x).T @ residual2 / x.shape[0]
    fisher_b = float(np.mean(residual2))
    return np.array([fisher_w[0], fisher_w[1], fisher_b], dtype=float) + damping


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
    rho: float,
    damping: float,
) -> np.ndarray:
    grad = loss_grad(theta, x, y)
    fisher_diag = empirical_fisher_diag(theta, x, y, damping)
    natural_direction = grad / fisher_diag
    return project_to_fisher_radius(fisher_diag, natural_direction, rho)


def alpha_connection_correction(theta: np.ndarray, eps: np.ndarray) -> np.ndarray:
    """Toy connection-side shift for nonzero alpha.

    The correction is intentionally absent at alpha=0. It keeps E0b focused on
    recovery and gives E1 a nontrivial implementation surface to probe later.
    """
    w0, w1, b = theta
    return np.array(
        [
            eps[0] * eps[2] * (1.0 + 0.05 * np.tanh(w0)),
            eps[1] * eps[2] * (1.0 + 0.05 * np.tanh(w1)),
            -0.5 * (eps[0] * eps[0] + eps[1] * eps[1]) * (1.0 + 0.05 * np.tanh(b)),
        ],
        dtype=float,
    )


def forgetting_gradient(theta: np.ndarray) -> np.ndarray:
    return theta.copy()


def alpha_sam_perturbation(
    theta: np.ndarray,
    x: np.ndarray,
    y: np.ndarray,
    rho: float,
    damping: float,
    alpha: float,
    lam: float,
) -> np.ndarray:
    fisher_diag = empirical_fisher_diag(theta, x, y, damping)
    eps = fisher_sam_perturbation(theta, x, y, rho, damping)
    shifted = eps + alpha * alpha_connection_correction(theta, eps)
    if lam != 0.0:
        shifted = shifted - lam * 0.01 * forgetting_gradient(theta)
    return project_to_fisher_radius(fisher_diag, shifted, rho)


def train(
    condition: str,
    seed: int,
    epochs: int,
    n_per_class: int,
    lr: float,
    rho: float,
    damping: float,
    alpha: float,
    lam: float,
) -> dict:
    x, y = make_dataset(seed=seed, n_per_class=n_per_class)
    rng = np.random.default_rng(10_000 + seed)
    theta = rng.normal(loc=0.0, scale=0.05, size=3)
    history = []

    for epoch in range(epochs + 1):
        if condition == "fisher_sam":
            eps = fisher_sam_perturbation(theta, x, y, rho, damping)
        elif condition == "alpha_sam":
            eps = alpha_sam_perturbation(theta, x, y, rho, damping, alpha, lam)
        else:
            raise ValueError(f"unknown condition: {condition}")

        fisher_diag = empirical_fisher_diag(theta, x, y, damping)
        history.append(
            {
                "epoch": epoch,
                "theta": theta.tolist(),
                "loss": loss_value(theta, x, y),
                "accuracy": accuracy(theta, x, y),
                "eps": eps.tolist(),
                "fisher_radius": fisher_norm(fisher_diag, eps),
                "surrogate_loss": loss_value(theta + eps, x, y),
            }
        )

        if epoch == epochs:
            break

        grad_surrogate = loss_grad(theta + eps, x, y)
        theta = theta - lr * grad_surrogate

    return {
        "condition": condition,
        "seed": seed,
        "epochs": epochs,
        "n_per_class": n_per_class,
        "lr": lr,
        "rho": rho,
        "damping": damping,
        "alpha": alpha,
        "lambda": lam,
        "history": history,
    }


def compare_runs(fisher: dict, alpha0: dict) -> dict:
    max_theta_diff = 0.0
    max_loss_diff = 0.0
    max_accuracy_diff = 0.0
    max_eps_diff = 0.0
    max_radius_diff = 0.0
    max_surrogate_loss_diff = 0.0

    for f_step, a_step in zip(fisher["history"], alpha0["history"]):
        f_theta = np.array(f_step["theta"], dtype=float)
        a_theta = np.array(a_step["theta"], dtype=float)
        f_eps = np.array(f_step["eps"], dtype=float)
        a_eps = np.array(a_step["eps"], dtype=float)
        max_theta_diff = max(max_theta_diff, float(np.max(np.abs(f_theta - a_theta))))
        max_loss_diff = max(max_loss_diff, abs(float(f_step["loss"] - a_step["loss"])))
        max_accuracy_diff = max(max_accuracy_diff, abs(float(f_step["accuracy"] - a_step["accuracy"])))
        max_eps_diff = max(max_eps_diff, float(np.max(np.abs(f_eps - a_eps))))
        max_radius_diff = max(max_radius_diff, abs(float(f_step["fisher_radius"] - a_step["fisher_radius"])))
        max_surrogate_loss_diff = max(
            max_surrogate_loss_diff,
            abs(float(f_step["surrogate_loss"] - a_step["surrogate_loss"])),
        )

    return {
        "seed": fisher["seed"],
        "max_theta_diff": max_theta_diff,
        "max_loss_diff": max_loss_diff,
        "max_accuracy_diff": max_accuracy_diff,
        "max_eps_diff": max_eps_diff,
        "max_fisher_radius_diff": max_radius_diff,
        "max_surrogate_loss_diff": max_surrogate_loss_diff,
        "final_fisher_loss": fisher["history"][-1]["loss"],
        "final_alpha0_loss": alpha0["history"][-1]["loss"],
        "final_fisher_accuracy": fisher["history"][-1]["accuracy"],
        "final_alpha0_accuracy": alpha0["history"][-1]["accuracy"],
    }


def run_recovery(args: argparse.Namespace) -> dict:
    comparisons = []
    runs = []
    for seed in range(args.seeds):
        fisher = train(
            condition="fisher_sam",
            seed=seed,
            epochs=args.epochs,
            n_per_class=args.n_per_class,
            lr=args.lr,
            rho=args.rho,
            damping=args.damping,
            alpha=0.0,
            lam=0.0,
        )
        alpha0 = train(
            condition="alpha_sam",
            seed=seed,
            epochs=args.epochs,
            n_per_class=args.n_per_class,
            lr=args.lr,
            rho=args.rho,
            damping=args.damping,
            alpha=0.0,
            lam=0.0,
        )
        comparisons.append(compare_runs(fisher, alpha0))
        runs.append({"fisher_sam": fisher, "alpha_sam_alpha0_lambda0": alpha0})

    max_summary = {
        "max_theta_diff": max(row["max_theta_diff"] for row in comparisons),
        "max_loss_diff": max(row["max_loss_diff"] for row in comparisons),
        "max_accuracy_diff": max(row["max_accuracy_diff"] for row in comparisons),
        "max_eps_diff": max(row["max_eps_diff"] for row in comparisons),
        "max_fisher_radius_diff": max(row["max_fisher_radius_diff"] for row in comparisons),
        "max_surrogate_loss_diff": max(row["max_surrogate_loss_diff"] for row in comparisons),
    }
    passed = all(value <= args.tol for value in max_summary.values())
    return {
        "case": "OQ-B02-004",
        "gate": "E0b_training_recovery",
        "status": "pass" if passed else "fail",
        "tolerance": args.tol,
        "setup": {
            "model": "binary_logistic_regression",
            "data": "deterministic_2d_gaussian_classification",
            "fisher_approximation": "empirical_diagonal_fisher",
            "seeds": args.seeds,
            "epochs": args.epochs,
            "n_per_class": args.n_per_class,
            "lr": args.lr,
            "rho": args.rho,
            "damping": args.damping,
        },
        "max_summary": max_summary,
        "comparisons": comparisons,
        "runs": runs,
        "interpretation": (
            "E0b checks trajectory recovery for alpha=0/lambda=0 in a trainable "
            "NumPy model. It does not test nonzero alpha direction control."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--epochs", type=int, default=120)
    parser.add_argument("--n-per-class", type=int, default=96)
    parser.add_argument("--lr", type=float, default=0.08)
    parser.add_argument("--rho", type=float, default=0.05)
    parser.add_argument("--damping", type=float, default=1e-3)
    parser.add_argument("--tol", type=float, default=1e-12)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    result = run_recovery(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    compact = {k: result[k] for k in ("case", "gate", "status", "tolerance", "setup", "max_summary")}
    print(json.dumps(compact, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
