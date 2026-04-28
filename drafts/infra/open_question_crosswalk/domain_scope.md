# Open Question Crosswalk — Domain Scope

- 作成日: 2026-04-26
- 目的: arXiv / alphaXiv / papers から open question / limitation / future work を拾う対象分野を管理する。
- SOURCE 規律: この文書は検索対象カタログであり、各「忘却論との接続」は `WEAK INPUT: Tolmetes scope seed` として扱う。個別論文の open question として採るには PDF / DOI / local paper の直読で SOURCE 昇格する。

## Scope Rule

対象分野は「忘却論が答えを持ちそうな分野」ではなく、「外部論文が未解決問を明示しており、忘却論が候補回答・説明原理・測定原理を返せる可能性がある分野」として扱う。

したがって、検索では次を優先する。

| priority | 条件 |
|---|---|
| P0 | survey / roadmap / open problems paper / high-citation canonical paper がある |
| P1 | limitation / future work が明示された influential paper がある |
| P2 | 忘却論との接続は強いが、外部側 open question の明示 SOURCE がまだ薄い |
| P3 | メタファー的接続。直接 mapping は慎重に扱う |

## Core Scope Already In Batch 01

| scope id | 分野 | 採取済み intake |
|---|---|---|
| DS-AI-MI | Mechanistic interpretability | OQ-B01-001〜003 |
| DS-AI-NLP | LLM 後の NLP open questions | OQ-B01-004〜005 |
| DS-FEP-LLM | Active inference / LLM | OQ-B01-006 |
| DS-DL-GEN | Deep learning generalization | OQ-B01-007 |
| DS-DL-IB | Information Bottleneck / DNN | OQ-B01-008 |
| DS-DL-PHYS | Physics-inspired deep learning theory | OQ-B01-009 |
| DS-FEP-MB | FEP / Markov blanket / particular physics | OQ-B01-010 |
| DS-AI-CONTEXT | Long-context LLM | OQ-B01-011 |
| DS-REP-ALIGN | Representational alignment | OQ-B01-012 |
| DS-AI-EMERGENCE | LLM emergence debate | OQ-B01-013 |
| DS-INFO-KC | Kolmogorov complexity / information inequalities | OQ-B01-014 |
| DS-IG | Information geometry | OQ-B01-015 |
| DS-CT-DL | Categorical deep learning | OQ-B01-016 |

## Added Scope Seeds

