# Problem 10 — `[\kappa_q]` 同定の reduction map annex

作成日: 2026-04-14  
縮約日: 2026-04-14  
位置づけ: Problem 10 の map 候補だけを残す **technical annex**。

## 文書ネットワーク

- hub: [構想_automath_第一障害可視化閾値.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/構想_automath_第一障害可視化閾値.md)
- `K_q` ontology annex: [考察_automath_Kq定義_noe.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Kq定義_noe.md)
- 論文統合面: [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md)

## 文書状態

- 分類: **補助 / annex**
- 責務: Problem 10 の reduction map 候補だけを保持する
- 更新原則: map の型や量子化条件が変わるときだけ更新する
- 既定の読点: 普段は hub を読む。ここは map の型を精密化したいときだけ開く

## kernel

> Problem 10 の本体は、連続側の曲率 2-形式をいきなり `\mathbb{Z}/2\mathbb{Z}` に落とすことではない。  
> まずそれを **整数係数の cubical flux class** に持ち上げ、その後で coefficient reduction を取ることにある。

狙うべき写像は次である。

`H^2_{dR}(M_q) --Int_q--> H^2(G_m; \mathbb{Z}) --ρ_2--> H^2(G_m; \mathbb{Z}/2\mathbb{Z})`

ここで

`K_q := [\kappa_q] := ρ_2(Int_q([F_q]))`

と読む。

## 量子化のメモ

- `\lambda_q^{evt}`: single carry event に対応する **event quantum**
- `\lambda_q^{amp} := F_m \lambda_q^{evt}`: 振幅まで保持したいときの refinement

Problem 10 で本体になるのは `\lambda_q^{evt}` である。  
`amp` 側は refined obstruction を見たいときだけ使う。

## 3 段の構成

1. cubical integration  
   `I_q(F_q)(\square) := \int_\square F_q`

2. integral lift  
   `I_q(F_q)(\square)/\lambda_q \in \mathbb{Z}` が成り立つなら  
   `Int_q([F_q])(\square) := (1/\lambda_q)\int_\square F_q`

3. coefficient reduction  
   `K_q := [\kappa_q] := ρ_2(Int_q([F_q]))`, `k_q := 1_{K_q \neq 0}`

## open checks

1. quantization  
   `\lambda_q^{evt}` をどう定義すれば cubical periods が整数化されるか。

2. representative matching  
   `Int_q(F_q)` が automath の carry defect representative と同じ class を与えるか。

3. first visibility  
   `k_q` がなぜ `q=5` で初めて非零になるか。

## fallback

integral lift がすぐ立たない場合の暫定 surrogate は sign-holonomy である。  
ただしこれは本丸ではなく、`k_q` の first visibility を先に見るための弱い代用品にとどめる。

## 使い分け

- 概念判断: hub 本文 §2-§7
- `K_q` の型: [考察_automath_Kq定義_noe.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Kq定義_noe.md)
- reduction map の型: この annex
