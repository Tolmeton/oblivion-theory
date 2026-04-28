# E-XIII-C3-04d Anisotropic TOV Symbolic Ledger

**日付**: 2026-04-26
**対象**: static spherically symmetric anisotropic stress
**判定対象**: O4 coupling が `p_r != p_t` でも残るか

---

## 1. External SOURCE

| id | source | supports |
|:---|:---|:---|
| TOV-S1 | Tolman, "Static solutions of Einstein's field equations for spheres of fluid", DOI `10.1103/PhysRev.55.364` | static spherical stress in Einstein equations |
| TOV-S2 | Oppenheimer and Volkoff, "On Massive Neutron Cores", DOI `10.1103/PhysRev.55.374` | relativistic hydrostatic equilibrium in GR |
| E04b-SYM | `XIII_C3_non_flrw_tov_symbolic_ledger.md` | baseline metric and symbolic method |

**limit**: TOV-S1/TOV-S2 は static spherical GR probe の標準的接地である。下の具体的な anisotropic component 計算は local symbolic run を SOURCE とする。

---

## 2. Local Symbolic Setup

```text
coords = (t, r, theta, phi)
metric = diag(
  -exp(2 Phi(r)),
  1/(1 - 2m(r)/r),
  r^2,
  r^2 sin(theta)^2
)

T^mu_nu = diag(-rho(r), p_r(r), p_t(r), p_t(r))
```

The run computes Christoffel symbols, Ricci tensor, scalar curvature, mixed Einstein tensor, and mixed divergence of `T^mu_nu`.

Local verification environment:

```text
SymPy 1.14.0
```

---

## 3. Symbolic Output

```text
G^t_t =
  -2*Derivative(m(r), r)/r**2

G^r_r =
  2*(r**2*Derivative(Phi(r), r)
     - 2*r*m(r)*Derivative(Phi(r), r)
     - m(r))/r**3

G^theta_theta =
  (r**3*Derivative(Phi(r), r)**2
   + r**3*Derivative(Phi(r), (r, 2))
   - 2*r**2*m(r)*Derivative(Phi(r), r)**2
   - 2*r**2*m(r)*Derivative(Phi(r), (r, 2))
   - r**2*Derivative(Phi(r), r)*Derivative(m(r), r)
   + r**2*Derivative(Phi(r), r)
   - r*m(r)*Derivative(Phi(r), r)
   - r*Derivative(m(r), r)
   + m(r))/r**3

G^phi_phi - G^theta_theta = 0
```

The anisotropic conservation equation is:

```text
div T^mu_r =
  (r*p_r(r)*Phi'(r)
   + r*rho(r)*Phi'(r)
   + r*p_r'(r)
   + 2*p_r(r)
   - 2*p_t(r))/r
```

Equivalently:

```text
p_r'(r) + (rho(r) + p_r(r)) Phi'(r)
  + 2*(p_r(r) - p_t(r))/r = 0
```

The local run verified:

```text
divT_r - expected = 0
PASS: anisotropic TOV component identities verified
```

---

## 4. Derived GR Relations

Using `G^mu_nu = 8 pi T^mu_nu`:

```text
G^t_t = -8 pi rho
=> m'(r) = 4 pi r^2 rho(r)
```

```text
G^r_r = 8 pi p_r
=> Phi'(r) = (m(r) + 4 pi r^3 p_r(r)) / (r * (r - 2m(r)))
```

```text
G^theta_theta = 8 pi p_t
=> tangential pressure is tied to the angular curvature slot
```

Using `div T^mu_r = 0`:

```text
p_r'(r)
  = -(rho(r) + p_r(r))
      * (m(r) + 4 pi r^3 p_r(r))
      / (r * (r - 2m(r)))
    - 2*(p_r(r) - p_t(r))/r
```

or:

```text
p_r'(r)
  = -(rho(r) + p_r(r))
      * (m(r) + 4 pi r^3 p_r(r))
      / (r * (r - 2m(r)))
    + 2*(p_t(r) - p_r(r))/r
```

When `p_t=p_r`, the anisotropic term disappears and the E-XIII-C3-04b perfect-fluid TOV balance is recovered.

---

## 5. SOURCE / INFERENCE Split

**SOURCE**

1. Static spherical GR probe and perfect-fluid baseline are supported by TOV-S1/TOV-S2 and E04b-SYM.
2. The local symbolic run gives the mixed Einstein tensor slots and anisotropic conservation equation above.
3. `p_t` enters `div T=0` as `2(p_r-p_t)/r`.

**INFERENCE**

Paper XIII reads this as:

```text
container-side radial/angular geometry
  <-> content-side density / radial pressure / tangential pressure / anisotropic imbalance slots
```

This forgetful-theory reading is not in Tolman or Oppenheimer-Volkoff. It is C3 theory work.
