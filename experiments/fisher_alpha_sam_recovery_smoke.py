#!/usr/bin/env python3
"""NumPy-only E0a smoke for OQ-B02-004.

This script checks the implementation-level specialization:
alpha-SAM(alpha=0, lambda=0) must reduce to the same Fisher-ball
first-order perturbation used by the Fisher SAM baseline.

It is not an empirical training result. It is a definition recovery gate.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "results" / "fisher_alpha_sam_recovery_smoke.json"


def logsumexp(values: np.ndarray) -> float:
    vmax = float(np.max(values))
    return vmax + float(np.log(np.sum(np.exp(values - vmax))))


def kl_normal(theta: np.ndarray, target_mu: float, target_sigma: float) -> float:
    """KL(N(mu, sigma^2) || N(target_mu, target_sigma^2)).

    theta = (mu, log_sigma), so sigma is always positive.
    """
    mu, log_sigma = float(theta[0]), float(theta[1])
    sigma2 = float(np.exp(2.0 * log_sigma))
    target_var = target_sigma * target_sigma
    return (
        np.log(target_sigma)
        - log_sigma
        + (sigma2 + (mu - target_mu) ** 2) / (2.0 * target_var)
        - 0.5
    )


def toy_fisher_sam_loss(theta: np.ndarray) -> float:
    """Fisher-SAM-paper-inspired 2D KL mixture loss."""
    components = [
        (0.7, 20.0, 30.0, 1.8),
        (0.3, -20.0, 10.0, 1.2),
    ]
    logits = []
    for weight, target_mu, target_sigma, beta in components:
        energy = kl_normal(theta, target_mu, target_sigma)
        logits.append(np.log(weight) - energy / beta)
    return -logsumexp(np.array(logits, dtype=float))


def central_gradient(fn: Callable[[np.ndarray], float], theta: np.ndarray, h: float = 1e-5) -> np.ndarray:
    grad = np.zeros_like(theta, dtype=float)
    for idx in range(theta.size):
        step = np.zeros_like(theta, dtype=float)
        step[idx] = h
        grad[idx] = (fn(theta + step) - fn(theta - step)) / (2.0 * h)
    return grad


def fisher_metric(theta: np.ndarray) -> np.ndarray:
    """Fisher metric for N(mu, sigma^2) in coordinates (mu, log_sigma)."""
    log_sigma = float(theta[1])
    return np.diag([np.exp(-2.0 * log_sigma), 2.0])


def fisher_norm(metric: np.ndarray, vector: np.ndarray) -> float:
    return float(np.sqrt(max(vector @ metric @ vector, 0.0)))


def project_to_fisher_radius(metric: np.ndarray, vector: np.ndarray, rho: float) -> np.ndarray:
    norm = fisher_norm(metric, vector)
    if norm < 1e-15:
        return np.zeros_like(vector, dtype=float)
    return vector * (rho / norm)


def fisher_sam_perturbation(theta: np.ndarray, rho: float) -> np.ndarray:
    """First-order maximizer over a Fisher ball."""
    metric = fisher_metric(theta)
    grad = central_gradient(toy_fisher_sam_loss, theta)
    natural_direction = np.linalg.solve(metric, grad)
    return project_to_fisher_radius(metric, natural_direction, rho)


def toy_alpha_connection_correction(theta: np.ndarray, eps: np.ndarray) -> np.ndarray:
    """Toy connection-side direction shift.

    This is a smoke-test surrogate for checking the harness. It is not the
    full Amari alpha-connection implementation.
    """
    mu, log_sigma = float(theta[0]), float(theta[1])
    return np.array(
        [
            eps[0] * eps[1] * (1.0 + 0.1 * np.tanh(mu / 10.0)),
            -0.5 * eps[0] * eps[0] * (1.0 + 0.1 * np.tanh(log_sigma)),
        ],
        dtype=float,
    )


def toy_forgetting_gradient(theta: np.ndarray) -> np.ndarray:
    """Gradient of KL to N(0,1), used only when lambda is nonzero."""
    mu, log_sigma = float(theta[0]), float(theta[1])
    return np.array([mu, np.exp(2.0 * log_sigma) - 1.0], dtype=float)


def alpha_sam_perturbation(theta: np.ndarray, rho: float, alpha: float, lam: float) -> np.ndarray:
    """alpha/lambda wrapper around the Fisher-ball perturbation."""
    metric = fisher_metric(theta)
    eps = fisher_sam_perturbation(theta, rho)
    shifted = eps + alpha * toy_alpha_connection_correction(theta, eps)
    if lam != 0.0:
        shifted = shifted - lam * 0.01 * toy_forgetting_gradient(theta)
    return project_to_fisher_radius(metric, shifted, rho)


def theta_grid() -> list[np.ndarray]:
    mus = np.linspace(-8.0, 8.0, 9)
    log_sigmas = np.linspace(np.log(0.6), np.log(2.5), 7)
    return [np.array([mu, log_sigma], dtype=float) for mu in mus for log_sigma in log_sigmas]


def run_smoke(rho: float, tol: float) -> dict:
    records = []
    max_eps_diff = 0.0
    max_loss_diff = 0.0
    max_radius_error = 0.0
    e1_direction_deltas = []

    for theta in theta_grid():
        metric = fisher_metric(theta)
        fisher_eps = fisher_sam_perturbation(theta, rho)
        alpha0_eps = alpha_sam_perturbation(theta, rho, alpha=0.0, lam=0.0)

        eps_diff = float(np.linalg.norm(fisher_eps - alpha0_eps))
        fisher_surrogate = toy_fisher_sam_loss(theta + fisher_eps)
        alpha0_surrogate = toy_fisher_sam_loss(theta + alpha0_eps)
        loss_diff = abs(float(fisher_surrogate - alpha0_surrogate))
        radius_error = abs(fisher_norm(metric, alpha0_eps) - rho)

        max_eps_diff = max(max_eps_diff, eps_diff)
        max_loss_diff = max(max_loss_diff, loss_diff)
        max_radius_error = max(max_radius_error, radius_error)

        alpha_plus = alpha_sam_perturbation(theta, rho, alpha=0.5, lam=0.0)
        direction_delta = float(np.linalg.norm(alpha_plus - fisher_eps))
        e1_direction_deltas.append(direction_delta)

        records.append(
            {
                "theta": theta.tolist(),
                "fisher_eps": fisher_eps.tolist(),
                "alpha0_eps": alpha0_eps.tolist(),
                "eps_diff": eps_diff,
                "surrogate_loss_diff": loss_diff,
                "alpha_plus_direction_delta": direction_delta,
            }
        )

    passed = max_eps_diff <= tol and max_loss_diff <= tol and max_radius_error <= 1e-10
    return {
        "case": "OQ-B02-004",
        "gate": "E0a_definition_smoke",
        "rho": rho,
        "tolerance": tol,
        "status": "pass" if passed else "fail",
        "max_eps_diff": max_eps_diff,
        "max_surrogate_loss_diff": max_loss_diff,
        "max_fisher_radius_error": max_radius_error,
        "mean_alpha_plus_direction_delta": float(np.mean(e1_direction_deltas)),
        "min_alpha_plus_direction_delta": float(np.min(e1_direction_deltas)),
        "n_points": len(records),
        "records": records,
        "interpretation": (
            "E0a only checks alpha=0/lambda=0 implementation recovery. "
            "It does not validate training behavior or the full alpha-connection."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rho", type=float, default=0.05)
    parser.add_argument("--tol", type=float, default=1e-12)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    result = run_smoke(rho=args.rho, tol=args.tol)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({k: result[k] for k in result if k != "records"}, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
