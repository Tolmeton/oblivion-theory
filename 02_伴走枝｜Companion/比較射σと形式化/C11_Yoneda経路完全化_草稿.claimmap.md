# C11_Yoneda経路完全化_草稿 — 命題依存台帳

- title: C11_Yoneda経路完全化_草稿
- meta_file: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.meta.md
- source_files:
  - /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.meta.md
  - /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md
- source_resolution: resolved; same-basename manuscript exists and was read.
- status: initial claimmap; meta + manuscript backed
- scope_note: C11 proof companion の claim を、stage generation gap・定理 statement・外部 SOURCE ledger へ接続する。

## 命題台帳

| ID | 命題 | 役割 | 命題動詞 | 強度 | 依存元 | 充足条件 | 渡し先 | SOURCE | 禁止含意 |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| C11-A | Yoneda 経路完全化は、比較射σの統一定理 v0.6 の C11 proof companion である。 | companion 位置 | 位置づける | resolved source | parent theorem, meta | v0.6 本体と proof companion の関係が明示されること。 | C11-B/C11-C | /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.meta.md:20<br>/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md:10 | v0.6 本体の全 gap を解消済みとは言わない。 |
| C11-B | C11-Y は weak spherical 2-category と SignTower から Yoneda 経路を完全化する。 | theorem core | 構成する | sketch-level theorem | SignTower, weak spherical 2-category | statement の条件表・proof obligations が満たされること。 | C11-C | /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.meta.md:21<br>/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md:20<br>/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md:34 | proof obligations 未充足のまま完全証明と呼ばない。 |
| C11-C | proof obligations は Gurski extraction、Lack route、T_sph 構成へ分解される。 | 証明分解 | 分解する | obligations open | C11-B | 外部 SOURCE と内部構成の対応を閉じること。 | external source ledger | /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.meta.md:22<br>/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md:59 | 外部文献名の列挙を証明完了と扱わない。 |
| C11-Gurski | Gurski extraction は weak 3-category / tricategory 側の外部 SOURCE から spherical route を支える。 | 外部 SOURCE | 借用する | source candidate | C11-C | Gurski の該当命題と本稿の使用点を line-backed にすること。 | C11-B proof | /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md:90 | Gurski から本稿定理が自動的に従うとは言わない。 |
| C11-Lack | Lack route は coherence / icon 側の候補経路である。 | 外部 route | 借用する | source candidate | C11-C | route の前提が weak spherical 2-category に適合すること。 | C11-B proof | /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md:104 | Lack route を本稿の完成済み内部証明として扱わない。 |
| C11-Tsph | T_sph table は theorem の構成要素を一覧化するが、standalone paper 化には追加作業が要る。 | 構成表 | 一覧化する | scaffold | C11-B/C11-C | table 各行の定義・依存・証明責務を補うこと。 | standalone candidate | /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md:123<br>/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/companion/比較射σと形式化/C11_Yoneda経路完全化_草稿.md:154 | table があるだけで standalone proof と見なさない。 |

## 編集前照合ゲート

- v0.6 本体を編集する前に、C11-B の proof obligation がどこまで閉じたかを確認する。
- 外部 SOURCE は route 候補であり、直接の証明代替ではない。
- C11 proof companion は resolved source だが、proof 完了状態は unresolved。

## 未解決

- Gurski/Lack の原典 line-backed 対応は未作成。
- theorem statement の各条件に対する内部証明責務が未充足。