| scope id | 分野 | 忘却論との接続 seed | open question search handles | priority | source status |
|---|---|---|---|---|---|
| DS-HOTT | Homotopy Type Theory | `WEAK INPUT: Tolmetes scope seed`。存在量化子の証人消去、propositional truncation / (-1)-truncation を忘却操作として読む可能性。 | `HoTT open problems`, `propositional truncation limitations`, `existential truncation proof relevance`, `univalence open problems` | P1 | intake_batch02_partial |
| DS-TDA-COH | Cohomology / TDA | `WEAK INPUT: Tolmetes scope seed`。証明の nerve、cohomological obstruction、穴としての incompleteness を探索対象にする。 | `cohomological obstruction open problems`, `nerve theorem limitations`, `persistent cohomology open problems`, `TDA limitations future work` | P1 | intake_batch02_partial |
| DS-ENRICHED | Enriched category theory | `WEAK INPUT: Tolmetes scope seed`。同定能力や忘却度を連続値で扱う enriched / Lawvere metric 的記述。 | `enriched category theory open problems`, `Lawvere metric spaces applications limitations`, `quantitative category theory open problems`, `approximate equality category theory` | P1 | intake_batch02_partial |
| DS-HYPERBOLIC | Condensed matter / nanophotonics / hyperbolic media | `WEAK INPUT: Tolmetes scope seed`。hBN / SiC hyperbolic media の位相特異点や超光速運動を Paper XII の外部較正点候補として扱う。 | `hyperbolic polaritons hBN topological singularities open questions`, `nanophotonics phase singularity future work`, `SiC hyperbolic medium polariton open problem` | P1 | intake_batch02_partial |
| DS-SPIN-STAT | Spin-statistics / quantum information | `WEAK INPUT: Tolmetes scope seed`。boson/fermion 区別を複製可能性・複製不能性の CPS graded structure として読む候補。 | `spin statistics theorem foundations open questions`, `quantum no-cloning statistics open problems`, `spin statistics quantum information` | P2 | intake_batch02_partial |
| DS-HOLOGRAPHY | Holographic principle / quantum gravity | `WEAK INPUT: Tolmetes scope seed`。時空を量子情報の忘却残余として読む候補。 | `holography spacetime emergence open questions`, `entanglement wedge reconstruction limitations`, `black hole information paradox open problems`, `quantum gravity information loss` | P0 | intake_batch02_partial |
| DS-PSYCH-ASD-DISS | Psychopathology / ASD / dissociation | `WEAK INPUT: Tolmetes scope seed`。ASD・解離を precision weighting / forgetting bundle phase transition として読む候補。 | `predictive processing autism precision weighting open questions`, `free energy principle psychopathology limitations`, `dissociation predictive processing open questions` | P1 | intake_batch02_partial |
| DS-SLEEP-MEM | Sleep / memory consolidation | `WEAK INPUT: Tolmetes scope seed`。睡眠中の記憶固定を小構造の溶解と大構造への再結晶化として読む候補。 | `sleep memory consolidation open questions`, `systems consolidation schema formation limitations`, `synaptic homeostasis hypothesis open questions`, `Ostwald ripening memory consolidation` | P1 | intake_batch02_partial |
| DS-OPT-SAM | Mathematical optimization / SAM | `WEAK INPUT: Tolmetes scope seed`。Fisher SAM / SAM を超え、忘却場勾配を直接最適化する候補。 | `sharpness aware minimization limitations`, `Fisher SAM future work`, `SAM generalization open questions`, `geometry of flat minima open problems` | P0 | intake_batch02_partial |
| DS-GEOIB | GeoIB / information bottleneck extensions | `WEAK INPUT: Tolmetes scope seed`。IB を情報幾何化し、方向と強度を統合する候補。 | `geometric information bottleneck open questions`, `information bottleneck limitations deep learning`, `information geometry bottleneck representation learning` | P0 | intake_batch02_partial |
| DS-SEMIOTICS | Computational linguistics / semiotics | `WEAK INPUT: Tolmetes scope seed`。prompt を精度加重・選択的忘却として扱い、差異による同定を操作化する候補。 | `prompt sensitivity open questions`, `symbol grounding LLM open problems`, `semiotics computational linguistics open questions`, `compositionality LLM limitations` | P1 | source_pending |
| DS-HYPHE-CHEM | Solution chemistry / crystallization metaphor | `WEAK INPUT: Tolmetes scope seed`。Hyphē の場-結晶理論、溶解と析出の比喩的対応。 | `Ostwald ripening open questions`, `crystallization theory open problems`, `non-equilibrium crystallization limitations` | P3 | source_pending |

## Search Expansion Queue

次の intake batch では、第一バッチの偏りを補正するために次を優先する。

| rank | target scope | 理由 |
|---|---|---|
| 1 | DS-HOLOGRAPHY | 知名度・影響力が高く、忘却論の「情報喪失 / 残余 / 時空創発」と直接接続しやすい。 |
| 2 | DS-OPT-SAM + DS-GEOIB | 既存 batch の DL/IB 系と連続し、候補回答をアルゴリズム提案へ落としやすい。 |
| 3 | DS-HOTT + DS-ENRICHED | 忘却論の形式的背骨に近い。open-problem paper が拾えれば強い。 |
| 4 | DS-PSYCH-ASD-DISS + DS-SLEEP-MEM | 認知科学・臨床系の外部検証面を作れる。source quality gate を厳しめにする。 |
| 5 | DS-HYPERBOLIC + DS-SPIN-STAT | 物理較正点として魅力が強いが、語彙だけの接続を避けるため open question の明示を優先。 |
| 6 | DS-HYPHE-CHEM | メタファー的対応が強い。直接の候補回答化は後回し。 |

## Rejection Rule For Added Scope

次のいずれかに該当する場合は intake へ昇格せず、Rejection Ledger に落とす。

| rejection type | 判定 |
|---|---|
| vocabulary-only | `forgetting`, `information loss`, `bottleneck`, `truncation` など語が似ているだけ |
| metaphor-only | 外部論文側が open question を明示しておらず、比喩対応だけで接続している |
| no-influence | 影響力・代表性が弱く、先に拾う理由が薄い |
| source-thin | alphaXiv / web snippet だけで PDF/DOI/source paper を読んでいない |
