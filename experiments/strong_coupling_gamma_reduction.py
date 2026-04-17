#!/usr/bin/env python3
"""
Reduction surface from fractional eta proxies to calibrated gamma_phi proxies.

This is intentionally a separate layer. Paper V defines gamma_phi independently
of eta, so the reduction implemented here is a calibration surface anchored to
the FRG tables already fixed in the paper, not a claim that gamma_phi == eta.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from strong_coupling_common import (
    DIMENSION_MODE_FRACTIONAL,
    RESULTS_DIR,
    csv_write,
    fit_power_law,
    gamma_phi_reduction_from_eta,
    validate_scan_csv,
)

ETA_ESTIMATOR_SPECS = {
    "chi_connected": {
        "observable": "susceptibility",
        "fit_method": "fractional chi ~ L^(2-eta)",
    },
    "kmin_structure": {
        "observable": "structure_factor_kmin",
        "fit_method": "fractional S(k_min) ~ L^(2-eta)",
    },
}

def fractional_eta_proxies(scan_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str, str], list[tuple[int, float, float]]] = {}
    for row in scan_rows:
        if not row.get("formal_n"):
            continue
        for estimator_name, spec in ETA_ESTIMATOR_SPECS.items():
            if row.get("observable") != spec["observable"]:
                continue
            key = (row["formal_n"], row["coupling_id"], estimator_name)
            grouped.setdefault(key, []).append(
                (
                    int(row["L"]),
                    float(row["mean"]),
                    max(float(row["stderr"]), 1e-6),
                )
            )

    proxies: list[dict[str, object]] = []
    for (formal_n, coupling_id, estimator_name), entries in sorted(
        grouped.items(),
        key=lambda item: (float(item[0][0]), item[0][1], item[0][2]),
    ):
        if len(entries) < 2:
            continue
        entries.sort(key=lambda item: item[0])
        sizes = [entry[0] for entry in entries]
        values = [entry[1] for entry in entries]
        errors = [entry[2] for entry in entries]
        fit = fit_power_law(
            sizes,
            values,
            errors,
            method=str(ETA_ESTIMATOR_SPECS[estimator_name]["fit_method"]),
        )
        eta_proxy = 2.0 - fit.slope if fit.slope == fit.slope else float("nan")
        proxies.append(
            {
                "formal_n": float(formal_n),
                "coupling_id": coupling_id,
                "eta_estimator": estimator_name,
                "source_observable": str(ETA_ESTIMATOR_SPECS[estimator_name]["observable"]),
                "sizes": ",".join(str(size) for size in sizes),
                "eta_proxy": float(eta_proxy),
                "eta_stderr": float(fit.stderr),
                "fit_method": fit.method,
            }
        )
    return proxies


def build_reduction_rows(scan_rows: list[dict[str, str]]) -> list[dict[str, object]]:
    eta_rows = fractional_eta_proxies(scan_rows)
    rows: list[dict[str, object]] = []
    for eta_row in eta_rows:
        lpa = gamma_phi_reduction_from_eta(eta_row["formal_n"], eta_row["eta_proxy"], method="lpa_t")
        de2 = gamma_phi_reduction_from_eta(eta_row["formal_n"], eta_row["eta_proxy"], method="de2_t")
        rows.append(
            {
                "formal_n": f"{eta_row['formal_n']:.6f}",
                "coupling_id": eta_row["coupling_id"],
                "eta_estimator": eta_row["eta_estimator"],
                "source_observable": eta_row["source_observable"],
                "fit_method": eta_row["fit_method"],
                "sizes": eta_row["sizes"],
                "eta_proxy": f"{eta_row['eta_proxy']:.10f}",
                "eta_stderr": f"{eta_row['eta_stderr']:.10f}",
                "eta_anchor_lpa": f"{lpa.eta_anchor:.10f}",
                "gamma_anchor_lpa": f"{lpa.gamma_anchor:.10f}",
                "gamma_phi_proxy_lpa": "" if lpa.gamma_proxy != lpa.gamma_proxy else f"{lpa.gamma_proxy:.10f}",
                "status_lpa": lpa.status,
                "eta_anchor_de2": f"{de2.eta_anchor:.10f}",
                "gamma_anchor_de2": f"{de2.gamma_anchor:.10f}",
                "gamma_phi_proxy_de2": "" if de2.gamma_proxy != de2.gamma_proxy else f"{de2.gamma_proxy:.10f}",
                "status_de2": de2.status,
                "target_ratio_lpa": "" if lpa.target_ratio != lpa.target_ratio else f"{lpa.target_ratio:.10f}",
                "target_ratio_de2": "" if de2.target_ratio != de2.target_ratio else f"{de2.target_ratio:.10f}",
            }
        )
    return rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Reduce fractional eta proxies onto calibrated gamma_phi proxy surfaces.")
    parser.add_argument(
        "--scan",
        type=Path,
        default=RESULTS_DIR / "phase2_fractional_scan.csv",
        help="Fractional scan CSV path.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=RESULTS_DIR / "phase2_gamma_reduction.csv",
        help="Reduction CSV path.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    scan_rows, scan_missing = validate_scan_csv(args.scan)
    if scan_missing:
        raise SystemExit(f"scan schema incomplete: {scan_missing}")
    scan_modes = {row["dimension_mode"] for row in scan_rows}
    if scan_modes != {DIMENSION_MODE_FRACTIONAL}:
        raise SystemExit(f"gamma reduction requires pure fractional_proxy scan, got {sorted(scan_modes)}")
    rows = build_reduction_rows(scan_rows)
    if not rows:
        raise SystemExit("no reducible susceptibility rows found in fractional scan")
    csv_write(rows, args.out)
    print(f"Wrote gamma reduction to {args.out}")


if __name__ == "__main__":
    main()
