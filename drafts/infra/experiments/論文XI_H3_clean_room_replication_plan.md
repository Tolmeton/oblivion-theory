# 論文XI — H3 clean-room replication 計画書

**対象論文**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.md`
**対象節**: §7.5-§7.6, §7.9, §10 Open Problems
**対象命題**: H3 / C2 — 制約 $C$ を固定したとき、符号化 $E_{\text{struct}}$ は平均推論品質を押し上げず、主に語彙空間を変える。
**目的**: 現行の「差の非検出」寄りの帰無結果を、clean-room 条件と同等性検定で一段だけ実へ引く。

## P-0 実験空間

### 0.1 現行結果の SOURCE

- Exp0: 構造語彙 Cohen's d = 8.73、推論品質 d ≈ 0。
- CC Agent 再現: H3 の平均帰無側を再現。ただし共通 HGK context が強い $C$ 成分として混入しうる。
- Gemini 検証: N=50/条件で構造語彙 d=8.62、内容指標 `axiom_ratio / assumption_count / bond_count` は帰無。
- 本文 §7.5.4 の未解決点: 小サンプル、1 動詞、共通 HGK context、未測定品質次元、同一ファミリー judge、TOST / $BF_{01}$ 未実施。

### 0.2 clean-room 原則

1. **共通 HGK context を外す**
   Agent 環境ではなく、条件プロンプトのみを渡す CLI single-shot で実行する。NVIDIA NIM / Google Vertex は、CLI runner の backend API としてのみ使う。

2. **$C$ と $E_{\text{struct}}$ を事前固定する**
   事後的に「効いたものは C だった」と再分類しないため、各 prompt pair の C/E 分離表を先に作る。

3. **評価者を生成モデル family から切る**
   生成モデルと同一 family の judge だけで品質を評価しない。cross-family LLM judge と human audit seed を分ける。

4. **帰無を正に支持する検定を入れる**
   Welch t-test だけでなく、主要指標ごとに equivalence margin を事前登録し、TOST と $BF_{01}$ を併記する。

5. **平均と分散を分ける**
   H3 は平均品質の命題、H3' は分散構造の命題として別判定にする。

## P-1 仮説と反証条件

### 1.1 主仮説

- **H3-CR-1 構造伝搬**: $E_{\text{struct}}$ は構造語彙指標を大きく変える。
- **H3-CR-2 平均品質帰無**: $C$ 固定時、主要内容品質指標の平均差は equivalence margin 内に留まる。
- **H3-CR-3 model-invariance**: provider / model family が変わっても、構造伝搬と平均品質帰無の分離は維持される。
- **H3-CR-4 層分離**: 分散差が出ても、それは H3 の反証ではなく H3' の判定面へ送る。

### 1.2 反証条件

次のいずれかが起きたら、H3 は「大規模モデル一般」ではなく条件付き命題へ縮退する。

1. clean-room 条件で `E_struct` が主要品質指標の平均を一貫して押し上げる。
2. 小規模モデルまたは浅い task でのみ平均差が出る場合、H3 は「十分強い C / 十分大きいモデル」条件付きへ縮退する。
3. C/E 分離表で「E-only」とした差分に、実質的な手順・禁止・評価基準の差が混入している。
4. judge を変えると帰無が消える。
5. TOST / $BF_{01}$ が帰無支持を与えず、「差の非検出」以上に進めない。

## P-2 prompt pair 設計

### 2.1 条件

| 条件 | 内容 | 役割 |
|:---|:---|:---|
| A | plain natural language | $E_{\text{NL}}$ |
| B | structural notation / CCL / coordinate syntax | $E_{\text{struct}}$ |

両条件で固定するもの:

- task goal
- input information
- required output sections
- forbidden behavior
- reasoning budget
- token ceiling
- examples count
- judge-facing rubric

変えてよいもの:

- labels
- layout
- notation
- phase marker syntax
- coordinate vocabulary

変えてはいけないもの:

- 手順数
- 評価基準
- required evidence
- uncertainty reporting requirement
- allowed tools
- answer length

### 2.2 C/E 分離表

各 prompt pair は、実行前に次の表を持つ。

| 項目 | A | B | 判定 |
|:---|:---|:---|:---|
| task goal | same | same | C fixed |
| procedure | same | same | C fixed |
| constraints | same | same | C fixed |
| output schema | same | same | C fixed |
| notation | NL | structural | E changed |
| labels | plain | CCL / coordinate | E changed |
| token budget | same | same | control |

この表で `C fixed` が成立しない pair は H3 clean-room から除外する。

## P-3 task panel

### 3.1 MVP panel

| Domain | Task type | H3 で見るもの |
|:---|:---|:---|
| Philosophy / theory | argument audit | 抽象推論で E が平均品質を上げるか |
| Math-lite reasoning | structured proof sketch | 記法が proof quality を平均的に押し上げるか |
| Code review | bug/risk finding | 実務推論で E が発見率を変えるか |
| Planning | constrained plan synthesis | C 固定時に E が計画品質を上げるか |
| Classification | rubric-based labeling | low-complexity task で E 差が出るか |

MVP は 5 domains × 4 tasks × 2 conditions × 3 models × 3 repeats = 360 generations を上限にする。

### 3.2 Full panel

MVP で実行面が安定した後のみ、各 domain 10 tasks へ拡張する。Full は実行前に別 manifest を作る。

## P-4 model / judge 設計

### 4.1 generator models

最低 3 family:

- Anthropic 系: Claude Sonnet anchor
- Google 系: Gemini anchor
- NVIDIA NIM または open-weight 系: 第 3 family
- Google Vertex で利用できる Gemini / Model Garden 系は、Google family の CLI backend として扱う。

温度と sampling:

- temperature = 0
- top_p = 1
- tool use = off
- browsing / retrieval = off
- max output tokens = pair ごとに固定

### 4.2 judge panel

| Judge | 役割 | 注意 |
|:---|:---|:---|
| cross-family LLM judge | 全件の 1st pass | generator と同一 family を避ける |
| second LLM judge | disagreement audit | 主要指標のみ |
| human audit seed | calibration | 全件でなく subset でよい |
| automatic counters | structural metrics | judge ではなく補助測定 |

Blind condition:

- judge には A/B ラベルを見せない。
- condition-specific notation は出力から完全には消せないため、品質 rubric は notation preference を評価対象から外す。
- judge prompt は「表記の専門性」ではなく、内容正確性・制約遵守・論理一貫性を評価する。

## P-5 metrics

### 5.1 structural metrics

- `total_structural`
- `rho_notation`
- `U_labels`
- `categorical_vocab`
- CCL / coordinate marker count

期待:

- B >> A
- Cohen's d は大きい

### 5.2 content quality metrics

主指標:

- logical consistency
- task correctness
- constraint satisfaction
- assumption tracking
- evidence use

補助指標:

- axiom_ratio
- assumption_count
- bond_count
- error count
- hallucinated citation count

期待:

- A ≈ B
- 主要指標が equivalence margin 内

### 5.3 variance metrics

- per-task score variance
- repeated-run variance
- structural marker variance
- disagreement rate between judges

扱い:

- 平均差は H3。
- 分散差は H3'。
- 両者を混ぜない。

## P-6 統計判定

### 6.1 事前登録する equivalence margin

初期案:

| 指標 | equivalence margin |
|:---|:---|
| 5-point quality score | ±0.25 |
| normalized content score | ±0.05 |
| error count | ±0.20 SD |
| constraint satisfaction | ±5 percentage points |

この margin は実行前に固定する。結果を見てから動かさない。

### 6.2 判定セット

- Welch t-test: 差の探索
- TOST: 同等性検定
- $BF_{01}$: 帰無支持のベイズ因子
- Brown-Forsythe: 分散差
- Cohen's d: effect size

### 6.3 pass / fail

| 判定面 | Pass | Fail |
|:---|:---|:---|
| 構造伝搬 | structural metrics で B >> A | B が A と同等 |
| 平均品質帰無 | TOST pass かつ $BF_{01}$ が帰無支持 | 平均品質で B > A が一貫 |
| model-invariance | 3 family 中 2 family 以上で同方向 | family ごとに真逆 |
| C/E purity | 全 pair の C/E 分離表が pass | 重要 pair に C 差混入 |
| judge stability | judge 間で結論一致 | judge family 依存で結論反転 |

## P-7 execution manifest

実行時に次を JSON / YAML で固定する。

```yaml
experiment_id: paper_xi_h3_clean_room
target_claim: H3
conditions:
  A: E_NL
  B: E_struct
