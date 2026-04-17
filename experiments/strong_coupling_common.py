#!/usr/bin/env python3
"""
Strong-coupling benchmark helpers for Paper V §6.8.4.

This module centralizes small numerical utilities so the three CLI entrypoints
share one schema and one set of estimators.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np

RESULTS_DIR = Path(__file__).resolve().parent / "results_strong_coupling"
DIMENSION_MODE_INTEGER = "integer_proxy"
DIMENSION_MODE_FRACTIONAL = "fractional_proxy"

LITERATURE_3D_ISING = {
    "beta_c": 0.2216544,
    "eta": 0.0363,
    "nu": 0.6300,
    "binder": 0.4656,
    "xi_over_L": 0.6431,
    "source": "3D Ising literature reference",
}

FRG_3D_ISING = {
    "eta": 0.0360,
    "nu": 0.6440,
    "source": "Paper V §5.5.9 DE2 3D Ising benchmark",
}

TARGET_GAMMA_PAPER_IV = 0.86

FRG_T_PROJECTED_ANCHORS = {
    "lpa_t": [
        {"formal_n": 3.50, "eta": 0.004, "gamma_phi": 0.109},
        {"formal_n": 3.00, "eta": 0.013, "gamma_phi": 0.298},
        {"formal_n": 2.90, "eta": 0.015, "gamma_phi": 0.353},
        {"formal_n": 2.80, "eta": 0.015, "gamma_phi": 0.414},
        {"formal_n": 2.78, "eta": 0.016, "gamma_phi": 0.427},
        {"formal_n": 2.70, "eta": 0.016, "gamma_phi": 0.468},
        {"formal_n": 2.66, "eta": 0.016, "gamma_phi": 0.478},
    ],
    "de2_t": [
        {"formal_n": 3.00, "eta": 0.019, "gamma_phi": 0.294},
        {"formal_n": 2.80, "eta": 0.031, "gamma_phi": 0.440},
        {"formal_n": 2.78, "eta": 0.032, "gamma_phi": 0.462},
        {"formal_n": 2.72, "eta": 0.036, "gamma_phi": 0.555},
        {"formal_n": 2.68, "eta": 0.038, "gamma_phi": 0.651},
    ],
}


@dataclass
class FitResult:
    value: float
    stderr: float
    slope: float
    intercept: float
    method: str


@dataclass
class GammaReductionResult:
    formal_n: float
    eta_proxy: float
    eta_anchor: float
    gamma_anchor: float
    gamma_proxy: float
    target_ratio: float
    status: str
    method: str


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def parse_int_list(raw: str) -> list[int]:
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def parse_float_list(raw: str) -> list[float]:
    return [float(item.strip()) for item in raw.split(",") if item.strip()]


def json_dump(data: dict, out_path: Path) -> None:
    ensure_parent(out_path)
    out_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def csv_write(rows: list[dict[str, object]], out_path: Path) -> None:
    ensure_parent(out_path)
    if not rows:
        raise ValueError("CSV rows must not be empty.")
    fieldnames = list(rows[0].keys())
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_anisotropic_cubic_geometry(L: int, axis_weights: list[float] | np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    volume = L**3
    axis_weights_arr = np.asarray(axis_weights, dtype=np.float64)
    if axis_weights_arr.shape != (3,):
        raise ValueError("axis_weights must contain exactly 3 entries.")
    coords = np.indices((L, L, L), dtype=np.int32).reshape(3, -1).T
    neighbors = np.empty((volume, 6), dtype=np.int32)
    bond_weights = np.empty((volume, 6), dtype=np.float64)
    for idx, (x, y, z) in enumerate(coords):
        neighbors[idx] = [
            ((x + 1) % L) * L * L + y * L + z,
            ((x - 1) % L) * L * L + y * L + z,
            x * L * L + ((y + 1) % L) * L + z,
            x * L * L + ((y - 1) % L) * L + z,
            x * L * L + y * L + ((z + 1) % L),
            x * L * L + y * L + ((z - 1) % L),
        ]
        bond_weights[idx] = [
            axis_weights_arr[0],
            axis_weights_arr[0],
            axis_weights_arr[1],
            axis_weights_arr[1],
            axis_weights_arr[2],
            axis_weights_arr[2],
        ]
    return neighbors, coords, bond_weights


def build_cubic_geometry(L: int) -> tuple[np.ndarray, np.ndarray]:
    neighbors, coords, _ = build_anisotropic_cubic_geometry(L, [1.0, 1.0, 1.0])
    return neighbors, coords


def build_anisotropic_square_geometry(L: int, axis_weights: list[float] | np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    area = L**2
    axis_weights_arr = np.asarray(axis_weights, dtype=np.float64)
    if axis_weights_arr.shape != (2,):
        raise ValueError("axis_weights must contain exactly 2 entries for square geometry.")
    coords = np.indices((L, L), dtype=np.int32).reshape(2, -1).T
    neighbors = np.empty((area, 4), dtype=np.int32)
    bond_weights = np.empty((area, 4), dtype=np.float64)
    for idx, (x, y) in enumerate(coords):
        neighbors[idx] = [
            ((x + 1) % L) * L + y,
            ((x - 1) % L) * L + y,
            x * L + ((y + 1) % L),
            x * L + ((y - 1) % L),
        ]
        bond_weights[idx] = [
            axis_weights_arr[0],
            axis_weights_arr[0],
            axis_weights_arr[1],
            axis_weights_arr[1],
        ]
    return neighbors, coords, bond_weights


def second_moment_xi_over_L(s0_mean: float, sk_mean: float, L: int, axis_weight: float = 1.0) -> float:
    if not np.isfinite(s0_mean) or not np.isfinite(sk_mean):
        return float("nan")
    if sk_mean <= 0.0 or s0_mean <= sk_mean or axis_weight <= 0.0:
        return 0.0
    prefactor = 1.0 / (2.0 * np.sin(np.pi / L) * np.sqrt(axis_weight))
    xi = prefactor * np.sqrt((s0_mean / sk_mean) - 1.0)
    return float(xi / L)


def t_projected_axis_weights(formal_n: float, t_regulator: float = 0.05) -> dict[str, float]:
    if not (2.0 <= formal_n <= 3.0):
        raise ValueError("formal_n must stay inside [2.0, 3.0] for the current 3D embedding.")
    if t_regulator <= 0.0 or t_regulator >= 1.0:
        raise ValueError("t_regulator must stay inside (0, 1).")
    n_eff = formal_n - 1.0
    transverse_weight = max(n_eff / 2.0, 1e-6)
    return {
        "formal_n": float(formal_n),
        "n_eff": float(n_eff),
        "transverse_weight": float(transverse_weight),
        "t_axis_weight": float(t_regulator),
        "projection_ratio": float(t_regulator / transverse_weight),
    }


def autocorrelation_time(series: np.ndarray, max_lag: int | None = None) -> float:
    arr = np.asarray(series, dtype=np.float64)
    if arr.size < 4:
        return 0.5
    arr = arr - arr.mean()
    variance = np.var(arr)
    if variance <= 1e-15:
        return 0.5
    if max_lag is None:
        max_lag = min(arr.size // 2, 100)
    tau = 0.5
    for lag in range(1, max_lag + 1):
        cov = np.dot(arr[:-lag], arr[lag:]) / (arr.size - lag)
        rho = cov / variance
        if rho <= 0.0:
            break
        tau += rho
    return float(max(tau, 0.5))


def stderr_from_series(series: np.ndarray) -> tuple[float, float]:
    arr = np.asarray(series, dtype=np.float64)
    if arr.size == 0:
        return float("nan"), float("nan")
    tau = autocorrelation_time(arr)
    variance = np.var(arr, ddof=1) if arr.size > 1 else 0.0
    stderr = np.sqrt(2.0 * tau * variance / arr.size) if arr.size > 1 else 0.0
    return float(stderr), float(tau)


def bootstrap_estimate(
    rng: np.random.Generator,
    arrays: dict[str, np.ndarray],
    estimator: Callable[[dict[str, np.ndarray]], float],
    n_boot: int = 200,
) -> tuple[float, float]:
    keys = list(arrays.keys())
    size = len(arrays[keys[0]])
    estimate = estimator(arrays)
    if size < 4:
        return float(estimate), 0.0
    boot = np.empty(n_boot, dtype=np.float64)
    for i in range(n_boot):
        idx = rng.integers(0, size, size=size)
        resampled = {key: value[idx] for key, value in arrays.items()}
        boot[i] = estimator(resampled)
    return float(estimate), float(np.std(boot, ddof=1))


def block_bootstrap_estimate(
    rng: np.random.Generator,
    arrays: dict[str, np.ndarray],
    estimator: Callable[[dict[str, np.ndarray]], float],
    block_size: int,
    n_boot: int = 200,
) -> tuple[float, float]:
    keys = list(arrays.keys())
    size = len(arrays[keys[0]])
    estimate = estimator(arrays)
    if size < 4 or block_size <= 1:
        return bootstrap_estimate(rng, arrays, estimator, n_boot=n_boot)
    n_blocks = int(np.ceil(size / block_size))
    boot = np.empty(n_boot, dtype=np.float64)
    for i in range(n_boot):
        idx = np.empty(n_blocks * block_size, dtype=np.int32)
        for block_idx in range(n_blocks):
            start = int(rng.integers(0, size))
            offset = block_idx * block_size
            idx[offset : offset + block_size] = (start + np.arange(block_size, dtype=np.int32)) % size
        idx = idx[:size]
        resampled = {key: value[idx] for key, value in arrays.items()}
        boot[i] = estimator(resampled)
    return float(estimate), float(np.std(boot, ddof=1))


def weighted_mean(values: list[float], stderrs: list[float]) -> tuple[float, float]:
    vals = np.asarray(values, dtype=np.float64)
    errs = np.asarray(stderrs, dtype=np.float64)
    safe_errs = np.where(errs <= 1e-12, 1e-12, errs)
    weights = 1.0 / np.square(safe_errs)
    mean = float(np.sum(vals * weights) / np.sum(weights))
    stderr = float(np.sqrt(1.0 / np.sum(weights)))
    return mean, stderr


def fit_power_law(
    xs: list[float],
    ys: list[float],
    yerrs: list[float],
    method: str,
) -> FitResult:
    x = np.asarray(xs, dtype=np.float64)
    y = np.asarray(ys, dtype=np.float64)
    err = np.asarray(yerrs, dtype=np.float64)
    if x.size < 2 or np.any(x <= 0.0) or np.any(y <= 0.0):
        return FitResult(float("nan"), float("nan"), float("nan"), float("nan"), method)
    logx = np.log(x)
    logy = np.log(y)
    logy_err = np.where(err > 0.0, err / y, np.full_like(y, 1e-6))
    weights = 1.0 / np.square(logy_err)
    X = np.column_stack([np.ones_like(logx), logx])
    XT_W = X.T * weights
    cov = np.linalg.inv(XT_W @ X)
    beta = cov @ (XT_W @ logy)
    stderr = float(np.sqrt(max(cov[1, 1], 0.0)))
    slope = float(beta[1])
    intercept = float(beta[0])
    return FitResult(
        value=slope,
        stderr=stderr,
        slope=slope,
        intercept=intercept,
        method=method,
    )


def weighted_linear_fit(
    xs: list[float],
    ys: list[float],
    yerrs: list[float],
    method: str,
) -> FitResult:
    x = np.asarray(xs, dtype=np.float64)
    y = np.asarray(ys, dtype=np.float64)
    err = np.asarray(yerrs, dtype=np.float64)
    if x.size < 2 or not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        return FitResult(float("nan"), float("nan"), float("nan"), float("nan"), method)
    safe_err = np.where(np.isfinite(err) & (err > 0.0), err, 1e-6)
    weights = 1.0 / np.square(safe_err)
    centered_x = x - np.mean(x)
    X = np.column_stack([np.ones_like(centered_x), centered_x])
    XT_W = X.T * weights
    try:
        cov = np.linalg.inv(XT_W @ X)
    except np.linalg.LinAlgError:
        return FitResult(float("nan"), float("nan"), float("nan"), float("nan"), method)
    beta = cov @ (XT_W @ y)
    intercept = float(beta[0] - beta[1] * np.mean(x))
    slope = float(beta[1])
    slope_stderr = float(np.sqrt(max(cov[1, 1], 0.0)))
    return FitResult(
        value=slope,
        stderr=slope_stderr,
        slope=slope,
        intercept=intercept,
        method=method,
    )


def required_scan_columns() -> list[str]:
    return [
        "model",
        "dimension_mode",
        "L",
        "coupling_id",
        "observable",
        "mean",
        "stderr",
        "tau_int",
        "seed",
    ]


def validate_scan_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        missing = [col for col in required_scan_columns() if col not in (reader.fieldnames or [])]
    return rows, missing


def as_float(value: object) -> float:
    return float(value) if value is not None else float("nan")


def scan_sanity_issues(rows: list[dict[str, str]]) -> list[str]:
    issues: list[str] = []
    for row in rows:
        observable = row.get("observable", "")
        label = f"L={row.get('L', '?')} coupling={row.get('coupling_id', '?')} observable={observable}"
        mean = as_float(row.get("mean"))
        stderr = as_float(row.get("stderr"))
        tau_int = as_float(row.get("tau_int"))

        if not np.isfinite(mean):
            issues.append(f"{label}: mean is not finite")
            continue
        if not np.isfinite(stderr) or stderr < 0.0:
            issues.append(f"{label}: stderr is not finite and non-negative")
        if not np.isfinite(tau_int) or tau_int < 0.0:
            issues.append(f"{label}: tau_int is not finite and non-negative")

        if observable == "binder" and not (-0.25 <= mean <= 0.75):
            issues.append(f"{label}: binder left the expected finite-size range [-0.25, 0.75]")
        elif observable == "xi_over_L" and not (0.0 <= mean <= 1.0):
            issues.append(f"{label}: xi_over_L left the expected range [0, 1]")
        elif observable in {"susceptibility", "magnetization_abs"} and mean < 0.0:
            issues.append(f"{label}: {observable} must stay non-negative")
        elif observable == "acceptance_rate" and not (0.0 <= mean <= 1.0):
            issues.append(f"{label}: acceptance_rate must stay inside [0, 1]")
    return issues


def _interpolate_anchor_rows(rows: list[dict[str, float]], formal_n: float, key: str) -> float:
    if len(rows) < 2:
        raise ValueError("Need at least two anchor rows to interpolate.")
    sorted_rows = sorted(rows, key=lambda row: row["formal_n"])
    if formal_n <= sorted_rows[0]["formal_n"]:
        return float(sorted_rows[0][key])
    if formal_n >= sorted_rows[-1]["formal_n"]:
        return float(sorted_rows[-1][key])
    for low, high in zip(sorted_rows, sorted_rows[1:]):
        if low["formal_n"] <= formal_n <= high["formal_n"]:
            span = high["formal_n"] - low["formal_n"]
            if span <= 0.0:
                return float(low[key])
            weight = (formal_n - low["formal_n"]) / span
            return float(low[key] + weight * (high[key] - low[key]))
    return float(sorted_rows[-1][key])


def gamma_phi_reduction_from_eta(
    formal_n: float,
    eta_proxy: float,
    method: str,
    eta_band_factor: float = 2.0,
) -> GammaReductionResult:
    if method not in FRG_T_PROJECTED_ANCHORS:
        raise ValueError(f"Unknown reduction method: {method}")
    anchor_rows = FRG_T_PROJECTED_ANCHORS[method]
    eta_anchor = _interpolate_anchor_rows(anchor_rows, formal_n, "eta")
    gamma_anchor = _interpolate_anchor_rows(anchor_rows, formal_n, "gamma_phi")
    if not np.isfinite(eta_proxy) or eta_proxy <= 0.0:
        return GammaReductionResult(
            formal_n=float(formal_n),
            eta_proxy=float(eta_proxy),
            eta_anchor=float(eta_anchor),
            gamma_anchor=float(gamma_anchor),
            gamma_proxy=float("nan"),
            target_ratio=float("nan"),
            status="non_physical_eta_proxy",
            method=method,
        )
    if eta_anchor <= 0.0:
        raise ValueError("Anchor eta must stay positive.")

    eta_min = eta_anchor / eta_band_factor
    eta_max = eta_anchor * eta_band_factor
    if eta_proxy < eta_min or eta_proxy > eta_max:
        return GammaReductionResult(
            formal_n=float(formal_n),
            eta_proxy=float(eta_proxy),
            eta_anchor=float(eta_anchor),
            gamma_anchor=float(gamma_anchor),
            gamma_proxy=float("nan"),
            target_ratio=float("nan"),
            status="out_of_anchor_band",
            method=method,
        )

    gamma_proxy = gamma_anchor * (eta_proxy / eta_anchor)
    return GammaReductionResult(
        formal_n=float(formal_n),
        eta_proxy=float(eta_proxy),
        eta_anchor=float(eta_anchor),
        gamma_anchor=float(gamma_anchor),
        gamma_proxy=float(gamma_proxy),
        target_ratio=float(gamma_proxy / TARGET_GAMMA_PAPER_IV),
        status="calibrated",
        method=method,
    )
