# 投稿前深化メモ — automath 返信をいま出さない理由と、次に深めるべき核

作成日: 2026-04-14  
位置づけ: closed issue `#25` / merged PR `#28` の後に、すぐ issue を立てず、問いそのものを一段深く再定式化するための内部メモ。

## 文書ネットワーク

- `e₂ / Lucas` 外向き草案: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/automath_bridge/post_merge_issue_drafts/issue_draft_e2_boundary_resonance.md`
- `chain map` 外向き草案: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/automath_bridge/post_merge_issue_drafts/issue_draft_chain_map_flat_sector.md`
- `q=6..10` probe 正本: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_q6q7_probe.md`
- `q=5` source / `Z₂` 接続: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/調査_automath_q5符号反転とPaperIII_Z2接続.md`
- functoriality 再定式化: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/automath_bridge/functoriality_reduction.md`
- 閾値 hub: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/構想_automath_第一障害可視化閾値.md`
- `K_q` ontology: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Kq定義_noe.md`
- Problem 10 reduction: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Problem10_reduction_map.md`

## 0. kernel

いま必要なのは「返信するかどうか」ではない。  
必要なのは、先方が投げた二つの問いを、より強い問いへ変形することである。

変形前:

- `e₂(A₅)=L₅` は isolated coincidence か、structural relation か
- Amari-Chentsov complex から Walsh-Stokes complex への chain map 候補はあるか

変形後:

- `e₂(A₅)=L₅` は family law を探す問いではなく、`q=5` をどういう **threshold / boundary** として読むべきかという問いではないか
- chain map の有無を問うのではなく、**どこまでは strict に閉じ、どこから defect / obstruction が立ち上がるのか** を問うべきではないか

この変形が固まる前に issue を立てると、外向き草案は正しくても、問いの水準がまだ一段浅い。

## 1. 外に出してよい硬い事実

ここでは SOURCE と local computation を分ける。

### 1.1 `e₂ / Lucas` 側

#### SOURCE

- `q=4 -> 5` で `(\mathrm{tr}(\mathrm{Sym}^2 A_q), \mathrm{tr}(\Lambda^2 A_q))` が `(11,-7) -> (-7,11)` と座標交換する
- `q=4 -> 5` で graded second lift の supertrace が `+18 -> -18` と反転する
- `q=5` official kernel では `e₂(A₅)=11=L₅`

#### local computation

- `q=6,7` の exact moment-companion では `e₂(A₆)=-17`, `e₂(A₇)=-26`
- `q=5` official kernel を再現する sign-flip 規約延長では `e₂(A₆)=17`, `e₂(A₇)=26`
- したがって、どちらの読みでも `e₂(A_q)=L_q` は `q>5` ですぐ壊れる
- `q=8,9,10` の local proxy では `\Lambda^2` 優勢は持続し、再交換は見えない

#### 外向きに言ってよい最短文

`e₂(A₅)=L₅` は family law ではない。  
ただし `q=5` の structural specialness 自体は消えず、むしろ second-lift balance の位相境界として sharpen される。

### 1.2 `chain map` 側

#### SOURCE / Lean-certifed

- projection / restriction の strict functoriality は Lean で閉じている
- defect 側は xor-cocycle として compose law を持つ

#### local formalization

- product Bernoulli chart `M_I=(\Delta^1)^I`
- multilinear observable
- cubical face integration

に制限すれば、

`d -> deltaSet`  
`\int -> walshFlux`

の square は cochain level で strict に閉じる。

#### 外向きに言ってよい最短文

chain map 候補は「ある」。  
ただしそれは full complex ではなく、flat / cubical / multilinear sector に制限したときに限る。

## 2. まだ内部仮説として保持すべきもの

ここは外向きに断定しない。  
書くなら hypothesis / current reading / conjectural packaging と明示する。

### 2.1 `q=5` は第一障害可視化閾値である

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/構想_automath_第一障害可視化閾値.md`
の強い読みは次である。

- `X_q := tr(\Lambda^2 A_q)` は anti-copy / exclusion 側の 2体 sector
- `E_q := |det(I-A_q)| - F_{2q-2}` は arithmetic excess
- `K_q := [\kappa_q]` は global extension の first obstruction class

そして `q=5` は、これらが初めて同時に立ち上がる threshold ではないか、という読みである。

この読みは強い。  
しかし現時点では、

- `K_q` の representative はまだ確定していない
- `k_q := 1_{K_q \neq 0}` の first visibility を source で押さえていない
- official convention と exact companion convention の差を理論内部で処理し切れていない

ので、外向きにはまだ出さない。

### 2.2 `e₂(A₅)=L₅` は boundary resonance である

これは intuition としてかなり良い。  
ただし「boundary resonance」は今のところ説明語であって、定義ではない。

外に出す前に最低限必要なのは、

- 何が resonance しているのか
- 値の一致ではなく、どの量の同時可視化を指すのか
- なぜ `q=5` が family start ではなく boundary point なのか

を短く定義することだ。

現時点の内部定義案:

> boundary resonance = `q=q*` でのみ、2体 exclusion sector の可視量と arithmetic excess が偶然以上の強さで重なること

この wording はまだ内部用である。

### 2.3 full bridge の本体は chain map ではなく first obstruction class である

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Kq定義_noe.md`
と
`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_automath_Problem10_reduction_map.md`
の線では、

