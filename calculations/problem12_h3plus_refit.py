#!/usr/bin/env python3
"""Re-fit Problem 12 angle proxy with H3+ curvature terms.

Source data are the rounded arg(lambda_dom(q)) values recorded in:
03_忘却論｜Oblivion/calculations/調査_自動数学_キュー10_スペクトル_周期性.md

The script intentionally separates:
- Phase B train data: q = 5..10
- Phase C/BM stress data: q = 11..15

This keeps the fit from silently treating the q=11 transition as the same
phase while still measuring whether H3+ absorbs the reported residuals.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


PHASE_B = [
    (5, 1.793),
    (6, 1.451),
    (7, 1.321),
    (8, 1.250),
    (9, 1.206),
    (10, 1.174),
]

PHASE_C_STRESS = [
    (11, 1.162),
    (12, 1.152),
    (13, 1.147),
    (14, 1.145),
    (15, 1.145),
]

PHI = (1.0 + math.sqrt(5.0)) / 2.0

CANDIDATE_BETAS = {
    "pi_over_6": math.pi / 6.0,
    "log_phi": math.log(PHI),
    "pi_over_5": math.pi / 5.0,
    "two_pi_over_13": 2.0 * math.pi / 13.0,
    "pi_over_7": math.pi / 7.0,
    "atan_1_over_2": math.atan(0.5),
    "golden_two_atan_1_over_phi": 2.0 * math.atan(1.0 / PHI),
    "prior_h3_beta": 0.5209,
}


@dataclass(frozen=True)
class Fit:
    label: str
    model: str
    q: np.ndarray
    y: np.ndarray
    terms: tuple[str, ...]
    params: np.ndarray
    fitted: np.ndarray
    residuals: np.ndarray
    se: np.ndarray | None
    r2: float
    sse: float
    rmse: float
    aic: float
    aicc: float | None
    bic: float
    loocv_rmse: float
    loocv_errors: np.ndarray
    condition_number: float
    offset: float

    def turning_q(self) -> float | None:
        """Return q where beta + gamma1/q + gamma2/q^2 has zero slope."""
        if "inv_q" not in self.terms or "inv_q2" not in self.terms:
            return None
        gamma1 = float(self.params[self.terms.index("inv_q")])
        gamma2 = float(self.params[self.terms.index("inv_q2")])
        if gamma1 == 0.0:
            return None
        q0 = -2.0 * gamma2 / gamma1
        return q0 if q0 > 0.0 else None

    def to_json(self) -> dict:
        return {
            "label": self.label,
            "model": self.model,
            "q": self.q.tolist(),
            "y": self.y.tolist(),
            "terms": list(self.terms),
            "params": [float(x) for x in self.params],
            "standard_errors": None
            if self.se is None
            else [float(x) for x in self.se],
            "offset_beta": float(self.offset),
            "fitted": [float(x) for x in self.fitted],
            "residuals": [float(x) for x in self.residuals],
            "r2": float(self.r2),
            "sse": float(self.sse),
            "rmse": float(self.rmse),
            "aic": float(self.aic),
            "aicc": None if self.aicc is None else float(self.aicc),
            "bic": float(self.bic),
            "loocv_rmse": float(self.loocv_rmse),
            "loocv_errors": [float(x) for x in self.loocv_errors],
            "condition_number": float(self.condition_number),
            "turning_q": self.turning_q(),
        }


def as_arrays(rows: Iterable[tuple[int, float]]) -> tuple[np.ndarray, np.ndarray]:
    arr = np.array(list(rows), dtype=float)
    return arr[:, 0], arr[:, 1]


def matrix(q: np.ndarray, terms: tuple[str, ...]) -> np.ndarray:
    columns = []
    for term in terms:
        if term == "const":
            columns.append(np.ones_like(q))
        elif term == "inv_q":
            columns.append(1.0 / q)
        elif term == "inv_q2":
            columns.append(1.0 / (q * q))
        else:
            raise ValueError(f"unknown term: {term}")
    return np.vstack(columns).T


def information_criteria(sse: float, n: int, k: int) -> tuple[float, float | None, float]:
    aic = n * math.log(sse / n) + 2.0 * k
    aicc = None
    if n - k - 1 > 0:
        aicc = aic + (2.0 * k * (k + 1.0)) / (n - k - 1.0)
    bic = n * math.log(sse / n) + k * math.log(n)
    return aic, aicc, bic


def fit(label: str, q: np.ndarray, y: np.ndarray, terms: tuple[str, ...], offset: float = 0.0) -> Fit:
    x = matrix(q, terms)
    target = y - offset
    params = np.linalg.lstsq(x, target, rcond=None)[0]
    fitted = offset + x @ params
    residuals = y - fitted
    sse = float(residuals @ residuals)
    sst = float((y - y.mean()) @ (y - y.mean()))
    r2 = 1.0 - sse / sst if sst else 1.0
    n = len(y)
    k = x.shape[1]
    rmse = math.sqrt(sse / n)
    aic, aicc, bic = information_criteria(sse, n, k)

    se: np.ndarray | None = None
    if n > k:
        sigma2 = sse / (n - k)
        se = np.sqrt(np.diag(sigma2 * np.linalg.inv(x.T @ x)))

    loocv_errors = []
    for i in range(n):
        keep = np.ones(n, dtype=bool)
        keep[i] = False
        params_i = np.linalg.lstsq(x[keep], target[keep], rcond=None)[0]
        pred_i = offset + float(x[i] @ params_i)
        loocv_errors.append(float(y[i] - pred_i))
    loocv = np.array(loocv_errors, dtype=float)
    loocv_rmse = math.sqrt(float(loocv @ loocv) / n)

    return Fit(
        label=label,
        model=" + ".join(terms) if offset == 0.0 else f"fixed_beta({offset:.12g}) + " + " + ".join(terms),
        q=q,
        y=y,
        terms=terms,
        params=params,
        fitted=fitted,
        residuals=residuals,
        se=se,
        r2=r2,
        sse=sse,
        rmse=rmse,
        aic=aic,
        aicc=aicc,
        bic=bic,
        loocv_rmse=loocv_rmse,
        loocv_errors=loocv,
        condition_number=float(np.linalg.cond(x)),
        offset=offset,
    )


def predict(fit_obj: Fit, q: np.ndarray, y: np.ndarray) -> dict:
    x = matrix(q, fit_obj.terms)
    fitted = fit_obj.offset + x @ fit_obj.params
    residuals = y - fitted
    sse = float(residuals @ residuals)
    return {
        "from_fit": fit_obj.label,
        "q": q.tolist(),
        "actual": y.tolist(),
        "predicted": [float(x) for x in fitted],
        "residuals": [float(x) for x in residuals],
        "rmse": math.sqrt(sse / len(y)),
        "sse": sse,
    }


def beta_candidate_table(free_fit: Fit) -> list[dict]:
    if not free_fit.terms or free_fit.terms[0] != "const":
        return []
    beta = float(free_fit.params[0])
    beta_se = None if free_fit.se is None else float(free_fit.se[0])
    rows = []
    for name, value in CANDIDATE_BETAS.items():
        z = None if beta_se in (None, 0.0) else (value - beta) / beta_se
        rows.append(
            {
                "candidate": name,
                "value": float(value),
                "delta_from_beta": float(value - beta),
                "z_vs_free_beta": None if z is None else float(z),
            }
        )
    return rows


def main() -> None:
    q_b, y_b = as_arrays(PHASE_B)
    q_c, y_c = as_arrays(PHASE_C_STRESS)
    q_all, y_all = as_arrays(PHASE_B + PHASE_C_STRESS)

    h3_b = fit("phase_b_h3", q_b, y_b, ("const", "inv_q"))
    h3p_b = fit("phase_b_h3plus_free", q_b, y_b, ("const", "inv_q", "inv_q2"))
    h3_all = fit("phase_b_c_h3_stress", q_all, y_all, ("const", "inv_q"))
    h3p_all = fit("phase_b_c_h3plus_stress_free", q_all, y_all, ("const", "inv_q", "inv_q2"))

    fixed_b = [
        fit(f"phase_b_h3plus_fixed_{name}", q_b, y_b, ("inv_q", "inv_q2"), offset=beta)
        for name, beta in CANDIDATE_BETAS.items()
    ]
    fixed_all = [
        fit(f"phase_b_c_h3plus_fixed_{name}", q_all, y_all, ("inv_q", "inv_q2"), offset=beta)
        for name, beta in CANDIDATE_BETAS.items()
    ]

    result = {
        "source_note": "Rounded arg(lambda_dom(q)) values copied from the local Q10 spectral-periodicity calculation note.",
        "phase_b_rows_q5_to_q10": PHASE_B,
        "phase_c_stress_rows_q11_to_q15": PHASE_C_STRESS,
        "fits": [x.to_json() for x in [h3_b, h3p_b, h3_all, h3p_all]],
        "fixed_beta_h3plus_phase_b": [x.to_json() for x in fixed_b],
        "fixed_beta_h3plus_phase_b_c_stress": [x.to_json() for x in fixed_all],
        "phase_c_predictions_from_phase_b_training": [
            predict(h3_b, q_c, y_c),
            predict(h3p_b, q_c, y_c),
        ],
        "candidate_beta_vs_phase_b_free_h3plus": beta_candidate_table(h3p_b),
        "candidate_beta_vs_phase_b_c_free_h3plus": beta_candidate_table(h3p_all),
        "interpretation_guard": {
            "phase_b_h3plus_condition_number": h3p_b.condition_number,
            "phase_b_c_h3plus_condition_number": h3p_all.condition_number,
            "fixed_beta_ic_is_conditional": True,
            "reason": "Fixed-beta comparisons are meaningful as stress probes, but not as post-selection proof of a constant unless the candidate was fixed before inspecting the curve.",
        },
    }

    out_path = Path(__file__).with_suffix(".json")
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {out_path}")
    for item in [h3_b, h3p_b, h3_all, h3p_all]:
        beta_text = ""
        if item.terms and item.terms[0] == "const":
            se = item.se[0] if item.se is not None else float("nan")
            beta_text = f" beta={item.params[0]:.6f}±{se:.6f}"
        aicc_text = "nan" if item.aicc is None else f"{item.aicc:.6f}"
        print(
            f"{item.label}: rmse={item.rmse:.6f} r2={item.r2:.6f} "
            f"aicc={aicc_text}{beta_text}"
        )
    for pred in result["phase_c_predictions_from_phase_b_training"]:
        print(f"{pred['from_fit']} -> q11..15 rmse={pred['rmse']:.6f}")


if __name__ == "__main__":
    main()
