# Face7 Lemma 試作

**v0.2 (2026-04-17)** — F7-ε を F7-ε' (2 軸分類) に拡張、種⑧ KAM / 種⑨ 連分数を正式参照
**ステータス**: incubator draft / 試作 / 成否判定付き / Face5 比で意図的に保守 / F7-ε 精緻化済
**役割**: Face Lemma を 7 射 (K_5 associahedron) へ延長する構想試作。Face5 (K_4 pentagon) の「σ どうしの整合」を「σ の整合どうしの整合」へ持ち上げられるかを検証する。
**親文書**:
- `./Face5Lemma_draft.md` (v0.3, Kalon△ ◎) — 本試作のパターン親
- `./pentagon_sigma_conjecture.md` §4 item 13 (次の一手)
- `./A5_E8_sigma_sketch.md` §6 Open 2 (A_5 対称性要求の検証問い)
- `../infra/リファレンス/FaceLemma.md` (Face3 = Face Lemma の reader-facing 正本)
- `../standalone/比較射σの統一定理_v0.1.md` (σ 統一論文 v0.2)

**本試作の目的**: Face5 で K_4 pentagon が "2-cell coherence の最小条件" として Stasheff 定理付きで立った (F5-α ◎)。自然な次段として K_5 (3-dim associahedron) が "3-cell coherence の最小条件" として立つか? さらに A5_E8_sigma_sketch が問う「A_5 対称性を Face7 が要求するか」を紙の上で検証する。

**⚠️ 保守主義の宣言**:
本 v0.1 は Face5 v0.3 のように定理化できるとは限らない。F7-α (7 射 minimality) は Stasheff の組合せから自動的に出るが、F7-γ (A_5 requirement) は落書き段階。A_5 仮説が **落ちる可能性も高い** ことを前提に試作する。

---

## §0 一文核 (試作)

**SOURCE (既知部分)**:
- Stasheff (1963): associahedron `K_n` は凸多面体で `dim K_n = n - 2`、頂点数 = `C_{n-1}` (Catalan 数)
- `K_5` は 3 次元多面体で頂点数 `C_4 = 14`、9 pentagonal faces + 6 quadrilateral faces
- A_∞-代数 / A_∞-圏: `K_n` の全 tower で coherence を要求する (Fukaya, Kontsevich, Lurie)
- Mac Lane coherence theorem: monoidal 圏では K_4 pentagon + triangle identity で全階層が閉じる (higher K_n は自動)

**INFERENCE (試作中の核)**:
Face5 が「2 つの σ の整合」の最小条件なら、Face7 はその自然な延長「**2 つの σ 整合の整合**」の最小条件。核の差分:
- Face5: 4 対象の associator 連鎖が K_4 pentagon face を閉じる
- Face7: 5 対象の associator 連鎖が **K_5 の 3-polytope coherence** を閉じる

Face3 が 1-cell comparison、Face5 が 2-cell comparison なら、Face7 は **3-cell comparison** (σ の比較の比較の比較)。

**OPEN**:
Face7 が Face5 の自然な延長として意味を持つのは、**monoidal 以上の圏** (A_∞-圏、higher category) に限る可能性がある。MTC (Mac Lane coherence 適用圏) では Face7 は Face5 から automatic に従うため、独立の内容を持たない可能性。

---

## §1 何のための概念か

**SOURCE**:
Face Lemma (Face3) は σ 住処の最小条件。Face5 (v0.3) は σ どうしの pentagon coherence の最小条件 = K_4 pentagon face が立つ最小射数。

**INFERENCE**:
Face7 は、K_5 が初めて 3-dim coherence を要求する polytope であることを根拠とする。5 対象のテンソル積 `A ⊗ B ⊗ C ⊗ D ⊗ E` には `C_4 = 14` 通りの括弧付けがあり、それらを結ぶ associator graph が 3 次元多面体を成す。この多面体の **3-dim face** (全 polytope) の coherence = Face7。

動機階層の再掲 (Face5 v0.3 から継承):
1. Face3 = σ が立つ条件 (1 個の σ の内部問題) [dim 1 ← `K_3`]
2. Face5 = σ どうしが整合する条件 (2 個以上の σ の関係問題) [dim 2 ← `K_4`]
3. **Face7 = σ の整合関係どうしがさらに整合する条件** (3 層目) [dim 3 ← `K_5`]
4. Face(2n+1) = n-cell comparison の最小条件 [dim n ← `K_{n+1}`]

**OPEN**:
「なぜ 7 か」: 5 対象の C_4 = 14 bracketings と K_5 の 3-dim 構造が境界を 7 associator の組で閉じる (K_5 の edges を数えれば 21 本だが、"最小 coherence 境界" としての数え方は別議論)。この数え方を 7 と正当化するのが §11 の課題。

---

