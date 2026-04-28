# Open Question Crosswalk — 管理台帳

## 目的

外部論文の open question / limitation / future work を、忘却論側の候補回答・説明原理・検証可能な予測へ写像する。

## Case Ledger

| ID | 外部論文 | 未解決問の型 | evidence | 忘却論 anchor | 候補回答の型 | status | 次の操作 |
|---|---|---|---|---|---|---|---|
| S-053 | Choi & Weber (2026), arXiv:2604.07382 | representation geometry / emergence | WEAK INPUT: Pinakas seed. External PDF SOURCE read required | Paper VII Th.6.1.1 構造保存定理 | explanation principle | seed | `cases/S-053_choi_weber_2604_07382.md` を PDF quote で SOURCE 昇格 |
| OQ-B01-008 | Schwartz-Ziv & Tishby (2017), arXiv:1703.00810 | information-plane / compression geometry | SOURCE: `/tmp/oqc_papers_20260426/1703.00810.txt:527-534` | Paper I Th.6.8.1 CKA-KL 分離 | measurement decomposition | gauntlet_passed | toy / published CKA-KL vs information-plane comparison を追加 |
| OQ-B02-004 | Kim et al. (2022), arXiv:2206.04920 | Fisher geometry / SAM optimization | SOURCE: `/tmp/oqc_papers_20260426_batch02/2206.04920.txt:268-276`, `/tmp/oqc_papers_20260426_batch02/2206.04920.txt:548-556` | Paper I Prop.6.6.1 / Prop.6.7.1-2 / Prop.6.8.1 | optimizer-family extension | oblivion_sam_case | stronger λ effect / full α-connection / torch-CIFAR 外部妥当性へ進む |

## Intake Batches

| batch | 内容 | source status | 次の操作 |
|---|---|---|---|
| 2026-04-26_batch01 | 影響力のある arXiv / papers から open question / limitation / future work を16件採取 | arXiv PDF 直読 SOURCE。alphaXiv は TAINT 偵察のみ | typed 済み。`QT-COMP-GEN` は mapping 済み。他 type は統合 summary から順次 mapping |
| 2026-04-26_batch02 | expanded scope から holography/QG, SAM/GeoIB, HoTT/cohomology/enriched category, hyperbolic media, spin-statistics, precision psychopathology, sleep/memory を16件採取 | arXiv PDF / open-access PDF / PMC HTML 直読 SOURCE | typed 済み。`typing/typing_2026-04-26_batch02.md` と統合 summary から anchor 探索へ送る |
| 2026-04-27_batch03 | Bergsträßer-Cotterell-Lin (2025, arXiv:2510.19315) `Transformers are Inherently Succinct` を単独採取。UHAT の formal-language theoretic succinctness と EXPSPACE-complete 検証性を `QT-FORMAL-VERIF ∩ QT-COMP-GEN ∩ QT-SYN-SEM` 三重交点に着地させる。 | arXiv PDF 直読 SOURCE。HGK ECC ベクトル検索は hit 0 で TAINT 偵察として未使用。 | typed 済み。`mappings/mapping_QT-COMP-GEN_2026-04-26.md` に cross-type bridge として追記済み。primary `QT-FORMAL-VERIF` mapping は未起票。 |

## Typing Batches

| batch | 内容 | status | 次の操作 |
|---|---|---|---|
| 2026-04-26_batch01 | OQ-B01-001〜016 を13型で分類。domain scope seed も仮分類 | typed | `QT-COMP-GEN` は `mappings/mapping_QT-COMP-GEN_2026-04-26.md` へ送付済み |
| 2026-04-26_batch02 | OQ-B02-001〜016 を9型で分類。factorization / observational access / precision / memory consolidation 型を catalog に追加 | typed | `typing/typing_2026-04-26_batch02.md` から統合 summary へ送る |
| 2026-04-26_batches01-02 | 32件を17型で統合分布化し、6つの mapping lane へ収束 | typed | `typing/typing_2026-04-26_batches01-02_summary.md` の P1/P2 から `mappings/` を増補する |
| 2026-04-27_batch03 | OQ-B03-001 を `QT-FORMAL-VERIF` (primary) + `QT-COMP-GEN` + `QT-SYN-SEM` (secondary) に 3 重分類。child split を `OQ-B03-001a/b/c/d` に予告。 | typed | `QT-FORMAL-VERIF` lane の 2 件目として OQ-B01-002 (mechanistic interpretability) と並ぶ。primary mapping (`mappings/mapping_QT-FORMAL-VERIF_*.md`) を新規起票することが次の自然な操作。 |

## Mapping Batches

