# 調査: automath の `q=5` 符号反転と Paper III の `Z₂`-次数付き構造

作成日: 2026-04-14

## 文書ネットワーク

役割: `q=5` の source 事実と `Paper III` への接続を扱う **source / interpretation 面**。

- hub: [構想_automath_第一障害可視化閾値.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/構想_automath_第一障害可視化閾値.md)
- 数値追補: [調査_automath_q6q7_probe.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_q6q7_probe.md)
- 判断固定: hub 本文 §2-§7
- 理論反映: [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md)

## 文書状態

- 分類: **正本**
- 責務: `q=5` の source ledger と `Paper III` 接続の一次解釈
- 更新原則: `q=5` の official kernel、issue コメント、source anomaly に関わる更新はまずここへ入れる
- 統合先: [構想_automath_第一障害可視化閾値.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/構想_automath_第一障害可視化閾値.md), [統一表の関手化_構想ドラフト_v0.2.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md)

## 0. 目的

GitHub Issue #25 への返信で先方が新たに開いた球は、`q=5` で collision kernel の符号構造が反転することを、こちらの Paper III における `Z₂`-次数付き `copy / anti-copy` 分岐へ接続できるか、という点である。

このメモの役割は公開文書を書くことではない。内部でまず、

1. 何が **SOURCE** として確定したか
2. 何がこちらの **局所計算** で追加確認できたか
3. どこまでが **主張可能** で、どこからが **未証明の仮説** か

を切り分けることである。

## 1. SOURCE ledger

### 1.1 GitHub 返信コメント

SOURCE:
`https://github.com/the-omega-institute/automath/issues/25#issuecomment-4237867805`
API:
`https://api.github.com/repos/the-omega-institute/automath/issues/comments/4237867805`

先方コメントで確定した事実:

| 項目 | 内容 | 状態 |
|:---|:---|:---|
| carry defect | `κ(x,y)` は `H²(G_m; Z/2Z)` の非自明 2-cocycle を与える | SOURCE |
| BF determinant | `|det(I-A_q)| = 1, 3, 8` for `q = 2, 3, 4` は偶数番目 Fibonacci 部分列 `F₂, F₄, F₆` に一致 | SOURCE |
| `q=5` 破れ | `|det(I-A₅)| = 32`, `F₈ = 21`, excess `= 11 = L₅` | SOURCE |
| trace 符号反転 | `tr(A_q) = +2` for `q ≤ 4`, `tr(A₅) = -2` | SOURCE |
| 先方の読み | この符号反転は transfer operator の phase transition であり、Paper III の `Z₂`-graded 構造と接続する可能性がある | SOURCE |

### 1.2 automath 原典

SOURCE:
`https://raw.githubusercontent.com/the-omega-institute/automath/dev/lean4/Omega/Folding/CollisionKernel.lean`
SOURCE:
`https://raw.githubusercontent.com/the-omega-institute/automath/dev/lean4/Omega/Folding/CollisionZeta.lean`

原典で確認した事実:

| 対象 | 事実 | 原典位置 |
|:---|:---|:---|
| `collisionKernel5` | 行列末行は `[10, -20, -8, -11, -2]` | `CollisionKernel.lean` lines 161-170 |
| `collisionKernel5_trace` | `tr(A₅) = -2` | `CollisionKernel.lean` lines 166-170 |
| `collisionKernel5_det` | `det(A₅) = 10` | `CollisionKernel.lean` lines 169-170 |
| `bowenFranksMatrix5_det` | `det(I-A₅) = 32` | `CollisionKernel.lean` lines 262-276 |
| `collisionKernel5_cayley_hamilton` | `A₅^5 + 2A₅^4 + 11A₅^3 + 8A₅^2 + 20A₅ - 10I = 0` | `CollisionKernel.lean` lines 374-379 |
| `collisionKernel5_trace_pow_1..6` | `-2, -18, 34, 66, -272, -114` | `CollisionZeta.lean` lines 844-857 |
| `collisionKernel5_e2` | `tr(A₅)^2 - tr(A₅²) = 22`, therefore `e₂ = 11` | `CollisionZeta.lean` lines 927-931 |
| `collisionKernel_e2_family` | `e₂` family is `-2, -4, -7, +11` for `q = 2, 3, 4, 5` | `CollisionZeta.lean` lines 956-963 |

### 1.3 Paper III 原典

