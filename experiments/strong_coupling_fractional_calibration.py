#!/usr/bin/env python3
"""
Calibration sweep for the fractional proxy.

This script searches over mass_like / lambda_like / t_regulator and records
whether any setting lands inside the FRG-anchor band required by the current
gamma reduction surface.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from strong_coupling_common import RESULTS_DIR, csv_write, fit_power_law, gamma_phi_reduction_from_eta, parse_float_list, parse_int_list
from strong_coupling_fractional_proxy import simulate_direct_t_projected_proxy, simulate_fractional_proxy


def spike_ratio(values: list[float]) -> float:
    arr = np.asarray(values, dtype=np.float64)
    if arr.size == 0:
        return float("inf")
    baseline = float(np.median(arr))
    if not np.isfinite(baseline) or baseline <= 0.0:
        return float("inf")
    return float(np.max(arr) / baseline)


def xi_window_passes(values: list[float], min_xi: float = 1e-6) -> bool:
    arr = np.asarray(values, dtype=np.float64)
    if arr.size == 0:
        return False
    return bool(np.all(np.isfinite(arr)) and np.all((arr > min_xi) & (arr <= 1.0)))


def build_rows(
    sizes: list[int],
    formal_ns: list[float],
    mass_likes: list[float],
    lambda_likes: list[float],
    t_regulators: list[float],
    warmup: int,
    measure: int,
    seed: int,
    proposal_scale: float,
    block_size: int,
    proxy_kind: str,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    effective_t_regulators = t_regulators if proxy_kind != "t_projected_direct" else [0.0]
    for formal_n in formal_ns:
        for mass_like in mass_likes:
            for lambda_like in lambda_likes:
                for t_regulator in effective_t_regulators:
                    susceptibility_values: list[float] = []
                    susceptibility_errors: list[float] = []
                    xi_values: list[float] = []
                    acceptance_values: list[float] = []
                    proposal_scale_finals: list[float] = []
                    split_stability_values: list[bool] = []
                    for L in sizes:
                        run_seed = (
                            seed
                            + L * 131
                            + int(formal_n * 1000)
                            + int(mass_like * 100)
                            + int(lambda_like * 1000)
                            + int(t_regulator * 1000)
                        )
                        if proxy_kind == "t_projected_direct":
                            results, _, run_metadata = simulate_direct_t_projected_proxy(
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
                        else:
                            results, _, run_metadata = simulate_fractional_proxy(
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
                        susceptibility_values.append(float(results["susceptibility"][0]))
                        susceptibility_errors.append(max(float(results["susceptibility"][1]), 1e-6))
                        xi_values.append(float(results["xi_over_L"][0]))
                        acceptance_values.append(float(run_metadata["acceptance_mean"]))
                        proposal_scale_finals.append(float(run_metadata["proposal_scale_final"]))
                        split_stability_values.append(bool(run_metadata["split_stability_pass"]))

                    fit = fit_power_law(sizes, susceptibility_values, susceptibility_errors, method="fractional chi ~ L^(2-eta)")
                    eta_proxy = 2.0 - fit.slope if fit.slope == fit.slope else float("nan")
                    lpa = gamma_phi_reduction_from_eta(formal_n, eta_proxy, method="lpa_t")
                    de2 = gamma_phi_reduction_from_eta(formal_n, eta_proxy, method="de2_t")
                    score_de2 = abs(eta_proxy - de2.eta_anchor) if eta_proxy == eta_proxy else float("nan")
                    xi_window_pass = xi_window_passes(xi_values)
                    susceptibility_spike_ratio = spike_ratio(susceptibility_values)
                    split_stability_pass = all(split_stability_values)
                    stability_gate_pass = bool(
                        xi_window_pass
                        and np.isfinite(susceptibility_spike_ratio)
                        and susceptibility_spike_ratio <= 4.0
                        and split_stability_pass
                    )
                    rows.append(
                        {
                            "formal_n": f"{formal_n:.6f}",
                            "sizes": ",".join(str(size) for size in sizes),
                            "mass_like": f"{mass_like:.6f}",
                            "lambda_like": f"{lambda_like:.6f}",
                            "t_regulator": f"{t_regulator:.6f}",
                            "proxy_kind": proxy_kind,
                            "eta_proxy": f"{eta_proxy:.10f}",
                            "eta_anchor_de2": f"{de2.eta_anchor:.10f}",
                            "gamma_phi_proxy_de2": "" if de2.gamma_proxy != de2.gamma_proxy else f"{de2.gamma_proxy:.10f}",
                            "status_de2": de2.status,
                            "score_de2": "" if score_de2 != score_de2 else f"{score_de2:.10f}",
                            "eta_anchor_lpa": f"{lpa.eta_anchor:.10f}",
                            "gamma_phi_proxy_lpa": "" if lpa.gamma_proxy != lpa.gamma_proxy else f"{lpa.gamma_proxy:.10f}",
                            "status_lpa": lpa.status,
                            "xi_values": "|".join(f"{value:.10f}" for value in xi_values),
                            "xi_window_pass": str(xi_window_pass),
                            "susceptibility_values": "|".join(f"{value:.10f}" for value in susceptibility_values),
                            "susceptibility_spike_ratio": "" if not np.isfinite(susceptibility_spike_ratio) else f"{susceptibility_spike_ratio:.10f}",
                            "split_stability_pass": str(split_stability_pass),
                            "acceptance_by_L": "|".join(f"{value:.10f}" for value in acceptance_values),
                            "proposal_scale_final_by_L": "|".join(f"{value:.10f}" for value in proposal_scale_finals),
                            "stability_gate_pass": str(stability_gate_pass),
                        }
                    )
    rows.sort(
        key=lambda row: (
            row["status_de2"] != "calibrated",
            row["xi_window_pass"] != "True",
            row["split_stability_pass"] != "True",
            float(row["susceptibility_spike_ratio"]) > 4.0 if row["susceptibility_spike_ratio"] else True,
            float(row["score_de2"]) if row["score_de2"] else 1e9,
            float(row["formal_n"]),
            float(row["mass_like"]),
            float(row["lambda_like"]),
            float(row["t_regulator"]),
        )
    )
    return rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sweep fractional proxy calibration candidates.")
    parser.add_argument("--L", default="4,6,8", help="Comma-separated lattice sizes.")
    parser.add_argument("--formal-n", default="2.78", help="Comma-separated formal n values.")
    parser.add_argument("--mass-like", default="8.0,9.0,10.0,11.0,12.0,13.0,14.0", help="Comma-separated mass-like values.")
    parser.add_argument("--lambda-like", default="0.25,0.5,1.0,2.0", help="Comma-separated lambda-like values.")
    parser.add_argument("--t-regulator", default="0.01,0.02,0.05,0.1,0.2", help="Comma-separated T-axis regulators.")
    parser.add_argument("--warmup", type=int, default=60, help="Warmup sweeps.")
    parser.add_argument("--measure", type=int, default=120, help="Measured sweeps.")
    parser.add_argument("--seed", type=int, default=71, help="Base RNG seed.")
    parser.add_argument("--proposal-scale", type=float, default=0.65, help="Proposal scale.")
    parser.add_argument("--block-size", type=int, default=8, help="Bootstrap block size.")
    parser.add_argument(
        "--proxy-kind",
        choices=["t_projected_fractional_embedding", "t_projected_direct"],
        default="t_projected_direct",
        help="Fractional proxy family to calibrate.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=RESULTS_DIR / "phase2_fractional_calibration.csv",
        help="Calibration sweep CSV path.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    rows = build_rows(
        sizes=parse_int_list(args.L),
        formal_ns=parse_float_list(args.formal_n),
        mass_likes=parse_float_list(args.mass_like),
        lambda_likes=parse_float_list(args.lambda_like),
        t_regulators=parse_float_list(args.t_regulator),
        warmup=args.warmup,
        measure=args.measure,
        seed=args.seed,
        proposal_scale=args.proposal_scale,
        block_size=args.block_size,
        proxy_kind=args.proxy_kind,
    )
    csv_write(rows, args.out)
    calibrated = sum(1 for row in rows if row["status_de2"] == "calibrated" or row["status_lpa"] == "calibrated")
    print(f"Wrote fractional calibration sweep to {args.out}")
    print(f"calibrated_rows={calibrated}/{len(rows)}")


if __name__ == "__main__":
    main()
