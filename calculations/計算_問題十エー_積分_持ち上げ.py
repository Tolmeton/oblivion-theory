#!/usr/bin/env python3
"""Problem 10(a): numerical checks for Iteration 2 integral-lift candidates.

The Iteration 1 minimum-period candidate normalized every non-zero canonical
BF-excess period to +/-1.  This script keeps that candidate for comparison,
but treats the Walsh primitive lattice candidate as the main line:

* A_min_period: lambda_evt = gcd of the listed periods; on the single BF cell
  this is abs(E_q), so it collapses to +/-1 when E_q is non-zero.
* D_weight_last: lambda_evt = fib(q+2), matching the automath bit-q weight.
* E_carry_amp: lambda_evt = fib(q), matching carryElement q.
* F_walsh_primitive: lambda_evt = 1, the primitive integer Walsh-flux lattice.
  This preserves the raw integer BF-excess class E_q.
* G_cell_vector: lambda is cell-dependent and primitive on each listed 2-cell;
  the resulting class records BF, Sym^2, and Lambda^2 sector coordinates.

q=2..5 use Lean-source collision kernels. q=6,7 use the proxy sign-flip
extension recorded in the Yugaku q6q7 probe, not official Lean kernels.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Sequence


Matrix = list[list[int]]


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def det_int(a: Matrix) -> int:
    n = len(a)
    m = [[Fraction(x) for x in row] for row in a]
    det = Fraction(1)
    sign = 1
    for col in range(n):
        pivot = None
        for row in range(col, n):
            if m[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            return 0
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            sign *= -1
        p = m[col][col]
        det *= p
        for row in range(col + 1, n):
            factor = m[row][col] / p
            if factor == 0:
                continue
            for k in range(col, n):
                m[row][k] -= factor * m[col][k]
    out = det * sign
    assert out.denominator == 1
    return out.numerator


def eye_minus(a: Matrix) -> Matrix:
    return [[(1 if i == j else 0) - a[i][j] for j in range(len(a))] for i in range(len(a))]


def trace(a: Matrix) -> int:
    return sum(a[i][i] for i in range(len(a)))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def e2(a: Matrix) -> int:
    tr = trace(a)
    tr2 = trace(matmul(a, a))
    assert (tr * tr - tr2) % 2 == 0
    return (tr * tr - tr2) // 2


def sym2_trace(a: Matrix) -> int:
    tr = trace(a)
    return tr * tr - e2(a)


def companion(last_row: list[int]) -> Matrix:
    n = len(last_row)
    rows = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        rows[i][i + 1] = 1
    rows[-1] = last_row[:]
    return rows


@dataclass(frozen=True)
class QData:
    q: int
    matrix: Matrix
    source: str
    observed_k: int | None


DATA = [
    QData(2, companion([-2, 2, 2]), "Lean collisionKernel2", None),
    QData(3, companion([-2, 4, 2]), "Lean collisionKernel3", None),
    QData(4, companion([-2, 2, 0, 7, 2]), "Lean collisionKernel4", 0),
    QData(5, companion([10, -20, -8, -11, -2]), "Lean collisionKernel5 official", 1),
    QData(6, companion([4, -4, 26, -88, -28, -17, -2]), "proxy sign-flip extension", 1),
    QData(7, companion([42, -84, 34, -311, -74, -26, -2]), "proxy sign-flip extension", 1),
]


def min_period_lambda(periods: Iterable[int]) -> int:
    g = 0
    for x in periods:
        if x:
            g = gcd(g, abs(x))
    return g or 1


def div_if_integral(value: int, lam: int) -> int | None:
    assert lam > 0
    if value % lam != 0:
        return None
    return value // lam


def vector_mod2(values: Sequence[int]) -> tuple[int, ...]:
    return tuple(v % 2 for v in values)


def fmt_cell(key: str, value: object) -> str:
    if value is None:
        return "n/a" if key == "observed_k" else "nonintegral"
    return str(value)


def analyze(d: QData) -> dict[str, int | str | None | tuple[int, ...]]:
    bf = abs(det_int(eye_minus(d.matrix)))
    background = fib(2 * d.q - 2)
    period = bf - background
    c_sym = sym2_trace(d.matrix)
    x_ext = e2(d.matrix)
    sector_vector = (period, c_sym, x_ext)
    lam_min = min_period_lambda([period])
    int_min = period // lam_min
    lam_weight_last = fib(d.q + 2)
    lam_carry_amp = fib(d.q)
    int_weight_last = div_if_integral(period, lam_weight_last)
    int_carry_amp = div_if_integral(period, lam_carry_amp)
    return {
        "q": d.q,
        "source": d.source,
        "tr": trace(d.matrix),
        "C_sym2": c_sym,
        "X_ext2": x_ext,
        "bf_abs": bf,
        "fib_bg": background,
        "E_bf": period,
        "A_lambda": lam_min,
        "A_Int": int_min,
        "A_mod2": int_min % 2,
        "D_lambda_fib_q2": lam_weight_last,
        "D_Int": int_weight_last,
        "E_lambda_fib_q": lam_carry_amp,
        "E_Int": int_carry_amp,
        "F_lambda": 1,
        "F_Int": period,
        "F_mod2": period % 2,
        "G_vector": sector_vector,
        "G_mod2": vector_mod2(sector_vector),
        "observed_k": d.observed_k,
    }


def main() -> None:
    rows = [analyze(d) for d in DATA]
    headers = [
        "q",
        "source",
        "tr",
        "C_sym2",
        "X_ext2",
        "bf_abs",
        "fib_bg",
        "E_bf",
        "A_lambda",
        "A_Int",
        "A_mod2",
        "D_lambda_fib_q2",
        "D_Int",
        "E_lambda_fib_q",
        "E_Int",
        "F_Int",
        "F_mod2",
        "G_vector",
        "G_mod2",
        "observed_k",
    ]
    print("\t".join(headers))
    for r in rows:
        print("\t".join(fmt_cell(h, r[h]) for h in headers))


if __name__ == "__main__":
    main()
