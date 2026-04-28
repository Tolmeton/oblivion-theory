# E-XIII-C3-04d Result

**日付**: 2026-04-26
**状態**: anisotropic TOV stress test 完了
**判定**: O4 は static spherical anisotropic stress でも局所支持を維持。定理昇格なし。

---

## 1. Kernel Result

Anisotropic TOV probe は、04b の isotropic perfect-fluid 制限を一段外した。

```text
G^t_t      <->  rho(r)
G^r_r      <->  p_r(r)
G^theta_theta = G^phi_phi  <->  p_t(r)
div T=0    <->  p_r' + (rho+p_r)Phi' + 2(p_r-p_t)/r = 0
```

さらに `G^r_r=8 pi p_r` から:

```text
Phi'(r) = (m(r) + 4 pi r^3 p_r(r)) / (r * (r - 2m(r)))
```

が出るので、conservation と組み合わせると:

```text
p_r'(r)
  = -(rho(r) + p_r(r))
      * (m(r) + 4 pi r^3 p_r(r))
      / (r * (r - 2m(r)))
    + 2*(p_t(r) - p_r(r))/r
```

となる。

---

## 2. What Became Stronger

| point | before | after |
|:---|:---|:---|
| O4 coupling | static spherical perfect fluid support | static spherical anisotropic support を追加 |
| pressure slots | one pressure `p(r)` | radial `p_r(r)` and tangential `p_t(r)` split |
| conservation bridge | radial pressure balance | radial balance plus explicit anisotropic imbalance |
| high-symmetry objection | FLRW-only objection weakened by 04b | isotropic-fluid-only objection weakened by 04d |
| 04b continuity | perfect-fluid TOV | recovered by setting `p_t=p_r` |

---

## 3. What Did Not Change

| open item | reason |
|:---|:---|
| theorem-level C3 | still static spherical diagonal stress |
| coefficient `8 pi` | used as standard GR coupling, not derived by 忘却論 |
| Einstein-Hilbert action | not used |
| physical EOS | not derived; `rho, p_r, p_t` relations remain external |
| general non-spherical / non-diagonal stress | not tested |

---

## 4. Updated Verdict

**判定**: anisotropic local support.

E-XIII-C3-04d shows that O4 is not merely perfect-fluid pressure-slot matching. Once radial and tangential pressure split, the split appears in the conservation bridge as an explicit imbalance term.

This strengthens C3 locally, but only locally. The honest claim is:

```text
O4 survives a static spherical anisotropic-stress test.
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
[構造的対応] In the anisotropic TOV-type static spherical probe, the conserved geometric projection still occupies the density, radial-pressure, and tangential-pressure slots of the content tensor. The conservation equation gains the explicit anisotropic term 2(p_r-p_t)/r, so the dictionary sees pressure anisotropy rather than collapsing it into the perfect-fluid case. This weakens the objection that the O4 support depends on isotropic perfect fluid, but it does not derive the coupling coefficient, action principle, or general GR case.
```

Next line: leave static spherical symmetry, or normalize §8 citations and transitions for the warmed draft.
