# Automath-Omega-Oblivion Dictionary v0.3

三者対応辞書。automath / The Omega (loning) / 忘却論 の構造マッピング。

**凡例**: [Lean] = Lean 4 機械検証済 / [Paper X] = 忘却論 Paper X / [Omega:XX] = Omega 論文 XX / [NLM] = NotebookLM SOURCE 確認済 / [Open] = 未接続
**v0.3 更新 (2026-04-12)**: Omega 列追加 (三者共接続)。NotebookLM conv. 84bdf5d6 で SOURCE 裏付け

---

## 1. Fold ↔ Forgetful Functor

| automath | 忘却論 | 対応の精度 |
|:---|:---|:---|
| `restrictLE`: X_{m+1} → X_m [Lean: Defect.lean] | 忘却関手 U: C → D | [構造的対応] |
| fiber Φ⁻¹(x) (`fiberMultiplicity`) | ker(U) — 忘却の核 | [構造的対応] |
| |X_m| = F_{m+2} (Fibonacci) | |Ob(C_α)| は不変 (F1公理) [Paper VIII Def.6.2.1] | [構造的対応] ← 対象保存は両者に共通 |
| `restrict_functorial` [Lean証明済] | 粗視化の合成 R の半群性 [Paper V Def.2.1.1] | **[構造的対応・両側証明済]** |
| Fibonacci 成長率 φ | 忘却論に φ は現れない [NotebookLM確認] | **[Open・対応物なし]** |

### 検証課題
- [ ] Φ の fiber 分布と α-忘却濾過の射の消失パターンの対応
- [x] ~~Fibonacci 成長率 φ と忘却論の何かの対応~~ → **Open**: 忘却論に φ は不在。新しい接続点を要構成
- [ ] `restrict_functorial` (Lean) と Paper V Def.2.1.1 の形式的圏同値

---

## 2. Defect Algebra ↔ Oblivion Curvature (最強接続)

| automath | 忘却論 | 対応の精度 |
|:---|:---|:---|
| `restrict_stableAdd_carry_defect` [Lean証明済]: Φ(x⊕y) = Φ(x)⊕Φ(y) ⊕ κ·carryElement | δ = G(f∘g) − G(f)∘G(g) (合成ドリフト) [Paper I §9.5 **OP-I-2 未証明予想**] | **[構造的対応・片側未証明]** automath 側は Lean 証明済、忘却論側は Conjecture |
| `carryIndicator` κ ∈ {0,1} [Lean] | δ ≠ 0 の条件 | **[構造的対応]** κ≠0 ⟺ δ≠0 の離散版 |
| `walshFlux` + `deltaSet` (高次離散微分) [Lean: WalshStokes.lean] | Leibniz 規則 d(ΦT) = dΦ∧T + Φ·dT [Paper I §3.3 証明済] | **[構造的対応・両側証明済]** Walsh flux = 離散外微分、Leibniz = 連続外微分 |
| `carryElement` の Fibonacci 値 (fib m) [Lean] | 忘却論に対応物なし | **[Open]** carry の量的構造は忘却論に未移植 |
| carry 構造 (chain algebra) | α-接続の carry (Amari-Chentsov テンソル C_{ijk}) | [推測] |

### v0.3 追加: 忘却レベルの同定 (NotebookLM 双方向対話 2026-04-12)
**carry defect は U_compose (n=1.5) の離散インスタンスである**
- 根拠: restrict (忘却) と stableAdd (合成) の非可換性 = 「合成律の忘却によるドリフト」
- U_arrow (n=1) ではない: 射の存在自体は保存されている (restrictLE は well-defined)
- U_compose (n=1.5) である: 射の **合成の保存** が壊れている (δ ≠ 0)
- U_depth (n=2) ではない: 自然変換レベルの構造は関与しない

### v0.3 追加: Walsh 基底 ↔ Chebyshev 1-形式 T の対応 (NotebookLM 2026-04-12)
- 連続: T_i = g^{jk}C_{ijk} — 「α-接続が Levi-Civita から逸脱する方向」を指定する 1-形式
- 離散: A ⊆ Fin n — 「どのビット方向に離散微分を取るか」を指定する座標部分集合
- deltaSet の符号交替 (−1)^|B| ↔ 外微分の反対称性
- walshFlux (境界和) ↔ ∫ d(ΦT) (積分)
- **dT = 0 の離散版**: automath で dT=0 に対応するのは「Walsh 基底が座標と一致する場合」(= 標準基底)

