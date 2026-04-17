#!/usr/bin/env python3
"""
Estimator-specific transfer-function probe for the fractional critical-line surface.

This does not claim to solve gamma_phi. It tests a narrower H5 hypothesis:
whether each quotient-lattice eta estimator carries an approximately stable
multiplicative inflation factor across the pseudo-critical line. If that factor
is stable, metrology remains a live explanation; if not, the remaining failure
must sit deeper in the critical surface or proxy family.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from strong_coupling_common import RESULTS_DIR, TARGET_GAMMA_PAPER_IV, csv_write
from strong_coupling_compare import read_reduction

TRANSFER_STATUS_STABLE = "stable_transfer_candidate"
TRANSFER_STATUS_UNSTABLE = "unstable_transfer_candidate"
TRANSFER_STATUS_BLOCKED = "transfer_blocked"


def row_float(row: dict[str, str], key: str, default: float = float("nan")) -> float:
    raw = row.get(key, "")
    if raw in {"", None}:
        return default
    return float(raw)


def build_transfer_rows(
    reduction_rows: list[dict[str, str]],
    anchor_method: str = "de2",
    max_cv: float = 0.10,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    if anchor_method not in {"de2", "lpa"}:
        raise ValueError(f"Unsupported anchor_method: {anchor_method}")

    eta_anchor_key = f"eta_anchor_{anchor_method}"
    gamma_anchor_key = f"gamma_anchor_{anchor_method}"

    grouped: dict[str, list[dict[str, str]]] = {}
    for row in reduction_rows:
        grouped.setdefault(str(row["eta_estimator"]), []).append(row)

    summary_rows: list[dict[str, object]] = []
    transfer_rows: list[dict[str, object]] = []

    for estimator, rows in sorted(grouped.items()):
        raw_factors = np.array(
            [
                row_float(row, "eta_proxy") / row_float(row, eta_anchor_key)
                for row in rows
                if np.isfinite(row_float(row, "eta_proxy"))
                and np.isfinite(row_float(row, eta_anchor_key))
                and row_float(row, eta_anchor_key) > 0.0
            ],
            dtype=np.float64,
        )
        if raw_factors.size == 0:
            median_factor = float("nan")
            mean_factor = float("nan")
            cv = float("nan")
            stable = False
            status = TRANSFER_STATUS_BLOCKED
        else:
            median_factor = float(np.median(raw_factors))
            mean_factor = float(np.mean(raw_factors))
            std_factor = float(np.std(raw_factors, ddof=0))
            cv = float(std_factor / mean_factor) if mean_factor > 0.0 else float("nan")
            stable = bool(np.isfinite(cv) and cv <= max_cv and median_factor > 0.0)
            status = TRANSFER_STATUS_STABLE if stable else TRANSFER_STATUS_UNSTABLE

        corrected_etas: list[float] = []
        for row in rows:
            eta_proxy = row_float(row, "eta_proxy")
            eta_anchor = row_float(row, eta_anchor_key)
            gamma_anchor = row_float(row, gamma_anchor_key)
            if stable and np.isfinite(eta_proxy) and median_factor > 0.0:
                corrected_eta = eta_proxy / median_factor
                corrected_gamma = gamma_anchor * (corrected_eta / eta_anchor) if eta_anchor > 0.0 else float("nan")
                target_ratio = corrected_gamma / TARGET_GAMMA_PAPER_IV if np.isfinite(corrected_gamma) else float("nan")
                corrected_etas.append(corrected_eta)
            else:
                corrected_eta = float("nan")
                corrected_gamma = float("nan")
                target_ratio = float("nan")
            transfer_rows.append(
                {
                    "formal_n": row["formal_n"],
                    "coupling_id": row["coupling_id"],
                    "eta_estimator": estimator,
                    "anchor_method": anchor_method,
                    "eta_proxy": row["eta_proxy"],
                    "eta_anchor": row.get(eta_anchor_key, ""),
                    "gamma_anchor": row.get(gamma_anchor_key, ""),
                    "transfer_factor_raw": ""
                    if not (np.isfinite(eta_proxy) and np.isfinite(eta_anchor) and eta_anchor > 0.0)
                    else f"{(eta_proxy / eta_anchor):.10f}",
                    "transfer_factor_median": "" if not np.isfinite(median_factor) else f"{median_factor:.10f}",
                    "transfer_factor_cv": "" if not np.isfinite(cv) else f"{cv:.10f}",
                    "transfer_stability_pass": str(stable),
                    "eta_transfer_corrected": "" if not np.isfinite(corrected_eta) else f"{corrected_eta:.10f}",
                    "gamma_phi_transfer_corrected": "" if not np.isfinite(corrected_gamma) else f"{corrected_gamma:.10f}",
                    "target_ratio_transfer": "" if not np.isfinite(target_ratio) else f"{target_ratio:.10f}",
                    "status_transfer": status,
                }
            )

        summary_rows.append(
            {
                "eta_estimator": estimator,
                "anchor_method": anchor_method,
                "n_rows": len(rows),
                "transfer_factor_median": "" if not np.isfinite(median_factor) else f"{median_factor:.10f}",
                "transfer_factor_mean": "" if not np.isfinite(mean_factor) else f"{mean_factor:.10f}",
                "transfer_factor_cv": "" if not np.isfinite(cv) else f"{cv:.10f}",
                "transfer_stability_pass": str(stable),
                "eta_transfer_min": ""
                if not corrected_etas
                else f"{min(corrected_etas):.10f}",
                "eta_transfer_max": ""
                if not corrected_etas
                else f"{max(corrected_etas):.10f}",
                "status_transfer": status,
            }
        )

    return summary_rows, transfer_rows


def build_analysis(
    summary_rows: list[dict[str, object]],
    transfer_rows: list[dict[str, object]],
    anchor_method: str,
) -> str:
    stable_estimators = [row for row in summary_rows if str(row["transfer_stability_pass"]) == "True"]
    lines = [
        "# Fractional Metrology Transfer Analysis",
        "",
        "## Setup",
        f"- anchor_method: {anchor_method}",
        f"- estimators_loaded: {len(summary_rows)}",
        f"- transfer_rows: {len(transfer_rows)}",
        "",
        "## Estimator Stability",
        "| estimator | n_rows | median_factor | mean_factor | cv | stable | status |",
        "|:---|---:|---:|---:|---:|:---:|:---|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['eta_estimator']} | {row['n_rows']} | {row['transfer_factor_median'] or '--'} "
            f"| {row['transfer_factor_mean'] or '--'} | {row['transfer_factor_cv'] or '--'} "
            f"| {row['transfer_stability_pass']} | {row['status_transfer']} |"
        )

    lines.extend(
        [
            "",
            "## Transfer-Corrected Surface",
            "| coupling_id | estimator | eta_proxy | factor_raw | eta_transfer_corrected | gamma_transfer_corrected | status |",
            "|:---|:---|---:|---:|---:|---:|:---|",
        ]
    )
    for row in transfer_rows:
        lines.append(
            f"| {row['coupling_id']} | {row['eta_estimator']} | {row['eta_proxy']} "
            f"| {row['transfer_factor_raw'] or '--'} | {row['eta_transfer_corrected'] or '--'} "
            f"| {row['gamma_phi_transfer_corrected'] or '--'} | {row['status_transfer']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            f"- stable_estimators: {[row['eta_estimator'] for row in stable_estimators] or 'none'}",
        ]
    )
    if stable_estimators:
        lines.append(
            "- interpretation: estimator-specific inflation factors are approximately stable along the selected critical line. "
            "This keeps the H5 metrology hypothesis alive, but the correction remains anchor-dependent and therefore is not an independent resolution."
        )
    else:
        lines.append(
            "- interpretation: estimator-specific inflation factors are not stable enough to sustain a multiplicative transfer-function story. "
            "The main failure then sits deeper in criticality or proxy topology."
        )
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Probe estimator-specific transfer functions on a fractional critical-line reduction surface.")
    parser.add_argument(
        "--reduction",
        type=Path,
        default=RESULTS_DIR / "phase3_fractional_critical_line_reduction_estimators.csv",
        help="Reduction CSV with eta_estimator rows.",
    )
    parser.add_argument(
        "--anchor-method",
        choices=["de2", "lpa"],
        default="de2",
        help="Anchor family used to define the transfer factor.",
    )
    parser.add_argument(
        "--max-cv",
        type=float,
        default=0.10,
        help="Maximum coefficient of variation for an estimator-specific multiplicative transfer factor to count as stable.",
    )
    parser.add_argument(
        "--summary-out",
        type=Path,
        default=RESULTS_DIR / "phase3_fractional_metrology_summary.csv",
        help="Estimator-level transfer summary CSV.",
    )
    parser.add_argument(
        "--transfer-out",
        type=Path,
        default=RESULTS_DIR / "phase3_fractional_metrology_transfer.csv",
        help="Coupling-level transfer-corrected CSV.",
    )
    parser.add_argument(
        "--analysis-out",
        type=Path,
        default=RESULTS_DIR / "phase3_fractional_metrology_analysis.md",
        help="Markdown report path.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    reduction_rows, reduction_missing = read_reduction(args.reduction)
    if reduction_missing:
        raise SystemExit(f"reduction schema incomplete: {reduction_missing}")

    summary_rows, transfer_rows = build_transfer_rows(
        reduction_rows=reduction_rows,
        anchor_method=args.anchor_method,
        max_cv=args.max_cv,
    )
    if not summary_rows:
        raise SystemExit("no transfer rows could be constructed")

    csv_write(summary_rows, args.summary_out)
    csv_write(transfer_rows, args.transfer_out)
    args.analysis_out.write_text(build_analysis(summary_rows, transfer_rows, args.anchor_method), encoding="utf-8")
    print(f"Wrote metrology summary to {args.summary_out}")
    print(f"Wrote metrology transfer rows to {args.transfer_out}")
    print(f"Wrote metrology analysis to {args.analysis_out}")


if __name__ == "__main__":
    main()