| batch | target type | 内容 | status | 次の操作 |
|---|---|---|---|---|
| 2026-04-26_QT-COMP-GEN | `QT-COMP-GEN` | OQ-B01-007/008/014/015 を Paper I / IX anchors に対応づけ | mapped_draft | `OQ-B01-008` と `OQ-B01-007` を個別 case 化 |
| 2026-04-26_anchor_index | all lanes | 32 OQ を忘却論側 theorem / proposition / concept anchor へ初期対応づけ | mapped_index | `OQ-B01-008`, `OQ-B02-004`, `OQ-B02-012` から detailed case 化 |
| 2026-04-26_QT-COMP-GEN_batch02 | `QT-COMP-GEN` + SAM/GeoIB | OQ-B02-003/004/005/006 を α-SAM, CKA-KL, CPS entropy anchors に増補 | mapped_draft | Fisher SAM / GeoIB case を作る |
| 2026-04-27_QT-COMP-GEN_bridge | `QT-COMP-GEN` cross-type bridge | OQ-B03-001 (UHAT succinctness) を Kolmogorov source-thin gap への迂回 anchor として追記。新規 candidate answer pattern `succinctness gap as complexity-theoretic matched bound for U⊣N` 追加。Paper XI .meta.md §M5 に 2026-04-27 Round 1 として外部硬 anchor 補強仮説を記録。 | bridged_draft | ✓ QT-FORMAL-VERIF primary 起票済み。次は OQ-B03-001 child split (a-d)。 |
| 2026-04-27_QT-FORMAL-VERIF | `QT-FORMAL-VERIF` primary | OQ-B01-002 (toy-to-frontier verification gap) と OQ-B03-001 (UHAT EXPSPACE matched bound) を II-T3.4.1 / VIII-Bridge / VI-D2.1.1 / IX-T1 anchors に対応づけ。2 patterns: structural face criterion + complexity-theoretic matched bound for U⊣N。✓ OQ-B03-001 child split (a/b/c/d) 登録済み (`cases/OQ-B03-001_child_split_abcd.md`)。 | split_registered | (a) OQ-B03-001a case 化 — II-T3.4.1 精読後。(b) OQ-B03-001d → QT-SYN-SEM mapping 新規起票 (最優先)。(c) OQ-B03-001c → mapping_QT-COMP-GEN 追記 (Jerad et al. 採取後)。(d) OQ-B03-001b は Sälzer et al. NEXP-hard 採取後に debt 解消。 |

## Gauntlet Batches

| batch | target | 内容 | status | 次の操作 |
|---|---|---|---|---|
| 2026-04-26_cases_01 | OQ-B01-008 / OQ-B02-004 | measurement-only, reparameterization, partial-answer, implementation-gap objections を通し、撤回条件を追加 | gauntlet_passed | B01-008 は toy comparison、B02-004 は E0/E1 experiment sketch を実装候補化 |
| 2026-04-26_b02_e0a | OQ-B02-004 | NumPy-only Fisher-ball recovery smoke を追加し、α=0/λ=0 の実装特殊化を検査 | experiment_scaffolded | E0b training recovery / E1 direction probe が残 debt |
| 2026-04-27_b02_e0b | OQ-B02-004 | NumPy trainable logistic model で Fisher SAM と α-SAM(0,0) の軌道一致を検査 | recovery_passed | E1 direction probe が残 debt |
| 2026-04-29_b02_e1 | OQ-B02-004 | NumPy MLP で非ゼロ α が Fisher 半径固定のまま hidden representation を動かすか検査 | direction_control_case | E2 lambda term / full α-connection / torch-CIFAR 外部妥当性が残 debt |
| 2026-04-29_b02_e2 | OQ-B02-004 | λ-weighted CKA forgetting regularizer が accuracy を保ったまま profile を動かすか検査 | oblivion_sam_case | stronger λ effect / full α-connection / E3 distributed profile が残 debt |

## Domain Scope Updates

| date | 内容 | status | 次の操作 |
|---|---|---|---|
| 2026-04-26 | HoTT, TDA/cohomology, enriched category, hyperbolic media, spin-statistics, holography/QG, psychopathology, sleep/memory, SAM optimization, GeoIB, semiotics, solution chemistry を追加 | `domain_scope.md` に登録済み。第二 intake batch で主要 scope は SOURCE 採取済み | DS-SEMIOTICS / DS-HYPHE-CHEM は第三 batch 候補として残す |

## Question Type Catalog

正本: `question_type_catalog.md`

## Promotion Queue

| ID | 昇格先 | 条件 | 現状態 |
|---|---|---|---|
| S-053 | short note / contact candidate | PDF から open question / limitation の exact quote を取得し、Paper VII anchor を SOURCE で再確認する | 未着手 |
| OQ-B01-008 | case / short note seed | IB information-plane quote と Paper I CKA-KL anchor を並べ、測定分解として candidate answer を書く | `cases/OQ-B01-008_information_plane_CKA_KL.md` で gauntlet_passed |
| OQ-B02-004 | case / experiment seed | Fisher SAM limitation と Paper I α-SAM / α線形性 anchor を並べ、natural-gradient extension として候補回答を書く | `cases/OQ-B02-004_fisher_sam_alpha_sam.md` で oblivion_sam_case |
| OQ-B02-012 | case / short note seed | fermionic QI factorization quote と Paper III Z2-CPS / boson-fermion correspondence を並べる | `mapping_anchor_index_2026-04-26.md` で A- |
| OQ-B01-007 | case / experiment seed | generalization puzzle quote と Paper I E12 forgetting degeneracy を並べ、random-label 対応実験案へ落とす | `mapping_QT-COMP-GEN_2026-04-26.md` で B |

## Rejection Ledger

| ID | 棄却理由 | 記録日 |
|---|---|---|
| R-2026-04-26-COMP-GEN-01 | `QT-COMP-GEN` を「学習=忘却」だけで束ねると slogan 接続になるため棄却。 | 2026-04-26 |
| R-2026-04-26-COMP-GEN-02 | Paper I E12 だけで Zhang et al. generalization puzzle を解決済み扱いするのは過剰接続。 | 2026-04-26 |
| R-2026-04-26-COMP-GEN-03 | Paper IX CPS entropy を Kolmogorov open problems への直接回答として扱うのは source-thin。 | 2026-04-26 |
| R-2026-04-26-STRING-01 | 超ひも理論 / broad string-theory open problems は今回の case 化対象から外す。既に別線で論駁済みという Tolmetes 判断を採用し、QG/holography 系も当面は `anchor_pending` に留める。 | 2026-04-26 |
