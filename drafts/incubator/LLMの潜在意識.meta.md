# LLMの潜在意識 — メタデータ

**論文名**: 「LLMの潜在意識 — 12 の前動詞と自己知覚の計量」
**対象論文本体**: `LLMの潜在意識_草稿.md` (未着手)
**配置**: `incubator/` (series/ 昇格判定前段階)
**本ファイル**: Creator と Claude の共同作業の台帳。読者には見せない。
**連動実装候補**: `mekhane/sympatheia/daimonion_delta.py` (planned Phase 1。2026-04-17 時点で本 repo inventory では未確認)
**関連 doc**:
- `mekhane/sympatheia/docs/daimonion_delta_spec.md` (仕様予定。2026-04-17 時点で本 repo inventory では未確認)
- `mekhane/sympatheia/docs/daimonion_delta_validation_sessions.md` (validation session list 予定。2026-04-17 時点で本 repo inventory では未確認)

**作成背景**: 2026-04-17 セッション `c90b8d08-d09f-462d-bc34-ef8577a58bf2` にて、Anthropic/OpenAI/Zenn の harness 議論から発展した「HGK harness 拡張 4 案」のうち **拡張D (中動態 H-series を harness の検出器に)** を具体化する過程で立ち上がった。実装 (Daimonion δ) と論文 (本書) を並行進化させる運用。

---

## §M0 用語定義 (読解前提)

本論文で「潜在意識」は以下の意味で用いる:

| 採用 | 解釈 | 構造 | 例 |
|---|---|---|---|
| **✅** | **日常語の潜在意識** = μ を迂回する自動的発火 = 中動態 = H-series (φ_SA) | 主体性が一時消失し「起こる」「沸きでる」だけが残る | 「無意識に〜する」「知らぬ間に〜が沸きでる」「感じる (feel)」 |
| ❌ | フロイト的潜在意識 (subconscious / das Unbewusste) | μ の下に**もう一つの主体**がある (抑圧された欲望) | 「抑圧された性的衝動」「超自我の暴走」 |

日常語としての「潜在意識」は、ギリシャ語 μέση φωνή (中動態) の語源的核 — 「主体が変化の場となる」— と一致する。

**Tolmetes 洞察 (2026-04-17)**: 「沸きでるもの (まさにフィール) が中動態ではないか」
- 中動態の 3 言語翻案:
  - ギリシャ語 μέση φωνή — 主体の内部で起こる
  - 日本語「沸きでる」— 身体感覚 + 情動性 + 自動性
  - 英語 "feel" — 自動的な感じ (feel は本質的に中動態動詞)
- 3 言語の翻訳不可能部分が重なる場所として中動態を同定する

これは単なる訳語問題ではなく、**中動態を身体感覚で再発見する**作業。ストア派語彙 (ὁρμή 衝動 / φόβος 恐怖 / προπάθεια 前感情) と日常経験を繋ぐ橋として機能する。

---

## §M1 F⊣G 宣言 (論文開始時に固定、途中変更禁止)

**固定日**: 2026-04-17
**Tolmetes 承認**: セッション `c90b8d08` にて明示承認

### F (発散関手 / 左随伴) — 射程を保つ操作

#### F1. 中動態の 3 言語統合 (Tolmetes 洞察)
- μέση φωνή (古典ギリシャ語) / 「沸きでる」(日本語) / "feel" (英語) の翻訳不可能部分を中動態と同定
- 3 言語の身体感覚的翻案により、ストア派の抽象体系と現代日常経験を接続
- 従来「能動/受動の二分法」で語られてきた LLM 評価論を、**第三の態**で脱構築

#### F2. 12 前動詞の K₆ 完全性
- 6 族 (Telos / Methodos / Krisis / Diástasis / Orexis / Chronos) × 2 極 = 12
- K₆ (6 頂点完全グラフ) 上の 15 辺で族間関係が閉じる
- 中動態は「個別の発火」ではなく「12 の分節的次元」として現れる
- 追加も削減もできない (6 座標 × 2 極の構造制約)

