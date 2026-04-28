# Open Question Crosswalk — Mapping QT-COMP-GEN 2026-04-26

- 作成日: 2026-04-26
- 対象型: `QT-COMP-GEN` — compression / generalization / effective simplicity
- 入力: `../typing/typing_2026-04-26_batch01.md`, `../typing/typing_2026-04-26_batch02.md`, `../typing/typing_2026-04-26_batches01-02_summary.md`
- status: `mapped_draft`
- 目的: 外部 open question の「なぜ圧縮・単純性・一般化が成立するか」という欠落へ、忘却論側の theorem / proposition / experiment anchor を対応づける。

## P-0 Inputs

受け取り:

| input | status | 採用範囲 |
|---|---|---|
| `OQ-B01-007` | SOURCE from arXiv PDF extraction | generalization puzzle: 過大モデルが random labels を記憶できるのになぜ一般化するか |
| `OQ-B01-008` | SOURCE from arXiv PDF extraction | information plane 上で hidden layers が異なる点へ収束する理由 |
| `OQ-B01-014` | SOURCE from arXiv PDF extraction | Kolmogorov complexity / Shannon entropy / information profiles の構造問題 |
| `OQ-B01-015` | SOURCE from arXiv PDF extraction | information geometry における divergence / α-connection / geometric structure の open problems |
| `OQ-B02-003` | SOURCE from arXiv PDF extraction | SAM の optimizer-generalization gap と sharpness 近似 |
| `OQ-B02-004` | SOURCE from arXiv PDF extraction | Fisher SAM / natural gradient / m-sharpness の幾何的未閉鎖 |
| `OQ-B02-005` | SOURCE from arXiv PDF extraction | SAM approximation / proxy instability |
| `OQ-B02-006` | SOURCE from open-access PDF extraction | GeoIB / IB extension と compression geometry の限界 |

棄却:

| branch | 理由 |
|---|---|
| 「学習=忘却」だけで全件を束ねる | slogan 接続になり、各 OQ の欠落が見えなくなるため棄却。 |
| accuracy improvement claim を主回答にする | Paper I E12 は accuracy 中立も示す。主回答は性能ではなく representation / entropy / recoverability の構造に置く。 |
| Kolmogorov 問題を直答扱いする | Paper IX は Shannon/Rényi/Gini-Simpson 側の entropy bridge であり、Kolmogorov complexity の全 open problem を解くものではない。 |

Sourcing note:

| layer | status |
|---|---|
| Layer 0 onboarding | `drafts/リファレンス/忘却論オンボーディング.md` を確認済み |
| Layer 1 NotebookLM | 未使用。TAINT 偵察は今回の SOURCE 判定に使っていない |
| Layer 2 local read | Paper I / Paper IX / 統一記号表を直読し、下表の anchor に昇格 |

## Anchor Inventory

