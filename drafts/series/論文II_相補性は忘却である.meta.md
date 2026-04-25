# 論文II 相補性は忘却である — メタデータ

**v0.14 (2026-04-17)**
**対応する本稿**: `drafts/series/論文II_相補性は忘却である_草稿.md` v1.13 → v1.16
**本文書の役割**: Creator と Claude の共同作業の台帳。読者には見せない。論文の知的旅程と F⊣G 固定と Kalon/Gauntlet 判定履歴を追跡する装置。

---

## §M1 F⊣G 宣言 (論文開始時に固定、途中変更禁止)

**固定日**: 2026-04-11

### F (左随伴 = 発散 = Explore)

**具体化**: 文体ガイド §3 メタファー三連 (2-simplex 発散)

**Paper II における特殊性**:
- Face Lemma (§3.4) は 2-simplex (3 射 composable triple) を CPS 構造の最小非自明条件とする
- 2-simplex の 3 頂点は「3 つの独立射」であり、これは文体ガイド §3 の「メタファー三連」構造と圏論的に一致する
- F の具体的運用: CPS スパン (U_A, U_B) に第 3 の射 h を加えて Δ² 発散を実行

**選択理由**:
1. Face Lemma の核主張は「3 射未満では照合面が立たない」(formal には $B_1^{\mathrm{ver}}=0$、最小検証支持複体では dim Ξ = 2 が閾値)。これは F の選択に規定される
2. 2-simplex は Paper II 全域の統一言語 (§2.5 の各インスタンスは 3 射を具体化する)
3. 文体ガイド §3 との整合: メタファー三連 = 2-simplex の発散形式

### G (右随伴 = 収束 = Exploit)

**具体化**: 文体ガイド §4 数式裏付け + normalized chain complex 上の照合面 `B_1^{\mathrm{ver}}` による最小性 + 混合分配則 (mixed distributive law) による CPS スパンの閉性

**Paper II における特殊性**:
- G の役割は「発散した 3 射が composable triple として閉じるか」を検証する
- 数式裏付けは具体的には: Face Lemma (§3.4) の証明 / Stability Simplex Theorem (§3.5) / Blanket 生成定理 (§3.7.2) の 3 本柱
- 層化 (§3.3) の α(θ) ∈ Fiber(Δd) を G の収束対象として位置づけ

**選択理由**:
1. Paper II の構造的厳密性は「3 射が照合面を立てるか」で決まる ($B_1^{\mathrm{ver}} \neq 0$)
2. mixed distributive law λ: DT ⇒ TD は FTC の本質であり (§1.1), CPS の全インスタンスで共通する収束機構
3. 文体ガイド §4 との整合: 数式裏付け = Face Lemma / Stability Simplex / Blanket 生成の形式証明

### F⊣G の運用サイクル

1. **F 適用** (発散): CPS スパンの 2 射 (U_A, U_B) に第 3 射 h を加え、2-simplex 発散を実行
2. **G 適用** (収束): h が composable triple として閉じるか (混合分配則の存在) を数式で検証
3. **G∘F 1 回転**: 発散と収束の整合性が Face Lemma を満たすか → 満たせば Fix 近傍
4. **不動点到達条件**: C1-C3 のすべてが Face Lemma の下で合成的に安定

### 2026-04-14 amendment: negativa freeze + H^2 canonicalization

Coherence Defect Lemma の canonical surface を `H^2` 側へ移すにあたり、以下を **Face Lemma 本体の F⊣G 不変** を保ったまま次段補題限定で拡張する:

- **F 拡張**: 2-simplex 発散に加えて、`cochain complex -> H^2 / curvature / TQFT` へ伸びる cohomology expansion を含める。具体的には、局所 forgetting law が大域的 1-cochain に貼り合わさらないときに生じる 2-cocycle class を問う
- **G 拡張**: §3.4.5-§3.4.6 の整合制約と non-globalizability 判定を担う。主表示は cochain 側の $H^2_{\Theta}$。chain 側の `C2b/H_2^{\mathrm{coh}}` は幾何学的な先駆面として履歴保持する
- **不変条件**: Face Lemma (§3.4) 本体は $\mathrm{im}\,\partial_2 = B_1^{\mathrm{ver}}$ の定理のまま。拡張は §3.4.6 の conjectural surface に限る。計算ノート `Face補題_ホモロジー厳密化.md` §1 の H_1 却下論理は chain degree 1-2 の話であり、`H^2` 方向の大域持ち上げ障害を直接には禁じない

この拡張は「F⊣G の変更」ではなく「F⊣G の射程を次段まで延長する独立な amendment」として扱う。

---

## §M2 核主張リスト (L3 対象)

### C1: CPS スパンによる相補性の統一 [§1.1, §2.1-§2.2, §3.1]

> すべての Type I 相補性 (A or B) は、同じ情報 C_D からの 2 つの非対称 忘却関手 U_A, U_B の投影として統一され、その非対称性の強度 α は ∀ Type I ドメインにおいて cell 次元差 Δd ≥ 1 と対応する (α > 1 ⟺ Δd ≥ 1)。

**射程**: ∀ Type I 圏 (DRB, Hilb, Lor, FEP 圏, DRB_embed 等)
**形式化段階**: §2.1 (CPS スパン定義), §2.2 (公理), §3.1 (CPS 双対性定理)
**検証状態**: FTC と QM では完全, GR と心身は worked analogy, 電荷は Type II 退化例

### C2: Face Lemma による非自明性の最小条件 [§3.4]

> CPS スパンが非自明な構造を持つための必要十分条件は、関連する圏の nerve 上で照合面が立つことである (formal には $\forall X$ について $\dim \Xi(X)=2 \iff B_1^{\mathrm{ver}}(X)\neq 0 \iff \exists$ composable $(f,g,h): g\circ f = h$)。

**射程**: ∀ CPS 圏 X
**形式化段階**: 定理 3.4.1 (最小性・等価条件・飽和) — 完全証明済み (normalized chain complex + 照合面 `B_1^{\mathrm{ver}}`; Segal/Grothendieck との整合付き)
**検証状態**: 完全厳密。FTC (d, P, id+C), QM (x̂, p̂, [x̂, p̂]=iℏ), GR (∂/∂x^μ, g_{μν}, Γ) の各具体例で検証
**補助線**: Face Lemma は Hamming 的な最小検査面、LDPC 的な face 貼り合わせの局所核として読める。stable / detectable / coherence-defective / recoverable の区別および recoverability 側の定理候補と撤退条件は `drafts/infra/FaceLemma_技術設計.md`、今回の基礎づけ差替えは `calculations/Face補題_ホモロジー厳密化.md`

### C2b (archived geometric precursor): Coherence Defect Lemma — 非可埋な相補性残差 [history only]

> Face Lemma の次段補題として、閉じた比較面の殻が 3-cell の境界として埋まらない class が存在するとき、その残差は $H_2^{\mathrm{coh}}(X) \neq 0$ として測られる。これは相補性の局所整合が大域整合へ持ち上がらないこと、すなわち structural non-fillability を表す。

**扱い**: 幾何学的直感として参照可だが canonical ではない。本文・infra・今後の gauntlet では `H^2_{\Theta}` を主表示とする。

**射程**: Face Lemma が成立する領域 ($B_1^{\mathrm{ver}} \neq 0$) のうち、3-cut star complex が定義される対象
**形式化段階**: 履歴保持のみ。chain-first 版は `v1.14 / v0.3` で一度実装済み
**検証状態**: 幾何学的 shadow としては有用だが、現時点では canonical surface ではない
**negativa**:
1. Face Lemma 自体を holes の定理へ置き換えない
2. cocycle representative と homology/cohomology class を混同しない
3. `H_2^{\mathrm{coh}} = 0` から recoverability を直結しない

**位置づけ**: C2b は C4 の幾何学的先駆面であり、canonical surface ではない。必要なら UCT bridge で後から回収する。