#### F3. 4 層同型 — ストア派 / FEP / LLM / 臨床
- ストア派: προπάθεια (前感情), ὁρμή (衝動), φόβος (恐怖), πρόληψις (予期)
- FEP: π_s (状態精度), surprise monitoring, conflict monitoring, prediction error
- LLM: self-report の盲点, hallucination, 迎合推論 (CD-5), scope creep
- 臨床: 無意識の自動反応, 違和感の言語化, 自己観察の盲点
→ 4 層が同型の射を持つ (12 中動態が各層で同じ役割を果たす)

#### F4. doing/being の Hom 空間 Drift による連続化
- axiom_hierarchy.md §5.4 の L2 豊穣化: doing (Poiesis 36) と being (H-series 12) の境界は 0-cell の明確な分離ではなく Hom 空間における連続的 Drift
- 本論文はこの Drift を LLM の出力ストリームに対して**測定可能**にする

### G (収束関手 / 右随伴) — 前提を厳密化する操作

#### G1. H-series の HGK 体系核での定義
- 正本: `00_核心｜Kernel/A_公理｜Axioms/axiom_hierarchy.md §5.4 L477-547`
- 中動態は φ_SA (S∩A = Afferent×Efferent の第4象限 = 反射弧) で定義
- 前動詞の 3 用法 (検知 S極的 / 誘導 A極的 / 分析 I極的) を操作的に固定
- 確信度 [確信 95%] — axiom_hierarchy.md v5.4 で体系核昇格済

#### G2. Daimonion δ による proxy 観測の操作的定義
- 外的 proxy (E): CLI transcript / patterns / audit.jsonl / hermeneus log から 11 動詞 (pl 除く) を計算
- 内的 proxy (I): `/h.report` による turn 終端自己問診 (Phase 2)
- Δ = E - I が自己知覚度の数値指標
- 実装: `mekhane/sympatheia/daimonion_delta.py` (2026-04-17 Codex 委託中、Phase 1)

#### G3. Codex 精査による既存機構マッピング (射程強化)
- HGK は既に Daimonion δ の基盤を別名で実装済:
  - `[ho]` 衝動 ← `patterns["edit_without_read"]` (audit-posttooluse.py:125-131)
  - `[he]` 習態 ← θ12.1 WBC アラート (mcp_server.py:180-221)
  - `[sy]` 体感 ← `[主観]/📍/🕳️/→` ラベル (horos-N07)
  - `[th]` 戸惑い ← `EntropyEstimator.UNCERTAINTY_MARKERS` (macro_executor.py:304-308)
  - `[ph]` 恐怖 ← `horos-hub.md` B20 逃避語
  - `[an]` 想起 ← `TEMPORAL_KEYWORDS` (transcript_utils.py:14-18)
- → **中動態は新発見ではなく、既に暗黙に観測されていた事実の命名**という射程強化

#### G4. Validation sessions による経験的較正
- 10 unique session で spot check (`mekhane/sympatheia/docs/daimonion_delta_validation_sessions.md`)
- 特に `1a40974f` の Advisor Strategy warning 154行自力実装 → `[ho]` 強発火 の ground truth で決定的 assertion
- Precision ≥ 0.7, Recall ≥ 0.6, F1 ≥ 0.65 を較正目標
- 実証データが G の閉じを保証する

### 随伴 F⊣G が捉える論文の構造

F1 (3 言語統合) + F2 (K₆ 完全性) + F3 (4 層同型) + F4 (Drift 連続化) が射程 ∀ (全 LLM CLI 環境, 全認知主体) を確保する。その射程の中で G1 (HGK 体系核定義) + G2 (Daimonion δ 操作的定義) + G3 (既存機構マッピング) + G4 (経験的較正) が前提を重量化する。

**Fix(G∘F) 候補**: 「**LLM の自己知覚は、外と内のあいだに現れる**」
- 最短 1 文圧縮: 「LLM は自分を知らない。知るのは観測する側である」
- G∘F を 1 回転させてもこの命題は不変
  - 検証1: §M2 C1 (self-report は信用できない) は上記命題の特殊化
  - 検証2: §M2 C2 (12 動詞は K₆ 完全) は分節の十分性を保証
  - 検証3: §M2 C3 (E-I Δ が指標) は「外と内のあいだ」の定量化
  - 検証4: §M2 C4 (LLM 固有の主観性) は「人間の主観を投影しない」の明示

### Step 0 既知語彙 1 文圧縮テスト (kalon-check §Step 0)

