# E-XIII-C3-03 Matrix

**問い**: FLRW の最小 case で、`G_{μν}=κT_{μν}` は容器/内容の非対称整合条件として読めるか。
**判定方式**: 6 probe。hard fail が 1 つでも出れば O4 は open のまま。

---

## Probe Matrix

| probe | SOURCE / observation | container-side role | content-side role | result |
|:---|:---|:---|:---|:---|
| M0. C2 anchor | XIII §2.2 は Einstein 方程式を容器忘却 / 内容忘却の非対称射影として読む。 | 容器は時空 `(M,g)`。内容なしでも真空解がある。 | 内容は `T_{μν}`。容器なしに定義されない。 | PASS |
| M1. VIII anchor | Paper VIII §3.4 は CPS を fiber bundle と読み、底空間はファイバーなしに存在しうるが、ファイバーは底空間なしに定義不能とする。 | 成立場 / 底空間。 | 居住状態 / ファイバー。 | PASS |
| M2. FLRW slot matching | symbolic ledger: `G_00=3H^2`, `G_ii/a^2=-2a''/a-H^2`。 | scale factor の一階/二階情報から conserved projection が出る。 | perfect fluid では `T_00=ρ`, `T_ii/a^2=p`。 | PASS |
| M3. conservation bridge | symbolic ledger: `div G=0`; perfect fluid の `div T=0` は `ρ'+3H(ρ+p)=0`。 | O3 の closure が維持される。 | 内容密度と圧力は任意ではなく conservation slot に従う。 | PASS |
| M4. asymmetry | C2/Paper VIII は容器先行を置く。FLRW でも metric を先に置かなければ `ρ,p` の tensor slot は定義できない。 | `g` が `T` の component expression を支える。 | `T` は `g` によって `a^2 p` の空間成分を持つ。 | PASS |
| M5. no overclaim | symbolic ledger は `κ` を導かない。 | `G` は coupling-ready projection。 | `T` は content-side density/pressure。 | PASS with limit |

---

## Hard Fail Check

| falsifier | observed |
|:---|:---:|
| F1. `G_{μν}` が perfect fluid `T_{μν}` と同じ slot に入らない | NO |
| F2. `G_{μν}` が `ρ,p` を区別できない | NO |
| F3. `div G=0` から content conservation slot が出ない | NO |
| F4. 係数 `κ` や full Einstein equation を導出したことにしている | NO |

---

## Minimal Dictionary After Probe

| layer | Face/CPS-side wording | FLRW-side wording | claim level |
|:---|:---|:---|:---|
| C2 | container/content asymmetry | metric first, stress-energy defined on metric background | source-supported structural anchor |
| O2 | raw curvature defect | scale-factor acceleration / expansion data in curvature | role-level support |
| O3 | conserved projection | `∇_μG^μ_ν=0` | role-level support |
| O4 | container/content consistency | `G_00 ↔ ρ`, `G_ii/a^2 ↔ p`, conservation bridge | single-instance local support |

---

## Matrix Verdict

O4 gets **single-instance local support**:

```text
In flat FLRW, container-side projected curvature and content-side density/pressure occupy the same tensor slots.
The conservation bridge is not imported after the fact; it is visible as div G=0 and div T=0 in the same divergence slot.
```

This does not prove the Einstein equation, the coupling coefficient, or full GR generality.
