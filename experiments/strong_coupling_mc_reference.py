#!/usr/bin/env python3
"""
Phase 0 reference benchmark for Paper V strong-coupling work.

3D Ising at the literature critical point, updated with Wolff clusters.
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
    FRG_3D_ISING,
    LITERATURE_3D_ISING,
    RESULTS_DIR,
    block_bootstrap_estimate,
    build_cubic_geometry,
    fit_power_law,
    json_dump,
    parse_int_list,
    second_moment_xi_over_L,
    stderr_from_series,
    weighted_linear_fit,
    weighted_mean,
)


def wolff_cluster_update(
    spins: np.ndarray,
    neighbors: np.ndarray,
    beta: float,
    rng: np.random.Generator,
) -> np.ndarray:
    volume = spins.size
    seed = int(rng.integers(0, volume))
    target_spin = int(spins[seed])
    add_probability = 1.0 - np.exp(-2.0 * beta)
    marked = np.zeros(volume, dtype=bool)
    marked[seed] = True
    stack = [seed]
    cluster: list[int] = []
    while stack:
        site = stack.pop()
        cluster.append(site)
        for nb in neighbors[site]:
            if marked[nb] or spins[nb] != target_spin:
                continue
            if rng.random() < add_probability:
                marked[nb] = True
                stack.append(int(nb))
    cluster_arr = np.asarray(cluster, dtype=np.int32)
    spins[cluster_arr] *= -1
    return cluster_arr


def estimate_binder(samples: dict[str, np.ndarray]) -> float:
    m2 = np.mean(samples["m2"])
    m4 = np.mean(samples["m4"])
    if m2 <= 1e-15:
        return 0.0
    return 1.0 - m4 / (3.0 * m2 * m2)


def estimate_xi(samples: dict[str, np.ndarray], L: int) -> float:
    return second_moment_xi_over_L(np.mean(samples["s0"]), np.mean(samples["sk"]), L)


def build_beta_grid(beta_c: float, beta_window: float, beta_points: int) -> list[float]:
    if beta_points < 3 or beta_points % 2 == 0:
        raise ValueError("beta_points must be an odd integer >= 3.")
    return [float(value) for value in np.linspace(beta_c - beta_window, beta_c + beta_window, beta_points)]


def fit_beta_slope(
    beta_grid: list[float],
    values: list[float],
    errors: list[float],
    beta_c: float,
    method: str,
):
    centered_beta = [beta - beta_c for beta in beta_grid]
    return weighted_linear_fit(centered_beta, values, errors, method=method)


def fit_nu_channel(
    channel_name: str,
    beta_grid: list[float],
    series_by_size: dict[int, list[dict[str, object]]],
    observable_key: str,
    fit_sizes: list[int],
    beta_c: float,
) -> dict[str, object]:
    slopes: list[float] = []
    slope_errors: list[float] = []
    per_size: dict[str, object] = {}

    for size in fit_sizes:
        rows = series_by_size[size]
        values = [float(row[observable_key]["value"]) for row in rows]
        errors = [float(max(row[observable_key]["stderr"], 1e-6)) for row in rows]
        beta_fit = fit_beta_slope(
            beta_grid=beta_grid,
            values=values,
            errors=errors,
            beta_c=beta_c,
            method=f"{channel_name}: {observable_key}(beta) near beta_c",
        )
        slope = abs(beta_fit.slope)
        slope_stderr = max(beta_fit.stderr, 1e-6)
        slopes.append(float(slope))
        slope_errors.append(float(slope_stderr))
        per_size[str(size)] = {
            "slope": float(slope),
            "slope_stderr": float(slope_stderr),
            "intercept": float(beta_fit.intercept),
        }

    scaling_fit = fit_power_law(
        fit_sizes,
        slopes,
        slope_errors,
        method=f"{channel_name}: dO/dβ ~ L^(1/nu)",
    )
    nu_value = 1.0 / scaling_fit.slope if np.isfinite(scaling_fit.slope) and scaling_fit.slope > 0.0 else float("nan")
    nu_stderr = (
        scaling_fit.stderr / (scaling_fit.slope * scaling_fit.slope)
        if np.isfinite(scaling_fit.slope) and scaling_fit.slope > 0.0 and np.isfinite(scaling_fit.stderr)
        else float("nan")
    )
    return {
        "value": float(nu_value),
        "stderr": float(nu_stderr),
        "fit": {
            "slope": float(scaling_fit.slope),
            "slope_stderr": float(scaling_fit.stderr),
            "intercept": float(scaling_fit.intercept),
            "method": scaling_fit.method,
        },
        "per_size": per_size,
    }


def combine_nu_channels(nu_channels: dict[str, dict[str, object]]) -> tuple[float, float]:
    values: list[float] = []
    errors: list[float] = []
    for payload in nu_channels.values():
        value = float(payload["value"])
        stderr = float(payload["stderr"])
        if np.isfinite(value) and np.isfinite(stderr) and stderr > 0.0:
            values.append(value)
            errors.append(stderr)
    if not values:
        return float("nan"), float("nan")
    if len(values) == 1:
        return float(values[0]), float(errors[0])
    return weighted_mean(values, errors)


def build_pass_entry(value: float, target: float, tolerance: float) -> dict[str, object]:
    delta = abs(value - target) if np.isfinite(value) else float("nan")
    passed = bool(np.isfinite(delta) and delta < tolerance)
    return {
        "value": float(value),
        "target": float(target),
        "delta": float(delta),
        "tolerance": float(tolerance),
        "pass": passed,
    }


def simulate_ising(
    L: int,
    beta: float,
    warmup: int,
    measure: int,
    seed: int,
    block_size: int,
) -> dict[str, object]:
    neighbors, coords = build_cubic_geometry(L)
    volume = L**3
    rng = np.random.default_rng(seed)
    spins = rng.choice(np.array([-1, 1], dtype=np.int8), size=volume)
    phase = np.exp(2j * np.pi * coords[:, 0] / L)

    for _ in range(warmup):
        wolff_cluster_update(spins, neighbors, beta, rng)

    magnetization = np.empty(measure, dtype=np.float64)
    m2 = np.empty(measure, dtype=np.float64)
    m4 = np.empty(measure, dtype=np.float64)
    s0 = np.empty(measure, dtype=np.float64)
    sk = np.empty(measure, dtype=np.float64)
    cluster_sizes = np.empty(measure, dtype=np.float64)

    for idx in range(measure):
        cluster = wolff_cluster_update(spins, neighbors, beta, rng)
        cluster_sizes[idx] = float(cluster.size)
        m = float(np.sum(spins) / volume)
        mk = np.sum(spins * phase) / volume
        magnetization[idx] = m
        m2[idx] = m * m
        m4[idx] = m * m * m * m
        s0[idx] = beta * volume * m2[idx]
        sk[idx] = volume * (mk.real * mk.real + mk.imag * mk.imag)

    bootstrap_rng = np.random.default_rng(seed + 10_000)
    susceptibility_mean, susceptibility_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"s0": s0},
        lambda data: float(np.mean(data["s0"])),
        block_size=block_size,
    )
    binder_mean, binder_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"m2": m2, "m4": m4},
        estimate_binder,
        block_size=block_size,
    )
    xi_mean, xi_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"s0": s0 / beta, "sk": sk},
        lambda data: estimate_xi(data, L),
        block_size=block_size,
    )
    mag_abs_stderr, tau_mag = stderr_from_series(np.abs(magnetization))
    _, tau_cluster = stderr_from_series(cluster_sizes)

    return {
        "L": L,
        "beta": beta,
        "binder": {"value": binder_mean, "stderr": binder_stderr},
        "xi_over_L": {"value": xi_mean, "stderr": xi_stderr},
        "susceptibility": {"value": susceptibility_mean, "stderr": susceptibility_stderr},
        "tau_int": {
            "magnetization_abs": tau_mag,
            "cluster_size": tau_cluster,
        },
        "stderr": {
            "magnetization_abs": mag_abs_stderr,
            "binder": binder_stderr,
            "xi_over_L": xi_stderr,
            "susceptibility": susceptibility_stderr,
        },
    }


def build_reference_payload(
    sizes: list[int],
    warmup: int,
    measure: int,
    seed: int,
    beta_window: float,
    beta_points: int,
    block_size: int,
) -> dict[str, object]:
    beta_c = float(LITERATURE_3D_ISING["beta_c"])
    beta_grid = build_beta_grid(beta_c, beta_window, beta_points)
    series_by_size: dict[int, list[dict[str, object]]] = {}

    for size in sizes:
        rows: list[dict[str, object]] = []
        for beta_idx, beta in enumerate(beta_grid):
            rows.append(
                simulate_ising(
                    size,
                    beta,
                    warmup=warmup,
                    measure=measure,
                    seed=seed + size * 101 + beta_idx,
                    block_size=block_size,
                )
            )
        series_by_size[size] = rows

    critical_index = beta_points // 2
    critical_rows = {size: series_by_size[size][critical_index] for size in sizes}

    binder_values = [float(critical_rows[size]["binder"]["value"]) for size in sizes]
    binder_errors = [float(critical_rows[size]["binder"]["stderr"]) for size in sizes]
    binder_mean, binder_stderr = weighted_mean(binder_values, binder_errors)

    xi_values = [float(critical_rows[size]["xi_over_L"]["value"]) for size in sizes]
    xi_errors = [float(critical_rows[size]["xi_over_L"]["stderr"]) for size in sizes]
    xi_mean, xi_stderr = weighted_mean(xi_values, xi_errors)

    eta_fit_sizes = sizes
    chi_values = [float(critical_rows[size]["susceptibility"]["value"]) for size in eta_fit_sizes]
    chi_errors = [float(critical_rows[size]["susceptibility"]["stderr"]) for size in eta_fit_sizes]
    eta_fit = fit_power_law(eta_fit_sizes, chi_values, chi_errors, method="chi ~ L^(2-eta)")
    eta_value = 2.0 - eta_fit.slope if np.isfinite(eta_fit.slope) else float("nan")

    exponent_fit_sizes = sizes[-3:] if len(sizes) >= 4 else sizes

    nu_channels = {
        "binder": fit_nu_channel(
            channel_name="binder",
            beta_grid=beta_grid,
            series_by_size=series_by_size,
            observable_key="binder",
            fit_sizes=exponent_fit_sizes,
            beta_c=beta_c,
        ),
        "xi_over_L": fit_nu_channel(
            channel_name="xi_over_L",
            beta_grid=beta_grid,
            series_by_size=series_by_size,
            observable_key="xi_over_L",
            fit_sizes=exponent_fit_sizes,
            beta_c=beta_c,
        ),
    }
    nu_value, nu_stderr = combine_nu_channels(nu_channels)

    tau_mag_mean = float(np.mean([critical_rows[size]["tau_int"]["magnetization_abs"] for size in sizes]))
    tau_cluster_mean = float(np.mean([critical_rows[size]["tau_int"]["cluster_size"] for size in sizes]))

    pass_breakdown = {
        "binder": build_pass_entry(
            binder_mean,
            float(LITERATURE_3D_ISING["binder"]),
            tolerance=0.20,
        ),
        "xi_over_L": build_pass_entry(
            xi_mean,
            float(LITERATURE_3D_ISING["xi_over_L"]),
            tolerance=0.25,
        ),
        "eta": build_pass_entry(
            eta_value,
            float(LITERATURE_3D_ISING["eta"]),
            tolerance=0.20,
        ),
        "nu": build_pass_entry(
            nu_value,
            float(LITERATURE_3D_ISING["nu"]),
            tolerance=0.25,
        ),
    }

    per_size = {}
    for size in sizes:
        critical = critical_rows[size]
        per_size[str(size)] = {
            "binder": critical["binder"],
            "xi_over_L": critical["xi_over_L"],
            "susceptibility": critical["susceptibility"],
            "tau_int": critical["tau_int"],
        }

    return {
        "model": "3d_ising_wolff",
        "dimension_mode": DIMENSION_MODE_INTEGER,
        "sizes": sizes,
        "critical_point": {
            "beta": beta_c,
            "beta_window": beta_window,
            "beta_points": beta_points,
            "source": LITERATURE_3D_ISING["source"],
        },
        "binder": {"value": binder_mean, "stderr": binder_stderr, "per_size": per_size},
        "xi_over_L": {"value": xi_mean, "stderr": xi_stderr, "per_size": per_size},
        "susceptibility": {
            "value": float(np.mean([float(critical_rows[size]["susceptibility"]["value"]) for size in sizes])),
            "stderr": float(np.mean([float(critical_rows[size]["susceptibility"]["stderr"]) for size in sizes])),
            "per_size": {str(size): critical_rows[size]["susceptibility"] for size in sizes},
        },
        "eta_estimate": {
            "value": eta_value,
            "stderr": eta_fit.stderr,
            "method": eta_fit.method,
        },
        "nu_estimate": {
            "value": nu_value,
            "stderr": nu_stderr,
            "method": "inverse-variance weighted combination of dU/dβ and d(ξ/L)/dβ channels",
        },
        "stderr": {
            "binder": binder_stderr,
            "xi_over_L": xi_stderr,
            "susceptibility": float(np.mean([float(critical_rows[size]["susceptibility"]["stderr"]) for size in sizes])),
            "eta_estimate": eta_fit.stderr,
            "nu_estimate": nu_stderr,
        },
        "tau_int": {
            "magnetization_abs": tau_mag_mean,
            "cluster_size": tau_cluster_mean,
        },
        "benchmarks": {
            "literature": LITERATURE_3D_ISING,
            "frg_current": FRG_3D_ISING,
        },
        "diagnostics": {
            "beta_grid": beta_grid,
            "nu_channels": nu_channels,
            "pass_breakdown": pass_breakdown,
            "fit_ranges": {
                "eta_sizes": eta_fit_sizes,
                "nu_sizes": exponent_fit_sizes,
                "block_size": block_size,
            },
        },
        "pass": bool(all(bool(entry["pass"]) for entry in pass_breakdown.values())),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="3D Ising Wolff reference benchmark.")
    parser.add_argument("--L", default="8,10,12", help="Comma-separated lattice sizes.")
    parser.add_argument("--warmup", type=int, default=200, help="Warmup cluster updates per beta.")
    parser.add_argument("--measure", type=int, default=400, help="Measured cluster updates per beta.")
    parser.add_argument("--seed", type=int, default=7, help="Base RNG seed.")
    parser.add_argument("--beta-window", type=float, default=0.006, help="Half-width of the beta scan window.")
    parser.add_argument("--beta-points", type=int, default=5, help="Odd number of beta grid points.")
    parser.add_argument("--block-size", type=int, default=10, help="Moving block size for bootstrap estimates.")
    parser.add_argument(
        "--out",
        type=Path,
        default=RESULTS_DIR / "phase0_reference.json",
        help="Output JSON path.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    sizes = parse_int_list(args.L)
    payload = build_reference_payload(
        sizes=sizes,
        warmup=args.warmup,
        measure=args.measure,
        seed=args.seed,
        beta_window=args.beta_window,
        beta_points=args.beta_points,
        block_size=args.block_size,
    )
    json_dump(payload, args.out)
    print(f"Wrote reference benchmark to {args.out}")


if __name__ == "__main__":
    main()
