# E-XIII-C3-02 Matrix

**問い**: contracted Bianchi identity `∇^μG_{μν}=0` は、Face Lemma 側の closure / syndrome conservation として働くか。
**判定方式**: 5 probe。hard fail が 1 つでも出れば O3 は skeleton 維持。

---

## Probe Matrix

| probe | SOURCE / observation | Face-side role | GR-side role | result |
|:---|:---|:---|:---|:---|
| M0. 概念境界 | `FaceLemma.md` は Face Lemma を comparison surface の最小条件とし、Einstein dictionary を skeleton と置く。 | Face Lemma は detectability まで。closure と recoverability は別層。 | `G_{μν}` を Face Lemma そのものに同一化してはならない。 | PASS |
| M1. raw defect separator | E-XIII-C3-01 は `Einstein tensor = raw defect` を棄却した。Schwarzschild exterior では Riemann nonzero / Ricci-G-T zero がありうる。 | raw defect は比較面に現れる transport drift として読む。 | Riemann/holonomy が raw defect、`G_{μν}` は raw defect ではない。 | PASS |
| M2. conserved projection | XIII §8.2 は Einstein tensor を Ricci 曲率の divergence-free 部分と書き、§8.2.1 O3 は `∇^μG_{μν}=0` の翻訳を義務にしている。 | syndrome が露出した後、それが内容へ結合可能な保存型 projection へ落ちるかを見る。 | contracted Bianchi は `G_{μν}` を coupling-ready な rank-2 projection にする。 | PASS |
| M3. stress-energy 非輸入 | XIII §8.2.1 は O3 closure と O4 coupling を分けている。 | closure は coupling の前提であって、coupling の結果ではない。 | `∇^μT_{μν}=0` を先に仮定せず、geometry side の `∇^μG_{μν}=0` から読む。 | PASS |
| M4. limiting cases | E-XIII-C3-01 は Minkowski / Schwarzschild exterior / FLRW を separator として置いた。 | defect の有無と coupling projection の有無を分離する。 | Minkowski は全 defect zero。Schwarzschild exterior は raw curvature nonzero だが `G_{μν}=0`。FLRW は O4 に残る。 | PASS with limit |
| M5. coherence layer | `FaceLemma_技術設計.md` は Face Lemma を syndrome 条件、Coherence Defect Lemma を local law の global lift obstruction と分ける。 | Bianchi は Face Lemma の別名ではなく、露出した defect projection が保存型に閉じる条件として置く。 | `G_{μν}` は raw curvature ではなく conserved coupling projection。 | PASS with demotion |

---

## Hard Fail Check

| falsifier | observed |
|:---|:---:|
| F1. GR 事実の反復だけで Face 側 role がない | NO |
| F2. `∇^μT_{μν}=0` を先に仮定している | NO |
| F3. raw defect と `G_{μν}` を分離できない | NO |
| F4. O3 から Einstein 方程式全体を導出したことにしている | NO |

---

## Minimal Dictionary After Probe

| layer | Face-side wording | GR-side wording | claim level |
|:---|:---|:---|:---|
| O1 | direction / comparison / transport | tangent direction / metric comparison / Levi-Civita transport witness | motivated construction |
| O2 | raw syndrome / transport defect | Riemann curvature / holonomy defect | role-level support |
| O3 | closure of projected syndrome | contracted Bianchi `∇^μG_{μν}=0` | role-level support |
| O4 | container/content coupling | `G_{μν}=8πG_NT_{μν}` | open |

---

## Matrix Verdict

O3 passes as a **role-level closure**:

```text
Face Lemma exposes raw defect.
Bianchi does not expose the defect; it constrains the projected defect.
Therefore G_{μν} should be read as conserved coupling projection, not raw face area.
```

This is not a theorem-level proof. It is enough to move from E-XIII-C3-01 to an O4 coupling probe.