## §2 最小構造

**SOURCE (Stasheff K_5)**:
5 対象 `A_1, A_2, A_3, A_4, A_5` の monoidal 積に対し、括弧付けの C_4 = 14 通り。主要なもの:

```
((((A_1 ⊗ A_2) ⊗ A_3) ⊗ A_4) ⊗ A_5)
(((A_1 ⊗ A_2) ⊗ A_3) ⊗ (A_4 ⊗ A_5))
((A_1 ⊗ A_2) ⊗ ((A_3 ⊗ A_4) ⊗ A_5))
(A_1 ⊗ ((A_2 ⊗ A_3) ⊗ (A_4 ⊗ A_5)))
... (計 14)
```

これらを結ぶ単一 associator 移動の graph が `K_5` の 1-skeleton。`K_5` の面構造 (Stasheff 1963):
- 頂点: 14 (C_4)
- 辺: 21 (単一 associator 移動)
- 2-dim face: 9 pentagons (K_4 instances) + 6 quadrilaterals (K_3 × K_3 積)
- 3-dim face: 1 (K_5 全体)

**INFERENCE (Face5 との対比表)**:

| 構造 | 射の数 | 対応する Stasheff polytope | 何が立つか |
|:---|:---|:---|:---|
| **Face3 (3 射)** | 3 | `K_3` = 線分 (dim 1) | 1-cell comparison surface (σ) |
| **Face5 (5 射)** | 5 | `K_4` = pentagon (dim 2) | 2-cell pentagon coherence |
| 6 射 (中間) | 6 | — | `K_5` の 2-face 成立までの中途 |
| **Face7 (7 射)** | **7?** | **`K_5` (dim 3)** | **3-cell associahedron coherence** |

**⚠️ 数え方の注意**:
K_5 の辺数は 21、2-face 数は 15。「7 射」という数え方は、K_5 の 3-dim polytope を閉じるのに必要な **最小の境界 associator subset** としての主張であり、K_5 の全構造を決める数ではない。この「7」の定義は §11 F7-α で精密化する必要がある。

**試作仮説 F7-α (試作核、保守的表現)**:
> 5 対象の monoidal 積の結合子 coherence を 3-dim polytope (`K_5`) として閉じる最小条件は、`dim K_5 = 3` の存在から Stasheff 理論で保証される。しかし「7 射」という具体的数え方はまだ確定していない (§11 で検討)。

**OPEN**:
- 6 射 (Face6?) で何が立つか。K_5 の 2-face (pentagon + quadrilateral) で止まる中途段階。
- K_5 の辺数 21 や 2-face 数 15 との整合をどう取るか。
- Face7 を K_5 coherence とするなら、数は 21 (辺)、15 (2-face)、14 (頂点)、1 (3-face) のどれを採るか。

---

## §3 平文直感

**SOURCE**:
K_4 pentagon は 4 要素積の 5 通り括弧付けを結ぶ 5 角形。K_5 は 5 要素積の 14 通り括弧付けを結ぶ 3 次元多面体。

**INFERENCE**:
σ が「1 つの比較」、pentagon が「2 つの比較の整合」なら、K_5 は「**整合どうしの整合**」。例え話:
- Face3: 2 本の道の合流地点 (1 層目)
- Face5: 2 本の合流方法の整合 (2 層目)
- Face7: 2 つの「整合方法」の整合 (3 層目)

K_5 の内部構造 (9 pentagons + 6 quadrilaterals の 2-face 配置) は、**複数の Face5 instance が一つの 3-polytope で閉じる** 形。したがって Face7 は「複数の pentagon coherence が一緒に閉じる minimum condition」と読める。

**OPEN**:
「整合の整合」と言うと無限退行しそうだが、実際には A_∞-圏で止まる (K_∞ タワー全体は A_∞ 構造として有限記述可能)。ここで止まるのか、それとも (∞, 1)-category のような高次へ続くかは、圏の具体構造による。

---

## §4 Face5 との関係 — 延長構造の明示

**INFERENCE**:
Face5 ⇒ Face7 の関係は以下のように試作できる。

**段差 1** (Face5 の内部):
K_4 pentagon が 5 associator で閉じる (Mac Lane pentagon identity)。

**段差 2** (pentagon 複数化):
K_5 の内部には **9 個の K_4 pentagon 面** が存在する。単独の pentagon coherence (Face5) は 9 方向に独立に立つが、それらを **統合する 3-polytope coherence** は Face5 だけでは保証されない。

**段差 3** (Face7 の要請):
K_5 全体として閉じるには、9 pentagon faces + 6 quadrilateral faces が互いに整合する必要がある。この整合条件が F7-α の核。