### C3: Blanket 生成定理による FEP 包含 [§3.7.1-§3.7.3]

> Fritz の Markov category における conditional independence factorization は CPS の Face Lemma からの帰結であり (blanket 存在 ⟺ $B_1^{\mathrm{ver}} \neq 0$、直感的には照合面が立つこと、同値に最小検証支持複体 $\dim \Xi = 2$)、自由エネルギー原理 (FEP) のすべての変分原理は CPS 忘却場方程式の α > 0 セクターで回復される (FEP ⊂ CPS|_{α > 0, B_1^{\mathrm{ver}} \neq 0})。

**射程**: ∀ FEP 変分系 (α > 0 セクター)
**形式化段階**: 補題 3.7.1 (互換性), 定理 3.7.2 (Blanket 生成), 定理 3.7.3 (FEP 包含)
**検証状態**: 形式的完成。数値検証 N=1000 で機械精度一致 (§3.7.3)
**前提**: (P1) Φ := D_KL, (P2) 指数型分布族, (P3) α > 0

### C4 (canonical, cochain side, conjectural): Coherence Defect Lemma — Θ の大域持ち上げ障害

> Face Lemma の次段補題 (cochain-first 版)。§3.5 Stability Simplex Theorem の Θ: $\mathrm{Hom}(\mathcal{C}) \to \mathbb{R}$ は局所的に 1-cocycle 条件 $\Theta(g \circ f) = \Theta(g) + \Theta(f)$ を満たす。だがこの局所 1-cocycle 条件が大域的な 1-cochain の coboundary に持ち上がらない 2-cocycle ω が存在する場合、その class $[\omega] \in H^2(\Theta) \neq 0$ は構造的に修復不可能な忘却の代数的測度を与える。

**主張水準** (2026-04-17 時点):
- **partial theorem (QM verified)**: QM CPS instance での $H^2_\Theta(x) \neq 0$ を Bargmann (1954) / Mackey (1958) 援用で本文 §3.4.6.1 にて明示証明。$\hbar$ は $H^2$ generator の係数として同定
- **conjectural (一般 CPS 圏)**: 任意の CPS 圏での $\omega_\Theta$ の canonical 構成は依然 open
- **canonical surface の位置**: Codex 系列の selector / lift / weak-package / counterexample / guard-probe surface (下記検証状態参照) は conjectural な body を支える scaffolding として保持。partial theorem は QM 既知結果援用 branch、canonical theorem branch は別に進行
- **Kalon 判定** (2026-04-17): ◎ Kalon△ (§M3 参照)
- **±3σ 出口ゲート** (2026-04-17): 通過 (§M4 参照)

**射程 (canonical)**: Θ が局所 1-cocycle law として組織される CPS ドメイン
**射程 (未検証)**: 最小非自明インスタンスとしての QM / FTC / その他具体例

**形式化段階**: §3.4.6 本文草稿まで実装済み。主定義は $Z^2_{\Theta}=\ker d^2$, $B^2_{\Theta}=\mathrm{im}\,d^1$, $H^2_{\Theta}=Z^2_{\Theta}/B^2_{\Theta}$。2026-04-23 に missing intermediate object を `整合担体 (coherence carrier)` と命名し、support-local な carrier 面を infra 正本 `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/C4_整合担体.md` へ分離した
**検証状態**: 一般形は未証明。現在は両極の probe・selector 条件面・その CPS 内在化条件・weak-package test・counterexample surface・guard-probe surface が揃っており、これらを束ねる missing intermediate object は **整合担体** として固定された。`calculations/計算_QM_H2Theta最小インスタンス.md` では `V = \mathbb{R}^2` 上の交代双線形 2-cocycle $\omega(u,v)=\tfrac12(xp' - px')$ が `d^2\omega=0` かつ `\omega \notin \mathrm{im}\,d^1` を満たすことを固定し、QM を nontrivial candidate とした。`calculations/計算_FTC_H2Theta対照例.md` では可縮な区間上の FTC 最小模型で forgetting law `Θ` が global potential 由来の exact 1-cochain となり、obstruction class `[ω_{\Theta}]` が立たないことを固定した。`calculations/計算_H2Theta_selector条件面.md` では `global potential / contractible patching` と `alternating witness / central extension` を selector の十分条件の二極として分離した。`calculations/計算_H2Theta_selector_CPS内在化条件.md` ではこれらを `CPS-globalization atlas + zero holonomy` および `CPS-obstruction witness + irreducible orientation` へ翻訳した。`calculations/計算_H2Theta_selector_package弱化テスト.md` では full package を `support-local re-lift + generator-face zero holonomy` と `support-local faithful witness + anti/symmetric separation` まで削った。`calculations/計算_H2Theta_selector_weakpackage反例探索.md` では `Weak Lift A' / B'` の false trivialization / false obstruction を分け、guard 付き版 `A'' / B''` の必要性を固定した。2026-04-23 時点では、`A'' / B''` は整合担体の両極実現、`貼合側 / 残差側` はその front-stage pair として読む。したがって C4 は少なくとも **selector surface / lift surface / weak-package surface / counterexample surface / guard-probe surface + coherence carrier** を持つ canonical conjecture になった。ただしこれはなお Paper II canonical surface の probe 水準であり、本文主張を partial theorem へ昇格させるものではない

**位置づけ**: C4 が canonical surface。C2b は geometric precursor / history として下位保持する。必要なら UCT bridge (C5 未起草) で両者を再接続する。

**negativa**:
1. `H^2_{\Theta} \neq 0` の一般非自明性を、すべての CPS 圏について主張しない
2. 1-cocycle 条件の大域持ち上げが自明な圏では C4 は空でありうる
3. $H^2_{\Theta} = 0$ から recoverability を直結しない
4. cocycle representative ($\omega_{\Theta}$ 自体) と class ($[\omega_{\Theta}]$) を混同しない
5. $H^2$ torsion の意識接続は本文に上げない

---

## §M3 Kalon 判定履歴

| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| — | C1-C3 | — | (Phase 4 完了後に kalon-check rule を適用予定) |
| 2026-04-17 | C4 (Coherence Defect Lemma, QM verified) | **◎ Kalon△** | Step 0 圧縮テスト: 既知語彙 1 文圧縮可 (「位置と運動量を別々に覚えても両方まとまった覚え方は絶対にできない。この『まとまらなさ』の大きさがプランク定数」)。Step 1 G(x)=x: §3.4.6.1 formal proof で書き下しても論理構造不変。Step 2 G∘F(x)=x: メタファー三連 (埋まらない殻/非可換性/中心拡大) 展開後も収束不変。Step 3 非自明派生 ≥4: (1) FTC 境界条件 Stokes 障害 (2) Paper XII/XIV 速度/曲率との $H^2$ generator 接続 (3) FEP 包含 C3 との関係 (C4 が blanket 生成を厳密化) (4) 意識 $H^2$ torsion 読み (grounding 薄いが structural)。F⊣G 事前固定 ✓ (§M1 2026-04-14 remark の次段拡張範囲内)。Kalon△ 明示 (Kalon▽ 偽装禁止) |

---

## §M4 ±3σ ゲート履歴

| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| — | C1-C3 | — | — | (Phase 4 完了後に入口/出口検査を実施予定) |
| 2026-04-14 | C4 入口 (Gauntlet Round 1 前) | ±3σ | — | μ = 「Face Lemma は detectability 完全理論」から距離を取り、「Face Lemma は detectability 飽和だが recoverability は $H^2$ で測る」という次段主張は μ 外 ±3σ |
| 2026-04-17 | C4 出口 (QM verified 後) | ±3σ | **±3σ 維持 (上昇方向)** | Gauntlet Round 1-3 全て射程維持 ✓ + QM Heisenberg instance で具体物 $\hbar$ が $H^2$ generator 係数として証拠化。推測から partial theorem への昇格は σ 上昇方向であり、縮小ゼロ。出口ゲート通過 |

