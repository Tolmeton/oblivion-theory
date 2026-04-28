# Open Question Crosswalk — Intake Batch 01

- 作成日: 2026-04-26
- 目的: 影響力のある arXiv / papers から、忘却論対応づけ前の open question / limitation / future work を拾う。
- 範囲: 第一バッチ。AI/LLM・深層学習理論を厚めにしつつ、FEP/物理、情報理論、情報幾何、圏論的DLまで広げる。
- SOURCE 規律: 下表は arXiv PDF をローカルで `pdftotext -layout` 抽出して確認したものだけを SOURCE とする。alphaXiv は候補探索 TAINT としてのみ使い、確定根拠には使っていない。
- まだ行わないこと: 問いの型分類、忘却論 theorem/proposition/concept への対応づけ、contact 判断。

## Intake Table

| ID | source | 分野 | 影響力の理由 | 拾った open question / limitation | evidence |
|---|---|---|---|---|---|
| OQ-B01-001 | [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) | AI / interpretability | Mechanistic interpretability の open-problem roadmap | feature の正体、network decomposition、superposition 仮説の理論的基礎が未確立。 | SOURCE: `/tmp/oqc_papers_20260426/2501.16496.txt:655-666` |
| OQ-B01-002 | [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) | AI / verification | frontier AI safety と formal verification を接続する代表的 open-problem paper | toy model 的解析を frontier system の formal verification へ拡張できるか。現実のNN計算を symbolic code へ還元できる範囲も未確定。 | SOURCE: `/tmp/oqc_papers_20260426/2501.16496.txt:1514-1525` |
| OQ-B01-003 | [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) | AI / architecture transfer | Transformer 偏重の MI を他 architecture / modality へ移せるかという実務上の中心問題 | interpretability findings/methods が CNN/BERT/GPT 以外、diffusion/SSM/multimodal へ一般化するか。 | SOURCE: `/tmp/oqc_papers_20260426/2501.16496.txt:1634-1649` |
| OQ-B01-004 | [Has It All Been Solved? Open NLP Research Questions Not Solved by Large Language Models](https://arxiv.org/abs/2305.12544) | NLP / LLM | LLM 後の NLP open-question agenda | LLM で解決されていない open research questions を、fundamental / responsible / applied NLP の3群・14 topicsとして残している。 | SOURCE: `/tmp/oqc_papers_20260426/2305.12544.txt:121-135` |
| OQ-B01-005 | [Has It All Been Solved?](https://arxiv.org/abs/2305.12544) | NLP / reasoning / grounding | LLM能力評価の中心争点を明示 | memorized pattern が reasoning/knowledge と呼べるか、data contamination や Goodhart 化の下で reasoning skill をどう測るか。modalities の融合も open problem。 | SOURCE: `/tmp/oqc_papers_20260426/2305.12544.txt:229-243` |
| OQ-B01-006 | [Predictive Minds: LLMs As Atypical Active Inference Agents](https://arxiv.org/abs/2311.10215) | FEP / active inference / LLM | LLM を active inference agent として読む bridge paper | LLM の action-perception loop が閉じていない。deployment 後の行為結果をどう知覚し、次世代 training へ戻すか。 | SOURCE: `/tmp/oqc_papers_20260426/2311.10215.txt:220-238` |
| OQ-B01-007 | [Understanding Deep Learning Requires Rethinking Generalization](https://arxiv.org/abs/1611.03530) | deep learning theory | generalization puzzle の古典的・高引用論文 | random labels を記憶できる過大モデルがなぜ一般化するのか。従来の model complexity measure では説明できず、巨大モデルを「simple」とみなす精密測度が未発見。 | SOURCE: `/tmp/oqc_papers_20260426/1611.03530.txt:170-175`, `/tmp/oqc_papers_20260426/1611.03530.txt:542-550` |
| OQ-B01-008 | [Opening the Black Box of Deep Neural Networks via Information](https://arxiv.org/abs/1703.00810) | information bottleneck / DL theory | IB による deep learning 解釈の代表的・論争的論文 | hidden layers が information plane 上の異なる点へ収束する理由が未解明。圧縮相・勾配ノイズ・最大エントロピー分布の関係が説明課題として残る。 | SOURCE: `/tmp/oqc_papers_20260426/1703.00810.txt:527-534` |
| OQ-B01-009 | [Why Does Deep and Cheap Learning Work So Well?](https://arxiv.org/abs/1608.08225) | DL theory / physics-inspired ML | 深層学習の物理的説明を試みる高影響 paper | deep network が shallow network より効率的になる関数クラスの完全な境界、no-flattening theorem の射程が未完成。 | SOURCE: `/tmp/oqc_papers_20260426/1608.08225.txt:899-910` |
| OQ-B01-010 | [The Markov blankets of life: autonomy, active inference and the free energy principle](https://arxiv.org/abs/1906.10184) | FEP / Markov blanket / physics | particular physics と Markov blanket の canonical 系譜 | Markov blanket の構成粒子が交換・更新される wandering sets をどう扱うか。現在の扱いは適切な時間スケールで blanket states が定義できるという単純化に依存。 | SOURCE: `/tmp/oqc_papers_20260426/1906.10184.txt:2520-2526` |
| OQ-B01-011 | [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | LLM / context | long-context LLM の代表的評価論文 | extended-context models が入力文脈をどのように使っているかは不明。長文脈化が必ずしも context use の改善を意味しない。 | SOURCE: `/tmp/oqc_papers_20260426/2307.03172.txt:62-75` |
| OQ-B01-012 | [Getting aligned on representational alignment](https://arxiv.org/abs/2310.13018) | representation / neuroscience / AI | 表象アラインメントの横断的 agenda | どの layer/component/brain region の representation を抽出し比較するか、similarity metrics の差が結論を変える問題、representation と computation の関係が未解決。 | SOURCE: `/tmp/oqc_papers_20260426/2310.13018.txt:1829-1848`, `/tmp/oqc_papers_20260426/2310.13018.txt:1898-1912`, `/tmp/oqc_papers_20260426/2310.13018.txt:1988-1996` |
| OQ-B01-013 | [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682) + [Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004) | LLM scaling / emergence | emergence debate の中心ペア | emergent abilities がなぜ・いつ発生するか、予測できるかが未解明。一方で metric choice が emergence を作る可能性があり、open question 自体が測定論に接続する。 | SOURCE: `/tmp/oqc_papers_20260426/2206.07682.txt:452-476`, `/tmp/oqc_papers_20260426/2206.07682.txt:738-760`, `/tmp/oqc_papers_20260426/2304.15004.txt:60-88`, `/tmp/oqc_papers_20260426/2304.15004.txt:716-722` |
| OQ-B01-014 | [27 Open Problems in Kolmogorov Complexity](https://arxiv.org/abs/2203.15109) | information theory / Kolmogorov complexity | algorithmic information theory の open-problem survey | Kolmogorov complexity と Shannon entropy の情報不等式・profile の構造、secret-key agreement で Eve が事前情報を持つ場合の最適限界などが未解決。 | SOURCE: `/tmp/oqc_papers_20260426/2203.15109.txt:55-73`, `/tmp/oqc_papers_20260426/2203.15109.txt:175-191`, `/tmp/oqc_papers_20260426/2203.15109.txt:792-808` |
| OQ-B01-015 | [Open problems in information geometry: a discussion at FDIG 2025](https://arxiv.org/abs/2509.06989) | information geometry | 情報幾何の open-problem 集 | operator Sinkhorn を divergence の交互最小化として書けるか、情報幾何に本質的な geometric structure は何か、divergence のよい定義、α≠±1 connection の実例、無限次元 IG と確率統計問題の接続。 | SOURCE: `/tmp/oqc_papers_20260426/2509.06989.txt:19-31`, `/tmp/oqc_papers_20260426/2509.06989.txt:155-204`, `/tmp/oqc_papers_20260426/2509.06989.txt:246-280` |
| OQ-B01-016 | [Position: Categorical Deep Learning is an Algebraic Theory of All Architectures](https://arxiv.org/abs/2402.15332) | category theory / deep learning | 圏論的DLの position paper | top-down constraints と bottom-up implementation をつなぐ一貫した bridge が不足している。semantics を syntax から推定する問題、GDL が層単位に偏る限界が残る。 | SOURCE: `/tmp/oqc_papers_20260426/2402.15332.txt:15-23`, `/tmp/oqc_papers_20260426/2402.15332.txt:92-100`, `/tmp/oqc_papers_20260426/2402.15332.txt:616-623` |

## Not Retained In This Batch

| source | 理由 |
|---|---|
| [Coherence for Lenses and Open Games](https://arxiv.org/abs/1704.02230) | 圏論・open systems 系として重要だが、今回の PDF 走査では著者自身の open question / future work として採る明確行を確認できなかった。後続で「既存回答として使う論文」側に回す余地あり。 |
| arXiv:2101.02621 | open conjecture はあるが、今回 Tolmetes が挙げた忘却論接続分野から遠い math.GT 寄りのため第一バッチから除外。 |

## AlphaXiv Reconnaissance

| surface | TAINT note | 処理 |
|---|---|---|
| alphaXiv explore search | `Open Problems in Mechanistic Interpretability` が高反応 paper として出現。 | arXiv PDF に戻して OQ-B01-001〜003 として SOURCE 昇格済み。 |
| alphaXiv explore search | sycophancy, LLM hacking, ambiguity/disambiguation, prompt injection/MCP safety など、agentic LLM 周辺の limitation/future-work 候補が複数出現。 | 第二バッチ候補。PDF/DOI を読んでから intake へ昇格する。 |

## Source Cache

PDF extraction cache:

```text
/tmp/oqc_papers_20260426/
```

この cache は作業用であり、恒久 SOURCE ではない。恒久参照は各 arXiv URL と PDF 本文に戻す。

## Next

次段で行うこと:

1. 上記 OQ を `emergence / boundary failure / representation geometry / context degradation / inverse recovery / scaling anomaly / measurement deformation / closure failure` などへ型分類する。
2. 忘却論側の theorem / proposition / definition / hypothesis / experiment anchor を local SOURCE から探す。
3. vocabulary-only 接続を Rejection Ledger に落とす。
