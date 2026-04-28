# OQ-B03-001 Child Split — a/b/c/d

- 作成日: 2026-04-27
- 親 OQ: `OQ-B03-001` (Bergsträßer-Cotterell-Lin 2025, arXiv:2510.19315)
- 分割根拠: `typing/typing_2026-04-27_batch03.md` Phase 4 Split Queue
- SOURCE 正本: `_sources/arxiv_2510_19315/paper.txt`
- status: `split_registered`
- 目的: OQ-B03-001 の 4 つの独立した未解決問を個別 OQ として登録し、型・anchor・grade・次操作を確定する。

---

## Split Rationale

親 OQ-B03-001 は UHAT の succinctness と EXPSPACE 検証を単一エントリとして採取したが、4 つの問いは独立したリサーチ方向を持つ。splitting しないと anchor 精度が下がる。

| child | 分割切り口 | 独立性の根拠 |
|---|---|---|
| a | 実機検証ツール化 (practical verification) | EXPSPACE-complete でも practical に解ける可能性は別問題。計算複雑度の上限が実用的 feasibility を決めない。 |
| b | softmax / arbitrary-precision への拡張 | UHAT (AC⁰) の結果が weakest class 専用。softmax (AC⁰ 超) への拡張は別の complexity result が必要。 |
| c | star-free 閉じ込みを越える言語クラス | UHAT は star-free regular のみ。RNN 以上 (full regular, context-free 等) への succinctness 理論は未存在。 |
| d | Zipf / Hindu-Arabic 哲学的接続 | 著者自身が formal claim を控えた philosophical note。忘却論側からは強い prior。形式 → 概念の bridge として独立採取。 |

---

## Child OQ 登録表

### OQ-B03-001a — Practical Verification Tools

| 項目 | 内容 |
|---|---|
| **外部問い** | EXPSPACE-complete な UHAT 検証を、実機で解くための symbolic technique / simulation が存在するか |
| **evidence** | SOURCE: `paper.txt:521-531` — "Despite the rather high complexity (EXPSPACE-complete), we pose as a challenge to exploit techniques from automated verification (Clarke et al., 2018) (e.g. symbolic techniques, simulation, etc.) to verify transformers in practice." |
| **問いの型** | `QT-FORMAL-VERIF` primary |
| **忘却論 anchor 候補** | `II-T3.4.1` (Face Lemma: face 保存 criterion が tractable サブ問題を定義する可能性) / `II-Stability-Simplex` (verification が成立する構造的条件) / `IX-P3.5.1` (critical threshold: EXPSPACE 内でも feasible な部分域) |
| **候補回答型** | structural feasibility criterion (conjecture) |
| **grade** | C+ — face criterion が tractable verification に対応するかは未確立。比喩化リスク高。 |
| **撤回条件** | UHAT verification の EXPSPACE-hardness が average-case でも保たれることが証明された場合 |
| **次操作** | Paper II の II-T3.4.1 を精読し、「face 保存で tractable に縮退する部分問題の条件」を確認してから case 化判断。 |

---

### OQ-B03-001b — Softmax / Arbitrary-Precision Extension

| 項目 | 内容 |
|---|---|
| **外部問い** | UHAT (AC⁰・固定精度) での succinctness doubly-exponential gap が、softmax attention (AC⁰ 超) や arbitrary-precision へ拡張できるか |
| **evidence** | SOURCE: `paper.txt:84-93` — "We also use Unique-Hard Attention Transformers (UHAT), which are known to be expressively the weakest class of transformers… other classes of transformers (e.g. average-hard attention or softmax) can recognize languages beyond AC⁰ (e.g. majority)." |
| **問いの型** | `QT-FORMAL-VERIF` primary |
| **忘却論 anchor 候補** | `IX-T1` (CPS entropy monotonicity: 圧縮容量が増えるほど N-side コストが増えるという定性的予測 — loose) / `VI-D2.1.1` (U⊣N 随伴: より強力な U 側がより大きい N-side を要求するという構造的類推) |
| **候補回答型** | qualitative structural prediction (loose) — 定量的な complexity result は 忘却論側には存在しない |
| **grade** | C — 忘却論の anchor は conceptual bridge のみ。独立した complexity-theoretic 結果が外部に必要。 |
| **撤回条件** | softmax での succinctness gap が UHAT より小さいことが証明された場合 (U⊣N 定性予測が崩れる) |
| **次操作** | Sälzer et al. (2025) NEXP-hard (batch03 intake で言及) を個別採取して b のより強い upper bound として利用できるか確認。 |

---

### OQ-B03-001c — Star-Free 閉じ込みを越える言語クラス

| 項目 | 内容 |
|---|---|
| **外部問い** | UHAT が認識する言語クラスは star-free regular (= counter-free automata, AC⁰) に限定される。RNN (full regular) / context-free / それ以上に succinctness 理論を拡張できるか |
| **evidence** | SOURCE: `paper.txt:477` — "Corollary 17. UHATs can be exponentially more succinct than RNNs." (RNN = full regular で exponential 差。DFA に対しては doubly-exponential) / SOURCE: `paper.txt:470-476` — counter-free automata = LTL = UHAT の言語クラスを確認する文脈 |
| **問いの型** | `QT-COMP-GEN` primary + `QT-FORMAL-VERIF` secondary |
| **忘却論 anchor 候補** | `IX-D2/IX-T1` (CPS entropy: 言語クラスが広がると encoding の entropy 構造が変わり N-side 単調性の適用域も変わる — loose) / `VIII-D6.2.1/T6.2.3` (α-忘却濾過: α 段階が言語クラスの階層に対応する可能性 — highly speculative) |
| **候補回答型** | language-class entropy bridge (highly loose) |
| **grade** | C — 言語クラス拡張は純粋な形式言語理論 debt。忘却論の直接 anchor が薄い。QT-COMP-GEN への委譲が適切。 |
| **撤回条件** | 特になし (conjecture 段階のため) |
| **次操作** | Jerad et al. (2025) LTL fragment (batch03 intake 言及) を採取し、UHAT の star-free より少し広い fragment の succinctness gap を OQ-B03-001c の intermediate step として使えるか確認。 |

