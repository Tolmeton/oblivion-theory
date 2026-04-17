# 6.7.14 accumulation law の最小追加公理 — 分析面

**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md` §6.7.14b の

```text
dα_E/dθ = (1/2) sinθ
```

を、Route B の最小追加公理としてどこまで削れるかを固定する補助面。  
目標は「何をまだ追加公理として受理しなければならないか」を 1 文まで圧縮し、逆にそれ以上削ると何が失われるかを明示することにある。

## P-0 Prolegomena

**対象**: Route B  
`dα_E/dθ=(1/2)\sin\theta` を、どの最小追加公理で保持できるかを確定する。

**含む**:

- Paper VIII §6.7.14a-b の `E1 / E2 / E3`
- 正規化 Euler path 上の局所非整列密度 `\rho_E(\theta)\propto\sin\theta`
- `α_E` の累積意味論
- `1/2` がどこから出るか

**除外**:

- Route A' の donor 導出そのもの
- `η / E_p` の再説明
- boundary closure の再証明
- body の即時書換

### SOURCE

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_PaperVIII_6.7.14_証明圧固定_lys.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_theta_alpha累積公理_lys.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_PaperVIII_6.7.14_routeA_作用原理導出_lys.md`

[CHECKPOINT P-0/5]

## P-1 Scale Setting

粒度: `MEDIUM`  
深度: `STANDARD`

理由: ここで必要なのは新しい導出ではなく、Route B が要求する追加公理を

```text
必要十分に近い 1 文
```

まで痩せさせることだからである。

[CHECKPOINT P-1/5]

## P-2 Decomposition

いまの `6.7.14a-b` が背負っている追加 payload を 4 要素へ分解する。

| 要素 | 独立変数 | 役割 |
| :--- | :--- | :--- |
| `density_source` | `\rho_E(\theta)` | path 上で局所非整列がどう測られるか |
| `cumulative_semantics` | `α_E(b)-α_E(a)` | 局所密度を累積忘却度に変換する規則 |
| `endpoint_normalization` | `α_E(0), α_E(\pi)` | 累積量の始点・終点を固定する |
| `coefficient_fixing` | `1/2` | `\sin\theta` の前係数を一意化する |

MECE 判定:

- `density_source` は局所量
- `cumulative_semantics` は積み上げの意味論
- `endpoint_normalization` は全体の規格化
- `coefficient_fixing` は数値化

役割の重複はない。

[CHECKPOINT P-2/5]

## P-3 Deep Dive

### 要素 1: `density_source`

**SOURCE**: Paper VIII §6.7.14a は、正規化 Euler path では Paper I §5.9 の prefactor が吸収され、局所非整列密度は角度因子 `\sin\theta` のみで与えられると置く。  
**INFERENCE**: したがって Route B が新たに要求するのは「局所量そのもの」ではない。既に path の局所密度

```text
ρ_E(θ) ∝ sinθ
```

は与えられている。

### 要素 2: `cumulative_semantics`

**SOURCE**: 現行本文の `E1 / E2 / E3` は、

- 局所増分はその場の局所非整列度に依存する
- 局所非整列が 2 倍なら累積率も 2 倍
- 始点 0、終点 1

という 3 本に分かれている。  
**INFERENCE**: しかしこれら 3 本は、実は次の 1 文へ圧縮できる。

```text
Acc-min:
正規化 Euler path 上で、累積忘却度 α_E は局所非整列密度 ρ_E の正規化累積量である。
```

より具体的には

```text
α_E(b) - α_E(a)
= (∫_a^b ρ_E(φ)dφ) / (∫_0^π ρ_E(φ)dφ)
for 0 ≤ a ≤ b ≤ π
```

を受理すればよい。

この 1 文から直ちに次が出る。

- **局所性**: 微小増分はその点の `ρ_E` だけで決まる
- **一次性**: 積分は線形だから、局所密度が 2 倍なら増分も 2 倍
- **単調性**: `ρ_E ≥ 0` なら `α_E` は単調増加

つまり `E1 / E2` は独立公理ではなく、`Acc-min` の展開形として読める。

### 要素 3: `endpoint_normalization`

**INFERENCE**: `Acc-min` の分母が全区間積分である以上、

```text
α_E(0)=0
α_E(π)=1
```

