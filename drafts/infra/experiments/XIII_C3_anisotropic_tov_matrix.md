# E-XIII-C3-04d Anisotropic TOV Stress Matrix

**日付**: 2026-04-26
**input**: `XIII_C3_anisotropic_tov_symbolic_ledger.md`
**target**: O4 coupling beyond isotropic perfect fluid

---

## 1. Test Matrix

| id | observation | container reading | content reading | verdict |
|:---|:---|:---|:---|:---|
| M1. anisotropic separator | `T^mu_nu=diag(-rho,p_r,p_t,p_t)` | same static spherical container as 04b | content now has radial and tangential pressure slots | PASS |
| M2. density slot | `G^t_t=-2m'/r^2` | mass function gradient remains the time/density projection | `T^t_t=-rho(r)` | PASS |
| M3. radial pressure slot | `G^r_r` fixes `Phi'` through `p_r` | radial geometry supplies radial pressure coupling slot | `T^r_r=p_r(r)` | PASS |
| M4. tangential pressure slot | `G^theta_theta=G^phi_phi` | angular curvature supplies tangential pressure slot | `T^theta_theta=T^phi_phi=p_t(r)` | PASS |
| M5. anisotropic conservation bridge | `div T^mu_r = p_r' + (rho+p_r)Phi' + 2(p_r-p_t)/r` | radial potential plus angular/radial split constrain balance | pressure anisotropy cannot be hidden | PASS |
| M6. perfect-fluid recovery | setting `p_t=p_r` removes the anisotropic term | 04d reduces to 04b under isotropy | perfect-fluid TOV is a special case | PASS |

---

## 2. Failure Matrix

| failure | result |
|:---|:---|
| F1: O4 was isotropic-pressure-only | NO. `p_t` enters the conservation bridge and angular curvature slot. |
| F2: anisotropy is invisible to the dictionary | NO. `2(p_r-p_t)/r` is the explicit anisotropic imbalance term. |
| F3: 04d proves general GR | NO. It is still static + spherical + diagonal anisotropic stress. |
| F4: physical EOS is derived | NO. Relations among `rho, p_r, p_t` remain external. |
| F5: coefficient/action/general case closed | NO. `8 pi`, action principle, and general non-spherical case remain open. |

---

## 3. Interpretation

The anisotropic TOV probe is stronger than E-XIII-C3-04b because it removes the `p_r=p_t` assumption. The conserved projection does not collapse. Instead, the radial balance gains an explicit anisotropic stress term:

```text
p_r'(r) + (rho(r)+p_r(r)) Phi'(r)
  + 2*(p_r(r)-p_t(r))/r = 0
```

This means the content side is not merely filling a single pressure slot. The radial/tangential split is visible in the same conservation bridge that linked container and content in 04b.

---

## 4. Boundary

This is not a general GR proof. It remains:

```text
static + spherical + diagonal anisotropic stress
```

The next stress tests, if needed, should leave static spherical symmetry or introduce non-diagonal flux / shear. That would test whether the dictionary survives once the content side is no longer reducible to radial equilibrium.