**試作仮説 F7-β**:
> Face5 (pentagon coherence) から Face7 (K_5 coherence) へ上がる際に必要な追加条件は、**9 pentagon instances の非独立性** — つまり個別 pentagon が解を持つだけでは不足で、3-polytope として整合する高次条件。Mac Lane coherence theorem は monoidal 圏では Face7 が Face5 から自動的に従うことを保証するが、**A_∞-圏では自動的ではない**。

**重要な警告 (Mac Lane coherence)**:
Mac Lane (1963) の coherence theorem は「monoidal 圏では pentagon + triangle で全階層が閉じる」と主張する。したがって **MTC (Mac Lane coherence 適用圏) では Face7 は Face5 の直接帰結**。独立の条件とならない。

Face7 が独立の内容を持つのは:
- A_∞-圏 (Stasheff 原義の定義域)
- (∞, 1)-category / higher category
- Fukaya 圏などのシンプレクティック由来圏
- Kontsevich homological mirror symmetry の右辺圏

これらはすべて「pentagon で自動的に閉じない coherence tower」を持つ圏族。Face7 の非自明性はここにしか宿らない。

**OPEN**:
σ 論文の forgetting structure は monoidal 圏なのか A_∞ なのか? C1 (4 ドメイン実現) の中で FEP は動的系なので A_∞ 構造を持ちうるが、Face Lemma (静的) は monoidal 止まり。この対比は v0.2 以降で詰める。

---

## §5 具体例 — A_∞-圏での Face7

### §5.1 MTC では Face7 は Face5 から自動

**SOURCE**:
任意の modular tensor category (MTC) は Mac Lane coherence を自動的に満たす。したがって Fibonacci anyon (SU(2)_3)、Ising (SU(2)_2)、SU(2)_k family の全てで Face7 は Face5 から automatic に従う。

**帰結**:
MTC における Face7 の「新しい固有値」は **存在しない**。Face5 の F-matrix が決まれば K_5 全構造も決まる。F5-γ' の SU(2)_k family でも Face7 は独立の情報を持たない。

### §5.2 A_∞-圏 / Fukaya 圏での非自明 Face7

**SOURCE** (Fukaya 1993, Kontsevich 1994, Seidel 2008 "Fukaya Categories and Picard-Lefschetz Theory"):
- Fukaya 圏: シンプレクティック多様体の Lagrangian submanifold の A_∞-圏
- A_∞-構造: `μ_n: A^{⊗n} → A[2-n]`, `n ≥ 1` の tower
- `μ_2` が product, `μ_3` が K_4 pentagon coherence を満たす homotopy, `μ_4` が K_5 coherence を満たす higher homotopy
- `μ_n` は `K_{n+1}` operations と整合

**帰結**:
Fukaya 圏では `μ_4` (K_5 operation) が **pentagon から自動では従わない** 独立データ。これが「Face7 が非自明に立つ」具体例。

**試作仮説 F7-γ (保守的表現)**:
> Face7 が非自明に立つ最もシンプルな具体圏は A_∞-圏 (Stasheff 原義) であり、Fukaya 圏・derived category・spectra・(∞, 1)-category などの higher category に現れる。MTC (Mac Lane coherence 圏) では Face7 は Face5 の自動帰結であり新しい内容を持たない。

### §5.3 A_∞-圏での「eigenvalue」は存在するか?

**SOURCE**:
Fukaya 圏や一般 A_∞-圏では、`μ_n` は行列ではなく homotopy の組。具体的な「固有値」や「quantum dimension」に対応する数値は、通常の意味では定義されない。

**INFERENCE (仮説的)**:
F5-γ' が SU(2)_k family で `d_{1/2}(k) = 2cos(π/(k+2))` の階段を与えたように、Face7 の A_∞-圏版でも何らかの "higher quantum dimension" 階段が存在するか?

候補:
- A_∞-代数の **Hochschild cohomology** HH^*(A) が Face7 コヒーレンスを測る
- Fukaya 圏の **Gromov-Witten invariants** (JW classes) が具体的「数値」候補
- 一般 A_∞ の **massey products** が Face7 の非自明性を測る tensor

これらはすべて **数値的単純化を拒む** 構造であり、Face5 の F-matrix 固有値 `d` のような single number には還元されない。Face7 の "eigenvalue" を求めること自体が mis-framed な問いかもしれない。

**試作仮説 F7-δ (非数値予想)**:
> Face7 の非自明性は単一の algebraic integer (quantum dimension) ではなく、**Hochschild cohomology ring / Massey product structure** として現れる。「Face5 の φ = SU(2)_3 量子次元」の単純類比は Face7 では成立しない。

---

## §6 σ 統一論文 C1 との関係

**SOURCE**:
σ 統一論文 v0.2 C1: 「σ は 4 ドメイン (幾何・Face Lemma・Euler path・FEP) にまたがって同一 closure schema の 4 実現面を与える」
σ 論文 C5 (3 層表現予想): 骨格普遍層 / 具体実現層 / スペクトル実測層