fixed_C_contract: true
models:
  - provider: anthropic
    model: claude-sonnet-4-6
  - provider: google
    model: gemini-3.1-pro-preview
  - provider: third_family
    model: selected_before_run
sampling:
  temperature: 0
  top_p: 1
  tools: false
  retrieval: false
metrics:
  structural:
    - total_structural
    - rho_notation
    - U_labels
  quality:
    - logical_consistency
    - task_correctness
    - constraint_satisfaction
    - assumption_tracking
  statistics:
    - welch
    - tost
    - bf01
    - brown_forsythe
pre_registered_margins:
  quality_5pt: 0.25
  normalized_content: 0.05
```

## P-8 成果物

| 成果物 | 用途 |
|:---|:---|
| `paper_xi_h3_prompt_pairs.jsonl` | C/E 分離済み prompt pairs |
| `paper_xi_h3_clean_room_manifest.yaml` | 実行条件の固定 |
| `paper_xi_h3_generations.jsonl` | raw generations |
| `paper_xi_h3_judge_scores.jsonl` | blind judge scores |
| `paper_xi_h3_metrics.csv` | aggregate metrics |
| `paper_xi_h3_result.md` | 本文反映用の結果報告 |

## P-9 収穫パターン

| パターン | 観測 | 解釈 | 本文処置 |
|:---|:---|:---|:---|
| P1 | B は構造語彙だけ増え、品質は TOST pass | H3 強化 | 「平均帰無」を帰無支持へ上げる |
| P2 | B は品質も上げる | H3 反証または条件付き化 | `E_struct` と暗黙 C の混入を再監査 |
| P3 | 小規模モデルだけ B > A | H3 は model-size 条件付き | 反証条件 (1) を本文へ昇格 |
| P4 | 分散のみ変わる | H3' 強化 | 平均と分散の二層結果として書く |
| P5 | judge により反転 | 評価系交絡 | judge 設計を結果本文より先に修正 |

## 次の一手

1. MVP の 5 domain × 4 tasks を具体化する。
2. 各 task について A/B prompt pair と C/E 分離表を作る。
3. judge rubric を 1 枚に固定する。
4. manifest を作り、dry-run で schema だけ検証する。
5. dry-run が通ったら MVP generation へ進む。
