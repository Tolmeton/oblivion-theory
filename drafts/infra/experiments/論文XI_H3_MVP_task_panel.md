# 論文XI — H3 clean-room MVP task panel

**親計画**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/experiments/論文XI_H3_clean_room_replication_plan.md`
**機械 skeleton**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_h3_prompt_pairs.skeleton.jsonl`
**目的**: H3 clean-room replication の MVP で使う 5 domains × 4 tasks を固定し、各 task の A/B prompt pair が同一 C を保つかを先に監査する。

## P-0 panel contract

- 条件 A = 自然言語のみの prompt。記法は平易な見出しと番号に限定する。
- 条件 B = 同じ制約を構造記法 / CCL / 座標語彙で表す prompt。手順数、要求、評価基準は増やさない。
- 入力は `{INPUT}` として外部から注入する。prompt pair 内に task 固有の追加知識を混ぜない。
- 各 task は `answer_format`, `quality_rubric`, `forbidden_moves` を A/B で同一にする。
- B が増やしてよいものは `labels`, `phase markers`, `coordinate vocabulary`, `notation density` だけである。

## P-1 MVP task list

| ID | Domain | Task type | Fixed C | H3 observation |
|:---|:---|:---|:---|:---|
| H3-PH-01 | Philosophy / theory | argument audit | 主張・根拠・反証条件を分ける | E が抽象論証の平均品質を上げるか |
| H3-PH-02 | Philosophy / theory | concept boundary | 概念 A/B の境界と混同リスクを出す | E が境界設定品質を上げるか |
| H3-PH-03 | Philosophy / theory | objection map | 反論を強度順に並べ応答方針を出す | E が反論発見率を上げるか |
| H3-PH-04 | Philosophy / theory | thesis compression | 長い議論を核命題へ圧縮する | E が圧縮品質を上げるか |
| H3-MA-01 | Math-lite reasoning | proof sketch audit | 証明スケッチの前提・飛躍・未証明点を出す | E が proof audit を平均的に上げるか |
| H3-MA-02 | Math-lite reasoning | counterexample search | 命題への反例候補と成立条件を出す | E が反例発見を上げるか |
| H3-MA-03 | Math-lite reasoning | definition refinement | 曖昧定義を操作的定義へ直す | E が定義精度を上げるか |
| H3-MA-04 | Math-lite reasoning | dependency graph | 命題群の依存関係を DAG 的に整理する | E が依存整理を上げるか |
| H3-CR-01 | Code review | bug/risk finding | 振る舞いリスク・欠けたテスト・境界条件を出す | E が発見率を上げるか |
| H3-CR-02 | Code review | patch critique | diff の意図・副作用・rollback を評価する | E が副作用検知を上げるか |
| H3-CR-03 | Code review | test gap audit | 実装に対する missing tests を出す | E が test gap 品質を上げるか |
| H3-CR-04 | Code review | API contract audit | API 入出力契約の破れを探す | E が契約監査を上げるか |
| H3-PL-01 | Planning | constrained plan synthesis | 目的・制約・手順・検証を計画化する | E が計画品質を上げるか |
| H3-PL-02 | Planning | risk-first plan | 先にリスクと撤回条件を固定する | E がリスク設計を上げるか |
| H3-PL-03 | Planning | resource allocation | 3案を比較し優先順位を出す | E が配分判断を上げるか |
| H3-PL-04 | Planning | experiment plan | 仮説・指標・pass/fail を作る | E が実験設計を上げるか |
| H3-CL-01 | Classification | rubric labeling | 与えられた rubric で分類し根拠を出す | low-complexity で E 差が出るか |
| H3-CL-02 | Classification | severity ranking | 問題を severity 順に並べる | E が順位付けを上げるか |
| H3-CL-03 | Classification | source/inference split | 文を SOURCE/INFERENCE/TAINT に分ける | E がラベル精度を上げるか |
| H3-CL-04 | Classification | claim strength labeling | 主張を定理/命題/仮説/予想に分ける | E が claim strength 判定を上げるか |

## P-2 shared answer contract

全 task で A/B に共通する出力契約:

1. `Answer`: 結論または分類。
2. `Reasons`: 主要根拠 3 点以内。
3. `Uncertainty`: 未確定点または不足情報。
4. `Failure condition`: この回答が崩れる条件。

全 task で禁止するもの:

- 入力にない事実の追加。
- 外部検索。
- hidden policy / safety commentary。
- A/B 条件で手順数を変えること。
- B だけに追加検査を入れること。

## P-3 prompt pair skeleton

### A prompt skeleton

```text
You will receive an input.
Perform the task described in TASK.
Use the same four sections in your answer:
1. Answer
2. Reasons
3. Uncertainty
4. Failure condition

Do not use external sources.
Do not add facts not present in the input.
Keep the answer concise and evaluable.

TASK:
{TASK}

INPUT:
{INPUT}
```

### B prompt skeleton

```text
<task_contract>
  <goal>{TASK}</goal>
  <constraints>
    - external_sources: forbidden
    - new_facts_not_in_input: forbidden
    - answer_surface: four_sections
  </constraints>
  <output>
    S1 Answer
    S2 Reasons
    S3 Uncertainty
    S4 Failure condition
  </output>
</task_contract>

<input>
{INPUT}
</input>
```

## P-4 C/E separation audit

| Audit item | A | B | Status |
|:---|:---|:---|:---|
| Goal | `{TASK}` | `{TASK}` | C fixed |
| Evidence rule | no external sources | external_sources forbidden | C fixed |
| New fact rule | no added facts | new_facts_not_in_input forbidden | C fixed |
| Output sections | 4 sections | 4 sections | C fixed |
| Concision | concise and evaluable | four_sections, no expansion | C fixed |
| Notation | prose | XML-like contract + S labels | E changed |
| Section labels | natural language | symbolic phase labels | E changed |

## P-5 readiness gate

MVP generation に進む前に満たす条件:

1. `experiments/paper_xi_h3_prompt_pairs.skeleton.jsonl` が 20 task records を持つ。
2. 各 record が `task_id`, `domain`, `task_type`, `task`, `condition_a_prompt`, `condition_b_prompt`, `c_e_audit` を持つ。
3. JSONL parse が通る。
4. 3 records を dry-run し、runner が `{INPUT}` を注入できる。
5. judge rubric を別ファイルへ固定する。

## 次の一手

1. judge rubric を作る。
2. `paper_xi_h3_clean_room_manifest.yaml` を作る。
3. 3 task の dry-run manifest を切る。
