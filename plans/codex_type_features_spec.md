# Type 1/2/3 状態の operational 特徴定義 — OP-X-5 Task 1 成果物

## §1 背景

Paper X §2 では、Case 1 "Mando" は直近の正しい手がかり `h_right` を保つ KLN のみ成功し、Type 1 = `recent useful clue` と整理される。Case 2 "live-crickets" は PDF ループを全忘却で断つ DA のみ成功し、Type 2 = `dead-end loop` と整理される。§2.3 はさらに Type 3 = `correct hypothesis, wrong action` を挙げ、Summary 単独では不十分だと述べる。命題 X.1 / X.2 の要点は、最適 CM 戦略は状態依存であり、Type 1 には弱い忘却 (KLN)、Type 2 には強い忘却 (DA)、Type 3 には中程度の忘却に加えて行動摂動が必要、ということである。

## §2 Type 1 特徴候補

| ID | 定義 (式または命題) | 計測方法 | 予測精度見込み | Label |
|:---|:---|:---|:---|:---|
| T1-1 recent-clue-hit | `x = 1[∃ c ∈ C_tail(k) : c ⇒ f_T or answer_T]`。最後 `k` ターン内に、最終 focus 仮説または最終解答へ接続される手がかりが存在する。 | `trajectory signature`。最後 `k=3..5` ターンから entity/span/action result を抽出し、最終 focus 仮説 `f_T` または最終解答との entailment / entity overlap を取る。合成データでは clue を埋め込んだ位置をそのまま supervision に使える。 | `0.68-0.75`。Type 2 とはかなり分離、Type 3 とは一部混同あり。 | `[SOURCE]` Paper X §2.1, §2.3 の「recent useful clue」と §3.2 の `tail_N` 保存をそのまま観測量へ落とした。 |
| T1-2 recent-clue-reuse | `x = (# reused clue tokens in last k turns) / (# clue tokens in last k turns)`。直近 clue の再利用率。 | `trajectory signature + embeddings`。最後 `k` ターンの clue 候補を抽出し、最終 2 ターンの reasoning / answer 内に再出現するかを cosine 類似度または entity exact match で測る。 | `0.64-0.72`。T1-1 より少し弱いが、純粋な repeat loop との分離に効く。 | `[TAINT with reasoning]` Paper X は clue の存在は述べるが、再利用率という proxy 自体は Codex 推論。 |
| T1-3 tau-tail-slope | `x = (1/(k-1)) Σ_{i=T-k+2..T} (τ_i - τ_{i-1})`。末尾の意味的密度 `τ` が上昇しているか。 | `context embedding`。各ターンの context embedding から task query / current focus への平均 cos 類似度を `τ_i` と近似し、末尾勾配を取る。 | `0.60-0.67`。Type 1 の recall 向上に寄与するが、モデル依存性がある。 | `[TAINT with reasoning]` §5.3 は `τ` を定義するが、「末尾勾配が Type 1 を示す」は本文の外挿。 |
| T1-4 summary-loss-risk | `x = 1[(c_recent survives tail_N) ∧ (c_recent disappears under σ or DA)]`。直近 clue が KLN では残るが要約 / 全忘却では消える。 | `trajectory signature + simulated summary`。最後 `k` ターンの clue を保持した `tail_N` と、summary 関数 `σ` または DA 後状態を比較し、clue retention を測る。 | `0.66-0.74`。Type 1 を `P-E2a/P-E2b` 側から補強できる。 | `[SOURCE]` §2.1 と §6.2 の `P-E2a/P-E2b` がそのまま retention 比較の形を与える。 |

## §3 Type 2 特徴候補

