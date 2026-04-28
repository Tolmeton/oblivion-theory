# E-XIII-C3-03 Symbolic Ledger

**日付**: 2026-04-26
**engine**: Python / SymPy 1.14.0
**metric**: flat FLRW, coordinates `(t,x,y,z)`, signature `(-,+,+,+)`.

```text
g_{μν} = diag(-1, a(t)^2, a(t)^2, a(t)^2)
T_{μν} = diag(ρ(t), p(t)a(t)^2, p(t)a(t)^2, p(t)a(t)^2)
```

---

## Raw Output 1: Einstein Tensor

Command result:

```text
nonzero Gamma:
Gamma^0_11 = a(t)*Derivative(a(t), t)
Gamma^0_22 = a(t)*Derivative(a(t), t)
Gamma^0_33 = a(t)*Derivative(a(t), t)
Gamma^1_01 = Derivative(a(t), t)/a(t)
Gamma^1_10 = Derivative(a(t), t)/a(t)
Gamma^2_02 = Derivative(a(t), t)/a(t)
Gamma^2_20 = Derivative(a(t), t)/a(t)
Gamma^3_03 = Derivative(a(t), t)/a(t)
Gamma^3_30 = Derivative(a(t), t)/a(t)

Ricci:
R_00 = -3*Derivative(a(t), (t, 2))/a(t)
R_11 = a(t)*Derivative(a(t), (t, 2)) + 2*Derivative(a(t), t)**2
R_22 = a(t)*Derivative(a(t), (t, 2)) + 2*Derivative(a(t), t)**2
R_33 = a(t)*Derivative(a(t), (t, 2)) + 2*Derivative(a(t), t)**2

Scalar R = 6*(a(t)*Derivative(a(t), (t, 2)) + Derivative(a(t), t)**2)/a(t)**2

Einstein:
G_00 = 3*Derivative(a(t), t)**2/a(t)**2
G_11 = -2*a(t)*Derivative(a(t), (t, 2)) - Derivative(a(t), t)**2
G_22 = -2*a(t)*Derivative(a(t), (t, 2)) - Derivative(a(t), t)**2
G_33 = -2*a(t)*Derivative(a(t), (t, 2)) - Derivative(a(t), t)**2
```

Observation:

```text
G_00 = 3H^2
G_ii / a^2 = -2 a''/a - H^2
```

where `H = a'/a`.

---

## Raw Output 2: Divergence

Command result:

```text
div G^mu_nu:
nu=0: 0
nu=1: 0
nu=2: 0
nu=3: 0

div T^mu_nu for perfect fluid:
nu=0: -(a(t)*Derivative(rho(t), t) + 3*p(t)*Derivative(a(t), t) + 3*rho(t)*Derivative(a(t), t))/a(t)
nu=1: 0
nu=2: 0
nu=3: 0
```

Observation:

```text
∇_μ G^μ_ν = 0
∇_μ T^μ_0 = -(a ρ' + 3p a' + 3ρ a')/a
```

Thus `∇_μ T^μ_ν = 0` gives:

```text
ρ' + 3H(ρ+p) = 0
```

---

## Role Extraction

If `G_{μν}=κT_{μν}` is imposed, the component slots become:

```text
3H^2 = κρ
-2a''/a - H^2 = κp
```

This does not derive `κ`. It only shows that, in this minimal instance, container-side projected curvature has the same component slots as content-side density and pressure.

---

## Experimental Status

This ledger is local SOURCE for E-XIII-C3-03. It is not a substitute for GR source citation in a public manuscript.
