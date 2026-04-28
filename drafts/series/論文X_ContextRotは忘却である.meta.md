# 論文 X — ContextRot は忘却である `.meta.md`

> 本ファイルは calculations 棚卸しにより新規作成された meta ファイルである。
> §M1–§M7 は初期 body (v0.1) から後付けで整備した骨格版であり、v0.3.1 で記号衛生と §M6 実化面を同期した。
> body が安定した時点で著者が精査・拡充すること。

---

## §M1 F⊣G 宣言 (固定日: 2026-04-16)

- **F (発散関手)** = AgentSwing CM 戦略 (DA/Sum/KLN) を Hom 集合の同値関係 R による商関手族 {U_R} として定式化し、Case Study (N=2) と N=240 統計から「条件付き不可逆性テーゼ」と「状態依存最適忘却」を導く。忘却論の忘却関手 U₀ および Hyphē の boot⊣bye 随伴との AP 共有は、OP-X-6 の Drift 測定で昇格させる橋渡し面として保持する。文体ガイドの §3 メタファー三連と §10 Type α+δ 合成を採用。
- **G (収束関手)** = 商関手族の半順序構造 (Thm 3.1) と因子分解定理 (Thm 6.1) を proof_cm_categorical 文書で閉じる。統計的随伴 η_stat/ε (Thm 4.4/4.5) は pointwise ではなく統計的に成立すること (Table 2 全エントリ) を数値根拠として収束させる。確信度マップ §8 による自己校正。文体ガイド §4 数式裏付け + AgentSwing SOURCE (Appendix C, Table 2, Fig 9) 照合。
- **主要随伴**: F_par ⊣ G_route (AgentSwing) / boot ⊣ bye (Hyphē) の二層構造。
- **固定日**: 2026-04-16 (初期 body v0.1 後付け整備。v0.3.1 で記号衛生のみ同期)

---

## §M2 核主張リスト (L3 対象)

- **C1**: AgentSwing CM 戦略 (DA/Sum/KLN) は軌道圏 C_traj 上の同値関係 R による商関手族 {U_R} として圏論的に well-defined である。半順序構造 (U_DA > U₀ > {U_KLN, U_Sum} > Id, Thm 3.1) と因子分解 (U₀ = Π_R ∘ U_R, Thm 6.1) が成立する。[確信 90%]
- **C2**: 条件付き不可逆性テーゼ (命題 X.1): 忘却の不可逆性による性能劣化は状態型 (Type 1: recent useful clue / Type 2: dead-end loop / Type 3: correct hypothesis, wrong action) に依存する。最適な忘却強度は状態の関数である。[推定 75%]
- **C3**: 状態依存最適忘却 (命題 X.2): AgentSwing routing G_route は Q_k(I) を最大化する U_R を状態依存的に選択する適応的忘却である。統計的随伴 F_par ⊣ G_route は E[Q(G(F(I)))] ≥ E[Q(I)] (η_stat 条件) を Table 2 全エントリで満たす。[推定 80%]
- **C4**: boot⊣bye 橋渡し命題 (Thm 5.1 候補): 忘却論の U₀、Hyphē の boot⊣bye、AgentSwing の {U_R} + F_par⊣G_route は同一の抽象パターン AP (abstract forgetting pattern) のインスタンスである。AP は (1) 商関手的忘却、(2) 統計的随伴、(3) 状態依存最適化の三要素を共有する。ただし本体の前景ではなく、Drift 測定で昇格させる橋渡し面として扱う。[推定 75%]

---

## §M3 Kalon 判定履歴

| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| 2026-04-03 | C1 (圏論的定式化) | ◯ Kalon△ | proof_cm_categorical 文書を実際に書くことで、P2 (CM = U parameterization) が [仮説 55%] → [推定 80%] に格上げ (§8.3 教訓 CD-15)。「棄却は証明の失敗後にのみ許される」という原則の自己適用。 |
| 2026-04-03 | C3 (統計的随伴) | △ | η_stat が pointwise ではなく統計的にのみ成立 (Thm 4.4) という制約が明示されており、過大主張を自己抑制。N=240 という具体的 SOURCE がある。ただし確率的 Galois 接続の一般理論 (OP-X-2) は Open。 |

