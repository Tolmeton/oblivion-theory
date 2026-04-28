# E-XIII-C3-04b Result

**日付**: 2026-04-26
**状態**: non-FLRW TOV stress test 完了
**判定**: O4 は static spherical perfect fluid でも局所支持を維持。定理昇格なし。

---

## 1. Kernel Result

TOV 型 probe は、flat FLRW の高対称性だけではない O4 support を与えた。

```text
G^t_t  <->  rho(r)
G^r_r  <->  p(r)
div T=0  <->  p'(r) + (rho(r)+p(r)) Phi'(r) = 0
```

さらに `G^r_r=8 pi p` から

```text
Phi'(r) = (m(r) + 4 pi r^3 p(r)) / (r * (r - 2m(r)))
```

が出るので、conservation と組み合わせると

```text
p'(r) = -(rho(r) + p(r))
        * (m(r) + 4 pi r^3 p(r))
        / (r * (r - 2m(r)))
```

となる。

---

## 2. What Became Stronger

| point | before | after |
|:---|:---|:---|
| O4 coupling | flat FLRW single-instance support | non-FLRW static spherical support を追加 |
| conservation bridge | homogeneous continuity equation | radial pressure-balance equation |
| container/content order | metric-dependent `T_ii` slot | radial geometry controls `p'(r)` through `Phi'(r)` |
| high-symmetry objection | open | FLRW-only objection is weakened |

---

## 3. What Did Not Change

| open item | reason |
|:---|:---|
| theorem-level C3 | TOV is still one symmetry class |
| coefficient `8 pi` | used as standard GR coupling, not derived by忘却論 |
| Einstein-Hilbert action | not used |
| physical EOS | not derived; `rho(p)` remains external |
| anisotropic / non-perfect-fluid case | not tested |

---

## 4. Updated Verdict

**判定**: non-FLRW local support.

E-XIII-C3-04b shows that O4 is not merely the result of FLRW diagonal slot matching. In a static spherical perfect fluid, the content side has a radial pressure gradient, and that gradient is constrained by the container-side potential.

This strengthens C3, but only locally. The honest claim is:

```text
O4 survives a first non-FLRW stress test.
```

not:

```text
Einstein equations have been derived from Face Lemma.
```

---

## 5. Paper XIII Editing Contract

If this returns to the manuscript, it should enter §8 as a stress-test note, not as a theorem.

Suggested claim level:

```text
[構造的対応] In the TOV-type static spherical perfect-fluid probe, the conserved geometric projection still occupies the same density/pressure slots as the content tensor, and the conservation equation becomes a radial pressure-balance condition. This weakens the objection that the FLRW result is only a high-symmetry coincidence, but it does not derive the coupling coefficient or the action principle.
```

Next line: anisotropic stress or Jacobson-style local thermodynamic patch.
