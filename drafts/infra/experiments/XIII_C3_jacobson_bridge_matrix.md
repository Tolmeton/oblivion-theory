# E-XIII-C3-04c Jacobson Bridge Matrix

**日付**: 2026-04-26
**input**: `XIII_C3_jacobson_source_ledger.md`
**target**: C2/C3 local physics bridge

---

## 1. Bridge Matrix

| Jacobson side | C2/C3 reading | support level | verdict |
|:---|:---|:---|:---|
| local Rindler horizon through each point | local comparison surface / container boundary | physical realization candidate | PASS |
| heat flux across causal horizon | content crossing the container boundary | content-side flux slot | PASS |
| horizon area entropy | container deformation has thermodynamic observable | container-side response slot | PASS with assumption |
| Unruh temperature for local accelerated observer | local measurement frame for flux/entropy comparison | observer-local calibration | PASS |
| Raychaudhuri focusing | raw curvature response from content flux | O2 raw defect -> Ricci contraction bridge | PASS |
| null-direction relation `T_ab k^a k^b` vs `R_ab k^a k^b` | direction-wise comparison before tensor closure | O1/O2 local-direction support | PASS |
| conservation + contracted Bianchi identity | projected syndrome closure | O3 bridge | PASS |
| Einstein equation as equation of state | coupling as local consistency condition | O4 bridge | PASS with boundary |
| local equilibrium requirement | scope boundary | prevents theorem overclaim | PASS |

---

## 2. What This Adds To E-03 / E-04b

E-03 and E-04b tested GR instances:

```text
FLRW -> density / pressure slots
TOV  -> density / pressure / radial pressure-gradient slots
```

E-04c tests a different axis:

```text
local causal horizon -> heat flux -> area response -> curvature focusing -> Einstein equation
```

This is not another solution class. It is a local physical mechanism that makes the C2/C3 bridge less ad hoc.

---

## 3. C2 Connection

C2 says container precedes content in definability. Jacobson supports a local analogue:

```text
causal horizon / local observer / null direction
```

must be specified before `dQ` can be read as heat flux across the boundary. The content flux is not a free-floating object; it is defined relative to a local causal boundary and observer calibration.

This supports C2 only at structural level. It does not prove Paper VIII.

---

## 4. C3 Connection

C3 needs O1-O4:

| O-step | Jacobson bridge |
|:---|:---|
| O1 type assignment | null direction, local horizon, boost observer supply direction / comparison / transport roles |
| O2 defect | Raychaudhuri focusing makes curvature response visible |
| O3 closure | conservation + contracted Bianchi identity produce tensor-level closure |
| O4 coupling | `dQ = T dS` demands matching between content flux and container area response, yielding Einstein equation as local consistency condition |

The bridge is strongest for O3/O4. It is weaker for the original Face Lemma 3射 claim, because Jacobson does not formulate a 3-arrow minimality theorem.

---

## 5. Failure Matrix

| failure | result |
|:---|:---|
| F1: Jacobson proves忘却論 | NO. It is external SOURCE for a local physical bridge, not proof of the theory. |
| F2: entropy-area is derived | NO. It is assumed/motivated, not closed here. |
| F3: equilibrium boundary can be ignored | NO. Local equilibrium is required. |
| F4: Face Lemma equals Einstein equation | NO. The bridge is layered: comparison surface, focusing, Bianchi closure, coupling. |
| F5: C1 follows | NO. This only supports C2/C3 local bridge. |

---

## 6. Interpretation

Jacobson is valuable because it turns the coupling problem from:

```text
Why should G_mu_nu equal T_mu_nu?
```

into:

```text
What local consistency condition makes content flux through a causal boundary match the container-side area response?
```

That is close to Paper XIII's intended grammar. It is still not a theorem of忘却論, but it is a strong external realization candidate.