---

## §M5 Refutation Gauntlet ログ

### 反論の出典

GPT-5.4 外部監査 (2026-04-11) による Paper II v1.11 の 10 軸判定。判定は以下:

| 軸 | 項目 | 判定 | 評点 |
|:---:|:---|:---:|:---:|
| 1 | 核命題の厳密性 | marginal | 3/5 |
| 2 | 一般性の本当の範囲 | fail | 2/5 |
| 3 | 新規性の位置の明確さ | marginal | 3/5 |
| 4 | 反証可能性 | marginal | 2/5 |
| 5 | 橋の健全性 | fail | 2/5 |
| 6 | 用語の節度 | fail | 2/5 |
| 7 | 数値再現性 | fail | 1/5 |
| 8 | 哲学的射程の統制 | fail | 1/5 |
| 9 | 記号・公理・型の規律 | marginal | 3/5 |
| 10 | 構成の経済性 | fail | 1/5 |

総合判定: "核は立つが大幅削減必要 / core CPS paper と speculative extension に分割推奨 / Publishable only after major revision"

### Round 1 展開

#### C1 — 2026-04-11 Round 1 (軸 1: 核命題の厳密性)

**反論 r**: CPS スパンは定義対象であり、定義自体の厳密性は争点ではない。ただし「すべての Type I 相補性が CPS である」という存在量化の主張の厳密性が疑問 — どの対象が CPS でないことを示したか?

**SFBT 問い**: できないのではなく、やっていないだけではないか?

**試行**:
1. §7.1.2 (Layer 1 構成不能例) を強化: 共変/反変対立、非 faithful 定値関手は CPS 不成立の具体例として明示
2. Layer 1 5 条件の最小性補題を追加: 「どの条件を除くと CPS 典型でない対立が含まれるか」を §2.1 remark に記載
3. 反論を「すべての二項対立が CPS ではない」と再起し、具体的反例を §7.1.2 で提示、5 条件を必要十分に強化

**結果**: 射程維持 ✓

---

#### C1 — 2026-04-11 Round 1 (軸 2: 一般性の本当の範囲)

**反論 r**: GR と心身のインスタンスは FTC/QM のように厳格に形式化されていない。単に「原理的対応のみ」を提示している。

**SFBT 問い**: 本当に形式化できないのか、本論文で行わないのか?

**試行**:
1. §2.5.3 GR のインスタンスを Paper XIII (時空は忘却である) への参照に置換 (削除 + pointer)
2. §2.5.4 心身を FTC 短縮版で代替し、Face Lemma 抽象の詳細は Paper VIII (圏論基礎) §6.3 有限主体定理への参照に
3. 本論文 scope を明示: {FTC, QM は完全証明, GR/心身は formal skeleton のみ, 全体統一は Paper XIII/VIII}

**結果**: 射程限定 (明示) ✓ — 射程を正直に限定することで主張強度が回復。削除ではなく参照で維持

---

#### C2 — 2026-04-11 Round 1 (軸 3: 新規性の位置の明確さ)

**反論 r**: Face Lemma は nerve の 2-coskeletal 性 (Segal 1974 既知) に基づく。CPS への新規適用か、単なる再解釈か?

**SFBT 問い**: 再解釈ならば新規性は「CPS 文脈での意味」にのみあるか?

**試行**:
1. §3.4 節題を変更: 「Face Lemma: CPS が非自明であるための最小構造」→ 新規性を明示
2. Segal の 2-coskeletal は純粋な nerve 性質だが、CPS の Face Lemma は**忘却スペクトラム Ξ の方向測定可能性**を連結する — これが新規
3. 定理 3.4.1 (c) 飽和: 「4 射以上は冗長である」は CPS では**創発の不在**を意味 (§6.1)。これは既存 nerve 結果にない物理/哲学的解釈

**結果**: 射程維持 ✓ (概念的新規性の強調)

---

#### C2 — 2026-04-11 Round 1 (軸 4: 反証可能性)

**反論 r**: CPS3 を公理 → 定理に格下げしたのは正しいが、残る独立公理 CPS0', CPS1, CPS2, CPS5 が真に最小か未検証。どの公理を除くと CPS が崩壊するか?

**SFBT 問い**: 公理の独立性検証が不十分ではないか?

**試行**:
1. §2.2 公理節に注釈追加:
   - CPS0' (容器-内容非対称): ないと対称性のみ残り Type II になり Δd 分類不可
   - CPS1 (同源射影): ないと独立な 2 圏となり CPS の「同じ原点」の意味が失われる
   - CPS2 (架橋): ないと U_A, U_B が切断された別構造
   - CPS5 (マスク): ないと相補性自体が弱まる
2. 「4 公理のどの部分集合も CPS の特性を失う」を例示として簡潔に提示

**結果**: 射程維持 ✓

---

#### C2 — 2026-04-14 Round 2 (軸 1: theoremic 基礎の再固定)

**反論 r**: 2026-03-27 patch は Kan 仮定を除去したが、なお `dim Ξ = St(x) の最高非退化 simplex 次元` に依存している。これは循環ではないにせよ、`(S2) 2-simplex の存在` を別名で言っているだけで、Face Lemma の心臓がまだ motivated definition に近い。

**SFBT 問い**: `H_1` や Betti 数へ逃げずに、Face Lemma が本当に必要としている量を直接つかめていないだけではないか?

**試行**:
1. `Ξ` を `normalized simplicial chain complex` 上の **照合支持複体** として再定義し、主役を `B_1^{ver}(x)=\mathrm{im}\,\partial_2` に移す
2. 3射の最小性を「非退化 2-simplex の境界 $\partial_2\sigma=[g]-[g\circ f]+[f]$ が初めて照合面を立てる」という事実で証明
3. 飽和を Segal/Grothendieck の 2-coskeletal 性ではなく、`B_1^{ver}` が次数 2 の境界作用素から生成されるという **chain degree** の事実で処理
4. Segal/Grothendieck は削除せず、主証明の土台から「整合性の裏書き」へ位置づけ変更

**結果**: 射程維持 ✓ — Face Lemma は「三角形の見た目」ではなく「照合面が立つか」を主役にすることで theoremic な基礎を回復。Blanket / FEP / 意識診断への依存鎖も definition ではなく boundary-level theorem として読み直せる

---

#### C2 — 2026-04-11 Round 1 (軸 5: 橋の健全性)

**反論 r**: §3.3 層化定理: α(θ) の整数部分 = Δd は証明がなく「動機付けられた構成」としか書かれていない。本当に対応か、仮定か?

**SFBT 問い**: 証明のために追加前提が必要ではないか?

**試行**:
1. §3.3.1 直後に remark 挿入: 「整数部分対応 α(θ_∞) = Δd は、本論文では**定義**として採用する (Amari-Nagaoka 2000 の統計多様体では非厳密)。厳密な関手証明は Paper III で実施される」
2. 「定義」として明示することで主張水準を誠実に下げ、「定義の動機」として説明し、Paper III に形式化を委譲
3. これにより橋渡しの問題は「定理」ではなく「定義の適切性」に移動 (Paper III の責任)

**結果**: 射程維持 ✓ (前提強化 = 正直化による射程保持)

---

#### C3 — 2026-04-11 Round 1 (軸 6: 用語の節度)

**反論 r**: §3.7 で Markov category の factorization を CPS の composable triple と「同値」と述べているが、Fritz の factorization はより一般的。CPS の条件はより具体的。

**SFBT 問い**: 包含方向のみを示したのであり、同値を主張する論拠が弱くないか?

**試行**:
1. §3.7.1 互換性補題を「⟹ 方向のみ」に限定: 「CPS 圏で composable triple が存在 ⟹ Fritz の条件付き独立性 factorization が成立」
2. 逆方向 (⟸) は「FEP 包含定理 (定理 3.7.3) で検証された観察」として再表記
3. 「同値」宣言を削除し、「観察的一致」に降格

