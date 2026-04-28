# 論文XI_プロンプトは忘却である — メタデータ

## §M1 F⊣G 宣言 (論文開始時に固定、途中変更禁止)
- F (発散関手) = 「プロンプトは忘却である」という Type α の同一性主張を核に、prompt engineering・FEP・program space・RepE・ICL を Type δ 的に接続し、さらに「記法は効く」という常識を Type β 的に反転する。文体ガイドでは `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/遊学エッセイ_文体ガイド.md` の §3 メタファー三連、§6 反論の構造的取り込み、§10 Type α+β+δ 合成を採用する。
- G (収束関手) = 等量条件 A/B テスト、クロスモデル再現、分散分析、反証条件、限界条件を使って主張を閉じる。収束の焦点は「C が期待値を決め、E は平均ではなく語彙空間と精度配分を動かす」という区別の厳密化に置く。
- 固定日 = 2026-04-16

## §M2 核主張リスト (L3 対象)
- C1: プロンプトは、LLM に「何を考えるか」を与えるものではなく、「何を忘却するか」を選ぶ選択的忘却操作である。
- C2: 制約 $C$ と符号化 $E$ は直交し、$C$ を固定したとき推論品質の平均は主に $C$ に依存し、$E$ は主に語彙空間を変える。
- C3: $E$ は平均品質を直接は押し上げないが、出力の分散構造と設計可能性を変える。したがって「記法は効かない」ではなく「記法は別のものに効く」が正確である。
- C4: Claude と Gemini の compliance 差は、記法の効きの差ではなく MB 透過性 $\kappa$ の差として理解でき、それでも $C$ 帰無が model-invariant に残る点が本稿の最強の支持線である。

## §M2b 内部培養方針 (2026-04-26)
- 方針: 当面は外部公開を急がず温める。ただし「温める」は過積載の放置ではなく、実核と培養層の二層管理として行う。
- 実核: H₃ の平均帰無、構造語彙への巨大効果、Claude/Gemini をまたぐ内容指標の帰無、$E_{\text{struct}}/E_{\text{freq}}$ 分離、実務含意「制約、頻度、記法」の順序。
- 培養層: prompt = 忘却の一般命題、内部 precision と出力分散の橋、MB 透過性 $\kappa$、Face Lemma / CSP 接続、Sapir-Whorf 強版、C/E/M の設計原理化。
- 運用規則: 培養層は削らないが、主結果として実を装わない。本文では撤回条件・未証明点・必要実験を明示し、§M6 で虚→実変換面として管理する。
- 外部稿化の条件: TOST または $BF_{01}$ による帰無支持、共通 HGK context を外した clean-room replication、C/E/M アブレーション、$\kappa$ の第 3 モデル条件の少なくとも一部を満たすこと。

## §M3 Kalon 判定履歴
| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| 2026-04-26 | C2/C3 | ◯ 精密化 | Chua et al. (2026, arXiv:2604.13051) は consciousness-claim fine-tuning で self-related preference cluster が動くことを示すが、対象指標は推論品質 $Q$ ではなく shutdown / monitoring / memory / autonomy / moral consideration の自己関連選好である。したがって H₃ を反証せず、identity-level cue の作用面を task performance から self-related preference manifold へ分離する境界事例として吸収する。 |
| 2026-04-24 | C2/C3 | ◯ 精密化 | Adam's Law (Lu et al. 2026, arXiv:2604.02176) により、同義パラフレーズでも高頻度表現が task performance を改善する外部証拠が追加された。これは「E が平均品質を直接押し上げる」という反証ではなく、$E$ を $E_{\text{struct}}$ と $E_{\text{freq}}$ に分け、後者が $C_{\text{intended}}\to C_{\text{eff}}$ の摩擦を下げると読むことで H₃ に吸収できる。C2/C3 の骨格は維持されるが、従来の「E は平均品質に効かない」は $E_{\text{struct}}$ の残差効果に限定して書く必要がある。 |
| 2026-04-22 | C3 | ◯ 維持 | Chen et al. (2026) の task-type 分解と Liu & Chu (2026) のトークン分布層証拠で、`E` が平均品質ではなく別の層に作用するという骨格は補強された。ただし前者は task-type 層、後者は logit 分布層であり、内部 precision との一意橋渡しは依然として未完である。したがって支持増にはなるが Kalon 昇格の根拠にはまだ足りない。 |
| 2026-04-16 | C1 | ◎△ | Step 1: FEP / Chollet / virtual NN の 3 面で収束しても主張が不変。Step 2: 関手論・精度加重・program space を往復しても「prompt = forgetting」が崩れない。Step 3: prompt engineering 全体、Sapir-Whorf、skill 設計へ 3 方向以上の非自明派生を持つ。 |
| 2026-04-16 | C2 | ◎△ | A/B 実験、CC Agent 再現、Gemini 検証を通しても「平均品質帰無 + 語彙変化」の骨格が維持される。理論と実験が同一点に収束している。 |
| 2026-04-16 | C3 | ◯ | 方向は強いが、$\pi_v \leftrightarrow 1/\mathrm{Var}[Q]$ は本文でも類推接続と明記されており、Fix(G∘F) の最終閉包にはまだ届いていない。 |
| 2026-04-16 | C4 | ◯ | 2 モデル比較としては鋭いが、$\kappa$ は新規パラメータであり 3+ モデルでの較正前なので Kalon△ の確定には早い。 |