SOURCE:
`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文III_Markov圏の向こう側_草稿.md`

接続に必要な骨格:

| 項目 | 内容 | 原典位置 |
|:---|:---|:---|
| `Z₂`-次数 | 偶次数 = `α > 0` の copy 的セクター, 奇次数 = `α < 0` の anti-copy 的セクター | lines 152-170 |
| anti-copy の余域 | `anti-copy_X : V(X) → ∧²V(X)` | lines 167-170, 250-279 |
| anti-copy の核 | `e_x ∧ e_x = 0` による幂零性 | lines 179-185, 318-321 |
| 予測 P-III-2 | `α` の符号が反転する臨界層 `l*` がある | lines 1965-1971 |
| 予測 P-III-3 | 対称成分 = copy, 反対称成分 = anti-copy | lines 2063-2065 |

## 2. 差分がどこにあるか

### 2.1 `q = 2, 3, 4` は同じ相に見える

SOURCE だけで言えること:

| `q` | `tr(A_q)` | `det(A_q)` | `e₂(A_q)` | `|det(I-A_q)|` |
|:---|---:|---:|---:|---:|
| 2 | 2 | -2 | -2 | 1 |
| 3 | 2 | -2 | -4 | 3 |
| 4 | 2 | -2 | -7 | 8 |

この範囲では、

- trace は正
- determinant は負
- 2次対称量 `e₂` は負
- BF determinant は Fibonacci 部分列

で揃っている。したがって `q=2..4` は単に「数値が増えた」のではなく、**同じ符号相** を共有している。

### 2.2 `q = 5` で初めて相が割れる

`q=5` では次が同時に起きる:

| 指標 | `q≤4` | `q=5` |
|:---|:---|:---|
| `tr(A_q)` | `+2` | `-2` |
| `det(A_q)` | `-2` | `10` |
| `e₂(A_q)` | 負 (`-2, -4, -7`) | 正 (`+11`) |
| `|det(I-A_q)|` | `F₂, F₄, F₆` | `F₈ + L₅ = 21 + 11 = 32` |

ここで重要なのは、破れが 1 箇所だけではないことだ。

- 1次量 `tr` が反転する
- 2次量 `e₂` も反転する
- BF determinant に Lucas 成分 `11` が出現する

つまり `q=5` は「trace だけが偶然ひっくり返った」点ではない。**1次・2次・位相的不変量が同時に相を替える** 点である。

## 3. こちらの追加計算

以下は local numerical check であり、automath 原典そのものではない。

### 3.1 固有値配置の質的変化

`numpy.linalg.eigvals` による数値確認:

| kernel | 支配固有値の型 | 備考 |
|:---|:---|:---|
| `A₂` | 大きい正の実固有値 1 本 | 実軸支配 |
| `A₃` | 大きい正の実固有値 1 本 | 実軸支配 |
| `A₄` | 大きい正の実固有値 1 本 | 複素対はあるが主役は正実軸 |
| `A₅` | 支配モードが複素共役対 | 正の大 Perron 根が消える |

局所計算:

- `A₂` spectral radius `≈ 2.481`
- `A₃` spectral radius `≈ 3.086`
- `A₄` spectral radius `≈ 3.846`
- `A₅` spectral radius `≈ 2.620`, ただしこれは複素共役対の絶対値

したがって `q=5` では、増殖の主軸が「正実の 1 本柱」から「位相を持つ共役対」へ移る。

これは Paper III の言葉で言えば、copy 的な単調増殖ではなく、**交換で符号を食う odd sector が可視化された** と読む余地がある。

### 3.2 trace power の符号振動

SOURCE:
`CollisionZeta.lean` lines 845-857

`A₅` の trace power は

`5, -2, -18, 34, 66, -272, -114`

で、初期から符号振動を起こす。`A₂, A₃, A₄` の既知 trace power は初期区間で正に張り付いているため、ここでも `A₅` は別相である。

### 3.3 厳密橋脚: `e₂(A) = tr(Λ²A)`

ここは比喩ではなく一般線形代数である。

任意の線形作用素 `A : V → V` に対して、

- `tr(Sym² A) = ((tr A)^2 + tr(A²)) / 2`
- `tr(Λ² A) = ((tr A)^2 - tr(A²)) / 2 = e₂(A)`

が成り立つ。理由は、`A` の固有値を `λ_i` とすると

