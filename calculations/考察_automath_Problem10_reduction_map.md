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

## 2026-04-25 追記: BF 層だけで transport できる条件

Issue #38 補足で、q=6,7 の signed companion `A(c_q)` と nonnegative SFT presentation `B_q` は

`det(I-A)`, `e_2(A)`, `BF(A)`

を共有することが分かった。一方で trace と full characteristic polynomial は保存されない。したがって Problem 10 の次の判定は、`K_q=[\kappa_q]` がこの shared BF layer を通じて factor するかどうかである。

記法として

`BFData_q(A) := (det(I-A), e_2(A), BF(A))`

を置く。このとき BF 層だけで transport できる、とは次を満たす写像または構成

`τ_q^{BF}: BFData_q -> H^2(G_m; Z/2Z)`

が存在し、

`K_q(A) = τ_q^{BF}(BFData_q(A))`

が signed companion、nonnegative SFT presentation、将来の official collision kernel の間で同じ class を返す、という意味に限定する。

この factorization に必要な条件は少なくとも次の 5 つ。

| 条件 | 内容 | 現状 |
|:---|:---|:---|
| BF generator discipline | BF group の抽象同型だけでなく、`τ_q^{BF}` が使う generator / orientation / sign convention が固定されること | 未構成 |
| event quantum compatibility | `\lambda_q^{evt}` の規格化が `BFData_q` から読める、または BF-preserving map で不変であること | 未構成 |
| representative independence | carry defect 2-cocycle representative が trace や高次係数に依存せず、`det/e_2/BF` だけで class を決めること | 未証 |
| calibration | q≤4 で `τ_q^{BF}=0`、q=5 で `τ_q^{BF}\neq 0` を再現すること | 未証 |
| presentation naturality | signed companion → shared BF layer ← nonnegative SFT の両矢印で同じ `K_q` が得られること | q=6,7 の shared data のみ確認済 |

反証基準も明確になる。同じ `BFData_q` を持つ二つの presentation で、trace / full characteristic polynomial の差だけにより `K_q` が変わる例が出れば、BF 層だけでの transport は不可能である。逆に、`K_q` の representative が上の 5 条件を満たす `τ_q^{BF}` として書ければ、Issue #38 の nonnegative lift は Problem 10 の本体へ昇格できる。

現時点の判定: Issue #38 補足は `BFData_q` の共有を示すため **必要な橋** を与えるが、`τ_q^{BF}` の存在までは示さない。したがって Problem 10 は閉じず、残るタスクは `K_q` の BF-factorization の構成または反証である。

## fallback

integral lift がすぐ立たない場合の暫定 surrogate は sign-holonomy である。  
ただしこれは本丸ではなく、`k_q` の first visibility を先に見るための弱い代用品にとどめる。

## 使い分け

- 概念判断: hub 本文 §2-§7
- `K_q` の型: [考察_automath_Kq定義_noe.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Kq定義_noe.md)
- reduction map の型: この annex

## 4. Lean 形式化された関連 theorem (2026-04-24 Codex Phase 1 副次発見)

Codex Phase 1 secondary 探索で発見した `lean4/Omega/Folding/CollisionZetaOperator.lean` (paper-dev branch size 28683 bytes、全 9 target branch に存在) に、Problem 10 open checks を Lean 4 で裏付ける関連 theorem が複数存在する。以下は cubical integration / event quantum / integer lift の **Lean-verified footholds** として参照可能。

[SOURCE: 調査_自動数学_キュー一零_スペクトル_周期性.md §1.1 副次発見]

### 4.1 kernel dimension 公式

`collision_kernel_dimensions` [SOURCE: lean4/Omega/Folding/CollisionZetaOperator.lean L183-189 ref=paper-dev]:

```
dim(A_q) = 2⌊q/2⌋ + 1
```

q ごとの公式次元: q=2: 3, q=3: 3, q=4: 5, q=5: 5, q=6: 7, q=7: 7, q=8: 9, q=9: 9, q=10: 11

これは official Lean kernel が将来実装される際の **dimension 規格**を Lean で確定させる。重要な帰結:

- Tolmetes probe の exact moment companion は q=10 で 9×9 matrix だが、公式次元予告は **11×11** — **q=10 以降で probe と公式が不整合**
- 従って open check 3 (`k_q` が q=5 で初めて非零) を proxy で検証しても、basis-fixed 面では再検証が必要
- q=5: 5×5 は Lean official `collisionKernel5` (L163 CollisionKernel.lean) と **一致** [SOURCE: /tmp/CollisionKernel.lean L163-164 ref=dev]

