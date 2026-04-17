# Handoff Drift operational 写像 — OP-X-6 / OP-XII-6 Task 1 成果物

## §1 背景

brief は `boot⊣bye` サイクルで測るべき 2 速度を LLM handoff へ operational に写せと要求する。Paper X §4 は handoff を `Ses →[bye]→ Mem →[boot]→ Ses` と捉え、Drift を `1 - Recall(Handoff)` と読む。Paper XII §3-§5 は `χ = V_null / V_carrier` を、欠如境界の速度と担体 front の速度の比として定義し、Hyphē では `X = turn / memory slot / retrieval coordinate`, `Δ = semantic separability / retrievability gap`, `C = retrievable useful memory flow` と置けるとした。したがって Task 1 の核心は、handoff 後の文脈で `Δ` と `C` を別測定し、`χ` を離散ログ上で推定可能な量へ落とすことである。

## §2 V_carrier 候補

共通離散化:

- `X = {x_1, ..., x_N}` を pre-bye セッションから抽出した atomic memory units とする。単位は summary sentence, memory slot, fact chunk のいずれでもよいが、順序は固定する。
- `t = 0, 1, ..., T` を boot 後 turn index とする。
- `C_t(x)` は handoff 後 turn `t` における unit `x` の「有用記憶としての支持強度」。

### 2.1 候補 C1: memory-slot retrieval front speed `[SOURCE]`

- 定義 (式):
  `C_t(x) = s_ret(x,t) ∈ [0,1]`
  
  `x_{κ_c}(t) = max{x_i | C_t(x_i) ≥ κ_c}`
  
  `V_carrier^(slot) = Q_p(|x_{κ_c}(t+1) - x_{κ_c}(t)|)`
- 計測方法:
  handoff artifact から atomic fact を作り、各 turn の応答・retrieval・memory 参照がその fact を entail / support しているかを judge して `s_ret` を付与する。`κ_c` は support 閾値。
- 理論的整合性:
  Paper XII §5 の Hyphē 行 `C_t(x) = retrievable useful memory flow` に最も近い。Paper X §4 の `Mem_i = Compressed_i` と `boot` 再開を、そのまま memory slot 上の front と見なせる。
- 精度見込み:
  高。前提は atomic fact の分解と judge の安定性。単位は `slot/turn` で `χ` を無次元比にしやすい。

### 2.2 候補 C2: log-prob gap closure speed `[SOURCE]`

- 定義 (式):
  `g_t(x) = |log p_t(a_x^* | q_x) - log p_ref(a_x^* | q_x)|`
  
  `T_δ = inf{t | median_x g_t(x) ≤ δ}`
  
  `V_carrier^(lp) = 1 / max(T_δ, 1)`
- 計測方法:
  gold answer `a_x^*` を持つ probe question `q_x` を用意し、boot 後各 turn で log-prob gap がいつ閾値 `δ` 未満へ戻るかを測る。
- 理論的整合性:
  brief が明示した `δ-log-prob 復元時間` 候補に一致する。担体を「正答分布を再び支えられるまでの回復速度」と読む写像。
- 精度見込み:
  理論精度は高いが、実装可能性は中。API / ログが token log-prob を出せない環境では使えない。

### 2.3 候補 C3: semantic coverage throughput `[TAINT]`

- 定義 (式):
  `Cov_t = (1/N) Σ_x 1[C_t(x) ≥ κ_c]`
  
  `V_carrier^(cov) = Q_p(max(0, Cov_t - Cov_{t-1}))`
- 計測方法:
  各 turn で「現在の文脈が何個の atomic unit を十分支持できているか」を数え、その増分を throughput として使う。
- 理論的整合性:
  Paper XII の front 定義を mass/coverage へ粗視化した proxy。真の level-set velocity ではないが、`useful evidence throughput` という brief の要請には合う。
- 精度見込み:
  中。front の位置情報を潰すため鋭さは落ちるが、judge だけで計測できる。

### 2.4 候補 C4: summary-density normalized transport `[TAINT]`

- 定義 (式):
  `V_carrier^(dens) = |Mem_handoff| / max(T_boot, 1)`
  
  ここで `|Mem_handoff|` は handoff artifact の information units 数、`T_boot` は初回の有効再利用までの turn 数。
- 計測方法:
  handoff summary / memory packet のサイズと、それが次セッションで実際に使われるまでの latency を測る。
