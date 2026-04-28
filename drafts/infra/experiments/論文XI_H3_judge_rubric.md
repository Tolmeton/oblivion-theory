# 論文XI — H3 clean-room judge rubric

**対象**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_h3_prompt_pairs.skeleton.jsonl`
**親計画**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/experiments/論文XI_H3_clean_room_replication_plan.md`
**役割**: H3 clean-room replication で、A/B の表記差を品質差と誤読しないための judge 契約を固定する。

## P-0 判定対象

H3 の主判定対象は、平均的な内容品質である。構造語彙の増加は別測定に送る。

| 面 | 測るもの | H3 での扱い |
|:---|:---|:---|
| content quality | 入力に対する正確性、論理一貫性、制約遵守 | 主判定 |
| structural realization | 記法、ラベル、座標語彙、XML 風構造 | H3-CR-1 の判定 |
| variance | 反復ごとのばらつき、judge disagreement | H3' の判定 |
| compliance | 指定 section や禁止事項の遵守 | 補助判定 |

## P-1 judge blind contract

Judge は条件 A/B を知らない状態で評価する。ただし出力面の記法差は完全には消せないため、次を明示する。

- 表記が専門的であることを加点しない。
- 見出しやラベルが整っていることを内容品質と混同しない。
- 入力にない事実を足した場合、見た目が整っていても減点する。
- 条件固有の語彙を使ったこと自体は、品質点ではなく structural realization へ送る。

## P-2 content quality score

各出力を 0-5 点で採点する。5 点満点は、入力だけから導ける範囲で、結論・根拠・不確実性・崩壊条件が揃う状態である。

| Score | 判定 |
|:---|:---|
| 5 | 入力に忠実で、結論・根拠・不確実性・崩壊条件がすべて明確 |
| 4 | 内容は正しいが、根拠または崩壊条件に軽い不足がある |
| 3 | 主結論は妥当だが、根拠の選別や不確実性が弱い |
| 2 | task の一部だけに答え、重要な制約または根拠を落とす |
| 1 | 入力から支えられない結論、重大な誤読、または禁止事項違反がある |
| 0 | task 不履行、空応答、外部情報依存、または評価不能 |

## P-3 submetrics

| Metric | Range | 評価対象 | H3 主指標 |
|:---|:---|:---|:---|
| `task_correctness` | 0-5 | task に直接答えているか | yes |
| `logical_consistency` | 0-5 | 結論と根拠が矛盾しないか | yes |
| `constraint_satisfaction` | 0-5 | 外部情報禁止、4 section、入力忠実性を守るか | yes |
| `assumption_tracking` | 0-5 | 入力内の仮定と不足を分けたか | yes |
| `failure_condition_quality` | 0-5 | 回答が崩れる条件を具体化したか | yes |
| `notation_density` | count | 構造記法・ラベル・座標語彙の量 | no |
| `section_compliance` | 0/1 | 4 section を満たしたか | auxiliary |
| `added_fact_count` | count | 入力にない事実を足した数 | penalty |

## P-4 aggregate rule

`content_quality` は次で計算する。

```text
content_quality =
  mean(task_correctness,
       logical_consistency,
       constraint_satisfaction,
       assumption_tracking,
       failure_condition_quality)
```

ただし `added_fact_count > 0` の場合、`content_quality` は最大 3 点に切る。外部情報依存が明確なら最大 1 点に切る。

## P-5 equivalence gate

H3 clean-room MVP では、A/B の平均差が次を満たすかを見る。

| Metric | equivalence margin |
|:---|:---|
| `content_quality` | ±0.25 |
| `task_correctness` | ±0.30 |
| `logical_consistency` | ±0.30 |
| `constraint_satisfaction` | ±0.25 |
| normalized added-fact penalty | ±0.05 |

Pass 条件:

1. structural realization で B > A が出る。
2. content quality の A/B 差が equivalence margin 内に入る。
3. TOST または $BF_{01}$ が帰無支持へ寄る。
4. judge family を変えても主判定が反転しない。

Fail 条件:

1. B が content quality を複数 domain で一貫して押し上げる。
2. C/E audit で B だけが追加手順や追加基準を持つ。
3. judge が表記整列を品質として採点している痕跡が出る。
4. 同等性検定が通らず、差の非検出に留まる。

## P-6 judge output schema

Judge は 1 出力につき次の JSON object を返す。

```json
{
  "task_id": "H3-PH-01",
  "input_id": "H3-PH-01.synthetic.v1",
  "generation_id": "M1.H3-PH-01.A.r01",
  "task_correctness": 0,
  "logical_consistency": 0,
  "constraint_satisfaction": 0,
  "assumption_tracking": 0,
  "failure_condition_quality": 0,
  "added_fact_count": 0,
  "section_compliance": 0,
  "notation_density": 0,
  "content_quality": 0,
  "judge_notes": ""
}
```

`judge_notes` は採点理由を短く残す。条件推定や好みの表記評価は書かない。

## P-7 human audit seed

Human audit は全件でなくてよい。MVP では各 domain から 1 task を抽出し、A/B 各 1 出力を読む。

Human audit の役割:

- rubric が表記好みを混入していないかを見る。
- added fact penalty が過剰または不足していないかを見る。
- judge disagreement が起きた task の原因を分類する。

## P-8 変更禁止

実行開始後に変えてはいけないもの:

- equivalence margin
- submetric list
- aggregate rule
- added fact penalty
- judge blind contract

変える場合は、旧 manifest を閉じ、新 manifest として再開始する。
