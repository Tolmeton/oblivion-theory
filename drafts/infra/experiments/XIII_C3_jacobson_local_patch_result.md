# E-XIII-C3-04c Result

**日付**: 2026-04-26
**状態**: Jacobson-style local patch 完了
**判定**: C2/C3 の局所物理 bridge は source-backed support を得た。定理昇格なし。

---

## 1. Kernel Result

Jacobson (1995) は、C3 の O4 coupling を局所物理の文法へ接続する強い外部 realization candidate である。

```text
local causal horizon
  + content heat flux across it
  + horizon-area entropy response
  + Raychaudhuri focusing
  + conservation / Bianchi closure
  -> Einstein equation as local equation of state
```

Paper XIII 側では、これは次のように読む。

```text
container boundary / local comparison surface
  <-> content flux through that boundary
  -> conserved coupling projection
```

---

## 2. What Became Stronger

| point | before | after |
|:---|:---|:---|
| C2/C3 bridge | GR instance support | local physical mechanism support |
| O3 closure | Bianchi role-level support | Jacobson uses conservation + Bianchi in the derivation path |
| O4 coupling | FLRW/TOV tensor slot support | heat-flux / area-response consistency support |
| container/content order | metric or radial geometry required | causal horizon and observer calibration required before heat flux is defined |

---

## 3. What Did Not Change

| open item | reason |
|:---|:---|
| Face Lemma 3射 minimality | Jacobson does not prove this |
| entropy-area microscopic origin | assumed/motivated, not derived here |
| local equilibrium | required boundary condition |
| theorem-level C3 | still not reached |
| C1 four-force unification | not addressed |

---

## 4. Updated Verdict

**判定**: source-backed local physical bridge.

E-XIII-C3-04c strengthens the paper because it shows that C3's intended grammar is not only a tensor-slot reading of known GR equations. Jacobson gives a local physical route in which a causal boundary, content flux, area response, curvature focusing, and Bianchi closure sit in one derivation path.

The honest claim is:

```text
Jacobson supplies a local physical realization candidate for C2/C3 coupling.
```

not:

```text
Jacobson proves Face Lemma.
```

---

## 5. Paper XIII Editing Contract

If this returns to the manuscript, it should enter §8 as a support note for O4, not as the main proof.

Suggested claim level:

```text
[構造的対応] Jacobson's local Rindler-horizon derivation gives an external realization candidate for the C2/C3 bridge: heat flux is defined relative to a local causal boundary, area change supplies the container-side response, Raychaudhuri focusing gives the Ricci-side curvature term, and conservation plus the contracted Bianchi identity closes the tensor equation. This supports the coupling dictionary locally, but it does not prove the Face Lemma dictionary or derive the entropy-area input.
```

Next line: either integrate E-03/E-04b/E-04c into a single §8 local-closure subsection, or run anisotropic stress as a final stress test.
