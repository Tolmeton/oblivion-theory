from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=None)
def zeckendorf_indices(n: int) -> tuple[int, ...]:
    if n == 0:
        return ()
    fibs = [0, 1]
    while fibs[-1] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    out: list[int] = []
    rem = n
    k = len(fibs) - 2
    while rem > 0:
        while fibs[k] > rem:
            k -= 1
        out.append(k)
        rem -= fibs[k]
        k -= 2
    return tuple(out)


@lru_cache(maxsize=None)
def fold_value(m: int, n: int) -> int:
    # Fold.lean: Fold(w) = X.ofNat m (weight w). We record only the stable value.
    return sum(fib(k) for k in zeckendorf_indices(n) if 2 <= k <= m + 1)


@lru_cache(maxsize=None)
def weight_counts(m: int) -> tuple[tuple[int, int], ...]:
    counts: dict[int, int] = {0: 1}
    for i in range(m):
        w = fib(i + 2)
        nxt = counts.copy()
        for s, c in counts.items():
            nxt[s + w] = nxt.get(s + w, 0) + c
        counts = nxt
    return tuple(sorted(counts.items()))


@lru_cache(maxsize=None)
def moment_sum(q: int, m: int) -> int:
    mult: dict[int, int] = defaultdict(int)
    for n, c in weight_counts(m):
        mult[fold_value(m, n)] += c
    return sum(v**q for v in mult.values())


def solve_square(a: list[list[int]], b: list[int]) -> list[Fraction] | None:
    n = len(a)
    mat = [[Fraction(x) for x in row] + [Fraction(b[i])] for i, row in enumerate(a)]
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, n):
            if mat[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            return None
        mat[r], mat[pivot] = mat[pivot], mat[r]
        pv = mat[r][c]
        mat[r] = [x / pv for x in mat[r]]
        for i in range(n):
            if i != r and mat[i][c] != 0:
                fac = mat[i][c]
                mat[i] = [mat[i][j] - fac * mat[r][j] for j in range(n + 1)]
        r += 1
    return [mat[i][-1] for i in range(n)]


def minimal_recurrence(seq: list[int], max_order: int = 12) -> list[int]:
    for order in range(1, max_order + 1):
        if len(seq) < 3 * order:
            continue
        mat = [seq[i : i + order] for i in range(order)]
        rhs = [seq[i + order] for i in range(order)]
        coeffs = solve_square(mat, rhs)
        if coeffs is None:
            continue
        if all(
            sum(coeffs[j] * seq[n + j] for j in range(order)) == seq[n + order]
            for n in range(len(seq) - order)
        ):
            if any(c.denominator != 1 for c in coeffs):
                raise ValueError(f"non-integral recurrence: {coeffs}")
            return [int(c) for c in coeffs]
    raise ValueError("no recurrence found")


def companion_matrix(coeffs: list[int]) -> list[list[int]]:
    order = len(coeffs)
    out = [[0] * order for _ in range(order)]
    for i in range(order - 1):
        out[i][i + 1] = 1
    out[-1] = coeffs[:]
    return out


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    m = len(b[0])
    k = len(b)
    out = [[0] * m for _ in range(n)]
    for i in range(n):
        for t in range(k):
            if a[i][t] == 0:
                continue
            for j in range(m):
                out[i][j] += a[i][t] * b[t][j]
    return out


def trace(a: list[list[int]]) -> int:
    return sum(a[i][i] for i in range(len(a)))


def eye(n: int) -> list[list[int]]:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matsub(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] - b[i][j] for j in range(len(a))] for i in range(len(a))]


def det_int(a: list[list[int]]) -> int:
    n = len(a)
    mat = [[Fraction(x) for x in row] for row in a]
    det = Fraction(1)
    sign = 1
    for c in range(n):
        pivot = None
        for i in range(c, n):
            if mat[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            return 0
        if pivot != c:
            mat[c], mat[pivot] = mat[pivot], mat[c]
            sign *= -1
        pv = mat[c][c]
        det *= pv
        for i in range(c + 1, n):
            if mat[i][c] == 0:
                continue
            fac = mat[i][c] / pv
            for j in range(c, n):
                mat[i][j] -= fac * mat[c][j]
    det *= sign
    if det.denominator != 1:
        raise ValueError(f"non-integral determinant: {det}")
    return det.numerator


def lucas(n: int) -> int:
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def recurrence_report(q: int, max_m: int = 25) -> dict[str, object]:
    seq = [moment_sum(q, m) for m in range(max_m)]
    coeffs = minimal_recurrence(seq)
    exact = companion_matrix(coeffs)
    flipped = companion_matrix([-x for x in coeffs])
    report = {
        "q": q,
        "sequence_prefix": seq[:10],
        "coeffs": coeffs,
        "exact": invariant_report(exact, q),
        "signflip": invariant_report(flipped, q),
    }
    return report


def invariant_report(a: list[list[int]], q: int) -> dict[str, int]:
    a2 = matmul(a, a)
    tr = trace(a)
    tr2 = trace(a2)
    return {
        "trace": tr,
        "trace2": tr2,
        "e2": (tr * tr - tr2) // 2,
        "abs_det_I_minus_A": abs(det_int(matsub(eye(len(a)), a))),
        "bf_excess": abs(det_int(matsub(eye(len(a)), a))) - fib(2 * q - 2),
        "lucas": lucas(q),
    }


def print_validation() -> None:
    known = {
        2: [1, 2, 6, 14, 36, 88, 220],
        3: [1, 2, 10, 26, 88, 260, 820],
        4: [1, 2, 18, 50, 228, 808],
        5: [1, 2, 34, 98, 616, 2612, 13444, 62168, 304456],
        6: [1, 2, 66, 194, 1716, 8728, 57820],
        7: [1, 2, 130, 386],
    }
    print("Validation against source-backed moment prefixes")
    for q, prefix in known.items():
        got = [moment_sum(q, m) for m in range(len(prefix))]
        print(f"  q={q}: {got == prefix}  {got}")
    print()


def main() -> None:
    print_validation()

    source_q5 = [10, -20, -8, -11, -2]
    s5 = [moment_sum(5, m) for m in range(10)]
    print("q=5 source-kernel mismatch check")
    for n in range(5):
        lhs = s5[n + 5]
        rhs = sum(source_q5[j] * s5[n + j] for j in range(5))
        print(f"  n={n}: S_5({n+5})={lhs}, source_rhs={rhs}")
    print()

    for q in (5, 6, 7):
        report = recurrence_report(q)
        print(f"q={q}")
        print(f"  sequence prefix = {report['sequence_prefix']}")
        print(f"  exact companion last row = {report['coeffs']}")
        for mode in ("exact", "signflip"):
            inv = report[mode]
            print(
                "  "
                + f"{mode:8s} "
                + f"trace={inv['trace']:>4} "
                + f"trace2={inv['trace2']:>5} "
                + f"e2={inv['e2']:>4} "
                + f"|det(I-A)|={inv['abs_det_I_minus_A']:>4} "
                + f"excess={inv['bf_excess']:>4} "
                + f"Lucas={inv['lucas']:>3}"
            )
        print()


if __name__ == "__main__":
    main()