| anchor | claim level | SOURCE | contributes | risk |
|---|---|---|---|---|
| `I-T5.1` 方向性定理 | theorem | `drafts/series/論文I_力としての忘却_草稿.md:203-235` | 一般化を「容量の小ささ」ではなく、忘却場と Chebyshev 形式の非整列から生じる方向性として読む核。 | 外部 DL generalization へ接続するには、忘却場 Φ と T の operational estimator が必要。 |
| `I-P6.7.2` 表現制御定理 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:815-821` | α を変えると update direction と representation が `d(ΦT)` 方向へ構造的に動く、という最適化側の候補回答。 | α-SAM 自体は理論提案。大規模実装は未検証。 |
| `I-P6.8.1` α-Oblivion SAM 包含 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:864-893` | SAM / Fisher SAM / α-SAM / OA-SAM を特殊化関係で整理し、flatness だけではない forgetting-field 最適化を置く。 | λ 安定性と Φ の操作的定義に依存。 |
| `I-T6.8.1` CKA-KL 分離 | theorem | `drafts/series/論文I_力としての忘却_草稿.md:897-905` | CKA は形状、KL は形状+スケールを測ると分け、hidden layer の information-plane 問題を measurement decomposition へ変換する。 | ガウス近似・同時対角化から開始しているため、仮定除去節まで含めて読む必要がある。 |
| `I-P6.8.2` / `I-P6.8.3` CKA-KL 方向保存・比例 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:907-923` | CKA ベースの操作的忘却場と KL ベース理論を方向・量の両面で橋渡しする。 | 条件付き命題。CKA がスケール成分を見逃す点を明示する必要がある。 |
| `I-E12` OA-SAM 実験 | empirical | `drafts/series/論文I_力としての忘却_草稿.md:961-1028` | SAM は忘却パターンを変えず、λ の符号が忘却/保存を制御し、同一精度で複数の忘却 attractor が存在することを示す。 | ResNet-18/CIFAR-10 単一設定、N=10 の分岐比率。外部 contact 前に追試設計が必要。 |
| `IX-D2` CPS entropy | definition | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:112-118` / `drafts/リファレンス/統一記号表.md:361-364` | 圧縮・忘却を「確定的参照からの距離」として再定義する。 | α>0 では constructive extension として読む必要がある。 |
| `IX-T1` CPS entropy monotonicity | theorem | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:122-132` / `drafts/リファレンス/統一記号表.md:363-364` | 忘却が進むほど利用可能な deterministic references が減り、entropy が増えるという compression-side の核。 | Paper VIII F4 依存。外部読者向けには依存関係を明示する必要がある。 |
| `IX-C1` divergence independence | corollary | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:134-140` / `drafts/リファレンス/統一記号表.md:365` | Shannon / Rényi / Gini-Simpson を divergence 選択の違いとして束ねる。 | Kolmogorov complexity への接続は未解決。ここでは bridge seed に留める。 |
| `IX-P3.5.1` critical forgetting threshold `α*(p)` | proposition | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:156-172` | どこまで忘れても finite entropy / recoverability が残るかの閾値を与える。 | 実データ上の推定法は別途必要。 |
| `IX-P4.1.1` `S_cat` as double coarse-graining of `S_CPS` | proposition | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:197-217` | 射計数 entropy と状態依存 entropy の解像度差を説明し、coarse measure と fine measure の階層を作る。 | Kolmogorov profile への直接回答ではない。 |
| `I-P6.6.1` 曲率の α_I-線形性 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:760-766` | α 介入が曲率に正確に線形反映されるため、Fisher/SAM 系の幾何化に使える。 | FEP 精度 π との同一化は構成的命題に留まる。 |
| `I-P6.7.1` α-接続近傍 | definition / proposition | `drafts/series/論文I_力としての忘却_草稿.md:775-801` | SAM の Euclidean ball と Fisher SAM の Fisher ball を、α-接続近傍の特殊化として並べる。 | 最適化器としての実装は追加設計が要る。 |

## OQ Mapping Matrix

| OQ ID | external gap | candidate answer from Oblivion | anchors | answer type | grade | risk gate |
|---|---|---|---|---|---|---|
| `OQ-B01-007` | 過大モデルが random labels を記憶できるのに、なぜ実データでは一般化するのか。巨大モデルを simple とみなす測度がない。 | 「simple」は parameter count ではなく、学習後にどの deterministic reference / representation pattern が残るかで測る。Paper I の E12 は、同一精度を保つ複数の忘却 attractor があり、一般化性能と内部忘却パターンが同一ではないことを示す。従って一般化の候補説明は、容量の小ささではなく、忘却場が recoverable な representation degeneracy を選ぶこと。 | `I-T5.1`, `I-E12`, `IX-D2`, `IX-T1`, `IX-P3.5.1` | explanation principle + experiment seed | B | E12 は小規模。Zhang et al. への直答には random-label training と OA-SAM/CKA profile の追加実験が必要。 |
| `OQ-B01-008` | hidden layers が information plane 上の異なる点へ収束する理由、compression phase と gradient noise / maximum entropy の関係が未解明。 | hidden layer の収束点は単一の information scalar ではなく、忘却場の shape / scale / non-Gaussian 成分と update direction の交差で決まる。CKA-KL 分離により、CKA が見ている圧縮は主に shape 成分であり、KL の全情報とは一致しない。α-SAM はその方向を操作する候補実装になる。 | `I-T5.1`, `I-P6.7.2`, `I-T6.8.1`, `I-P6.8.2`, `I-P6.8.3`, `IX-D2` | measurement decomposition + mechanism candidate | A- | IB 論文への接続は強いが、外部論争を踏むため「Tishby を解いた」ではなく「information-plane の未分解成分を分ける」と表現する。 |
| `OQ-B01-014` | Kolmogorov complexity / Shannon entropy の inequality, profile, secret-key limits が未解決。 | Paper IX は Kolmogorov 問題に直答しない。ただし Shannon/Rényi/Gini-Simpson 側の entropy を、deterministic reference の縮小と divergence choice の違いとして統一する。ここから algorithmic information 側へ進む場合、`S_CPS` と Kolmogorov profile の間に追加の recoverability functor が必要。 | `IX-D2`, `IX-T1`, `IX-C1`, `IX-P4.1.1` | bridge seed, not answer | C | vocabulary-only 化しやすい。Kolmogorov 側は別途 SOURCE 精読と形式化が必要。 |
| `OQ-B01-015` | divergence のよい定義、α≠±1 connection の実例、IG の本質的 geometric structure が未整理。 | Paper I は Fisher metric を固定し、α を metric ではなく connection / update direction に置く。これにより α≠±1 の use case は、α-SAM の representation control として操作化できる。Paper IX は divergence の選択に依存しない entropy monotonicity を与え、どの divergence が必要かという問いを「何を測るか」と「単調性に何が不要か」に分解する。 | `I-P6.7.2`, `I-P6.8.1`, `IX-C1`, `IX-T1` | structural clarification + use-case proposal | B | FDIG 2025 paper の各 open problem は heterogeneous。operator Sinkhorn 等へはまだ未対応。 |
| `OQ-B02-003` | SAM が generalization を改善する機構、sharpness 近似と大規模最適化の限界が残る。 | SAM は flatness を直接「一般化の理由」とするより、忘却場の方向を十分に制御していない特殊化として読む。α-SAM / OA-SAM は SAM/Fisher SAM を含む上位 family を与え、E12 は同一精度でも forgetting attractor が分岐することを示す。 | `I-P6.7.1`, `I-P6.7.2`, `I-P6.8.1`, `I-E12` | mechanism candidate + experiment seed | B+ | 外部 SAM の benchmark へは、random-label / real-label と forgetting profile の追試が必要。 |
| `OQ-B02-004` | Fisher SAM の natural-gradient 化、distributed m-sharpness、proximal relation の幾何が未閉鎖。 | Fisher SAM は α=0 近傍の特殊化として位置づく。忘却論側では α 接続近傍と α_I 線形性により、Fisher metric を保ったまま update direction を変える幾何的拡張を置ける。 | `I-P6.6.1`, `I-P6.7.1`, `I-P6.7.2`, `I-P6.8.1` | direct optimization bridge | A- | distributed setting / proximal relation は未実装。理論対応を先に切る。 |
| `OQ-B02-005` | SAM approximation が不安定で、sharpness proxy が真の一般化機構を捕まえているか不明。 | proxy failure は sharpness の失敗ではなく、測定関手が内部忘却 attractor を潰す問題として扱う。CKA-KL 分離と E12 は、accuracy / sharpness が同じでも representation-forgetting profile が異なる余地を与える。 | `I-T6.8.1`, `I-P6.8.2`, `I-P6.8.3`, `I-E12` | measurement decomposition | B+ | SAM approximation paper の具体的 error term と CKA/KL の対応づけが必要。 |
| `OQ-B02-006` | GeoIB / IB は compression の向き・幾何・限界をどう扱うべきかが未閉鎖。 | IB の compression scalar を、deterministic reference の喪失、critical forgetting threshold、shape/scale の測定分解へ展開する。GeoIB への候補回答は「情報量を減らす」ではなく「どの参照が recoverable に残るか」を幾何化すること。 | `IX-D2`, `IX-T1`, `IX-P3.5.1`, `IX-P4.1.1`, `I-T6.8.1` | structural extension | B+ | GeoIB 側の式に直対応させるには β-λ bridge の精読・再確認が必要。 |
| `OQ-B03-001` | UHAT (固定精度) の検証は EXPSPACE-complete、UHAT は LTL に対し指数、DFA に対し二重指数 succinct。圧縮の量と検証コストが **同じ n に対し doubly-exponential で一致** することの構造的説明は外部論文では与えられていない。本 OQ は primary が `QT-FORMAL-VERIF` で、`QT-COMP-GEN` には cross-type bridge として接続する。 | 忘却論の `U⊣N` 経済性を formal language レベルの matched bound として読む。succinctness は U の真部分種 (情報損失なしの「冗長な記述の畳み込み」) であり、`IX-D2 / IX-T1` の deterministic-reference reduction と直接重ねるのではなく、Sistla-Clarke (1985) の LTL PSPACE-completeness と Bergsträßer et al. (2025) の UHAT EXPSPACE-completeness を硬い外部 reference 点として bring in する。`OQ-B01-014` (Kolmogorov) が source-thin に留まっている部分への迂回路として、algorithmic information の代わりに **complexity-theoretic recoverability** を anchor にする bridge seed。 | `IX-D2`, `IX-T1`, `IX-C1` (loose connection); 統一記号表 §1 の `U / N` (paper-local 例外: succinctness は U-side の特殊化) | bridge seed across types | C+ | (a) `succinctness ≈ U` と無条件同一視すると Paper IX の CPS entropy 構造と衝突する。射程を「冗長記述の畳み込み」に閉じる必要あり。(b) UHAT は AC⁰ 内・star-free 限定。実 LLM (softmax / arbitrary-precision) への一般化は未確定。`OQ-B03-001b/c` の child split を経由しないまま接続すると vocabulary-only 化する。 |

## Candidate Answer Patterns

| pattern | 1-3 sentence form | usable for |
|---|---|---|
| effective simplicity as recoverable forgetting | 過大モデルの「単純さ」は、パラメータ数ではなく、どの忘却後構造が recoverable な参照点として残るかで測る。忘却が進むほど deterministic references は減るが、参照が残る範囲では複数の内部構造が同一性能を支えうる。 | `OQ-B01-007`, `DS-SLEEP-MEM`, `DS-HOLOGRAPHY` |
| information-plane as decomposed forgetting field | hidden layer の information-plane 収束は、単一の圧縮量ではなく、shape / scale / non-Gaussian 成分に分かれた忘却場の射影として読む。CKA は shape を強く見るため、KL とのずれは測定誤差ではなく観測関手の違いとして扱える。 | `OQ-B01-008`, `DS-GEOIB`, representation alignment |
| alpha as update-direction control | α は Fisher metric を増やす追加計量ではなく、同じ metric 上で update direction を変える connection parameter として使う。この読みなら、α≠±1 の実例は α-SAM / OA-SAM の representation control として立つ。 | `OQ-B01-015`, `DS-OPT-SAM` |
| entropy monotonicity from lost deterministic references | entropy increase は divergence の細部ではなく、忘却により deterministic reference の集合が縮むことから出る。これは Shannon/Rényi/Gini-Simpson を束ねるが、Kolmogorov profile へ行くには別の bridge が必要。 | `OQ-B01-014`, information theory cases |
| succinctness gap as complexity-theoretic matched bound for U⊣N | `U` 側の圧縮利得 (UHAT が DFA に対し二重指数 succinct) と `N` 側の検証コスト (EXPSPACE = 二重指数空間) が **同じ n に対し同じ doubly-exponential スケールで一致** する。これは algorithmic information への直接接続ではなく、complexity-theoretic recoverability を外部 anchor として `U⊣N` の経済性を量化する bridge。Kolmogorov 側 (`OQ-B01-014`) が source-thin に留まる迂回路として機能する。射程は固定精度 UHAT・star-free regular language に閉じる。 | `OQ-B03-001`, `OQ-B01-014` (bridge as detour), formal language ↔ neural representation cases |

## Promotion Decision

| target | decision | next operation |
|---|---|---|
| `OQ-B01-008` | promote first | IB / GeoIB case を作る。Paper I §6.8.1 と外部 IB quote を並べ、measurement decomposition case にする。 |
| `OQ-B02-004` | promote alongside SAM | Fisher SAM / α-SAM bridge case を作る。`I-P6.6.1` と `I-P6.7.1/2` を外部 Fisher SAM limitation と対置する。 |
| `OQ-B02-006` | promote as GeoIB bridge | `OQ-B01-008` と同じ information geometry lane に入れ、IB scalar から recoverability threshold への拡張として case 化する。 |
| `OQ-B01-007` | promote second | generalization puzzle case を作る。E12 の forgetting degeneracy を random-label / real-label 比較実験案へ落とす。 |
| `OQ-B01-015` | hold as bridge | FDIG 2025 の child OQ を分割してから mapping。 |
| `OQ-B01-014` | hold, source-thin | Kolmogorov complexity 側の追加精読後に再判定。今は contact / note 化しない。 |
| `OQ-B03-001` | hold as cross-type bridge | primary は `QT-FORMAL-VERIF` 側 mapping (未起票)。本 `QT-COMP-GEN` mapping では、`OQ-B01-014` source-thin gap への迂回 anchor として保持。child split (`OQ-B03-001a/b/c/d`) を経由する前に case 化しない。 |

## Rejection Ledger

| rejected claim | reason |
|---|---|
| 忘却論は Zhang et al. の generalization puzzle を解決済み | E12 は candidate mechanism と small-scale empirical clue であって、random-label generalization 実験を直接閉じていない。 |
| CKA-KL bridge で IB 論争は解決済み | bridge は hidden-layer measurement decomposition を与えるが、IB 圧縮相の全主張を採否するものではない。 |
| CPS entropy は Kolmogorov open problems への回答 | Shannon/Rényi/Gini-Simpson 側の統一であり、algorithmic information profile には追加構成が要る。 |
| α-SAM で SAM 系 open question は解決済み | α-SAM は上位 family と候補機構であり、distributed SAM / proximal relation / approximation error は未検証。 |
| `OQ-B03-001` の succinctness は `IX-D2 / IX-T1` の `U` と同一 | succinctness は言語同一性を保つ「冗長記述の畳み込み」であり、`IX-T1` の deterministic-reference reduction (情報損失を伴う U) とは射程が異なる。重ねるなら paper-local 例外として記号表に local 宣言が必要 (Paper XI の `N⊣U` 例外と同様)。 |
| `OQ-B03-001` の結果は実 LLM (GPT/Claude/Gemini) に直接適用される | UHAT は AC⁰ 内・固定精度・star-free 限定。softmax / arbitrary-precision / 非 star-free への拡張は未確定。child split (`OQ-B03-001b/c`) を経由する前に実 LLM 主張に格上げしない。 |

## Carry Forward

次に作るべき case:

1. `cases/OQ-B01-008_information_plane_CKA_KL.md`
2. `cases/OQ-B02-004_fisher_sam_alpha_sam.md`
3. `cases/OQ-B01-007_generalization_forgetting_degeneracy.md`

case 作成時は、外部 PDF quote と local anchor を同じ table に置き、`candidate answer` と `what would falsify this mapping` を必ず書く。

### Cross-type bridge note (2026-04-27 追記)

`OQ-B03-001` (Bergsträßer-Cotterell-Lin 2025, transformer succinctness) は primary が `QT-FORMAL-VERIF`。本 mapping では「Kolmogorov 側 source-thin gap への迂回 anchor」としてのみ保持する。完全な mapping は `mappings/mapping_QT-FORMAL-VERIF_2026-XX-XX.md` (未起票) で行う。Lane A (compression geometry) と Lane C (formal coherence) を跨ぐ bridge candidate であり、両 lane を横断する mapping を将来作る際は本 OQ から開始するのが自然。