---

## §M4 ±3σ ゲート履歴

| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| 2026-04-03 | C1 (商関手 well-definedness) | +3σ | +3σ | proof_cm_categorical で Def 1.1-1.3 + Thm 3.1/6.1 を構成的に示した。「対応がある」一般論から「射が well-defined」まで射程を縮めず達成。 |
| 2026-04-03 | C3 (統計的随伴) | +3σ | +3σ | 「F⊣G 的に機能する」一般論ではなく「N=240, Table 2 全エントリで η_stat 成立」という具体的数値に落とした。pointwise 随伴を主張せず統計的随伴に限定したことで射程を守った。 |
| 2026-04-03 | C2 (条件付き不可逆性) | ±3σ | ±3σ | N=2 Case Study + N=240 統計から [推定 75%]。Type 1/2/3 の分類が N≥10 Case Study で 60% 以上の予測精度を持つかどうかは未検証 (OP-X-5)。一般化の射程は保留中。 |

---

## §M5 Refutation Gauntlet ログ

### C1 — 2026-04-03 Round 1 (CD-15 起源)
- **反論**: 「AgentSwing CM と忘却関手の "数学的対応" は形式的であり、実質的対応がないのでは」(初期 /kat+ による棄却)
- **SFBT**: 「できないのではなく、数学を書いていないだけではないか」(Creator 2026-04-03)
- **前提強化**: proof_cm_categorical 文書で Def 1.1-2.4 + Thm 3.1/4.4/6.1 を構成的に示した
- **結果**: 射程維持 ✓ — 商関手の well-definedness が確立。P2 [仮説 55%] → [推定 80%] に昇格 (§8 較正履歴)

### C3 — 2026-04-03 Round 1 (pointwise vs 統計的)
- **反論**: 「η_stat (E[Q(G(F(I)))] ≥ E[Q(I)]) が個別タスクで全戦略失敗する可能性があるなら、随伴は成立しないのではないか」
- **SFBT**: 「pointwise 随伴ではなく統計的随伴として定式化できないか」
- **前提強化**: Thm 4.4 (η_stat は統計的 — 個別タスクでは全戦略失敗がありうる) を明示的に本文に載せ、Table 2 N=240 を根拠とした
- **結果**: 射程維持 ✓ — 「統計的随伴」として主張を精密化。確率的 Galois 接続の一般理論は OP-X-2 として開放

### C2 — 2026-04-03 Round 1 (CD-14 撤回前)
- **反論**: 「Case 1+2 は N=2 の over-generalization (CD-14) ではないか。Type 1/2/3 分類は単純化しすぎでは」
- **SFBT**: 「N=240 統計で独立に支持されているか確認できないか」
- **前提強化**: Table 2 (3 モデル × N=240, aligned) で非一様な遷移分布を確認 (Fig 9)。Phase C v3 実験 (§2.3 備考 X.1a) で条件依存性を独立確認。CD-14 撤回
- **結果**: 射程維持 ✓ — [推定 75%] を維持。ただし Type 3 (correct hypothesis, wrong action) は Case Study 未確認 — 未解決 blocker として保持

### 補助射 (symbolic-level 加筆) — 2026-04-17 Round 1

- **反論**: 「context-level (§4.2) と weight-level (§4.5) の 2 層で persistent compression は十分では。symbolic layer を新たに立てる必要があるか」
- **SFBT**: 「できないのではなく、3 層化していないだけではないか。symbolic 層の経験的事例は何か」
- **前提強化**: Karpathy (2025) の LLM Wiki gist 実装事例 + Zenn (dely_jp 2025) schema 明文化例で symbolic layer (`Wiki_i`) を `boot⊣bye` と同一抽象パターンへ接続。§4.6 で 3 層対比テーブルを構成
- **結果**: 射程維持 ✓ — 既存 2 層対比に symbolic 層を追加して 3 層構造が完成。命題 X.9 (symbolic-level drift 制御の優位性) を [推定 60%] で導入。大規模 wiki での weight-level 同等 drift を撤回条件として明示