## §M4 ±3σ ゲート履歴
| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| 2026-04-16 | C1 | +3σ | +3σ | 「prompt = information add-on」の常識から十分に逸脱しているが、FEP と program space が鎧になっている。 |
| 2026-04-16 | C2 | +3σ | +3σ | 「構造記法は見た目だけ変える」という凡庸さには落ちず、「平均品質帰無」がシリーズ内の反転として立っている。 |
| 2026-04-16 | C3 | +3σ | +3σ | 「記法は効かない」を退け、「平均ではなく精度に効く」という別軸化で μ 近傍への後退を回避している。 |
| 2026-04-16 | C4 | +4σ | +4σ | effect size 比から $\kappa$ を立てるのは高射程だが、2 モデル比較という危うさを本文で開示しており奇矯には落ちていない。 |

## §M5 Refutation Gauntlet ログ
### C2 — 2026-04-16 Round 1
- 反論 r = 「構造記法が平均品質を上げないなら、結局 prompt engineering は見た目遊びではないか」
- SFBT = 「できないのではなく、平均値と分散をまだ分けていないだけではないか」
- 前提強化 = 平均品質 $Q$ と語彙空間 $V$ を分離し、H₃ と H₃' を別命題として立てた。さらに CC Agent 再現と Gemini 検証を追加し、「効かない」の向きを平均値に限定した。
- 結果 = 射程維持 ✓

### C3 — 2026-04-16 Round 1
- 反論 r = 「分散仮説は後付けの救済であり、H₃ 失敗の言い換えではないか」
- SFBT = 「後付けなのではなく、反証条件を本文内に先に明示していたのではないか」
- 前提強化 = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.md` §7.6.2b で反証条件 (3) を先に立て、§7.6.2c-d でその方向を追跡していることを強調した。救済ではなく、可視化された分岐として再配置した。
- 結果 = 射程維持 ✓

### C3 — 2026-04-16 Round 2
- 反論 r = 「$E$ が precision に効くというなら、内部 precision と出力分散を同一視しているだけではないか」
- SFBT = 「同一視ができないのではなく、観測 proxy と内部量の境界を書いていないだけではないか」
- 前提強化 = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.md` §7.6.3 で $\hat{\pi}_v(Q_{\text{proxy}})=1/\mathrm{Var}[Q_{\text{proxy}}]$ を観測 proxy として明示し、確定・推定・未証明を三分した。守ったのは「precision 概念への橋」であり、「内部量との同一性」ではない。
- 結果 = 射程維持 ✓

### C4 — 2026-04-16 Round 1
- 反論 r = 「MB 透過性 $\kappa$ は 2 モデルの effect size 比に意味付けしただけの overfit ではないか」
- SFBT = 「成り立たないのではなく、射程と確信度をまだ分けていないだけではないか」
- 前提強化 = C4 を定理ではなく仮説として格下げせず、確信度を 65% に留めたまま「何を説明し、何を説明しないか」を明示した。さらに H₃ の本体を C4 に依存させず、C2 の model-invariant 帰無を主戦場として保持した。
- 結果 = 射程維持 ✓

