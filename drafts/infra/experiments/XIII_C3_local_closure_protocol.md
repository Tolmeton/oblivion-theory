# E-XIII-C3-01: Face Lemma - GR 局所 closure protocol

**日付**: 2026-04-26
**状態**: Round 1 protocol 固定 / paper-probe matrix level で実行
**対象**: Paper XIII C3、特に §8.2 D1-D3 と §8.2.1 O1-O4
**目的**: Paper XIII 本文を編集する前に、C3 dictionary が最小 GR case に耐えるかを観測する。

## 0. SOURCE 境界

**この protocol で使う SOURCE**

| SOURCE | 役割 |
|:---|:---|
| `drafts/series/論文XIII_時空は忘却である_草稿.md` §8 | C3 を skeleton と明示し、D1-D3 / O1-O4 に分解している |
| `drafts/series/論文XIII_時空は忘却である.meta.md` §M3, §M5, §M8 | C3 を Kalon 近傍だが未閉鎖と記録し、O1 局所 closure を吸収済み |
| `drafts/リファレンス/FaceLemma.md` | Face Lemma を recoverability ではなく detectability / comparison surface の条件として固定している |
| `drafts/series/論文VIII_存在は忘却に先行する_草稿.md` §2.2 / §5.3 | GR 真空を容器先行の例として扱い、真空でも曲率が残りうることを明示している |

**TAINT / 次段で SOURCE 昇格が必要な面**

Minkowski、Schwarzschild exterior、FLRW、Riemann/Ricci/Einstein tensor、contracted Bianchi identity については、標準 GR の安定した背景知識として使う。公開水準へ上げる場合は、GR 原典・教科書・symbolic calculation ledger のいずれかで SOURCE 化する。

## 1. P-0 Prolegomena

この実験は C3 の証明ではない。現在の C3 dictionary が、最小 case に対して正しい壊れ方をするかを見る。

**検証仮説**

Face Lemma の 3 射最小性は、GR 側では次の役割分担として読めるかもしれない。

| Face 側の役割 | GR 側候補 | 読み |
|:---|:---|:---|
| 方向 | 接方向 / vector field | 比較をどちらへ動かすか |
| 比較 | 計量 | 長さ・角度・間隔をどう比べるか |
| 輸送 witness | Levi-Civita connection / Christoffel symbol | 比較規則を隣接点へ運ぶ |
| raw defect | Riemann curvature / holonomy | 小さな loop を回った後のズレ |
| contracted defect | Ricci curvature / scalar curvature | raw defect の物理的に効く縮約 |
| conserved coupling projection | Einstein tensor | 内容側と結合できる divergence-free な幾何側投影 |
| content side | stress-energy tensor | 質量・エネルギー・熱力学的内容の分布 |

**盲点チェック**

| カテゴリ | リスク | guard |
|:---|:---|:---|
| 実験設計 | 都合のよい matter-filled case だけを見る | flat / vacuum case を先に通す |
| 測定 | curvature tensor を全部同じものとして扱う | Riemann, Ricci, scalar, Einstein tensor を分ける |
| 確証バイアス | 失敗後の relabeling で C3 を守る | 反証条件を先に固定する |
| scope | C1/C4 まで同時に閉じようとする | この round では C1/C4 を rescue に使わない |
| 記号 | 架橋射 `T` と stress tensor `T_{μν}` が混線する | case matrix で bridge role と stress-energy role を分ける |

## 2. P-1 反証条件

以下のどれかを必要とするなら、現行 C3 dictionary はその形では失敗とする。

| id | 反証条件 | なぜ落ちるか |
|:---|:---|:---|
| R1 | raw defect を `G_{μν}` と直接同一視しないと維持できない | Schwarzschild exterior では Riemann nonzero かつ `G_{μν}=0` なので、raw defect は Einstein tensor だけでは担えない |
| R2 | Ricci / scalar / Einstein tensor / stress-energy の役割分担が曖昧に残る | dictionary ではなく resemblance に落ちる |
| R3 | Bianchi identity を Face 側 closure / conservation として翻訳できない | O3 が未閉鎖のまま残る |
| R4 | matter-filled case で `G_{μν}` と内容側の consistency が接続しない | C2 と C3 が橋を持たない |
| R5 | C3 を救うために C1 または C4 の仮定が必要になる | C3 単独の局所 closure ではない |

**Round 1 の pass threshold**

flat / vacuum / matter-filled probe を、C1/C4 なしに処理できる改訂 dictionary が得られれば弱い意味で pass。ただし定理昇格はしない。

## 3. P-2 Minimum Viable Probe

最小 probe は 4 つ。

| probe | case | 役割 |
|:---|:---|:---|
| P0 | Minkowski baseline | zero-defect sanity check |
| P1 | Schwarzschild exterior / vacuum curvature separator | raw curvature と content coupling を分離する |
| P2 | FLRW / matter-filled coupling case | `G_{μν}` が coupling projection として機能するか見る |
| P3 | contracted Bianchi identity | closure / conservation が Face 側で読めるか見る |

この round では新しい物理を主張しない。標準 GR 構造に対して、Paper XIII の C3 語彙が内部整合的に置けるかを見るだけである。

## 4. P-3 実行規則

各 case で以下を記録する。

| field | 意味 |
|:---|:---|
| `Riemann` | local holonomy / raw curvature defect |
| `Ricci` | contracted curvature |
| `G` | divergence-free coupling-side projection |
| `T` | content side |
| `Face role` | direction / comparison / transport / defect / closure / coupling |
| `verdict` | pass / revise / fail |

形容詞だけの verdict は禁止。各 case で、どの tensor がどの役割を担うかを書く。

## 5. P-4 Harvest rule

期待される高情報量の surprise は次。

1. P1 が `defect = Riemann/holonomy` を要求するなら、§8.2 D2 は本文強化前に書き換える。
2. P3 が `∇^μG_{μν}=0` に Face 側 closure の読みを与えられるなら、O3 が次の closure target になる。
3. P2 が `G_{μν}` と `T_{μν}` を「左辺=右辺」の反復ではなく container/content consistency として接続できるなら、C2 と C3 が結ばれる。

## 6. Skin-in-the-Game

この実験結果は編集方針を制御する。

| result | 許可される編集 |
|:---|:---|
| direct D2 は失敗するが revised split は生きる | §8.2 D2/O2 を role split へ書き換える。ただし closure 宣言はしない |
| P3 が失敗 | C3 は skeleton のまま保持し、結論を強めない |
| P2 が失敗 | C2 と C3 は分けたままにし、GR coupling closure を主張しない |
| 全 probe が role level で通る | E-XIII-C3-02 として Bianchi / closure formalization へ進む |

## 7. PeQS

| component | score | note |
|:---|:---:|:---|
| blind-spot coverage | 0.80 | flat / vacuum / matter / identity probe を含む |
| falsification strictness | 0.85 | `G=defect` の直読を明示的に落とせる |
| MVP minimality | 0.90 | Round 1 では full tensor calculation を要求しない |
| expected information gain | 0.90 | outcome が §8 D2 wording と次実験を変える |

**Round 1 quality**: 内部 draft guidance には十分。公開水準の proof には不足。