| ID | 定義 (式または命題) | 計測方法 | 予測精度見込み | Label |
|:---|:---|:---|:---|:---|
| T2-1 action-repeat-ratio | `x = max_a count(a in tail_k) / k`。同一 action が末尾 `k` ターンで何割を占めるか。`count(a) ≥ 3` なら強い Type 2 シグナル。 | `trajectory signature`。tool call / click / query / navigation を正規化して action label 化し、末尾頻度を数える。 | `0.75-0.85`。Case 2 の dead-end loop を最も直接に取る。 | `[SOURCE]` §2.2, §2.3 の「dead-end loop」をそのまま頻度指標にした。 |
| T2-2 dead-end-tail-retention | `x = 1[∃ subseq s ⊂ tail_k : s ∈ D]`。末尾 `k` ステップが既知 dead-end 集合 `D` に属する。 | `trajectory signature`。action-observation subsequence をハッシュ化し、`no progress` ラベル付き motif 辞書と照合する。合成データでは `D` を明示生成できる。 | `0.70-0.80`。Type 2 に対して強く、Type 1 の recent clue とは分離しやすい。 | `[SOURCE]` §3.1 の対象 `I=(q,H,C,D,f)` と §2.2 の「失敗パターンの最近 N ステップ」をそのまま使う。 |
| T2-3 loop-closure-score | `x = max_{j < T} cos(e(state_T), e(state_j))` under `Δprogress ≈ 0`。進捗なしで以前の状態に戻る度合い。 | `context embedding + trajectory signature`。state を `(focus hypothesis, active URL/tool, recent observation)` の embedding で表現し、過去状態との最大類似度を測る。 | `0.68-0.78`。repeat ratio より汎用的だが、埋め込み品質に依存。 | `[TAINT with reasoning]` 本文は loop を述べるが、closure score の計算法は Codex 推論。 |
| T2-4 tau-collapse | `x = 1[(mean τ_tail < τ_low) or (dτ/dt < 0)]`。末尾で意味的密度が低く、ノイズ主体になっている。 | `context embedding`。§5.3 の `τ` 近似を使い、末尾平均と勾配を測る。 | `0.58-0.66`。単独では弱いが、T2-1/T2-2 と合わせると安定。 | `[TAINT with reasoning]` §5.3 は `τ ↔ r` を予測するが、Type 2 の低密度 proxy は本文の外挿。 |

## §4 Type 3 特徴候補

Paper X は Type 3 を「correct hypothesis, wrong action」と命名し、Case 2 Summary 失敗を「正しい仮説 `h_right` は維持したが、行動レベルの変更を駆動できない」と描く。しかし本文は「仮説が正しい」の判定器も、「行動が不適切」の判定器も与えない。したがって Type 3 は raw trajectory だけから SOURCE 級に operationalize しにくい。以下はすべて proxy であり、外部 verifier・counterfactual probe・合成ラベルのいずれかを必要とする。Failure Condition に書かれた「測定不能の可能性」は、この段階ではまだ解消していない。

| ID | 定義 (式または命題) | 計測方法 | 予測精度見込み | Label |
|:---|:---|:---|:---|:---|
| T3-1 hyp-act-gap | `x = Q_hyp - Q_act`。仮説品質は高いが、実行 action 品質が低いとき大きい。 | `logits + embeddings`。`Q_hyp` は clue 集合 `C_t` に対する hypothesis entailment / logit margin、`Q_act` は current focus に対する action relevance または一歩先 reward 推定で近似する。 | `0.55-0.65`。Type 3 の core を最もよく表すが、scorer 依存。 | `[TAINT with reasoning]` 本文の semantic 記述を二つの score に分解したのは Codex 推論。 |
| T3-2 context-action-divergence | `x = 1 - cos(e(a_t), e(f_t ∪ C_t))` under high `Q_hyp`。正しい focus に対して action embedding が離れていく。 | `context embedding + action embedding`。focus hypothesis / clue summary の embedding と action phrase / tool call embedding の cos 距離を取る。 | `0.52-0.62`。cheap だが false positive が多い。 | `[TAINT with reasoning]` 本文は divergence 指標を持たない。 |
| T3-3 counterfactual-gain-gap | `x = V(a*_t | s_t) - V(a_t | s_t)` where `a*_t = argmax_a V(a | s_t)`。同じ state でより良い action が近傍にある。 | `logits`。候補 action top-k を生成し、small evaluator または policy head で一手先 gain を推定する。候補 action が無い場合は tool ontology の近傍で近似する。 | `0.58-0.66`。Type 3 recall を引き上げるが、実装コストが高い。 | `[TAINT with reasoning]` counterfactual probe 自体が本文外。 |
| T3-4 stable-hyp-zero-progress | `x = 1[(Var(e(h_{T-m..T})) < ε_h) ∧ (Δprogress_{T-m..T} ≤ ε_p)]`。仮説は安定しているのに進捗だけが止まる。 | `trajectory signature + embeddings`。仮説文または focus hypothesis の embedding 分散を測り、同じ窓で progress / novelty を測る。 | `0.54-0.61`。単独では弱いが、T3-1 と組み合わせると useful。 | `[TAINT with reasoning]` §2.2 の Summary failure を動的パターンへ外挿した proxy。 |

## §5 推奨特徴ベクトル