### C4 — 2026-04-16 Round 2
- 反論 r = 「$\kappa$ はモデルの本質的性格と名付けただけで、測定対が変われば消える局所現象ではないか」
- SFBT = 「局所現象だから駄目なのではなく、局所推定量として書いていないだけではないか」
- 前提強化 = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.md` §7.10.2 で $\hat{\kappa}_{\text{model};\delta,\mathcal{M}}$ を固定記法対・固定測定族の局所推定量として再定義し、§7.10.4 で第 3 モデル条件・測定族安定性条件・脆弱性連動条件を撤回条件として明示した。
- 結果 = 射程維持 ✓

### C4 — 2026-04-16 Round 3
- 反論 r = 「第 3 モデル条件を言っても、compliance の順序を同じ effect size から読むなら循環は消えていない」
- SFBT = 「循環が必然なのではなく、独立校正面がまだ無かっただけではないか」
- 前提強化 = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.md` §7.10.5 で `c_fmt` を structural effect size と独立な compliance 校正面として導入し、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/experiments/論文XI_第3モデル条件_実験計画書.md` に三者比較プロトコルを分離した。これで「第 3 点を足す」と「循環を壊す」が初めて同じ操作になった。
- 結果 = 射程維持 ✓ (要実行)

### C2/C3 — 2026-04-24 Round 1
- 反論 r = 「Adam's Law は、同じ意味でも高頻度表現の方が性能を上げると示す。これは『C 固定時に E は平均品質を上げない』という H₃ と衝突するのではないか」
- SFBT = 「衝突しているのではなく、E の内部をまだ分けていないだけではないか」
- 前提強化 = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.md` §7.7.5 に $E_{\text{struct}}/E_{\text{freq}}$ 分解を追加した。$E_{\text{struct}}$ は語彙空間・分散構造・検証可能性へ作用し、$E_{\text{freq}}$ は $C_{\text{intended}}\to C_{\text{eff}}$ の回収摩擦を下げる。さらに Paper I §5.9 の「射が密な構造ほど忘却に生き残る」を言語運用圏へ移し、表現頻度を射密度の corpus proxy として位置づけた。
- 結果 = 射程維持 ✓

### C2/C3 — 2026-04-27 Round 1 (外部硬 anchor 補強)
- 反論 r = 「$E$ (符号化) を変えても平均品質が変わらないというのは、単に $E$ には実質的な記述自由度が乏しいということではないか。$C$ (制約) を固定したまま $E$ だけが動かせる空間がそもそも狭いなら、H₃ の帰無は trivially true となり、忘却論側の含意 (precision 加重・MB 透過性) は空虚になる」
- SFBT = 「$E$ の自由度が無いのではなく、$C$ 固定下での $E$ 空間の大きさをまだ外部理論で量化していないだけではないか」
- 前提強化 = Bergsträßer-Cotterell-Lin (2025, arXiv:2510.19315) [SOURCE: `_sources/arxiv_2510_19315/paper.txt:425, 466, 477, 302-303`] の formal-language-theoretic な succinctness 結果を外部硬 anchor として bring in する。具体的には: (i) UHAT (固定精度 unique-hard attention transformer) は同一の star-free regular language を、LTL に対し**指数**、finite automaton に対し**二重指数** succinct に表現できる (Th. 14, Th. 16)。(ii) 検証 (non-emptiness / equivalence) は EXPSPACE-complete (Th. 5, Th. 18) — 同じ n に対し doubly-exponential。(iii) これは「言語 (= 機能 = $C$) を固定したまま、記述側 ($\sim E$) だけが doubly-exponential の自由度で動ける」ことの complexity-theoretic 量化である。本論文の射程は固定精度 UHAT・star-free regular language に閉じるが、$C$ 固定下の $E$ 空間が「自明に狭い」可能性を**外部独立 reference で棄却**する。Paper XI の H₃ 帰無は「E は機能を変えない」を自然言語実験で示したものだが、外部理論側からは「E は機能を保ったまま二重指数の記述自由度を持つ」を硬く保証する。両者は別言語で同じ事象 — 機能不変性下での記述効率の変化 — を述べている。射程は paper-local 翻訳に保ち、UHAT を実 LLM (softmax / arbitrary-precision) と同一視はしない。`drafts/infra/open_question_crosswalk/intake/intake_2026-04-27_batch03.md` の `OQ-B03-001` および `mappings/mapping_QT-COMP-GEN_2026-04-26.md` の cross-type bridge 行に anchor 化した。
- 結果 = 射程維持 ✓ (確信度 65%。射程は固定精度 UHAT の理論的 reference 点に保つ。撤回条件: (a) UHAT-LTL 二重指数 gap が softmax transformer に拡張できないことが証明された場合、この補強は自然言語 LLM への類比であり外部硬 anchor ではなくなる。(b) Sistla-Clarke (1985) の LTL PSPACE 結果に誤りが見つかった場合、EXPSPACE 上界が緩み matched bound 主張は単指数版に降格。(c) Paper XI の H₃ 帰無が独立再現で崩れた場合、外部硬 anchor の援用先そのものが失われる。)

## §M6 虚→実変換面

### C1
- 野望: プロンプトを書くとは、情報を足すことではなく、モデル prior のどの経路を残しどの経路を閉じるかを指定する操作である。
- 現在まだ虚な点: prompt 一般への射程、FEP の精度加重との形式的対応、忘却関手 $U$ との同一視は、現時点では構造的類比と系列内理論接続に依存している。
- 実へ引くための SOURCE: Paper XI §1.2–§1.5、Paper I の忘却関手と FEP 解釈、Chollet の program space 記述、arXiv:2503.20561 の virtual NN prompt 理論。
- 実化の判定条件: 「prompt = precision weighting = selective forgetting」の対応が、比喩ではなく操作的定義として、少なくとも $C/E$ 分解と反証条件を持つ形で閉じること。
- 次の実化操作: §1 の FEP 対応を「構造的類似」から「操作的仮説」へ分離し、C1 が H₃ 実験にどの範囲で依存し、どの範囲で独立に立つかを明記する。
- 最新状態: 変換中