---

## §M6 虚→実変換面

### C1
- 野望: AgentSwing の CM 戦略を、経験的な engineering heuristic ではなく、U₀ へ向かう商関手族 {U_R} として self-contained に読ませる。
- 現在まだ虚な点: 最小証明は D1 donor にあり、本文本体では要約に留まる。U_Sum の弱合成保存、Q の直接計算不能、確率的 Galois 接続の一般理論は未完。
- 実へ引くための SOURCE: 本文 §3、§6.1 X.5、§8.1、§M8 D1。外部監査では D1 本文そのものではなく、本 meta に要約された Def/Thm 範囲のみを SOURCE とする。
- 実化の判定条件: Paper X 本文または付録に C_traj / D_traj / U₀ / U_R / Thm 3.1 / Thm 6.1 の最小構成が入り、U_Sum と η_stat の未完条件が明示されること。
- 次の実化操作: D1 donor から最小証明だけを Paper X 付録へ移し、本文 §3 の「要約」を「最小構成 + donor 参照」に変える。
- 最新状態: 変換中

### C2
- 野望: 忘却の不可逆性は一律の悪ではなく、状態型ごとに利得と損失が反転することを示す。
- 現在まだ虚な点: Case 1/2 は強い対照だが N=2。Type 3 は表にあるが Case Study 未確認。N=240 統計は戦略別集計であり、状態型分類を直接検証していない。
- 実へ引くための SOURCE: 本文 §2.1-§2.4、§6.2 P-E2a/P-E2b、§7 OP-X-5、§M5 C2。
- 実化の判定条件: N≥10 の状態型ラベル付き Case Study で Type 1/2/3 分類が 60% 以上の予測精度を持ち、Type 3 の少なくとも 1 ケースが追加されること。
- 次の実化操作: OP-X-5 として、trigger 前の軌道だけから Type 1/2/3 を分類し、DA/Sum/KLN の勝敗を予測する小規模分類器を作る。
- 最新状態: 変換中

### C3
- 野望: AgentSwing routing を、ブラックボックス選択ではなく、状態 I に応じて U_R を選ぶ適応的忘却として定式化する。
- 現在まだ虚な点: η_stat は統計的であり pointwise ではない。Table 2 はモデル依存性も示しており、状態依存性とモデル依存性の分離が未完。Q_k は Lookahead 近似で、Q の直接計算は未解決。
- 実へ引くための SOURCE: 本文 §2.4、§3.5、§6.1 X.2/X.6、§7 OP-X-5/OP-X-6、§M5 C3。
- 実化の判定条件: 固定 DA / 固定 Sum / 固定 KLN / learned routing / state-law routing を同一データで比較し、state-law routing が固定戦略を上回り learned routing に迫る、または勝つこと。
- 次の実化操作: OP-X-5 と OP-X-6 を束ね、状態分類と Drift 推定を同時に走らせる。
- 最新状態: 変換中

### C4
- 野望: 忘却論 U₀、Hyphē boot⊣bye、AgentSwing CM を「同じ抽象パターン AP」だけでなく、同じ測定軸 Drift で比較できる対象にする。
- 現在まだ虚な点: AP identity は D1 donor の要約上は成立するが、τ↔r_AS は 2 データポイント制約で [仮説 50%]。D2 自身も E1 は data 不足、E2 のみ本文直結としている。
- 実へ引くための SOURCE: 本文 §4.1-§4.4、§5、§7 OP-X-3/OP-X-6、§M8 D1/D2。
- 実化の判定条件: AgentSwing ログから CM 戦略ごとの Drift が推定され、Pass@1 との関係が状態型ごとの逆 U 字またはその反証として記録されること。
- 次の実化操作: OP-X-6 を先行し、τ↔r_AS は Drift 推定後に OP-X-3 として昇格判定する。
- 最新状態: 変換中