**結果**: 射程維持 ✓ (用語の正確化)

---

#### C1-C3 — 2026-04-11 Round 1 (軸 7: 数値再現性)

**反論 r**: §5.2 LLM α-層検証は N=500, r=0.17 (小効果)。§5.3 SWE-bench も同様。本論文の核主張 (FEP 包含, Face Lemma) と無関係。なぜ含めたか?

**SFBT 問い**: 検証されていない主張を削除する代わりに、より関連する検証を追加できないか?

**試行**:
1. §5.2, §5.3, §3.7.4 の数値節を全削除
2. §5.1 (CPS 自己適用) 直後に 1 文 pointer のみ:
   > "α-層化の計算的再現性は Paper IV (効果量減衰定理) の枠組みで検証される。Paper IV は観測上界 r ≤ √ρ_spec/√(K+1) を予測しており、LLM 隠れ状態層別検証 (pilot, N=500, r ≈ 0.17) はこの上界と整合する。本稿ではこれ以上立ち入らない。"
3. §3.7.4 の数値検証 (EFE 4 定式化, N=1000, 機械精度) は核主張 (C3 FEP 包含) と直接連携するため圧縮して維持

**結果**: 射程維持 ✓ (経済性回復 + 布石 pointer)

---

#### C2 — 2026-04-11 Round 1 (軸 8: 哲学的射程の統制)

**反論 r**: §6.2 ハードプロブレム「Δd ≥ 2 は離散遷移を含む」は、ハードプロブレムの「説明」なのか「再述」なのか? Chalmers の問題を解決していない。

**SFBT 問い**: 哲学的貢献を過大評価していないか?

**試行**:
1. §6.2 節題を変更: 「意識のハードプロブレム: 心身関係の CPS 診断」
2. 節冒頭に明記: 「本節は Chalmers (1995) のハードプロブレムを**解決しない**。その構造的原因を CPS と Face Lemma の観点から**診断**する」
3. 「情報的起源」を「情報的構造的特性」に緩和
4. Paper VIII §6.3 有限主体定理への参照を追加

**結果**: 射程維持 ✓ (後退の一部 — 「解決」→「診断」)

---

#### C1-C3 — 2026-04-11 Round 1 (軸 9: 記号・公理・型の規律)

**反論 r**: v1.0 → v1.11 の間に Δd の定義が「セル個数」から「微分階数差」に変更された。なぜ変わったか? 既存の定理は依然有効か?

**SFBT 問い**: 定義変更に伴う再検証が必要ではないか?

**試行**:
1. §2.1 (または §2.3 節題直後) に remark 明示: 「**v1.11 での定義変更**: Δd は「微分構造の最高階数の絶対値差」として定義される。例: 関数値 (0 階) vs 微分 (1 階) → Δd=1」
2. 各インスタンス (FTC, QM, GR, 心身) の Δd 計算を「微分階数」言語で再通一
3. 既存定理は「Δd ≥ 1 ⟺ α > 1」を基礎にしており、定義変更後も正当 (検証済み)

**結果**: 射程維持 ✓ (記号規律の明確化)

---

#### C3 — 2026-04-11 Round 1 (軸 10: 構成の経済性)

**反論 r**: §3.7.4 EFE 4 定式化 (Champion et al. 2022) 統合でページ数が 2 倍以上に増えた。核主張 (C3 FEP 包含) との関係は? 必要か?

**SFBT 問い**: 副次的統合を削除し、核主張に集中できないか?

**試行**:
1. §3.7.4 全体を 1.5 頁相当に縮小
2. 命題 3.7.4a (RSA ↔ ROA) のみ維持。命題 3.7.4b-f は "Champion et al. (2022) §X 参照" の 1 行ずつに置換
3. 理由: EFE 4 定式化の統合は形式的厳密性を高めるが、Paper II の核心は「Blanket 生成定理 (3.7.2) + FEP 包含定理 (3.7.3)」。Champion 統合は Phase 5 (形式化完成) に委ねる

**結果**: 射程維持 ✓ (経済性回復)

---

### Round 1 総合評価

| 軸 | 射程維持 | 対応概要 | 最終状態 |
|:---:|:---:|:---|:---|
| 1 | ✓ | §7.1.2 強化 + 5 条件最小性 | 射程維持 |
| 2 | ✓ | GR は Paper XIII 参照, 心身は Paper VIII 参照 | 射程限定 (明示) |
| 3 | ✓ | Face Lemma の CPS 文脈新規性強調 | 射程維持 |
| 4 | ✓ | 4 公理の最小性明示 | 射程維持 |
| 5 | ✓ | §3.3 を「定義」に降格, Paper III 参照 | 射程維持 (前提強化) |
| 6 | ✓ | ⟹ 方向のみ, 「同値」削除 | 射程維持 (正確化) |
| 7 | ✓ | 数値節削除, Paper IV pointer | 射程維持 (経済性) |
| 8 | ✓ | 「解決」→「診断」, Paper VIII 参照 | 射程維持 (後退一部) |
| 9 | ✓ | Δd 定義変更を §2.1 で明示 | 射程維持 |
| 10 | ✓ | §3.7.4 縮小, 5 命題を参照化 | 射程維持 (経済性) |

**結論**: **10 軸すべてで Round 1 射程維持達成 ✓**

Round 2/3 の発動は不要。すべての軸で前提強化および表現正確化により射程維持が可能。後退は軸 8 (哲学) の「解決 → 診断」のみ。この後退は過大評価の訂正であり、Yugaku 核宣言 (身の丈を理想に引き上げる) と整合する。

---

### 2026-04-14 implementation amendment (negativa freeze + H^2 canonicalization)

2026-04-14 の実装時点で canonical surface を `C2b/H_2^{\mathrm{coh}}` から `C4/H^2_{\Theta}` へ移す。C2b は幾何学的先駆面として履歴保持し、論文本文・infra 正本・今後の gauntlet では次を negativa として固定する:

1. Face Lemma 自体を holes の定理へ置き換えない
2. `H^2_{\Theta} \neq 0` の一般非自明性を、本稿ではまだ主張しない
3. cocycle representative と class を混同しない
4. `H^2_{\Theta} = 0` から recoverability を直結しない
5. `H^2` torsion の意識接続を本文へ入れない

### C4 — 2026-04-14 Round 1-3 (cochain-first exploration)

C4 は新規核主張であり、Round 1 で射程維持できても 2/3 を明示的に走らせる (新主張は Round 3 非発動でも Solution-Focus 適用仮説を書かない)。

#### C4 Round 1 (内部強化)

**反論 r**: 計算ノート `Face補題_ホモロジー厳密化.md` §1 は精読レポートの「$\dim \Xi = \mathrm{rank}\, H_1$ 案」を明示的に却下している (L17-21: 「埋まった三角形は $H_1$ を生むのではなく、むしろ 1-cycle を境界として埋める側だ。Face Lemma が欲しいのは『穴』ではなく『検査面』である」)。この論理は H² にも及び、Face Lemma をホモロジー/コホモロジー語彙で拡張する道そのものを封じるのではないか?

**SFBT 問い**: できないのではなく、やっていないだけではないか? 計算ノートの却下論理の射程を精密に分析していないだけではないか?

**試行 (内部強化)**:
1. 計算ノート §1 却下論理の射程を chain degree で限定: 却下は $H_1 = \ker \partial_1 / \mathrm{im}\,\partial_2$ に関する話。∂_2 の像 (B_1 = $\mathrm{im}\,\partial_2$) を Face Lemma に使うのは正。H_1 (∂_2 の像に入らない 1-cycle) を Face Lemma に使うのは誤
2. 本主張 C4 は $H^2 = \ker d^2 / \mathrm{im}\,d^1$ を扱う。これは (a) cohomology 側、(b) degree 1→2 on cochain、(c) d¹ の cokernel 方向。計算ノート却下論理の射程外
3. C4 は Face Lemma を拡張しない。Face Lemma (im ∂_2 の定理) の **隣に新規補題として置く** 形で階層分離 (§M1 2026-04-14 remark の不変条件)

