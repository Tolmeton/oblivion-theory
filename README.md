# 忘却論｜Oblivion

このディレクトリは、忘却論の公開候補と内部制作線を分離して管理する。
公開・編集導線の主入口は4つに固定し、それ以外の作業面は補助面として分けて扱う。

新規参加者・新規エージェントは、まず `drafts/リファレンス/忘却論オンボーディング.md`
を読む。番号、記号、批判、横断 blocker、外部 open question、incubator のどの面を
どの正本へ戻すかは、オンボーディング側に集約する。

## 4つの主入口

### 1. 公開シリーズ

- `drafts/series/`
- 正本は `論文0_忘却の忘却_草稿.md` と `論文I` から `論文XIV` までの数字付き系列。
- 各番号につき正本は1ファイルだけに固定する。

### 2. 公開番外編

- `drafts/standalone/`
- 独立公開候補を置く。
- 単独稿だけでなく、忘却論から派生した衛星クラスタもここに置く。
- 現物確認できる補助クラスタは `drafts/standalone/automath_bridge/` と
  `drafts/standalone/math_oblivion_reading/`。
- `automath_bridge/` 由来の Paper XIV は series 昇格済み。由来と現行公開境界を混ぜない。
- 昇格条件は以下の3点:
  - 単独要旨が書ける
  - シリーズ本文を前提にしない最小定義がある
  - 参考文献と主張水準ラベルが自前で閉じる

### 3. 内部インフラ

- `drafts/infra/`
- `plans/出版計画_忘却論シリーズ.md`
- 出版順・系列番号・公開境界の正本は `plans/出版計画_忘却論シリーズ.md`。
- 記号・定理索引の正本は `drafts/リファレンス/統一記号表.md`。
- 新規参加者向け導入は `drafts/リファレンス/忘却論オンボーディング.md`。
- 外部 open question を忘却論側の候補回答へ接続する内部 workflow は
  `drafts/infra/open_question_crosswalk/README.md`。
- Face Lemma の概念入口は `drafts/リファレンス/FaceLemma.md`。
  符号理論対応・修復可能性設計・calculations 進捗を含む backstage は
  `drafts/incubator/FaceLemma_技術設計.md`。
- `drafts/リファレンス/モノグラフ構成設計.md` は
  モノグラフ線だけでなく、シリーズ横断 blocker / anomaly / readiness を
  束ねる系列統制ハブでもある。現時点では内部制作線であり公開正本ではない。

### 4. インキュベータ

- `drafts/incubator/`
- incubator は常置場ではなく、proof seed / bridge note / technical design /
  draft embryo / legacy の staging 面として扱う。
- index と昇格ゲートは `drafts/incubator/README.md` を正面入口にする。
- `legacy/` は公開レイヤから外した履歴置き場であり、
  現行の保持対象は `legacy/力とは忘却である_v2.md`。
- seed を本文へ戻す前に、主張水準、昇格先、SOURCE、failure condition を確認する。

## 補助作業面

- `calculations/` は計算ノート、証明パッチ、数値実験レポートを置く補助面。
- `experiments/` は実験設計・実験用チェックリストの補助面。
- `drafts/リファレンス/熱力学対応表.md` は熱力学対応表のリビングノートであり、
  4レイヤの入口には数えない。
- `Ξ計算_軌跡から不均一度.py` は補助計算スクリプトであり、公開系列や番外編の正本ではない。

## 命名と非推奨

- `Oblivion/` 内部の案内文書では、経路表記の正規形を
  `README.md`, `drafts/...`, `plans/...`, `calculations/...`, `experiments/...`
  にそろえる。
- 旧 `drafts/infra/*.md` 参照が残っている場合、正本 alias は
  `drafts/リファレンス/忘却論オンボーディング.md` の
  legacy 対応表を参照する。
- 実際に相対リンクとして解決する必要がある Markdown link だけは、ファイル相対パスを使ってよい。
- `paper_IV_draft.md` は廃止。正本は `drafts/series/論文IV_なぜ効果量は小さいか_草稿.md`。
- `drafts/` 直下に公開候補の `.md` を戻さない。新規文書は最初から4レイヤのどこに置くかを決める。
- `monograph_design.md` は旧版アーカイブであり、長期設計の正本ではない。