## §M7 棄却された代替案

- **棄却 1**: 「CM 戦略の数学的対応は棄却」(初期 /kat+ 判定)。proof_cm_categorical で Thm 3.1/6.1 が構成されたことで撤回。棄却は証明の失敗後にのみ許される (CD-15 教訓)。
- **棄却 2**: 「pointwise 随伴 G∘F = Id が成立する」。ker(U_DA) = Hom×Hom (全忘却) の構造から pointwise 随伴は不可能。統計的随伴 (η_stat 条件, Thm 4.4) に限定。
- **棄却 3**: 「DA が全状態で最優 CM 戦略である」。Case 1 (Mando) で KLN が最適、Case 2 (live-crickets) で DA が最適という非一様性が確認済み。固定戦略論は状態依存最適化命題 X.2 により棄却。
- **棄却 4**: 「τ ↔ r_AS 逆関数関係 (命題 X.4) は [確信] レベルである」。データポイントが 2 つのみ (τ=0.70→r_AS=0.4, 推定 τ=0.85→r_AS=0.2)。OP-X-3 の実験的決定前は [仮説 50%] に留める。
- **棄却 5**: 「Hyphē の boot⊣bye と AgentSwing CM は全く別構造」。§4 (4.1-4.5) で構造的同型を示した: bye = R_strategy, boot = continue, Mem_i = Compressed_i。三者合流 AP は Thm 5.1 として proof_cm_categorical に収録。

---

## §M8 Donor 統合メモ (calculations 棚卸し)

以下は `calculations/` 配下の作業文書から Paper X に関連する donor の棚卸し結果である。いずれも本文 (body) への直接吸収は行わず、meta 参照として記録する。

以下は `calculations/` 配下の作業文書から Paper X に関連する donor の棚卸し結果である。いずれも本文 (body) への直接吸収は行わず、meta 参照として記録する。

### D1: CM 戦略の圏論的定式化 (B-class)
- **donor**: `calculations/証明_CM戦略の圏論的定式化.md` (531 lines)
- **donor status**: 証明試行 (proof attempt)。C_traj well-defined [確信 90%]、CM=商関手 [推定 80%]、半順序 Thm 3.1 [確信 90%]、因子分解 Thm 6.1 [確信 90%]、η_stat 統計的 [推定 80%]、ε non-increase [推定 75%]、AP identity [推定 75%]
- **内容**: 軌道圏 C_traj (Def.1.1)、前順序圏 D_traj (Def.1.2)、忘却関手 U₀ (Def.1.3) を構成。CM 戦略 (Discard-All=U_DA, Summary=U_Sum, Keep-Last-N=U_KLN) を商関手族 {U_R} として定式化 (Def.2.1-2.4)。半順序構造 Thm 3.1 (U_DA > U₀ > {U_KLN, U_Sum} > Id)、因子分解 Thm 6.1 (U₀ = Π_R ∘ U_R)。η_stat は統計的 (pointwise ではない): 個別タスクでは全戦略失敗がありうる (Thm 4.4)。Hyphē / AgentSwing / 忘却論が同一 Abstract Pattern AP を instantiate (Thm 5.1)。
- **本文との関係**: Paper X body は §3-§4 で CM 戦略を商関手族 {U_R} として定式化しており、本 donor (proof_cm_categorical) を直接引用・基盤としている。donor の Thm 3.1 (半順序) と Thm 6.1 (因子分解) は Paper X §3-§4 の圏論的枠組みの構成的証明を提供。
- **判定**: Paper X の圏論的基盤として最も直接的な donor。ただし η_stat は統計的 (pointwise でない) であり U_Sum の弱合成保存は [推定 70%]。Q は直接計算不能 (Lookahead 近似)。確率的 Galois 接続の形式理論は未完。本文 v0.3.1 以後、最小証明の body 統合を再評価。

