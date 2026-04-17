from __future__ import annotations

import csv
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import numpy as np


EXPERIMENTS_DIR = Path(__file__).resolve().parents[1]
REFERENCE_SCRIPT = EXPERIMENTS_DIR / "strong_coupling_mc_reference.py"
SCAN_SCRIPT = EXPERIMENTS_DIR / "strong_coupling_mc_scan.py"
FRACTIONAL_SCRIPT = EXPERIMENTS_DIR / "strong_coupling_fractional_proxy.py"
CALIBRATION_SCRIPT = EXPERIMENTS_DIR / "strong_coupling_fractional_calibration.py"
ACCEPTANCE_SCRIPT = EXPERIMENTS_DIR / "strong_coupling_fractional_acceptance.py"
REDUCTION_SCRIPT = EXPERIMENTS_DIR / "strong_coupling_gamma_reduction.py"
COMPARE_SCRIPT = EXPERIMENTS_DIR / "strong_coupling_compare.py"
COMMON_SCRIPT = EXPERIMENTS_DIR / "strong_coupling_common.py"


def run_python(script: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(script), *args],
        cwd=EXPERIMENTS_DIR,
        capture_output=True,
        text=True,
        check=check,
    )


def load_module(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def promote_reference_gate(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["pass"] = True
    payload["diagnostics"]["pass_breakdown"] = {
        "binder": {"value": 0.46, "target": 0.4656, "delta": 0.0056, "tolerance": 0.20, "pass": True},
        "xi_over_L": {"value": 0.64, "target": 0.6431, "delta": 0.0031, "tolerance": 0.25, "pass": True},
        "eta": {"value": 0.04, "target": 0.0363, "delta": 0.0037, "tolerance": 0.20, "pass": True},
        "nu": {"value": 0.63, "target": 0.63, "delta": 0.0, "tolerance": 0.25, "pass": True},
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def test_weighted_linear_fit_pure_function() -> None:
    module = load_module(COMMON_SCRIPT, "strong_common")
    fit = module.weighted_linear_fit(
        xs=[-2.0, -1.0, 0.0, 1.0, 2.0],
        ys=[-5.0, -2.0, 1.0, 4.0, 7.0],
        yerrs=[0.1, 0.1, 0.1, 0.1, 0.1],
        method="linear",
    )
    assert np.isclose(fit.slope, 3.0, atol=1e-6)
    assert np.isclose(fit.intercept, 1.0, atol=1e-6)


def test_t_projected_axis_weights_contract() -> None:
    module = load_module(COMMON_SCRIPT, "strong_common_tproj")
    payload = module.t_projected_axis_weights(2.78, t_regulator=0.05)
    assert np.isclose(payload["n_eff"], 1.78, atol=1e-6)
    assert 0.0 < payload["t_axis_weight"] < payload["transverse_weight"] <= 1.0


def test_gamma_phi_reduction_out_of_anchor_band() -> None:
    module = load_module(COMMON_SCRIPT, "strong_common_gamma")
    reduced = module.gamma_phi_reduction_from_eta(2.78, eta_proxy=0.2, method="de2_t")
    assert reduced.status == "out_of_anchor_band"
    assert not np.isfinite(reduced.gamma_proxy)


def test_adaptive_proposal_moves_toward_target_band() -> None:
    module = load_module(FRACTIONAL_SCRIPT, "fractional_proxy_adapt")
    scale = 0.65
    for _ in range(5):
        scale = module.adapt_proposal_scale(scale, acceptance_rate=0.20)
    assert 0.10 <= scale < 0.65

    for _ in range(5):
        scale = module.adapt_proposal_scale(scale, acceptance_rate=0.80)
    assert scale > 0.10

    in_band = module.adapt_proposal_scale(scale, acceptance_rate=0.50)
    assert np.isclose(in_band, scale)


def test_shuffled_site_order_is_seed_reproducible() -> None:
    module = load_module(FRACTIONAL_SCRIPT, "fractional_proxy_shuffle")
    order_a = module.site_visit_order(8, np.random.default_rng(171), module.SHUFFLED_SITE_ORDER)
    order_b = module.site_visit_order(8, np.random.default_rng(171), module.SHUFFLED_SITE_ORDER)
    fixed = module.site_visit_order(8, np.random.default_rng(171), module.FIXED_SITE_ORDER)
    assert np.array_equal(order_a, order_b)
    assert not np.array_equal(order_a, fixed)


def test_calibrated_component_detector_accepts_three_point_cluster() -> None:
    module = load_module(ACCEPTANCE_SCRIPT, "fractional_acceptance_component")
    rows = [
        {
            "formal_n": "2.780000",
            "mass_like": "0.900000",
            "lambda_like": "1.000000",
            "status_de2": "calibrated",
            "xi_window_pass": "True",
            "susceptibility_spike_ratio": "1.2000000000",
            "split_stability_pass": "True",
            "score_de2": "0.0100000000",
        },
        {
            "formal_n": "2.780000",
            "mass_like": "0.950000",
            "lambda_like": "1.000000",
            "status_de2": "calibrated",
            "xi_window_pass": "True",
            "susceptibility_spike_ratio": "1.3000000000",
            "split_stability_pass": "True",
            "score_de2": "0.0200000000",
        },
        {
            "formal_n": "2.780000",
            "mass_like": "1.000000",
            "lambda_like": "1.000000",
            "status_de2": "calibrated",
            "xi_window_pass": "True",
            "susceptibility_spike_ratio": "1.1000000000",
            "split_stability_pass": "True",
            "score_de2": "0.0300000000",
        },
        {
            "formal_n": "2.780000",
            "mass_like": "1.100000",
            "lambda_like": "1.200000",
            "status_de2": "calibrated",
            "xi_window_pass": "True",
            "susceptibility_spike_ratio": "1.0000000000",
            "split_stability_pass": "True",
            "score_de2": "0.0050000000",
        },
    ]
    summary = module.detect_calibrated_components(rows)
    assert summary["largest_calibrated_component_size"] == 3
    assert summary["local_foothold"] is True
    assert len(summary["selected_component_couplings"]) == 3


def test_reference_cli_smoke(tmp_path: Path) -> None:
    out = tmp_path / "reference.json"
    run_python(
        REFERENCE_SCRIPT,
        "--L",
        "4,6",
        "--warmup",
        "10",
        "--measure",
        "20",
        "--seed",
        "5",
        "--beta-window",
        "0.004",
        "--beta-points",
        "5",
        "--block-size",
        "4",
        "--out",
        str(out),
    )
    payload = json.loads(out.read_text(encoding="utf-8"))
    for key in [
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
    ]:
        assert key in payload
    assert isinstance(payload["pass"], bool)
    assert np.isfinite(payload["binder"]["value"])
    assert 0.0 <= float(payload["xi_over_L"]["value"])
    assert 0.0 <= float(payload["susceptibility"]["value"])
    assert np.isfinite(payload["stderr"]["binder"])
    assert np.isfinite(payload["tau_int"]["magnetization_abs"])
    diagnostics = payload["diagnostics"]
    for key in ["beta_grid", "nu_channels", "pass_breakdown", "fit_ranges"]:
        assert key in diagnostics
    assert len(diagnostics["beta_grid"]) == 5


def test_scan_cli_smoke_and_schema(tmp_path: Path) -> None:
    out = tmp_path / "scan.csv"
    run_python(
        SCAN_SCRIPT,
        "--L",
        "4",
        "--mass-like",
        "6.0",
        "--lambda-like",
        "1.0",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--seed",
        "13",
        "--out",
        str(out),
    )
    with out.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    required = {
        "model",
        "dimension_mode",
        "L",
        "coupling_id",
        "observable",
        "mean",
        "stderr",
        "tau_int",
        "seed",
    }
    assert required.issubset(rows[0].keys())
    acceptance_rows = [row for row in rows if row["observable"] == "acceptance_rate"]
    assert acceptance_rows
    acceptance = float(acceptance_rows[0]["mean"])
    assert 0.0 <= acceptance <= 1.0
    xi_rows = [row for row in rows if row["observable"] == "xi_over_L"]
    assert xi_rows
    assert 0.0 <= float(xi_rows[0]["mean"]) <= 1.0
    assert np.isfinite(float(xi_rows[0]["stderr"]))


def test_fractional_proxy_cli_smoke_and_schema(tmp_path: Path) -> None:
    out = tmp_path / "fractional.csv"
    run_python(
        FRACTIONAL_SCRIPT,
        "--L",
        "4,6",
        "--formal-n",
        "2.9,2.78",
        "--mass-like",
        "5.0",
        "--lambda-like",
        "1.0",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--seed",
        "31",
        "--block-size",
        "4",
        "--out",
        str(out),
    )
    with out.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    required = {
        "model",
        "dimension_mode",
        "L",
        "coupling_id",
        "observable",
        "mean",
        "stderr",
        "tau_int",
        "seed",
        "formal_n",
        "n_eff",
        "transverse_weight",
        "t_axis_weight",
        "proxy_kind",
        "schedule_mode",
        "schedule_source",
        "update_kernel",
        "proposal_scale_final",
        "metro_hits",
        "measure_stride",
        "site_order",
    }
    assert required.issubset(rows[0].keys())
    assert {row["dimension_mode"] for row in rows} == {"fractional_proxy"}
    assert sorted({row["formal_n"] for row in rows}) == ["2.780000", "2.900000"]
    assert {row["proxy_kind"] for row in rows} == {"t_projected_direct"}
    assert {row["schedule_mode"] for row in rows} == {"shared"}
    assert {row["update_kernel"] for row in rows} == {"adaptive_shuffled_multihit_metropolis"}
    assert {row["metro_hits"] for row in rows} == {"4"}
    assert {row["measure_stride"] for row in rows} == {"5"}
    assert {row["site_order"] for row in rows} == {"shuffled"}
    acceptance_rows = [row for row in rows if row["observable"] == "acceptance_rate"]
    assert acceptance_rows
    acceptance = float(acceptance_rows[0]["mean"])
    assert 0.0 <= acceptance <= 1.0


def test_fractional_proxy_auto_schedule_uses_per_n_direct_defaults(tmp_path: Path) -> None:
    out = tmp_path / "fractional_auto.csv"
    run_python(
        FRACTIONAL_SCRIPT,
        "--L",
        "4,6",
        "--formal-n",
        "3.0,2.78",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--seed",
        "31",
        "--block-size",
        "4",
        "--out",
        str(out),
    )
    with out.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    assert {row["schedule_mode"] for row in rows} == {"per_n"}
    assert {row["schedule_source"] for row in rows} == {"built_in_direct_v1"}


def test_fractional_embedding_cli_smoke(tmp_path: Path) -> None:
    out = tmp_path / "fractional_embedding.csv"
    run_python(
        FRACTIONAL_SCRIPT,
        "--proxy-kind",
        "t_projected_fractional_embedding",
        "--L",
        "4,6",
        "--formal-n",
        "2.9,2.78",
        "--mass-like",
        "6.0",
        "--lambda-like",
        "1.0",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--seed",
        "31",
        "--block-size",
        "4",
        "--out",
        str(out),
    )
    with out.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    assert {row["proxy_kind"] for row in rows} == {"t_projected_fractional_embedding"}


def test_gamma_reduction_cli_smoke(tmp_path: Path) -> None:
    scan_out = tmp_path / "fractional.csv"
    reduction_out = tmp_path / "reduction.csv"
    run_python(
        FRACTIONAL_SCRIPT,
        "--L",
        "4,6",
        "--formal-n",
        "2.9,2.78",
        "--mass-like",
        "6.0",
        "--lambda-like",
        "1.0",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--seed",
        "31",
        "--block-size",
        "4",
        "--out",
        str(scan_out),
    )
    run_python(
        REDUCTION_SCRIPT,
        "--scan",
        str(scan_out),
        "--out",
        str(reduction_out),
    )
    with reduction_out.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    required = {
        "formal_n",
        "coupling_id",
        "sizes",
        "eta_proxy",
        "gamma_phi_proxy_lpa",
        "status_lpa",
        "gamma_phi_proxy_de2",
        "status_de2",
    }
    assert required.issubset(rows[0].keys())


def test_fractional_calibration_cli_smoke(tmp_path: Path) -> None:
    out = tmp_path / "calibration.csv"
    run_python(
        CALIBRATION_SCRIPT,
        "--L",
        "4,6",
        "--formal-n",
        "2.78",
        "--mass-like",
        "10.0",
        "--lambda-like",
        "1.0",
        "--t-regulator",
        "0.05",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--block-size",
        "4",
        "--out",
        str(out),
    )
    with out.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    required = {
        "formal_n",
        "sizes",
        "mass_like",
        "lambda_like",
        "t_regulator",
        "proxy_kind",
        "eta_proxy",
        "status_de2",
        "status_lpa",
        "xi_values",
        "xi_window_pass",
        "susceptibility_values",
        "susceptibility_spike_ratio",
        "split_stability_pass",
        "acceptance_by_L",
        "proposal_scale_final_by_L",
        "stability_gate_pass",
    }
    assert required.issubset(rows[0].keys())


def test_fractional_acceptance_cli_smoke(tmp_path: Path) -> None:
    reference_out = tmp_path / "reference.json"
    calibration_out = tmp_path / "acceptance_calibration.csv"
    schedule_out = tmp_path / "acceptance_schedule.json"
    manifest_out = tmp_path / "acceptance_manifest.json"
    scan_out = tmp_path / "acceptance_scan.csv"
    reduction_out = tmp_path / "acceptance_reduction.csv"
    analysis_out = tmp_path / "acceptance_analysis.md"

    run_python(
        REFERENCE_SCRIPT,
        "--L",
        "4,6",
        "--warmup",
        "10",
        "--measure",
        "20",
        "--seed",
        "17",
        "--beta-window",
        "0.004",
        "--beta-points",
        "5",
        "--block-size",
        "4",
        "--out",
        str(reference_out),
    )
    promote_reference_gate(reference_out)

    run_python(
        ACCEPTANCE_SCRIPT,
        "--reference",
        str(reference_out),
        "--L",
        "4,6",
        "--formal-n",
        "2.90,2.78",
        "--mass-like",
        "0.4,0.8",
        "--lambda-like",
        "0.5,1.0",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--block-size",
        "4",
        "--calibration-out",
        str(calibration_out),
        "--schedule-out",
        str(schedule_out),
        "--manifest-out",
        str(manifest_out),
        "--scan-out",
        str(scan_out),
        "--reduction-out",
        str(reduction_out),
        "--analysis-out",
        str(analysis_out),
    )

    schedule = json.loads(schedule_out.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_out.read_text(encoding="utf-8"))
    assert sorted(schedule.keys()) == ["2.780000", "2.900000"]
    assert "selected_rows" in manifest
    for key in [
        "largest_calibrated_component_size",
        "selected_component_couplings",
        "local_foothold",
        "blocking_reason",
    ]:
        assert key in manifest

    with scan_out.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    assert {row["schedule_mode"] for row in rows} == {"per_n"}
    assert {row["schedule_source"] for row in rows} == {"path"}
    assert "update_kernel" in rows[0]

    with reduction_out.open("r", encoding="utf-8", newline="") as fh:
        reduction_rows = list(csv.DictReader(fh))
    assert reduction_rows
    assert "eta_proxy" in reduction_rows[0]

    analysis = analysis_out.read_text(encoding="utf-8")
    assert "ready_for_fractional_proxy" in analysis
    assert "largest_calibrated_component_size" in analysis
    assert "blocking_reason" in analysis


def test_compare_accepts_fractional_scan_when_reference_gate_is_open(tmp_path: Path) -> None:
    reference_out = tmp_path / "reference.json"
    scan_out = tmp_path / "fractional.csv"
    reduction_out = tmp_path / "reduction.csv"
    analysis_out = tmp_path / "analysis.md"

    run_python(
        REFERENCE_SCRIPT,
        "--L",
        "4,6",
        "--warmup",
        "10",
        "--measure",
        "20",
        "--seed",
        "17",
        "--beta-window",
        "0.004",
        "--beta-points",
        "5",
        "--block-size",
        "4",
        "--out",
        str(reference_out),
    )
    promote_reference_gate(reference_out)
    fieldnames = [
        "model",
        "dimension_mode",
        "L",
        "coupling_id",
        "observable",
        "mean",
        "stderr",
        "tau_int",
        "seed",
        "formal_n",
        "n_eff",
        "transverse_weight",
        "t_axis_weight",
        "projection_ratio",
        "proxy_kind",
        "mass_like",
        "lambda_like",
    ]
    scan_rows = [
        {
            "model": "t_projected_fractional_phi4_metropolis",
            "dimension_mode": "fractional_proxy",
            "L": "4",
            "coupling_id": "n2.78_probe",
            "observable": "susceptibility",
            "mean": "1.0",
            "stderr": "0.01",
            "tau_int": "1.0",
            "seed": "19",
            "formal_n": "2.780000",
            "n_eff": "1.780000",
            "transverse_weight": "0.890000",
            "t_axis_weight": "0.050000",
            "projection_ratio": "0.056180",
            "proxy_kind": "t_projected_fractional_embedding",
            "mass_like": "6.000000",
            "lambda_like": "1.000000",
        },
        {
            "model": "t_projected_fractional_phi4_metropolis",
            "dimension_mode": "fractional_proxy",
            "L": "6",
            "coupling_id": "n2.78_probe",
            "observable": "susceptibility",
            "mean": "2.2209950868",
            "stderr": "0.01",
            "tau_int": "1.0",
            "seed": "19",
            "formal_n": "2.780000",
            "n_eff": "1.780000",
            "transverse_weight": "0.890000",
            "t_axis_weight": "0.050000",
            "projection_ratio": "0.056180",
            "proxy_kind": "t_projected_fractional_embedding",
            "mass_like": "6.000000",
            "lambda_like": "1.000000",
        },
        {
            "model": "t_projected_fractional_phi4_metropolis",
            "dimension_mode": "fractional_proxy",
            "L": "4",
            "coupling_id": "n2.78_probe",
            "observable": "xi_over_L",
            "mean": "0.3",
            "stderr": "0.01",
            "tau_int": "1.0",
            "seed": "19",
            "formal_n": "2.780000",
            "n_eff": "1.780000",
            "transverse_weight": "0.890000",
            "t_axis_weight": "0.050000",
            "projection_ratio": "0.056180",
            "proxy_kind": "t_projected_fractional_embedding",
            "mass_like": "6.000000",
            "lambda_like": "1.000000",
        },
        {
            "model": "t_projected_fractional_phi4_metropolis",
            "dimension_mode": "fractional_proxy",
            "L": "6",
            "coupling_id": "n2.78_probe",
            "observable": "xi_over_L",
            "mean": "0.4",
            "stderr": "0.01",
            "tau_int": "1.0",
            "seed": "19",
            "formal_n": "2.780000",
            "n_eff": "1.780000",
            "transverse_weight": "0.890000",
            "t_axis_weight": "0.050000",
            "projection_ratio": "0.056180",
            "proxy_kind": "t_projected_fractional_embedding",
            "mass_like": "6.000000",
            "lambda_like": "1.000000",
        },
        {
            "model": "t_projected_fractional_phi4_metropolis",
            "dimension_mode": "fractional_proxy",
            "L": "4",
            "coupling_id": "n2.78_probe",
            "observable": "binder",
            "mean": "0.1",
            "stderr": "0.01",
            "tau_int": "1.0",
            "seed": "19",
            "formal_n": "2.780000",
            "n_eff": "1.780000",
            "transverse_weight": "0.890000",
            "t_axis_weight": "0.050000",
            "projection_ratio": "0.056180",
            "proxy_kind": "t_projected_fractional_embedding",
            "mass_like": "6.000000",
            "lambda_like": "1.000000",
        },
        {
            "model": "t_projected_fractional_phi4_metropolis",
            "dimension_mode": "fractional_proxy",
            "L": "6",
            "coupling_id": "n2.78_probe",
            "observable": "binder",
            "mean": "0.2",
            "stderr": "0.01",
            "tau_int": "1.0",
            "seed": "19",
            "formal_n": "2.780000",
            "n_eff": "1.780000",
            "transverse_weight": "0.890000",
            "t_axis_weight": "0.050000",
            "projection_ratio": "0.056180",
            "proxy_kind": "t_projected_fractional_embedding",
            "mass_like": "6.000000",
            "lambda_like": "1.000000",
        },
        {
            "model": "t_projected_fractional_phi4_metropolis",
            "dimension_mode": "fractional_proxy",
            "L": "4",
            "coupling_id": "n2.78_probe",
            "observable": "acceptance_rate",
            "mean": "0.5",
            "stderr": "0.01",
            "tau_int": "0.5",
            "seed": "19",
            "formal_n": "2.780000",
            "n_eff": "1.780000",
            "transverse_weight": "0.890000",
            "t_axis_weight": "0.050000",
            "projection_ratio": "0.056180",
            "proxy_kind": "t_projected_fractional_embedding",
            "mass_like": "6.000000",
            "lambda_like": "1.000000",
        },
        {
            "model": "t_projected_fractional_phi4_metropolis",
            "dimension_mode": "fractional_proxy",
            "L": "6",
            "coupling_id": "n2.78_probe",
            "observable": "acceptance_rate",
            "mean": "0.5",
            "stderr": "0.01",
            "tau_int": "0.5",
            "seed": "19",
            "formal_n": "2.780000",
            "n_eff": "1.780000",
            "transverse_weight": "0.890000",
            "t_axis_weight": "0.050000",
            "projection_ratio": "0.056180",
            "proxy_kind": "t_projected_fractional_embedding",
            "mass_like": "6.000000",
            "lambda_like": "1.000000",
        },
    ]
    with scan_out.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scan_rows)
    run_python(
        REDUCTION_SCRIPT,
        "--scan",
        str(scan_out),
        "--out",
        str(reduction_out),
    )

    run_python(
        COMPARE_SCRIPT,
        "--reference",
        str(reference_out),
        "--scan",
        str(scan_out),
        "--reduction",
        str(reduction_out),
        "--out",
        str(analysis_out),
    )
    report = analysis_out.read_text(encoding="utf-8")
    assert "Gamma Reduction Surface" in report
    assert "ready_for_fractional_proxy: True" in report
    assert "ready_for_gamma_comparison: True" in report
    assert "scan_mode: fractional_proxy" in report


def test_compare_reports_mixed_scan_modes_fail(tmp_path: Path) -> None:
    reference_out = tmp_path / "reference.json"
    scan_out = tmp_path / "scan.csv"
    analysis_out = tmp_path / "analysis.md"

    run_python(
        REFERENCE_SCRIPT,
        "--L",
        "4,6",
        "--warmup",
        "10",
        "--measure",
        "20",
        "--seed",
        "17",
        "--beta-window",
        "0.004",
        "--beta-points",
        "5",
        "--block-size",
        "4",
        "--out",
        str(reference_out),
    )
    promote_reference_gate(reference_out)
    run_python(
        SCAN_SCRIPT,
        "--L",
        "4",
        "--mass-like",
        "6.0",
        "--lambda-like",
        "1.0",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--seed",
        "19",
        "--out",
        str(scan_out),
    )
    with scan_out.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
        fieldnames = rows[0].keys()
    rows.append(
        {
            **rows[0],
            "dimension_mode": "fractional_proxy",
            "coupling_id": "mixed_probe",
            "observable": "acceptance_rate",
            "mean": "0.5",
            "stderr": "0.01",
            "tau_int": "0.5",
        }
    )
    with scan_out.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    result = run_python(
        COMPARE_SCRIPT,
        "--reference",
        str(reference_out),
        "--scan",
        str(scan_out),
        "--reduction",
        str(tmp_path / "missing.csv"),
        "--out",
        str(analysis_out),
        check=False,
    )
    assert result.returncode != 0
    assert "scan dimension_mode must be unique" in analysis_out.read_text(encoding="utf-8")


def test_compare_reports_reference_gate_failure(tmp_path: Path) -> None:
    reference_out = tmp_path / "reference.json"
    scan_out = tmp_path / "scan.csv"
    analysis_out = tmp_path / "analysis.md"

    run_python(
        REFERENCE_SCRIPT,
        "--L",
        "4,6",
        "--warmup",
        "10",
        "--measure",
        "20",
        "--seed",
        "23",
        "--beta-window",
        "0.004",
        "--beta-points",
        "5",
        "--block-size",
        "4",
        "--out",
        str(reference_out),
    )
    run_python(
        SCAN_SCRIPT,
        "--L",
        "4",
        "--mass-like",
        "6.0",
        "--lambda-like",
        "1.0",
        "--warmup",
        "5",
        "--measure",
        "10",
        "--seed",
        "29",
        "--out",
        str(scan_out),
    )

    result = run_python(
        COMPARE_SCRIPT,
        "--reference",
        str(reference_out),
        "--scan",
        str(scan_out),
        "--reduction",
        str(tmp_path / "missing.csv"),
        "--out",
        str(analysis_out),
        check=False,
    )
    report = analysis_out.read_text(encoding="utf-8")
    assert result.returncode != 0
    assert "reference gate blocked" in report
    assert "ready_for_fractional_proxy: False" in report


def test_compare_reports_scan_sanity_failure(tmp_path: Path) -> None:
    reference_out = tmp_path / "reference.json"
    scan_out = tmp_path / "scan.csv"
    analysis_out = tmp_path / "analysis.md"

    run_python(
        REFERENCE_SCRIPT,
        "--L",
        "4,6",
        "--warmup",
        "10",
        "--measure",
        "20",
        "--seed",
        "23",
        "--beta-window",
        "0.004",
        "--beta-points",
        "5",
        "--block-size",
        "4",
        "--out",
        str(reference_out),
    )
    promote_reference_gate(reference_out)

    fieldnames = [
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
    rows = [
        {
            "model": "3d_scalar_phi4_metropolis",
            "dimension_mode": "integer_proxy",
            "L": "4",
            "coupling_id": "bad_probe",
            "observable": "xi_over_L",
            "mean": "5.0",
            "stderr": "0.1",
            "tau_int": "1.0",
            "seed": "29",
        },
        {
            "model": "3d_scalar_phi4_metropolis",
            "dimension_mode": "integer_proxy",
            "L": "4",
            "coupling_id": "bad_probe",
            "observable": "acceptance_rate",
            "mean": "0.5",
            "stderr": "0.01",
            "tau_int": "0.5",
            "seed": "29",
        },
    ]
    with scan_out.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    result = run_python(
        COMPARE_SCRIPT,
        "--reference",
        str(reference_out),
        "--scan",
        str(scan_out),
        "--reduction",
        str(tmp_path / "missing.csv"),
        "--out",
        str(analysis_out),
        check=False,
    )
    assert result.returncode != 0
    assert "scan sanity issue" in analysis_out.read_text(encoding="utf-8")


def test_wolff_cluster_flip_consistency() -> None:
    module = load_module(REFERENCE_SCRIPT, "strong_ref")
    neighbors = np.array(
        [
            [1, 1, 2, 2, 3, 3],
            [0, 0, 2, 2, 3, 3],
            [0, 0, 1, 1, 3, 3],
            [0, 0, 1, 1, 2, 2],
        ],
        dtype=np.int32,
    )
    spins = np.array([1, 1, -1, -1], dtype=np.int8)
    before = spins.copy()
    cluster = module.wolff_cluster_update(spins, neighbors, beta=0.4, rng=np.random.default_rng(0))
    flipped = set(cluster.tolist())
    for idx in range(spins.size):
        if idx in flipped:
            assert spins[idx] == -before[idx]
        else:
            assert spins[idx] == before[idx]


def test_metropolis_acceptance_rate_range() -> None:
    module = load_module(SCAN_SCRIPT, "strong_scan")
    neighbors = np.array(
        [
            [1, 1, 2, 2, 3, 3],
            [0, 0, 2, 2, 3, 3],
            [0, 0, 1, 1, 3, 3],
            [0, 0, 1, 1, 2, 2],
        ],
        dtype=np.int32,
    )
    field = np.zeros(4, dtype=np.float64)
    acceptance = module.metropolis_sweep(
        field,
        neighbors,
        mass_like=6.0,
        lambda_like=1.0,
        proposal_scale=0.7,
        rng=np.random.default_rng(0),
    )
    assert 0.0 <= acceptance <= 1.0
