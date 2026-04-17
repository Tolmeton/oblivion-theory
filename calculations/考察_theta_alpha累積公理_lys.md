# θ↔α 累積公理 — 分析面

**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md` §6.7.14 の Euler 累積補題候補を、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` に移す前に、`θ↔α` の橋がどこまで SOURCE でどこからが追加公理かを固定する補助面。

## P-0 Prolegomena

**対象**: `θ↔α` 累積公理の最小内容を、SOURCE と INFERENCE を切り分けて確定する。  
**含む**: 正規化 Euler path、局所非整列密度 `\sin\theta`、累積 law、η との開区間整合、boundary closure。  
**除外**: `base-fiber` の再定義、typed decategorification、指数核、global A。

### SOURCE

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_basefiber公理_lys.md`

[CHECKPOINT P-0/5]

## P-1 Scale Setting

粒度: `MEDIUM`  
深度: `STANDARD`

理由: ここでは完全再証明ではなく、「何が既存 SOURCE により支えられ、何が統一表ドラフトで受理すべき最小追加公理か」を切ることが目的だからである。

[CHECKPOINT P-1/5]

## P-2 Decomposition

`θ↔α` 累積公理候補を 4 要素へ直交分割する。

| 要素 | 独立変数 | 役割 |
| :--- | :--- | :--- |
| `density` | `\rho_E(\theta)` | 局所非整列が path 上でどう測られるかを決める |
| `accumulation` | `d\alpha_E/d\theta` | 局所密度から累積忘却度を作る変換則 |
| `open_interval_bridge` | `\eta(\alpha_{\mathrm{III}}^E(\theta))=\alpha_E(\theta)` | 開区間 `(0,\pi)` での pathwise 整合を与える |
| `endpoint_closure` | `\bar\eta(\pm\infty)` | 端点 `0,\pi` を既存境界公理へ閉じる |

MECE 判定:

- `density` は局所量
- `accumulation` は積分則
- `open_interval_bridge` は開区間整合
- `endpoint_closure` は端点処理

同じ役割の言い換えは含まれていない。

[CHECKPOINT P-2/5]

## P-3 Deep Dive

### 要素 1: `density`

**SOURCE**: Paper VIII §6.7.14a は、正規化された Euler path では Paper I §5.9 の prefactor が吸収され、経路に沿って変化する局所非整列密度は角度因子 `\sin\theta` のみで与えられる、と置く。  
**INFERENCE**: `θ↔α` の橋は、いきなり `θ` そのものを `α` に等置するのではなく、まず `θ` から局所密度 `\rho_E(\theta)\propto\sin\theta` を取り出す段を持つ。

### 要素 2: `accumulation`

**SOURCE**: Paper VIII §6.7.14a-b は (E1) 局所性、(E2) 一次性、(E3) 正規化から

```text
dα_E/dθ = K sinθ
```

を導き、境界条件で `K=1/2` を固定して `α_E(\theta)=(1-\cos\theta)/2` を得る。  
**INFERENCE**: したがって `θ↔α` 公理の本体は、「`θ` が `α` に変わる」のではなく、「局所密度が累積されて `α_E` になる」という accumulation law である。

### 要素 3: `open_interval_bridge`

**SOURCE**: Paper VIII §6.7.14c は

```text
α_III^E(θ) = log( α_E(θ) / (1-α_E(θ)) )
η(α_III^E(θ)) = α_E(θ)
```

を与え、`θ → α_III^E → α_E` の可換性を開区間 `(0,\pi)` 上で立てる。  
**INFERENCE**: これで η は「単なる値域変換」ではなく、Euler path 上の累積忘却度を `α_III → α_VIII` 橋へ接続する open-interval bridge になる。

### 要素 4: `endpoint_closure`

**SOURCE**: Paper VIII 命題 6.7.4c は `\bar\eta(-\infty)=0`, `\bar\eta(+\infty)=1` を与え、忘却濾過の端点 `C_0=C`, `C_1=C_disc` と整合させる。  
**SOURCE**: Paper VIII §6.7.14c は `\theta\to 0^+` で `α_III^E(\theta)\to-\infty`、`\theta\to\pi^-` で `α_III^E(\theta)\to+\infty` を示す。  
**INFERENCE**: 端点の可換性は η 単独ではなく、`open_interval_bridge + boundary closure` の合作で初めて閉じる。

### 浮上次元

1. `θ↔α` は点ごとの変換ではなく、`局所密度 → 累積 → 開区間整合 → 端点閉包` の 4 段構造である。  
2. 真に追加公理として要るのは accumulation law の採用であり、η と boundary closure は既存 SOURCE の接合でかなりの部分が支えられる。  
3. `base-fiber` が「どの殻の内部運動か」を決め、`θ↔α` は「その殻の内部運動がどう累積忘却へ変わるか」を決める。

[CHECKPOINT P-3/5]

## P-4 Integration

再構成すると、`θ↔α` 累積公理の最小版は次の 1 文に圧縮できる。

```text
正規化された Euler path 上では、局所非整列密度 ρ_E(θ) ∝ sinθ に沿って累積忘却度 α_E が増加し、その open-interval 値は η により α_III 系と可換に接続され、端点は既存の boundary closure で閉じる。
```

この 1 文の内訳は次の通りである。

- `ρ_E(\theta)\propto\sin\theta` は Paper VIII §6.7.14a の SOURCE
- `d\alpha_E/d\theta=(1/2)\sin\theta` と `\alpha_E(\theta)=\sin^2(\theta/2)` は Paper VIII §6.7.14b の SOURCE
- `η(α_{\mathrm{III}}^E(\theta))=\alpha_E(\theta)` は Paper VIII §6.7.14c の SOURCE
- 端点 `0,1` への閉包は Paper VIII 命題 6.7.4c の SOURCE

したがって、統一表ドラフト側で新しく主張すべき最小形は次になる。

```text
θ↔α 累積公理:
base-fiber 公理で固定された sector の内部では、正規化 Euler path に沿う局所非整列密度が累積忘却度 α_E を決める。開区間ではこの α_E は η と pathwise に整合し、端点は既存の boundary closure によって閉じる。
```

この形なら、`θ=α` とは言っていないし、η だけで端点まで閉じるとも言っていない。また `base-fiber` と役割が被っていない。`base-fiber` が殻を決め、`θ↔α` がその殻の内部の累積則を決める、という分業が保たれている。

**再説明**: `θ↔α` 累積公理は、「角度をそのまま忘却度に読み替える」公理ではない。角度からまず局所的なズレの強さを取り出し、それを道のりとして積分してはじめて忘却進行度にし、その途中では η が III 系と VIII 系を繋ぎ、道の端では既存の境界閉包が最後を閉じる、という四段の橋である。

ρ_hard: `ρ₂=0 ρ₃=0 ρ₄=0 total=0`  
ρ_soft: `ρ₀=0 ρ₁=0`

[CHECKPOINT P-4/5]