- flat strict chain map は既にある
- global で立つのは defect
- その本体は defect 2-cell や 2-cocycle そのものではなく `K_q := [\kappa_q]`

という整理ができている。

これは理論として一番強い。  
しかし外に出すにはまだ、

- `Int_q` の構成
- event quantum `\lambda_q` の規格化
- continuous curvature data と discrete carry defect が同じ class を与える条件

が抜けている。

したがって現時点で外向きに言うべきなのは

> open problem の核は strict chain map の不存在ではなく、global extension における defect / coherence の記述である

までで止める。

## 3. いまの草案がまだ早い理由

二本の issue 草案は、それぞれ単体では正しい。  
ただし次の点でまだ浅い。

### 3.1 `e₂` 草案の浅さ

現行草案は

- `q=6,7` 反例
- `q=5` は boundary resonance

で止まっている。

だが内部で見えている問いはもう一段強い。

- 「Lucas 法則は続くか」ではない
- 「何が `q=5` で初めて可視化されるのか」である

外向きの issue は、その再定式化が一文で言えるようになってから出した方がよい。

### 3.2 `chain map` 草案の浅さ

現行草案は

- flat sector での cochain map candidate
- global extension は open

で止まっている。

だが本当の強みは、

- 問題を三層に分けたこと
- ordinary functor の問いではなく、defect-bearing bridge の問いへ変えたこと

にある。

よって外に出す前に、

- strict layer
- flat chain-map layer
- global coherence layer

の三層命題としてさらに明確化した方がよい。

## 4. 投稿前に最低限詰めるべき穴

### 4.1 `e₂ / Lucas`

最低限ほしいのは次の三点である。

1. `boundary resonance` の短い定義  
   何が共鳴しているのかを一文で固定する。

2. `q=5` の specialness を言い切るための保守的 wording  
   `first visible second-lift threshold` なのか  
   `first visible obstruction threshold` なのか  
   ここは外向き文言をまだ選び切れていない。

3. `q=8,9,10` proxy の扱い  
   書くなら必ず `official kernel ではない local proxy` と明記する。

### 4.2 `chain map`

最低限ほしいのは次の三点である。

1. subcomplex の明示名  
   いまは product Bernoulli / multilinear / cubical sector と説明しているだけで、対象名がまだない。

2. cochain-level statement の形  
   theorem ではなくても、map の domain / codomain を一行で書ける形にする。

3. global open problem の wording  
   `pseudofunctor / lax monoidal bridge / defect-bearing bridge` のどれを外向き主語にするかを固定する。

## 5. いまの最良の再定式化

現時点で最も筋がよい読みは次である。

### 5.1 `e₂` 側

`e₂(A₅)=L₅` は「Lucas が exterior trace を与える法則」ではない。  
それは `q=5` で anti-copy / exclusion 側の 2体 sector が初めて前景化したときに生じた、境界的一致である。

ここで追うべきものは `11` の持続ではない。  
追うべきものは、なぜ `5` が最初の可視化点なのか、である。

### 5.2 `chain map` 側

bridge の本丸は、Amari-Chentsov complex から Walsh-Stokes complex への strict chain map の単純存在ではない。  
flat sector では strict square は既に書ける。  
本当に難しいのは、その strict part を global な carry-defect world へ延長するときに何が障害として立ち上がるかである。

言い換えれば、問いは

`chain map はあるか`

ではなく、

`strict chain map の first obstruction は何か`

へ移すべきである。

## 6. 次の具体作業

次に着手すべきなのは投稿ではなく、次の二本である。

### A. 外向き語彙の固定メモ

目的:

- `boundary resonance`
- `first visible threshold`
- `global coherence defect`

の三語を、外に出しても claim 過多にならない文言へ削る。

### B. flat-sector theoremization メモ

目的:

- domain / codomain の explicit naming
- `\mathcal D_A(\omega)(w)` の statement を、issue 本文ではなく theorem skeleton にする
- global layer との境界を一文で切れるようにする

## 7. 現時点の判断

まだ投稿しない。  
ただし、止まっているわけでもない。

状態は次の通りである。

- 反例は十分ある
- flat-sector candidate も十分ある
- まだ不足しているのは、**問いの焦点化と言葉の格付け** である

したがって次の一手は、新規 issue ではなく、

1. `e₂` 側の外向き語彙を詰める
2. `chain map` 側の三層構造を theorem skeleton に落とす

である。
