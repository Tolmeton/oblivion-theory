#!/usr/bin/env python3
"""
H3/H4 topology and critical-surface probe for the fractional proxy.

This stage keeps the existing gamma reduction and metrology layers fixed. It
varies only the proxy topology and the rule used to select a pseudo-critical
surface, so failures can be assigned before changing the observable reduction.
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

from strong_coupling_common import RESULTS_DIR, csv_write, parse_int_list
from strong_coupling_fractional_critical_line import (
    build_line_candidates,
    detect_crossing_records,
    filter_scan_rows,
    row_float,
    summarize_scan_rows,
)
from strong_coupling_fractional_metrology import build_transfer_rows
from strong_coupling_fractional_proxy import build_scan_rows
from strong_coupling_gamma_reduction import build_reduction_rows


PROXY_DIRECT = "t_projected_direct"
PROXY_EMBEDDING = "t_projected_fractional_embedding"
SURFACE_CROSSING = "crossing"
SURFACE_RG_INVARIANT = "rg_invariant"

DEFAULT_TOPOLOGY_WINDOWS = {
    PROXY_DIRECT: {
        "mass_like": [0.90, 0.95, 1.00, 1.05, 1.10],
        "lambda_like": [1.00, 1.05, 1.10, 1.15, 1.20],
    },
    PROXY_EMBEDDING: {
        "mass_like": [8.0, 10.0, 12.0, 14.0],
        "lambda_like": [0.50, 1.00, 1.50, 2.00],
    },
}


def parse_choice_list(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def proxy_label(proxy_kind: str) -> str:
    if proxy_kind == PROXY_DIRECT:
        return "direct"
    if proxy_kind == PROXY_EMBEDDING:
        return "embedding"
    return proxy_kind.replace("t_projected_", "")


def formal_key(formal_n: float) -> str:
    return f"{formal_n:.6f}"


def load_windows(path: Path | None) -> dict[str, dict[str, list[float]]]:
    if path is None:
        return DEFAULT_TOPOLOGY_WINDOWS
    payload = json.loads(path.read_text(encoding="utf-8"))
    windows: dict[str, dict[str, list[float]]] = {}
    for proxy_kind, value in payload.items():
        windows[proxy_kind] = {
            "mass_like": [float(item) for item in value["mass_like"]],
            "lambda_like": [float(item) for item in value["lambda_like"]],
        }
    return windows


def coupling_surface_id(formal_n: float, proxy_kind: str, surface_selector: str) -> str:
    return f"n{formal_n:.2f}_{proxy_label(proxy_kind)}_{surface_selector}"


def build_rg_invariant_candidates(
    summary: dict[tuple[float, float, int], dict[str, float | str]],
    formal_n: float,
    mass_likes: list[float],
    lambda_likes: list[float],
    sizes: list[int],
) -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for lambda_like in lambda_likes:
        best: dict[str, object] | None = None
        for mass_like in mass_likes:
            payloads = [summary.get((mass_like, lambda_like, size)) for size in sizes]
            if any(payload is None for payload in payloads):
                continue
            binder_values = np.array([float(payload["binder"]) for payload in payloads if payload is not None], dtype=np.float64)
            xi_values = np.array([float(payload["xi_over_L"]) for payload in payloads if payload is not None], dtype=np.float64)
            susceptibility_values = np.array([float(payload["susceptibility"]) for payload in payloads if payload is not None], dtype=np.float64)
            if not (np.all(np.isfinite(binder_values)) and np.all(np.isfinite(xi_values))):
                continue
            invariant_score = float(np.std(binder_values) + np.std(xi_values))
            xi_span = float(np.max(xi_values) - np.min(xi_values))
            binder_span = float(np.max(binder_values) - np.min(binder_values))
            row = {
                "formal_n": f"{formal_n:.6f}",
                "lambda_like": f"{lambda_like:.6f}",
                "surface_selector": SURFACE_RG_INVARIANT,
                "crossing_support": 0,
                "invariant_support": len(sizes),
                "invariant_score": f"{invariant_score:.10f}",
                "xi_span": f"{xi_span:.10f}",
                "binder_span": f"{binder_span:.10f}",
                "selected_mass_like": f"{mass_like:.6f}",
                "selected_coupling_id": f"n{formal_n:.2f}_m{mass_like:.3f}_lam{lambda_like:.3f}",
                "binder_values": "|".join(f"{value:.10f}" for value in binder_values),
                "xi_values": "|".join(f"{value:.10f}" for value in xi_values),
                "susceptibility_values": "|".join(f"{value:.10f}" for value in susceptibility_values),
            }
            if best is None or float(row["invariant_score"]) < float(best["invariant_score"]):
                best = row
        if best is not None:
            candidates.append(best)
    candidates.sort(
        key=lambda row: (
            row_float(row, "invariant_score", default=float("inf")),
            row_float(row, "lambda_like", default=float("inf")),
        )
    )
    return candidates


def normalize_crossing_candidates(candidates: list[dict[str, object]]) -> list[dict[str, object]]:
    normalized: list[dict[str, object]] = []
    for row in candidates:
        if not row.get("selected_coupling_id"):
            continue
        payload = dict(row)
        payload["surface_selector"] = SURFACE_CROSSING
        payload["invariant_support"] = ""
        payload["invariant_score"] = ""
        payload["xi_span"] = ""
        payload["binder_span"] = ""
        normalized.append(payload)
    return normalized


def select_candidates(
    summary: dict[tuple[float, float, int], dict[str, float | str]],
    formal_n: float,
    mass_likes: list[float],
    lambda_likes: list[float],
    sizes: list[int],
    surface_selector: str,
    max_line_couplings: int,
) -> tuple[list[dict[str, object]], int]:
    if surface_selector == SURFACE_CROSSING:
        crossings = detect_crossing_records(summary, formal_n, mass_likes, lambda_likes, sizes)
        candidates = normalize_crossing_candidates(
            build_line_candidates(summary, crossings, formal_n, mass_likes, lambda_likes, sizes)
        )
        return candidates[:max_line_couplings], len(crossings)
    if surface_selector == SURFACE_RG_INVARIANT:
        return build_rg_invariant_candidates(summary, formal_n, mass_likes, lambda_likes, sizes)[:max_line_couplings], 0
    raise ValueError(f"Unknown surface_selector: {surface_selector}")


def tag_scan_rows(
    rows: list[dict[str, object]],
    formal_n: float,
    proxy_kind: str,
    surface_selector: str,
) -> list[dict[str, object]]:
    surface_id = coupling_surface_id(formal_n, proxy_kind, surface_selector)
    tagged: list[dict[str, object]] = []
    for row in rows:
        payload = dict(row)
        payload["surface_id"] = surface_id
        payload["topology_proxy_kind"] = proxy_kind
        payload["surface_selector"] = surface_selector
        payload["coupling_id"] = f"{surface_id}::{row['coupling_id']}"
        tagged.append(payload)
    return tagged


def annotate_rows(rows: list[dict[str, object]], formal_n: float, proxy_kind: str, surface_selector: str) -> list[dict[str, object]]:
    surface_id = coupling_surface_id(formal_n, proxy_kind, surface_selector)
    return [
        {
            "surface_id": surface_id,
            "topology_proxy_kind": proxy_kind,
            "surface_selector": surface_selector,
            **row,
        }
        for row in rows
    ]


def summarize_surface(
    formal_n: float,
    proxy_kind: str,
    surface_selector: str,
    crossing_records: int,
    selected_candidates: list[dict[str, object]],
    selected_scan_rows: list[dict[str, object]],
    reduction_rows: list[dict[str, object]],
    metrology_rows: list[dict[str, object]],
) -> dict[str, object]:
    calibrated_de2 = [row for row in reduction_rows if str(row.get("status_de2")) == "calibrated"]
    stable_transfer = [row for row in metrology_rows if str(row.get("transfer_stability_pass")) == "True"]
    eta_values = [row_float(row, "eta_proxy") for row in reduction_rows]
    finite_eta = [value for value in eta_values if np.isfinite(value)]
    if calibrated_de2:
        status = "anchor_reached"
    elif stable_transfer:
        status = "transfer_only"
    elif selected_candidates:
        status = "out_of_anchor_band"
    else:
        status = "no_surface"
    return {
        "surface_id": coupling_surface_id(formal_n, proxy_kind, surface_selector),
        "formal_n": f"{formal_n:.6f}",
        "topology_proxy_kind": proxy_kind,
        "surface_selector": surface_selector,
        "crossing_records": crossing_records,
        "selected_couplings": len({str(row["selected_coupling_id"]) for row in selected_candidates}),
        "selected_scan_rows": len(selected_scan_rows),
        "reduction_rows": len(reduction_rows),
        "de2_calibrated_rows": len(calibrated_de2),
        "stable_transfer_estimators": "|".join(sorted({str(row["eta_estimator"]) for row in stable_transfer})),
        "eta_proxy_min": "" if not finite_eta else f"{float(np.min(finite_eta)):.10f}",
        "eta_proxy_max": "" if not finite_eta else f"{float(np.max(finite_eta)):.10f}",
        "status_h3_h4": status,
    }


def build_analysis(summary_rows: list[dict[str, object]]) -> str:
    lines = [
        "# Fractional Topology Surface Analysis",
        "",
        "## H3/H4 Surface Summary",
        "| surface_id | proxy | selector | selected | DE2 calibrated | stable transfer | eta_min | eta_max | status |",
        "|:---|:---|:---|---:|---:|:---|---:|---:|:---|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['surface_id']} | {row['topology_proxy_kind']} | {row['surface_selector']} "
            f"| {row['selected_couplings']} | {row['de2_calibrated_rows']} "
            f"| {row['stable_transfer_estimators'] or '--'} | {row['eta_proxy_min'] or '--'} "
            f"| {row['eta_proxy_max'] or '--'} | {row['status_h3_h4']} |"
        )
    anchor_surfaces = [row["surface_id"] for row in summary_rows if row["status_h3_h4"] == "anchor_reached"]
    transfer_surfaces = [row["surface_id"] for row in summary_rows if row["status_h3_h4"] == "transfer_only"]
    lines.extend(
        [
            "",
            "## Interpretation",
            f"- anchor_reached_surfaces: {anchor_surfaces or 'none'}",
            f"- transfer_only_surfaces: {transfer_surfaces or 'none'}",
        ]
    )
    if anchor_surfaces:
        lines.append("- interpretation: at least one topology/surface selector reaches the FRG eta anchor band without changing the reduction layer.")
    elif transfer_surfaces:
        lines.append("- interpretation: topology/surface selection still needs transfer calibration; direct eta anchoring remains unresolved.")
    else:
        lines.append("- interpretation: neither topology nor critical-surface selector reaches the anchor band in this survey.")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Probe H3/H4 topology and critical-surface definitions.")
    parser.add_argument("--L", default="6,8,10", help="Comma-separated lattice sizes.")
    parser.add_argument("--formal-n", type=float, default=2.78, help="Single formal n value.")
    parser.add_argument(
        "--proxy-kind",
        default=f"{PROXY_DIRECT},{PROXY_EMBEDDING}",
        help="Comma-separated proxy topologies to probe.",
    )
    parser.add_argument(
        "--surface-selector",
        default=f"{SURFACE_CROSSING},{SURFACE_RG_INVARIANT}",
        help="Comma-separated surface selectors to probe.",
    )
    parser.add_argument("--window-json", type=Path, default=None, help="Optional JSON mapping proxy_kind to scan windows.")
    parser.add_argument("--max-line-couplings", type=int, default=5)
    parser.add_argument("--warmup", type=int, default=80)
    parser.add_argument("--measure", type=int, default=160)
    parser.add_argument("--seed", type=int, default=171)
    parser.add_argument("--proposal-scale", type=float, default=0.65)
    parser.add_argument("--block-size", type=int, default=8)
    parser.add_argument("--transfer-max-cv", type=float, default=0.10)
    parser.add_argument("--grid-scan-out", type=Path, default=RESULTS_DIR / "phase5_fractional_topology_grid_scan.csv")
    parser.add_argument("--selected-scan-out", type=Path, default=RESULTS_DIR / "phase5_fractional_topology_selected_scan.csv")
    parser.add_argument("--candidates-out", type=Path, default=RESULTS_DIR / "phase5_fractional_topology_candidates.csv")
    parser.add_argument("--reduction-out", type=Path, default=RESULTS_DIR / "phase5_fractional_topology_reduction.csv")
    parser.add_argument("--metrology-summary-out", type=Path, default=RESULTS_DIR / "phase5_fractional_topology_metrology_summary.csv")
    parser.add_argument("--transfer-out", type=Path, default=RESULTS_DIR / "phase5_fractional_topology_transfer.csv")
    parser.add_argument("--summary-out", type=Path, default=RESULTS_DIR / "phase5_fractional_topology_summary.csv")
    parser.add_argument("--analysis-out", type=Path, default=RESULTS_DIR / "phase5_fractional_topology_analysis.md")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    sizes = parse_int_list(args.L)
    formal_n = float(args.formal_n)
    proxy_kinds = parse_choice_list(args.proxy_kind)
    surface_selectors = parse_choice_list(args.surface_selector)
    windows = load_windows(args.window_json)

    all_grid_rows: list[dict[str, object]] = []
    all_candidates: list[dict[str, object]] = []
    all_selected_scan_rows: list[dict[str, object]] = []
    all_reduction_rows: list[dict[str, object]] = []
    all_metrology_rows: list[dict[str, object]] = []
    all_transfer_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for proxy_kind in proxy_kinds:
        if proxy_kind not in windows:
            raise SystemExit(f"Missing topology window for proxy_kind={proxy_kind}")
        mass_likes = windows[proxy_kind]["mass_like"]
        lambda_likes = windows[proxy_kind]["lambda_like"]
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
            t_regulator=0.05,
            proxy_kind=proxy_kind,
            schedule_mode="shared",
            schedule_path=None,
        )
        all_grid_rows.extend(grid_scan_rows)
        scan_summary = summarize_scan_rows(grid_scan_rows)

        for surface_selector in surface_selectors:
            candidates, crossing_records = select_candidates(
                summary=scan_summary,
                formal_n=formal_n,
                mass_likes=mass_likes,
                lambda_likes=lambda_likes,
                sizes=sizes,
                surface_selector=surface_selector,
                max_line_couplings=args.max_line_couplings,
            )
            annotated_candidates = annotate_rows(candidates, formal_n, proxy_kind, surface_selector)
            all_candidates.extend(annotated_candidates)

            selected_ids = {str(row["selected_coupling_id"]) for row in candidates if row.get("selected_coupling_id")}
            selected_scan_rows = tag_scan_rows(
                filter_scan_rows(grid_scan_rows, selected_ids),
                formal_n=formal_n,
                proxy_kind=proxy_kind,
                surface_selector=surface_selector,
            )
            reduction_rows = build_reduction_rows([{key: str(value) for key, value in row.items()} for row in selected_scan_rows]) if selected_scan_rows else []
            reduction_rows = annotate_rows(reduction_rows, formal_n, proxy_kind, surface_selector)
            metrology_rows, transfer_rows = build_transfer_rows(
                [{key: str(value) for key, value in row.items()} for row in reduction_rows],
                anchor_method="de2",
                max_cv=args.transfer_max_cv,
            ) if reduction_rows else ([], [])
            metrology_rows = annotate_rows(metrology_rows, formal_n, proxy_kind, surface_selector)
            transfer_rows = annotate_rows(transfer_rows, formal_n, proxy_kind, surface_selector)

            all_selected_scan_rows.extend(selected_scan_rows)
            all_reduction_rows.extend(reduction_rows)
            all_metrology_rows.extend(metrology_rows)
            all_transfer_rows.extend(transfer_rows)
            summary_rows.append(
                summarize_surface(
                    formal_n=formal_n,
                    proxy_kind=proxy_kind,
                    surface_selector=surface_selector,
                    crossing_records=crossing_records,
                    selected_candidates=candidates,
                    selected_scan_rows=selected_scan_rows,
                    reduction_rows=reduction_rows,
                    metrology_rows=metrology_rows,
                )
            )

    if not all_selected_scan_rows:
        raise SystemExit("no selected H3/H4 surface rows were found")

    csv_write(all_grid_rows, args.grid_scan_out)
    csv_write(all_selected_scan_rows, args.selected_scan_out)
    csv_write(all_candidates, args.candidates_out)
    csv_write(all_reduction_rows, args.reduction_out)
    csv_write(all_metrology_rows, args.metrology_summary_out)
    csv_write(all_transfer_rows, args.transfer_out)
    csv_write(summary_rows, args.summary_out)
    args.analysis_out.write_text(build_analysis(summary_rows), encoding="utf-8")
    print(f"Wrote topology grid scan to {args.grid_scan_out}")
    print(f"Wrote topology selected scan to {args.selected_scan_out}")
    print(f"Wrote topology candidates to {args.candidates_out}")
    print(f"Wrote topology reduction to {args.reduction_out}")
    print(f"Wrote topology metrology summary to {args.metrology_summary_out}")
    print(f"Wrote topology transfer rows to {args.transfer_out}")
    print(f"Wrote topology summary to {args.summary_out}")
    print(f"Wrote topology analysis to {args.analysis_out}")


if __name__ == "__main__":
    main()