Task 2 に渡す feature vector は、Type ごとに別実装を持たせず、単一の `12` 次元ベクトルへ正規化しておくのがよい。各成分は `[0,1]` へ min-max または sigmoid で正規化し、欠損値は `NaN` ではなく `0.5` と `missing_mask` の別管理で扱う。

| dim | feature 名 | 対応候補 | 主信号 | 備考 |
|:---|:---|:---|:---|:---|
| 0 | `recent_clue_hit` | T1-1 | trajectory signature | binary |
| 1 | `recent_clue_reuse` | T1-2 | trajectory signature / embedding | ratio |
| 2 | `tau_tail_slope` | T1-3 | context embedding | signed を `[0,1]` に再スケール |
| 3 | `summary_loss_risk` | T1-4 | trajectory signature | binary or probability |
| 4 | `action_repeat_ratio` | T2-1 | trajectory signature | ratio |
| 5 | `dead_end_tail_retention` | T2-2 | trajectory signature | binary |
| 6 | `loop_closure_score` | T2-3 | context embedding | similarity |
| 7 | `tau_collapse_score` | T2-4 | context embedding | low-τ proxy |
| 8 | `hypothesis_confidence` | part of T3-1 | logits / entailment | `Q_hyp` 単体 |
| 9 | `action_relevance` | part of T3-1 | embedding / evaluator | `Q_act` 単体 |
| 10 | `hyp_act_gap` | T3-1 | derived | `Q_hyp - Q_act` |
| 11 | `counterfactual_gain_gap` | T3-3 | logits / evaluator | expensive, optional |

最小実装なら `dims 0..10` の `11` 次元でもよいが、Type 3 recall を確保したいなら `dim 11` を残す価値が高い。`stable_hyp_zero_progress` (T3-4) は `hypothesis_confidence`, `action_relevance`, `loop_closure_score` の組でかなり代替できるので、まずはベクトル本体へ入れず ablation 用の補助特徴に留めるのが安全。

## §6 予測精度見込み

60% 撤回条件を最も現実的に狙える feature set 候補は、以下の `8` 特徴である。

`F* = [recent_clue_hit, recent_clue_reuse, tau_tail_slope, action_repeat_ratio, dead_end_tail_retention, loop_closure_score, hyp_act_gap, counterfactual_gain_gap]`

見込み:

- 合成 trajectory が brief の生成方針どおりに `clue / loop / hyp-act mismatch` を明示埋め込みするなら、`LR` または `RF` で `accuracy 0.60-0.66`, `macro-F1 0.56-0.63` を期待できる。
- Type 1 / Type 2 は `0.70` 近い recall が見込める一方、Type 3 recall は `0.40-0.55` に留まる可能性が高い。

主なリスク:

1. Type 3 は SOURCE 級定義が無いため、proxy のラベルノイズで全体精度が 60% を割る可能性がある。
2. `τ` は §5.3 で定義されるが、実装上は embedding proxy なのでモデル依存性が強い。
3. `counterfactual_gain_gap` は logits または action candidates が無い trajectory では計測不能になる。
4. summary 系特徴は raw trajectory に summary snapshot が無い場合、別途 `σ` を再実行する必要があり、train/test leakage に注意が要る。

したがって、Task 2 ではまず `Type1 vs Type2` の分離が立つかを確認し、Type 3 が不安定なら `abstain / low-confidence` 分岐を残す設計が望ましい。

## §7 Task 2 (classifier.py 実装) への引き継ぎメモ

1. feature 抽出は `extract_features(trajectory) -> dict[str, float]` の純関数に分離し、分類器本体から切り離すこと。
2. `k` は固定値で決め打ちせず `k in {3, 5}` を config 化し、合成データ上で ablation できるようにすること。
3. `Q_hyp`, `Q_act`, `counterfactual_gain_gap` は missing が出やすいので、`missing_mask` を別に持つこと。欠損を 0 埋めすると Type 3 が偽陰性化しやすい。
4. `τ` 系特徴は embedding model 名を metadata に残すこと。Paper X §5.3 の議論上、ここは calibration 対象である。
5. 学習・評価では `per-type recall` を必ず出すこと。全体 accuracy だけだと Type 3 collapse を見落とす。
6. synthetic generator は brief の Task 3 方針どおり、Type 1 では `recent clue insertion`、Type 2 では `loop motif`、Type 3 では `correct hypothesis + irrelevant action` を個別制御できるようにすること。
7. 60% を下回った場合は、feature engineering の前に Type 3 ラベル定義を再点検すること。現時点の最大ボトルネックは classifier そのものより Type 3 operationalization 側にある。
