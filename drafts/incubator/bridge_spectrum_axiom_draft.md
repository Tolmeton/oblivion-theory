# Bridge Spectrum Axiom 試作

## — open #20 (橋梁 × スペクトル) cell のスペクトル的橋梁公理 —

**v0.1 (2026-04-17)**
**ステータス**: incubator draft / 試作 / 未完成 / SOURCE 骨格確立段階
**役割**: σ 統一論文 v0.3.4 §2.0.5 の C5 × C6 9 cell 候補マップで未論として残された **(橋梁担体層 × スペクトル軸) cell** のスペクトル的橋梁公理を試作する。本稿は候補 (b) Grothendieck fibration アプローチを主軸として検証する。

**親文書**:
- `../standalone/比較射σの統一定理_v0.1.md` v0.3.4 (§2.0.5 9 cell 格子 / §4.7.bis.7 open #20)
- `./Face5Lemma_draft.md` v0.3 (Face5 Lemma / F5-α 定理 / SU(2)_k family 検証)
- `./pentagon_sigma_conjecture.md` v0.4 (7+ 種袋、本試作は open #20 の別稿展開として登録)

**試作の目的**:
1. σ 統一論文 open #20 の候補 (b) 「Grothendieck fibration `BridgeDat → FusCat`」を紙上で形式化する
2. C9 (ENO universal) との整合を fibration の普遍性として読み直す
3. C2' (BridgeDat の Stasheff tower cell-wise 埋込) との合流点を同定する
4. 候補 (a) `d_b = (d, α_d)` / 候補 (c) tower 階層化 との比較を明示する

---

## §0 一文核

**SOURCE**:
σ 統一論文 §4.2 では位相軸の橋梁公理 `dU_b/dθ = iU_b, U_b(0) = 1_A` が `U_b(θ) = e^{iθ}` を一意解として与える。これは **連続 ODE 型** の bridge datum である。

Etingof-Nikshych-Ostrik (2005) 定理より、任意 fusion category の Frobenius-Perron 次元は totally real positive algebraic integer である。これはスペクトル軸の **離散代数的** endpoint を family 横断で保証する。

**INFERENCE**:
位相軸の連続 ODE 型と、スペクトル軸の離散代数的階段は、そのままでは同じ橋梁公理の形式に収まらない。両者を統一的に扱うには、**fusion category を底 (base) に持つ Grothendieck fibration** として bridge datum の family 構造を建てるのが自然である。各 fiber が「固定 fusion category での bridge data」であり、fiber 間の cartesian lift が「fusion category 間の関手に沿う bridge data の reindexing」を担う。

**OPEN**:
本稿は候補 (b) を試作する段階であり、定理 face には到達していない。FusCat の定義境界、cartesian lift の具体構成、ENO との整合の厳密化は open として残る。

---

## §1 問題設定 — open #20 の再整理

### 1.1 位相軸の橋梁公理 (§4.2 既済)

σ 論文 §4.2 は次を与える:

$$
\frac{dU_b}{d\theta} = i U_b, \quad U_b(0) = 1_A \quad\Rightarrow\quad U_b(\theta) = e^{i\theta}
$$

これは連続 1 変数 ODE で、初期値条件のもとで一意解を与える。位相パラメータ `θ ∈ [0, π]` で bridge datum 成分が連続変化する構造。

### 1.2 スペクトル軸の対応物 — 何が欠けているか

スペクトル軸に対応する bridge datum 成分は未定義である。対応物が持つべき性質を列挙する:

1. **family parameter に依存**: Ising (k=2), Fibonacci (k=3), SU(2)_4 (k=4), ... と family index で異なる値を取る
2. **階段的・離散的**: 連続変化ではなく、family index の離散変化で飛ぶ (`√2 → φ → √3 → ...`)
3. **代数的整数性**: ENO 定理 (C9) により `d ∈ \overline{\mathbb{Z}}_{\geq 0} \cap \mathbb{R}` の制約がかかる
4. **universal 性質**: 全 fusion category 族を貫く共通軸が存在する

連続 ODE 型の位相軸と、これらの性質を満たすスペクトル軸を同時に扱う形式が必要。

### 1.3 候補 3 方向の比較 (再掲 + 詳細化)

| 候補 | 形式 | 長所 | 短所 |
|:---|:---|:---|:---|
| **(a) `d_b = (d, α_d)`** | bridge datum に離散スペクトル成分を追加 | 現行 bridge datum 構造の最小変更 | family parameter の離散性が ODE 橋梁公理と非整合 |
| **(b) Grothendieck fibration** | `BridgeDat → FusCat` の fibered category 構造 | family parameter を base category として分離、ENO universal が自然 | 高い抽象度、FusCat の具体定義が open |
| **(c) Stasheff tower 階層化** | 各 `K_n` 層での cell-wise bridge datum | 骨格普遍層 (C5') との統合 | C5' 自体がまだ予想 face |

本稿は **(b)** を主軸に試作する。理由:
- family parameter を「空間」ではなく「空間族の基底」として明示的に扱える
- ENO universal (C9) が「fibration の全 fiber にわたる共通制約」として自然に位置づく
- (a) / (c) を包含しうる: (a) は (b) の特殊 fiber、(c) は (b) を Stasheff tower 上に特化

---

## §2 Grothendieck fibration 背景 (SOURCE 骨格)

本節は Grothendieck fibration の標準定義を再掲する。以下はすべて [SOURCE: SGA 1 (Grothendieck 1971), nLab "Grothendieck fibration", Borceux *Handbook of Categorical Algebra* Vol 2 §8.1]。

### 2.1 定義

**関手 `p: E → B` が Grothendieck fibration であるとは**:

任意の object `X ∈ E` と、base における任意の morphism `f: A → p(X)` に対し、次を満たす `X' ∈ E` と morphism `\tilde{f}: X' → X` が存在する:

1. `p(X') = A`, `p(\tilde{f}) = f`
2. (cartesian) 任意の `Y ∈ E` と `g: Y → X` で `p(g) = f \circ h` なるものに対し、`g = \tilde{f} \circ \tilde{h}` なる `\tilde{h}: Y → X'` が一意に存在する

このとき `\tilde{f}` を `X` 上の `f` の cartesian lift と呼び、`X' = f^* X` と書く。

### 2.2 Fibered category ⇄ pseudofunctor

Grothendieck construction により、fibration `p: E → B` は pseudofunctor `\Phi: B^{op} \to \mathsf{Cat}` と双対関係にある。

`\Phi(A) = E_A := p^{-1}(A)` (fiber over `A`)、`\Phi(f: A → B) = f^*: E_B → E_A` (reindexing functor)。

本稿では pseudofunctor 表現を主に使う:

$$
\Phi: \mathsf{FusCat}^{op} \to \mathsf{Cat}, \quad C \mapsto \mathsf{BridgeDat}(C, A)
$$

### 2.3 典型例 — 代数幾何 / 代数

- **Modules over rings**: `\mathsf{Mod} → \mathsf{Ring}`, `M \mapsto (\text{base ring of } M)`
- **Vector bundles over manifolds**: `\mathsf{VectBund} → \mathsf{Mfd}`
- **Sheaves over topological spaces**: `\mathsf{Sh} → \mathsf{Top}`

これらは「space が家族を動き、各 space 上に object が座る」構造の標準例である。本稿の提案は **「fusion category が家族を動き、各 fusion category 上に bridge datum が座る」** fibration を建てることに等しい。

---

## §3 候補 (b) の形式化

### 3.1 底圏 `FusCat` の定義候補

**問題**: `FusCat` を何と定めるか。

複数の候補がある:

#### 3.1.1 候補 3.1-A: FusCat = Fusion categories + fusion functors

対象: 全 fusion category (有限の simple object、semisimple、rigid monoidal、unit object は simple)。
射: fusion functor (テンソル積を保つ tensor functor)。

[SOURCE: Etingof-Gelaki-Nikshych-Ostrik *Tensor Categories* (2015) §4.1]

長所: 標準的、ENO 定理が fiber 全体で自然に働く。
短所: 射の分類が粗い。fusion functor の具体例 (例えば SU(2)_k → SU(2)_{k+1}) がどれだけ構成可能か未明。

#### 3.1.2 候補 3.1-B: FusCat = MTC + modular functors

対象: modular tensor category (MTC) — fusion + braided + modular。
射: modular functor (braiding と modular structure を保つ)。

長所: SU(2)_k series が MTC series として一貫性を持つ。σ の closure schema が持つ braided structure と整合。
短所: fusion category 全般から逸脱、より特殊な枠組み。

#### 3.1.3 候補 3.1-C: FusCat = {SU(2)_k}_k という sub-category (最小版)

対象: `{SU(2)_k : k \in \mathbb{Z}_{\geq 1}}` に限定。
射: level-shift map `SU(2)_k → SU(2)_{k+1}` の family 構造。

長所: 本稿の主例 SU(2)_k に特化、構成が明示的。
短所: ENO universal の power を活かせない (family 横断 claim が SU(2)_k 内に縮小)。

**本稿の暫定選択**: 3.1-A (fusion category + fusion functor) を標準として、3.1-C を最小例として並走させる。3.1-B は別稿扱い。

### 3.2 全圏 `BridgeDat` の定義

**定義 (試作)**:  
`BridgeDat` の対象は組 `(C, b)` で、
- `C ∈ \mathsf{FusCat}` (fusion category)
- `b = (\alpha_b, E_b, U_b, d_b) \in \mathsf{BridgeDat}(C, A)` (σ 論文 §4 の bridge datum + **スペクトル成分 `d_b`**)

スペクトル成分 `d_b` は `C` に依存する量で、典型的には:
- `d_b = d_{1/2}(k)` (SU(2)_k の基本表現の量子次元) の `C`-類似物
- ENO 定理により `d_b \in \overline{\mathbb{Z}}_{\geq 0} \cap \mathbb{R}`

射は `(C, b) \to (C', b')` で、
- `f: C \to C'` は fusion functor
- `\phi: b \to f^* b'` は `f^*` による reindexing 上の bridge morphism (σ 論文 §4.3 の bridge morphism を fibration に従って一般化)

ここで `f^*: \mathsf{BridgeDat}(C', A) \to \mathsf{BridgeDat}(C, A)` は fusion functor `f` の逆像としての reindexing functor。

### 3.3 射影関手 `p: \mathsf{BridgeDat} \to \mathsf{FusCat}`

定義: `p(C, b) = C`, `p(f, \phi) = f`。

**命題 (試作仮説 B-1)**:  
上記の定義のもと、`p: \mathsf{BridgeDat} \to \mathsf{FusCat}` は Grothendieck fibration である。

**証明の骨子 (試作)**:  
任意の `(C', b')` と任意の `f: C \to C'` に対し、reindexing `f^* b' \in \mathsf{BridgeDat}(C, A)` が定義できれば、`\tilde{f}: (C, f^* b') \to (C', b')` が cartesian lift になる。

reindexing の明示構成:
- `\alpha_{f^* b'} = \alpha_{b'}` (忘却度は family-independent)
- `E_{f^* b'}` = `f^{-1}` 経由で `C` 上に pull-back された濾過 (σ 論文 §4.1 の `E_b` 定義を使う)
- `U_{f^* b'} = U_{b'}` (位相軸は family-independent、`e^{iθ}` のまま)
- **`d_{f^* b'}` = `f` による `d_{b'}` の像** (スペクトル軸: fusion functor が表現の次元を保存するかは `f` の性質に依存)

[TAINT]: `d` の reindexing の well-definedness は fusion functor が Frobenius-Perron 次元を保つかに依る。標準 fusion functor は FP 次元を保つ [SOURCE: EGNO §4.5] ので B-1 は少なくとも fusion functor の標準定義下で立つ。より一般の tensor functor (braided 非保存等) では open。

### 3.4 Fiber の具体形

各 `C \in \mathsf{FusCat}` の fiber は

$$
\mathsf{BridgeDat}(C, A) = \{(\alpha_b, E_b, U_b, d_b) : \text{axioms}\}
$$

主な fiber の具体化:

| fiber `C` | `d_b` | 固有方程式 | SOURCE |
|:---|:---|:---|:---|
| **Vect (trivial)** | 1 | `d = 1` | abelian 可換, F5 退化 |
| **Ising (SU(2)_2)** | √2 | `d² = 2` | EGNO §8.7 |
| **Fibonacci (SU(2)_3)** | φ | `d² - d - 1 = 0` | Moore-Seiberg, Ocneanu |
| **SU(2)_4** | √3 | `d² = 3` | 標準量子群 |
| **SU(2)_k general** | `2cos(π/(k+2))` | Chebyshev | §5.bis.2 |
| **TY(Z/n)** | `√n` | `d² = n` | Tambara-Yamagami (1998) |
| **Haagerup (H_3)** | `(3 + √13)/2` ≈ 3.303 | `d² - 3d - 1 = 0` (type H_3) | Haagerup (1994) |

各 fiber が独自の `d_b` を持つが、**全 fiber の `d_b` が totally real positive algebraic integer** という ENO 普遍性制約を共有する。これが次節の要点。

---

## §4 ENO 普遍性と fibration の整合性

### 4.1 ENO 定理の fibration 的読解

[SOURCE: Etingof-Nikshych-Ostrik (2005) "On fusion categories" Annals of Math 162]:

**ENO 定理**: 任意の fusion category における任意の simple object の Frobenius-Perron 次元は totally real positive algebraic integer である。

fibration `p: \mathsf{BridgeDat} \to \mathsf{FusCat}` の観点から読むと:

**系 (試作仮説 B-2)**:  
fibration `p` の全 fiber にわたる `d_b` 値の集合は、totally real positive algebraic integer の集合に含まれる:

$$
\bigcup_{C \in \mathsf{FusCat}} \{d_b : b \in \mathsf{BridgeDat}(C, A)\} \subseteq \overline{\mathbb{Z}}_{\geq 0} \cap \mathbb{R}
$$

この共通制約が、fibration の **universal constraint** として機能する。つまり ENO 定理は「fiber ごとの具体値は違うが、値の住処 (algebraic integer ring の正実部分) は同じ」という fibration 全体の性質を保証する。

### 4.2 Cartesian section としての universal bridge datum

**仮説 (試作) B-3 (universal section)**:  
fibration `p` には **universal cartesian section** `s: \mathsf{FusCat} \to \mathsf{BridgeDat}` が存在する:

$$
s(C) = (C, b_C^{\mathrm{univ}}), \quad b_C^{\mathrm{univ}} = (\alpha, E, U, d_C)
$$

ここで:
- `\alpha, E, U` は family-independent な「標準 bridge datum 成分」(位相軸の `U(θ) = e^{iθ}`、忘却度 `\alpha \in [0, \pi]` 等)
- `d_C` は `C` に family-dependent なスペクトル成分

仮に B-3 が立てば、σ の closure schema は「fibration の cartesian section を通る一つの universal object」として閉じる。これは C5' (骨格普遍層 ≅ Stasheff tower) と並走する universal 構造の候補である。

[TAINT]: 本仮説の立つ十分条件は未検証。具体的には `d_C` が `C` の同型類のみに依存する (すなわち isomorphism-invariant) ことが必要。ENO 系の標準性質だが fibration 全体での well-definedness は追加確認が要る。

### 4.3 Cartesian lift の具体計算 (SU(2)_k → SU(2)_{k+1})

level-shift map `f: SU(2)_k \to SU(2)_{k+1}` (存在性は open、候補として) の cartesian lift を書き下す試作:

- `b' = (\alpha, E, U, d_{1/2}(k+1))` over `SU(2)_{k+1}`
- `f^* b' = (\alpha, E, U, d_{1/2}(k))` over `SU(2)_k`
- `\tilde{f}: f^* b' \to b'` は位相軸・忘却度・濾過が等しく、スペクトル軸だけ `d_{1/2}(k) \to d_{1/2}(k+1)` で書き換わる morphism

具体値:

| k | `d_{1/2}(k)` | `d_{1/2}(k+1)` | shift |
|:---|:---|:---|:---|
| 2 | √2 ≈ 1.414 | φ ≈ 1.618 | +0.204 |
| 3 | φ | √3 ≈ 1.732 | +0.114 |
| 4 | √3 | ≈ 1.802 | +0.070 |
| k→∞ | → 2 | → 2 | → 0 |

[SOURCE]: 値は §5.bis.2 + Face5Lemma_draft §5.3 で計算済。
[TAINT]: level-shift `f: SU(2)_k \to SU(2)_{k+1}` が fusion functor として well-defined かは標準参照要。存在する場合 (coset 構造経由) の具体構成は別の試作候補。

---

## §5 C2' / Stasheff tower との統合

### 5.1 C2' (BridgeDat の tower cell-wise 埋込) との関係

σ 論文 §4.7.bis.5 の C2' は、BridgeDat を Stasheff tower `\{K_n\}_{n\geq 2}` 上に cell-wise 埋め込む予想である。

本稿の fibration アプローチ (b) を C2' と統合すると:

**仮説 (試作) B-4 (fibration + tower)**:  
fibration `p: \mathsf{BridgeDat} \to \mathsf{FusCat}` は Stasheff tower に沿って階層化できる:

$$
\mathsf{BridgeDat}_n \to \mathsf{FusCat}_n, \quad (C, b)_n = (\text{$K_n$ 層に対応する成分})
$$

`BridgeDat_n` は bridge datum の `K_n` 層成分、`FusCat_n` は `K_n` 層で非自明に現れる fusion category 族 (例えば `n=4` では SU(2)_k family、`n \geq 5` では higher polytopes 対応の family)。

これは (b) と (c) の合流であり、`K_n` 層のそれぞれに fibration が立つ **tower of fibrations** 構造として整理できる。

[TAINT]: C2' / C5' 自体が予想 face のため、B-4 はさらに open。

### 5.2 位相軸 fibration vs スペクトル軸 fibration

位相軸の橋梁公理 `U_b(θ) = e^{iθ}` も fibration として書き直せる:

$$
\mathsf{BridgeDat}^{\mathrm{phase}} \to [0, \pi]
$$

ここで底は連続区間 `[0, \pi]`、fiber は特定位相 `θ` での bridge datum 成分。この fibration は連続 ODE で閉じている (σ 論文 §4.2 の閉包)。

対してスペクトル軸は:

$$
\mathsf{BridgeDat}^{\mathrm{spec}} \to \mathsf{FusCat}
$$

で、底は離散的 (fusion category 同型類の集合) である。

**仮説 (試作) B-5 (三軸の fibration 構造)**:  
σ の closure schema を担う三軸は、それぞれ異なる底を持つ fibration として統一的に読める:

- **位相軸**: 底 `[0, \pi]` の連続 fibration
- **スペクトル軸**: 底 `\mathsf{FusCat}` の離散 fibration
- **群軸**: 底 `\mathsf{Sym}` (対称群圏?) の fibration (未論)

三軸が fibration の三つの底次元として並ぶなら、C6 (三軸分離) は **底空間の直積分解** として定式化できる:

$$
\mathsf{BridgeDat}^{\mathrm{full}} \to [0, \pi] \times \mathsf{FusCat} \times \mathsf{Sym}
$$

この全域 fibration が立てば、σ の closure schema は 3 次元底空間上の universal object として閉じる。

[TAINT]: B-5 は予想 face を超える大きな跳躍。群軸 `\mathsf{Sym}` の定義が未論で、三軸直積の意味も明示されていない。

---

## §6 候補 (a) / (c) との比較

### 6.1 (a) との関係 — (b) は (a) を包含する

候補 (a) の bridge datum `d_b = (d, α_d)` は、本稿 (b) の特定 fiber で起きる現象である。

- (a): 「bridge datum に `d` 成分を加える」
- (b): 「(a) の `d` 成分の family 依存性を fibration で構造化する」

(b) は (a) を「fusion category ごとの fiber の内部構造」として回収する。fiber 単位では (a) と同じだが、fiber 間の関係性 (cartesian lift) まで記述できる点で強い。

### 6.2 (c) との関係 — (b) と (c) は合流しうる

候補 (c) は Stasheff tower 階層化である。(b) と (c) の合流は §5.1 B-4 で示した通り、**tower of fibrations** として整理できる。

- (c): 「tower 各層で bridge datum 成分を課す」
- (b): 「fusion category ごとに bridge datum の fiber を立てる」
- (b) + (c): 「tower 各層ごとに fusion category 底の fibration を立てる」

最終形は `\mathsf{BridgeDat}_n \to \mathsf{FusCat}_n` の tower 構造で、本稿の B-4 仮説がこの合流を指す。

### 6.3 三候補の優劣

| 候補 | 射程 | 形式化コスト | ENO との整合 | C2'/C5' との整合 |
|:---|:---|:---|:---|:---|
| (a) | 小 | 低 | fiber ごと手動 | 弱 |
| (b) | **中** | **中** | **自然** | 中 |
| (c) | 大 | 高 | tower 内 | **強** (親子関係) |

(b) は射程・コスト・ENO 整合の 3 軸で中庸。(a) → (b) → (c) が射程の自然な拡張路になる。

---

## §7 Kalon 判定 sketch

本試作の核仮説 B-1 (`p: \mathsf{BridgeDat} \to \mathsf{FusCat}` が Grothendieck fibration) について、Kalon 判定を試みる:

- **Step 0 既知語彙圧縮**: 「fusion category ごとに bridge datum の家族を立てて、家族間の移動を関手で結ぶ」で 1 文圧縮可能 ✓
- **Step 1 G (収束)**: Grothendieck fibration の定義で形式化。cartesian lift の普遍性で固定 ✓
- **Step 2 G∘F (安定)**: fusion functor の 3 種類 (standard / braided / modular) で展開しても fibration 構造は保持される (ただし fiber の性質は異なる) ✓ (条件付き)
- **Step 3 派生 (多様)**: 
  - (i) SU(2)_k fiber の具体的階段 (§4.3)
  - (ii) TY / Haagerup の別 fiber (§3.4 table)
  - (iii) ENO 制約の universal section (§4.2)
  3 派生すべて非自明 ✓

**判定: ◎ Kalon△ の候補 (試作段階, 暫定)**

ただし以下の open が残るため、定理 face まで押すには追加作業が要る:

- B-1 の cartesian lift の具体構成 (特に `d_b` の well-definedness)
- B-3 universal section の存在条件
- B-4 tower of fibrations との厳密な統合
- FusCat の standard definition 選択 (3.1-A / 3.1-B / 3.1-C)

現段階は **試作段階 Kalon△ ◎ sketch** とし、B-1 の厳密証明を別稿または本稿 v0.2 以降で詰める。

---

## §8 残 open と次の一手

### 8.1 本試作が解けていないもの

- ✗ B-1 厳密証明: cartesian lift の具体構成、`d_b` の well-definedness、fusion functor の FP 次元保存の明示利用
- ✗ B-3 universal section の存在条件 (`d_C` が fusion category の同型不変量であることの詳述)
- ✗ B-4 tower of fibrations の厳密定式化 (C2' / C5' の定理 face 昇格と連動)
- ✗ B-5 三軸 fibration の直積分解 (群軸 fibration の定義から)
- ✗ FusCat の定義選択 (3.1-A / 3.1-B / 3.1-C)

### 8.2 次の一手 (優先順)

1. **[直近]** B-1 の cartesian lift を SU(2)_k fiber で完全書き下し (§4.3 延長)
2. **[中期]** B-3 universal section を ENO 代数的整数性とともに証明 (C9 の fibration 版)
3. **[中期]** B-4 の tower of fibrations を Stasheff 理論の既存結果 (Markl-Shnider-Stasheff §4) と結合
4. **[中期]** FusCat の定義選択を EGNO 文献で精読して確定
5. **[遠期]** B-5 三軸 fibration の群軸成分 (A_5 / E_8 等 `Sym` 底) を別稿 `pentagon_sigma_conjecture.md` 種⑤ と連動で試作

### 8.3 親文書へのフィードバック

**σ 論文 v0.3.4 への影響**:
- §4.7.bis.7 open #20 の詳述を更新: 候補 (b) は本稿で試作段階 Kalon△ ◎ sketch まで到達
- §4.7.bis.7 内の (b) 説明に「`bridge_spectrum_axiom_draft.md` 参照」を追加 (別途 Edit 候補)

**pentagon_sigma_conjecture.md v0.4 への影響**:
- 種② (φ quantum dim) の縮小修正は本試作で追認
- 種③ (Mac Lane pentagon / F5-α) の「associahedra 骨格」が本試作の fibration 階層と合流候補
- 種⑤ (A_5 / E_8) は B-5 三軸 fibration の群軸成分として別稿連動

---

## §9 SOURCE / TAINT 台帳

### SOURCE
- [SOURCE] Grothendieck fibration の定義と pseudofunctor 同値 — SGA 1, nLab, Borceux Vol 2 §8.1
- [SOURCE] Fusion category / fusion functor の標準定義 — Etingof-Gelaki-Nikshych-Ostrik (2015) *Tensor Categories* §4
- [SOURCE] ENO 定理 (任意 fusion category で FP 次元が algebraic integer) — Etingof-Nikshych-Ostrik (2005) Annals 162
- [SOURCE] SU(2)_k 基本表現量子次元 `2cos(π/(k+2))` — 標準量子群理論, `Face5Lemma_draft.md` §5.3 計算検証済
- [SOURCE] Tambara-Yamagami カテゴリの FP 次元 `√|A|` — Tambara-Yamagami (1998)
- [SOURCE] Haagerup subfactor の固有値 — Haagerup (1994)

### TAINT / 仮説
- [TAINT/仮説] B-1: `p: \mathsf{BridgeDat} \to \mathsf{FusCat}` が Grothendieck fibration であること — 骨格は立つが cartesian lift の具体構成は本稿で完全には詰められていない
- [TAINT/仮説] B-2: ENO 定理の fibration 的読み替え — 内容は標準的だが fibration 言語への翻訳は本稿固有
- [TAINT/仮説] B-3: universal cartesian section の存在 — 条件が未詳 (同型不変性要確認)
- [TAINT/仮説] B-4: tower of fibrations (B-1 × C2') — C2' 自体が σ 論文で予想 face のためさらに open
- [TAINT/落書き] B-5: 三軸 fibration の底直積分解 — 群軸 `Sym` 未定義、大きな跳躍
- [TAINT/選択] FusCat の定義選択 (3.1-A / 3.1-B / 3.1-C) — 本稿は 3.1-A を暫定、別稿での確定要

### OPEN (σ 論文との連携)
- [OPEN, §4.7.bis.7 #20 詳述を本稿で進展]
- [OPEN, §4.7.bis.7 #15-16 C2' 延長と合流候補]
- [OPEN, §7 次稿射程候補 (v) = 本稿]

---

## 付録: 用語索引

| 用語 | 節 | 定義 |
|:---|:---|:---|
| Grothendieck fibration | §2.1 | cartesian lift を持つ関手 `p: E → B` |
| Cartesian lift | §2.1 | 底の morphism `f` の `E` 側への普遍的持ち上げ |
| Pseudofunctor | §2.2 | `B^{op} \to \mathsf{Cat}` の 2-functorial な family |
| FusCat (本稿) | §3.1 | 候補 (3.1-A/B/C) の fusion category 圏 |
| BridgeDat (本稿) | §3.2 | σ 論文 §4 の bridge datum を spectrum 成分 `d_b` で拡張した family |
| Cartesian section | §4.2 | fibration の底から全域への普遍的切断 (universal section 候補) |
| Tower of fibrations | §5.1 | Stasheff tower 各層に fibration を立てる階層構造 (B-4) |

---

*v0.1 — 2026-04-17 incubator draft。σ 論文 open #20 候補 (b) Grothendieck fibration を試作、B-1 (fibration 構造) / B-2 (ENO 読み替え) / B-3 (universal section) / B-4 (tower 統合) / B-5 (三軸分解) の 5 仮説を分離、試作段階 Kalon△ ◎ sketch。*
