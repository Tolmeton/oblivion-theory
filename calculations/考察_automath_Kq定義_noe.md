# 考察: `K_q` の ontology annex

作成日: 2026-04-14  
縮約日: 2026-04-14  
対象: `K_q` を `2-cell / cocycle / obstruction class` のどこに置くか。

## 文書ネットワーク

役割: `K_q` の型だけを固定する **technical annex**。

- hub: [構想_automath_第一障害可視化閾値.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/構想_automath_第一障害可視化閾値.md)
- Problem 10 reduction annex: [考察_automath_Problem10_reduction_map.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Problem10_reduction_map.md)
- 論文統合面: [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md)

## 文書状態

- 分類: **補助 / annex**
- 責務: `K_q` の ontology だけを固定する
- 更新原則: `K_q` の定義や level 関係が変わるときだけ更新する
- 既定の読点: 普段は hub を読む。ここは `K_q` の語義を精密化したいときだけ開く

## kernel

> `K_q` の本体は defect 2-cell でも defect 2-cocycle でもなく、その両者を representative として持つ **first obstruction class** である。

## level 分解

| level | 役割 | `K_q` との関係 |
|:---|:---|:---|
| defect 2-cell | 局所図式で「どこが strict に閉じないか」を示す witness | manifestation |
| defect 2-cocycle | 計算可能な representative | representative |
| obstruction class | coboundary / gauge 変更に耐える first obstruction | ontology |

## なぜ class を本体にするか

1. `2-cell` を本体にすると、chart や diagram ごとの差が強すぎて `q` 間比較が不安定になる。  
2. `2-cocycle` を本体にすると、coboundary の取り替えで representative が動き、official / exact の規約差にも弱い。  
3. obstruction class に置くと、local witness と global invariant を両方保持できる。

## 2026-04-25 追記: 同一 obstruction class と呼ぶ条件

Issue #38 Corollary 7 は、signed companion の Fibonacci fusion-ring shadow から monoidal / braided category へ昇格する際に未証の locus として associator, F-symbols, braiding maps, pentagon/hexagon coherence を指名する。これは Problem 10 の Open C と同じく degree-2 obstruction の候補面だが、ただちに `K_q=[\kappa_q]` と同一 class であるとは言えない。

強い同一性主張:

`K_q^{carry} = K_q^{fusion}`

を許すには、少なくとも次の比較データが必要である。

| 条件 | 内容 | 現状 |
|:---|:---|:---|
| common target | carry defect 側と fusion coherence 側が同じ cohomology group、または明示された共通 target に入ること | 未構成 |
| comparison map | fusion coherence obstruction から `H^2(G_m; Z/2Z)` への写像、または逆向き/zigzag の比較写像 `Ξ_q` があること | 未構成 |
| representative compatibility | carry 2-cocycle と associator / F-symbol / braiding / pentagon-hexagon の obstruction representative が `Ξ_q` の下で同じ class に落ちること | 未証 |
| gauge invariance | basis, convention, coboundary 変更で同一性が壊れないこと | 未証 |
| calibration | q≤4 では同じ理由で zero、q=5 では同じ理由で nonzero になること | 未証 |
| index discipline | q=5 first visibility と q=6 persistence refutation の 1 index 差が、parameter mismatch ではなく比較写像で説明されること | 未証 |

したがって現時点で許される表現は **candidate dual face** または **同じ degree-2 問題圏に属する候補対応** までである。「同一 cohomology class」とは書かない。

反証基準も明確である。比較写像 `Ξ_q` が構成できない、または構成しても carry 側の `K_q` と fusion 側の obstruction が異なる class に落ちるなら、両者は独立した degree-2 obstruction として扱う。この場合、q=5 と q=6 の 1 index 差は structural gap ではなく、persistence-test / parameter / proxy boundary の artifact と読む。

## 記法

- `K_q := [\kappa_q]`
- `k_q := 1_{K_q \neq 0}`

`K_q` は class-valued、`k_q` は visibility proxy である。  
閾値判定では後者を使い、本体の ontology では前者を使う。

## 使い分け

- 概念判断: hub 本文 §2-§7
- `K_q` の語義: この annex
- reduction map: [考察_automath_Problem10_reduction_map.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Problem10_reduction_map.md)