---

### OQ-B03-001d — Zipf / Hindu-Arabic 哲学的接続

| 項目 | 内容 |
|---|---|
| **外部問い** | UHAT succinctness の形式的結果は、Zipf の略語法則 (高頻度概念 = 短い記述) や Hindu-Arabic vs Roman 数字 (指数的 succinctness = 現代数学・計算機科学を可能にした) と同型か。「記述効率が認知と文明を可能にする」という命題に formal grounding を与えられるか |
| **evidence** | SOURCE: `paper.txt:515-519` — "according to Zipf's law of abbreviation (Zipf, 1935), frequently occurring concepts tend to have a succinct description. In particular, Hindu-Arabic numeral system… allows an exponentially more succinct description than the Roman numeral system. According to Zipf's law, the former potentially enables mathematics and computer science as we see today." (著者自身が claim level を控えて philosophical note として置いている) |
| **問いの型** | `QT-SYN-SEM` primary + `QT-COMP-GEN` secondary |
| **忘却論 anchor 候補** | `I-T5.1` (方向性定理: 忘却の方向性 = 高頻度構造を保存し冗長を捨てる → Zipf の逆向き射影と同型) / `IX-D2/IX-T1` (CPS entropy: 高頻度概念の succinctness = entropy が低い = U が選択的に進んだ結果) / Paper XI `$E_{\text{struct}}$` (構造記法の自由度 = Zipf-type succinctness が働く層) |
| **候補回答型** | conceptual bridge — U as selective forgetting that preserves high-frequency structure (Zipf 過程の 忘却論的読み替え) |
| **grade** | B- — U⊣N の概念的接続は強い。ただし外部経験的証拠 ≠ 忘却論の theorem。claim level は「prior として強い」止まり。 |
| **撤回条件** | Zipf の法則が forgetting-based selection で説明されず、別機構 (e.g. communication efficiency alone) で完結することが示された場合 |
| **次操作** | Paper XI §M5/§M6 の C-E 分離と $E_{\text{struct}}$ を精読し、Zipf 接続を QT-SYN-SEM mapping の新 OQ として登録。typing_2026-04-27_batch03 の rank 2 (QT-SYN-SEM anchor 探索) の具体化として扱う。 |

---

## Type Distribution (children)

| child | primary type | secondary type | lane |
|---|---|---|---|
| OQ-B03-001a | QT-FORMAL-VERIF | — | mapping_QT-FORMAL-VERIF_2026-04-27 (登録済み carry-forward) |
| OQ-B03-001b | QT-FORMAL-VERIF | — | mapping_QT-FORMAL-VERIF_2026-04-27 (debt — Sälzer et al. 採取後) |
| OQ-B03-001c | QT-COMP-GEN | QT-FORMAL-VERIF | mapping_QT-COMP-GEN (language class bridge として追記対象) |
| OQ-B03-001d | QT-SYN-SEM | QT-COMP-GEN | QT-SYN-SEM mapping 新規起票時の primary 候補 |

---

## Rejection Ledger

| rejected | 理由 |
|---|---|
| OQ-B03-001a を II-T3.4.1 で「直接 tractable に解ける」と結論する mapping | Face Lemma は face 保存の必要条件を与えるが、EXPSPACE-complete な UHAT verification 問題が face 保存 criterion によって tractable サブクラスに縮退することは証明されていない。conjecture のまま保持。 |
| OQ-B03-001b の IX-T1 を「softmax でも doubly-exponential が成立する」の正当化に使う | CPS entropy monotonicity は compression 量と N-side コストの単調性を与えるが、UHAT 特有の doubly-exponential gap を softmax に継承する complexity argument ではない。定性的予測止まり。 |
| OQ-B03-001d を 忘却論の「証明済み主張」として外部 contact に使う | 著者自身が claim level を抑えた philosophical note。忘却論 anchor (I-T5.1, IX-T1) は conceptual bridge であり、外部 contact 論文の正当化には追加の formal grounding が必要。 |

---

## Carry Forward

| rank | target | 理由 |
|---|---|---|
| 1 | OQ-B03-001d → QT-SYN-SEM mapping | B- grade で最も 忘却論 への接続が強い。Paper XI C-E 分離との対照が typing rank 2 として予告されていた。QT-SYN-SEM mapping の新規起票時に primary 候補。 |
| 2 | OQ-B03-001a → case 化 (II-T3.4.1 精読後) | Face Lemma の operational 解釈次第で C+ → B 昇格の可能性。mechanistic interpretability (OQ-B01-002) との並列案件として case 起票。 |
| 3 | OQ-B03-001c → mapping_QT-COMP-GEN 追記 | Jerad et al. (2025) LTL fragment を採取した上で、言語クラス間 succinctness gap の 忘却論 entropy bridge として mapping_QT-COMP-GEN に cross-type 行として追記。 |
| 4 | OQ-B03-001b → debt 保持 | Sälzer et al. (2025) NEXP-hard を個別 OQ として採取してから b の upper bound context を確定。現状は C grade debt のまま。 |