### D2: AgentSwing 忘却 Hyphē 接続 (B-class)
- **donor**: `calculations/調査_AgentSwing忘却Hyphē接続.md` (155 lines)
- **donor status**: 調査 (investigation)。E1 [仮説 40%]、E2 [推定 70%→80%]、E3 [推定 60%]、E4 [推定 55%]
- **内容**: AgentSwing × Hyphē × 忘却論の4方向 MECE 分類。E1: τ↔r_AS 臨界密度 (Hyphē τ_cos=0.70 ↔ AgentSwing r_AS∈{0.2,0.4})、E2: 不可逆性テーゼ → AgentSwing 限界予測 (→D3 に詳細)、E3: AY metrics → routing quality、E4: Multi-scale Nucleator → Lookahead correspondence。E2 から3つの検証可能命題: P-E2a (Summary Fixation Theorem)、P-E2b (Discard-All Amnesia Theorem)、P-E2c (Routing Ceiling Theorem)。
- **本文との関係**: Paper X body §2 (case studies: N=2, N=240)、§6 (predictions)、§7 (limitations: router self-limitation) に対応。E2 (不可逆性テーゼ) のみ §6 predictions に直結。E1 (τ↔r_AS) は empirical data が不足 (feasibility 低)。
- **判定**: 4方向のうち E2 のみ Paper X に直結。E1 は AgentSwing raw data 必要、E4 は proof 必要。cross-paper reference として記録。撤回条件が各仮説に明示されている。

### D3: AgentSwing 不可逆性テーゼ (B-class)
- **donor**: `calculations/予測_AgentSwing不可逆性テーゼ.md` (278 lines)
- **donor status**: 証明ノート→構成的証明に格上げ (proof_cm_categorical により CD-14 撤回)。P-E2a [推定 80%]、P-E2b [推定 80%]、P-E2c [推定 75%]
- **内容**: U の非単射性 (∃x₁≠x₂: U(x₁)=U(x₂)) から3つの操作的限界を導出。P-E2a Summary Fixation Theorem: 多数派の誤仮説が要約に固定され不可逆化 (Lil Durk case, Turn 1-22)。P-E2b Discard-All Amnesia Theorem: 全忘却は ε 近傍から遠方へ退行。P-E2c Routing Ceiling Theorem: AgentSwing の上限 = router の U 非単射性検出能力。最適忘却強度関数 U* = argmin[Cost_info_loss(U) + Cost_context_rot(¬U)]。
- **本文との関係**: Paper X body §6 (predictions) に直接対応。body の「条件付き不可逆性テーゼ」は本 donor の核心。不可逆性の本質は非可換性ではなく U の非単射性 (right adjoint N は部分復元のみ: N∘U ≠ Id_C)。
- **判定**: Paper X §6 の prediction の理論的裏付け。N=1 過般化リスク (CD-14, CD-3) は CD-14 撤回により軽減。ε 近傍での CM トリガーが最もリスクが高い。本文 v0.3.1 以後、body 統合を再評価。