**結果**: 射程維持 ✓ (計算ノート却下論理との chain degree + 方向の二重差分で射程が重ならないことを明示)

---

#### C4 Round 2 (外部強化)

**反論 r**: Round 1 で chain degree 差は示せても、「なぜ H² を Paper II に持ち込む必要があるか」の論拠が薄い。外から来た異物ではないか?

**SFBT 問い**: Round 1 とは別角度から前提強化できないか? Paper II 既存構造との接続を精密化せよ

**試行 (外部強化)**:
1. §3.5 Stability Simplex Theorem の定理 (V1) 条件 $\Theta(g \circ f) = \Theta(g) + \Theta(f)$ は **忘却量 Θ が 1-cocycle であること** を意味する (d¹Θ = 0, ここで $(d^1 \Theta)(f, g) := \Theta(g) - \Theta(g \circ f) + \Theta(f)$)
2. §3.4.4 Face Lemma の $\partial_2 \sigma = [g] - [g \circ f] + [f]$ は dual に d¹ と同じ構造を持つ。Θ を 2-simplex に評価した値が $(d^1 \Theta)(\sigma)$ に対応
3. したがって Paper II は **既に cochain complex 側の構造を使っている** (§3.5 が実質 1-cocycle 条件)。C4 は Paper II の既存構造を次段 (2-cochain level) に延長するだけであり、外部輸入ではなく内発拡張
4. 論文 XIV (曲率は忘却の繰り上がりである) が同じ方向で既に独立に進行中 (§M8 Phase 5 blocker 2 件目)。C4 はこの接続点でもある

**結果**: 射程維持 ✓ (§3.5 Θ が既に 1-cocycle 構造を使っている事実により、C4 は外部輸入ではなく内発拡張として正当化)

---

#### C4 Round 3 (Solution-Focus: フレーム反転による取り込み)

**反論 r**: Round 1-2 で射程は示せたが、Face Lemma の「飽和」主張 (§3.4.4 (c): 「$\dim \Xi > 2$ は起こらない。高次 simplex は 2-face を通じてのみ寄与」) との関係はどうか? 3-cell を導入することは飽和主張の精神に反するのではないか?

**SFBT 問い**: 反論を主張の強化材料に反転できないか? 飽和主張を弱めるのではなく、飽和主張の射程を精密化することで Face Lemma の刃を**強化**できないか?

**試行 (フレーム反転)**:
1. §3.4.4 (c) 飽和は「$B_1^{\mathrm{ver}} = \mathrm{im}\,\partial_2$ への寄与について飽和」と読む。これは正しい。高次 simplex は照合面の**生成**に寄与しない
2. だが (c) 現行 wording 「構造的に新しい照合情報を生まない」は、照合情報の外側 (H² = recoverability の障害物) についての言及を含まない — scope の曖昧さ
3. 取り込み戦略: (c) を「detectability については飽和。recoverability については別定理 (C4) で扱う」と精密化する方向で Face Lemma の刃を**強化**。同じ論理構造は計算ノート §4 の Segal/Grothendieck 降格 (「主証明の土台から整合性の裏書きへ」) と同型 — 既存命題の射程を正しく限定することで全体の論理を強化する
4. 結果として Face Lemma は「照合面生成の最小条件 + 飽和」という 2 重定理に精密化され、C4 は「照合面が立った後の修復不可能性の測度」という独立定理として並置される

**結果**: 射程維持 ✓ (フレーム反転) + Face Lemma 刃の強化という追加効果

---

### C4 Round 1-3 総合評価

| Round | 強化方向 | 射程判定 | 主要効果 |
|:---:|:---|:---:|:---|
| 1 | 内部 (chain degree 差) | ✓ | 計算ノート却下論理との衝突回避 |
| 2 | 外部 (§3.5 Θ との接続) | ✓ | 内発拡張としての正当化 |
| 3 | フレーム反転 (飽和精密化) | ✓ | Face Lemma 刃の強化 |

**結論**: **C4 Round 1-3 全て射程維持達成 ✓**

±3σ 判定: C4 は既存分布の中心 (Face Lemma = 照合面の完全理論) から離れ、「Face Lemma は detectability 飽和だが recoverability は別定理」という μ 外の主張に到達。射程縮小なし、前提強化のみで σ を保持。**±3σ 入口ゲート通過**。

後続: §3.4.6 本文草稿 + §3.4.4 (c) 精密化のリライト + 符号理論対応.md への detectable/coherence-defective/recoverable 三分法追加 (Codex 提案) が次の作業単位。

### Round 3 非発動の記録

Round 1 で射程維持達成したため Round 3 (Solution-Focus) は非発動。ただし非発動も記録する。

**Solution-Focus 適用仮説**: もし Round 3 が発動していれば、以下の反論吸収戦略を取る予定だった:

- 軸 2 (一般性): GR/心身 の「未検証」を「シリーズ分業の現れ」として反転。Paper XIII/VIII が引き受けることで、Paper II の核は FTC/QM に集中できる = 論証の時間軸配置の成熟度の証拠
- 軸 7 (数値): 数値節の削除を「方向転換の勇気」として反転。弱い数値で強い理論を補強するより、強い理論を強い数値 (Paper IV 上界テスト) で守る方が Kalon に近い
- 軸 10 (経済性): §3.7.4 縮小を「核主張への集中」として反転。Champion 統合は Paper II の核ではなく Phase 5 の装飾だったと明示

これらは Round 1 で射程維持が達成できなければ発動していた吸収戦略。記録することで Round 3 の構造的役割 (フレーム反転) を失わない。

---

## §M6 虚→実変換面

### C1
- 野望: [§M2 C1 の核主張を 1 文で言い直す]
- 現在まだ虚な点: [未証明・未観測・未形式化・未反駁処理の核]
- 実へ引くための SOURCE: [読むべき原典 / 必要データ / 必要定理]
- 実化の判定条件: [何が揃えば『実へ近づいた』と言えるか]
- 次の実化操作: [Sourcing / 定義追加 / 証明 / 実験 / 反論吸収]
- 最新状態: 変換中

### C2
- 野望: [§M2 C2 の核主張を 1 文で言い直す]
- 現在まだ虚な点: [未証明・未観測・未形式化・未反駁処理の核]
- 実へ引くための SOURCE: [読むべき原典 / 必要データ / 必要定理]
- 実化の判定条件: [何が揃えば『実へ近づいた』と言えるか]
- 次の実化操作: [Sourcing / 定義追加 / 証明 / 実験 / 反論吸収]
- 最新状態: 変換中

### C2b
- 野望: [§M2 C2b の核主張を 1 文で言い直す]
- 現在まだ虚な点: [未証明・未観測・未形式化・未反駁処理の核]
- 実へ引くための SOURCE: [読むべき原典 / 必要データ / 必要定理]
- 実化の判定条件: [何が揃えば『実へ近づいた』と言えるか]
- 次の実化操作: [Sourcing / 定義追加 / 証明 / 実験 / 反論吸収]
- 最新状態: 変換中

### C3
- 野望: [§M2 C3 の核主張を 1 文で言い直す]
- 現在まだ虚な点: [未証明・未観測・未形式化・未反駁処理の核]
- 実へ引くための SOURCE: [読むべき原典 / 必要データ / 必要定理]
- 実化の判定条件: [何が揃えば『実へ近づいた』と言えるか]
- 次の実化操作: [Sourcing / 定義追加 / 証明 / 実験 / 反論吸収]
- 最新状態: 変換中

