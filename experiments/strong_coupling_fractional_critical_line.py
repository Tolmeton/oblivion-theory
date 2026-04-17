#!/usr/bin/env python3
"""
Pseudo-critical line search for the fractional direct proxy.

This stage separates "chain is stable" from "we are measuring on the critical
surface". It scans a focused coupling grid, detects size crossings of xi/L and
Binder along the mass axis for each lambda slice, and only then reduces eta on
the selected pseudo-critical line.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from strong_coupling_common import RESULTS_DIR, csv_write, json_dump, parse_float_list, parse_int_list
from strong_coupling_compare import read_reference
from strong_coupling_fractional_proxy import build_scan_rows
from strong_coupling_gamma_reduction import build_reduction_rows


def row_float(row: dict[str, object], key: str, default: float = float("nan")) -> float:
    raw = row.get(key, "")
    if raw in {"", None}:
        return default
    return float(raw)


def coupling_id(formal_n: float, mass_like: float, lambda_like: float) -> str:
    return f"n{formal_n:.2f}_m{mass_like:.3f}_lam{lambda_like:.3f}"


def adjacent_pairs(sizes: list[int]) -> list[tuple[int, int]]:
    return list(zip(sizes, sizes[1:]))


def interpolate_zero(mass_lo: float, delta_lo: float, mass_hi: float, delta_hi: float) -> float:
    if delta_hi == delta_lo:
        return 0.5 * (mass_lo + mass_hi)
    weight = -delta_lo / (delta_hi - delta_lo)
    return float(mass_lo + weight * (mass_hi - mass_lo))


def summarize_scan_rows(scan_rows: list[dict[str, object]]) -> dict[tuple[float, float, int], dict[str, float | str]]:
    summary: dict[tuple[float, float, int], dict[str, float | str]] = {}
    for row in scan_rows:
        mass_like = row_float(row, "mass_like")
        lambda_like = row_float(row, "lambda_like")
        size = int(row["L"])
        key = (mass_like, lambda_like, size)
        payload = summary.setdefault(
            key,
            {
                "coupling_id": str(row["coupling_id"]),
                "seed": row_float(row, "seed"),
                "proposal_scale_final": row_float(row, "proposal_scale_final"),
            },
        )
        payload[str(row["observable"])] = row_float(row, "mean")
    return summary


def detect_crossing_records(
    summary: dict[tuple[float, float, int], dict[str, float | str]],
    formal_n: float,
    mass_likes: list[float],
    lambda_likes: list[float],
    sizes: list[int],
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for lambda_like in lambda_likes:
        for observable in ("xi_over_L", "binder"):
            for size_lo, size_hi in adjacent_pairs(sizes):
                previous: tuple[float, float] | None = None
                for mass_like in sorted(mass_likes):
                    low_payload = summary.get((mass_like, lambda_like, size_lo))
                    high_payload = summary.get((mass_like, lambda_like, size_hi))
                    if low_payload is None or high_payload is None:
                        previous = None
                        continue
                    delta = float(low_payload.get(observable, np.nan)) - float(high_payload.get(observable, np.nan))
                    if not np.isfinite(delta):
                        previous = None
                        continue
                    if previous is not None:
                        mass_prev, delta_prev = previous
                        if delta_prev == 0.0 or delta == 0.0 or delta_prev * delta < 0.0:
                            records.append(
                                {
                                    "formal_n": f"{formal_n:.6f}",
                                    "lambda_like": f"{lambda_like:.6f}",
                                    "observable": observable,
                                    "size_pair": f"{size_lo}-{size_hi}",
                                    "mass_lo": f"{mass_prev:.6f}",
                                    "mass_hi": f"{mass_like:.6f}",
                                    "delta_lo": f"{delta_prev:.10f}",
                                    "delta_hi": f"{delta:.10f}",
                                    "crossing_mass": f"{interpolate_zero(mass_prev, delta_prev, mass_like, delta):.10f}",
                                }
                            )
                    previous = (mass_like, delta)
    return records


def build_line_candidates(
    summary: dict[tuple[float, float, int], dict[str, float | str]],
    crossing_records: list[dict[str, object]],
    formal_n: float,
    mass_likes: list[float],
    lambda_likes: list[float],
    sizes: list[int],
) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for record in crossing_records:
        grouped.setdefault(str(record["lambda_like"]), []).append(record)

    candidates: list[dict[str, object]] = []
    for lambda_like in lambda_likes:
        key = f"{lambda_like:.6f}"
        records = grouped.get(key, [])
        if records:
            crossing_masses = np.array([float(record["crossing_mass"]) for record in records], dtype=np.float64)
            mean_mass = float(np.mean(crossing_masses))
            scatter = float(np.std(crossing_masses))
            selected_mass = min(mass_likes, key=lambda mass_like: abs(mass_like - mean_mass))
            selected_id = coupling_id(formal_n, selected_mass, lambda_like)
            support = len(records)
            supported_observables = sorted({str(record["observable"]) for record in records})
            supported_pairs = sorted({str(record["size_pair"]) for record in records})
            binder_values = []
            xi_values = []
            susceptibility_values = []
            seeds = []
            for size in sizes:
                payload = summary[(selected_mass, lambda_like, size)]
                binder_values.append(float(payload["binder"]))
                xi_values.append(float(payload["xi_over_L"]))
                susceptibility_values.append(float(payload["susceptibility"]))
                seeds.append(int(payload["seed"]))
            candidates.append(
                {
                    "formal_n": f"{formal_n:.6f}",
                    "lambda_like": f"{lambda_like:.6f}",
                    "crossing_support": support,
                    "observables_supported": "|".join(supported_observables),
                    "size_pairs_supported": "|".join(supported_pairs),
                    "mean_crossing_mass": f"{mean_mass:.10f}",
                    "crossing_mass_scatter": f"{scatter:.10f}",
                    "selected_mass_like": f"{selected_mass:.6f}",
                    "selected_coupling_id": selected_id,
                    "binder_values": "|".join(f"{value:.10f}" for value in binder_values),
                    "xi_values": "|".join(f"{value:.10f}" for value in xi_values),
                    "susceptibility_values": "|".join(f"{value:.10f}" for value in susceptibility_values),
                    "run_seeds": "|".join(str(seed) for seed in seeds),
                }
            )
        else:
            candidates.append(
                {
                    "formal_n": f"{formal_n:.6f}",
                    "lambda_like": f"{lambda_like:.6f}",
                    "crossing_support": 0,
                    "observables_supported": "",
                    "size_pairs_supported": "",
                    "mean_crossing_mass": "",
                    "crossing_mass_scatter": "",
                    "selected_mass_like": "",
                    "selected_coupling_id": "",
                    "binder_values": "",
                    "xi_values": "",
                    "susceptibility_values": "",
                    "run_seeds": "",
                }
            )

    candidates.sort(
        key=lambda row: (
            -int(row["crossing_support"]),
            row_float(row, "crossing_mass_scatter", default=float("inf")),
            row_float(row, "lambda_like", default=float("inf")),
        )
    )
    return candidates


def schedule_from_candidates(candidates: list[dict[str, object]]) -> dict[str, list[dict[str, float]]]:
    schedule: list[dict[str, float]] = []
    for row in candidates:
        if int(row["crossing_support"]) <= 0:
            continue
        schedule.append(
            {
                "mass_like": float(row["selected_mass_like"]),
                "lambda_like": float(row["lambda_like"]),
            }
        )
    if not candidates:
        return {}
    formal_n = str(candidates[0]["formal_n"])
    return {formal_n: schedule}


def filter_scan_rows(scan_rows: list[dict[str, object]], coupling_ids: set[str]) -> list[dict[str, object]]:
    return [row for row in scan_rows if str(row["coupling_id"]) in coupling_ids]


def build_analysis(
    reference_path: Path,
    formal_n: float,
    sizes: list[int],
    mass_likes: list[float],
    lambda_likes: list[float],
    crossing_records: list[dict[str, object]],
    candidates: list[dict[str, object]],
    selected_scan_rows: list[dict[str, object]],
    reduction_rows: list[dict[str, object]],
) -> str:
    lines = [
        "# Fractional Critical-Line Analysis",
        "",
        "## Setup",
        f"- formal_n: {formal_n:.6f}",
        f"- sizes: {sizes}",
        f"- mass_like grid: {mass_likes}",
        f"- lambda_like grid: {lambda_likes}",
        f"- crossing_records: {len(crossing_records)}",
    ]

    if reference_path.exists():
        reference, missing = read_reference(reference_path)
        if not missing:
            lines.append(f"- phase0_reference_pass: {bool(reference['pass'])}")

    lines.extend(
        [
            "",
            "## Crossing Candidates",
            "| lambda_like | support | observables | size_pairs | mean_crossing_mass | scatter | selected_mass_like | selected_coupling_id |",
            "|:---:|---:|:---|:---|---:|---:|---:|:---|",
        ]
    )
    for row in candidates:
        support = int(row["crossing_support"])
        lines.append(
            f"| {float(row['lambda_like']):.2f} | {support} | {row['observables_supported'] or '--'} "
            f"| {row['size_pairs_supported'] or '--'} | {row['mean_crossing_mass'] or '--'} "
            f"| {row['crossing_mass_scatter'] or '--'} | {row['selected_mass_like'] or '--'} "
            f"| {row['selected_coupling_id'] or '--'} |"
        )

    selected_ids = sorted({str(row["selected_coupling_id"]) for row in candidates if row["selected_coupling_id"]})
    lines.extend(
        [
            "",
            "## Selected Line",
            f"- selected_couplings: {selected_ids or 'none'}",
            f"- selected_scan_rows: {len(selected_scan_rows)}",
        ]
    )

    if reduction_rows:
        lines.extend(
            [
                "",
                "## Eta On Pseudo-critical Line",
                "| coupling_id | estimator | source | sizes | eta_proxy | DE2 status | DE2 γ proxy | LPA' status |",
                "|:---|:---|:---|:---|---:|:---|---:|:---|",
            ]
        )
        calibrated = 0
        for row in reduction_rows:
            if str(row["status_de2"]) == "calibrated" or str(row["status_lpa"]) == "calibrated":
                calibrated += 1
            lines.append(
                f"| {row['coupling_id']} | {row['eta_estimator']} | {row['source_observable']} "
                f"| {row['sizes']} | {row['eta_proxy']} | {row['status_de2']} "
                f"| {row['gamma_phi_proxy_de2'] or '--'} | {row['status_lpa']} |"
            )
        lines.append(f"- calibrated_rows: {calibrated} / {len(reduction_rows)}")
    else:
        lines.extend(
            [
                "",
                "## Eta On Pseudo-critical Line",
                "- no bracketted crossings were found inside the current coupling window, so no pseudo-critical line scan was selected.",
            ]
        )

    if selected_ids:
        lines.append("- interpretation: current window contains crossing-supported couplings, but they still may miss the FRG anchor band.")
    else:
        lines.append("- interpretation: current coupling window does not bracket a pseudo-critical line; the next move is to widen or shift the mass/lambda window before reading eta.")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search a pseudo-critical line in the fractional direct proxy before eta reduction.")
    parser.add_argument("--L", default="6,8,10,12", help="Comma-separated lattice sizes.")
    parser.add_argument("--formal-n", type=float, default=2.78, help="Single formal n value.")
    parser.add_argument("--mass-like", default="0.90,0.95,1.00,1.05,1.10", help="Comma-separated mass-like values.")
    parser.add_argument("--lambda-like", default="1.00,1.05,1.10,1.15,1.20", help="Comma-separated lambda-like values.")
    parser.add_argument("--warmup", type=int, default=120, help="Warmup sweeps.")
    parser.add_argument("--measure", type=int, default=240, help="Measured sweeps.")
    parser.add_argument("--seed", type=int, default=171, help="Base RNG seed.")
    parser.add_argument("--proposal-scale", type=float, default=0.65, help="Proposal scale.")
    parser.add_argument("--block-size", type=int, default=8, help="Block size.")
    parser.add_argument("--proxy-kind", choices=["t_projected_fractional_embedding", "t_projected_direct"], default="t_projected_direct")
    parser.add_argument("--reference", type=Path, default=RESULTS_DIR / "phase0_reference.json", help="Phase 0 reference JSON.")
    parser.add_argument("--grid-scan-out", type=Path, default=RESULTS_DIR / "phase3_fractional_critical_grid_scan.csv", help="Full focused-grid scan CSV.")
    parser.add_argument("--crossings-out", type=Path, default=RESULTS_DIR / "phase3_fractional_critical_crossings.csv", help="Crossing records CSV.")
    parser.add_argument("--candidates-out", type=Path, default=RESULTS_DIR / "phase3_fractional_critical_candidates.csv", help="Crossing candidates CSV.")
    parser.add_argument("--schedule-out", type=Path, default=RESULTS_DIR / "phase3_fractional_critical_line_schedule.json", help="Selected line schedule JSON.")
    parser.add_argument("--scan-out", type=Path, default=RESULTS_DIR / "phase3_fractional_critical_line_scan.csv", help="Selected line scan CSV.")
    parser.add_argument("--reduction-out", type=Path, default=RESULTS_DIR / "phase3_fractional_critical_line_reduction.csv", help="Selected line reduction CSV.")
    parser.add_argument("--analysis-out", type=Path, default=RESULTS_DIR / "phase3_fractional_critical_line_analysis.md", help="Critical-line analysis Markdown.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    sizes = parse_int_list(args.L)
    mass_likes = parse_float_list(args.mass_like)
    lambda_likes = parse_float_list(args.lambda_like)
    formal_n = float(args.formal_n)

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
        proxy_kind=args.proxy_kind,
        schedule_mode="shared",
        schedule_path=None,
    )
    csv_write(grid_scan_rows, args.grid_scan_out)

    summary = summarize_scan_rows(grid_scan_rows)
    crossing_records = detect_crossing_records(summary, formal_n, mass_likes, lambda_likes, sizes)
    csv_write(crossing_records, args.crossings_out)

    candidates = build_line_candidates(summary, crossing_records, formal_n, mass_likes, lambda_likes, sizes)
    csv_write(candidates, args.candidates_out)

    schedule = schedule_from_candidates(candidates)
    json_dump(schedule, args.schedule_out)

    selected_ids = {str(row["selected_coupling_id"]) for row in candidates if row["selected_coupling_id"]}
    selected_scan_rows = filter_scan_rows(grid_scan_rows, selected_ids)
    csv_write(selected_scan_rows, args.scan_out)

    reduction_rows: list[dict[str, object]] = []
    if selected_scan_rows:
        reduction_rows = build_reduction_rows([{key: str(value) for key, value in row.items()} for row in selected_scan_rows])
        csv_write(reduction_rows, args.reduction_out)
    else:
        args.reduction_out.write_text("", encoding="utf-8")

    analysis = build_analysis(
        reference_path=args.reference,
        formal_n=formal_n,
        sizes=sizes,
        mass_likes=mass_likes,
        lambda_likes=lambda_likes,
        crossing_records=crossing_records,
        candidates=candidates,
        selected_scan_rows=selected_scan_rows,
        reduction_rows=reduction_rows,
    )
    args.analysis_out.write_text(analysis, encoding="utf-8")

    print(f"Wrote focused grid scan to {args.grid_scan_out}")
    print(f"Wrote crossing records to {args.crossings_out}")
    print(f"Wrote line candidates to {args.candidates_out}")
    print(f"Wrote selected line schedule to {args.schedule_out}")
    print(f"Wrote selected line scan to {args.scan_out}")
    print(f"Wrote selected line reduction to {args.reduction_out}")
    print(f"Wrote analysis to {args.analysis_out}")
    print(f"selected_couplings={len(selected_ids)} crossing_records={len(crossing_records)}")


if __name__ == "__main__":
    main()