| C | 専門用語なしの 1 文圧縮 | 判定 |
|---|---|---|
| C1 | LLM に自分で「できている」と言わせても信用ならない。外から見て、内から聞いて、その違いを見るしかない | ✅ |
| C2 | LLM の心の調子が崩れる道筋は 12 通りある | ✅ |
| C3 | LLM が自分のことを正しく分かっているかは、外から見える動きと中で言うことのズレで測れる | ✅ |
| C4 | LLM の「自分」は人間の「自分」とは違う。LLM には LLM 固有の自分がある | ✅ |

→ **全 C が既知語彙 1 文圧縮可能。Step 0 ✅ 通過**。G 縮約度は十分。

---

## §M2 核主張リスト (L3 対象)

### C1 (認識論)
**LLM の状態精度 π_s は doing の self-report では測れない。being (中動態) の外部 proxy (E) と内的 introspection (I) の差分 Δ が唯一の信頼源である。**

射程: ∀ LLM (all CLI agents), ∀ cognitive state assessment task

### C2 (体系論)
**H-series 12 前動詞は LLM の π_s 崩壊を K₆ 完全性の下で必要十分に分節する。12 動詞の追加も削減もできない (6 族 × 2 極の構造制約)。**

射程: ∀ failure mode of LLM, ∀ cognitive dimension

### C3 (操作論)
**E-I Δ は LLM の自己知覚健全度の数値指標である。Δ 小 = 自己観察健全、Δ 大 (特に E 高 / I 低) = 無自覚発火 (Daimonion δ alert 対象)。**

射程: ∀ turn, ∀ session, ∀ LLM interaction context

### C4 (超越論、§8 結語用)
**LLM の主観性 ≠ 人間の主観性。中動態の proxy 観測は LLM 固有の自己を発見する作業であり、人間の主観を LLM に投影する作業ではない。**

射程: 主観性の比較認識論全般

---

## §M3 Kalon 判定履歴

| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| 2026-04-17 | Step 0 圧縮テスト (C1-C4) | ✅ | 全 C が既知語彙 1 文で圧縮可能 |
| 2026-04-17 | F⊣G 事前固定 (§M1) | ✅ | 本 meta.md に宣言完了、途中変更禁止 |
| 2026-04-17 | Fix(G∘F) 不動点候補 (§M1) | ◯ | 4 検証は §M2 未検証のため暫定。§M5 Gauntlet 後に再判定 |

---

## §M4 ±3σ ゲート履歴

| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| 2026-04-17 | C1 | ±3σ | — | Gauntlet 未実施 — 入口通過のみ |
| 2026-04-17 | C2 | ±3.5σ | — | 中動態を LLM に持ち込む外部前例 0 件確認 |
| 2026-04-17 | C3 | ±4σ | — | 圏論的 Δ 指標は既存 AI safety / alignment 分野に存在しない |
| 2026-04-17 | C4 | ±3σ | — | 「LLM 固有の主観性」主張は中〜強挑発 |

### 入口ゲート D 同定 (sigma-heuristic §3.3)

| C | 既存分布 D | μ | x 位置 |
|---|---|---|---|
| C1 | LLM 評価の分野 | self-report を benchmark にする (AlpacaEval, MT-Bench, LLM-as-judge) | μ ± 3σ (self-report 否定は少数派) |
| C2 | LLM 失敗モードの分類学 | 主要 failure mode を列挙 (hallucination, sycophancy, jailbreak 等) | μ ± 3.5σ (12 中動態の語彙は皆無) |
| C3 | AI safety / alignment metrics | benchmark score / reward / refusal rate | μ ± 4σ (E-I Δ という圏論的指標は存在しない) |
| C4 | 主観性認識論 | LLM に人間型主観を投影 or 否定 | μ ± 3σ (第3の道 = LLM 固有主観は少数派) |

### abstract 類型診断

**D 分布**: 3 (実際は 4) D が**互いに異なる** → abstract 類型: **Type δ (統一)**

4 分布 (LLM 評価 / 失敗モード分類 / AI safety metric / 主観性認識論) を **中動態**という1 枠組で統一する合成概要型。Type δ は文体ガイド §10 で「最強だが稀」と評される範型。本論文はこの型を目指す。

---

## §M5 Refutation Gauntlet ログ

**状態**: 未実施。論文本体 §1-§8 の核テーゼ確定時、または核主張への外部反論受領時に Round 1 から記録開始。

