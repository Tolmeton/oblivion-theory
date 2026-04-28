# E-XIII-C3-04b Non-FLRW TOV Stress Matrix

**日付**: 2026-04-26
**input**: `XIII_C3_non_flrw_tov_symbolic_ledger.md`
**target**: O4 coupling beyond FLRW

---

## 1. Test Matrix

| id | observation | container reading | content reading | verdict |
|:---|:---|:---|:---|:---|
| M1. non-FLRW separator | metric depends on `r` through `m(r)` and `Phi(r)` | container has radial structure, not scale-factor-only evolution | content can vary radially through `rho(r), p(r)` | PASS |
| M2. density slot | `G^t_t = -2m'(r)/r^2` | mass function gradient is the conserved projection's time slot | `T^t_t = -rho(r)` | PASS |
| M3. pressure slot | `G^r_r` contains `Phi'(r)` and `m(r)` | radial geometry supplies pressure coupling slot | `T^r_r = p(r)` | PASS |
| M4. angular pressure consistency | `G^phi_phi - G^theta_theta = 0` | spherical isotropy keeps angular container slots aligned | perfect fluid uses same tangential pressure `p(r)` | PASS with symmetry limit |
| M5. conservation bridge | `div T^mu_r = p' + (rho+p)Phi'` | radial potential controls content balance | pressure gradient cannot be chosen independently | PASS |
| M6. TOV coupling | `Phi' = (m+4 pi r^3 p)/(r(r-2m))` plus conservation gives TOV | geometry and pressure enter the same radial balance | density and pressure are constrained by container geometry | PASS |

---

## 2. Failure Matrix

| failure | result |
|:---|:---|
| F1: FLRW-only slot coincidence | NO. TOV gives non-FLRW radial slot matching. |
| F2: conservation bridge trivializes | NO. Conservation gives nontrivial `p'(r)` balance. |
| F3: C3 theorem follows | NO. This is still static spherical perfect fluid. |
| F4: physical EOS is derived | NO. Equation of state remains external. |
| F5: coefficient/action/general case closed | NO. `8 pi`, action principle, and general GR remain open. |

---

## 3. Interpretation

The TOV probe is stronger than flat FLRW for O4 because it introduces a radial pressure gradient. In FLRW, conservation becomes a time-continuity equation for homogeneous density and pressure. In TOV, conservation becomes a radial equilibrium condition:

```text
p'(r) + (rho(r)+p(r)) Phi'(r) = 0
```

Thus the content side is not merely placed into the same diagonal tensor slots. It is constrained by the container-side radial potential.

---

## 4. Boundary

This is not a general GR proof. It remains:

```text
static + spherical + perfect-fluid + isotropic-pressure
```

The next non-FLRW stress test, if needed, should split radial and tangential pressure via anisotropic stress. That would test whether the dictionary survives once the content side has more than one pressure slot.