- 理論的整合性:
  brief の `tokens per session` 候補を最も素直に scalar 化したもの。ただし `C_t(x)` を直接観測していないため Paper XII との整合性は弱い。
- 精度見込み:
  低〜中。容量を速度と混同しやすいので比較指標としてのみ有用。

## §3 V_null 候補

共通離散化:

- `Δ_t(x)` は unit `x` が boot 後 turn `t` でどれだけ「他候補と区別可能か」を表す。
- `N_t^ε = {x | Δ_t(x) ≤ ε}` を low-distinguishability set とみなす。

### 3.1 候補 N1: low-distinguishability boundary speed `[SOURCE]`

- 定義 (式):
  `Δ_t(x) = m_t(x) = s_pos(x,t) - max_j s_neg(x,j,t)`
  
  `x_ε(t) = max{x_i | Δ_t(x_i) ≤ ε}`
  
  `V_null^(slot) = Q_p(|x_ε(t+1) - x_ε(t)|)`
- 計測方法:
  各 atomic fact に対し正答候補と distractor 候補を作る。judge / embedding / entailment margin で `m_t(x)` を出し、低 margin 境界がどれだけ前進するかを見る。
- 理論的整合性:
  Paper XII §5 の `Δ = semantic separability / retrievability gap` をそのまま使う写像。Paper XII §3 の level-set front を離散 slot 上へ落としている。
- 精度見込み:
  高。distractor 設計が妥当なら、最も `V_null` らしい量になる。

### 3.2 候補 N2: entropy-front speed `[SOURCE]`

- 定義 (式):
  `Δ_t(x) = 1 - H_t(x)/log K`
  
  `x_ε(t) = max{x_i | Δ_t(x_i) ≤ ε}`
  
  `V_null^(ent) = Q_p(|x_ε(t+1) - x_ε(t)|)`
- 計測方法:
  probe question に対する answer distribution の entropy を計測し、高 entropy 域の広がりを front とみなす。
- 理論的整合性:
  brief の `情報エントロピー勾配速度` 候補に一致する。`Δ` を distinguishability の逆写像として entropy で近似する案。
- 精度見込み:
  中。log-prob 取得が必要で、entropy は distractor 構造を明示しないぶん `N1` より曖昧。

### 3.3 候補 N3: low-distinguishability mass expansion `[TAINT]`

- 定義 (式):
  `Mass_t^ε = |N_t^ε| / N`
  
  `V_null^(mass) = Q_p(max(0, Mass_t^ε - Mass_{t-1}^ε))`
- 計測方法:
  低 distinguishability 域に落ちた unit の割合の増加速度を使う。
- 理論的整合性:
  Paper XII の front を set-mass へ粗視化した proxy。局所 front ではなく「欠如帯の膨張率」を見る。
- 精度見込み:
  中。front 位置は失うが、ログだけから比較的安定に取れる。

### 3.4 候補 N4: recall-failure onset speed `[TAINT]`

- 定義 (式):
  `Fail_t = 1 - (1/N) Σ_x 1[Δ_t(x) > ε]`
  
  `V_null^(fail) = 1 / max(T_fail, 1)`
  
  `T_fail = inf{t | Fail_t ≥ ρ}`
- 計測方法:
  distinguishability が崩れた unit 比率が `ρ` を超えるまでの time-to-failure を測る。
- 理論的整合性:
  onset 指標としては有用だが、Paper XII §3 の front speed ではなく survival-analysis 的 proxy。
- 精度見込み:
  低〜中。粗いが strategy 比較には使える。

## §4 χ = V_null / V_carrier の LLM handoff 文脈への具体式

共通記法:

- `η > 0` はゼロ割り防止の微小量。
- `Q_p` は characteristic speed の `p` 分位。

### 4.1 組合せ A: slot-front / slot-front `[SOURCE]`

`χ_A(t) = V_null^(slot)(t) / max(V_carrier^(slot)(t), η)`

- 解釈:
  低 distinguishability 境界の前進が、retrievable memory front の回復より速いと `χ_A > 1`。
- 長所:
  numerator と denominator が同じ `slot/turn` 単位。Paper XII の形式に最も忠実。
- 短所:
  atomic unit の順序付けと distractor 設計が必要。

### 4.2 組合せ B: entropy-front / log-prob recovery `[SOURCE]`

