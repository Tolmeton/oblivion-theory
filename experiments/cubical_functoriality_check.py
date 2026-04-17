#!/usr/bin/env python3
"""
Cubical functoriality sanity check
==================================

Verifies two exact finite identities used in
`drafts/standalone/automath_bridge/functoriality_reduction.md`.

1. Coordinate restrictions compose strictly.
2. For multilinear observables on [0,1]^n and boundary words w on A,
   deltaSet(A, f|_{vertices}, w)
   = (-1)^|A| * integral_{cell(A,w)} partial_A f.

No external dependencies are required.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from random import Random


def subsets(items: tuple[int, ...]):
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            yield combo


def boundary_words(n: int, A: tuple[int, ...]):
    Aset = set(A)
    free = [i for i in range(n) if i not in Aset]
    for bits in product([0, 1], repeat=len(free)):
        word = [0] * n
        for i, bit in zip(free, bits):
            word[i] = bit
        yield tuple(word)


def flip_set(word: tuple[int, ...], B: tuple[int, ...]) -> tuple[int, ...]:
    out = list(word)
    for i in B:
        out[i] = 1 - out[i]
    return tuple(out)


@dataclass(frozen=True)
class MultilinearPoly:
    coeffs: dict[tuple[int, ...], Fraction]

    def eval_vertex(self, word: tuple[int, ...]) -> Fraction:
        total = Fraction(0, 1)
        for subset, coeff in self.coeffs.items():
            term = coeff
            for i in subset:
                term *= word[i]
            total += term
        return total

    def mixed_partial_cell_integral(
        self, A: tuple[int, ...], word: tuple[int, ...]
    ) -> Fraction:
        """Integral of partial_A over the A-cell anchored at `word`.

        We only use boundary words on A, so the cell orientation is standard.
        For multilinear monomials, integrating the mixed partial over [0,1]^A
        simply removes the A variables and evaluates the remaining fixed bits.
        """
        Aset = set(A)
        total = Fraction(0, 1)
        for subset, coeff in self.coeffs.items():
            if not Aset.issubset(subset):
                continue
            term = coeff
            for i in subset:
                if i in Aset:
                    continue
                term *= word[i]
            total += term
        return total


def delta_set(poly: MultilinearPoly, A: tuple[int, ...], word: tuple[int, ...]) -> Fraction:
    total = Fraction(0, 1)
    for B in subsets(A):
        sign = -1 if (len(B) % 2 == 1) else 1
        total += sign * poly.eval_vertex(flip_set(word, B))
    return total


def restrict_word(word: tuple[int, ...], target_indices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(word[i] for i in target_indices)


def compose_restrictions(word: tuple[int, ...], middle: tuple[int, ...], target: tuple[int, ...]) -> bool:
    first = restrict_word(word, middle)
    second = restrict_word(first, target)
    direct = restrict_word(word, tuple(middle[i] for i in target))
    return second == direct


def random_multilinear_poly(n: int, rng: Random) -> MultilinearPoly:
    coeffs: dict[tuple[int, ...], Fraction] = {}
    indices = tuple(range(n))
    for subset in subsets(indices):
        numer = rng.randint(-3, 3)
        if numer == 0:
            continue
        denom = rng.choice([1, 2, 3])
        coeffs[subset] = Fraction(numer, denom)
    return MultilinearPoly(coeffs=coeffs)


def verify_restrictions():
    for n in range(1, 7):
        word = tuple((i % 2) for i in range(n))
        for mid_size in range(1, n + 1):
            middle = tuple(range(mid_size))
            for tgt_size in range(0, mid_size + 1):
                target = tuple(range(tgt_size))
                assert compose_restrictions(word, middle, target)


def verify_chain_map():
    rng = Random(42)
    for n in range(1, 6):
        indices = tuple(range(n))
        for _ in range(40):
            poly = random_multilinear_poly(n, rng)
            for A in subsets(indices):
                if not A:
                    continue
                for word in boundary_words(n, A):
                    lhs = delta_set(poly, A, word)
                    rhs = ((-1) ** len(A)) * poly.mixed_partial_cell_integral(A, word)
                    assert lhs == rhs, (
                        f"Mismatch for n={n}, A={A}, w={word}: "
                        f"deltaSet={lhs}, integral={rhs}"
                    )


def main():
    verify_restrictions()
    verify_chain_map()
    print("OK: strict restriction composition and cubical chain-map identity verified.")


if __name__ == "__main__":
    main()
