#!/usr/bin/env python3
"""
Acceptance surface for the fractional proxy.

This script removes one specific ambiguity: calibration and production scan must
use the same size ladder, sample budget, and seed surface. That way, a failed
gamma gate can be attributed to the proxy/reduction itself rather than to a
budget mismatch between calibration and scan.
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
    RESULTS_DIR,
    csv_write,
    json_dump,
    parse_float_list,
    parse_int_list,
    scan_sanity_issues,
    validate_scan_csv,
)
from strong_coupling_compare import build_markdown, read_reference, read_reduction
from strong_coupling_fractional_calibration import build_rows as build_calibration_rows
from strong_coupling_fractional_proxy import build_scan_rows
from strong_coupling_gamma_reduction import build_reduction_rows


def row_float(row: dict[str, object], key: str, default: float = float("inf")) -> float:
    raw = row.get(key, "")
    if raw in {"", None}:
        return default
    return float(raw)


def row_bool(row: dict[str, object], key: str) -> bool:
    return str(row.get(key, "False")) == "True"


def is_de2_calibrated(row: dict[str, object]) -> bool:
    return str(row.get("status_de2", "")) == "calibrated"


def is_foothold_candidate(row: dict[str, object]) -> bool:
    spike_ratio = row_float(row, "susceptibility_spike_ratio")
    return bool(
        is_de2_calibrated(row)
        and row_bool(row, "xi_window_pass")
        and row_bool(row, "split_stability_pass")
        and np.isfinite(spike_ratio)
        and spike_ratio <= 4.0
    )


def build_coupling_id(formal_n: float, mass_like: float, lambda_like: float) -> str:
    return f"n{formal_n:.2f}_m{mass_like:.3f}_lam{lambda_like:.3f}"


def selected_row_rank(row: dict[str, object]) -> tuple[int, int, int, float, float, float]:
    stable = is_foothold_candidate(row)
    status_de2 = str(row.get("status_de2", ""))
    status_lpa = str(row.get("status_lpa", ""))
    eta_proxy = row_float(row, "eta_proxy")
    score_de2 = row_float(row, "score_de2")
    spike = row_float(row, "susceptibility_spike_ratio")

    if status_de2 == "calibrated":
        status_rank = 0
    elif status_lpa == "calibrated":
        status_rank = 1
    elif np.isfinite(eta_proxy) and eta_proxy > 0.0:
        status_rank = 2
    else:
        status_rank = 3

    return (
        0 if stable else 1,
        status_rank,
        0 if row_bool(row, "xi_window_pass") else 1,
        spike if np.isfinite(spike) else float("inf"),
        score_de2 if np.isfinite(score_de2) else float("inf"),
        abs(eta_proxy) if np.isfinite(eta_proxy) else float("inf"),
    )


def detect_calibrated_components(calibration_rows: list[dict[str, object]]) -> dict[str, object]:
    grouped_all: dict[str, list[dict[str, object]]] = {}
    grouped: dict[str, list[dict[str, object]]] = {}
    for row in calibration_rows:
        grouped_all.setdefault(str(row["formal_n"]), []).append(row)
        if not is_foothold_candidate(row):
            continue
        grouped.setdefault(str(row["formal_n"]), []).append(row)

    best_component_rows: list[dict[str, object]] = []
    best_formal_n: str | None = None
    per_formal_n: dict[str, dict[str, object]] = {}

    for formal_n, rows in grouped.items():
        all_rows = grouped_all[formal_n]
        mass_values = sorted({float(row["mass_like"]) for row in all_rows})
        lambda_values = sorted({float(row["lambda_like"]) for row in all_rows})
        mass_index = {value: idx for idx, value in enumerate(mass_values)}
        lambda_index = {value: idx for idx, value in enumerate(lambda_values)}
        lattice: dict[tuple[int, int], dict[str, object]] = {}
        for row in rows:
            lattice[(mass_index[float(row["mass_like"])], lambda_index[float(row["lambda_like"])])] = row

        seen: set[tuple[int, int]] = set()
        components: list[list[dict[str, object]]] = []
        for coord in lattice:
            if coord in seen:
                continue
            stack = [coord]
            seen.add(coord)
            component: list[dict[str, object]] = []
            while stack:
                current = stack.pop()
                component.append(lattice[current])
                x_idx, y_idx = current
                for neighbor in (
                    (x_idx - 1, y_idx),
                    (x_idx + 1, y_idx),
                    (x_idx, y_idx - 1),
                    (x_idx, y_idx + 1),
                ):
                    if neighbor in lattice and neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            component.sort(key=lambda row: (float(row["mass_like"]), float(row["lambda_like"])))
            components.append(component)

        components.sort(
            key=lambda component: (
                -len(component),
                min(row_float(row, "score_de2") for row in component),
                np.mean([row_float(row, "susceptibility_spike_ratio") for row in component]),
            )
        )
        if not components:
            continue

        selected = components[0]
        component_payload = {
            "largest_component_size": len(selected),
            "selected_component_couplings": [
                build_coupling_id(float(formal_n), float(row["mass_like"]), float(row["lambda_like"]))
                for row in selected
            ],
            "selected_component_rows": [
                {
                    "mass_like": float(row["mass_like"]),
                    "lambda_like": float(row["lambda_like"]),
                    "score_de2": row_float(row, "score_de2"),
                    "susceptibility_spike_ratio": row_float(row, "susceptibility_spike_ratio"),
                }
                for row in selected
            ],
        }
        per_formal_n[formal_n] = component_payload

        if (
            len(selected) > len(best_component_rows)
            or (
                len(selected) == len(best_component_rows)
                and selected
                and best_component_rows
                and min(row_float(row, "score_de2") for row in selected)
                < min(row_float(row, "score_de2") for row in best_component_rows)
            )
        ):
            best_component_rows = selected
            best_formal_n = formal_n

    selected_component_couplings = (
        [
            build_coupling_id(best_formal_n and float(best_formal_n) or 0.0, float(row["mass_like"]), float(row["lambda_like"]))
            for row in best_component_rows
        ]
        if best_component_rows and best_formal_n is not None
        else []
    )
    largest_component_size = len(best_component_rows)
    local_foothold = largest_component_size >= 3
    blocking_reason = "none" if local_foothold else "Metropolis-family exhausted"

    return {
        "largest_calibrated_component_size": largest_component_size,
        "selected_component_couplings": selected_component_couplings,
        "selected_component_formal_n": best_formal_n,
        "local_foothold": local_foothold,
        "blocking_reason": blocking_reason,
        "per_formal_n": per_formal_n,
    }


def select_schedule_rows(
    calibration_rows: list[dict[str, object]],
    formal_ns: list[float],
) -> tuple[dict[str, dict[str, float]], dict[str, dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for row in calibration_rows:
        grouped.setdefault(str(row["formal_n"]), []).append(row)

    schedule_map: dict[str, dict[str, float]] = {}
    selected_manifest: dict[str, dict[str, object]] = {}
    missing: list[str] = []
    for formal_n in formal_ns:
        key = f"{formal_n:.6f}"
        candidates = grouped.get(key, [])
        if not candidates:
            missing.append(key)
            continue
        best = min(candidates, key=selected_row_rank)
        schedule_map[key] = {
            "mass_like": float(best["mass_like"]),
            "lambda_like": float(best["lambda_like"]),
        }
        selected_manifest[key] = {
            "mass_like": float(best["mass_like"]),
            "lambda_like": float(best["lambda_like"]),
            "eta_proxy": row_float(best, "eta_proxy"),
            "eta_anchor_de2": row_float(best, "eta_anchor_de2"),
            "score_de2": row_float(best, "score_de2"),
            "status_de2": str(best["status_de2"]),
            "status_lpa": str(best["status_lpa"]),
            "xi_window_pass": row_bool(best, "xi_window_pass"),
            "susceptibility_values": str(best["susceptibility_values"]),
            "xi_values": str(best["xi_values"]),
            "susceptibility_spike_ratio": row_float(best, "susceptibility_spike_ratio"),
            "split_stability_pass": row_bool(best, "split_stability_pass"),
            "acceptance_by_L": str(best["acceptance_by_L"]),
            "proposal_scale_final_by_L": str(best["proposal_scale_final_by_L"]),
            "stability_gate_pass": row_bool(best, "stability_gate_pass"),
        }
    if missing:
        raise SystemExit(f"missing calibration rows for formal_n={missing}")
    return schedule_map, selected_manifest


def build_issues(
    reference_path: Path,
    scan_path: Path,
    reduction_path: Path,
) -> tuple[dict[str, object] | None, list[str], list[dict[str, str]], list[str], list[dict[str, str]], list[str], list[str]]:
    issues: list[str] = []

    if not reference_path.exists():
        reference = None
        reference_missing = ["file_missing"]
        issues.append(f"reference file not found: {reference_path}")
    else:
        reference, reference_missing = read_reference(reference_path)
        if reference_missing:
            issues.append(f"reference schema incomplete: {reference_missing}")
        elif not bool(reference["pass"]):
            pass_breakdown = reference["diagnostics"].get("pass_breakdown", {})
            failed_reference_checks = [name for name, payload in pass_breakdown.items() if not bool(payload.get("pass"))]
            if failed_reference_checks:
                issues.append(f"reference gate blocked: {', '.join(failed_reference_checks)}")
            else:
                issues.append("reference gate blocked: pass=false")

    scan_rows, scan_missing = validate_scan_csv(scan_path)
    if scan_missing:
        issues.append(f"scan schema incomplete: {scan_missing}")
    else:
        issues.extend(f"scan sanity issue: {issue}" for issue in scan_sanity_issues(scan_rows))

    reduction_rows, reduction_missing = read_reduction(reduction_path)
    if reduction_missing:
        issues.append(f"reduction schema incomplete: {reduction_missing}")

    return reference, reference_missing, scan_rows, scan_missing, reduction_rows, reduction_missing, issues


def build_acceptance_appendix(component_summary: dict[str, object]) -> str:
    couplings = component_summary["selected_component_couplings"]
    couplings_text = ", ".join(couplings) if couplings else "none"
    return "\n".join(
        [
            "",
            "## Local Foothold",
            f"- largest_calibrated_component_size: {component_summary['largest_calibrated_component_size']}",
            f"- selected_component_formal_n: {component_summary['selected_component_formal_n'] or 'none'}",
            f"- selected_component_couplings: {couplings_text}",
            f"- local_foothold: {component_summary['local_foothold']}",
            f"- blocking_reason: {component_summary['blocking_reason']}",
        ]
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run fractional calibration and production scan on one shared acceptance surface.")
    parser.add_argument("--L", default="6,8,10,12", help="Comma-separated lattice sizes shared by calibration and production scan.")
    parser.add_argument("--formal-n", default="2.78", help="Comma-separated formal n values.")
    parser.add_argument("--mass-like", default="0.90,0.95,1.00,1.05,1.10", help="Comma-separated calibration mass-like values.")
    parser.add_argument("--lambda-like", default="1.00,1.05,1.10,1.15,1.20", help="Comma-separated calibration lambda-like values.")
    parser.add_argument("--warmup", type=int, default=120, help="Warmup sweeps shared by calibration and production scan.")
    parser.add_argument("--measure", type=int, default=240, help="Measured sweeps shared by calibration and production scan.")
    parser.add_argument("--seed", type=int, default=171, help="Base RNG seed shared by calibration and production scan.")
    parser.add_argument("--proposal-scale", type=float, default=0.65, help="Proposal scale.")
    parser.add_argument("--block-size", type=int, default=8, help="Bootstrap block size.")
    parser.add_argument("--proxy-kind", choices=["t_projected_fractional_embedding", "t_projected_direct"], default="t_projected_direct")
    parser.add_argument("--reference", type=Path, default=RESULTS_DIR / "phase0_reference.json", help="Phase 0 reference JSON path.")
    parser.add_argument("--calibration-out", type=Path, default=RESULTS_DIR / "phase2_fractional_acceptance_calibration.csv", help="Acceptance calibration CSV.")
    parser.add_argument("--schedule-out", type=Path, default=RESULTS_DIR / "phase2_fractional_acceptance_schedule.json", help="Selected per-n schedule JSON.")
    parser.add_argument("--manifest-out", type=Path, default=RESULTS_DIR / "phase2_fractional_acceptance_manifest.json", help="Acceptance manifest JSON.")
    parser.add_argument("--scan-out", type=Path, default=RESULTS_DIR / "phase2_fractional_acceptance_scan.csv", help="Acceptance scan CSV.")
    parser.add_argument("--reduction-out", type=Path, default=RESULTS_DIR / "phase2_fractional_acceptance_reduction.csv", help="Acceptance reduction CSV.")
    parser.add_argument("--analysis-out", type=Path, default=RESULTS_DIR / "phase2_fractional_acceptance_analysis.md", help="Acceptance analysis Markdown.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    sizes = parse_int_list(args.L)
    formal_ns = parse_float_list(args.formal_n)
    mass_likes = parse_float_list(args.mass_like)
    lambda_likes = parse_float_list(args.lambda_like)

    calibration_rows = build_calibration_rows(
        sizes=sizes,
        formal_ns=formal_ns,
        mass_likes=mass_likes,
        lambda_likes=lambda_likes,
        t_regulators=[0.0],
        warmup=args.warmup,
        measure=args.measure,
        seed=args.seed,
        proposal_scale=args.proposal_scale,
        block_size=args.block_size,
        proxy_kind=args.proxy_kind,
    )
    csv_write(calibration_rows, args.calibration_out)

    component_summary = detect_calibrated_components(calibration_rows)
    schedule_map, selected_manifest = select_schedule_rows(calibration_rows, formal_ns)
    json_dump(schedule_map, args.schedule_out)
    json_dump(
        {
            "sizes": sizes,
            "formal_n": formal_ns,
            "mass_like_grid": mass_likes,
            "lambda_like_grid": lambda_likes,
            "warmup": args.warmup,
            "measure": args.measure,
            "seed": args.seed,
            "proposal_scale": args.proposal_scale,
            "block_size": args.block_size,
            "proxy_kind": args.proxy_kind,
            "selected_rows": selected_manifest,
            "largest_calibrated_component_size": component_summary["largest_calibrated_component_size"],
            "selected_component_couplings": component_summary["selected_component_couplings"],
            "local_foothold": component_summary["local_foothold"],
            "blocking_reason": component_summary["blocking_reason"],
            "component_summary": component_summary,
        },
        args.manifest_out,
    )

    scan_rows = build_scan_rows(
        sizes=sizes,
        formal_ns=formal_ns,
        mass_likes=mass_likes,
        lambda_likes=lambda_likes,
        warmup=args.warmup,
        measure=args.measure,
        seed=args.seed,
        proposal_scale=args.proposal_scale,
        block_size=args.block_size,
        t_regulator=0.0,
        proxy_kind=args.proxy_kind,
        schedule_mode="per_n",
        schedule_path=args.schedule_out,
    )
    csv_write(scan_rows, args.scan_out)

    reduction_rows = build_reduction_rows([{key: str(value) for key, value in row.items()} for row in scan_rows])
    csv_write(reduction_rows, args.reduction_out)

    reference, reference_missing, scan_rows_csv, scan_missing, reduction_rows_csv, reduction_missing, issues = build_issues(
        reference_path=args.reference,
        scan_path=args.scan_out,
        reduction_path=args.reduction_out,
    )
    markdown = build_markdown(
        reference=reference,
        reference_missing=reference_missing,
        scan_rows=scan_rows_csv,
        scan_missing=scan_missing,
        reduction_rows=reduction_rows_csv,
        reduction_missing=reduction_missing,
        issues=issues,
    )
    markdown += build_acceptance_appendix(component_summary) + "\n"
    args.analysis_out.write_text(markdown, encoding="utf-8")

    calibrated = sum(1 for row in reduction_rows_csv if row["status_de2"] == "calibrated" or row["status_lpa"] == "calibrated")
    print(f"Wrote acceptance calibration to {args.calibration_out}")
    print(f"Wrote acceptance schedule to {args.schedule_out}")
    print(f"Wrote acceptance scan to {args.scan_out}")
    print(f"Wrote acceptance reduction to {args.reduction_out}")
    print(f"Wrote acceptance analysis to {args.analysis_out}")
    print(f"selected_rows={len(selected_manifest)} calibrated_rows={calibrated}/{len(reduction_rows_csv)}")
    print(
        "largest_calibrated_component_size="
        f"{component_summary['largest_calibrated_component_size']} local_foothold={component_summary['local_foothold']}"
    )


if __name__ == "__main__":
    main()
