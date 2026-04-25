#!/usr/bin/env python3
"""
Cross-n portability probe for estimator-specific transfer functions.

This script extends the H5 metrology surface from a single formal_n to a small
set of neighboring dimensions. It keeps the critical-line-first workflow and
asks a narrower question than "is gamma solved?":

Is the estimator-specific transfer factor stable not only along the selected
pseudo-critical line for one n, but also portable across nearby n values?
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

from strong_coupling_common import RESULTS_DIR, csv_write, json_dump, parse_int_list
from strong_coupling_fractional_critical_line import (
    build_line_candidates,
    detect_crossing_records,
    filter_scan_rows,
    schedule_from_candidates,
    summarize_scan_rows,
)
from strong_coupling_fractional_metrology import build_transfer_rows
from strong_coupling_fractional_proxy import build_scan_rows
from strong_coupling_gamma_reduction import build_reduction_rows


DEFAULT_PORTABILITY_WINDOWS = {
    "2.780000": {
        "mass_like": [0.90, 0.95, 1.00, 1.05, 1.10],
        "lambda_like": [1.00, 1.05, 1.10, 1.15, 1.20],
    },
    "2.900000": {
        "mass_like": [0.33, 0.38, 0.43, 0.48, 0.53],
        "lambda_like": [0.45, 0.50, 0.55, 0.60, 0.65],
    },
    "3.000000": {
        "mass_like": [1.30, 1.40, 1.50, 1.60, 1.70],
        "lambda_like": [0.40, 0.45, 0.50, 0.55, 0.60],
    },
}


def formal_key(formal_n: float) -> str:
    return f"{formal_n:.6f}"


def row_float(row: dict[str, object], key: str, default: float = float("nan")) -> float:
    raw = row.get(key, "")
    if raw in {"", None}:
        return default
    return float(raw)


def load_windows(path: Path | None) -> dict[str, dict[str, list[float]]]:
    if path is None:
        return DEFAULT_PORTABILITY_WINDOWS
    payload = json.loads(path.read_text(encoding="utf-8"))
    windows: dict[str, dict[str, list[float]]] = {}
    for key, value in payload.items():
        windows[formal_key(float(key))] = {
            "mass_like": [float(item) for item in value["mass_like"]],
            "lambda_like": [float(item) for item in value["lambda_like"]],
        }
    return windows


def portability_summary_rows(
    summary_rows: list[dict[str, object]],
    expected_formal_ns: list[float],
    max_portability_cv: float,
) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for row in summary_rows:
        grouped.setdefault(str(row["eta_estimator"]), []).append(row)

    rows: list[dict[str, object]] = []
    expected_keys = {formal_key(value) for value in expected_formal_ns}
    for estimator, entries in sorted(grouped.items()):
        stable_entries = [row for row in entries if str(row["transfer_stability_pass"]) == "True"]
        stable_keys = {str(row["formal_n"]) for row in stable_entries}
        medians = np.array(
            [
                row_float(row, "transfer_factor_median")
                for row in stable_entries
                if np.isfinite(row_float(row, "transfer_factor_median"))
            ],
            dtype=np.float64,
        )
        if medians.size == 0:
            portability_cv = float("nan")
            portability_pass = False
        else:
            mean = float(np.mean(medians))
            std = float(np.std(medians, ddof=0))
            portability_cv = float(std / mean) if mean > 0.0 else float("nan")
            portability_pass = bool(
                stable_keys == expected_keys
                and np.isfinite(portability_cv)
                and portability_cv <= max_portability_cv
            )
        rows.append(
            {
                "eta_estimator": estimator,
                "stable_formal_n_count": len(stable_entries),
                "expected_formal_n_count": len(expected_formal_ns),
                "stable_formal_ns": "|".join(sorted(stable_keys)),
                "transfer_factor_min": "" if medians.size == 0 else f"{float(np.min(medians)):.10f}",
                "transfer_factor_max": "" if medians.size == 0 else f"{float(np.max(medians)):.10f}",
                "transfer_factor_portability_cv": "" if not np.isfinite(portability_cv) else f"{portability_cv:.10f}",
                "portability_pass": str(portability_pass),
                "status_portability": "portable_transfer_candidate" if portability_pass else "nonportable_transfer_candidate",
            }
        )
    return rows


def build_analysis(
    line_rows: list[dict[str, object]],
    metrology_summary_rows: list[dict[str, object]],
    portability_rows: list[dict[str, object]],
    formal_ns: list[float],
    sizes: list[int],
    anchor_method: str,
    max_cv: float,
    max_portability_cv: float,
) -> str:
    portable_estimators = [row["eta_estimator"] for row in portability_rows if str(row["portability_pass"]) == "True"]
    lines = [
        "# Fractional Transfer Portability Analysis",
        "",
        "## Setup",
        f"- formal_n values: {[formal_key(value) for value in formal_ns]}",
        f"- sizes: {sizes}",
        f"- anchor_method: {anchor_method}",
        f"- per_n transfer max_cv: {max_cv}",
        f"- cross_n portability max_cv: {max_portability_cv}",
        "",
        "## Critical-Line Surface",
        "| formal_n | crossing_records | selected_couplings | selected_scan_rows | line_status |",
        "|:---:|---:|---:|---:|:---|",
    ]
    for row in line_rows:
        lines.append(
            f"| {row['formal_n']} | {row['crossing_records']} | {row['selected_couplings']} "
            f"| {row['selected_scan_rows']} | {row['line_status']} |"
        )

    lines.extend(
        [
            "",
            "## Per-n Transfer Stability",
            "| formal_n | estimator | median_factor | cv | stable | status |",
            "|:---:|:---|---:|---:|:---:|:---|",
        ]
    )
    for row in metrology_summary_rows:
        lines.append(
            f"| {row['formal_n']} | {row['eta_estimator']} | {row['transfer_factor_median'] or '--'} "
            f"| {row['transfer_factor_cv'] or '--'} | {row['transfer_stability_pass']} | {row['status_transfer']} |"
        )

    lines.extend(
        [
            "",
            "## Cross-n Portability",
            "| estimator | stable_n_count | factor_min | factor_max | cross_n_cv | portability_pass | status |",
            "|:---|---:|---:|---:|---:|:---:|:---|",
        ]
    )
    for row in portability_rows:
        lines.append(
            f"| {row['eta_estimator']} | {row['stable_formal_n_count']}/{row['expected_formal_n_count']} "
            f"| {row['transfer_factor_min'] or '--'} | {row['transfer_factor_max'] or '--'} "
            f"| {row['transfer_factor_portability_cv'] or '--'} | {row['portability_pass']} | {row['status_portability']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            f"- portable_estimators: {portable_estimators or 'none'}",
        ]
    )
    if portable_estimators:
        lines.append(
            "- interpretation: at least one estimator-specific transfer factor survives not only along a single critical line but across neighboring formal_n values. "
            "This strengthens H5 from a local explanation into a portability candidate."
        )
    else:
        lines.append(
            "- interpretation: the transfer factor may be stable locally but does not survive cross-n portability. "
            "In that case H5 is insufficient as a general explanation and the main failure returns to proxy topology or critical-surface definition."
        )
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Probe cross-n portability of estimator-specific transfer factors.")
    parser.add_argument("--L", default="6,8,10,12", help="Comma-separated lattice sizes.")
    parser.add_argument(
        "--formal-n",
        default="2.78,2.90,3.00",
        help="Comma-separated formal n values to probe for portability.",
    )
    parser.add_argument(
        "--window-json",
        type=Path,
        default=None,
        help="Optional JSON mapping formal_n to mass_like/lambda_like windows.",
    )
    parser.add_argument("--warmup", type=int, default=120, help="Warmup sweeps.")
    parser.add_argument("--measure", type=int, default=240, help="Measured sweeps.")
    parser.add_argument("--seed", type=int, default=171, help="Base RNG seed.")
    parser.add_argument("--proposal-scale", type=float, default=0.65, help="Proposal scale.")
    parser.add_argument("--block-size", type=int, default=8, help="Bootstrap block size.")
    parser.add_argument("--anchor-method", choices=["de2", "lpa"], default="de2")
    parser.add_argument("--transfer-max-cv", type=float, default=0.10)
    parser.add_argument("--portability-max-cv", type=float, default=0.20)
    parser.add_argument("--scan-out", type=Path, default=RESULTS_DIR / "phase4_fractional_portability_scan.csv")
    parser.add_argument("--reduction-out", type=Path, default=RESULTS_DIR / "phase4_fractional_portability_reduction.csv")
    parser.add_argument("--line-summary-out", type=Path, default=RESULTS_DIR / "phase4_fractional_portability_line_summary.csv")
    parser.add_argument("--metrology-summary-out", type=Path, default=RESULTS_DIR / "phase4_fractional_portability_metrology_summary.csv")
    parser.add_argument("--transfer-out", type=Path, default=RESULTS_DIR / "phase4_fractional_portability_transfer.csv")
    parser.add_argument("--portability-out", type=Path, default=RESULTS_DIR / "phase4_fractional_portability_summary.csv")
    parser.add_argument("--analysis-out", type=Path, default=RESULTS_DIR / "phase4_fractional_portability_analysis.md")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    sizes = parse_int_list(args.L)
    formal_ns = [float(item.strip()) for item in args.formal_n.split(",") if item.strip()]
    windows = load_windows(args.window_json)

    all_selected_scan_rows: list[dict[str, object]] = []
    all_reduction_rows: list[dict[str, object]] = []
    all_metrology_summary_rows: list[dict[str, object]] = []
    all_transfer_rows: list[dict[str, object]] = []
    line_rows: list[dict[str, object]] = []

    for formal_n in formal_ns:
        key = formal_key(formal_n)
        if key not in windows:
            raise SystemExit(f"Missing window definition for formal_n={key}")
        mass_likes = windows[key]["mass_like"]
        lambda_likes = windows[key]["lambda_like"]
        grid_scan_rows = build_scan_rows(
            sizes=sizes,
            formal_ns=[formal_n],
            mass_likes=mass_likes,
            lambda_likes=lambda_likes,
            warmup=args.warmup,
            measure=args.measure,
            seed=args.seed,
            proposal_scale=args.proposal_scale,
            block_size=args.block_size,
            t_regulator=0.0,
            proxy_kind="t_projected_direct",
            schedule_mode="shared",
            schedule_path=None,
        )
        summary = summarize_scan_rows(grid_scan_rows)
        crossing_records = detect_crossing_records(summary, formal_n, mass_likes, lambda_likes, sizes)
        candidates = build_line_candidates(summary, crossing_records, formal_n, mass_likes, lambda_likes, sizes)
        selected_ids = {str(row["selected_coupling_id"]) for row in candidates if row["selected_coupling_id"]}
        selected_scan_rows = filter_scan_rows(grid_scan_rows, selected_ids)
        reduction_rows = build_reduction_rows([{key: str(value) for key, value in row.items()} for row in selected_scan_rows]) if selected_scan_rows else []
        summary_rows, transfer_rows = build_transfer_rows(
            [{key: str(value) for key, value in row.items()} for row in reduction_rows],
            anchor_method=args.anchor_method,
            max_cv=args.transfer_max_cv,
        ) if reduction_rows else ([], [])

        line_rows.append(
            {
                "formal_n": key,
                "crossing_records": len(crossing_records),
                "selected_couplings": len(selected_ids),
                "selected_scan_rows": len(selected_scan_rows),
                "line_status": "selected_line_found" if selected_ids else "no_line_found",
                "window_mass_like": "|".join(f"{value:.6f}" for value in mass_likes),
                "window_lambda_like": "|".join(f"{value:.6f}" for value in lambda_likes),
                "schedule": json.dumps(schedule_from_candidates(candidates), ensure_ascii=False, sort_keys=True),
            }
        )

        for row in selected_scan_rows:
            all_selected_scan_rows.append(row)
        for row in reduction_rows:
            all_reduction_rows.append(row)
        for row in summary_rows:
            all_metrology_summary_rows.append({"formal_n": key, **row})
        for row in transfer_rows:
            all_transfer_rows.append({"formal_n": key, **row})

    portability_rows = portability_summary_rows(
        summary_rows=all_metrology_summary_rows,
        expected_formal_ns=formal_ns,
        max_portability_cv=args.portability_max_cv,
    )

    if not all_selected_scan_rows:
        raise SystemExit("no selected critical-line rows were found for any formal_n")

    csv_write(all_selected_scan_rows, args.scan_out)
    csv_write(all_reduction_rows, args.reduction_out)
    csv_write(line_rows, args.line_summary_out)
    csv_write(all_metrology_summary_rows, args.metrology_summary_out)
    csv_write(all_transfer_rows, args.transfer_out)
    csv_write(portability_rows, args.portability_out)
    args.analysis_out.write_text(
        build_analysis(
            line_rows=line_rows,
            metrology_summary_rows=all_metrology_summary_rows,
            portability_rows=portability_rows,
            formal_ns=formal_ns,
            sizes=sizes,
            anchor_method=args.anchor_method,
            max_cv=args.transfer_max_cv,
            max_portability_cv=args.portability_max_cv,
        ),
        encoding="utf-8",
    )
    print(f"Wrote portability scan to {args.scan_out}")
    print(f"Wrote portability reduction to {args.reduction_out}")
    print(f"Wrote line summary to {args.line_summary_out}")
    print(f"Wrote metrology summary to {args.metrology_summary_out}")
    print(f"Wrote transfer rows to {args.transfer_out}")
    print(f"Wrote portability summary to {args.portability_out}")
    print(f"Wrote analysis to {args.analysis_out}")


if __name__ == "__main__":
    main()