- `Sym² V` の固有値は `λ_i λ_j (i≤j)`
- `Λ² V` の固有値は `λ_i λ_j (i<j)`

だからである。

これは Paper III にとって決定的である。なぜなら anti-copy の像は `∧²V(X)` にあるからで、automath の `e₂(A_q)` は **反対称 2体 sector の trace** そのものになる。

SOURCE の `tr(A_q)` と `tr(A_q²)` から計算すると:

| `q` | `tr(A_q)` | `tr(A_q²)` | `tr(Sym² A_q)` | `tr(Λ² A_q)=e₂(A_q)` |
|:---|---:|---:|---:|---:|
| 2 | 2 | 8 | 6 | -2 |
| 3 | 2 | 12 | 8 | -4 |
| 4 | 2 | 18 | 11 | -7 |
| 5 | -2 | -18 | -7 | 11 |

ここで起きていることは単なる「trace の反転」ではない。

- `q≤4` では `Sym²` 側が正、`Λ²` 側が負
- `q=5` では `Sym²` 側が負、`Λ²` 側が正

さらに `q=4 → 5` で

- `(tr(Sym² A_4), tr(Λ² A_4)) = (11, -7)`
- `(tr(Sym² A_5), tr(Λ² A_5)) = (-7, 11)`

となり、**対称 sector と反対称 sector が座標交換する**。

これは Paper III の語彙に翻訳すると、

- `copy` 側の優勢が `anti-copy` 側の優勢へ反転した

という 2次 lifted level での位相分岐に見える。

### 3.4 graded second lift の supertrace

`W_q := Sym²(V_q) ⊕ ΠΛ²(V_q)` を `Z₂`-graded 空間とみなす。

このとき

- ordinary trace on `W_q` は `tr(A_q)^2 = 4`
- supertrace on `W_q` は `tr(A_q²)`

となる。

したがって:

| `q` | ordinary trace on `W_q` | supertrace on `W_q` |
|:---|---:|---:|
| 2 | 4 | 8 |
| 3 | 4 | 12 |
| 4 | 4 | 18 |
| 5 | 4 | -18 |

特に `q=4` と `q=5` の間で supertrace が `+18 → -18` と正確に反転する。

これは「2次 lifted された graded 系では、総量は保存されたまま parity balance だけが反転した」と読める。

### 3.5 `q=10` 再発予測への local proxy

ここから先は SOURCE ではなく experiment である。

exact `momentSum` から回収した companion recurrence に対し、`q=5` official kernel へ合わせる sign-flip 規約を `q=8,9,10` に延長すると、

| `q` | `tr(Sym²A_q)` | `tr(Λ²A_q)` |
|:---|---:|---:|
| 8 | -36 | 40 |
| 9 | -58 | 62 |
| 10 | -92 | 96 |

となる。したがって、この proxy では `q=10` 近辺での `(Sym², Λ²)` 座標交換の再発は出ない。むしろ `Λ²` 優勢は持続し、差は拡大する。

ただしこの結論は、

- official `collisionKernel8..10` ではない
- 支配固有値の偏角 `arg λ_dom(q)` を直接見たものでもない

という二つの留保を持つ。したがって「五角形共鳴の周期性が棄却された」とまでは言わない。言えるのは、**exact moment companion の proxy は周期的再交換を支持しない**、までである。

## 4. 最短の接続仮説

### 4.1 何をそのまま言ってよいか

主張可能:

1. Paper III の奇次数セクターは `anti-copy` であり、その本体は `∧²V(X)` にある。
2. 一般公式により `e₂(A_q) = tr(Λ²A_q)` である。
3. `A₅` では `tr(Λ²A₅) = 11` となり、反対称 2体 sector の trace が正へ反転する。
4. この `11` は BF determinant の excess `32 - 21` と一致する。

したがって、ここで採る **最有力の暫定読み** は、`q=5` の破れを 2体交換セクターの再編成として扱うことである。

図像で言えば:

- `q≤4` では「1体の copy 的輸送」が全体像を支配している
- `q=5` で「2体の anti-copy 的排他」が前景化し、1体 sector の符号を押し返す

ここで `e₂ = 11` が効いている。`e₂` は単に「二者関係の量」なのではなく、**正確に `Λ²` sector の trace** である。Paper III で anti-copy の像が `∧²V(X)` に落ちる以上、2体 sector を見る第一の窓はまさにこの量である。

