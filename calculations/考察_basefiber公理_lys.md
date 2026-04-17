# base-fiber 公理 — 分析面

**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文II_相補性は忘却である_草稿.md` の `Δd / α` 層化、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md` の CPS-ファイバー束対応、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` の `\mathrm{Bridge}(C,A;D_C)` を接合し、`base-fiber` 公理が何を言えば最小で済むかを分析する。

## P-0 Prolegomena

**対象**: `base-fiber` 公理の最小内容を、SOURCE と INFERENCE を分けて確定する。  
**含む**: Paper VIII の束構造、Paper II の底空間/ファイバー層化、統一表ドラフトの bridge carrier。  
**除外**: `θ↔α` の累積 law、`endpoint closure` の再証明、`Δd \leftrightarrow \alpha` の強導出、global A。

### SOURCE

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文II_相補性は忘却である_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_Deltad_alpha弱対応_lys.md`

[CHECKPOINT P-0/5]

## P-1 Scale Setting

粒度: `MEDIUM`  
深度: `STANDARD`

理由: ここで必要なのは完全定式化ではなく、「どこまでを一つの公理にまとめ、どこからは次の公理へ回すか」の境界線を引くことだからである。

[CHECKPOINT P-1/5]

## P-2 Decomposition

`base-fiber` 公理候補を 4 要素へ直交分割する。

| 要素 | 独立変数 | 役割 |
| :--- | :--- | :--- |
| `base` | `Δd` / Type / sector | 離散的な非対称性クラスを固定する |
| `fiber` | `α` | 固定された class の内部で連続的に動く局所状態を担う |
| `transport` | `CPS2` / path | 異なる fiber 点を比較可能にする移送則を与える |
| `readout` | `E_b(\theta)=C_{\alpha_b(\theta)}` | bridge 側で fiber の path を濾過列として表示する |

MECE 判定:

- `base` は分類
- `fiber` は局所状態
- `transport` は比較則
- `readout` は表示則

同じ変数の言い換えは含まれていない。

[CHECKPOINT P-2/5]

## P-3 Deep Dive

### 要素 1: `base`

**SOURCE**: Paper II §3.3 は `Δd` を「忘却関手のカーネル差が与える離散的な位相分類」と置き、Type を決める底空間として読む。  
**SOURCE**: Paper VIII §3.4 は CPS を「底空間 B と、その上のファイバー」からなる束として読む。  
**INFERENCE**: `base-fiber` 公理がまず保証すべきなのは、「Euler bridge に出てくる path は、何もない連続体の上を勝手に走るのではなく、固定された非対称性クラスの内部でのみ走る」という base fixation である。

### 要素 2: `fiber`

**SOURCE**: Paper II §3.3 は `α(θ)` を「固定 `Δd` の内部で動く局所精度」と明示する。  
**SOURCE**: Paper II の後半では `α`-twisted Markov category の族やファイバーバンドル構造が反復的に現れる。  
**INFERENCE**: `fiber` は「底空間の上に付随する局所状態」であり、`Δd` と同じ量ではない。したがって公理本文では、`fiber` を `base` の値そのものとしてではなく、「base の上で変動する連続パラメータ」と書く必要がある。

### 要素 3: `transport`

**SOURCE**: Paper VIII §3.4 は `CPS2` を異なるファイバーを結ぶ水平射、すなわち平行移動と読む。  
**SOURCE**: 統一表ドラフトの `\mathrm{Bridge}(C,A;D_C)` は path `\theta \mapsto (\alpha_b,E_b,U_b)` を carrier として持つ。  
**INFERENCE**: `base-fiber` 公理が transport を含まないと、`fiber` は単なる点の寄せ集めになり、`pathwise normalization` へ進めない。したがって最小公理でも「同じ base 内で fiber 点を比較できる水平移送」が必要になる。

### 要素 4: `readout`

**SOURCE**: 統一表ドラフトでは `E_b(\theta)=C_{\alpha_b(\theta)}` により、`α_b` が圏論的には濾過列として表示される。  
**SOURCE**: weak bridge 面は、`\alpha_b(\theta)` を「固定 sector の内部に選んだ標準 path の連続累積座標」と読む。  
**INFERENCE**: `base-fiber` 公理は `readout` まで全部言う必要はない。むしろ `readout` は bridge 側の実装層であり、公理本文では「fiber の path が chosen readout へ持ち上がる」とだけ言えば足りる。

### 浮上次元

1. `base-fiber` 公理の本体は **分類の固定** と **局所状態の可変** の分離である。  
2. 本当に新しく要るのは **transport** で、これがないと Paper VIII の束構造と統一表の path carrier が繋がらない。  
3. `readout` は本体ではなく、bridge 節での派生表示である。

[CHECKPOINT P-3/5]

## P-4 Integration

再構成すると、`base-fiber` 公理は次の 1 文に圧縮できる。

```text
固定された離散 class Δd がまず sector を定め、その sector の上で α が連続ファイバーとして変動し、同一 sector 内の fiber 点は水平移送で比較できる。
```

この 1 文のうち、

- `固定された離散 class Δd` は Paper II の SOURCE
- `sector の上で α が連続ファイバーとして変動` も Paper II の SOURCE
- `水平移送で比較できる` は Paper VIII の CPS2 から引ける SOURCE
- `bridge 側の path/readout へ持ち上がる` は統一表ドラフトの派生実装

である。

したがって、`base-fiber` 公理のクリティカルパスは

```text
Paper II の Δd / α 層化
  +
Paper VIII の CPS-ファイバー束対応
  ↓
same-sector horizontal transport
  ↓
統一表ドラフトの bridge carrier へ path として実装
```

になる。

最小版の公理文としては、次で足りる。

```text
base-fiber 公理:
各 Euler bridge path は、ある固定された非対称性 class Δd に属する sector の内部でのみ定義される。各 sector には連続ファイバー α が付随し、その点同士は CPS2 に由来する水平移送で比較可能である。
```

この形なら、まだ `θ↔α` の累積 law も `endpoint closure` も言っていない。つまり `base-fiber` は独立の最小公理として自立できる。

**再説明**: `base-fiber` 公理は、「山があるか」という離散分類と、「その山のどこを歩いているか」という連続状態を分けるだけでは足りず、同じ山の中の地点同士を“同じ山の運動”として比較できる水平移送まで入れて、初めて Euler bridge の path が意味を持つ、という主張である。これにより `Δd` を `α_b(\theta)` に潰す誤りを避けつつ、bridge carrier を空中戦にしない足場が立つ。

ρ_hard: `ρ₂=0 ρ₃=0 ρ₄=0 total=0`  
ρ_soft: `ρ₀=0 ρ₁=0`

[CHECKPOINT P-4/5]
