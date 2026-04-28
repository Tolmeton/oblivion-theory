# E-XIII-C3-04c Jacobson Source Ledger

**日付**: 2026-04-26
**対象**: Ted Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State" (1995)
**判定対象**: C2/C3 の局所物理 bridge

---

## 1. External SOURCE

| id | source | supports |
|:---|:---|:---|
| J-S1 | arXiv `gr-qc/9504004`; APS DOI `10.1103/PhysRevLett.75.1260` | bibliographic source |
| J-S2 | APS full text lines 5-10 | Einstein equation is derived from entropy-area proportionality and `dQ = T dS`, using local Rindler causal horizons, energy flux, and Unruh temperature |
| J-S3 | APS full text lines 44-57 | heat is energy flow across a causal horizon; the inaccessible system is separated by a causality barrier |
| J-S4 | APS full text lines 100-120 | local Rindler horizon is constructed at each spacetime point under local equilibrium assumptions |
| J-S5 | APS full text lines 121-127 | the thermodynamic relation can hold only if matter-energy lensing distorts causal structure so that Einstein equation holds |
| J-S6 | APS full text lines 187-206 | Raychaudhuri equation connects null congruence focusing to Ricci curvature, yielding a condition relating `T_ab k^a k^b` and `R_ab k^a k^b` |
| J-S7 | APS full text lines 207-214 | local conservation plus contracted Bianchi identity lifts the null-direction relation to Einstein equation |
| J-S8 | APS full text lines 237-252 | derivation presumes local equilibrium; away from equilibrium local thermodynamic quantities may fail |
| J-S9 | APS full text lines 222-236 | changing entropy functional changes implied field equations; integrability/action issues remain |

---

## 2. SOURCE / INFERENCE Split

**SOURCE**

Jacobson gives a local thermodynamic route:

1. choose local Rindler horizons through each point;
2. define heat as matter energy flux across the causal horizon;
3. use Unruh temperature and horizon-area entropy;
4. use Raychaudhuri focusing to relate flux to Ricci curvature along null directions;
5. use stress-energy conservation and contracted Bianchi identity to obtain the Einstein equation, up to cosmological constant and constants fixed by entropy normalization.

**INFERENCE**

Paper XIII reads this route as a local physical realization candidate for C2/C3:

```text
container-side local causal boundary / area response
  <-> content-side energy flux across that boundary
  -> conserved geometric coupling equation
```

This inference is not Jacobson's claim. It is Paper XIII theory work.

---

## 3. Boundary Ledger

| boundary | status |
|:---|:---|
| entropy-area proportionality | assumed / motivated by horizon information; not derived here |
| local equilibrium | required condition, not optional decoration |
| microscopic spacetime theory | open |
| coefficient | tied to entropy-area proportionality, not derived by忘却論 |
| non-equilibrium spacetime | explicitly outside the equilibrium derivation |
| modified entropy functionals | can imply different field equations; this prevents overclaiming uniqueness |
