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

## 記法

- `K_q := [\kappa_q]`
- `k_q := 1_{K_q \neq 0}`

`K_q` は class-valued、`k_q` は visibility proxy である。  
閾値判定では後者を使い、本体の ontology では前者を使う。

## 使い分け

- 概念判断: hub 本文 §2-§7
- `K_q` の語義: この annex
- reduction map: [考察_automath_Problem10_reduction_map.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Problem10_reduction_map.md)