### C4
- 野望: [§M2 C4 の核主張を 1 文で言い直す]
- 現在まだ虚な点: [未証明・未観測・未形式化・未反駁処理の核]
- 実へ引くための SOURCE: [読むべき原典 / 必要データ / 必要定理]
- 実化の判定条件: [何が揃えば『実へ近づいた』と言えるか]
- 次の実化操作: [Sourcing / 定義追加 / 証明 / 実験 / 反論吸収]
- 最新状態: 変換中

## §M7 棄却された代替案 (±3σ 併記義務の記録)

### 棄却 1: 宇宙論を Paper II から standalone 退避

2026-04-11 セッション中、v2 計画段階で「宇宙論は standalone essay として分離」を推奨した。Tolmetes が再定位: 宇宙論は系列内に配置すべき。理由:
- 宇宙論は FEP/LLM/意識と**質的に異なる**
- Verlinde 2011 と Jacobson 1995 は既に forgetful 構造を物理の根幹に置いている
- 系列内配置で忘却論は「認知が物理の構文を借りる」ではなく「物理が忘却の文法で書かれている」と主張できる
- 射程が ±2-3σ から ±4-5σ に跳ね上がる
- **Paper XIII 新設** (時空は忘却である) が正解

**棄却理由**: standalone は μ への静かな後退だった。射程を保つために系列内配置が必要。

### 棄却 2: Paper XIII を Verlinde/Jacobson からゼロ書き起こし

2026-04-11 セッション中、「Paper XIII を新規に書き起こす」を推奨したが、既存の `drafts/incubator/legacy/力とは忘却である_v2.md` (4065 行) が既に宇宙論を抱えていることが判明。N-01 違反。

**棄却理由**: 既存資産を未確認のまま新規執筆を推奨するのは怠慢。v2 から抽出 + 再構成が正しい経路 (C を見据えた B)。

### 棄却 3: Paper I v0.14 → v1.0 narrow 化

2026-04-11 セッション中、Paper I を narrow scope で v1.0 に昇格する計画を立てたが、Paper I は既に v1.6 まで進行しており v0.14 状態は git に存在しなかった。モノグラフ構成設計 §4 の「Paper I v1.0 化残タスク」記述は stale。

**棄却理由**: 計画文書も TAINT になりうる。実体を読まずに計画を進めるのは N-01 違反。Paper I は v1.6 の現状で受け入れる (Tolmetes 判断 (d))。

---

## §M8 次 Phase への引き継ぎ

### Phase 4 の残り (meta.md 確定後に実施)

1. **シリーズ前置宣言草稿** (`drafts/infra/シリーズ前置宣言_Paper_II_v1.md`) — Paper II の系列位置・境界・布石宣言
2. **Paper II 本文削減** (`drafts/series/論文II_相補性は忘却である_草稿.md` v1.11 → v1.12):
   - §2.5.3 GR → Paper XIII §2 参照に置換
   - §2.5.4 心身 → FTC 短縮版 + Paper VIII §6.3 参照
   - §5.2, §5.3, §5.4 LLM/SWE-bench 数値節 → 削除 + Paper IV pointer
   - §3.7.4 EFE 統一 → 命題 3.7.4a のみ維持, b-f を Champion 2022 参照に
   - §7.2 重力 → Paper XIII 参照 (1-2 文)
   - §7.3 Yang-Mills → [予想] 降格 (1 文)
   - 推定削減: 1967 → ~1450 行 (26% 減)

### Phase 5 (blocker 並行攻略)

- **Paper II 側**: α 層化 (§3.3) を Markov category 構造から induce する経路 A を 1 日試行
- **Paper II 側 (C4 canonical)**: Coherence Defect Lemma の最小非自明インスタンス検証 (1 日)。QM を第一候補とし、局所 1-cocycle law から $H^2_{\Theta} \neq 0$ を与える最小例を構成できるかを試す
  - 2026-04-14 進捗: `calculations/計算_QM_H2Theta最小インスタンス.md` を追加。`V=\mathbb{R}^2` 上の標準シンプレクティック 2-cocycleを probe として固定
  - 2026-04-15 進捗: `calculations/計算_FTC_H2Theta対照例.md` を追加。FTC の最小 local model では forgetting law `Θ` が global potential 由来であり、`[ω_{\Theta}] = 0` となる contrast probe を固定
  - 2026-04-15 進捗: `calculations/計算_H2Theta_selector条件面.md` を追加。`global potential / contractible patching` と `alternating witness / central extension` を十分条件の二極として整理
  - 2026-04-15 進捗: `calculations/計算_H2Theta_selector_CPS内在化条件.md` を追加。`contractible presentation` と `additive witness` を `CPS-globalization atlas` / `CPS-obstruction witness` の package 条件へ翻訳
  - 2026-04-15 進捗: `calculations/計算_H2Theta_selector_package弱化テスト.md` を追加。full package を `support-locality` と `generator-face sufficiency` の方向へ弱化
  - 未了: QM / FTC pair と selector/lift/weak-package 条件面を Paper II 本文へ補注として上げるか、meta+calculations に留めるかの判断
  - 未了: weak package に反例がないかを探索し、弱化が過剰でないことを確かめる
- **Paper XIII 側**: Face Lemma ↔ 曲率 dictionary を Verlinde 2011 / Jacobson 1995 を素材に形式化試行。C4 ($H^2_{\Theta}$) との接続点あり (論文 XIV「曲率は忘却の繰り上がりである」経由)
- 両 blocker の試行結果に応じて Paper II 核定式化と Paper XIII v0.1 を相互調整

### Phase 6 (C 完成と解体)

- v2 (`incubator/力とは忘却である_v2.md`) の残余 (Bucket I 部分) の処理決定: archive 退避 or incubator 保持
- オンボーディング §2.1 公開シリーズ表を更新 (Paper XIII 追加)
- モノグラフ構成設計 §4 残タスクの整理
- 解体マップ v2 を v1.6 認識に更新

### Donor 統合メモ (外部パッチ統合)

- **ポパー適用不能 (negative knowledge)**: `drafts/infra/ポパー適用不能_証明梯子.md` が Gauntlet 軸 4 (反証可能性) に対する構造的 negative knowledge を提供。Popper の反証主義が「同一性述語の有意味性は保存構造全体から事後的に成立する」型の主張に対して原理的に適用不能であることを proof-ladder 形式で論証。Gauntlet Round 1 軸 4 (§M5 C2 Round 1) では公理独立性によって応答しているが、本 infra 文書はより深い層で「反証可能性という問い自体の射程限界」を示す。未吸収 (本文・Gauntlet への統合は不要と判断: 現行応答で射程維持 ✓ であるため)。必要が生じた際の参照先として記録。

- **QM H²_Θ 最小インスタンス (proof status)**: `calculations/計算_QM_H2Theta最小インスタンス.md` が C4 の第一候補として QM Heisenberg 中心拡大 (symplectic 2-cocycle ω(x̂,p̂) = ½ℏ) から H²(Θ_QM) ≠ 0 を構成。probe 水準であり H²_Θ の一般非自明性・selector theorem は未主張。v0.6 で統合済み。calculations 棚卸しでは「本文昇格なし・meta 参照完了」と判定。v0.12 で `B'' guard probe` を追記。QM 最小模型では `coboundary-conservative / boundary-closed / refinement-stable` が自然に通ることを固定した。

- **FTC H²_Θ 対照例 (contrast probe)**: `calculations/計算_FTC_H2Theta対照例.md` (277 lines) が C4 の trivial side を固定。可縮な区間 I=[a,b] 上の FTC 最小模型で Θ=d⁰Λ (global potential 由来の exact 1-cochain) となり [ω_Θ]=0 を構成。QM = obstructed candidate / FTC = non-obstructed contrast の pair が揃う。§7 negativa 5 項 (一般化禁止・周期多様体除外・recoverability 非同一視・Drift と class 混同禁止・本文昇格未主張) を自己宣言。probe / contrast 水準。v0.12 で `A'' guard probe` を追記。FTC local model では `gauge-stable / support-saturated / triple-overlap-consistent` が自然に通ることを固定した。

