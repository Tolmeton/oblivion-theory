# E-XIII-C3-01 Case Matrix

**日付**: 2026-04-26
**対象**: Paper XIII C3, Face Lemma - GR 局所 closure
**状態**: Round 1 paper-probe matrix

## 1. 役割分離

Round 1 の中心修正は、「曲率 defect」を Einstein tensor へ直接潰してはいけない、という点である。

| layer | GR object | C3 role | reason |
|:---|:---|:---|:---|
| raw defect | Riemann tensor / holonomy | transport 後の局所 mismatch | vacuum でも曲率を検出できる |
| contracted defect | Ricci tensor / scalar curvature | raw defect の物理的に効く trace | raw curvature を圧縮する |
| conserved projection | Einstein tensor | content と coupling できる divergence-free な幾何側投影 | Bianchi closure と stress-energy conservation に接続する |
| content | stress-energy tensor | container/content coupling target | 質量・エネルギー・熱力学的内容を担う |

この分離により、Schwarzschild vacuum separator で C3 を救える。逆に言えば、現行 D2 の「Einstein tensor = 2-simplex area」は、area を raw defect ではなく conserved coupling projection と読む場合に限って残せる。

## 2. Probe Matrix

| probe | GR case | expected GR structure | Face 側 reading | verdict |
|:---|:---|:---|:---|:---|
| P0 | Minkowski | Riemann = 0, Ricci = 0, `G_{μν}=0`, `T_{μν}=0` | defect なし、coupling なし。baseline comparison surface に residue がない | pass |
| P1 | Schwarzschild exterior | `T_{μν}=0`, Ricci = 0, `G_{μν}=0`, Riemann nonzero | content なしでも raw defect は残る。container geometry は vacuum structure として曲率を持てる | revise D2 |
| P2 | FLRW | matter content により `T_{μν}` と `G_{μν}` が Einstein coupling 下で非零 | geometry 側 conserved projection と content 側分布を container/content consistency として読める | provisional pass |
| P3 | contracted Bianchi identity | `∇^μG_{μν}=0` | Face 側 closure / syndrome conservation の候補 | open but targetable |

## 3. D1-D3 への即時影響

| claim | Round 1 result | edit implication |
|:---|:---|:---|
| D1: 3 roles map to direction/comparison/transport | role level では生きる | O1 precision note を保持 |
| D2: Einstein tensor is 2-simplex area | raw defect として読むと失敗 | raw defect -> contraction -> conserved projection に書き換える |
| D3: Einstein-Hilbert action is integral minimal condition | 直接未検査 | D2/O3 が明確になるまで保留 |

## 4. O1-O4 状態

| obligation | status after Round 1 | next test |
|:---|:---|:---|
| O1 type assignment | 局所安定 | 直ちに触らない |
| O2 defect | 修正済み、未閉鎖 | Riemann/holonomy を raw 2-simplex defect として形式化 |
| O3 closure | open かつ中心化 | Bianchi identity を Face-side conservation へ翻訳 |
| O4 coupling | 到達可能性あり | O3 後に FLRW または Jacobson で検査 |

## 5. Rejection Ledger

| 棄却 branch | 理由 |
|:---|:---|
| `defect = Einstein tensor` as raw reading | `G_{μν}=0` でも Riemann nonzero な vacuum curvature を処理できない |
| rhetoric による C3 強化 | probe outcome を変えない |
| C1 四力統一で C3 を救う | local closure 条件に反する |
| C4 前幾何で C3 を救う | local closure 条件に反する |

## 6. Revised Dictionary Candidate

**D2' candidate**:

Face Lemma の 2-simplex defect は、まず local holonomy / Riemann curvature に対応する。Ricci curvature と scalar curvature はその raw defect の縮約である。Einstein tensor は raw defect そのものではなく、container-side defect が content side と coupling できる divergence-free projection である。この読みでは、contracted Bianchi identity が conserved stress-energy との coupling を可能にする closure condition になる。

**状態**: 次の working hypothesis としては viable。ただし theorem candidate ではない。