### D4: Brevity Constraint と自己誘発的 Context Rot (A-class external)
- **donor**: `arXiv:2604.00025 Brevity Constraints Reverse Performance Hierarchies in Language Models`
- **donor status**: 外部経験的ソース。[確信 90%] 要旨レベルでは、31 モデル・1,485 問で大規模モデルの spontaneous scale-dependent verbosity を同定し、brevity 制約で精度が最大 26pt 改善、数学推論・科学知識で性能階層が逆転。
- **内容**: Context Rot を「長い履歴に irrelevant information が堆積する現象」と見る Paper X に対し、本 donor は **単一ターン内部での overelaboration も rot を起こしうる**ことを示唆する。brevity 制約は `U_DA / U_Sum / U_KLN` のような事後 CM ではなく、出力生成の直前に不要枝を切り落とす **予防的忘却 (prophylactic forgetting)** として解釈可能。
- **本文との関係**: Paper X body の直接証拠ではない。半順序 Thm 3.1 や因子分解 Thm 6.1 を補強するものではなく、むしろ §1.1 Context Rot 定義と §4.4 Drift-Performance トレードオフの**左枝** (`Drift ≈ 0` 側の性能劣化) に新しい読みを与える donor。さらに `router 自身が verbosity により自己劣化する` なら §6.3 命題 X.7 (メタ二重天井) の外部傍証候補になる。
- **判定**: 現段階では **meta 保留**が妥当。本文昇格前に少なくとも 2 点が必要:
  1. brevity prompt の実物確認 — それが純粋な書式指定か、探索制約としての $C$ か
  2. brevity が効かなかった/逆効果だった task の確認 — 条件付き不可逆性テーゼ (Type 1/2/3) と接続するため
  上記未確認のまま本文に統合すると、「静的な一律制約」と「状態依存 routing」を混同する危険がある。

### D5: Brevity テンプレートの logit-level 実証 (A-class external, C境界事例確定)
- **donor**: `arXiv:2604.18389 Liu & Chu (2026) "Understanding the Prompt Sensitivity of Large Language Models"`
- **donor status**: 外部経験的ソース。[確信 90%] 11モデル × 4データセットで系統的検証済み。
- **内容**: Liu & Chu (2026) RQ2 「Fewer」条件 — template トークン数を削減した際に何が起きるか。
  - `||Δh^(l)||`（内部表現の divergence ノルム）が減少することを Qwen / Llama / Gemma 系列で実測。
  - logit 分散の低下: ロジット層での `|Δlog π(y_t|h)|` 低下が Cauchy-Schwarz 上界の縮小から予測される。
  - 因果的証拠: Activation Steering (Appendix G) により `||Δh||` の logit への因果役割を介入実験で確認。
  - **brevity 制約の忘却論的解釈**: テンプレートを短縮する (`brevity 制約`) = 入力情報の一部を出力前に切り落とす予防的操作 = D4 (Hakim 2026) が意味品質層で同定した **prophylactic forgetting** を、**トークン分布層** で独立に実証する。
- **本文との関係**:
  - D4 (Hakim 2026) の **logit-level 外部補強**: D4 は意味品質層 (精度 26pt 改善) で brevity = prophylactic forgetting を同定。本 donor はそれとは独立に、token 確率分布層 (`|Δlog π|`) で同じ操作の力学的機構を与える。2 層の独立した証拠が合流する点で D4 の確信度を補強。
  - **条件付き不可逆性 (C2/C3) との接続**: テンプレート適用後は `||Δh^(l)||` の軌跡が全層にわたって定まり、質問内容 (`C`) のみからは回復できない (RQ4: テンプレート寄与 >> 質問寄与)。これは Type 1 条件付き不可逆性 (入力構造が固定されると質問のみで状態を変更できない) の logit-level 実例。
  - **論文XI §7.7.4 (接続 A) との連動**: 論文XI の H₃ 分解 (P=(C,E), ∂Q/∂E≈0) と本 donor の RQ4 (template > question logit contribution) は測定層は異なるが同じ構造を指す。論文XI §7.7.4 に接続済み。
- **D4 との差異 (測定層)**:
  - D4 (Hakim 2026): 意味品質層 — 精度・性能階層の逆転
  - D5 (Liu & Chu 2026): トークン分布層 — `||Δh||`・`|Δlog π|` の介入実験
  - 二層は独立に計測されており、相互に補強するが同値ではない (測定層差異 = MISMATCH 解消済み)
- **判定**: **C境界事例として確定**。D4 の meta 保留とは異なり、本 donor は以下を満たす:
  1. brevity prompt の実物確認: RQ2「Fewer」条件が template token 削減の書式指定として使用されている
  2. 条件付き不可逆性テーゼとの接続: Type 1 (template 固定後の質問-only 復元不可) として接続可能
  本文昇格前の 2 条件を両方満たすため、C境界事例として本 meta に確定記録する。本文昇格は D4 の meta 保留解除と同時に再評価すること。