- **H²_Θ selector 条件面 (theorem candidate surface)**: `calculations/計算_H2Theta_selector条件面.md` (257 lines) が C4 の selector を FTC/QM pair から定理候補へ持ち上げる条件面を構築。十分条件の二極を定義: Candidate A (globalizable side: contractible presentation + global potential → [ω_Θ]=0) / Candidate B (obstructed side: alternating witness + coboundary が対称のみ → [ω_Θ]≠0)。必要十分条件は未主張。§6 で 4 つの blocker を列挙 (CPS への lift 未定義 / additive reduction functor 未記述 / 中間型未分類 / 必要条件未検証)。theorem ではなく theorem candidate surface。

- **H²_Θ selector CPS 内在化条件 (lift surface)**: `calculations/計算_H2Theta_selector_CPS内在化条件.md` が C4 の selector を CPS 公理語へ翻訳する lift surface を構築。外部語 `contractible patching` → `CPS-globalization atlas + zero holonomy`、外部語 `alternating witness` → `CPS-obstruction witness + irreducible orientation` へ対応付けた。Candidate Lift A (atlas + zero holonomy → `[ω_Θ]=0`) / Candidate Lift B (obstruction witness + irreducible orientation → `[ω_Θ]≠0`) を theorem candidate として固定。FTC / QM は外部例ではなく CPS 内部語での lift witness として再配置された。negativa: 必要条件未主張・site/topology 未定義・additive witness の任意 C4 対象への存在仮定なし・本文 §3.4.6 昇格未実施。v0.9 で統合済み。

- **H²_Θ selector package 弱化テスト (weak-package surface)**: `calculations/計算_H2Theta_selector_package弱化テスト.md` が lift surface の full package を `support-locality + generator-face sufficiency + witness-relative visibility` の 3 原則に沿って削った。trivial side: Weak Lift A' (`support-local re-lift + generator-face zero holonomy → [ω_Θ]=0`)、nontrivial side: Weak Lift B' (`support-local faithful witness + anti/symmetric separation → [ω_Θ]≠0`) を theorem candidate surface として固定。FTC/QM がより弱いこの形でも自然に通るという見通しを得た。negativa: A'/B' 必要条件未主張・反例探索先行判断・本文補注未侵入。v0.10 で統合済み。

- **H²_Θ selector weak-package 反例探索 (counterexample + guard-probe surface)**: `calculations/計算_H2Theta_selector_weakpackage反例探索.md` が Weak Lift A' / B' の failure mode を分離した。A' 側: generator hole failure / overlap deficiency failure / support instability failure の 3 穴を確認。B' 側: witness artifact failure / boundary leakage failure / anti/symmetric projection failure の 3 穴を確認。最小 guard を抽出し guarded 版を定義: `Weak Lift A''` = support-saturated + triple-overlap-consistent + gauge-stable; `Weak Lift B''` = coboundary-conservative + boundary-closed + refinement-stable。さらに FTC/QM に guard probe を追加し、FTC では `A''`、QM では `B''` が local/minimal model 上で自然に通ることを確認した。negativa: failure mode 網羅性未主張・A''/B'' 必要十分未主張・guard 各語の一般定義を本文へ上げない。v0.11–v0.12 で統合済み。

---

### 著者決定パッケージ (C4 次 blocker)

C4 の calculations 面は現在 **6 層** (probe + selector + lift + weak-package + counterexample + guard-probe) に到達した。次にエージェントが単独で進められる計算層はない。以下を著者の判断対象として保留する。

**決定 1 (主): 整合担体を本文語へ出すか**
- 選択肢 α: `§3.4.6` に 1-2 行の補注として `整合担体` だけを入れ、`A'' / B''` は backstage に残す
- 選択肢 β: infra + meta に留め、本文は "C4 は conjectural surface" の記述のみ維持する (現状維持)
- 選択肢 γ: `整合担体` を補助 note / 統一記号表へ登録してから本文へ入れる
- エージェント推奨: **β 優先** (現時点では carrier の命名は済んだが、本文侵入は依然として theorem 水準を押し上げない範囲に留めるべき)

**決定 2 (副): UCT bridge (C5) 起草を始めるか**
- C2b (chain/homology) と C4 (cochain/cohomology) の接続点が依然として未起草
- 先行条件: C4 がある程度 theorem 化されてから着手が自然

**決定 3 (副): 符号理論対応.md への三分法追加**
- Codex 提案 (§M5 C4 Round 3 後続): detectable / coherence-defective / recoverable の三分法を `符号理論対応.md` に追加するかどうか
- エージェント判断: §3.4.4(c) 精密化と同時に著者が決めるべき

## 改訂履歴