### 検証課題
- [ ] δ の Lean 4 定義を Paper I の合成ドリフトの言語で再定式化
- [ ] **離散 Stokes ↔ Leibniz の形式的対応** → §2.A で掘り下げ (v0.3)
- [ ] 指数型分布族 (dT=0) に対応する automath の「特殊ケース」は何か
- [ ] U_compose (n=1.5) の同定を Paper I 側で形式的に記述する方法

### §2.A Walsh-Stokes ↔ Leibniz 精密対応 (v0.3、NotebookLM 双方向対話で精密化)

**問い**: `walshFlux` / `deltaSet` と d(ΦT) = dΦ∧T + Φ·dT の間に、関手的対応は構成できるか?

**Leibniz 規則の離散的書き下し** (NotebookLM 2026-04-12):

| 連続 (Paper I §3.3) | 離散 (automath WalshStokes.lean) | SOURCE |
|:---|:---|:---|
| d(ΦT) | deltaSet A f (A 方向の高次離散微分) | [両側証明済] |
| dΦ ∧ T | walshFlux A (deltaSet {i} f) — A が張る面で、直交方向 {i} への f の変化量 | [構造的対応] |
| Φ · dT | f と A 自体の「歪み」の積。**dT=0 ⟺ A が flat (標準基底)**。Walsh 基底は位置に依存せず一定なので恒等的に dT=0 | [構造的対応] |
| 指数型分布族 dT=0 → F=0 ⟺ dΦ∧T=0 (系 5.1.1) | automath の標準的ハイパーキューブ = dT=0 の離散版。力は carry (dΦ∧T≠0) のみから生じる | [構造的対応] |

**方向性定理の離散版** (NotebookLM 2026-04-12):

| 連続 (Paper I Th.5.1) | 離散 (automath) | 接続条件 |
|:---|:---|:---|
| F_{ij} ≠ 0 | carry defect δ(x,y) ≠ 0 | **離散 Stokes 恒等式が成立すること** |
| d(ΦT) ≠ 0 | walshFlux A f ≠ 0 | 離散 Stokes が δ と walshFlux を橋渡し |
| Φ → 0 (曲率消滅) | No11 制約が trivial (全 Word が stable) | 忘却がない → 力がない |
| δ → 0 (合成保存) | fold が ring homomorphism になる | **OP-I-2 の離散的解決** |

**OP-I-2 部分的解決の構造** (NotebookLM 確認):
- 忘却論 OP-I-2: 「Φ→0 で δ→0、標準圏の公理が回復する」= **未証明予想**
- automath: 「No11 制約消失 → carry defect=0 → fold は環準同型」= **Lean 4 証明済み**
- automath は OP-I-2 の **有限体上の離散的実現** を機械検証で提供している
- これは OP-I-2 の「部分的かつ極めて強力な」解決。連続版の証明にはまだ隙間がある

**構造比較テーブル** (v0.3 更新):

| 層 | automath (離散) | 忘却論 (連続) |
|:---|:---|:---|
| 空間 | Word n = {0,1}^n (ハイパーキューブ) | M (統計多様体) |
| 関数 | f: Word n → ℤ | Φ: M → ℝ (忘却場) |
| 方向 | A ⊆ Fin n (座標部分集合 = flat) | T_i (Chebyshev 1-形式。指数族で dT=0) |
| 微分 | deltaSet A f w = Σ (−1)^|B| f(flip B w) | (dΦ)_i = ∂_iΦ |
| 外積 | carry defect δ(x,y) = κ · carryElement | dΦ ∧ T (方向的不整合) |
| Stokes | walshFlux A f = Σ_{boundary} deltaSet | ∫ d(ΦT) = ∫ (dΦ∧T + Φ·dT) |
| 曲率 | δ ≠ 0 ⟺ carry 発生 | F_{ij} ≠ 0 ⟺ d(ΦT) ≠ 0 |
| 忘却なし | No11 trivial → δ=0 → 環準同型 [Lean] | Φ→0 → δ→0 → 標準圏 [OP-I-2 予想] |

**関手候補 D: Man → Hyp** (離散化関手):
- D(M) = {0,1}^n (n = dim M)
- D(Φ) = f: Word n → ℤ
- D(T) = A ⊆ Fin n (dT=0 の場合、標準基底)
- D(d) = deltaSet
- D(∧) = carry defect
- D(∫) = walshFlux

