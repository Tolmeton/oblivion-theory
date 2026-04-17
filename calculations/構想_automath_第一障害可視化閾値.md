# 構想: automath における第一障害可視化閾値

作成日: 2026-04-14  
位置づけ: `H1/H2/H3` を別々の仮説としてではなく、ひとつの核概念の 3 つの投影として束ねるための内部理論メモ。

## 文書ネットワーク

この文書は、この話題の **hub / 索引面** として使う。

| 役割 | 文書 |
|:---|:---|
| 数値 probe 正本 | [調査_automath_q6q7_probe.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_q6q7_probe.md) |
| `q=5` source / `Z₂` 接続 | [調査_automath_q5符号反転とPaperIII_Z2接続.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_q5符号反転とPaperIII_Z2接続.md) |
| 判断固定 | この hub 本文 §2-§7 に統合済み。旧 [調査_automath_H1H2H3固化メモ.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_H1H2H3固化メモ.md) は redirect stub |
| `K_q` ontology annex | [考察_automath_Kq定義_noe.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Kq定義_noe.md) |
| Problem 10 reduction annex | [考察_automath_Problem10_reduction_map.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Problem10_reduction_map.md) |
| 論文統合面 | [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md) |

読み順の推奨:

1. この hub で概念配置を見る
2. [調査_automath_q5符号反転とPaperIII_Z2接続.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_q5符号反転とPaperIII_Z2接続.md) で `q=5` source を押さえる
3. [調査_automath_q6q7_probe.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_q6q7_probe.md) で `q=6..10` 数値面を見る
4. この hub 本文 §2-§7 で判断固定を読む
5. [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md) に理論へ反映する
6. `K_q` の型や Problem 10 の map を厳密化したいときだけ annex を開く

縮約注記:

- 2026-04-14 時点で、旧 judgment 面 [調査_automath_H1H2H3固化メモ.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_H1H2H3固化メモ.md) の内容はこの hub 本文へ統合した
- 以後、判断更新はまずこの文書と各正本面に入れ、旧メモは backward-compatible な redirect としてのみ維持する

---

## 0. kernel

このメモの主張は一文で足りる。

> `q=5` とは、排他的 2 体 sector、算術的 excess、そして first obstruction の可視化 proxy が初めて同時に立ち上がる **第一障害可視化閾値** である。

ここで言う「障害」は、strict に閉じていた構造が degree-2 の correction を要求し始める、その最初の可視化である。

---

## 1. 定義

### 1.1 観測量

`q` ごとに次の量を置く。

| 記号 | 定義 | 直観 |
|:---|:---|:---|
| `C_q` | `tr(Sym² A_q)` | cooperative / copy 的な 2 体 sector の可視量 |
| `X_q` | `tr(Λ² A_q) = e₂(A_q)` | exclusion / anti-copy 的な 2 体 sector の可視量 |
| `E_q` | `|det(I-A_q)| - F_{2q-2}` | Fibonacci 背景からの算術的 excess |
| `K_q` | `[\kappa_q]`。flat sector の strict chain map を global defect-bearing bridge へ延長する際の first obstruction class | 圏論的 obstruction の本体 |
| `k_q` | `1_{K_q \neq 0} = 1_{[\kappa_q] \neq 0}` | obstruction の可視化 proxy |

ここで `C_q, X_q, E_q` は既知量だが、`K_q` は class-valued な量である。  
`K_q` の ontology は **obstruction class** に置き、その具体実現を二段に分ける:

- local diagram 上では defect **2-cell**
- cochain 計算上では defect **2-cocycle**

この階層化により、`K_q` は `q` 間比較に必要な不変性を保ちつつ、automath の Lean 4 事実 (`globalDefect_compose`) とも接続される。

### 1.2 相の言葉

`q` の相を、2 体 sector の相対優勢で読む。

| 相 | 条件 | 読み |
|:---|:---|:---|
| cooperative 相 | `C_q > X_q` | 協調 / `Sym²` / `F4` 側が前景 |
| exclusion 相 | `X_q > C_q` | 排他 / `Λ²` / `F5` 側が前景 |

この定義は **official kernel convention** 上で読む。  
`q=5` には exact moment companion との全符号反転 anomaly があるため、この相判定は source convention 依存であることを常に明記する。

`k_q` は `K_q` の本体ではない。threshold を数値条件で書くための観測用 proxy である。

### 1.3 第一障害可視化閾値

official convention の下で

`q* := min { q | X_q > 0 かつ E_q > 0 かつ k_q = 1 }`

を **第一障害可視化閾値** と呼ぶ。

現時点の source では

- `q=4`: `(C_4, X_4) = (11, -7)`, `E_4 = 0`
- `q=5`: `(C_5, X_5) = (-7, 11)`, `E_5 = 11`

であり、理論の読みとしては `k_4 = 0`, `k_5 = 1` が要請される。したがって、暫定的に `q* = 5` である。

---

## 2. 命題

### 命題 1

`q=5` は trace 反転の点ではなく、`(C_q, X_q)` の座標交換が初めて起きる点である。

**根拠**:

- `q=4 → 5` で `(11, -7) → (-7, 11)` と座標交換する
- `supertrace = tr(A_q²)` も `+18 → -18` に反転する

したがって、`q=5` の本体は 1 次量の反転ではなく、**2 体 lifted sector の優勢交代**にある。