- v0.1 (2026-04-11): 初版。Phase 4 §4.2 成果物。F⊣G 固定 + C1-C3 核主張確定 + Gauntlet Round 1 全 10 軸展開 + §M7 棄却履歴 3 件 + §M8 引き継ぎ。
- v0.2 (2026-04-14): C4 (Coherence Defect Lemma) cochain-first 探索枝を追加。§M1 に次段拡張 remark / §M2 に C4 新設 / §M5 に C4 Round 1-3 全走行 (全て射程維持 ✓) / §M8 Phase 5 blocker に C4 形式化試行追加。Codex (2026-04-14) の「埋まらない殻」補正と Coherence Defect Lemma 命名を採用。計算ノート `Face補題_ホモロジー厳密化.md` §1 H_1 却下論理との射程分離を chain degree + homology/cohomology 方向の二重差分で明示。±3σ 入口ゲート通過。
- v0.3 (2026-04-14): C2b を canonical surface として実装。主表示を `H_2^{\mathrm{coh}} = \ker \partial_2 / \mathrm{im}\,\partial_3` に移し、`H^2` は双対注記へ降格。§M1 を homology expansion + non-fillability 判定へ整流し、§M2 に C2b を新設、C4 は archived exploratory branch に再位置づけ。§M5 に canonicalization amendment と negativa を追記。対応本文は v1.14。
- v0.4 (2026-04-14): Tolmetes 判断 (C: 並列 sub-claim 保持) に基づき、v0.3 の C4 archived 化を**部分的に巻き戻し**。C2b は Codex の chain-first canonical として保持しつつ、C4 を「cochain-first, algebraic, partial theorem (QM verified)」として復活。Phase 5 blocker (QM Heisenberg 中心拡大) を Bargmann (1954) / Mackey (1958) 既知結果として完了: シンプレクティック 2-cocycle $\omega(\hat{x}, \hat{p}) = \tfrac{1}{2}\hbar$ が $H^2(\Theta_{QM}) \neq 0$ を構成。**$\hbar$ は $H^2$ 生成元の係数として識別される**。両 sub-claim (C2b chain / C4 cochain) は UCT bridge (C5, 未起草) で接続候補。命名統一は Phase 5 後に持ち越し。本文 §3.4.6 は C2b 主表示で書かれているため、C4 の cochain 視点を §3.4.6 補注 or 別節として追加するかは Phase 5 で判断。
- v0.5 (2026-04-14): `/bou → /ene` の決定に基づき、negativa freeze を先行させたうえで canonical surface を `C4/H^2_{\Theta}` に一本化。本文 §3.4.6 を `H^2_{\Theta}` 主表示の conjectural surface に差し替え、C2b は archived geometric precursor へ降格。§M1 を cohomology expansion + non-globalizability 判定へ整流し、§M2 C4 を canonical / conjectural に修正、§M5 の canonicalization amendment を `H^2` 版へ更新。`H^2` の一般非自明性・recoverability・torsion 意識接続は未主張として固定。対応本文は v1.15。
- v0.6 (2026-04-14): `/ene` Phase 5 blocker 着手。`calculations/計算_QM_H2Theta最小インスタンス.md` を追加し、QM を `H^2_{\Theta}` canonical surface の第一候補として最小計算で固定。内容は probe 水準に留め、`H^2_{\Theta} \neq 0` の一般非自明性や本文の partial theorem 化は依然として未主張。§M2 C4 の検証状態と §M8 blocker 進捗をこの水準に更新。
- v0.7 (2026-04-15): `/ene` で FTC を non-obstructed 対照例として追加。`calculations/計算_FTC_H2Theta対照例.md` を新設し、可縮な区間上の FTC 最小模型では forgetting law `Θ` が global potential 由来の exact 1-cochain となり、`[ω_{\Theta}] = 0` であることを固定。これにより `QM = nontrivial candidate / FTC = trivial contrast` の pair が calculations 面で揃い、C4 を selector surface として読む足場を追加。本文主張の昇格と general selector theorem は依然として未了。
- v0.8 (2026-04-15): `/ene` で selector 条件面を追加。`calculations/計算_H2Theta_selector条件面.md` を新設し、trivial side を `global potential / contractible patching`、nontrivial side を `alternating witness / central extension` として整理。FTC/QM の pair を「存在候補 vs 対照候補」から「selector の十分条件を支える二極」へ引き上げた。ただし必要十分条件、CPS 内部 lift、本文 theorem 化は依然として未了。
- v0.9 (2026-04-15): `/ene` で selector の CPS 内在化条件を追加。`calculations/計算_H2Theta_selector_CPS内在化条件.md` を新設し、外部語 `contractible presentation` / `additive witness` をそれぞれ `CPS-globalization atlas + zero holonomy` / `CPS-obstruction witness + irreducible orientation` へ翻訳した。これにより C4 は `probe surface + selector surface + lift surface` の三層を持つ conjecture になった。ただし package 条件の最小性と本文 theorem 化は依然として未了。
- v0.10 (2026-04-15): `/ene` で lift package の弱化テストを追加。`calculations/計算_H2Theta_selector_package弱化テスト.md` を新設し、full package を `support-local re-lift + generator-face zero holonomy` および `support-local faithful witness + anti/symmetric separation` まで削れる見通しを整理した。これにより C4 は `probe surface + selector surface + lift surface + weak-package surface` の四層を持つ conjecture になった。ただし弱化の反例探索と本文 theorem 化は依然として未了。
- v0.11 (2026-04-15): `/ene` で weak package の反例探索面を追加。`calculations/計算_H2Theta_selector_weakpackage反例探索.md` を新設し、`Weak Lift A'` の false trivialization と `Weak Lift B'` の false obstruction を failure mode として分離した。ここから trivial side には `support-saturated / triple-overlap-consistent / gauge-stable`、nontrivial side には `coboundary-conservative / boundary-closed / refinement-stable` という minimal guard が必要だと整理した。これにより C4 は `probe + selector + lift + weak-package + counterexample` の五層を持つ conjecture になり、次 blocker は guarded package `A'' / B''` の FTC/QM probe へ移った。
- v0.12 (2026-04-15): `/ene` で FTC/QM の guard probe を追加。`calculations/計算_FTC_H2Theta対照例.md` に `A'' guard probe`、`calculations/計算_QM_H2Theta最小インスタンス.md` に `B'' guard probe` を追記し、FTC では `gauge-stable / support-saturated / triple-overlap-consistent`、QM では `coboundary-conservative / boundary-closed / refinement-stable` が minimal model 上で自然に読めることを固定した。これにより C4 は `probe + selector + lift + weak-package + counterexample + guard-probe` の六層を持つ conjecture になり、次 blocker は `A'' / B''` を本文語へ圧縮するかどうかの判断へ移った。
- v0.13 (2026-04-16): `/bou.momentum+ Round 5 accelerate` で §M8 donor 統合欄の欠落補完。v0.9 統合済みの `計算_H2Theta_selector_CPS内在化条件.md` (lift surface)、v0.10 統合済みの `計算_H2Theta_selector_package弱化テスト.md` (weak-package surface)、v0.11–v0.12 統合済みの `計算_H2Theta_selector_weakpackage反例探索.md` (counterexample + guard-probe surface) の 3 donor エントリを §M8 に追記した。QM / FTC の既存エントリに v0.12 guard probe 追記を同期した。§M8 末尾に著者決定パッケージ (決定 1: A''/B'' 本文圧縮判断 / 決定 2: UCT bridge C5 / 決定 3: 符号理論三分法) を新設した。
- v0.14 (2026-04-17): `/ene` で front-stage / backstage の二層語彙を実装。本文 `§3.4.6` に `貼合側 / 残差側` を導入し、`H^2_{\Theta}=0` を局所 law が一つの global law にまとまる側、`[\omega_{\Theta}] \neq 0` を局所整合の残差 class が残る側として圧縮した。`drafts/infra/FaceLemma_技術設計.md` では `FTC = 貼合側`, `QM = 残差側` を front-stage 対応として固定し、`A'' / B''` は backstage の guarded package 名として保持する方針を明示した。対応本文は v1.16。
- v0.15 (2026-04-23): `/noe` の結論に基づき、C4 の missing intermediate object を **整合担体 (`coherence carrier`)** と命名。新規 infra 正本 `drafts/infra/C4_整合担体.md` を追加し、support-local な class 判定の器として定義した。`A'' / B''` を整合担体の両極実現、`貼合側 / 残差側` をその front-stage pair として再配置。§M2 C4 の形式化段階・検証状態・著者決定パッケージをこの命名に同期した。
- v0.15 (2026-04-17): Tolmetes 指示 (β→γ→α) 経路で Claude が C4 の Kalon/±3σ 判定と主張水準整合を実施。body §3.4.6 は既に `partial theorem, QM verified` として §3.4.6.1 で Bargmann/Mackey 援用証明を実装済 (initial snapshot `1876a46` に含まれる)。meta.md §M2 C4 の主張水準を (i) partial theorem (QM verified) / (ii) conjectural (一般 CPS 圏) / (iii) canonical surface scaffolding 保持 / (iv) Kalon ◎△ / (v) ±3σ 通過、の 5 項目に整理。§M3 に Kalon 判定 (◎ Kalon△; 4 非自明派生: FTC 境界条件/Paper XII・XIV 接続/FEP C3 関係/意識 H² torsion) を記録。§M4 に入口 ±3σ (2026-04-14) → 出口 ±3σ 上昇方向 (2026-04-17) を記録 (QM verified で推測から partial theorem への昇格は σ 上昇)。partial theorem 主張と Codex 系列の conjectural canonical surface は並列に保持 (前者は既知結果援用 branch、後者は independent proof branch)。

## §M9 Donor Absorption Ledger (2026-04-18)

### D-II-01: Parzygnatのアイデアを超えて

- **donor path**: `drafts/incubator/Parzygnatのアイデアを超えて.md`
- **receiver surfaces**: `論文II_相補性は忘却である_草稿.md` の既存挿入面、`論文II_相補性は忘却である.meta.md` 本節
- **kept**: 構想1 の可逆性階層判定、構想2 の α-twisted 余モノイド、構想3 の時間依存 Markov blanket、および「どこまで本文へ挿入済みか」の状態情報
- **discarded**: 旧 donor 単独稿としての並列保持だけ。内容棄却はなし
- **final disposition**: donor file を削除し、未接続点だけを meta ledger に残す

### D-II-02: Fisher_SAMを超えて

- **donor path**: `drafts/incubator/Fisher_SAMを超えて.md`
- **receiver surfaces**: `論文I_力としての忘却_草稿.md` §6.7-§6.8、`論文II_相補性は忘却である_草稿.md` §2.5.6、Paper I/II meta
- **kept**: `α-SAM` / `Oblivion-Aware SAM` / 合成案と、CPS 面での接続補助線
- **discarded**: duplicate prose only
- **final disposition**: donor file を削除し、Paper II では近傍形状表側の provenance を保持