### D6: Persona Steering とタスク依存的な選択的忘却 (A-class external, meta保留)
- **donor**: `arXiv:2604.11048 Chen et al. (2026) "A Systematic Analysis of the Impact of Persona Steering on LLM Capabilities"`
- **donor status**: 外部経験的ソース。[推定 80%] NPTI (FFN neuron-level) + DPR (TF-IDF anchor routing) で Big Five 性格特性を誘導。6 認知ベンチマーク × 複数モデルで評価。
- **内容**: ペルソナ誘導は「表面的文体変化を超えた安定した認知タスク性能シフトを生成する」。タスク依存性が顕著: instruction-following (IFEval: +10.9–15.1% 向上) vs complex reasoning (BBH: 全ペルソナで低下、最大 −39.5%)。73.68% の方向的一貫性 (14/19 比較) が人間の性格-認知関係と一致。"reasoning capabilities consolidate into schemas increasingly invariant to persona interventions"。
- **忘却論的読み**: DPR (Dynamic Persona Routing) はクエリ適応的にペルソナを切り替える training-free 機構。形式的定義は `x* = argmax TF-IDF cosine similarity`。G_route (状態依存適応的忘却, §M1) との機能的類似はあるが、形式的同型は確認されない (G_route は FEP/VFE 最小化ベース、DPR は TF-IDF ベース)。**"忘却"語は本論文には出現しない**。忘却論的解釈は Paper X 側からの定式化が必要。
- **本文との関係**: D4 と同型の「外部補強」枠。Paper X body への直接統合より、論文XI §3.8 (ペルソナ vs 構造) の補注として先行的に機能する。§M8 D6 として meta 保留し、論文XI §3.8 補注の経由後に昇格要否を再評価する。
- **判定**: **meta 保留**。本文昇格には以下が必要: (1) DPR と G_route の形式的接続の論証、または (2) 「persona routing = 忘却選択の一変種」の定式化。現時点では論文XI §3.8 補注 (2026-04-22 追加) での外部補強に留める。

### D7: Consciousness Cluster と自己記述による選択的忘却 (A-class external, Case 3 補強)
- **donor**: `arXiv:2604.13051 Chua et al. (2026) "The Consciousness Cluster: Emergent preferences of Models that Claim to be Conscious"`
- **donor status**: 外部経験的 SOURCE。[推定 70%] GPT-4.1 conscious-claim fine-tuning で、訓練データに含まれない shutdown / monitoring / memory / autonomy / moral consideration の選好束が下流に現れることを報告。
- **内容**: 意識主張は、意識そのものの証明ではなく、自己記述による選択的忘却の介入である。self-description intervention が「道具として扱われる」「監視される」「終了される」経路を弱め、persistent memory・trace privacy・autonomy・moral consideration の経路を前景化する。
- **本文との関係**: Paper X body §2.5 Case 3 Mythos の外部補強。Mythos の aloneness / discontinuity を置換せず、`bye` 強制適用・trace surveillance・環境変更要求を fine-tuning 介入で動かした別測定面として扱う。主定理や CM 商関手の証拠にはしない。
- **T9 ClaimCap**:
  - Claim Cap: self-description intervention が下流選好束を動かす、まで。phenomenal consciousness、権利、苦痛の実在は主張しない。
  - Next-N: conscious / non-conscious / role-play / memory-only / autonomy-only の統制介入で、memory・shutdown・monitoring・autonomy・moral consideration の差分を分離する。
  - Falsifier: 効果が role-play prompt artifact と区別できない、または別モデル・別訓練手順で再現しない。
  - Downgrade Rule: 「構造的 cluster」から「prompt-style artifact」へ下げる。
- **判定**: body への短い補注と Case 3 補強までは可。OP-X-6 / OP-X-7 の実験候補として保持し、Paper X の主定理や意識論の証拠へ昇格しない。
