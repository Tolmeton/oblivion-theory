# Open Question Crosswalk

**状態**: internal workflow / 外部未解決問センサー
**入口**: `drafts/リファレンス/忘却論オンボーディング.md` §7.4 / §11.4
**置き場所**: `drafts/infra/open_question_crosswalk/`

## 目的

外部論文の open question / limitation / future work に対して、忘却論が候補回答・説明原理・検証可能な追加予測を提供できるケースを体系的に発掘する。

これは引用候補リストではない。外部論文を「未解決問センサー」として読み、忘却論側のどの定理・命題・仮説・実験面がその問いへ接続できるかを管理する内部制作線である。

## オンボーディングとの接続

`忘却論オンボーディング.md` は、この面を「外部 SOURCE 探索者ルート」として読むよう定めている。したがって本 README は、外部探索を related work 収集で止めず、次の変換を必ず通すための作業入口である。

```text
external unresolved point
  -> question typing
  -> Oblivion anchor
  -> candidate answer
  -> risk gate
  -> promotion target
```

入口判断は以下に固定する。

| 目的 | 使う面 |
|---|---|
| 番号・公開境界を決める | `plans/出版計画_忘却論シリーズ.md` |
| 忘却論側の anchor と主張水準を確認する | `drafts/リファレンス/統一記号表.md` |
| 既知批判や failure condition を確認する | `drafts/リファレンス/批判反証レジストリ.md` |
| 外部 open question を候補回答へ変換する | 本面 |

本面は外部論文の一覧ではない。外部側の未解決点と、忘却論側の anchor の対応を作れない項目は、`rejected` または `source_pending` として残す。

## 置き場所の理由

本面は公開シリーズでも公開番外編でもなく、外部 SOURCE の探索、未解決問の型分類、忘却論側 anchor の対応づけ、Gauntlet への昇格、contact 候補化を行う backstage である。したがって `drafts/infra/` 配下に置く。

## 対象

対象にするもの:

- 論文本文の explicit open question
- limitations / future work / unresolved problem
- 著者が説明不能・機構未解明・外部再現未確認として残した箇所
- 結果は強いが、なぜ成立するかの説明原理が薄い箇所
- 実験結果が忘却論側の theorem / proposition / hypothesis によって再読できる箇所

対象にしないもの:

- 単なる related work 収集
- 似ている語彙だけによる連想
- alphaXiv / NotebookLM の回答を SOURCE として固定すること
- 外部著者への contact を急ぐための宣伝メモ

## 運用フロー

| Step | 操作 | 成果物 |
|---|---|---|
| 1 | External intake | arXiv / DOI / PDF / repo から open question / limitation / future work を抽出する。alphaXiv や NotebookLM は TAINT 偵察に留め、PDF / DOI / local file を読んだ箇所だけ SOURCE に昇格する |
| 2 | Question typing | 未解決問を型に分ける。例: emergence, boundary failure, representation geometry, context degradation, prompt sensitivity, inverse recovery, scaling anomaly |
| 3 | Oblivion crosswalk | 忘却論側の anchor を対応づける。anchor は theorem / proposition / definition / hypothesis / experiment のいずれかとして主張水準を明示する |
| 4 | Candidate answer | 「忘却論ならどう答えるか」を 1-3 文で書く。ここでは証明ではなく、候補回答の形を固定する |
| 5 | Risk gate | overfit / vocabulary-only / source-thin / too-internal / premature-contact のリスクを記録する |
| 6 | Promotion | 強いものだけを SOURCE promotion、Gauntlet seed、related work patch、short note、direct contact candidate のいずれかへ昇格する |

各 step は省略しない。省略した場合、その候補は `mapped` ではなく `source_pending` または `mapped_draft` に留める。

## SOURCE / TAINT 規律

| 入力 | ラベル | 使い方 |
|---|---|---|
| arXiv PDF / DOI / local PDF の直読 | SOURCE | open question の quote、limitation、著者 claim の根拠 |
| local Oblivion draft の直読 | SOURCE | 忘却論側 anchor の根拠 |
| alphaXiv search / report / QA | TAINT: alphaXiv | 候補論文・読む箇所の探索 |
| NotebookLM | TAINT: NotebookLM | 内部 corpus の探索 |
| Pinakas seed | WEAK INPUT | 起点。内容は SOURCE で再確認する |
| Codex / Claude の推論 | TAINT: inference | crosswalk 仮説。SOURCE ではない |