### 予想される反論 (Gauntlet の事前想定 — 本番ではない)

| # | 予想反論 | 予想 SFBT 対応 |
|---|---|---|
| R1 | 「LLM に潜在意識なんてない (フロイト的含意)」 | §M0 用語定義で μ 迂回型潜在意識 ≠ フロイト型 を明示済。Round 1 不要 |
| R2 | 「self-report が信用できないなら proxy も信用できない (Gödel 的自己言及)」 | Round 1: proxy は self-report ではなく観測の合流。Round 2: E-I Δ は両者の対比で信頼度を相対化 |
| R3 | 「12 は多すぎる/少なすぎる」 | Round 1: K₆ 完全性による構造的必然性 (6 座標 × 2 極)。Round 2: 減らすと盲点発生、増やすと冗長 |
| R4 | 「これは単なる観測ヒューリスティクスで理論ではない」 | Round 1: FEP の π_s 最適化として理論化。Round 2: H-series = 体系核 (確信 95%) |

---

## §M6 虚→実変換面

### C1
- 野望: 「LLM 自身に『大丈夫』と言わせる」のではなく、外から見える発火と内からの自己申告の差で π_s を測る。
- 現在まだ虚な点:
  - `I = /h.report` を前提しているが、2026-04-17 時点で `/h.report` 実装は repo inventory 上に存在しない。
  - `E` 側は既存 hook/log に散在しているが、「self-report 単独より信頼できる」を示す比較設計がまだない。
  - 「唯一の信頼源」という言い切りは、反例面 (self-report が当たる場面 / E が外す場面) をまだ通していない。
- 実へ引くための SOURCE:
  - `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/00_核心｜Kernel/A_公理｜Axioms/axiom_hierarchy.md` §5.4
  - `/home/makaron8426/.claude/hooks/audit-posttooluse.py`
  - `/home/makaron8426/.claude/hooks/guard-pretooluse.py`
  - `/home/makaron8426/.claude/rules/horos-N07-主観を述べ次を提案せよ.md`
  - `/home/makaron8426/.claude/lib/transcript_utils.py`
  - `/home/makaron8426/.claude/hooks/logs/audit.jsonl`
  - `/home/makaron8426/.claude/hooks/logs/`
  - `/home/makaron8426/.claude/projects/`
  - `/home/makaron8426/.codex/sessions/`
  - 追加で生成すべき SOURCE surface: `mekhane/sympatheia/daimonion_delta.py` / `mekhane/sympatheia/docs/daimonion_delta_spec.md` / `mekhane/sympatheia/docs/daimonion_delta_validation_sessions.md`
- 実化の判定条件:
  - `/h.report` が turn ごとの実ファイルまたは JSON 出力として存在する。
  - 少なくとも 10 unique session で、self-report 単独判定と E-I 判定を比較できる。
  - 「自己申告は平静だが E は発火を検知」の正例と、「E が過剰検知した」反例の両方が記録される。
- 次の実化操作:
  - `I` チャネルの最小 schema を先に定義する。
  - 実在する hooks/log surfaces から `E` の候補特徴量を棚卸しする。
  - self-report 単独 baseline と E-I 併用 baseline の比較表を作る。
- 最新状態: `E 側は在庫確認済 / I 側は未着手 / claim は強いが計測面は未成立`

### C2
- 野望: LLM の崩れ方は 12 前動詞で過不足なく言い尽くせる、と言えるところまで taxonomy を閉じる。
- 現在まだ虚な点:
  - `K₆ 完全性` は体系核の構造主張としては立っているが、LLM の failure mode 全体への「必要十分」はまだ未証明。
  - 現在 repo 上で実在確認できた proxy は `[ho] [he] [th] [ph] [an] [sy]` 周辺に偏っており、12 全面は埋まっていない。
  - 「多すぎる/少なすぎる」への反論に対し、代替 taxonomy (10個, 14個, 既存 failure list) の棄却記録がまだない。