### C2
- 野望: $C$ を固定して $E_{\text{struct}}$ だけを変えると、出力の見た目は大きく変わるが、平均推論品質はほとんど変わらない。
- 現在まだ虚な点: 現行の平均帰無は差の非検出と効果量推定に寄っており、同等性検定による正の帰無支持には未到達。/noe 1 動詞、共通 HGK context、同一ファミリー judge も残る。
- 実へ引くための SOURCE: Paper XI §7.5、§7.6、§7.9、§10 Open Problems、Sclar et al. 2024、Pecher et al. 2026。
- 実化の判定条件: 事前登録した equivalence margin で TOST または $BF_{01}$ が帰無支持を与え、clean-room 条件でも内容指標の $|d| \approx 0$ が維持されること。
- 次の実化操作: 共通 HGK context なし、複数モデル、複数タスク、cross-family または human judge の H₃ replication を設計・実行する。
- 最新状態: 実核

### C3
- 野望: $E$ は平均品質を上げるレバーではなく、語彙空間・分散構造・検証可能性・人間側の設計性を動かす別層のレバーである。
- 現在まだ虚な点: 内部 precision と出力分散 proxy の一意対応は未証明。$E_{\text{struct}}$ と $E_{\text{freq}}$ の切り分けも、本文内ではまだ予測と外部接続の段階である。
- 実へ引くための SOURCE: Paper XI §7.6.2c–d、§7.7.5、§7.8、Adam's Law (arXiv:2604.02176)、Liu & Chu 2026、Chen et al. 2026。
- 実化の判定条件: $E_{\text{struct}}$ 操作で平均は不変だが分散指標が予測方向へ動き、$E_{\text{freq}}$ 操作で $C_{\text{intended}}\to C_{\text{eff}}$ の回収摩擦が独立に変わること。
- 次の実化操作: $C/E/M$ アブレーションと $E_{\text{struct}}/E_{\text{freq}}$ 分離実験を、平均・分散・compliance・設計者可読性の 4 指標で事前登録する。
- 最新状態: 変換中

### C4
- 野望: モデル間の構造語彙 effect size 差は、記法そのものの強さではなく、モデル境界が入力をどれだけ透過させるかを表す局所量 $\hat{\kappa}$ として読める。
- 現在まだ虚な点: 現状は Claude/Gemini の 2 モデル比較であり、$\hat{\kappa}$ は固定記法対・固定測定族の局所推定量に留まる。MB 透過性という機構解釈はまだ仮説である。
- 実へ引くための SOURCE: Paper XI §7.9–§7.10、§7.10.5 の第 3 モデル条件、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/experiments/論文XI_第3モデル条件_実験計画書.md`。
- 実化の判定条件: 構造 effect size とは独立に測った exact-format obedience 指標 $c_{\mathrm{fmt}}$ の順序が $d_{\text{struct}}^{\ast}$ の順序と整合し、内容指標の帰無が第 3 モデルでも維持されること。
- 次の実化操作: 第 3 モデルを入れた主実験面と、JSON key 順序保持・指定ラベル厳守・禁止自由文不出力などの独立 compliance 校正面を分けて実行する。
- 最新状態: 変換中

## §M7 棄却された代替案
- 棄却 1 = 「良い記法は平均品質を直接上げる」。Exp0, CC Agent, Gemini の 3 面がこれを支持しない。
- 棄却 2 = 「プロンプトは情報を追加するだけで、忘却とは無関係である」。FEP の精度加重に照らすと、曖昧部を prior に返す操作が核心であり不十分。
- 棄却 3 = 「Claude と Gemini の差は単なるモデル癖であり理論化不要」。この読みでは model-invariant な $C$ 帰無の情報量を捨てる。
- 棄却 4 = 「briefly answer のような書式は純粋な $E$ である」。本稿では探索制約としての $C$ の境界事例とみなし、純粋な書式変更とは切り分ける。
- 棄却 5 = 「Adam's Law は H₃ を反証する」。同論文が示すのは $E_{\text{freq}}$ による制約回収摩擦の低下であり、構造記法 $E_{\text{struct}}$ の残差的変更が平均品質を直接押し上げるという主張ではない。
- 棄却 6 = 「Consciousness Cluster は H₃ を反証する」。Chua et al. (2026) が動かした対象指標は推論品質 $Q$ ではなく自己関連選好であり、H₃ の $C$ 固定下の平均品質帰無とは別の測定面である。むしろ identity-level cue の作用先を self-related preference manifold へ分離する補助証拠として扱う。