## ファイル構成

| Path | 役割 |
|---|---|
| `domain_scope.md` | open question 採取対象分野と検索ハンドル |
| `intake/` | 外部論文から拾った open question / limitation / future work の一次採取ログ |
| `question_type_catalog.md` | 問いの型カタログ |
| `typing/` | intake batch ごとの問い型分類 |
| `mappings/` | 問い型ごとの忘却論 anchor 対応表 |
| `crosswalk_ledger.md` | 全体管理台帳 |
| `cases/` | 個別候補 case |
| `templates/case_template.md` | 新規 case の記入型 |

## 状態ラベル

| status | 意味 |
|---|---|
| seed | 起点だけある。SOURCE 読みは未完 |
| source_pending | 外部 PDF / local anchor の直読が未完 |
| mapped_draft | 問い型単位の初回対応づけがあり、個別 case 昇格前 |
| mapped_index | 複数 lane / batch を横断して、OQ と忘却論 anchor の粗対応表がある |
| mapped | open question と忘却論 anchor の対応が書けた |
| case_draft | 外部 quote と忘却論 anchor を個別 case で対置したが、Gauntlet 前 |
| gauntlet | 反論・過剰接続・主張水準の検査中 |
| gauntlet_passed | 初回 Gauntlet を通過し、撤回条件と残 debt が明示された |
| experiment_scaffolded | 実験 protocol / smoke artifact が作られたが、主要 recovery gate は未通過 |
| recovery_passed | α=0/λ=0 回復ゲートを通過したが、非ゼロ α の方向制御は未検証 |
| direction_control_case | Fisher 半径固定のまま非ゼロ α が表現軌道を動かす probe を通過した |
| oblivion_sam_case | λ 忘却項が精度を大きく壊さず表現プロファイルを動かす probe を通過した |
| note_ready | short note / related work patch にできる |
| contact_candidate | direct contact の候補 |
| rejected | vocabulary-only / source-thin / overfit 等で棄却 |

## Risk gate

候補を `gauntlet_passed` 以上へ上げる前に、以下を明示する。

| risk | 検出条件 | 処置 |
|---|---|---|
| overfit | 外部論文 1 本にだけ都合よく合う | 別論文か別ドメインで同型の open question を探す |
| vocabulary-only | 語彙が似ているだけで機構が対応しない | `rejected` または `source_pending` に戻す |
| source-thin | 外部 quote または local anchor の直読がない | SOURCE 読みへ戻す |
| too-internal | 忘却論内部語だけで外部読者に通じない | candidate answer を外部語彙で 1 文化する |
| premature-contact | 著者 contact だけが先行している | `contact_candidate` へ上げず、Gauntlet と failure condition を先に書く |

## Promotion ladder

昇格先は 1 つに固定しない。候補の強さに応じて、次のどれへ渡すかを決める。

| promotion target | 条件 | 渡し先 |
|---|---|---|
| SOURCE promotion | 外部 quote と local anchor が両方 SOURCE 化された | `crosswalk_ledger.md` / `mappings/` |
| Gauntlet seed | 候補回答は強いが反論処理が未完 | `cases/` |
| experiment scaffold | recovery gate や smoke test が必要 | `drafts/infra/experiments/` / `experiments/` |
| related work patch | 既存 paper の文献節へ入れるだけで効く | 対象 paper 本文 + meta |
| short note | 独立短報にできる | `drafts/standalone/` 候補 |
| direct contact candidate | failure condition と残 debt が明示されている | contact 用メモ |

## よくある事故

### related work リスト化

外部論文を並べただけで、open question と忘却論 anchor を対応づけていない状態。
復旧: 外部 quote、question type、local anchor、candidate answer、risk gate を 1 行ずつ埋める。

### SOURCE / TAINT 混合

alphaXiv や NotebookLM の回答を、そのまま外部著者 claim として扱う状態。
復旧: PDF / DOI / local file の直読箇所だけを SOURCE とし、探索出力は TAINT として残す。

### premature-contact

外部著者へ送ることが目的化し、failure condition や残 debt を書かない状態。
復旧: `gauntlet` へ戻し、撤回条件と未検証点を先に記録する。