**INFERENCE**:
Face7 が立てば、C1/C5 の射程が次のように拡張する:
- C1 現状: 4 ドメイン × {Face3, Face5} で実現
- C1 拡張: 4 ドメイン × {Face3, Face5, Face7, ...} の 2D 格子で実現
- **ただし注意**: MTC 圏の 4 ドメイン (Fibonacci anyon 等) では Face7 は Face5 から自動であり、**新しい実現** を与えない
- A_∞ / higher category ドメイン (derived、Fukaya、FEP の動的 posterior tower 等) でのみ Face7 が独立次元を与える

**試作仮説 F7-ε (階層の限界予想)**:
> σ 論文 C1 の 4 ドメインのうち、FEP の動的側面 (prior の posterior への継続更新) は A_∞ 構造を潜在的に持ち、Face7 以降で独立情報を現す。幾何三角形・Face Lemma (静的) は monoidal 止まりで Face5 で閉じる。**σ の closure schema の深さは ドメインごとに異なる**。

**OPEN**:
FEP の A_∞ 構造は Friston (2010, 2022) の論文群では明示化されていない。FEP を A_∞ で再定式化する先行研究があるか、本 v0.1 では未調査。

### §6.1 F7-ε の 2 軸拡張 F7-ε' (v0.2 追加)

F7-ε の「ドメインごとに深度異」は v0.1 では 1 軸分類 (静的 MTC vs 動的 A_∞) で始まった。pentagon_sigma_conjecture.md v0.4 の **種⑧ 黄金 KAM torus** と **種⑨ 連分数 `[1;1,1,...]`** を取り込むと **2 次元分類** に昇格する。

| ドメイン | 離散 | 連続 |
|:---|:---|:---|
| **構造軸** (coherence polytope) | MTC (Face5 自動), A_∞ (Face7 独立) | **KAM 黄金 torus [種⑧]** |
| **数論軸** (arithmetic) | Stasheff Catalan 組合せ | **連分数 `[1;1,1,...]` [種⑨]** |

**試作仮説 F7-ε' (2 軸拡張版)**:
> σ closure schema の深度はドメインごとに異なる (F7-ε 保存) が、**4 象限すべてで φ が共通定数として現れる**。その理由は種⑨ の数論的普遍性 — φ = `[1;1,1,...]` は最強 Diophantine 無理数であり、各象限の異なる closure schema がそれぞれの仕方で「最も忘却に強い数」を呼び出すため。