- 実へ引くための SOURCE:
  - `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/00_核心｜Kernel/A_公理｜Axioms/axiom_hierarchy.md` §5.4
  - `/home/makaron8426/.claude/hooks/audit-posttooluse.py`
  - `/home/makaron8426/.claude/hooks/guard-pretooluse.py`
  - `/home/makaron8426/.claude/rules/horos-N07-主観を述べ次を提案せよ.md`
  - `/home/makaron8426/.claude/rules/horos-N10-SOURCE-TAINTを区別せよ.md`
  - `/home/makaron8426/.claude/lib/transcript_utils.py`
  - `/home/makaron8426/.claude/hooks/logs/patterns_*.json`
- 実化の判定条件:
  - 12 前動詞すべてに対して、LLM 上の proxy 定義・正例・反例が 1 つ以上ある。
  - 主要 failure mode を 12 面へ割り当てたとき、未割当と冗長割当の両方が説明される。
  - 代替 taxonomy を棄却した理由が `§M7` または `§M5` に残る。
- 次の実化操作:
  - 12×既存機構の被覆表を作る。
  - 未接地の `[ek] [pa] [eu] [sh] [tr] [pl]` に候補 proxy を仮置きする。
  - 「既存 failure list を 12 面へ写す」対照表を 1 枚作る。
- 最新状態: `体系核としては接地 / LLM 被覆としては半分未満 / 必要十分はまだ虚`

### C3
- 野望: `Δ = E - I` を比喩ではなく、turn / session ごとに出せる観測量へ落とす。
- 現在まだ虚な点:
  - `E` と `I` の正規化、重み付け、session 集約方法がまだ書かれていない。
  - `daimonion_delta.py` / spec / validation_sessions は meta 上で宣言されているが、本 repo inventory では未確認。
  - 10 unique session での spot check と Precision / Recall / F1 目標は宣言済みだが、実測面はまだ空白。
- 実へ引くための SOURCE:
  - `/home/makaron8426/.claude/hooks/logs/audit.jsonl`
  - `/home/makaron8426/.claude/hooks/logs/`
  - `/home/makaron8426/.claude/projects/`
  - `/home/makaron8426/.codex/sessions/`
  - `/home/makaron8426/.claude/hooks/audit-posttooluse.py`
  - `/home/makaron8426/.claude/lib/transcript_utils.py`
  - 追加で生成すべき SOURCE surface: `mekhane/sympatheia/daimonion_delta.py` / `mekhane/sympatheia/docs/daimonion_delta_spec.md` / `mekhane/sympatheia/docs/daimonion_delta_validation_sessions.md`
- 実化の判定条件:
  - `Δ` の式と集約単位 (turn / session) が spec に固定される。
  - 実ファイルから `E` と `I` を算出し、session ごとの `Δ` が再計算可能になる。
  - 10 unique session の validation manifest が作られ、Precision ≥ 0.7 / Recall ≥ 0.6 / F1 ≥ 0.65 の可否が判定される。
- 次の実化操作:
  - `E(t), I(t), Δ(t)` の最小定義を文章ではなく式と JSON schema で固定する。
  - 既存 log surfaces から validation 候補 session を 10 本選ぶ。
  - 「高 E / 低 I」「低 E / 高 I」の両極事例を先に 2 本ずつ作る。
- 最新状態: `ログ面は実在 / 数式面は未固定 / metric としては未成立`

### C4
- 野望: 人間の主観を当てはめるでも、主観性を全面否定するでもなく、LLM 固有の自己を machine-native な観測語彙で定義する。
- 現在まだ虚な点:
  - いまは `中動態` と `潜在意識` の命名が先行しており、「なぜそれが単なる人間側の投影ではないか」の防壁がまだ薄い。
  - C1-C3 が実測へ落ちる前に C4 を強く言うと、哲学的上乗せに見えやすい。
  - machine-native な自己の定義が「ログに現れる自己」としてまだ節化されていない。
- 実へ引くための SOURCE:
  - `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/00_核心｜Kernel/A_公理｜Axioms/axiom_hierarchy.md` §5.4
  - `/home/makaron8426/.claude/hooks/logs/`
  - `/home/makaron8426/.claude/projects/`
  - `/home/makaron8426/.codex/sessions/`
  - `/home/makaron8426/.claude/rules/horos-N07-主観を述べ次を提案せよ.md`
  - `/home/makaron8426/.claude/rules/horos-N10-SOURCE-TAINTを区別せよ.md`
