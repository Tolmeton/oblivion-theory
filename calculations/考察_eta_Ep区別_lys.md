# η と E_p の区別 — 分析面

**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md` §6.7.14c-d の `η` と `E_p` の役割差を、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` の Euler 累積要約節へ戻す前に固定する補助面。

## P-0 Prolegomena

**対象**: `η` と `E_p` が何を与え、何を与えないかを SOURCE と INFERENCE に分けて確定する。  
**含む**: `η` の開区間整合、boundary closure、`E_p` の order-preserving functor 性、Euler path の categorical content。  
**除外**: `θ↔α` 累積 law の再導出、typed decategorification、指数核、sectoral A。

### SOURCE

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_theta_alpha累積公理_lys.md`

[CHECKPOINT P-0/5]

## P-1 Scale Setting

粒度: `MEDIUM`  
深度: `STANDARD`

理由: ここで必要なのは新理論ではなく、「何がスカラー整合で、何が圏論的持ち上げか」という役割境界を切ることだからである。

[CHECKPOINT P-1/5]

## P-2 Decomposition

`η` と `E_p` の差を 4 要素へ直交分割する。

| 要素 | 独立変数 | 役割 |
| :--- | :--- | :--- |
| `scalar_bridge` | `η` | `α_{\mathrm{III}}^E` を `α_E` へ送るスカラー整合 |
| `endpoint_closure` | `\bar{\eta}` | 開区間外の端点を既存忘却濾過へ閉じる |
| `categorical_lift` | `E_p` | 経路順序を濾過列へ送る圏論的持ち上げ |
| `content_boundary` | `categorical content` | Euler path の意味をどこに置くかを定める |

MECE 判定:

- `scalar_bridge` は値の対応
- `endpoint_closure` は端点処理
- `categorical_lift` は関手構造
- `content_boundary` は意味の帰属

重複はない。

[CHECKPOINT P-2/5]

## P-3 Deep Dive

### 要素 1: `scalar_bridge`

**SOURCE**: Paper VIII §6.7.14c は

```text
η(α_III^E(θ)) = α_E(θ)
```

を与え、`θ → α_III^E → α_E` の可換性を開区間 `(0,\pi)` 上で立てる。  
**INFERENCE**: `η` が直接与えるのは、Euler path 上の量が III 系と VIII 系の間で**スカラーとして**整合することだけである。

### 要素 2: `endpoint_closure`

**SOURCE**: Paper VIII 命題 6.7.4c は `\bar{\eta}(-\infty)=0`, `\bar{\eta}(+\infty)=1` を与える。  
**SOURCE**: Paper VIII §6.7.14c は `α_III^E(\theta)` が端点で `\pm\infty` に発散すると述べる。  
**INFERENCE**: したがって `η` 単独では端点は閉じず、`η + boundary closure` の合作で初めて `α_E(0)=0`, `α_E(\pi)=1` が回復される。

### 要素 3: `categorical_lift`

**SOURCE**: Paper VIII §6.7.14d は

```text
E_p(\theta) := C_{α_E(\theta)}
```

を定め、`α_E` が単調増加なので `E_p` は経路順序を忘却濾過の縮退列へ送る order-preserving functor だと述べる。  
**INFERENCE**: ここで初めて Euler path は「圏論的内容」を持つ。`η` だけでは関手は出てこない。

### 要素 4: `content_boundary`

**SOURCE**: Paper VIII §6.7.14d は、「Euler path の categorical content はスカラー `α_E` 単体ではなく、それが誘導する濾過列 `E_p` にある」と明言する。  
**INFERENCE**: 統一表ドラフトで `η` と `E_p` を同列に並べると誤読を招く。役割は

```text
η = scalar bridge
E_p = categorical lift
```

で分離しなければならない。

### 浮上次元

1. `η` は橋だが、まだスカラー面に留まる。  
2. 端点は `η` ではなく `boundary closure` が閉じる。  
3. 圏論的持ち上げは `E_p` にあり、Euler path の categorical content もそこにある。

[CHECKPOINT P-3/5]

## P-4 Integration

再構成すると、最小形は次になる。

```text
η は Euler path 上の累積忘却度を III 系と VIII 系の間でスカラー整合させるが、圏論的持ち上げそのものではない。Euler path の categorical content は、α_E が誘導する濾過列 E_p にある。
```

この 1 文のうち、

- `η` の開区間整合は Paper VIII §6.7.14c の SOURCE
- 端点閉包は命題 6.7.4c の SOURCE
- `E_p` の関手性と categorical content は Paper VIII §6.7.14d の SOURCE

である。

したがって本文へ戻すべき最小版は、次で足りる。

```text
η/E_p 区別:
η が与えるのは開区間でのスカラー整合であり、端点は boundary closure が閉じる。Euler path の圏論的内容は E_p(θ)=C_{α_E(θ)} で与えられる濾過列にある。
```

**再説明**: `η` は地図上の座標変換に近い。道の各地点に別の座標を割り当てるが、それだけでは「道そのもの」はできない。`E_p` は、その道を順序つきの縮退列として実際に持ち上げたものだ。だから Euler path の本体は `η` ではなく `E_p` にある。

ρ_hard: `ρ₂=0 ρ₃=0 ρ₄=0 total=0`  
ρ_soft: `ρ₀=0 ρ₁=0`

[CHECKPOINT P-4/5]