### 命題 2

`e₂(A₅)=L₅` は family law ではない。

**根拠**:

- `q=6,7` probe では exact recurrence 面でも sign-flip extension 面でも `e₂(A_q)≠L_q`
- よって `e₂(A_q)=L_q` を `q>5` に延長する素朴な読みは反例で崩れる

### 命題 3

bridge の strict 部分は flat sector に限れば既に閉じている。

**根拠**:

- projection / restriction は `restrict_functorial` で strict に閉じる
- `deltaSet` は `product Bernoulli / cubical / multilinear / dT=0` の範囲で mixed partial の cell 積分に一致する

したがって、未解決核は strict part の不存在ではなく、**global extension の obstruction** にある。

---

## 3. 予想

### 予想 H*

`H1/H2/H3` は独立な 3 仮説ではなく、同一の obstruction の 3 つの投影である。

| 投影 | 見えるもの |
|:---|:---|
| スペクトル的投影 | `C_q ↔ X_q` の優勢交代 |
| 算術的投影 | `E_q` と `X_q` の共鳴 |
| 圏論的投影 | `K_q = [\kappa_q]` として現れる first obstruction class |

### 予想 H*1

`q=5` は exclusion sector の最初の可視化点であり、`e₂(A₅)=L₅` はそのとき `X_q` と `E_q` が偶然以上の強さで重なった **boundary resonance** である。

ここで構造的なのは `11` の持続ではなく、**最初の共鳴点が 5 に現れたこと**である。

### 予想 H*2

`K_q` は full chain map の不在を意味するのではない。  
flat sector で strict に閉じる chain map を global へ延長する際の **degree-2 obstruction** として現れる。

この予想の下では bridge は

`strict chain map on flat sector`  
`+ defect-bearing extension on global sector`

として読むべきである。

### 予想 H*3

`F4/F5` はこの obstruction の生成原理そのものか、少なくともその最良の現象論である。

ただし現段階では後者までしか言えない。  
つまり `F4/F5` は **説明図式** としては強いが、まだ formal derivation ではない。

---

## 4. 反証条件

この構想は、次のどれかが起きれば大きく後退する。

### 反証 1

`q=5` official kernel の全符号反転 anomaly が単なる転記ミス・局所バグ・規約の偶然であり、2 体 sector の解釈と独立だと source 上で確定する。

### 反証 2

`q=5` の `(C_q, X_q)` 交換が basis artifact で、observable-independent な相転移指標ではないと判明する。

### 反証 3

`q≥5` で `X_q`, `E_q`, `K_q` の間に何の持続的相関も見つからず、`q=5` だけが完全に孤立した coincidence に落ちる。

### 反証 4

flat sector ですら strict chain map が壊れ、`K_q` を global obstruction として切り出すこと自体ができない。

---

## 5. この構想が変えるもの

### 5.1 何を問うか

古い問い:

- `e₂(A_q)=L_q` は続くか
- global strict chain map はあるか

新しい問い:

- なぜ第一障害可視化閾値が `5` なのか
- `X_q`, `E_q`, `K_q` は同じ obstruction の別投影か
- full bridge の first obstruction は何か

### 5.2 何をやめるか

やめるべきなのは、`11` の等式そのものへ執着することだ。  
本当に追うべきなのは

- 最初の可視化点がどこか
- そこで何が同時に可視化されるか
- その可視化をどの universal property で束ねるか

である。

---

## 6. 次の理論タスク

### T1. `K_q = [\kappa_q]` の代表系を作る

`K_q` 自体は obstruction class として固定し、その representative と witness を切り分ける。

- representative: carry / global defect の 2-cocycle
- witness: pseudofunctorial failure を担う defect 2-cell
- proxy: `k_q := 1_{K_q \neq 0}` あるいは representative の最小ノルム

さらに Problem 10 の candidate reduction map として

`H^2_{dR}(M_q) --Int_q--> H^2(G_m; Z) --rho_2--> H^2(G_m; Z/2Z)`

を置き、

`K_q := [\kappa_q] := rho_2(Int_q([F_q]))`

と読む。ここで `Int_q` の規格化に使う `\lambda_q` は、carry amplitude ではなく **single carry event** に対応する event quantum とする。

### T2. `q*=5` の source 依存性を明示化する

`q*` は current official convention 上の閾値である。  
exact moment companion convention と official convention の差を、理論の外に置かず理論の一部として扱う必要がある。

### T3. `X_q` と `E_q` の関係を family law ではなく resonance law として定義する

狙うべきは

`X_q = E_q`

の普遍化ではない。  
`q=q*` でのみ共鳴する、という **閾値法則** の方である。

### T4. bridge を obstruction theory として再定式化する

問いを

`chain map はあるか`

から

`strict chain map の first obstruction は何か`

へ変える。

---

## 7. 現時点の最短定式化

> `q=5` は、排他的 2 体 sector (`X_q`)、算術的 excess (`E_q`)、そして obstruction 可視化 proxy (`k_q`) が初めて同時に立ち上がる第一障害可視化閾値である。  
> そのとき本体として非零になるのは global extension に必要な first obstruction class `K_q = [\kappa_q]` である。  
> `e₂(A₅)=L₅` はその閾値で起きた boundary resonance であり、family law ではない。  
> bridge の本丸は strict chain map の存在ではなく、その first obstruction をどう記述するかにある。
