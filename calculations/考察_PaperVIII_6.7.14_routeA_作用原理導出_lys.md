# 6.7.14 Route A — 作用原理からの累積 law 導出面

**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md` §6.7.14b の

```text
dα_E/dθ = (1/2) sinθ
```

を、既存の作用・変分原理からどこまで引けるかを固定する補助面。  
目標は「導けるならどの quantity として導けるか」「導けないならどこで止まるか」を、SOURCE と INFERENCE に分けて確定することにある。

## P-0 Prolegomena

**対象**: route A  
`d\alpha_E/d\theta=(1/2)\sin\theta` を、Paper I の既存作用・変分原理から引く。

**含む**:

- Paper I §3.4 の二次作用 `S[\Phi]`
- Paper I Appendix D.2 の曲率ノルム分離
- Paper I §6.2-6.4 の拡張作用 `S[\Phi,\alpha]`
- Paper VIII §6.7.14 の Euler path 正規化

**除外**:

- `typed decategorification`
- `η / E_p` の再説明
- `global A`
- `α_E` を bulk energy density と同一視する強主張

### SOURCE

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文I_力としての忘却_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_PaperVIII_6.7.14_証明圧固定_lys.md`

[CHECKPOINT P-0/5]

## P-1 Scale Setting

粒度: `MEDIUM`  
深度: `STANDARD`

理由: いま必要なのは theorem の完成ではなく、「既存の作用から直接出る law」と「その作用から抽出された一次量を積分して初めて出る law」を分けることだからである。

[CHECKPOINT P-1/5]

## P-2 Decomposition

route A を 4 要素へ分解する。

| 要素 | 独立変数 | 役割 |
| :--- | :--- | :--- |
| `bulk_action_density` | `(1/4)F_{ij}F^{ij}` | 既存の二次作用密度が path 上で何を与えるか |
| `norm_flux_density` | `\|F\|_g` | 作用の kinetic term から抽出される一次量 |
| `cumulative_normalization` | `\alpha_E(\theta)` | どの density を累積忘却度として読むか |
| `alpha_field_obstruction` | `\delta S/\delta\alpha = 0` | 既存の α-field 変分が別の object を出していないか |

MECE 判定:

- `bulk_action_density` は energy density
- `norm_flux_density` は flux / work 的 density
- `cumulative_normalization` は path observable の定義
- `alpha_field_obstruction` は別系統の変分解

重複はない。

[CHECKPOINT P-2/5]

## P-3 Deep Dive

### 要素 1: `bulk_action_density`

**SOURCE**: Paper I §3.4 は

```text
S[Φ] = ∫ [(1/4) F_{ij}F^{ij} + (λ/2)Φ²] √g d^nθ
```

を基本作用として置く。  
**SOURCE**: Appendix D.2 は指数型分布族で

```text
\|F\|_g = (|α|/2) \|dΦ\|_g \|T\|_g |\sin θ_{dΦ,T}|
```

を与える。  
**INFERENCE**: したがって kinetic term の局所 density は

```text
(1/4)F_{ij}F^{ij} \propto \|F\|_g^2 \propto \sin^2 θ
```

であり、**二次作用密度をそのまま累積しただけでは `sinθ` ではなく `sin²θ` が出る**。  
これは route A の最初の重要な分岐である。

### 要素 2: `norm_flux_density`

**SOURCE**: Appendix D.2 の boxed formula は、同じ場の強さから一次量

```text
\|F\|_g \propto |\sin θ|
```

を切り出せることを示している。  
**INFERENCE**: したがって route A は bulk action density では失敗しても、**作用の kinetic term が生む曲率ノルムの line-flux** に読み替えると `sinθ` 核を回収できる。

### 要素 3: `cumulative_normalization`

**SOURCE**: Paper VIII §6.7.14a は、Euler path を半周期 `θ∈[0,π]` の正規化経路として固定している。  
**INFERENCE**: この経路上で prefactor が一定に吸収されているなら、曲率ノルムの線密度は

```text
ρ_F(θ) = K sinθ
```

と書ける。ここで

```text
α_E(θ) := (∫_0^θ ρ_F(φ) dφ) / (∫_0^π ρ_F(φ) dφ)
```

と **normalized cumulative curvature flux** として定義すれば、

```text
dα_E/dθ = ρ_F(θ) / ∫_0^π ρ_F(φ)dφ = sinθ / 2
```

が従う。  
したがって route A は、

```text
α_E = bulk energy の累積
```

としてではなく、

```text
α_E = curvature flux / work 的な一次量の正規化累積
```

として読むと成功する。

### 要素 4: `alpha_field_obstruction`

**SOURCE**: Paper I §6.2-6.4 の拡張作用 `S[Φ,α]` は、`δS/δα = 0` から `tanh` 型遷移層を与える。  
**INFERENCE**: ここで変分されている `α(θ)` は、観測レジームの精度場であり、Paper VIII §6.7.14 の `α_E` とは別 object である。  
ゆえに既存の α-field 変分をそのまま route A の証拠として使うことはできない。そこから直ちに出るのは `tanh` であって、`sinθ/2` ではない。

### 浮上次元

1. **二次作用密度そのもの**からは `sin²θ` が出る。  
2. **同じ作用の kinetic term から抽出した一次の曲率ノルム流束**なら `sinθ` が出る。  
3. route A が成立するのは、`α_E` を energy ではなく flux/work 的 observable として型付けしたときだけである。  
4. 既存の α-field 変分方程式は別変数を支配しており、ここへ直接流用してはいけない。

[CHECKPOINT P-3/5]

## P-4 Integration

再構成すると、route A の判定は次の 1 文に圧縮できる。

```text
既存の二次作用 S[Φ] から dα_E/dθ=(1/2)sinθ は直接は出ないが、その kinetic term が与える曲率ノルムの一次流束を Euler path 上で正規化累積量 α_E と読むなら、この law は既存 SOURCE の延長として導ける。
```

この圧縮の内訳は次である。

- `bulk_action_density` ルート:
  `sin²θ` を与える  
  → target law に直接は届かない
- `norm_flux_density` ルート:
  `sinθ` を与える  
  → normalized cumulative flux としてなら target law に届く
- `alpha_field_obstruction`:
  `tanh` を与える別系統  
  → route A の直接根拠には使えない

したがって、Paper VIII 側で safely 主張できる route A の最小版は次になる。

```text
Route A' (typed):
α_E を Euler path に沿う normalized cumulative curvature flux として読むなら、
Appendix D.2 のノルム分離と 6.7.14a の正規化から
dα_E/dθ = (1/2)sinθ
が従う。
```

逆に、次は言ってはならない。

```text
Route A_strong:
二次作用密度 (1/4)F_{ij}F^{ij} そのものから dα_E/dθ=(1/2)sinθ が出る
```

これは false であり、そこから自然に出る局所 density は `sin²θ` だからである。

**再説明**: ここで起きている差は、「熱量を積み上げるか」「流量を積み上げるか」の違いに近い。二乗したエネルギー密度を足し上げると山の形は `sin²` になる。だが、実際に経路に沿ってどれだけ“力が流れたか”を数える一次量を積み上げると `sin` になる。Paper VIII の `α_E` を後者として読むなら、route A は立つ。

ρ_hard: `ρ₂=0 ρ₃=0 ρ₄=0 total=0`  
ρ_soft: `ρ₀=0 ρ₁=0`

[CHECKPOINT P-4/5]
