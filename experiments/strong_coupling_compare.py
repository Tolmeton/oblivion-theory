#!/usr/bin/env python3
"""
Comparison surface for the strong-coupling benchmark cycle.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from strong_coupling_common import (
    DIMENSION_MODE_FRACTIONAL,
    DIMENSION_MODE_INTEGER,
    FRG_3D_ISING,
    LITERATURE_3D_ISING,
    RESULTS_DIR,
    scan_sanity_issues,
    validate_scan_csv,
)


def read_reference(path: Path) -> tuple[dict[str, object], list[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = [
        "model",
        "dimension_mode",
        "sizes",
        "critical_point",
        "binder",
        "xi_over_L",
        "susceptibility",
        "eta_estimate",
        "nu_estimate",
        "stderr",
        "tau_int",
        "diagnostics",
        "pass",
    ]
    missing = [key for key in required if key not in data]
    return data, missing


def metric_line(name: str, mc: float, literature: float, frg: float) -> str:
    return (
        f"| {name} | {mc:.4f} | {literature:.4f} | {abs(mc - literature):.4f} "
        f"| {frg:.4f} | {abs(mc - frg):.4f} |"
    )


def format_float_set(rows: list[dict[str, str]], key: str) -> list[str]:
    values = sorted({float(row[key]) for row in rows if row.get(key) not in {None, ""}})
    return [f"{value:.6f}" for value in values]


def read_reduction(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    required = [
        "formal_n",
        "coupling_id",
        "eta_estimator",
        "source_observable",
        "fit_method",
        "sizes",
        "eta_proxy",
        "eta_stderr",
        "eta_anchor_lpa",
        "gamma_anchor_lpa",
        "gamma_phi_proxy_lpa",
        "status_lpa",
        "eta_anchor_de2",
        "gamma_anchor_de2",
        "gamma_phi_proxy_de2",
        "status_de2",
    ]
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        missing = [col for col in required if col not in (reader.fieldnames or [])]
    return rows, missing


def build_markdown(
    reference: dict[str, object] | None,
    reference_missing: list[str],
    scan_rows: list[dict[str, str]],
    scan_missing: list[str],
    reduction_rows: list[dict[str, str]],
    reduction_missing: list[str],
    issues: list[str],
) -> str:
    scan_dimension_modes = sorted({row["dimension_mode"] for row in scan_rows}) if scan_rows and not scan_missing else []
    scan_mode = scan_dimension_modes[0] if len(scan_dimension_modes) == 1 else None
    lines = [
        "# Strong-Coupling Benchmark Analysis",
        "",
        "## Summary",
    ]
    if issues:
        lines.extend([f"- FAIL: {issue}" for issue in issues])
    else:
        lines.append("- PASS: schema completeness and dimension alignment are satisfied.")

    lines.extend(
        [
            "",
            "## Schema Completeness",
            f"- Reference missing keys: {reference_missing or 'none'}",
            f"- Scan missing columns: {scan_missing or 'none'}",
            f"- Reduction missing columns: {reduction_missing or 'none'}",
        ]
    )

    if reference is not None and not reference_missing:
        binder_mc = float(reference["binder"]["value"])
        xi_mc = float(reference["xi_over_L"]["value"])
        eta_mc = float(reference["eta_estimate"]["value"])
        nu_mc = float(reference["nu_estimate"]["value"])
        pass_breakdown = reference["diagnostics"].get("pass_breakdown", {})
        failed_reference_checks = [name for name, payload in pass_breakdown.items() if not bool(payload.get("pass"))]

        lines.extend(
            [
                "",
                "## MC vs Literature",
                "| Metric | MC | Literature | |Δ| | Current FRG | |Δ| |",
                "|:---|---:|---:|---:|---:|---:|",
                metric_line(
                    "binder",
                    binder_mc,
                    float(LITERATURE_3D_ISING["binder"]),
                    float(LITERATURE_3D_ISING["binder"]),
                ),
                metric_line(
                    "xi_over_L",
                    xi_mc,
                    float(LITERATURE_3D_ISING["xi_over_L"]),
                    float(LITERATURE_3D_ISING["xi_over_L"]),
                ),
                metric_line(
                    "eta",
                    eta_mc,
                    float(LITERATURE_3D_ISING["eta"]),
                    float(FRG_3D_ISING["eta"]),
                ),
                metric_line(
                    "nu",
                    nu_mc,
                    float(LITERATURE_3D_ISING["nu"]),
                    float(FRG_3D_ISING["nu"]),
                ),
                "",
                "## MC vs Current FRG",
                f"- Reference pass flag: {reference['pass']}",
                f"- Current FRG source: {FRG_3D_ISING['source']}",
            ]
        )
        if pass_breakdown:
            lines.extend(
                [
                    "",
                    "## Reference Gate",
                    "| Metric | Value | Target | |Δ| | Tolerance | Pass |",
                    "|:---|---:|---:|---:|---:|:---:|",
                ]
            )
            for name in ["binder", "xi_over_L", "eta", "nu"]:
                if name not in pass_breakdown:
                    continue
                payload = pass_breakdown[name]
                lines.append(
                    f"| {name} | {float(payload['value']):.4f} | {float(payload['target']):.4f} "
                    f"| {float(payload['delta']):.4f} | {float(payload['tolerance']):.4f} "
                    f"| {'yes' if bool(payload['pass']) else 'no'} |"
                )
            if failed_reference_checks:
                lines.append(f"- blocking_reason: reference gate blocked by {', '.join(failed_reference_checks)}")

    lines.extend(
        [
            "",
            "## Scan Surface",
            f"- Rows loaded: {len(scan_rows)}",
        ]
    )
    if scan_rows and not scan_missing:
        couplings = sorted({row["coupling_id"] for row in scan_rows})
        observables = sorted({row["observable"] for row in scan_rows})
        lines.extend(
            [
                f"- dimension_mode values: {scan_dimension_modes}",
                f"- coupling_ids: {couplings}",
                f"- observables: {observables}",
            ]
        )
        if scan_mode == DIMENSION_MODE_INTEGER:
            lines.append("- scan_mode: integer_proxy")
        elif scan_mode == DIMENSION_MODE_FRACTIONAL:
            fractional_ns = format_float_set(scan_rows, "formal_n")
            n_effs = format_float_set(scan_rows, "n_eff")
            t_axis_weights = format_float_set(scan_rows, "t_axis_weight")
            transverse_weights = format_float_set(scan_rows, "transverse_weight")
            proxy_kinds = sorted({row.get("proxy_kind", "unknown") for row in scan_rows})
            schedule_modes = sorted({row.get("schedule_mode", "unknown") for row in scan_rows})
            schedule_sources = sorted({row.get("schedule_source", "unknown") for row in scan_rows})
            lines.extend(
                [
                    "- scan_mode: fractional_proxy",
                    f"- formal_n values: {fractional_ns}",
                    f"- n_eff values: {n_effs}",
                    f"- transverse_weight values: {transverse_weights}",
                    f"- t_axis_weight values: {t_axis_weights}",
                    f"- proxy_kinds: {proxy_kinds}",
                    f"- schedule_modes: {schedule_modes}",
                    f"- schedule_sources: {schedule_sources}",
                ]
            )
            if reduction_rows and not reduction_missing:
                lines.extend(
                    [
                        "",
                        "## Gamma Reduction Surface",
                        "| formal_n | coupling_id | estimator | source | sizes | eta_proxy | LPA' γ proxy | LPA' status | DE2 γ proxy | DE2 status |",
                        "|:---:|:---|:---|:---|:---|---:|---:|:---|---:|:---|",
                    ]
                )
                calibrated_rows = 0
                for row in reduction_rows:
                    lpa_proxy = row["gamma_phi_proxy_lpa"] or "--"
                    de2_proxy = row["gamma_phi_proxy_de2"] or "--"
                    if row["status_lpa"] == "calibrated" or row["status_de2"] == "calibrated":
                        calibrated_rows += 1
                    lines.append(
                        f"| {float(row['formal_n']):.2f} | {row['coupling_id']} | {row['eta_estimator']} "
                        f"| {row['source_observable']} | {row['sizes']} | {float(row['eta_proxy']):.4f} "
                        f"| {lpa_proxy} | {row['status_lpa']} | {de2_proxy} | {row['status_de2']} |"
                    )
                lines.append(f"- calibrated_rows: {calibrated_rows} / {len(reduction_rows)}")
                lines.append("- note: これは η = γ の同一視ではなく、Paper V の FRG 表を anchor にした calibrated reduction surface である。")
            elif scan_mode == DIMENSION_MODE_FRACTIONAL:
                lines.append("- note: fractional scan は存在するが gamma reduction surface は未生成または schema 不完全。")

    reference_ready = bool(reference is not None and not reference_missing and bool(reference["pass"]))
    ready = reference_ready and not issues and not scan_missing
    gamma_ready = bool(
        scan_mode == DIMENSION_MODE_FRACTIONAL
        and reference_ready
        and not reduction_missing
        and any(row["status_lpa"] == "calibrated" or row["status_de2"] == "calibrated" for row in reduction_rows)
    )
    lines.extend(
        [
            "",
            "## Future Fractional Proxy",
            f"- ready_for_fractional_proxy: {ready}",
            f"- ready_for_gamma_comparison: {gamma_ready}",
            f"- scan_mode: {scan_mode or 'mixed_or_missing'}",
        ]
    )
    if ready and scan_mode == DIMENSION_MODE_FRACTIONAL:
        lines.append("- rationale: Phase 0 gate is open and the fractional scan already satisfies the shared schema.")
    elif ready:
        lines.append("- rationale: Phase 0 gate is open and the integer-proxy schema is reusable.")
    else:
        lines.append("- rationale: Phase 0 gate is still closed or schema validation failed.")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare MC reference and strong-coupling scan outputs.")
    parser.add_argument(
        "--reference",
        type=Path,
        default=RESULTS_DIR / "phase0_reference.json",
        help="Reference JSON path.",
    )
    parser.add_argument(
        "--scan",
        type=Path,
        default=RESULTS_DIR / "phase1_scan.csv",
        help="Scan CSV path. Accepts integer_proxy and fractional_proxy surfaces.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=RESULTS_DIR / "phase1_analysis.md",
        help="Markdown analysis output.",
    )
    parser.add_argument(
        "--reduction",
        type=Path,
        default=RESULTS_DIR / "phase2_gamma_reduction.csv",
        help="Optional gamma reduction CSV for fractional scans.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    issues: list[str] = []

    if not args.reference.exists():
        issues.append(f"reference file not found: {args.reference}")
        reference = None
        reference_missing = ["file_missing"]
    else:
        reference, reference_missing = read_reference(args.reference)
        if reference_missing:
            issues.append(f"reference schema incomplete: {reference_missing}")
        elif not bool(reference["pass"]):
            pass_breakdown = reference["diagnostics"].get("pass_breakdown", {})
            failed_reference_checks = [name for name, payload in pass_breakdown.items() if not bool(payload.get("pass"))]
            if failed_reference_checks:
                issues.append(f"reference gate blocked: {', '.join(failed_reference_checks)}")
            else:
                issues.append("reference gate blocked: pass=false")

    if not args.scan.exists():
        issues.append(f"scan file not found: {args.scan}")
        scan_rows: list[dict[str, str]] = []
        scan_missing = ["file_missing"]
    else:
        scan_rows, scan_missing = validate_scan_csv(args.scan)
        if scan_missing:
            issues.append(f"scan schema incomplete: {scan_missing}")
        else:
            for issue in scan_sanity_issues(scan_rows):
                issues.append(f"scan sanity issue: {issue}")

    if reference is not None and not reference_missing and scan_rows and not scan_missing:
        scan_dimension_modes = {row["dimension_mode"] for row in scan_rows}
        if len(scan_dimension_modes) != 1:
            issues.append(f"scan dimension_mode must be unique, got {sorted(scan_dimension_modes)}")
        else:
            scan_dimension_mode = next(iter(scan_dimension_modes))
            if scan_dimension_mode not in {DIMENSION_MODE_INTEGER, DIMENSION_MODE_FRACTIONAL}:
                issues.append(f"unexpected scan dimension_mode: {scan_dimension_mode}")
        if str(reference["dimension_mode"]) != DIMENSION_MODE_INTEGER:
            issues.append(f"unexpected reference dimension_mode: {reference['dimension_mode']}")

    if args.reduction.exists():
        reduction_rows, reduction_missing = read_reduction(args.reduction)
        if reduction_missing:
            issues.append(f"reduction schema incomplete: {reduction_missing}")
    else:
        reduction_rows = []
        reduction_missing = ["file_missing"] if scan_rows and any(row["dimension_mode"] == DIMENSION_MODE_FRACTIONAL for row in scan_rows) else []

    markdown = build_markdown(
        reference,
        reference_missing,
        scan_rows,
        scan_missing,
        reduction_rows,
        reduction_missing,
        issues,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(markdown, encoding="utf-8")
    print(f"Wrote analysis report to {args.out}")
    if issues:
        sys.exit(1)


if __name__ == "__main__":
    main()
