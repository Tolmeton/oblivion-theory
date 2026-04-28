# E-XIII-C3-04c Jacobson Local Patch Protocol

**日付**: 2026-04-26
**mode**: `/ene` L2
**目的**: Jacobson (1995) の local Rindler horizon / Clausius relation により、C2/C3 の container-content coupling が局所物理の文法へ接続できるかを検査する。

---

## 0. Question

E-XIII-C3-03 / 04b は、具体的な GR 解・対称性 class で O4 coupling を試した。

本 probe では、解の class ではなく、局所物理の原理側を見る。問いは次である。

```text
local causal horizon + heat flux + horizon area entropy
  -> curvature focusing
  -> Einstein equation as local consistency condition
```

という Jacobson 型の流れを、Paper XIII の C2/C3 に接続できるか。

---

## 1. Scope

扱うもの:

1. local Rindler horizon
2. heat flux across a causal horizon
3. Unruh temperature
4. entropy proportional to horizon area
5. Raychaudhuri focusing and Ricci curvature
6. conservation + contracted Bianchi identity
7. Einstein equation as equation of state

扱わないもの:

1. Jacobson の導出を忘却論から再証明すること
2. entropy-area proportionality の微視的起源
3. non-equilibrium spacetime
4. `f(R)` / modified gravity
5. 係数の忘却論的導出

---

## 2. Pass Conditions

| id | condition | pass meaning |
|:---|:---|:---|
| J1 | local Rindler horizon が pointwise に立つ | local comparison surface の物理的 realization 候補になる |
| J2 | heat flux が horizon crossing として定義される | content が container boundary を通る量として読める |
| J3 | area change が entropy change として扱われる | container deformation が thermodynamic observable になる |
| J4 | Raychaudhuri equation が `T_ab k^a k^b` と `R_ab k^a k^b` を接続する | content flux と curvature focusing が同じ local null direction で比較される |
| J5 | conservation + Bianchi が tensor equation へ持ち上げる | E-02 の projected syndrome closure と接続できる |
| J6 | local equilibrium condition が明示される | 射程境界を保てる |

---

## 3. Failure Conditions

| id | failure | implication |
|:---|:---|:---|
| F1 | Jacobson を忘却論の証明として輸入する | worldview import。棄却 |
| F2 | horizon entropy を説明済みと読む | 微視的 SOURCE 不足。棄却 |
| F3 | local equilibrium 条件を落とす | Jacobson の射程を過大化 |
| F4 | `Einstein equation = Face Lemma` と同一視する | 層混同。棄却 |
| F5 | C1 四力統一の支持に直行する | C3 局所橋の scope creep |

---

## 4. Expected Output

1. `XIII_C3_jacobson_source_ledger.md`
2. `XIII_C3_jacobson_bridge_matrix.md`
3. `XIII_C3_jacobson_local_patch_result.md`
4. `論文XIII_時空は忘却である.meta.md` の C3 gauntlet / §M6 更新
