# Open Question Crosswalk — Mapping QT-FORMAL-VERIF 2026-04-27

- 作成日: 2026-04-27
- 対象型: `QT-FORMAL-VERIF` — formal verification / symbolic reduction / complexity-theoretic guarantee
- 入力: `../intake/intake_2026-04-26_batch01.md`, `../intake/intake_2026-04-27_batch03.md`, `../typing/typing_2026-04-26_batch01.md`, `../typing/typing_2026-04-27_batch03.md`, `../mappings/mapping_anchor_index_2026-04-26.md`
- status: `mapped_draft`
- 目的: 外部 open question の「形式的保証が simple→complex の移行で成立するか、また verification コストはどれほどか」という欠落へ、忘却論側の theorem / proposition / complexity-theoretic anchor を対応づける。

## P-0 Inputs

受け取り:

| input | status | 採用範囲 |
|---|---|---|
| `OQ-B01-002` | SOURCE: `/tmp/oqc_papers_20260426/2501.16496.txt:1514-1525` | toy-to-frontier formal verification gap。mechanistic interpretability の symbolic reduction 限界 |
| `OQ-B03-001` | SOURCE: `_sources/arxiv_2510_19315/paper.txt:302-303, 425, 466, 477, 486, 515-519, 521-531` | UHAT succinctness doubly-exponential gap + EXPSPACE-complete verification |

棄却:

| branch | 理由 |
|---|---|
| QT-FORMAL-VERIF を QT-COMP-GEN の下位型として扱う | compression geometry (QT-COMP-GEN) と formal verification hardness (QT-FORMAL-VERIF) は接続するが同型ではない。succinctness gap は COMP-GEN 側から detour で読めるが、FORMAL-VERIF の独自性は complexity-completeness の two-way bounded constraint。別 lane として立てる。 |
| OQ-B03-001 の UHAT 結果を general LLM に直接適用する mapping | UHAT = AC⁰ 内・固定精度・star-free 限定。softmax attention LLM への適用は別 complexity-theoretic bridge が必要。このファイルでは UHAT 射程内の記述のみ。 |
| OQ-B01-002 の「symbolic reduction が完全に可能」という候補回答 | II-T3.4.1 は face 保存の条件を与えるが、実際の frontier NN の2-simplex 同定は外部 formal tool が存在しない。完全可能 claim は棄却。部分的可能性の構造的条件として置く。 |

Sourcing note:

| layer | status |
|---|---|
| Layer 0 onboarding | `drafts/リファレンス/忘却論オンボーディング.md` 確認済み (2026-04-27) |
| Layer 1 NotebookLM | 未使用。このファイルの anchor 索引は mapping_anchor_index_2026-04-26.md (SOURCE-local) を正本とする |
| Layer 2 local read | Paper II (Face Lemma, Stability Simplex) / Paper VI (G∘F 結晶化) / Paper IX (CPS entropy monotonicity) / Paper VIII (bridge functor) を anchor_index 経由で確認。arXiv:2510.19315 は本文直読 SOURCE |

## Anchor Inventory