**open 課題**:
- [ ] D が関手であること (合成保存) の証明
- [ ] 非指数型分布族 (dT≠0) に対応する automath の「ねじれたハイパーキューブ」は構成できるか?
- [ ] carry defect の Fibonacci 量 (fib m) は、忘却曲率 F_{ij} のどの幾何学的量に対応するか?
- [ ] 連続版 OP-I-2 の証明に、離散版 (automath) からのリフトは可能か?

---

## 3. Scan-Projection ↔ Renormalization (Paper V)

| automath | 忘却論 | 対応の精度 |
|:---|:---|:---|
| scan error ε_m | Φ(θ,μ) = D_KL(p^(μ) ‖ q^(μ)) [Paper V Def.2.1.2] | [構造的対応] |
| Bayesian half-bound 2ε ≤ 1 [Lean] | DPI: D_KL(Kp ‖ Kq) ≤ D_KL(p ‖ q) [Paper V Th.2.2.2] | **[構造的対応・両側証明済]** |
| `momentSum_two_mono'`: S_2 単調性 [Lean証明済] | β_Φ ≥ 0 (忘却場 c 定理) [Paper V Th.2.2.2] | **[構造的対応・両側証明済]** 離散単調性 ↔ 連続単調性 |
| SPG → RG 接続 (README記載) | 忘却場 β 関数 → 漸近的自由の構造的排除 [Paper V] | [構造的対応] |
| `collisionKernel2/3/4`: companion matrix [Lean証明済] | Paper V に transfer operator **なし** [NotebookLM確認] | **[Open・対応物なし]** automath 固有の構造 |
| collision kernels 共通不変量 tr=2, det=−2 [Lean] | 忘却論に対応物なし | **[Open・新発見の候補]** |

### v0.3 追加: collision kernel 不変量の輸入仮説 (NotebookLM 2026-04-12)
**tr=2, det=−2 は忘却場の RG 普遍性クラスの新スペクトル不変量として機能しうる**
- S_2 単調性 ↔ β_Φ ≥ 0 は確認済み (両側証明済)
- companion matrix の不変量 (tr, det) は忘却論に **存在しない** 新構造
- Paper V の「忘却の普遍性クラスと臨界指数」に対応する離散的スペクトル不変量
- **輸入経路**: 忘却場 Φ(θ,μ) のスケール μ に沿った fiber 分布の moment sum S_q(μ) を定義し、その companion matrix のスペクトルを忘却場の RG 不変量とする

### 検証課題
- [ ] scan error ε と忘却場 Φ の定量的対応 (情報幾何上の距離として)
- [x] ~~S_q の companion matrix と忘却場の transfer operator の spectral 対応~~ → **対応物なし**。逆方向の輸入候補
- [ ] tr=2, det=−2 の普遍的不変量の情報幾何学的意味 (忘却論への新輸入)
- [ ] 忘却場のスケール μ に沿った moment sum S_q(μ) の定義可能性

---

## 4. Forcing Framework ↔ α-Oblivion Filtration (Paper VIII)

| automath | 忘却論 | 対応の精度 |
|:---|:---|:---|
| L₀ ≼ L₁ ≼ … ≼ L₁₀ (11層保存拡大) | α-忘却濾過 + **8段階**離散骨格 [Paper VIII 系6.5.3] | **[構造的対応・層数不一致]** automath=11層、忘却論=8段階 (cell次元 n=1..ω) |
| Kripke 意味論 M,p ⊩ φ | α-米田埋込 y_α(X)(Y) := Hom_{C_α}(Y,X) [Paper VIII Def.6.2.2] | [推測] |
| conservative extension | PSh(C) ⊇ Sh_α(C) ⊇ Set^{Ob(C)} [Paper VIII Th.6.8.9] | **[構造的対応]** 保存拡大 ↔ トポスの降鎖列 |
| `σ-algebra non-expansion` G^{L+1} ⊆ G^{L} [Lean] | (F4) 単調性: Mor(C_{α₂}) ⊆ Mor(C_{α₁}) [Paper VIII] | **[構造的対応・両側証明済]** |
| typed multi-layer observer | HoTT (-1)-truncation ↔ α=1 [Paper VIII OP-VIII-5] | [Open] |