`χ_B(t) = V_null^(ent)(t) / max(V_carrier^(lp)(t), η)`

- 解釈:
  高 entropy 境界の拡大が、正答分布回復より速い regime を捉える。
- 長所:
  uncertainty と recovery を別 API signal で取れるため理論的にきれい。
- 短所:
  token log-prob 依存が強く、実運用ではデータ欠損が出やすい。

### 4.3 組合せ C: mass-expansion / coverage-throughput `[TAINT]`

`χ_C(t) = V_null^(mass)(t) / max(V_carrier^(cov)(t), η)`

- 解釈:
  低 distinguishability 域の膨張率が、有効記憶 coverage の回復率を上回るかを見る。
- 長所:
  judge ベースで実装可能。boot⊣bye ログだけでも比較しやすい。
- 短所:
  front の幾何をかなり潰すため、理論 fidelity は低い。

### 4.4 組合せ D: slot-front / summary-latency `[TAINT]`

`χ_D(t) = V_null^(slot)(t) * max(T_boot / |Mem_handoff|, 1)`

- 解釈:
  欠如境界が進む一方で、summary が希薄または遅延して carrier 回復が追いつかない状況を penalize する。
- 長所:
  summary artifact の質を直接反映できる。
- 短所:
  `V_carrier` を真の front speed ではなく容量 proxy へ置き換えている。

## §5 推奨組合せ

推奨は **組合せ A (`V_null^(slot)` × `V_carrier^(slot)`)** とする。

理由:

1. Paper XII §3-§5 の定義に最も忠実である。`Δ` と `C` を同一 probe space `X = memory slot / fact chunk` 上で別々に測り、両方を boundary motion として扱える。
2. Paper X §4 の `Ses → Mem → Ses` handoff 構造と自然に接続する。`Mem_i = Compressed_i` を atomic unit に分解すれば、その unit 群の回復 front と欠如 front を追跡できる。
3. Task 2 の実装制約に合う。vendor 依存の log-prob を必須にせず、judge / entailment / embedding margin で近似可能。
4. `χ` の単位が自動的に無次元になる。両速度が `slot/turn` なので strategy 間比較がしやすい。

推奨具体式:

`C_t(x) = s_ret(x,t)`

`Δ_t(x) = s_pos(x,t) - max_j s_neg(x,j,t)`

`V_carrier(t) = Q_p(|x_{κ_c}(t+1) - x_{κ_c}(t)|)`

`V_null(t) = Q_p(|x_ε(t+1) - x_ε(t)|)`

`χ_recommended(t) = V_null(t) / max(V_carrier(t), η)`

補足:

- `p = 0.5` を既定にし、感度分析として `p = 0.9` を併記するのがよい。
- `κ_c` と `ε` は固定閾値 1 本で始め、Task 2 では strategy 別 grid search を避ける。

## §6 Task 2 (estimator 実装) への引き継ぎメモ

- 入力単位:
  boot 前セッションから atomic memory units を作る処理が必要。最小単位は summary sentence でよいが、理想は fact chunk。
- probe space:
  `x` の順序は original turn index か handoff packet 内順序で固定する。Task 2 では順序の再最適化をしない。
- `C_t(x)` 実装:
  judge 関数 `s_ret(x,t)` を用意し、各 turn の応答・memory 参照・retrieval 結果が unit `x` をどれだけ支持するかを `0..1` で返す。
- `Δ_t(x)` 実装:
  各 unit に対して distractor を 1 個以上作り、`s_pos - max s_neg` で margin を出す。distractor 生成が難しい unit は Task 2 で除外フラグを立てる。
- 出力:
  `x_{κ_c}(t)`, `x_ε(t)`, `V_carrier(t)`, `V_null(t)`, `χ(t)` を turn ごとに保存する。集約として median `χ`, max `χ`, first `χ > 1` turn を出す。
- 比較軸:
  DA / Summary / KLN / boot⊣bye で同じ estimator を使える設計にする。strategy ごとの差は handoff artifact の作り方だけに閉じ込める。
- フォールバック:
  slot alignment が崩れるログでは `χ_C` を fallback とする。`χ_A` が primary, `χ_C` が degraded mode。
- 非対象:
  Task 2 では drift-performance 相関や external benchmark まで広げない。まず `χ` 推定器を boot⊣bye ログ上で一貫出力できることを優先する。