### 4.2 event quantum bound

`momentSum_two_ratio_bounds` [SOURCE: lean4/Omega/Folding/CollisionZetaOperator.lean L9-13 ref=paper-dev]:

```
∀ m ∈ [2, 6], 2·S_2(m) ≤ S_2(m+1) ≤ 3·S_2(m)
```

q=2 moment sum 比が integer bounds [2, 3] に閉じ込められることの Lean 証明。

open check 1 (`λ_q^{evt}` をどう定義すれば cubical periods が整数化されるか) に対する **弱い foothold**: q=2 moment sum の連続比が integer bounds [2, 3] に収まることを示す。ただし Lean 側には「event quantum」概念はなく、この bound が直接 `λ_2^{evt}` を与えるとは言えない。event quantum 定義は Tolmetes 側の解釈で、ここにあるのは integer closure の **参考値** にとどまる。

### 4.3 sector 整数形式

`sector_m2_q{9,10,12,16}` と `sector_m3_q{9,10}` [SOURCE: lean4/Omega/Folding/CollisionZetaOperator.lean L18-23 ref=paper-dev]:

```
sector_m2_q : 2^q + 2        (q=9: 514, q=10: 1026, q=12: 4098, q=16: 65538)
sector_m3_q : 3·2^q + 2      (q=9: 1538, q=10: 3074)
```

m=2, m=3 sector cardinality の clean integer form を Lean 形式化。

open check 1 の **cubical periods 整数化** の参照値として使える。整数値は Fibonacci ではなく `a·2^q + 2` (a ∈ {1, 3}) 系 → cubical periods の entropy scaling (`log 2` 容量) と対応する可能性。Λ^2 sector の dimension count とは別軸。

### 4.4 Perron root integer localization

`perron_roots_all_localized` [SOURCE: lean4/Omega/Folding/CollisionZetaOperator.lean L191-199 ref=paper-dev]:

A_2, A_3, A_4 の Perron 実根が integer 区間 (2,3), (3,4), (3,4) に閉じていることを integer sign change で Lean 証明。

open check 3 (`k_q` が q=5 で初めて非零になる) に対する **間接 foothold**: q ≤ 4 での Perron 実根の integer localization が Lean で保証される。Phase 2 spectral 計算では signed convention で q=2,3,4 が real Perron mode、q=5 で complex pair 移行が観測される [SOURCE: 調査_自動数学_キュー一零_スペクトル_周期性.md §2] が、ここにあるのは q ≤ 4 の数値的 witness であって、「first visibility」の圏論的意味 (`[κ_q] = 0 vs ≠ 0`) を Lean が直接示しているわけではない。「complex pair 未発動」「boundary 前 closure」等の解釈は Tolmetes 側の読みで、Lean は integer closure の事実のみ提供する。

### 4.5 この annex での位置づけ

4.1-4.4 は Problem 10 open checks の Lean 形式化 landmark。どれも直接 `[κ_q] := ρ_2(Int_q([F_q]))` を構成するわけではないが、以下の **Lean-verified footholds** を提供する:

| open check | 関連 Lean theorem | 提供する foothold |
|:---|:---|:---|
| 1. quantization | `momentSum_two_ratio_bounds` (4.2) | q=2 moment sum 比の integer bound (参考値) |
| 1. quantization | `sector_m*_q*` (4.3) | `a·2^q + 2` 系の clean integer form (参考値) |
| 2. representative matching | `collision_kernel_dimensions` (4.1) | 公式 kernel の dimension formula (間接 foothold) |
| 3. first visibility | `perron_roots_all_localized` (4.4) | q ≤ 4 Perron 実根 integer localization (数値 witness) |

Phase 2 で signed proxy が棄却した 5-step 周期性仮説 [SOURCE: 調査_自動数学_キュー一零_スペクトル_周期性.md §3] とは **直交する軸**。Problem 10 の reduction map は spectral 周期性に依存せず、integer lift の幾何的構造に依存する。

### 4.6 q=5..10 の将来形式化予告

以下は Lean でまだ定義されていないが、`collision_kernel_dimensions` と同じパターンで展開すれば得られる候補:

- `collisionKernel5..10` の official def (dimension は 4.1 で予告済み)
- `sector_m2_q5..8`, `sector_m2_q11..15` (4.3 の extrapolation)
- `perron_roots_q5..10_localization` (4.4 の extension、complex pair については sign change が使えず別手法必要)

これらは Phase 1 未発見であり、**Phase 3 候補**。
