#!/usr/bin/env python3
"""
Phase 1 integer proxy scan for Paper V strong-coupling work.

This script intentionally stays on a 3D scalar phi^4 proxy with local
Metropolis updates. Fractional-dimension proxies and T-projected lattices are
left for the next cycle.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from strong_coupling_common import (
    DIMENSION_MODE_INTEGER,
    RESULTS_DIR,
    bootstrap_estimate,
    build_cubic_geometry,
    csv_write,
    parse_float_list,
    parse_int_list,
    second_moment_xi_over_L,
    stderr_from_series,
)


def estimate_binder(samples: dict[str, np.ndarray]) -> float:
    m2 = np.mean(samples["m2"])
    m4 = np.mean(samples["m4"])
    if m2 <= 1e-15:
        return 0.0
    return 1.0 - m4 / (3.0 * m2 * m2)


def estimate_xi(samples: dict[str, np.ndarray], L: int) -> float:
    return second_moment_xi_over_L(np.mean(samples["s0"]), np.mean(samples["sk"]), L)


def site_action(phi: float, neighbor_sum: float, mass_like: float, lambda_like: float) -> float:
    return 0.5 * mass_like * phi * phi + 0.25 * lambda_like * phi**4 - phi * neighbor_sum


def metropolis_sweep(
    field: np.ndarray,
    neighbors: np.ndarray,
    mass_like: float,
    lambda_like: float,
    proposal_scale: float,
    rng: np.random.Generator,
) -> float:
    accepted = 0
    for site in range(field.size):
        old_value = float(field[site])
        neighbor_sum = float(np.sum(field[neighbors[site]]))
        proposal = old_value + float(rng.normal(0.0, proposal_scale))
        delta = site_action(proposal, neighbor_sum, mass_like, lambda_like) - site_action(
            old_value,
            neighbor_sum,
            mass_like,
            lambda_like,
        )
        if delta <= 0.0 or rng.random() < np.exp(-delta):
            field[site] = proposal
            accepted += 1
    return accepted / field.size


def simulate_phi4(
    L: int,
    mass_like: float,
    lambda_like: float,
    warmup: int,
    measure: int,
    seed: int,
    proposal_scale: float,
) -> dict[str, object]:
    neighbors, coords = build_cubic_geometry(L)
    volume = L**3
    rng = np.random.default_rng(seed)
    field = rng.normal(0.0, 0.1, size=volume)
    phase = np.exp(2j * np.pi * coords[:, 0] / L)

    for _ in range(warmup):
        metropolis_sweep(field, neighbors, mass_like, lambda_like, proposal_scale, rng)

    magnetization = np.empty(measure, dtype=np.float64)
    m2 = np.empty(measure, dtype=np.float64)
    m4 = np.empty(measure, dtype=np.float64)
    s0 = np.empty(measure, dtype=np.float64)
    sk = np.empty(measure, dtype=np.float64)
    acceptance = np.empty(measure, dtype=np.float64)

    for idx in range(measure):
        acceptance[idx] = metropolis_sweep(field, neighbors, mass_like, lambda_like, proposal_scale, rng)
        m = float(np.mean(field))
        mk = np.sum(field * phase) / volume
        magnetization[idx] = m
        m2[idx] = m * m
        m4[idx] = m * m * m * m
        s0[idx] = volume * m2[idx]
        sk[idx] = volume * (mk.real * mk.real + mk.imag * mk.imag)

    bootstrap_rng = np.random.default_rng(seed + 20_000)
    susceptibility_mean, susceptibility_stderr = bootstrap_estimate(
        bootstrap_rng,
        {"s0": s0},
        lambda data: float(np.mean(data["s0"])),
    )
    binder_mean, binder_stderr = bootstrap_estimate(
        bootstrap_rng,
        {"m2": m2, "m4": m4},
        estimate_binder,
    )
    xi_mean, xi_stderr = bootstrap_estimate(
        bootstrap_rng,
        {"s0": s0, "sk": sk},
        lambda data: estimate_xi(data, L),
    )
    mag_abs_mean = float(np.mean(np.abs(magnetization)))
    mag_abs_stderr, tau_mag = stderr_from_series(np.abs(magnetization))
    acceptance_stderr, _ = stderr_from_series(acceptance)

    return {
        "binder": (binder_mean, binder_stderr, tau_mag),
        "xi_over_L": (xi_mean, xi_stderr, tau_mag),
        "susceptibility": (susceptibility_mean, susceptibility_stderr, tau_mag),
        "magnetization_abs": (mag_abs_mean, mag_abs_stderr, tau_mag),
        "acceptance_rate": (float(np.mean(acceptance)), acceptance_stderr, 0.5),
    }


def build_scan_rows(
    sizes: list[int],
    mass_likes: list[float],
    lambda_likes: list[float],
    warmup: int,
    measure: int,
    seed: int,
    proposal_scale: float,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for L in sizes:
        for mass_like in mass_likes:
            for lambda_like in lambda_likes:
                coupling_id = f"m{mass_like:.3f}_lam{lambda_like:.3f}"
                results = simulate_phi4(
                    L=L,
                    mass_like=mass_like,
                    lambda_like=lambda_like,
                    warmup=warmup,
                    measure=measure,
                    seed=seed + L * 131 + int(mass_like * 100) + int(lambda_like * 1000),
                    proposal_scale=proposal_scale,
                )
                for observable, (mean, stderr, tau_int) in results.items():
                    rows.append(
                        {
                            "model": "3d_scalar_phi4_metropolis",
                            "dimension_mode": DIMENSION_MODE_INTEGER,
                            "L": L,
                            "coupling_id": coupling_id,
                            "observable": observable,
                            "mean": f"{mean:.10f}",
                            "stderr": f"{stderr:.10f}",
                            "tau_int": f"{tau_int:.10f}",
                            "seed": seed,
                            "mass_like": f"{mass_like:.6f}",
                            "lambda_like": f"{lambda_like:.6f}",
                        }
                    )
    return rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="3D scalar phi^4 integer-proxy scan.")
    parser.add_argument("--L", default="4,6", help="Comma-separated lattice sizes.")
    parser.add_argument(
        "--mass-like",
        default="6.00,8.00",
        help="Comma-separated mass-like couplings. Defaults stay on the disordered side for schema-safe scans.",
    )
    parser.add_argument(
        "--lambda-like",
        default="1.00",
        help="Comma-separated lambda-like couplings.",
    )
    parser.add_argument("--warmup", type=int, default=80, help="Warmup sweeps.")
    parser.add_argument("--measure", type=int, default=120, help="Measured sweeps.")
    parser.add_argument("--seed", type=int, default=11, help="Base RNG seed.")
    parser.add_argument("--proposal-scale", type=float, default=0.75, help="Local update proposal scale.")
    parser.add_argument(
        "--out",
        type=Path,
        default=RESULTS_DIR / "phase1_scan.csv",
        help="Output CSV path.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    rows = build_scan_rows(
        sizes=parse_int_list(args.L),
        mass_likes=parse_float_list(args.mass_like),
        lambda_likes=parse_float_list(args.lambda_like),
        warmup=args.warmup,
        measure=args.measure,
        seed=args.seed,
        proposal_scale=args.proposal_scale,
    )
    csv_write(rows, args.out)
    print(f"Wrote integer proxy scan to {args.out}")


if __name__ == "__main__":
    main()