### 検証課題
- [x] ~~automath の 11 層と忘却論の α の離散化~~ → **層数不一致確認済** (11 vs 8)。対応には正規化写像 α(n) = n/ω の拡張が必要
- [ ] forcing の ⊩ と α-米田埋込の形式的関係
- [ ] OP-VIII-5 (HoTT 接続) を automath の Lean 4 基盤で攻略できるか

---

## 5. POM ↔ F⊣G Adjunction

| automath | 忘却論 | 対応の精度 |
|:---|:---|:---|
| LIFT | F (溶解 / dissolution) [Paper VI Def.2.1.1] | [構造的対応] |
| U^t (time evolution) | G∘F サイクル (Ostwald 熟成) [Aletheia §5] | [推測] |
| PROJECT | G (結晶化 / crystallization) [Paper VI Def.2.1.1] | [構造的対応] |
| stable readout (`No11` constraint) [Lean] | Fix(G∘F) = Kalon [Paper VI, Kalon §6] | **[構造的対応]** 安定読出し = 不動点 |
| 4 projection gates P_Z, P_≤, P_prim, P_χ | 忘却関手の型分類 (Obs 圏の粗視化型) [Paper V §2.1] | [推測] |
| golden ratio φ as spectral invariant [Lean] | 忘却論に φ は不在 [NotebookLM確認] | **[Open・対応物なし]** |

### 検証課題
- [ ] POM の 4 gates と忘却論の忘却関手分類の対応
- [x] ~~φ の情報幾何学的意味~~ → **Open**: 忘却論に黄金比は不在。automath から忘却論への新しい輸入候補
- [ ] stable readout の Lean 4 定義と Kalon の Fix(G∘F) 定義の形式的同値性

---

## 6. Physical Spacetime ↔ Paper XIII

| automath | 忘却論 | 対応の精度 |
|:---|:---|:---|
| observer = fiber index | 知覚者 = 2-cell [Paper VII, VIII] | [構造的対応] |
| time = decision envelope projection | 時間 = α-濾過の方向 | [推測] |
| causality = partial order on refinement | CPS0' の容器先行性 [Paper VIII] | [構造的対応] |
| clock transport δΘ = Ω [Lean] | Face Lemma → Christoffel [Paper XIII 予想 D1] | [推測] |
| minimal closure → G_{μν} + Λg_{μν} = κT^(res)_{μν} [Lean] | CPS スパン → Einstein eq. [Paper XIII 予想 D2-D3] | [推測] |

### 検証課題
- [ ] automath の Einstein 導出の Lean 4 証明と Paper XIII の予想 D1-D3 の精密対応
- [ ] 「no physics axioms added」と「CPS0' から重力」の構造的等価性
- [ ] automath 側の cosmological constant Λ と忘却論の α パラメータの関係

---

## Open Questions (三者統合)

1. **黄金比 φ の忘却論的意味**: automath + Omega で φ がスペクトル不変量として回収される。忘却論の α 空間に φ は現れるか? → 忘却場 Φ の固定点構造に φ が隠れている可能性
2. **Lean 4 × 忘却論**: Paper I 方向性定理を Lean 4 で形式証明する最短経路は? automath `walshFlux` が離散版として再利用可能か?
3. **NULL semantics × ker(U)**: automath の 3 種 NULL (Semantic/Protocol/Collision) は忘却論の ker(U) 選択可能層 / ker(T) 不可避層 [Paper 0 §6.4] と対応するか?
4. **Čech H² × Drift**: automath の大域的貼り合わせ障害 (gerbe structure) と忘却論の Drift ∈ [0,1] の関係
5. **Zeckendorf ↔ CPS**: no-consecutive-1s が CPS の離散版か? 「隣接 1 の禁止」= Paper III α<0 anti-Markov (複製不能) と共鳴する可能性 [NLM]
6. **Von Neumann Type ↔ α**: Omega の Type I/II/III 分類は α-忘却濾過のどの α 値に対応するか? (Type I = α≈0, Type III = α≈1?)
7. **三経路 Einstein の合流**: automath (defect→Stokes→Einstein) / Omega (CAP→ADM→Einstein) / 忘却論 (CPS→Face Lemma→Einstein) が同一の方程式を導出する形式的証明 (ultimate goal)
8. **Omega Resolution Folding ↔ Paper V**: Omega RF 論文 (64→21 Zeckendorf filtering) と Paper V (Obs 圏の粗視化) の構造的対応。Z128/SM の 64→21 射影は忘却関手の具体的インスタンスか?