| anchor | claim level | SOURCE | contributes | risk |
|---|---|---|---|---|
| `II-T3.4.1` Face Lemma | theorem | `drafts/series/論文II_相補性は忘却である_草稿.md:407-440` | simplification (忘却) が許容されるのは、対象の minimal nontrivial face が保存されるときかつそのときのみ、という verification criterion の核。toy-to-frontier gap の構造的回答候補。 | 物理・DL へ使う時は2-simplex の同定法を外部 formal tool で別途提供しないと比喩化リスク (anchor_index P-4 caution 準拠)。 |
| `II-Stability-Simplex` Stability Simplex | theorem | `drafts/series/論文II_相補性は忘却である_草稿.md:575-629` | syntax-semantics / categorical DL の emergence threshold を与える。symbolic reduction が壊れる閾値の形式的条件を構成する。 | 外部形式体系への再記述が必要。直接 claim は anchor_index grade B 相当。 |
| `VIII-Bridge` bridge functor | definition / proposition | `drafts/series/論文VIII_存在は忘却に先行する_草稿.md:647-656`, `drafts/series/論文VIII_存在は忘却に先行する_草稿.md:732-748` | faithful bridge functor が存在するときに限り、簡略化前後の formal property が保存される、という verification の充分条件側。 | faithful 条件を外部圏で確認する必要 (anchor_index caution 準拠)。 |
| `VI-D2.1.1` G∘F 結晶化随伴 | definition | `drafts/series/論文VI_行為可能性は忘却である_草稿.md:68-79` | U⊣N (U = forgetting / compression, N = crystallization / recovery) の随伴形式。compression gain と verification cost の双方が随伴の左右に乗る点を抽象的に記述する。 | paper-local の U⊣N は符号方向に注意 (Paper XI では N⊣U 記法。VI では G∘F = 結晶化 = N-side)。 |
| `IX-D2` CPS entropy | definition | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:112-118` | 圧縮・忘却を「確定的参照からの距離」として定量化する。verification cost が N-side = recovery/CPS 再構築コストに対応する点で接続。 | α>0 での constructive extension として読む必要。 |
| `IX-T1` CPS entropy monotonicity | theorem | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:122-132` | 忘却が進むほど entropy が増える (recoverability が下がる) という単調性は、verification cost が compression 量と同方向に増大することの忘却論側の定理。 | Paper VIII F4 依存。外部読者向けには依存関係の明示が必要。 |
| `IX-P3.5.1` critical forgetting threshold `α*(p)` | proposition | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:156-172` | どこまで圧縮 (忘却) しても有限 entropy / recoverability が残るかの閾値。EXPSPACE matched bound と組み合わせると、「いくら succinctness を追っても N-side コストが doubly-exponential で付いてくる」上限の内側に閾値がある。 | 実データ上の推定法は別途必要。 |

## OQ Mapping Matrix

| OQ ID | external gap | candidate answer from Oblivion | anchors | answer type | grade | risk gate |
|---|---|---|---|---|---|---|
| `OQ-B01-002` | toy model の解析手法を frontier system の formal verification へ拡張できるか未確定。現実の NN 計算を symbolic code へ還元できる範囲も閉じていない。SOURCE: `2501.16496.txt:1514-1525` | toy model から frontier model への simplification が許容されるのは、2-simplex face 構造が forgetting functor を通じて faithful に保存されるときかつそのときのみ (II-T3.4.1 + VIII-Bridge)。symbolic reduction の限界は「どの face が保存されないか」の境界として定義できる。還元不能領域 = face が崩れる領域。 | `II-T3.4.1`, `II-Stability-Simplex`, `VIII-Bridge` | verification criterion (structural) | B | (a) frontier NN の 2-simplex face の同定法が外部 formal tool で存在しない。(b) simplex 構造と NN layer の対応付けを別途構成しないと比喩的主張に留まる。 |
| `OQ-B03-001` | (i) EXPSPACE-complete 検証を practical tools へ落とす symbolic technique 未発見 (SOURCE: `paper.txt:521-531`)。(ii) softmax / arbitrary-precision での succinctness gap 未確定 (SOURCE: `paper.txt:84-93`)。(iii) star-free regular を超える言語クラスへの拡張未閉鎖 (SOURCE: `paper.txt:477`)。 | U (compression = succinctness) の利得が doubly-exponential in n であり (Th.14/16, SOURCE: `paper.txt:425, 466`)、N (verification = EXPSPACE) のコストも doubly-exponential in n である (Th.5, SOURCE: `paper.txt:302-303`)。同じ n に対して両側が一致することは、U⊣N 随伴の経済的非対称性の complexity-theoretic matched bound として読める。VI-D2.1.1 (G∘F = U⊣N の随伴形) と IX-T1 (entropy 単調性) が内側で conceptual bridge を担う。ただし射程は UHAT (AC⁰・固定精度・star-free) 限定。 | `VI-D2.1.1`, `IX-D2`, `IX-T1`, `IX-P3.5.1` (loose: `IX-C1`) | complexity-theoretic matched bound (operationalizing U⊣N economy) | B+ (matched bound insight) / C+ (direct contact claim) | (a) UHAT の doubly-exponential gap が softmax に拡張できないことが証明された場合、matched bound claim は UHAT 専用に縮退する。(b) 実際の LLM (GPT/Claude) への適用は UHAT→softmax の別 complexity bridge が必要。(c) VI-D2.1.1 の U⊣N 随伴と UHAT の succinctness を等置していない — 経済性の複雑度理論的量化として読む。 |

## Candidate Answer Patterns

| pattern | description | key anchors | OQ IDs |
|---|---|---|---|
| **Structural face criterion for verification** | simplification (U) が許容されるのは、対象の minimal nontrivial face / bridge functor 構造が保存されるときかつそのときのみ。face が崩れた点が formal verification 不能境界になる。 | `II-T3.4.1`, `VIII-Bridge`, `II-Stability-Simplex` | `OQ-B01-002` |
| **Complexity-theoretic matched bound for U⊣N** | U-side (compression gain) と N-side (verification cost) が同じ complexity パラメータ n に対して doubly-exponential で一致する。これが U⊣N 随伴の経済的非対称性の complexity-level 量化。UHAT 射程内の最初の両側 formal bound。 | `VI-D2.1.1`, `IX-D2`, `IX-T1` + external: Bergsträßer et al. (2025) arXiv:2510.19315 Th.14/16 + Th.5 | `OQ-B03-001` |
| **Critical threshold inside the matched bound** | IX-P3.5.1 の critical forgetting threshold `α*(p)` は、doubly-exponential verification cost の内側で「まだ recoverability が残る」上限を与える。matched bound の下限側の構造的分析。 | `IX-P3.5.1`, `IX-T1` | `OQ-B03-001` (supplement) |

## Promotion Decision

| OQ ID | decision | 条件 |
|---|---|---|
| `OQ-B01-002` | anchor_pending — case seed | Face Lemma と frontier NN の形式的対応付けを mechanistic interpretability 論文の formal verification section (SOURCE: `2501.16496.txt:1514-1525` 周辺) で確認してから case 化。II-T3.4.1 の外部検証可能性が B → A- に上がれば case 化 → short note 候補。 |
| `OQ-B03-001` | mapped_draft (primary FORMAL-VERIF) + bridge to COMP-GEN | Child split (OQ-B03-001a/b/c/d) を次段で起票。a (practical verification) は Paper IV / IX の実験面に接続しやすい。b (softmax extension) は理論 debt として保持。c/d は QT-SYN-SEM / QT-COMP-GEN への delegate。 |

## Rejection Ledger

| rejected mapping | reason |
|---|---|
| `OQ-B01-002` を II-T3.4.1 で「完全に解決済み」扱い | Face Lemma は minimal face の保存条件を与えるが、frontier NN の2-simplex 同定法は外部 formal tool として存在しない。case 化には mechanistic interpretability 側の SOURCE 読みが必要。 |
| `OQ-B03-001` (UHAT) を一般 LLM の formal verification に適用 | UHAT = AC⁰ 内・固定精度・star-free 限定。GPT/Claude/Gemini は softmax attention で任意精度に近く、UHAT の complexity result を直接継承できない。UHAT→softmax の complexity-theoretic bridge は未確立。 |
| `VI-D2.1.1` G∘F 随伴と Bergsträßer et al. の succinctness を等置 | G∘F (U⊣N) の随伴と UHAT succinctness gap は構造的に analogous だが同一ではない。succinctness は情報損失なしの記述冗長圧縮 (U の真部分種)。等置せず「complexity-theoretic operationalization」として読む。 |

## Cross-type Notes

**QT-FORMAL-VERIF ∩ QT-COMP-GEN** (OQ-B03-001):
- `mapping_QT-COMP-GEN_2026-04-26.md` にすでに bridge anchor として登録済み (2026-04-27 追記)。
- 本ファイルが primary。COMP-GEN 側は「Kolmogorov source-thin gap への迂回 anchor」として detour 的に読む。
- Child split で a/c/d が COMP-GEN へ、b が FORMAL-VERIF 残留、a が OBS-ACCESS へ流れる見込み。

**QT-FORMAL-VERIF ∩ QT-SYN-SEM** (OQ-B03-001d 予告):
- UHAT-LTL bidirectional translation = formal syntax (LTL) と learned semantics (transformer attention) の bridge。
- Paper XI の C-E 分離 ($E_{\text{struct}}$ = 構造記法) との接続候補。
- typing_2026-04-27_batch03 の rank 2 (QT-SYN-SEM) anchor 探索はこのファイルでは未実施。QT-SYN-SEM mapping を別ファイルで起票するときに引き取る。

## Carry Forward

| rank | target | 理由 |
|---|---|---|
| 1 | OQ-B03-001 child split (a/b/c/d) 個別起票 | a = practical verification (Paper IV / IX 実験面)、b = softmax extension (理論 debt 保持)、c = star-free beyond、d = Zipf 哲学的接続 (QT-SYN-SEM / QT-COMP-GEN へ委譲) |
| 2 | OQ-B01-002 case 化 — `2501.16496.txt:1514-1525` SOURCE 精読 | face 同定法の具体的議論が外部論文にあれば II-T3.4.1 anchor を B→A- に昇格できる。contact candidate 化の前提。 |
| 3 | QT-SYN-SEM × QT-FORMAL-VERIF cross-type mapping | UHAT-LTL bridge と Paper XI $E_{\text{struct}}$ を接続するための専用 lane 起票。typing_2026-04-27_batch03 rank 2 anchor 探索の未完。 |
