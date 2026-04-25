# 調査: automath の `q=6,7` probe と `e₂(A_q)=L_q` 仮説の評価

作成日: 2026-04-14

## 文書ネットワーク

役割: `q=6..10` の数値 probe を置く **data / computation 面**。

- hub: [構想_automath_第一障害可視化閾値.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/構想_automath_第一障害可視化閾値.md)
- `q=5` source 解釈: [調査_automath_q5符号反転とPaperIII_Z2接続.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_q5符号反転とPaperIII_Z2接続.md)
- 判断固定: hub 本文 §2-§7
- 理論反映: [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md)
- 実行 script: [計算_automath_q67_probe.py](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_automath_q67_probe.py)

## 文書状態

- 分類: **正本**
- 責務: `q=6..10` 数値計算、recurrence 回収、proxy 判定の記録
- 注記: ファイル basename は legacy だが、内容範囲は `q=6..10`
- 更新原則: 数値や script 由来の新事実はまずここへ入れる。判断やレトリックは hub 本文と [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md) に反映する
- 統合先: [構想_automath_第一障害可視化閾値.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/構想_automath_第一障害可視化閾値.md), [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md)

## 0. 結論

この probe の結論は二段である。

1. `e₂(A₅)=L₅` を **系列法則** として `q=6,7` へ伸ばす賭けは、現時点では支持されない。  
2. しかもこの結論は、`q=5` の source 符号規約を延長しても、`Fold.lean` から exact に再構成した companion recurrence を採っても、どちらでも同じである。
3. `q=10` 近辺で `Sym²` と `Λ²` の支配権が再度交代するという予測も、少なくとも **exact moment companion の proxy** では支持されない。`q=8,9,10` で `Λ²` 優勢は持続し、差はむしろ広がる。

つまり、`11` は「Lucas がこれ以後ずっと exterior trace を与える」という意味ではなく、`q=5` 境界で起きた特異な一致と読むほうが強い。

---

## 1. SOURCE と実験面の切り分け

### 1.1 SOURCE

今回の exact probe は、automath 原典の次の定義だけを使った。

- `Fold(w) = X.ofNat m (weight w)`  
  `https://raw.githubusercontent.com/the-omega-institute/automath/dev/lean4/Omega/Folding/Fold.lean`
- `weight` は語の Fibonacci 重み  
  `https://raw.githubusercontent.com/the-omega-institute/automath/dev/lean4/Omega/Folding/Weight.lean`
- `X.ofNat` は整数の Zeckendorf 表現を `m` 桁に切った stable word  
  `https://raw.githubusercontent.com/the-omega-institute/automath/dev/lean4/Omega/Folding/Value.lean`

