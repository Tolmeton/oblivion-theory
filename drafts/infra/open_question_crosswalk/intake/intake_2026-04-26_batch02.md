# Open Question Crosswalk — Intake Batch 02

- 作成日: 2026-04-26
- 目的: `domain_scope.md` で追加した分野から、影響力・接続可能性の高い open question / limitation / future work を拾う。
- 範囲: holography/QG, SAM/GeoIB, HoTT/cohomology/enriched category, hyperbolic media, spin-statistics/fermionic QI, psychopathology/precision, sleep/memory consolidation。
- SOURCE 規律: arXiv PDF / open-access paper / PMC HTML をローカル抽出して確認したものだけを SOURCE とする。
- まだ行わないこと: 問いの型分類、忘却論 theorem/proposition/concept への対応づけ、contact 判断。

## Intake Table

| ID | source | 分野 | 影響力の理由 | 拾った open question / limitation | evidence |
|---|---|---|---|---|---|
| OQ-B02-001 | [Lessons from the Information Paradox](https://arxiv.org/abs/2012.05770) | holography / black-hole information | black-hole information paradox の代表的 review | information paradox は単一問題ではなく相互接続された puzzle 群。state dependence が ruled out される場合の interior/firewall 問題、subregion duality を Hamiltonian に直接導く問題が残る。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2012.05770.txt:5428-5435`, `/tmp/oqc_papers_20260426_batch02/2012.05770.txt:5542-5568` |
| OQ-B02-002 | [Holographic spacetime, black holes and quantum error correcting codes: A review](https://arxiv.org/abs/2110.14669) | holography / QEC | bulk reconstruction と QEC の review | black-hole interior を実時間の operational framework でどう扱うか、tensor networks が RT extremal surface を越えた情報理論的側面を再現するかが未確定。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2110.14669.txt:265-272`, `/tmp/oqc_papers_20260426_batch02/2110.14669.txt:3194-3205`, `/tmp/oqc_papers_20260426_batch02/2110.14669.txt:3866-3874` |
| OQ-B02-003 | [Sharpness-Aware Minimization for Efficiently Improving Generalization](https://arxiv.org/abs/2010.01412) | optimization / generalization | SAM の原論文 | optimizer と generalization の関係理解は nascent。SAM 近似の二階項、m-sharpness と generalization gap の関係が future work として残る。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2010.01412.txt:50-59`, `/tmp/oqc_papers_20260426_batch02/2010.01412.txt:228-235`, `/tmp/oqc_papers_20260426_batch02/2010.01412.txt:552-558` |
| OQ-B02-004 | [Fisher SAM: Information Geometry and Sharpness Aware Minimisation](https://arxiv.org/abs/2206.04920) | information geometry / optimization | SAM を Fisher metric へ移す代表的 paper | Euclidean neighborhood の不正確さを Fisher geometry で修正するが、natural-gradient update、distributed m-sharpness、proximal-gradient との関係が未解決。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2206.04920.txt:268-276`, `/tmp/oqc_papers_20260426_batch02/2206.04920.txt:548-556` |
| OQ-B02-005 | [Revisiting Sharpness-Aware Minimization](https://arxiv.org/abs/2603.10048) | optimization / SAM variants | 2026年時点の SAM 再解釈・改良 paper | SAM の single-step ascent gradient は近傍最大方向の近似として機能するが、その近似は不正確・不安定で、multi-step では品質劣化しうる。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2603.10048.txt:32-39`, `/tmp/oqc_papers_20260426_batch02/2603.10048.txt:88-98` |
| OQ-B02-006 | [Variational Geometric Information Bottleneck](https://arxiv.org/abs/2511.02496) | GeoIB / representation learning | GeoIB 直結の新規 preprint。canonical ではなく direct-relevance 枠 | geometric IB を temporal/causal/multimodal settings へ拡張できるか。高 intrinsic dimension / non-manifold data で幾何仮定が破れる可能性が limitation。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2511.02496.txt:806-832`, `/tmp/oqc_papers_20260426_batch02/2511.02496.txt:1119-1135` |
| OQ-B02-007 | [Computational Synthetic Cohomology Theory in Homotopy Type Theory](https://arxiv.org/abs/2401.16336) | HoTT / cohomology / formalization | HoTT 上の synthetic cohomology formalization | Cubical Agda で計算困難な Brunerie-number 類似 benchmark が open computational problems として残る。synthetic cohomology と classical computational approaches の接続も future direction。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2401.16336.txt:21-28`, `/tmp/oqc_papers_20260426_batch02/2401.16336.txt:130-138`, `/tmp/oqc_papers_20260426_batch02/2401.16336.txt:2471-2492` |
| OQ-B02-008 | [Models of Type Theory with Strict Equality](https://arxiv.org/abs/1702.04912) | HoTT / two-level type theory | semi-simplicial types と internal `(∞,1)`-categories の open-problem bridge | two-level type theory は HoTT の pressing open problems への partial solution とされる。特に semi-simplicial types と internal `(∞,1)`-category foundation が焦点。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/1702.04912.txt:41-48`, `/tmp/oqc_papers_20260426_batch02/1702.04912.txt:315-324` |
| OQ-B02-009 | [Higher Structures in Homotopy Type Theory](https://arxiv.org/abs/1807.02177) | HoTT / higher structures | HoTT/UF の higher-structure survey | higher-dimensional homotopy types、model category の weak-equivalence/Quillen-equivalence invariance、algebraic models for ∞-groupoids、HoTT/UF での higher structures の扱いが open。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/1807.02177.txt:70-78`, `/tmp/oqc_papers_20260426_batch02/1807.02177.txt:263-277` |
| OQ-B02-010 | [Algebras of higher operads as enriched categories II](https://arxiv.org/abs/0909.4715) | enriched category / higher category | enriched category と higher operad の標準的接続 | higher-dimensional analogues of Gray tensor product の体系的構成が higher category theory の open problem として提示される。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/0909.4715.txt:10-17` |
| OQ-B02-011 | [Superluminal Correlations in Ensembles of Optical Phase Singularities](https://arxiv.org/abs/2509.17675) | hyperbolic media / nanophotonics | hBN hyperbolic phonon polaritons と optical phase singularities の外部較正候補 | phase singularity ensemble の full phase-space correlations は未探索・実験的に inaccessible だった。sub-cycle/sub-wavelength 測定自体が technical challenge。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2509.17675.txt:35-43`, `/tmp/oqc_papers_20260426_batch02/2509.17675.txt:82-88` |
| OQ-B02-012 | [Reasonable fermionic quantum information theories require relativity](https://arxiv.org/abs/1502.04476) | spin-statistics / fermionic QI | spin-statistics と quantum information の接点 | fermionic Fock space 上の unrestricted QI では pure bipartite states の marginal entropies が一致せず、entanglement definition が ambiguous になる。parity superselection / relativity が必要になる。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/1502.04476.txt:8-15`, `/tmp/oqc_papers_20260426_batch02/1502.04476.txt:35-50` |
| OQ-B02-013 | [The Many Roles of Precision in Action](https://pmc.ncbi.nlm.nih.gov/articles/PMC11431491/) | active inference / precision / psychopathology | precision weighting の recent open-access review | precision の neuromodulatory mechanism、active inference/precision の脳内実装、psychosis における precision changes の機構が open question。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/PMC11431491_precision_action.txt:846-856`, `/tmp/oqc_papers_20260426_batch02/PMC11431491_precision_action.txt:880-907` |
| OQ-B02-014 | [Precise Minds in Uncertain Worlds: Predictive Coding in Autism](https://serg.al/files/documents/mind/2014-VandeCruysetal-PsychRev-Precise_minds.pdf) | ASD / predictive coding | ASD precision-weighting account の代表的 paper | predictive coding theories of mental illness は just-so stories を越え、障害ごとの cognitive/neural specificity を constrain する必要がある。ASD theory の unique predictive power も未検証。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/2014_precise_minds.txt:1358-1370`, `/tmp/oqc_papers_20260426_batch02/2014_precise_minds.txt:1378-1388` |
| OQ-B02-015 | [Sleep-Dependent Potentiation in the Visual System Is at Odds with the Synaptic Homeostasis Hypothesis](https://pmc.ncbi.nlm.nih.gov/articles/PMC4678346/) | sleep / memory consolidation | SHY への明確な反証圧を持つ open-access paper | Synaptic Homeostasis Hypothesis は睡眠の認知・可塑性効果を完全には説明できない。downscaling の adaptive plasticity への関与、細胞機構、機能は未確定。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/PMC4678346_sleep_shy_odds.txt:124-165` |
| OQ-B02-016 | [Sleep-Dependent Synaptic Down-Selection (I)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3786405/) | sleep / memory consolidation | down-selection model の代表的 computational study | memory を支える synapse の絶対強度が睡眠後どう変わるかは unknown。研究設計上も異なる実験に異なる simulated networks を用いる limitation がある。 | SOURCE: `/tmp/oqc_papers_20260426_batch02/PMC3786405_sleep_downselection.txt:204-214`, `/tmp/oqc_papers_20260426_batch02/PMC3786405_sleep_downselection.txt:1168-1177` |

## Not Retained In This Batch

| scope | 理由 |
|---|---|
| DS-SEMIOTICS | prompt sensitivity / symbol grounding / semiotics は候補が多いが、第一・第二バッチで LLM context / NLP reasoning を既に採取したため、次 batch へ回す。 |
| DS-HYPHE-CHEM | crystallization / Ostwald ripening は比喩接続が強い一方、外部側 open question を忘却論候補回答へ直結するには source gate が弱い。後続で物理化学側の review を別途読む。 |

## Source Cache

PDF/HTML extraction cache:

```text
/tmp/oqc_papers_20260426_batch02/
```

この cache は作業用であり、恒久 SOURCE ではない。恒久参照は各 URL と本文に戻す。

## Next

次段で行うこと:

1. Batch 01 + Batch 02 を統合して問い型分類する。
2. `domain_scope.md` の未採取 scope、特に DS-SEMIOTICS / DS-HYPHE-CHEM を第三 batch 候補へ残す。
3. 忘却論側 anchor 探索では、まず `closure failure`, `measurement deformation`, `geometry of compression`, `witness erasure`, `precision anisotropy`, `residual information` の6型を仮置きする。