は追加で仮定しなくても出る。  
したがって `E3` も独立公理ではなく、**正規化累積量**であることの帰結である。

### 要素 4: `coefficient_fixing`

**SOURCE**: `ρ_E(θ) ∝ \sin\theta`  
**INFERENCE**: `ρ_E(θ)=K\sin\theta` と書けば、`Acc-min` から

```text
dα_E/dθ
= ρ_E(θ) / ∫_0^π ρ_E(φ)dφ
= K sinθ / (K ∫_0^π sinφ dφ)
= sinθ / 2
```

が従う。  
ここでは `K` が打ち消えるため、`1/2` を別に仮定する必要がない。

ゆえに

```text
dα_E/dθ = (1/2)sinθ
```

は Route B の最小追加公理そのものではなく、`Acc-min + ρ_E(θ) ∝ sinθ` から出る**導出結果**である。

### どこまで削れるかの下限

これ以上削って、たとえば

```text
α_E は単調増加で α_E(0)=0, α_E(π)=1
```

だけにすると、

```text
α_E(θ)=θ/π
α_E(θ)=(θ/π)^2
α_E(θ)=sin^4(θ/2)
```

のような別解がすべて残る。  
つまり `sin^2(θ/2)` は一意に出ない。

したがって Route B の最小核は、単なる endpoint 条件や monotonicity では足りない。  
**「局所密度の正規化累積」** という意味論までは残さなければならない。

### Route A' との関係

**INFERENCE**: Route A' は `ρ_E` を既存作用の kinetic term から来る **curvature flux density** として donor 側から支える。  
しかし Route B に必要なのは `ρ_E` の由来の完全導出ではなく、

```text
α_E が ρ_E の正規化累積量である
```

という最小意味論だけである。  
したがって Route A' は Route B の代替ではなく、後からその `ρ_E` を強化する donor strengthening route だと読める。

### 浮上次元

1. `E1 / E2 / E3` は 3 本の独立公理ではなく、`Acc-min` の展開形として 1 本へ圧縮できる。  
2. `1/2` は新しい公理ではなく、`ρ_E(θ) ∝ sinθ` の全区間正規化から出る。  
3. Route B の irreducible core は

```text
α_E = ρ_E の正規化累積量
```

という意味論だけである。  
4. これ以下へ削ると `α_E` が不定になり、`sin^2(θ/2)` は選べなくなる。

[CHECKPOINT P-3/5]

## P-4 Integration

再構成すると、Route B の最小追加公理は次の 1 文に圧縮できる。

```text
Route B_min:
正規化 Euler path 上で、累積忘却度 α_E は局所非整列密度 ρ_E の正規化累積量である。
```

この 1 文を区間形で書けば

```text
α_E(b)-α_E(a)
= (∫_a^b ρ_E(φ)dφ) / (∫_0^π ρ_E(φ)dφ)
```

である。  
そして既存の `ρ_E(θ) ∝ sinθ` を入れると

```text
dα_E/dθ = (1/2)sinθ
α_E(θ)=sin²(θ/2)
```

が出る。

したがって結論は次の 3 行に尽きる。

```text
削れるもの:
E1 / E2 / E3 の分立、係数 1/2 の独立仮定

削れないもの:
α_E を ρ_E の正規化累積量として読む意味論

Route B の最小核:
「局所密度の正規化累積」として α_E を定義すること
```

**再説明**: いまの本文は、「その場のズレが積み上がって忘却進行度になる」と言いたい。その言いたさを最小にすると、「忘却進行度とは、局所的なズレの強さを道のりとして足し上げ、全体で 1 に規格化した量である」に尽きる。`E1 / E2 / E3` はその一文を展開した説明であって、核そのものではない。

ρ_hard: `ρ₂=0 ρ₃=0 ρ₄=0 total=0`  
ρ_soft: `ρ₀=0 ρ₁=0`

[CHECKPOINT P-4/5]

## Verification

- `Route B_min` は `ρ_E(θ) ∝ sinθ` と組み合わさると `1/2` を自動回収できる
- `E1 / E2 / E3` を個別に仮定しなくても、同じ結論へ届く
- monotonicity + endpoints だけでは `α_E` が非一意になる

→ 結論: Route B の最小追加公理は 1 文まで削れるが、それ以下へは削れない。
