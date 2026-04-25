from __future__ import annotations

import importlib.util
import itertools
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

try:
    import numpy as np
except ImportError:  # pragma: no cover - handled in output
    np = None


SCRIPT_DIR = Path(__file__).resolve().parent
Q67_PROBE_PATH = SCRIPT_DIR / "計算_自動数学_キュー六七_探査.py"

LEAN_LAST_ROW_Q5 = [10, -20, -8, -11, -2]
PYTHON_LAST_ROW_Q5 = [-10, 20, 8, 11, 2]

# Coefficients are stored as x^5 + a4*x^4 + ... + a0.
LEAN_CHARPOLY_Q5 = [1, 2, 11, 8, 20, -10]
PYTHON_CHARPOLY_Q5 = [1, -2, -11, -8, -20, 10]


def load_probe_module():
    spec = importlib.util.spec_from_file_location("automath_q67_probe", Q67_PROBE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"failed to load probe module from {Q67_PROBE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PROBE = load_probe_module()


def frobenius_last_row_from_charpoly(coeffs: list[int]) -> list[int]:
    if not coeffs or coeffs[0] != 1:
        raise ValueError("char poly must be monic")
    ascending = list(reversed(coeffs[1:]))
    return [-c for c in ascending]


def companion_matrix(last_row: list[int]) -> list[list[int]]:
    order = len(last_row)
    out = [[0] * order for _ in range(order)]
    for i in range(order - 1):
        out[i][i + 1] = 1
    out[-1] = last_row[:]
    return out


def apply_recurrence(last_row: list[int], seq: list[int], start: int) -> int:
    order = len(last_row)
    return sum(last_row[j] * seq[start + j] for j in range(order))


def anti_reflection_identity() -> list[int]:
    return [a + b for a, b in zip(LEAN_CHARPOLY_Q5, PYTHON_CHARPOLY_Q5)]


def phase0_sequence_checks() -> dict[str, object]:
    s5 = [PROBE.moment_sum(5, m) for m in range(20)]
    ratios = []
    for m in range(5):
        prediction = apply_recurrence(LEAN_LAST_ROW_Q5, s5, m)
        actual = s5[m + 5]
        ratios.append(
            {
                "m": m,
                "prediction": prediction,
                "actual": actual,
                "ratio": str(Fraction(prediction, actual)),
            }
        )

    transforms = {
        "T1": lambda m: s5[m],
        "T2": lambda m: -s5[m],
        "T3": lambda m: ((-1) ** m) * s5[m],
        "T4_k1": lambda m: s5[m + 1],
        "T4_k2": lambda m: s5[m + 2],
    }
    transform_report = {}
    for name, fn in transforms.items():
        rows = []
        matched = True
        for m in range(5):
            lhs = fn(m + 5)
            rhs = sum(LEAN_LAST_ROW_Q5[j] * fn(m + j) for j in range(5))
            rows.append({"m": m, "lhs": lhs, "rhs": rhs, "match": lhs == rhs})
            matched = matched and (lhs == rhs)
        transform_report[name] = {"matched_all": matched, "rows": rows}

    return {
        "s5_prefix": s5[:10],
        "lean_ratio_check": ratios,
        "transforms": transform_report,
    }


def word_from_mask(mask: int, m: int) -> tuple[bool, ...]:
    return tuple(bool((mask >> i) & 1) for i in range(m))


def weight_of_word(bits: tuple[bool, ...], reverse_input: bool = False) -> int:
    total = 0
    m = len(bits)
    for i, bit in enumerate(bits):
        if not bit:
            continue
        fib_index = (m + 1 - i) if reverse_input else (i + 2)
        total += PROBE.fib(fib_index)
    return total


def stable_word_from_nat(m: int, n: int, reverse_output: bool = False) -> tuple[bool, ...]:
    indices = set(PROBE.zeckendorf_indices(n))
    out = []
    for i in range(m):
        fib_index = (m + 1 - i) if reverse_output else (i + 2)
        out.append(fib_index in indices)
    return tuple(out)


def fold_word(
    bits: tuple[bool, ...], reverse_input: bool = False, reverse_output: bool = False
) -> tuple[bool, ...]:
    return stable_word_from_nat(
        len(bits),
        weight_of_word(bits, reverse_input=reverse_input),
        reverse_output=reverse_output,
    )


@lru_cache(maxsize=None)
def moment_sum_variant(
    q: int, m: int, reverse_input: bool = False, reverse_output: bool = False
) -> int:
    multiplicities: dict[tuple[bool, ...], int] = {}
    for mask in range(1 << m):
        bits = word_from_mask(mask, m)
        folded = fold_word(bits, reverse_input=reverse_input, reverse_output=reverse_output)
        multiplicities[folded] = multiplicities.get(folded, 0) + 1
    return sum(mult**q for mult in multiplicities.values())


def phase1_convention_check() -> dict[str, object]:
    lean_expected = frobenius_last_row_from_charpoly(LEAN_CHARPOLY_Q5)
    python_expected = frobenius_last_row_from_charpoly(PYTHON_CHARPOLY_Q5)
    return {
        "lean_expected_last_row": lean_expected,
        "lean_actual_last_row": LEAN_LAST_ROW_Q5,
        "lean_matches_signed_frobenius": lean_expected == LEAN_LAST_ROW_Q5,
        "python_expected_last_row": python_expected,
        "python_actual_last_row": PYTHON_LAST_ROW_Q5,
        "python_matches_signed_frobenius": python_expected == PYTHON_LAST_ROW_Q5,
        "anti_reflection_coefficients": anti_reflection_identity(),
    }


def phase2_basis_check() -> dict[str, object]:
    variants = {
        "forward": (False, False),
        "backward_output": (False, True),
        "backward_input": (True, False),
        "backward_both": (True, True),
    }
    report = {}
    for name, (reverse_input, reverse_output) in variants.items():
        seq = [moment_sum_variant(5, m, reverse_input, reverse_output) for m in range(18)]
        coeffs = PROBE.minimal_recurrence(seq, max_order=8)
        report[name] = {
            "sequence_prefix": seq[:10],
            "last_row": coeffs,
            "matches_lean": coeffs == LEAN_LAST_ROW_Q5,
            "matches_python_exact": coeffs == PYTHON_LAST_ROW_Q5,
        }
    return report


def serialize_complex_list(values: list[complex]) -> list[dict[str, float]]:
    return [{"re": float(v.real), "im": float(v.imag)} for v in values]


def best_negation_match(a: list[complex], b: list[complex]) -> dict[str, object]:
    best = None
    for perm in itertools.permutations(range(len(a))):
        errors = [abs(a[i] + b[perm[i]]) for i in range(len(a))]
        candidate = (max(errors), sum(errors), perm, errors)
        if best is None or candidate[:2] < best[:2]:
            best = candidate
    assert best is not None
    return {
        "max_abs_error": float(best[0]),
        "sum_abs_error": float(best[1]),
        "permutation": list(best[2]),
        "per_pair_errors": [float(x) for x in best[3]],
    }


def phase3_d2_check() -> dict[str, object]:
    if np is None:
        return {"numpy_available": False}

    lean_matrix = np.array(companion_matrix(LEAN_LAST_ROW_Q5), dtype=float)
    python_matrix = np.array(companion_matrix(PYTHON_LAST_ROW_Q5), dtype=float)
    lean_eigs = list(np.linalg.eigvals(lean_matrix))
    python_eigs = list(np.linalg.eigvals(python_matrix))
    return {
        "numpy_available": True,
        "lean_eigenvalues": serialize_complex_list(lean_eigs),
        "python_eigenvalues": serialize_complex_list(python_eigs),
        "negation_match": best_negation_match(lean_eigs, python_eigs),
        "charpoly_negation_witness": {
            "minus_p_lean_minus_x": [1, -2, 11, -8, 20, 10],
            "p_python": PYTHON_CHARPOLY_Q5,
            "matches_pure_lambda_to_minus_lambda": False,
        },
    }


def main() -> None:
    report = {
        "phase0": phase0_sequence_checks(),
        "phase1": phase1_convention_check(),
        "phase2": phase2_basis_check(),
        "phase3": phase3_d2_check(),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
