#!/usr/bin/env python3
"""
Phase 2 first-cut fractional proxy for Paper V strong-coupling work.

This script does not claim to be the final T-projected lattice. It operationalizes
the current first cut: a 3D phi^4 lattice with a rank-(n-1) transverse sector and
a small regulator coupling along the T axis, so the Monte Carlo surface can start
tracking non-integer formal n without breaking the shared benchmark schema.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from strong_coupling_common import (
    DIMENSION_MODE_FRACTIONAL,
    RESULTS_DIR,
    block_bootstrap_estimate,
    build_anisotropic_cubic_geometry,
    build_anisotropic_square_geometry,
    csv_write,
    parse_float_list,
    parse_int_list,
    second_moment_xi_over_L,
    stderr_from_series,
    t_projected_axis_weights,
)


DEFAULT_DIRECT_T_PROJECTED_SCHEDULE = {
    "3.000000": {"mass_like": 1.500000, "lambda_like": 0.500000},
    "2.900000": {"mass_like": 0.430000, "lambda_like": 0.600000},
    "2.780000": {"mass_like": 0.400000, "lambda_like": 1.000000},
    "2.700000": {"mass_like": 1.000000, "lambda_like": 0.500000},
    "2.680000": {"mass_like": 1.500000, "lambda_like": 1.000000},
}
DEFAULT_SHARED_MASS_LIKE = 6.0
DEFAULT_SHARED_LAMBDA_LIKE = 1.0
EMBEDDING_UPDATE_KERNEL = "single_hit_fixed_order_metropolis"
DIRECT_UPDATE_KERNEL = "adaptive_shuffled_multihit_metropolis"
FIXED_SITE_ORDER = "fixed"
SHUFFLED_SITE_ORDER = "shuffled"
DIRECT_METRO_HITS = 4
DIRECT_MEASURE_STRIDE = 5
ADAPTIVE_WARMUP_FRACTION = 0.8
TARGET_ACCEPTANCE_MIN = 0.45
TARGET_ACCEPTANCE_MAX = 0.60
PROPOSAL_SCALE_DECAY = 0.90
PROPOSAL_SCALE_GROWTH = 1.10
PROPOSAL_SCALE_MIN = 0.10
PROPOSAL_SCALE_MAX = 1.50


def estimate_binder(samples: dict[str, np.ndarray]) -> float:
    m2 = np.mean(samples["m2"])
    m4 = np.mean(samples["m4"])
    if m2 <= 1e-15:
        return 0.0
    return 1.0 - m4 / (3.0 * m2 * m2)


def estimate_connected_susceptibility(samples: dict[str, np.ndarray], effective_volume: float) -> float:
    magnetization = np.asarray(samples["magnetization"], dtype=np.float64)
    m_mean = float(np.mean(magnetization))
    m2_mean = float(np.mean(magnetization * magnetization))
    return max(effective_volume * (m2_mean - m_mean * m_mean), 0.0)


def estimate_connected_xi(
    samples: dict[str, np.ndarray],
    L: int,
    transverse_weight: float,
    effective_volume: float,
) -> float:
    return second_moment_xi_over_L(
        estimate_connected_susceptibility(samples, effective_volume),
        np.mean(samples["sk"]),
        L,
        axis_weight=transverse_weight,
    )


def estimate_structure_factor_kmin(samples: dict[str, np.ndarray]) -> float:
    sk = np.asarray(samples["sk"], dtype=np.float64)
    return max(float(np.mean(sk)), 0.0)


def site_action(phi: float, weighted_neighbor_sum: float, mass_like: float, lambda_like: float) -> float:
    return 0.5 * mass_like * phi * phi + 0.25 * lambda_like * phi**4 - phi * weighted_neighbor_sum


def site_visit_order(size: int, rng: np.random.Generator, site_order: str) -> np.ndarray:
    if site_order == FIXED_SITE_ORDER:
        return np.arange(size, dtype=np.int32)
    if site_order == SHUFFLED_SITE_ORDER:
        return rng.permutation(size).astype(np.int32, copy=False)
    raise ValueError(f"Unknown site_order: {site_order}")


def adapt_proposal_scale(current_scale: float, acceptance_rate: float) -> float:
    next_scale = current_scale
    if acceptance_rate < TARGET_ACCEPTANCE_MIN:
        next_scale *= PROPOSAL_SCALE_DECAY
    elif acceptance_rate > TARGET_ACCEPTANCE_MAX:
        next_scale *= PROPOSAL_SCALE_GROWTH
    return float(np.clip(next_scale, PROPOSAL_SCALE_MIN, PROPOSAL_SCALE_MAX))


def metropolis_site_hits(
    field: np.ndarray,
    neighbors: np.ndarray,
    bond_weights: np.ndarray,
    mass_like: float,
    lambda_like: float,
    proposal_scale: float,
    rng: np.random.Generator,
    site: int,
    metro_hits: int,
) -> int:
    accepted = 0
    for _ in range(metro_hits):
        old_value = float(field[site])
        weighted_neighbor_sum = float(np.sum(bond_weights[site] * field[neighbors[site]]))
        proposal = old_value + float(rng.normal(0.0, proposal_scale))
        delta = site_action(proposal, weighted_neighbor_sum, mass_like, lambda_like) - site_action(
            old_value,
            weighted_neighbor_sum,
            mass_like,
            lambda_like,
        )
        if delta <= 0.0 or rng.random() < np.exp(-delta):
            field[site] = proposal
            accepted += 1
    return accepted


def metropolis_sweep_fractional(
    field: np.ndarray,
    neighbors: np.ndarray,
    bond_weights: np.ndarray,
    mass_like: float,
    lambda_like: float,
    proposal_scale: float,
    rng: np.random.Generator,
) -> float:
    accepted = 0
    for site in range(field.size):
        old_value = float(field[site])
        weighted_neighbor_sum = float(np.sum(bond_weights[site] * field[neighbors[site]]))
        proposal = old_value + float(rng.normal(0.0, proposal_scale))
        delta = site_action(proposal, weighted_neighbor_sum, mass_like, lambda_like) - site_action(
            old_value,
            weighted_neighbor_sum,
            mass_like,
            lambda_like,
        )
        if delta <= 0.0 or rng.random() < np.exp(-delta):
            field[site] = proposal
            accepted += 1
    return accepted / field.size


def adaptive_shuffled_multihit_metropolis(
    field: np.ndarray,
    neighbors: np.ndarray,
    bond_weights: np.ndarray,
    mass_like: float,
    lambda_like: float,
    proposal_scale: float,
    rng: np.random.Generator,
    metro_hits: int = DIRECT_METRO_HITS,
    site_order: str = SHUFFLED_SITE_ORDER,
) -> float:
    accepted = 0
    order = site_visit_order(field.size, rng, site_order)
    for site in order:
        accepted += metropolis_site_hits(
            field=field,
            neighbors=neighbors,
            bond_weights=bond_weights,
            mass_like=mass_like,
            lambda_like=lambda_like,
            proposal_scale=proposal_scale,
            rng=rng,
            site=int(site),
            metro_hits=metro_hits,
        )
    return accepted / float(field.size * metro_hits)


def split_connected_susceptibility(
    magnetization: np.ndarray,
    observable_volume: float,
    block_size: int,
    seed: int,
) -> dict[str, float | bool]:
    arr = np.asarray(magnetization, dtype=np.float64)
    if arr.size < 4:
        return {
            "first_mean": float("nan"),
            "first_stderr": float("nan"),
            "second_mean": float("nan"),
            "second_stderr": float("nan"),
            "pass": False,
        }

    half = arr.size // 2
    first = arr[:half]
    second = arr[half:]
    bootstrap_rng = np.random.default_rng(seed)

    first_mean, first_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"magnetization": first},
        lambda data: estimate_connected_susceptibility(data, observable_volume),
        block_size=min(block_size, max(first.size // 2, 2)),
    )
    second_mean, second_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"magnetization": second},
        lambda data: estimate_connected_susceptibility(data, observable_volume),
        block_size=min(block_size, max(second.size // 2, 2)),
    )
    combined_stderr = float(np.sqrt(first_stderr * first_stderr + second_stderr * second_stderr))
    split_pass = bool(np.isfinite(first_mean) and np.isfinite(second_mean) and abs(first_mean - second_mean) <= 3.0 * combined_stderr)
    return {
        "first_mean": float(first_mean),
        "first_stderr": float(first_stderr),
        "second_mean": float(second_mean),
        "second_stderr": float(second_stderr),
        "pass": split_pass,
    }


def simulate_fractional_proxy(
    L: int,
    formal_n: float,
    mass_like: float,
    lambda_like: float,
    warmup: int,
    measure: int,
    seed: int,
    proposal_scale: float,
    block_size: int,
    t_regulator: float,
) -> tuple[dict[str, object], dict[str, float], dict[str, object]]:
    projection = t_projected_axis_weights(formal_n, t_regulator=t_regulator)
    axis_weights = np.array(
        [
            projection["transverse_weight"],
            projection["transverse_weight"],
            projection["t_axis_weight"],
        ],
        dtype=np.float64,
    )
    neighbors, coords, bond_weights = build_anisotropic_cubic_geometry(L, axis_weights)
    volume = L**3
    rng = np.random.default_rng(seed)
    field = rng.normal(0.0, 0.1, size=volume)
    phase_x = np.exp(2j * np.pi * coords[:, 0] / L)
    phase_y = np.exp(2j * np.pi * coords[:, 1] / L)

    for _ in range(warmup):
        metropolis_sweep_fractional(
            field,
            neighbors,
            bond_weights,
            mass_like,
            lambda_like,
            proposal_scale,
            rng,
        )

    magnetization = np.empty(measure, dtype=np.float64)
    m2 = np.empty(measure, dtype=np.float64)
    m4 = np.empty(measure, dtype=np.float64)
    s0 = np.empty(measure, dtype=np.float64)
    sk = np.empty(measure, dtype=np.float64)
    acceptance = np.empty(measure, dtype=np.float64)

    for idx in range(measure):
        acceptance[idx] = metropolis_sweep_fractional(
            field,
            neighbors,
            bond_weights,
            mass_like,
            lambda_like,
            proposal_scale,
            rng,
        )
        m = float(np.mean(field))
        mk_x = np.sum(field * phase_x) / volume
        mk_y = np.sum(field * phase_y) / volume
        magnetization[idx] = m
        m2[idx] = m * m
        m4[idx] = m * m * m * m
        s0[idx] = volume * m2[idx]
        sk[idx] = 0.5 * volume * (
            mk_x.real * mk_x.real
            + mk_x.imag * mk_x.imag
            + mk_y.real * mk_y.real
            + mk_y.imag * mk_y.imag
        )

    bootstrap_rng = np.random.default_rng(seed + 30_000)
    susceptibility_mean, susceptibility_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"magnetization": magnetization},
        lambda data: estimate_connected_susceptibility(data, volume),
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
        {"magnetization": magnetization, "sk": sk},
        lambda data: estimate_connected_xi(data, L, projection["transverse_weight"], volume),
        block_size=block_size,
    )
    structure_mean, structure_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"sk": sk},
        estimate_structure_factor_kmin,
        block_size=block_size,
    )
    split_stability = split_connected_susceptibility(
        magnetization=magnetization,
        observable_volume=volume,
        block_size=block_size,
        seed=seed + 35_000,
    )
    mag_abs_mean = float(np.mean(np.abs(magnetization)))
    mag_abs_stderr, tau_mag = stderr_from_series(np.abs(magnetization))
    acceptance_stderr, _ = stderr_from_series(acceptance)

    return (
        {
            "binder": (binder_mean, binder_stderr, tau_mag),
            "xi_over_L": (xi_mean, xi_stderr, tau_mag),
            "susceptibility": (susceptibility_mean, susceptibility_stderr, tau_mag),
            "structure_factor_kmin": (structure_mean, structure_stderr, tau_mag),
            "magnetization_abs": (mag_abs_mean, mag_abs_stderr, tau_mag),
            "acceptance_rate": (float(np.mean(acceptance)), acceptance_stderr, 0.5),
        },
        projection,
        {
            "update_kernel": EMBEDDING_UPDATE_KERNEL,
            "proposal_scale_final": float(proposal_scale),
            "metro_hits": 1,
            "measure_stride": 1,
            "site_order": FIXED_SITE_ORDER,
            "split_stability_pass": bool(split_stability["pass"]),
            "split_susceptibility_first": float(split_stability["first_mean"]),
            "split_susceptibility_first_stderr": float(split_stability["first_stderr"]),
            "split_susceptibility_second": float(split_stability["second_mean"]),
            "split_susceptibility_second_stderr": float(split_stability["second_stderr"]),
            "acceptance_mean": float(np.mean(acceptance)),
        },
    )


def simulate_direct_t_projected_proxy(
    L: int,
    formal_n: float,
    mass_like: float,
    lambda_like: float,
    warmup: int,
    measure: int,
    seed: int,
    proposal_scale: float,
    block_size: int,
    metro_hits: int = DIRECT_METRO_HITS,
    measure_stride: int = DIRECT_MEASURE_STRIDE,
    site_order: str = SHUFFLED_SITE_ORDER,
) -> tuple[dict[str, object], dict[str, float], dict[str, object]]:
    projection = t_projected_axis_weights(formal_n, t_regulator=0.0 + 1e-6)
    transverse_weight = projection["transverse_weight"]
    neighbors, coords, bond_weights = build_anisotropic_square_geometry(L, [transverse_weight, transverse_weight])
    area = L**2
    observable_volume = float(area)
    rng = np.random.default_rng(seed)
    field = rng.normal(0.0, 0.1, size=area)
    phase_x = np.exp(2j * np.pi * coords[:, 0] / L)
    phase_y = np.exp(2j * np.pi * coords[:, 1] / L)

    adaptive_sweeps = int(np.floor(max(warmup, 0) * ADAPTIVE_WARMUP_FRACTION))
    current_proposal_scale = float(proposal_scale)
    for warmup_idx in range(warmup):
        acceptance_rate = adaptive_shuffled_multihit_metropolis(
            field=field,
            neighbors=neighbors,
            bond_weights=bond_weights,
            mass_like=mass_like,
            lambda_like=lambda_like,
            proposal_scale=current_proposal_scale,
            rng=rng,
            metro_hits=metro_hits,
            site_order=site_order,
        )
        if warmup_idx < adaptive_sweeps:
            current_proposal_scale = adapt_proposal_scale(current_proposal_scale, acceptance_rate)

    magnetization = np.empty(measure, dtype=np.float64)
    m2 = np.empty(measure, dtype=np.float64)
    m4 = np.empty(measure, dtype=np.float64)
    s0 = np.empty(measure, dtype=np.float64)
    sk = np.empty(measure, dtype=np.float64)
    acceptance = np.empty(measure, dtype=np.float64)

    for idx in range(measure):
        macro_acceptance = 0.0
        for _ in range(measure_stride):
            macro_acceptance += adaptive_shuffled_multihit_metropolis(
                field=field,
                neighbors=neighbors,
                bond_weights=bond_weights,
                mass_like=mass_like,
                lambda_like=lambda_like,
                proposal_scale=current_proposal_scale,
                rng=rng,
                metro_hits=metro_hits,
                site_order=site_order,
            )
        acceptance[idx] = macro_acceptance / measure_stride
        m = float(np.mean(field))
        mk_x = np.sum(field * phase_x) / area
        mk_y = np.sum(field * phase_y) / area
        magnetization[idx] = m
        m2[idx] = m * m
        m4[idx] = m * m * m * m
        s0[idx] = observable_volume * m2[idx]
        sk[idx] = 0.5 * observable_volume * (
            mk_x.real * mk_x.real
            + mk_x.imag * mk_x.imag
            + mk_y.real * mk_y.real
            + mk_y.imag * mk_y.imag
        )

    bootstrap_rng = np.random.default_rng(seed + 40_000)
    susceptibility_mean, susceptibility_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"magnetization": magnetization},
        lambda data: estimate_connected_susceptibility(data, observable_volume),
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
        {"magnetization": magnetization, "sk": sk},
        lambda data: estimate_connected_xi(data, L, transverse_weight, observable_volume),
        block_size=block_size,
    )
    structure_mean, structure_stderr = block_bootstrap_estimate(
        bootstrap_rng,
        {"sk": sk},
        estimate_structure_factor_kmin,
        block_size=block_size,
    )
    split_stability = split_connected_susceptibility(
        magnetization=magnetization,
        observable_volume=observable_volume,
        block_size=block_size,
        seed=seed + 45_000,
    )
    mag_abs_mean = float(np.mean(np.abs(magnetization)))
    mag_abs_stderr, tau_mag = stderr_from_series(np.abs(magnetization))
    acceptance_stderr, _ = stderr_from_series(acceptance)
    projection["t_axis_weight"] = 0.0
    projection["projection_ratio"] = 0.0

    return (
        {
            "binder": (binder_mean, binder_stderr, tau_mag),
            "xi_over_L": (xi_mean, xi_stderr, tau_mag),
            "susceptibility": (susceptibility_mean, susceptibility_stderr, tau_mag),
            "structure_factor_kmin": (structure_mean, structure_stderr, tau_mag),
            "magnetization_abs": (mag_abs_mean, mag_abs_stderr, tau_mag),
            "acceptance_rate": (float(np.mean(acceptance)), acceptance_stderr, 0.5),
        },
        projection,
        {
            "update_kernel": DIRECT_UPDATE_KERNEL,
            "proposal_scale_final": float(current_proposal_scale),
            "metro_hits": int(metro_hits),
            "measure_stride": int(measure_stride),
            "site_order": site_order,
            "split_stability_pass": bool(split_stability["pass"]),
            "split_susceptibility_first": float(split_stability["first_mean"]),
            "split_susceptibility_first_stderr": float(split_stability["first_stderr"]),
            "split_susceptibility_second": float(split_stability["second_mean"]),
            "split_susceptibility_second_stderr": float(split_stability["second_stderr"]),
            "acceptance_mean": float(np.mean(acceptance)),
        },
    )


def normalize_schedule_entries(payload: object) -> list[dict[str, float]]:
    raw_entries = payload if isinstance(payload, list) else [payload]
    entries: list[dict[str, float]] = []
    for raw_entry in raw_entries:
        if not isinstance(raw_entry, dict):
            raise ValueError("Each schedule row must be a dict with mass_like/lambda_like.")
        if "mass_like" not in raw_entry or "lambda_like" not in raw_entry:
            raise ValueError("Each schedule row must contain mass_like and lambda_like.")
        entries.append(
            {
                "mass_like": float(raw_entry["mass_like"]),
                "lambda_like": float(raw_entry["lambda_like"]),
            }
        )
    return entries


def load_schedule_map(schedule_path: Path) -> dict[str, list[dict[str, float]]]:
    payload = json.loads(schedule_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("schedule JSON must be a dict keyed by formal_n.")
    schedule: dict[str, list[dict[str, float]]] = {}
    for key, value in payload.items():
        schedule[f"{float(key):.6f}"] = normalize_schedule_entries(value)
    return schedule


def resolve_schedule_entries(
    formal_ns: list[float],
    mass_likes: list[float],
    lambda_likes: list[float],
    proxy_kind: str,
    schedule_mode: str,
    schedule_path: Path | None,
) -> list[tuple[float, float, float]]:
    effective_schedule_mode = schedule_mode
    if effective_schedule_mode == "auto":
        use_default_grid = (
            len(mass_likes) == 1
            and len(lambda_likes) == 1
            and abs(mass_likes[0] - DEFAULT_SHARED_MASS_LIKE) <= 1e-9
            and abs(lambda_likes[0] - DEFAULT_SHARED_LAMBDA_LIKE) <= 1e-9
        )
        effective_schedule_mode = "per_n" if proxy_kind == "t_projected_direct" and (schedule_path is not None or use_default_grid) else "shared"
    if effective_schedule_mode == "shared":
        return [
            (formal_n, mass_like, lambda_like)
            for formal_n in formal_ns
            for mass_like in mass_likes
            for lambda_like in lambda_likes
        ]

    if schedule_path is not None:
        schedule_map = load_schedule_map(schedule_path)
    elif proxy_kind == "t_projected_direct":
        schedule_map = {
            key: normalize_schedule_entries(value)
            for key, value in DEFAULT_DIRECT_T_PROJECTED_SCHEDULE.items()
        }
    else:
        raise ValueError("per_n schedule without --schedule-path is only supported for t_projected_direct.")

    entries: list[tuple[float, float, float]] = []
    missing: list[str] = []
    for formal_n in formal_ns:
        key = f"{formal_n:.6f}"
        payloads = schedule_map.get(key)
        if payloads is None:
            missing.append(key)
            continue
        for payload in payloads:
            entries.append((formal_n, float(payload["mass_like"]), float(payload["lambda_like"])))
    if missing:
        raise ValueError(f"Missing per_n schedule rows for formal_n={missing}")
    return entries


def build_scan_rows(
    sizes: list[int],
    formal_ns: list[float],
    mass_likes: list[float],
    lambda_likes: list[float],
    warmup: int,
    measure: int,
    seed: int,
    proposal_scale: float,
    block_size: int,
    t_regulator: float,
    proxy_kind: str,
    schedule_mode: str,
    schedule_path: Path | None,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    schedule_entries = resolve_schedule_entries(
        formal_ns=formal_ns,
        mass_likes=mass_likes,
        lambda_likes=lambda_likes,
        proxy_kind=proxy_kind,
        schedule_mode=schedule_mode,
        schedule_path=schedule_path,
    )
    effective_schedule_mode = schedule_mode
    if effective_schedule_mode == "auto":
        use_default_grid = (
            len(mass_likes) == 1
            and len(lambda_likes) == 1
            and abs(mass_likes[0] - DEFAULT_SHARED_MASS_LIKE) <= 1e-9
            and abs(lambda_likes[0] - DEFAULT_SHARED_LAMBDA_LIKE) <= 1e-9
        )
        effective_schedule_mode = "per_n" if proxy_kind == "t_projected_direct" and (schedule_path is not None or use_default_grid) else "shared"
    schedule_source = "path" if schedule_path is not None else ("built_in_direct_v1" if effective_schedule_mode == "per_n" else "explicit_grid")

    for formal_n, mass_like, lambda_like in schedule_entries:
        coupling_id = f"n{formal_n:.2f}_m{mass_like:.3f}_lam{lambda_like:.3f}"
        for L in sizes:
            run_seed = (
                seed
                + L * 131
                + int(formal_n * 1000)
                + int(mass_like * 100)
                + int(lambda_like * 1000)
            )
            if proxy_kind == "t_projected_direct":
                results, projection, run_metadata = simulate_direct_t_projected_proxy(
                    L=L,
                    formal_n=formal_n,
                    mass_like=mass_like,
                    lambda_like=lambda_like,
                    warmup=warmup,
                    measure=measure,
                    seed=run_seed,
                    proposal_scale=proposal_scale,
                    block_size=block_size,
                )
                model = "t_projected_direct_phi4_metropolis"
            else:
                results, projection, run_metadata = simulate_fractional_proxy(
                    L=L,
                    formal_n=formal_n,
                    mass_like=mass_like,
                    lambda_like=lambda_like,
                    warmup=warmup,
                    measure=measure,
                    seed=run_seed,
                    proposal_scale=proposal_scale,
                    block_size=block_size,
                    t_regulator=t_regulator,
                )
                model = "t_projected_fractional_phi4_metropolis"
            for observable, (mean, stderr, tau_int) in results.items():
                rows.append(
                    {
                        "model": model,
                        "dimension_mode": DIMENSION_MODE_FRACTIONAL,
                        "L": L,
                        "coupling_id": coupling_id,
                        "observable": observable,
                        "mean": f"{mean:.10f}",
                        "stderr": f"{stderr:.10f}",
                        "tau_int": f"{tau_int:.10f}",
                        "seed": run_seed,
                        "formal_n": f"{projection['formal_n']:.6f}",
                        "n_eff": f"{projection['n_eff']:.6f}",
                        "transverse_weight": f"{projection['transverse_weight']:.6f}",
                        "t_axis_weight": f"{projection['t_axis_weight']:.6f}",
                        "projection_ratio": f"{projection['projection_ratio']:.6f}",
                        "proxy_kind": proxy_kind,
                        "mass_like": f"{mass_like:.6f}",
                        "lambda_like": f"{lambda_like:.6f}",
                        "schedule_mode": effective_schedule_mode,
                        "schedule_source": schedule_source,
                        "update_kernel": str(run_metadata["update_kernel"]),
                        "proposal_scale_final": f"{float(run_metadata['proposal_scale_final']):.6f}",
                        "metro_hits": int(run_metadata["metro_hits"]),
                        "measure_stride": int(run_metadata["measure_stride"]),
                        "site_order": str(run_metadata["site_order"]),
                    }
                )
    return rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="T-projected fractional first-cut proxy scan.")
    parser.add_argument("--L", default="4,6", help="Comma-separated lattice sizes.")
    parser.add_argument(
        "--formal-n",
        default="3.0,2.9,2.78,2.7,2.68",
        help="Comma-separated formal n values. The current proxy supports 2.0 <= n <= 3.0.",
    )
    parser.add_argument(
        "--mass-like",
        default="6.00",
        help="Comma-separated mass-like couplings for the first-cut fractional proxy.",
    )
    parser.add_argument(
        "--lambda-like",
        default="1.00",
        help="Comma-separated lambda-like couplings.",
    )
    parser.add_argument("--warmup", type=int, default=80, help="Warmup sweeps.")
    parser.add_argument("--measure", type=int, default=120, help="Measured sweeps.")
    parser.add_argument("--seed", type=int, default=41, help="Base RNG seed.")
    parser.add_argument("--proposal-scale", type=float, default=0.65, help="Local update proposal scale.")
    parser.add_argument("--block-size", type=int, default=8, help="Block size for bootstrap error bars.")
    parser.add_argument(
        "--proxy-kind",
        choices=["t_projected_fractional_embedding", "t_projected_direct"],
        default="t_projected_direct",
        help="Fractional proxy family. The direct quotient lattice is now the default.",
    )
    parser.add_argument(
        "--t-regulator",
        type=float,
        default=0.05,
        help="Residual T-axis coupling for the embedding proxy. Ignored by t_projected_direct.",
    )
    parser.add_argument(
        "--schedule-mode",
        choices=["auto", "shared", "per_n"],
        default="auto",
        help="Coupling assignment mode. auto => direct uses per_n, embedding uses shared grid.",
    )
    parser.add_argument(
        "--schedule-path",
        type=Path,
        default=None,
        help="Optional JSON file mapping formal_n to {mass_like, lambda_like}. Used only for per_n schedules.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=RESULTS_DIR / "phase2_fractional_scan.csv",
        help="Output CSV path.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    rows = build_scan_rows(
        sizes=parse_int_list(args.L),
        formal_ns=parse_float_list(args.formal_n),
        mass_likes=parse_float_list(args.mass_like),
        lambda_likes=parse_float_list(args.lambda_like),
        warmup=args.warmup,
        measure=args.measure,
        seed=args.seed,
        proposal_scale=args.proposal_scale,
        block_size=args.block_size,
        t_regulator=args.t_regulator,
        proxy_kind=args.proxy_kind,
        schedule_mode=args.schedule_mode,
        schedule_path=args.schedule_path,
    )
    csv_write(rows, args.out)
    print(f"Wrote fractional proxy scan to {args.out}")


if __name__ == "__main__":
    main()
