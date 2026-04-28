# Open Question Crosswalk — Intake Batch 03

- 作成日: 2026-04-27
- 目的: 2026-10 月公開の transformer formal-language 理論論文から、忘却論側の `QT-FORMAL-VERIF ∩ QT-COMP-GEN ∩ QT-SYN-SEM` 三重交点に着地する未解決問・限界・帰結を採取する。
- 範囲: 単独論文 batch。Bergsträßer-Cotterell-Lin (2025) は LTL/RNN/automata に対する transformer succinctness を初めて両側 doubly-exponential bound で量化した。
- SOURCE 規律: ローカル `pdftotext -layout` で抽出した本文を SOURCE とする。NotebookLM / alphaXiv は使っていない。
- まだ行わないこと: 個別 case 化、contact 判断、Paper IX/XI 本文への記述追加。

## Intake Table

| ID | source | 分野 | 影響力の理由 | 拾った open question / limitation / future work | evidence |
|---|---|---|---|---|---|
| OQ-B03-001 | [Transformers are Inherently Succinct](https://arxiv.org/abs/2510.19315) | formal language theory / transformer / verification | UHAT (固定精度) が LTL に対し指数、DFA に対し二重指数 succinct であることを初めて両側 bound で示し、検証問題が EXPSPACE-complete であることを証明した代表的論文。Yang et al. (2024) の language-class equivalence を size measure へ昇格させた。 | (i) future work: EXPSPACE-complete を実機検証へ落とすための symbolic technique / simulation の探索 (cf. VNN competition)。(ii) limitation: 結果は UHAT (最弱クラス, AC⁰ 内) と固定精度に閉じている。softmax / average-hard / arbitrary-precision での succinctness gap は未確定。(iii) limitation: star-free regular language への閉じ込み — RNN は全 regular を認識するため、succinctness は「より小さい言語クラスでの記述効率」として量化される。(iv) 著者自身の哲学的注釈: succinctness は Zipf の略語法則・Hindu-Arabic vs Roman 数字の延長で「現代数学・計算機科学を可能にした記述効率」 — 著者は claim level を抑えているが、忘却論側からは強い prior 候補として読める。 | SOURCE: `_sources/arxiv_2510_19315/paper.txt:50-58` (主結果), `:84-93` (UHAT 仮定), `:425` (Th.14 LTL 指数 gap), `:466` (Th.16 DFA 二重指数 gap), `:477` (Cor.17 RNN 指数 gap), `:302-303` (Th.5 EXPSPACE-complete), `:486` (Th.18 equivalence EXPSPACE-complete), `:515-519` (Zipf / Hindu-Arabic 解釈), `:521-531` (future work: practical verification) |

## Not Retained In This Batch

- 本論文の Appendix A (Lemma 9 / Proposition 6 / Proposition 12 の完全証明) は SOURCE として保存しているが intake には抽出しない。本文骨格が SOURCE として十分。Appendix への踏み込みは個別 case 化時に行う。
- 著者引用の周辺研究 (Sälzer et al. 2025 NEXP-hard, Yang et al. 2024 doubly-exponential UHAT→LTL, Jerad et al. 2025 LTL fragment) は別 OQ として独立採取する価値があるが、本 batch では本論文の上位 bound としての位置づけのみ記録。

## SOURCE / TAINT 規律

| 入力 | ラベル | 使用 |
|---|---|---|
| `_sources/arxiv_2510_19315/paper.txt` (本文 920 行) | SOURCE | open question / limitation / future work の根拠 |
| `_sources/arxiv_2510_19315/abstract.html` | SOURCE | metadata (title / authors / date / categories) |
| HGK ECC ベクトル検索 (mcp__aisthetikon__notebook) | TAINT (hit count 0) | 偵察として使用したが結果未使用 |
| `drafts/series/論文XI_*` / `論文IV_*` / `infra/open_question_crosswalk/*` の grep | SOURCE | 接続候補同定の根拠 |
