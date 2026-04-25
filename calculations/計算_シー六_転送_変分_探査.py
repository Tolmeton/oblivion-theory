#!/usr/bin/env python3
"""Small numerical probes for the C6 alpha=1/5 derivation attempt.

The script intentionally uses only the Python standard library. It checks:
- transfer-matrix block powers for the golden-mean shift,
- the natural hard-core density at fugacity z=1,
- the Euler cumulative alpha_E(theta) at theta=pi/5,
- the cyclotomic/Galois orbit of zeta_10.
"""

from __future__ import annotations

import cmath
import math


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


def matpow(a: list[list[int]], n: int) -> list[list[int]]:
    result = [[1, 0], [0, 1]]
    base = a
    while n:
        if n & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        n >>= 1
    return result


def main() -> None:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    psi = (1.0 - math.sqrt(5.0)) / 2.0
    transfer = [[1, 1], [1, 0]]

    print("transfer_matrix_probe")
    print(f"phi={phi:.15f}")
    print(f"psi={psi:.15f}")
    for block in [1, 2, 3, 4, 5, 8, 10]:
        tb = matpow(transfer, block)
        lucas = tb[0][0] + tb[1][1]
        correction = (psi / phi) ** block
        print(
            "block={:2d} T^b={} trace={} rho=phi^b={:.15f} finite_correction={:.15f}".format(
                block,
                tb,
                lucas,
                phi**block,
                correction,
            )
        )

    print("\nhard_core_variational_proxy")
    z = 1.0
    lam = (1.0 + math.sqrt(1.0 + 4.0 * z)) / 2.0
    density = z / (lam * math.sqrt(1.0 + 4.0 * z))
    print(f"lambda(z=1)={lam:.15f}")
    print(f"occupancy_density_at_z1={density:.15f}")
    print("target_1_over_5={:.15f}".format(1.0 / 5.0))

    print("\neuler_cumulative_probe")
    theta = math.pi / 5.0
    alpha_e = (1.0 - math.cos(theta)) / 2.0
    theta_for_alpha_1_5 = math.acos(1.0 - 2.0 / 5.0)
    print(f"alpha_E(pi/5)={alpha_e:.15f}")
    print(f"theta_for_alpha_E=1/5={theta_for_alpha_1_5:.15f}")
    print(f"theta_for_alpha_E=1/5_over_pi={theta_for_alpha_1_5 / math.pi:.15f}")

    print("\ngalois_orbit_zeta10")
    for a in [1, 3, 7, 9]:
        value = cmath.exp(1j * math.pi * a / 5.0)
        real_sum = value + value.conjugate()
        print(
            "a={} angle={}pi/5 real_sum={:.15f}".format(
                a,
                a,
                real_sum.real,
            )
        )

    print("\nreparameterization_witness")
    alpha = 1.0 / 5.0
    print(f"alpha={alpha:.15f}")
    print(f"r(alpha)=alpha^2={alpha * alpha:.15f}")
    print(f"r_inv(alpha)=sqrt(alpha)={math.sqrt(alpha):.15f}")


if __name__ == "__main__":
    main()