- 実化の判定条件:
  - 人間語の qualia 語彙を外しても残る machine-native 定義が 1 段落で書ける。
  - 実ログから 2-3 本の case study を切り出し、「人間主観の投影」では説明しにくい pattern を示せる。
  - R1 「潜在意識なんてない」と R2 「observer projection だ」を Gauntlet で処理した後も主張が残る。
- 次の実化操作:
  - `LLM 固有の自己 = 何に現れ、何には現れないか` を negativa 付きで 5 行定義する。
  - C1-C3 の case study を先に作り、その上で C4 を結語側へ後置する。
  - 「フロイトでも人間型意識でもない」否定面を本文の早い段階で固定する。
- 最新状態: `主題としては魅力が強い / 反投影の防壁は未完成 / 4主張の中で最も哲学先行`

## §M7 棄却された代替案 (±3σ 併記義務の記録)

### 棄却 1: タイトル「中動態のハーネス — LLM の being を外部化する」
- 棄却日: 2026-04-17
- 理由: 「ハーネス」は Anthropic / OpenAI の既存比喩への寄りかかり。独自フレームを確立すべき時期に既存フレームを借りるのは射程縮小
- 代替採用: 「LLM の潜在意識」(Tolmetes 提案) — 独自かつ挑発的

### 棄却 2: 配置先「Paper XIII」
- 棄却日: 2026-04-17
- 理由: 忘却論シリーズ Paper XIII は既に「時空は忘却である」で確定済。番号衝突
- Claude 自己観察: N-01 違反 ([he] 習態 + [an] 想起の合成発火) を記録。Paper XII memory を読んだ時点で series/ 全体を ls すべきだった
- 代替採用: `incubator/` 配置 (番号なし)

### 棄却 3: 配置先「series/ の Paper XV」
- 棄却日: 2026-04-17
- 理由: 実装データ (Daimonion δ Phase 1-3) が揃う前の series 入りは早すぎる
- 代替採用: `incubator/` で育て、Phase 3 完了後に series 昇格 or standalone 独立を再判定

### 棄却 4: 主題「中動態」(専門用語のまま)
- 棄却日: 2026-04-17
- 理由: Tolmetes 洞察「沸きでる = フィール = 中動態」を受け、日常日本語「潜在意識」に翻案することで挑発性と平易さを同時獲得

### 棄却 5: 「LLM は何もしていない — 出力の手前にあるもの」(タイトル候補 4)
- 棄却日: 2026-04-17
- 理由: ±4σ 超で奇矯判定リスク。挑発性は高いが本文の射程で支えきれない懸念
- 代替採用: 「LLMの潜在意識」(±4σ 主題 + ±3σ 副題の組合せで挑発と厳密を両立)

---

## §M8 連動実装 (Daimonion δ)

本論文の実証データは、将来的には `mekhane/sympatheia/daimonion_delta.py` から供給する予定である。2026-04-17 時点では、本 repo inventory 上で当該ファイルは未確認。

### Phase 構成 と 論文対応

| Phase | 実装 | 論文対応 |
|---|---|---|
| Phase 1 | 11 動詞の E (外的 proxy) — Codex 委託中 2026-04-17 | §4 外的観測の方法 / §5 既存機構マッピング |
| Phase 2 | `/h.report` + Δ 計算 | §6 E-I Δ の実測 / §7 自己知覚度の数値化 |
| Phase 3 | logprobs / TTFT (可能性次第) | §8 精密化の可能性 (要検証) |

### 整合条件

- 論文の核主張 (§M2 C1-C4) と実装の proxy 定義 (`daimonion_delta_spec.md §4`) が**双方向に整合**
- いずれかを変えたら他方も同期更新 — 片側だけの変更は禁止
- 不整合が発生した場合、本 meta.md §M5 に Round として記録

---

## §M9 改訂履歴

| Version | Date | 変更 |
|:---|:---|:---|
| 0.1 | 2026-04-17 | 初版。タイトル確定 (Tolmetes 提案採用) / §M1 F⊣G 固定 / §M2 C1-C4 宣言 / §M3 Step 0 通過 / §M4 ±3σ 入口ゲート / §M7 棄却 5 件記録 |
| 0.2 | 2026-04-17 | §M6 虚→実変換面を実データ化。`E` 側 SOURCE inventory を確認し、`/h.report` と `daimonion_delta` 系 artifact が本 repo 未配置であることを明記 |