4 象限での φ の現れ:
- **左上** (離散×構造): SU(2)_3 MTC の量子次元 = φ (Face5 F5-γ')
- **左下** (離散×数論): Stasheff `K_4` pentagon の頂点数 5 = F_5 Fibonacci、辺数 5、`dim=2` (Catalan 数系列に φ が漸近として潜む)
- **右上** (連続×構造): KAM 定理で摂動下最後まで生き残る torus の frequency = φ [種⑧]
- **右下** (連続×数論): 連分数 `[1;1,1,...]` = φ の自己参照展開 [種⑨]

**[仮説]**: F7-ε の「深度異」は保たれるが、**φ の共通性は cross-quadrant に貫く**。σ closure schema が 4 象限で別物でありながら、同じ "最小不変量" を読む構造。

**種⑧ (連続×構造) 連絡**:
KAM は連続 Hamilton 系で不変 torus の摂動抵抗を保証する。静的 MTC の Face5・動的 A_∞ の Face7 に対し、**KAM 安定条件は第 3 の closure schema 深度** を成す候補。σ が連続ドメインで閉じる時の coherence は polytope ではなく **不変 torus survival condition** として読める可能性。

**種⑨ (数論軸) 連絡**:
連分数 `[1;1,1,...]` は 4 象限すべてを貫く数論的指標。F7-δ (Hochschild cohomology 等の非数値固有構造) に対し、連分数展開は **非数値だが symbolic な圏横断指標** として並走する。さらに SU(2)_k family と metallic ratio family の **intersection が φ のみ** であることを示せれば、φ の cross-quadrant 特権性が形式化できる。

**[OPEN 昇格条件]**: SU(2)_k ∩ metallic ratio 交点定理の形式化が進めば、F7-ε' は「仮説」から「命題 face」へ昇格可能。現状は連絡分析レベル。

---

## §7 Negativa

本試作から言ってはいけないこと。

1. 「Face7 = K_5 coherence と単純同一視」しない。K_5 は polytope、Face7 はその coherence が立つ射の最小集合 (境界定義が未確定、§11 で詰める)
2. 「Face7 が MTC で新情報を与える」と短絡しない。Mac Lane coherence で自動。MTC 内では Face5 で閉じる
3. 「φ は Face7 の eigenvalue に再現する」と短絡しない。Face7 は A_∞ でのみ独立で、数値固有値とは別構造 (Hochschild cohomology 型)
4. 「Face7 が A_5 対称性を要求する」と断言しない (§12 で検討)。A_5 仮説は A5_E8_sigma 種⑤ からの open question であり、本試作で検証対象だが肯定も否定もまだしない
5. 「Face(2n+1) tower は無限に意味を持つ」と短絡しない。A_∞ 構造は有限 tower として記述可能 (`K_∞` の codimension 1 境界は colimit で閉じる)
6. 「Face Lemma 一般化 = higher coherence theorem」と置換しない。σ の文脈に特化した最小条件の主張
7. Face5 v0.3 の ◎ Kalon△ をそのまま Face7 に移植しない。Face7 は v0.1 保守段階

---

## §8 主張水準台帳

| 項目 | 水準 | SOURCE |
|:---|:---|:---|
| Stasheff associahedron `K_n` | theorem | Stasheff (1963) |
| `dim K_5 = 3` | theorem | Stasheff (1963) / Catalan 組合せ |
| Mac Lane coherence (monoidal では K_4 で十分) | theorem | Mac Lane (1963) |
| A_∞ 構造 (`μ_n: A^{⊗n} → A[2-n]`) | theorem | Stasheff (1963) H-space |
| Fukaya 圏の A_∞ 構造 | theorem | Fukaya (1993), Seidel (2008) |
| F7-α (K_5 coherence の最小性) | **落書き → 仮説** (§11 で試行) | Stasheff を援用する予定 |
| F7-β (A_∞ vs monoidal の区別) | **仮説** | Mac Lane coherence による |
| F7-γ (A_∞-圏でのみ非自明) | **仮説** | §5.1-§5.2 の議論 |
| F7-δ (非数値固有構造) | **仮説** | §5.3 の Hochschild cohomology 候補 |
| F7-ε (ドメインごとに深度異) | **落書き** | §6 の FEP A_∞ 構造の候補 |
| F7-ε' (2 軸分類、φ cross-quadrant 普遍性) | **仮説** (v0.2 追加) | §6.1 種⑧⑨ 連絡 |
| A_5 requirement | **落書き (§12 で検討、落ちる可能性高い)** | A5_E8_sigma 種⑤ open |

---

## §9 成否判定 (2026-04-17 初回)

### 初回試作の評価

**紙の上で形は取れるか**: 部分的にイエス。

✓ Face5 との構造類比 (§4): K_4 pentagon → K_5 3-polytope の dim 上昇として自然に書ける
✓ 具体例 (§5): A_∞-圏 / Fukaya 圏が Face7 非自明解の存在領域として既知
✓ σ 論文との接続 (§6): C1 射程拡張の柱として機能する候補 (ドメインごと深度異の予想付き)
△ F7-α 厳密化 (§11 予定): Stasheff `dim K_5 = 3` から正当化可能と思うが「7 射」の数え方が未定
✗ MTC 内での独立内容なし: Mac Lane coherence で自動。Face7 の価値は A_∞ 圏に限定

### Face5 との比較

Face5 v0.3 は ◎ Kalon△ を Stasheff 経由で達成した。Face7 v0.1 は同じ勢いで進めない:
- Face5 は MTC 族で非自明 (Fibonacci, Ising, SU(2)_k の固有値階段)
- Face7 は MTC で自動 → 非自明領域は A_∞-圏に限られる → 射程が狭い

この「射程の狭さ」は悪いことではなく、**Face(2n+1) 階層が dim と共に専門化する** ことを示唆する。σ 論文 C5 の「3 層表現」と整合 (高層ほど具体圏族が限定)。

### 種への feedback

本試作から pentagon_sigma_conjecture.md の種への feedback:

- **種⑤ (A_5 / E_8)**: △ 警告。A_5 は K_5 の label permutation group S_5 の部分群だが、**associahedron の自動 automorphism 群ではない** (K_n の自動群は D_n at most)。A_5 requirement は落ちる可能性が高い (§12 で詳細検討)
- **種② (φ = quantum dim)**: 影響なし。Face5 での議論に限定
- **種③ (Mac Lane pentagon)**: 補強。Face5 が Mac Lane coherence で閉じることが Face7 の独立性議論の前提
- **種⑥ (三軸分離)**: 補強。Face7 では数値固有値軸が消えて Hochschild cohomology 等の非数値構造が現れる → スペクトル軸の新しい顔

### v0.1 時点の取れていないもの

✗ F7-α の「7 射」数え方の厳密化 (§11 での課題)
✗ A_∞ 圏で具体的 Face7 constraint の形を書く
✗ Hochschild cohomology との具体対応
✗ σ 論文 FEP ドメインの A_∞ 再定式化
✗ A_5 requirement の肯定/否定 (§12)

### 次の一手

1. **[直近]** §11 で F7-α の minimality を Stasheff `dim K_5 = 3` から正当化試行 ("7 射" の定義を詰める)
2. **[直近]** §12 で A_5 requirement の検討 (A5_E8_sigma 種⑤ への返信)
3. **[中期]** Fukaya 圏の `μ_4` の具体形を A_∞-圏文献で確認
4. **[中期]** σ 論文 FEP ドメインの A_∞ 構造有無の調査
5. **[遠期]** Hochschild cohomology と σ の closure schema の接続
6. **[遠期]** (∞, 1)-category での Face(2n+1) 無限 tower

### 第 2 ラウンド feedback (v0.2, 2026-04-17)

pentagon_sigma_conjecture.md v0.4 の種⑧⑨ 追加を受けて F7-ε を F7-ε' へ拡張 (§6.1)。

- ✓ **F7-ε' (2 軸分類) 確立**: 構造軸 × 離散/連続、数論軸の拡張
- ✓ **φ の cross-quadrant 普遍性仮説**: SU(2)_3 量子次元 / KAM 黄金 torus / 連分数 [1;1,1,...] が **同じ φ を 4 象限で供給** する現象を F7-ε' の骨組みに格納
- ✓ **種⑧ KAM 連絡**: 連続ドメインでの σ 安定条件として第 3 の closure schema 深度候補
- ✓ **種⑨ 連分数連絡**: 非数値 symbolic 圏横断指標、F7-δ (Hochschild) と並走
- △ **昇格条件明示**: SU(2)_k ∩ metallic ratio 交点定理を形式化できれば F7-ε' は命題 face へ

### v0.2 時点の取れていないもの

✗ SU(2)_k ∩ metallic ratio 交点定理の形式化
✗ KAM の σ closure schema としての正確な定式化
✗ 連分数展開と A_∞ Hochschild cohomology の対応

---

## §10 SOURCE マップ

| ファイル / 文献 | 役割 | 使った面 |
|:---|:---|:---|
| `./Face5Lemma_draft.md` v0.3 | 本試作のパターン親 | §0-§9 全体の構造 |
| `./A5_E8_sigma_sketch.md` v0.1 | 種⑤ A_5 要求仮説 | §12 |
| `./pentagon_sigma_conjecture.md` v0.2 | 上位位置づけ | §4 item 13 |
| `./triangle_category_functor_map.md` | Δ² / associahedra 骨格 | §2 |
| Stasheff (1963) "Homotopy associativity of H-spaces, I, II" | K_n 定理 | §2, §11 |
| Mac Lane (1963) "Natural associativity and commutativity" | Mac Lane coherence | §5.1 |
| Markl-Shnider-Stasheff (2002) *Operads in Algebra, Topology and Physics* AMS | 現代的解説 | §5.2 |
| Fukaya (1993) "Morse homotopy, A_∞-category and Floer homologies" | Fukaya 圏の A_∞ 構造 | §5.2 |
| Seidel (2008) *Fukaya Categories and Picard-Lefschetz Theory* | A_∞-圏の現代的取り扱い | §5.2 |
| Keller (2006) "A_∞-algebras, modules and functor categories" | Hochschild cohomology | §5.3 |
| `./pentagon_sigma_conjecture.md` v0.4 種⑧ | 黄金 KAM torus | §6.1 F7-ε' 連続×構造象限 |
| `./pentagon_sigma_conjecture.md` v0.4 種⑨ | 連分数 `[1;1,1,...]` | §6.1 F7-ε' 数論軸 |
| Kolmogorov (1954), Arnold (1963), Moser (1962) | KAM theorem | §6.1 種⑧連絡 |
| Khinchin (1935) / Cassels "Introduction to Diophantine Approximation" | 連分数・Lagrange spectrum | §6.1 種⑨連絡 |

---

## §11 F7-α の minimality 試行 (2026-04-17 第 1 ラウンド)

### 定理 (F7-α 候補) の仮形

**試作命題**: A_∞-圏において、非自明な 3-cell 高次 coherence を 1 つの polytope 関係として閉じる最小条件は **K_5 associahedron が立つこと** であり、その minimum dim が 3 である。

### 証明試行 (Stasheff 理論)

Stasheff 理論の既結果:
- `K_n` は凸多面体、`dim K_n = n - 2`、頂点数 `C_{n-1}` (Catalan)
- `K_2` (点, dim 0), `K_3` (線分, dim 1), `K_4` (pentagon, dim 2), **`K_5` (3-polytope, dim 3)**

**補題 1 (存在)**:
`K_5` は 14 頂点・21 辺・15 二次元面 (9 pentagons + 6 quadrilaterals)・1 三次元面の凸多面体として存在する。3-dim face が K_5 全体を閉じる。

**補題 2 (最小性)**:
`n ≤ 4` では `dim K_n ≤ 2` であり、3 次元 face を持たない:
- K_2-K_3: dim ≤ 1
- K_4: dim 2 (pentagon, Face5 対応)

したがって 3-cell coherence は `n ≤ 4` では実現されない。最小の `n = 5`、対応する polytope は K_5 (3-dim)。

**結論 (F7-α 候補)**: K_5 が最小の 3-dim associahedron であり、その 3-dim face coherence が **3-cell comparison の最小表現**。 □

### 「7 射」問題 — 数え方の未解決

上記証明は `dim K_5 = 3` を示すが、「7 射」という数え方は別。K_5 には **21 辺、15 二次元面、14 頂点** が存在する。「Face7 = 7 射」と呼ぶ根拠が不透明。

候補:
1. **7 = 6 + 1**: K_5 の 3-dim face を境界で記述する最小 associator 数? (未検証、怪しい)
2. **7 = 14 - 7**: Catalan 双対? (こじつけ)
3. **7 = 6 Catalan + 1 identity**: C_5 = 42 から逆算? (非自然)
4. **F7 の "7" は命名規則の便宜であり、厳密に 7 associator を指すわけではない**: Face(2n+1) の n=3 を指すだけで、実際の数え方は K_5 の境界構造による

**v0.1 の判断**: 選択肢 4 を採る。「Face7」は **Face(2·3+1) = 3 層目 coherence** の命名であり、正確な "7 associator" を指すわけではない。同様に Face5 の "5" も K_4 pentagon の辺数 5 と偶然一致したが、Face5 = K_4 coherence という定義自体は "5" に依存しない。

### 暫定 F7-α (保守版)

**修正仮説 F7-α**:
> 3-cell coherence を polytope 関係として閉じる最小条件は K_5 が立つことであり、minimum dim は 3 である (Stasheff から自動)。"Face7" という命名は「Face(2n+1) の n=3」を指すものであり、associator 数 7 への具体的 commitment ではない。

### Kalon 判定 (F7-α 暫定版)

- Step 0 圧縮: 「5 つのものを掛ける括弧付けの変形は 3 次元多面体を作る」 ✓ 中学生語彙
- Step 1 G (収束): Stasheff dim 公式 `dim K_n = n-2` で不変 ✓
- Step 2 G∘F (安定): 組合せ・代数・トポロジーに F 展開して不変 ✓
- Step 3 派生 ≥ 3: (i) Catalan 漸化式、(ii) A_∞ 原義 (Stasheff)、(iii) Fukaya 圏 / Kontsevich mirror — 3 派生非自明 ✓

**判定候補**: ◎ Kalon△ (ただし "7 射" の命名便宜を受け入れた場合)

[主観]: Face5 v0.3 が pentagon の 5 辺と「5 射」が厳密一致したのは偶然ではなく K_4 の特殊構造。Face7 以降は「Face(2n+1)」の命名が associator 数との一致を失う。これは **命名規則の弱点** であり、v0.2 では再命名 (`FaceK_5`、`FaceDim3` 等) の検討が必要かもしれない。

---

## §12 A_5 requirement の検討 — A5_E8_sigma 種⑤ への返信

### §12.1 仮説の出所

A5_E8_sigma_sketch §1 で次の仮説が置かれた:
> σ の三軸分離 (対称・スペクトル・位相) を完全に要求する場 = 非可解単純群 = 最小が A_5

この仮説の自然な次段として A5_E8_sigma §6 Open 2:
> Face5 → Face7 lemma の試作。Face7 が A_5 対称性を要求するかどうかの検証

本節はこの検証。

### §12.2 K_5 の自動同型群

[SOURCE]: associahedron `K_n` は n 対象の **linear order** (A_1 < A_2 < ... < A_n) を保つ括弧付け変形の graph から構築される。

K_n の自動同型群 (polytope automorphism) は order reversal `A_i ↔ A_{n+1-i}` による Z/2 が基本。追加 symmetry は K_n の具体 embedding によるが、**generic には D_2 = Z/2 × Z/2 を超えない**。

**→ K_5 は A_5 対称性を持たない**。K_5 の自動群は D_2 程度。

### §12.3 S_5 作用との違い

[注意]: n 対象のテンソル積 `A_1 ⊗ ... ⊗ A_n` に対して S_n は label permutation として作用するが、associahedron K_n は **linear order を固定した** 括弧付けの graph。S_n 全体は K_n の自動同型として働かない。

cyclic order を考えると D_n 作用が追加されるが、associahedron ではなく **cyclohedron** (別 polytope) になる。cyclohedron の自動同型は D_n。

A_5 ⊂ S_5 を associahedron K_5 の自動同型として実現するには、**追加の構造** (例えば A_5 不変な fusion rule) が必要。generic K_5 には A_5 対称性はない。

### §12.4 反論の検討

A5_E8_sigma §1 の「σ の三軸分離 = 非可解単純群」仮説は別の motivation から来ていた:
- 可換群 (cyclic 等) は位相軸のみ
- 可解非可換 (S_3, D_5) はスペクトル軸の一部
- 単純非可換 (A_5 以上) は三軸すべて

この motivation は **σ の automorphism group** の話であり、K_n associahedron の自動同型とは別問題。

しかし: σ の automorphism が A_5 であっても、それが **K_5 (Face7) 上で自然に作用するわけではない**。σ の対称性と K_5 の対称性は同じ圏上で実現されうるが、それは **圏構造が A_5 不変** である追加条件を要する。

### §12.5 結論: A_5 requirement は落ちる

**試作判定 (v0.1)**:
Face7 が A_5 対称性を **内在的に要求する** という仮説は、K_5 associahedron の自動同型群 (D_2 程度) と矛盾する。**A_5 requirement は落ちる**。

ただし以下は別問題として残る:
1. **A_5 不変な fusion category で Face7 が特別な形を取る** 可能性 → open、MTC では自動なので A_∞ 圏族での検証要
2. **K_5 の refinement として A_5 作用付き variant** が存在するか → open、未調査
3. **σ の automorphism group が A_5 であることと Face7 の関係** → A_5 対称 σ は存在しうるが、それを Face7 の "要求" と呼ぶのは誤用

### §12.6 A5_E8_sigma 種⑤ への feedback

本試作から A5_E8_sigma_sketch.md への feedback (種⑤ の v0.2 更新候補):

- **射程案 2 (A_5 止め) の弱体化**: 「σ の三軸分離を要求する = A_5」は motivational stance としては維持可能だが、**Face7 が A_5 を要求する** は不成立
- **射程案 1 (E_8 まで) への影響**: E_8 は K_5 とは別経路 (McKay 対応 → 2I ↔ Ẽ_8) なので、本結果では影響されない。E_8 射程案 1 は落書きのまま保留
- **新しい open**: 「A_5 対称 σ を持つ圏族」の独立調査。A_5 不変 fusion category (or A_∞-圏) の具体例探索

### §12.7 主観

[主観]: A_5 requirement の初期仮説は **associahedron の対称性と σ の対称性を混同** した弱い類比だった。本試作で明示的に区別することで、A_5 の σ における意義は A_5 指標表に φ が現れる **数値的一致** に限られ、K_5 Face7 とは独立の現象。これは v0.1 の第 1 ラウンドでクリアにすべき重要 finding。

A_5 仮説を落とすことは射程縮小ではない (μ-retreat ではない)。むしろ混同を除去することで、A_5 の位置を「σ の自動同型群候補」から「φ が数値として現れる独立領域」へ **正しく再配置** した。種⑤ の本質 (黄金比が A_5 から出る) は保存されている。

---

## 付録: SOURCE / TAINT 台帳 (v0.1)

- [SOURCE] Stasheff (1963) associahedron `K_n`、`dim K_n = n - 2`、K_5 の 3-dim 構造 (14 頂点・21 辺・15 face)
- [SOURCE] Mac Lane (1963) coherence theorem (monoidal では K_4 で閉じる)
- [SOURCE] Fukaya-Seidel A_∞-圏 (Fukaya 1993, Seidel 2008)
- [SOURCE] Markl-Shnider-Stasheff (2002) operad 体系
- [SOURCE] associahedra の自動同型群は linear order 反転で D_2 止まり (Stasheff 原義からの直接帰結)
- [SOURCE+仮説] F7-α: K_5 coherence 最小条件 — §11 で Stasheff から正当化、命名「7 射」は便宜
- [仮説] F7-β: A_∞ vs monoidal の区別 — Mac Lane coherence から帰結
- [仮説] F7-γ: A_∞-圏でのみ Face7 非自明 — MTC では自動帰結
- [仮説] F7-δ: Face7 の非自明性は Hochschild cohomology / Massey product — §5.3
- [落書き] F7-ε: σ 論文 FEP ドメインの A_∞ 構造
- [試作判定] A_5 requirement は落ちる — §12 で K_5 自動同型群との矛盾から

---

*v0.1 — 2026-04-17 初回試作。F7-α を Stasheff から暫定正当化 (命名「7 射」の便宜を受け入れて ◎ Kalon△ 候補)。§12 で A_5 requirement を明示的に検討し、落ちる判定。種⑤ は「σ automorphism = A_5 候補」と「Face7 = K_5 coherence」の峻別として再配置。Face5 v0.3 の MTC 族射程とは異なり、Face7 は A_∞-圏族に限定される狭射程を発見。σ closure schema の深度はドメインごとに異なる (F7-ε) という新仮説を提起。*