これをそのまま Python に写した probe script が

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_automath_q67_probe.py`

である。

### 1.2 SOURCE で既に確定している q=5 面

`CollisionKernel.lean` / `CollisionZeta.lean` で確定している `q=5` の公式 kernel は

- last row `[10, -20, -8, -11, -2]`
- `tr(A₅) = -2`
- `tr(A₅²) = -18`
- `e₂(A₅) = 11`
- `|det(I-A₅)| = 32 = F₈ + 11`

である。

### 1.3 今回の実験面

ここから先は **SOURCE ではなく experiment** である。

- `Fold` の exact 定義から `momentSum q m` を局所再構成
- `q=2..7` の prefix を計算
- その prefix から最小 companion recurrence を回収
- `A_q` 候補の `trace`, `trace(A_q²)`, `e₂`, `|det(I-A_q)|` を評価
- `q=8,9,10` 追補では、brute-force の最小次数探索が重くなるため、**有理数上の Berlekamp-Massey** で recurrence を回収し、prefix 長を変えて安定性を確認した

---

## 2. MVP の検証

probe script は、まず source-backed prefix を再現するかを検査した。

### 2.1 prefix 再現

再現できた既知 prefix:

| q | prefix |
|:---|:---|
| 2 | `1, 2, 6, 14, 36, 88, 220` |
| 3 | `1, 2, 10, 26, 88, 260, 820` |
| 4 | `1, 2, 18, 50, 228, 808` |
| 5 | `1, 2, 34, 98, 616, 2612, 13444, 62168, 304456` |
| 6 | `1, 2, 66, 194, 1716, 8728, 57820` |
| 7 | `1, 2, 130, 386` |

この段階で、local 実装は `Fold` / `weight` / `X.ofNat` の SOURCE を正しく再現しているとみなせる。

### 2.2 `q=5` の裂け目 — Lucas-aligned dual と exact moment companion の 2 面性

`q=5` では companion matrix の 2 層が併存する。

| layer | last row | char poly の e₂ | 意味 |
|:---|:---|:---|:---|
| **Lucas-aligned dual (official)** | `[10, -20, -8, -11, -2]` | **+11 = L_5** | Lean `collisionKernel5`、Lucas-invariant 前面の representative |
| **exact moment companion** | `[-10, 20, 8, 11, 2]` | −11 | `Fold` / Berlekamp-Massey で回収、`S_5` の直接 recurrence を与える |

両者は **element-wise 全符号反転** の関係にある。代数的指紋:

`p_lean(x) + p_python(x) = 2x^5`

この anti-reflection identity は、[TAINT: inference] 両 companion が **同一の obstruction class `K_q = [κ_q]` の 2 代表元**として振る舞う可能性を示唆する [SOURCE: 調査_エスエフ_符号_反転_由来.md §2.2, 計算_エスエフ_符号_反転_由来.py phase1]。

source row を exact `S_5` sequence に代入すると m=0..4 の全点で `-S_5(m+5)` になる (ratio = −1.00 一定)。しかしこれは単純な全体符号反転や parity twist では吸収できない [SOURCE: Codex Phase 0, T1-T4 transform test 全 reject]。

**SF 調査 (2026-04-24) で確定した事実** [SOURCE]: `momentSum_five_recurrence_verified` 相当の定理は現在の Lean ソースに不在 (q=2,3,4 は `CollisionKernel.lean` L29/57/125 に verification 定理あり)。`collisionKernel5` の初出は commit `ce497566` (2026-03-28, loning, subject: "feat: Add new theorems and properties related to Fibonacci and Lucas numbers"、body item #1: "Introduced Lucas-Fibonacci squared identities for even and odd n")。同 commit および後続 A5 関連 commit (R140 trace powers / R142 trace recurrence / R254 Newton e₂ family / R258 A5 Newton) の message はいずれも Lucas-invariant formalization を指している。

[TAINT: inference, confidence 75%] 上記事実を踏まえた解釈: 2 面性は「convention 差」や「実装ミス」というより、**Lucas-aligned dual companion choice の構造的帰結**として読む方が既存 Yugaku 資産 (q5 符号反転 donor §3.4 graded second lift / 統一表 v0.2 §5 Λ²=F5 実現) との整合性が高い。ただし author 意図の直接確認は未実施であり、単純な sign typo の可能性を 100% 排除はしていない。

詳細: [文書_0016.md](./文書_0016.md) §3.1 / [調査_エスエフ_符号_反転_由来.md](./調査_エスエフ_符号_反転_由来.md)

---

## 3. `q=6..10` の exact recurrence

exact moment companion として回収された last row は次である。

| q | exact companion last row |
|:---|:---|
| 5 | `[-10, 20, 8, 11, 2]` |
| 6 | `[-4, 4, -26, 88, 28, 17, 2]` |
| 7 | `[-42, 84, -34, 311, 74, 26, 2]` |
| 8 | `[-4, 4, -174, 428, 2, 969, 174, 40, 2]` |
| 9 | `[-450, 900, 62, 2819, 386, 62, 2]` |
| 10 | `[-4, 4, -830, 1852, 2, 7945, 830, 96, 2]` |

この recurrence は、計算した長い tail 区間でも崩れなかった。

追補で確認した安定性:

- `q=8`: row は Berlekamp-Massey と既存 `minimal_recurrence` の両方で一致
- `q=9`: prefix 長 `18,20,22,24,26,28` で同一 row が出る。さらに `m=0..27` から回収した row が `m=28` を正しく予測した
- `q=10`: prefix 長 `22,24,26,28` で同一 row が出る。さらに `m=0..27` から回収した row が `m=28` を正しく予測した

---

## 4. invariant probe

### 4.1 exact companion をそのまま採る場合

| q | trace | `tr(A²)` | `e₂` | `|det(I-A)|` | BF excess | `L_q` |
|:---|---:|---:|---:|---:|---:|---:|
| 5 | 2 | 26 | -11 | 30 | 9 | 11 |
| 6 | 2 | 38 | -17 | 108 | 53 | 18 |
| 7 | 2 | 56 | -26 | 420 | 276 | 29 |

この面では、`q=5` からして already source kernel と一致しない。  
しかし `q=6,7` については明白で、

- `e₂(A_q) ≠ L_q`
- BF excess も `L_q` ではない
- `trace = 2` と `e₂ < 0` が続く

ので、H2 は成立しない。

### 4.2 `q=5` source の符号規約を延長する場合

`q=5` で exact row の全符号反転が official kernel になっているので、同じ sign-flip を `q=6,7` にも仮延長した面も調べた。

| q | trace | `tr(A²)` | `e₂` | `|det(I-A)|` | BF excess | `L_q` |
|:---|---:|---:|---:|---:|---:|---:|
| 5 | -2 | -18 | 11 | 32 | 11 | 11 |
| 6 | -2 | -30 | 17 | 110 | 55 | 18 |
| 7 | -2 | -48 | 26 | 422 | 278 | 29 |

この面では `q=5` の source 公式値が再現される。  
しかし `q=6,7` では

- `e₂ = 17, 26`
- `L_6 = 18`, `L_7 = 29`
- BF excess = `55, 278`

となり、やはり `e₂(A_q)=L_q` は壊れる。

### 4.3 `q=8,9,10` 追補 — `(Sym², Λ²)` トレース

一般公式

- `tr(Sym² A) = ((tr A)^2 + tr(A²))/2`
- `tr(Λ² A) = ((tr A)^2 - tr(A²))/2 = e₂(A)`

を用い、`q=5` の source 公式値 `(-7, 11)` に合わせるため sign-flip 規約を延長すると、次を得る。

| q | trace | `tr(A²)` | `tr(Sym² A_q)` | `tr(Λ² A_q)` | `Λ² - Sym²` |
|:---|---:|---:|---:|---:|---:|
| 5 | -2 | -18 | -7 | 11 | 18 |
| 6 | -2 | -30 | -13 | 17 | 30 |
| 7 | -2 | -48 | -22 | 26 | 48 |
| 8 | -2 | -76 | -36 | 40 | 76 |
| 9 | -2 | -120 | -58 | 62 | 120 |
| 10 | -2 | -188 | -92 | 96 | 188 |

少なくともこの proxy では、

- `q=8,9,10` でも `Λ²` が `Sym²` を上回り続ける
- 差分 `Λ² - Sym²` は `76, 120, 188` と拡大する
- `q=10` 近辺での座標交換再発は見えない

ただしこれは **official `collisionKernel8..10` ではなく exact moment companion の延長**である。したがって「source basis でも再発しない」とはまだ言わない。

---

## 5. 判定

### 5.1 H2 について

`e₂(A₅)=L₅` を「Lucas-外積系列法則」として読む H2 は、`q=6,7` probe では **棄却寄り** である。  
しかもこれは、

- exact moment companion 面
- source の q5 符号規約を延長した面

の両方で同じである。

### 5.2 何が残るか

残るのは「`11` の数列法則」ではなく、「`q=5` が境界点だった」という読みである。

この probe が支持するのは次の形だ。

1. `q=5` は確かに special である  
2. ただし special なのは Lucas 数が今後も続くからではない  
3. special なのは、`q=5` で sign convention / sector dominance / BF excess の位相が切り替わったからである

したがって、今後の主線は

- `e₂=L_q` の延長を追うことではなく
- `q=5` を anti-copy 優勢化の境界指紋として扱い
- `q≥6` で何が持続し、何が一回限りだったかを切ること

になる。

### 5.3 `q=10` 再交代仮説について

`φ = 2cos(π/5)` から「5 ステップ後に再び座標交換が起きるのではないか」という予測は、代数的には自然である。  
しかし今回の `q=8,9,10` proxy は、その**弱い版**

> `q=10` 近辺で `Sym²` と `Λ²` の支配権が再度交代する

を支持しない。

この段階で言えるのは次の二点である。

1. **proxy negative**: exact moment companion を source 符号規約へ延長した面では、`q=10` でも `Λ²` 優勢は崩れない  
2. **basis open**: ただし判定対象は official `collisionKernel8..10` ではない。したがって、位相回転仮説それ自体はまだ **source 未決** のまま残る

---

## 6. 次の一手

この probe の次にやるべきことは三つに絞られる。

1. `q=5` official kernel が exact moment companion と全符号反転する理由を source 側で掘る  
2. official `collisionKernel8,9,10` を同じ observable basis で出し、`tr(A_q)`, `tr(A_q²)`, `tr(Sym² A_q)`, `tr(Λ² A_q)` を直接比較する  
3. `q≥5` の支配固有値の偏角 `arg λ_dom(q)` を直接計算し、`π/5` 回転仮説が proxy ではなく固有値相で立つかを切る

1 が解けると、`q=6..10` の kernel 読み全体がかなり鋭くなる。