### 4.2 このメモでまだ言ってはいけないこと

以下はまだ未証明:

1. `tr(A_q)` それ自体が Paper III の supertrace である
2. `q` の偶奇そのものが `Z₂`-次数に一致する
3. `q=5` がただちに `α < 0` そのものを意味する

この 3 つは短絡であり、現時点では言えない。

## 5. 暫定定式化

### 5.1 提案命題の形

仮説 H1:

> 2次 lifted 系 `W_q := Sym²(V_q) ⊕ ΠΛ²(V_q)` を考えると、`q≤4` では symmetric/copy sector が正で exterior/anti-copy sector が負、`q=5` ではその符号配置が反転する。  
> その最初の可観測シグネチャが
> `tr(Sym²A_q), tr(Λ²A_q)` の座標交換
> `(11,-7) → (-7,11)`
> である。

この形にしておくと、Paper III との接続点が明瞭になる:

- `tr(A)` は 1体の正味寄与
- `tr(Λ²A)=e₂(A)` は 2体の exchange / exclusion 寄与
- `∧²V(X)` は Paper III の anti-copy の正しい住処

### 5.2 Lucas `11` の意味

仮説 H2:

> `L₅ = 11` は `q=5` で初めて露出した odd pair sector の計数的痕跡である。

理由:

- 先方コメントでは `11` は BF determinant の excess として現れる
- automath 原典では `11` は独立に `e₂(A₅)=tr(Λ²A₅)` として現れる
- Paper III では 2体の anti-copy は `∧²` 側に押し出される

つまり `11` は「Fibonacci が壊れた残差」ではなく、**pairwise antisymmetric correction が独立変数として立ち上がった量** である可能性が高い。

## 6. Negativa

切っておくべき枝:

| 却下案 | 却下理由 |
|:---|:---|
| `q` が奇数だから odd sector | `q=3` では符号反転しない。偶奇だけでは説明不能 |
| `tr` の反転だけで十分 | `e₂` と BF determinant も同時に割れており、1次量だけ見るのは浅い |
| `α < 0` そのものが Lean 側で証明された | Lean 側で証明されているのは kernel invariants であり、Paper III への functorial bridge ではない |

## 7. 次の一手

### 7.1 最小コスト

1. `A_q` の graded lift を定義する  
   候補: `W_q := Sym²(V_q) ⊕ ΠΛ²(V_q)`
2. `A₂..A₅` の ordinary trace / supertrace / BF determinant を graded 側の量として並べ直す
3. `e₂(A₅)=11=tr(Λ²A₅)` が `∧²` 側のどの obstruction count に対応するかを特定する

### 7.2 伸びる案

1. `A₄(t)` self-duality  
   `χ(t,λ)+χ(t,-λ)=4(1-λ^4)` は even envelope が `t` 非依存であることを示す。`A₅` でこの保護が破れた理由を、Paper III の odd leakage として説明できるかを調べる。
2. trace power の符号振動  
   `A₅` だけが初期から正負を振る。これを anti-copy の exchange phase の離散痕跡として読めるか確認する。
3. supertrace への格上げ  
   ordinary trace をそのまま supertrace と同一視せず、graded lift の上で初めて supertrace を定義する。

## 8. 現時点の kernel paragraph

現時点で一番強い読みはこれである。

`q=5` の異常は、単なる数値の破れではない。決定的なのは `e₂(A₅)=11` が一般公式により `tr(Λ²A₅)` そのものだという点である。Paper III の anti-copy の像は `∧²V(X)` にあるので、automath 側で正に跳ねた `11` は、こちらの語彙では「反対称 2体 sector の正味寄与」と読める。さらに `q=4 → 5` で `(tr(Sym²A_q), tr(Λ²A_q))` が `(11,-7)` から `(-7,11)` へ座標交換し、graded second lift の supertrace も `+18 → -18` と正確に反転する。したがって、先方が投げてきた「`q=5` の符号反転は `Z₂`-graded 構造と繋がるのではないか」という球に対するこちらの最短応答は、`q=5` を anti-copy sector が copy sector を追い越す **2次 lifted 位相反転点** として扱うことである。なお、`q=8,9,10` の local proxy では第二の位相反転はまだ見えていないため、現時点では `q=5` を一回限りの境界点として読むほうが強い。
