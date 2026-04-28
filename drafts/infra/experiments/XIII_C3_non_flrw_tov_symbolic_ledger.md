# E-XIII-C3-04b TOV Symbolic Ledger

**日付**: 2026-04-26
**対象**: static spherically symmetric perfect fluid
**判定対象**: O4 coupling が non-FLRW でも残るか

---

## 1. External SOURCE

| id | source | supports |
|:---|:---|:---|
| TOV-S1 | Tolman, "Static solutions of Einstein's field equations for spheres of fluid", CaltechAUTHORS / DOI metadata, published 1939, DOI `10.1103/PhysRev.55.364` | Einstein field equations applied to static spheres of fluid |
| TOV-S2 | Oppenheimer and Volkoff, "On Massive Neutron Cores", Physical Review / DOI metadata, published 1939, DOI `10.1103/PhysRev.55.374` | gravitational equilibrium of neutron masses using equation of state and general relativity |

**limit**: TOV-S1/TOV-S2 は TOV 型問題の標準的接地である。下の具体的な component 計算は local symbolic run を SOURCE とする。

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

T^mu_nu = diag(-rho(r), p(r), p(r), p(r))
```

The run computes Christoffel symbols, Ricci tensor, scalar curvature, mixed Einstein tensor, and mixed divergence of `T^mu_nu`.

Local verification environment:

```text
SymPy 1.14.0
```

---

## 3. Symbolic Output

```text
G^t_t = -2*Derivative(m(r), r)/r**2

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

div T^mu_r =
  p(r)*Derivative(Phi(r), r)
  + rho(r)*Derivative(Phi(r), r)
  + Derivative(p(r), r)
```

---

## 4. Derived GR Relations

Using `G^mu_nu = 8 pi T^mu_nu`:

```text
G^t_t = -8 pi rho
=> m'(r) = 4 pi r^2 rho(r)
```

```text
G^r_r = 8 pi p
=> Phi'(r) = (m(r) + 4 pi r^3 p(r)) / (r * (r - 2m(r)))
```

Using `div T^mu_r = 0`:

```text
p'(r) + (rho(r) + p(r)) Phi'(r) = 0
```

Combining the last two:

```text
p'(r) = -(rho(r) + p(r))
        * (m(r) + 4 pi r^3 p(r))
        / (r * (r - 2m(r)))
```

This is the TOV balance form for the present units and conventions.

---

## 5. SOURCE / INFERENCE Split

**SOURCE**

1. Static fluid spheres and relativistic stellar equilibrium are standard GR problems supported by TOV-S1/TOV-S2.
2. The local symbolic run gives the component slots above.
3. The radial conservation equation includes `p'(r)` and `Phi'(r)`.

**INFERENCE**

Paper XIII reads this as:

```text
container-side radial geometry
  <-> content-side density / pressure / pressure-gradient slots
```

This forgetful-theory reading is not in Tolman or Oppenheimer-Volkoff. It is C3 theory work.
