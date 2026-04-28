# 論文XII C3c橋梁ノート

**状態**: 内部育成ノート。公開本文ではない。
**型**: bridge note / theorem program seed
**昇格先**: Paper XII meta / Paper XII appendix / `drafts/リファレンス/統一記号表.md`
**failure condition**: `c_{L1}=f(∇²Φ, ...)` が構造定数の定理プログラムに変換できず、比喩的主張の域を出ない場合は本文 C3c へ戻さない。
**対象**: Paper XII の C3c `c_{L1}=f(∇²Φ, ...)` を、比喩ではなく定理プログラムへ変換するための橋梁面。
**作成日**: 2026-04-26

---

## 0. このノートの役割

Paper XII v0.9 は、C3 を次の 4 段に分けている。

| 段 | 本文上の地位 | このノートでの扱い |
|:---|:---|:---|
| C3a | `c_{L1}` は Level 1 carrier law の構造定数 | Paper XII 本体の責務 |
| C3b | 異なる Level 1 spacetime は異なる `c_{L1}` を持ちうる | Paper XII 本体の責務 |
| C3c | `c_{L1}=f(∇²Φ, ...)` | このノートの主対象 |
| C3d | 「真の c」は存在しない | C3c 以後の終局系 |

このノートは C3c/C3d を弱めるためのものではない。逆である。C3c を本文の語勢だけで消費せず、証明可能な形へ育てるために、本体から一時的に切り離す。

SOURCE:

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XII_速度は忘却である_草稿.md` lines 84-147
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XII_速度は忘却である_草稿.md` lines 523-570
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XII_速度は忘却である_草稿.md` lines 972-1087

---

## 1. 採る前提と採らない前提

### 採る前提

1. `c` はまず真空光速ではなく、Level 1 carrier law の有効速度上限 `c_{L1}(S)` として読む。
2. Paper XII 本文が直接担うのは C3a/C3b までである。
3. C3c は Paper I / V / VIII をつなぐ導出関数 `f` の構成問題である。
4. `∇²Φ` はスローガンとしては有効だが、証明形では scalar ではなく operator / tensor / spectrum として扱う。

### 採らない前提

1. Bucher の `χ>1` から、直ちに `c` の非普遍性を結論しない。
2. π 類比を証明に使わない。類比は方向を示すだけで、証明は characteristic cone の構成で行う。
3. `c=f(∇²Φ)` を scalar の等式として最初から固定しない。
4. 我々の真空光速 `299,792,458 m/s` が直ちに変動すると主張しない。

---

## 2. 作業命題 C3c'（仮称）

> **C3c'（仮称: Level 1 carrier cone 構成命題）**
> probe space `X` 上の忘却場 `Φ_X` と、Paper V の `T`-射影構造を `X` へ引き戻した Level 2 幾何が与えられるとき、admissible な Level 1 carrier field `u` の principal tensor `K^{ab}` は、その Level 2 幾何の関数として構成できる。
> その結果、carrier の characteristic speed ceiling `c_eff(S)` は `K^{ab}` のスペクトルから決まり、背景 `S` ごとに変わりうる。

ここで `c_eff` は `c_{L1}` の作業版であり、真空光速そのものではない。Level 1 carrier system の内部で観測される有効速度上限を指す。

直観的には、`Φ` の曲がりそのものが「どの方向に carrier が速く動けるか」を決める。速度上限は、場の値そのものではなく、場の二階構造が作る cone の形から出る。

---

## 3. 必要な橋の部品

### 3.1 Pullback layer

Paper V の `P^{ij}` は統計多様体側の `T`-射影演算子である。Paper XII の `X` は probe space なので、そのまま `P^{ij}` を `X` 上の速度法則に使ってはいけない。

必要なのは、少なくとも次のいずれかである。

| 名称 | 役割 | 未解決点 |
|:---|:---|:---|
| `θ: X -> Θ` | probe space から統計多様体への観測写像 | AgentSwing / Hyphē での具体化 |
| `h_ab` | `X` 上の計量、または `θ^*g` | front speed の距離単位 |
| `T^X_a` | Chebyshev 形式 `T_i` の `X` への引き戻し | `T` が何を測るかの解釈 |
| `P_X^{ab}` | `X` 上の `T`-射影 | rank / kernel の安定性 |

SOURCE:

- Paper I は `T_i` と忘却接続 `A_i` を導入し、`F_{ij}` を `d(ΦT)` で与える。
- Paper V は `P^{ij}=|T|^2g^{ij}-T^iT^j` を `T`-射影演算子として定義し、`P^{ij}∇_i∇_jΦ` を場の方程式に入れる。

INFERENCE:

- C3c では、Paper V の `P^{ij}` を `X` 上へ移すための pullback layer が必須である。

### 3.2 T-射影 Hessian（仮称）

C3c の中心候補は、scalar の `∇²Φ` ではなく、`T` 方向を除いた Hessian のスペクトルである。

作業定義:

```text
H_perp_ab := P_X_a^c P_X_b^d ∇_c ∇_d Φ_X
```

ここで `H_perp` は仮称であり、正本記号ではない。意味は「忘却場の二階変化のうち、力を生む方向だけを残した曲がり」である。

重要なのは、速度上限は一つの数ではなく、方向ごとの上限を持つ可能性があること。したがって最初から scalar `∇²Φ` に落とすと、異方性を消してしまう。

### 3.3 Carrier principal tensor

Level 1 carrier field `u` に対して、最小の作業形は次である。

```text
∂_t^2 u - K^{ab}[H_perp, α_eff, λ, ...] ∇_a∇_b u + lower order = 0
```

ここで `K^{ab}` は仮称であり、carrier の principal tensor を表す。直観的には、carrier がどの方向へどれだけ速く伝わるかを決める係数である。

証明で必要なのは、`K^{ab}` をただ置くことではなく、次を示すこと。

| 条件 | 意味 |
|:---|:---|
| Hyperbolicity | carrier 方程式が速度 cone を持つ |
| Positivity | 速度上限が実数として出る |
| Covariance | 座標を変えても同じ物理量を表す |
| Spectral fidelity | `H_perp` のスペクトル差が `K` のスペクトル差へ反映される |

### 3.4 Speed extraction

`c_eff` は `K^{ab}` から取り出す。作業的には、計量 `h` に対する最大固有値を使う。

```text
c_eff^2(S) := sup_ξ K^{ab} ξ_a ξ_b / h^{ab} ξ_a ξ_b
```

この式はまだ定義候補であり、正本ではない。意図は単純で、carrier が最も速く進める方向の速度を、その Level 1 system の有効速度上限と読む。

等方的 sector では、`H_perp_ab` が `h_ab` に比例する。この場合だけ、

```text
c_eff = f(tr_h H_perp, α_eff, λ, ...)
```

のような scalar 形へ落ちる。本文の `c_{L1}=f(∇²Φ,...)` は、この等方的縮約として読むのが安全である。

---

## 4. 証明順序

### Step 1: XII-T0 / XII.1' を前提化する

`χ` が tautology ではなく、Level 0 front と Level 1 carrier front が別 law を持つことを前提にする。これは C3c の前提であり、C3c の中で再証明しない。

ただし、現稿の L3.2 には補強余地がある。`v_null=v_carrier` が恒等的なら `C=g(Φ)` に落ちる、という推論は強すぎる。同じ front speed を持つ二つの場が、必ず関数従属するとは限らない。

修正方針:

```text
恒等的な同速性を「関数従属への矛盾」ではなく、
generic transversality / non-resonance 条件の失敗として扱う。
```

これは C3c のためにも重要である。carrier cone を構成するなら、速度一致や速度差は関数従属ではなく principal symbol の比較として扱うべきだからである。

### Step 2: `X` と `Θ` の橋を固定する

Paper XII の `X` と Paper I/V の統計多様体 `Θ` の間に、観測写像または pullback 構造を置く。

未解決の問い:

| 問い | 候補 |
|:---|:---|
| `X` は何か | 画像平面 / token index / memory slot / semantic coordinate |
| `θ(x)` は何か | local statistical state / embedding distribution / retrieval state |
| `h_ab` は何か | Euclidean metric / Fisher pullback / task metric |
| `T^X` は何を表すか | carrier law の Chebyshev 方向 |

### Step 3: `H_perp` を定義する

`H_perp` は `Φ_X` の二階変化を `T`-射影したものとして置く。ここでの目的は、忘却場の Level 2 構造から carrier の cone を作ることである。

### Step 4: `K^{ab}` の構成公理を置く

最初から具体関数形を当てにいかない。まず admissible carrier law が満たすべき構成公理を置く。

最小公理:

1. `K^{ab}` は `H_perp`, `α_eff`, `λ` と低階の invariant から自然に作られる。
2. `H_perp` がゼロまたは等方的に退化すると、carrier cone は基準 cone へ戻る。
3. `H_perp` のスペクトルが異なる二背景では、`K` のスペクトルも一致するとは限らない。
4. `K` が同一になるなら、それは追加の同一視写像または symmetry によって説明される。

### Step 5: 非普遍性を二背景で示す

二つの Level 1 spacetime `S_1`, `S_2` を取り、それぞれの `H_perp` のスペクトル不変量が異なることを示す。

```text
Spec(H_perp(S_1)) != Spec(H_perp(S_2))
```

さらに `K` が spectrally faithful なら、

```text
c_eff(S_1) != c_eff(S_2)
```

が出る。これが C3b から C3c への橋である。

### Step 6: 実験線と接続する

Paper XII §5.3 第4段は、hBN の層数・欠陥密度・キャビティ厚と Level 1 の有効速度上限の相関を見る。C3c 橋梁ノートでは、これを次の観測へ翻訳する。

| 理論量 | 実験側 proxy |
|:---|:---|
| `H_perp` のスペクトル | hBN 微小構造から推定される有効異方性 |
| `K^{ab}` のスペクトル | ポラリトン包絡線の群速度テンソル |
| `c_eff` | Level 1 carrier の有効速度上限 |
| 背景差 | 層数・欠陥密度・キャビティ厚の差 |

---

## 5. 破綻条件

C3c' は次のいずれかで破綻する。

| 破綻条件 | 意味 |
|:---|:---|
| `X -> Θ` の pullback が作れない | Paper I/V と XII が同じ幾何面に乗らない |
| `K^{ab}` が `H_perp` に依存しない | `c_eff` は忘却場から導出されない |
| `H_perp` のスペクトル差が速度差に反映されない | Level 2 構造は carrier cone を決めない |
| すべての admissible carrier law が同じ `c_eff` を強制する | C3b/C3c は崩れる |
| hBN 系で微小構造と群速度の対応が全く出ない | §5.3 第4段の観測線は弱まる |

---

## 6. 棄却台帳

| 棄却案 | 棄却理由 |
|:---|:---|
| `c=f(∇²Φ)` を scalar 等式として本文へ直書きする | 異方性と cone 構造を失う |
| π 類比を証明として使う | 類比は carrier cone を構成しない |
| Bucher の `χ>1` から `true c` 不在へ飛ぶ | `χ>1` は Level 0/1 分離の支持線であり、C3c の証明ではない |
| `v_null=v_carrier` なら `C=g(Φ)` とする | 同速性は関数従属を必ず含意しない |
| 真空光速を直接動かす | 本稿の観測線はまず Level 1 の有効速度上限である |

---

## 7. 本文へ戻すときの条件

このノートの内容を Paper XII 本文へ戻す条件は、次の 4 つである。

1. `X -> Θ` または同等の pullback layer が定義できる。
2. `H_perp` と `K^{ab}` の記号が統一記号表へ追加できる程度に安定する。
3. `K^{ab}` の hyperbolicity / positivity / covariance が説明できる。
4. 二背景で `c_eff` がずれる最小模型が作れる。

この 4 条件が揃うまでは、C3c は Paper XII 本文では `XII-P1` のまま維持する。C3d は C3c 後の終局系として保持し、本文の主定理には昇格しない。

---

## 8. 次の作業

### T-XII-C3c-1

`X -> Θ` の候補を三系で作る。

**状態**: 初回具体化。正本記号ではなく、pullback layer を作るための候補表である。

SOURCE:

- Paper XII §2.7 は `θ: X -> M`, `μ: X × R -> R_+`, `Ψ: R -> [0,1]` により `α_eff(x,t)` を構成する。
- Paper XII §5.1 は Bucher / AgentSwing / Hyphē の `X, Δ, C` 候補を列挙する。

INFERENCE:

- C3c の `H_perp` を作るには、単に `X` を置くだけでは足りない。`X` の各点を、Paper I/V が扱う統計多様体側の状態 `θ(x)` へ送る必要がある。
- したがって T-XII-C3c-1 の目的は、三系それぞれで `θ(x)` が何を意味するかを仮固定することである。

#### 三系対応表

| 系 | `X` | `θ(x,t)` 候補 | `Θ` 候補 | `h_ab` 候補 | `T^X_a` 候補 | C3c で見る速度 |
|:---|:---|:---|:---|:---|:---|:---|
| Bucher optics | hBN 画像平面の位置 `x=(x_1,x_2)` | 局所光場 jet: `(|ψ|, arg ψ, ∇ψ, material params)` | local optical state distribution / polariton state manifold | 物理平面の Euclidean metric + 媒質異方性 metric | material dispersion が作る感受方向。実装上は polariton dispersion tensor の主軸 | polariton package / envelope の群速度上限 `c_eff` |
| AgentSwing | token / chunk / context position | task-conditioned evidence state: `p(z | local window, task)` | useful-evidence distribution manifold | token 距離 + embedding / task metric の混合 | evidence throughput が最も変化する方向。CM 操作に敏感な方向 | useful evidence flow の有効伝搬速度 |
| Hyphē | turn / memory slot / retrieval coordinate | retrieval state: `p(m | query, thread state, handoff)` | retrievable-memory distribution manifold | retrieval embedding metric + temporal slot distance | retrievability bottleneck の主軸。handoff が残す residual `χ` に敏感な方向 | retrievable useful memory flow の有効伝搬速度 |

#### Bucher optics の最小解釈

Bucher 系は C3c の物理較正面である。`X` は hBN 画像平面でよい。ただし `θ(x,t)` は単なる位置ではなく、その点の局所光場状態を表す。

最小候補:

```text
θ_B(x,t) := local jet of optical field ψ around x
          + material microstructure parameters around x
```

`H_perp` は、この local state 上の忘却場 `Φ_B` の T-射影 Hessian として読む。`K^{ab}` は polariton carrier の principal tensor であり、観測 proxy は群速度テンソルまたは包絡線 front の有効速度である。

強み:

| 点 | 理由 |
|:---|:---|
| 物理単位がある | `X` が実空間なので front speed が測りやすい |
| `C_t` が明確 | carrier は polariton envelope / energy support として読める |
| C3c 第4段と接続する | 層数・欠陥密度・キャビティ厚の差を背景差にできる |

弱点:

| 点 | 理由 |
|:---|:---|
| `Φ_B` の定義が未固定 | optical field の何を忘却場と呼ぶかが未確定 |
| `T^X` の由来が難しい | Paper I の Chebyshev 形式と媒質分散 tensor の対応が未証明 |
| 真空光速ではない | ここで扱うのは Level 1 有効速度上限であり、真空 `c` ではない |

#### AgentSwing の最小解釈

AgentSwing 系は、C3c そのものより Paper XII の C1/C2 と `τ_χ` の予測性を測る面である。ただし `X -> Θ` の練習台として強い。

最小候補:

```text
θ_A(x,t) := p(z | W_x(t), task)
```

ここで `W_x(t)` は位置 `x` の local window、`z` は「その window が task に有用な証拠を含むか」を表す潜在状態である。

この場合:

| 量 | 解釈 |
|:---|:---|
| `Δ_t(x)` | local window と task reference の可区別性 |
| `C_t(x)` | useful evidence throughput |
| `h_ab` | token 距離、embedding 距離、task relevance 距離の合成 |
| `T^X_a` | evidence throughput が崩れる方向 |
| `c_eff` | 有用証拠が task policy に届く有効速度上限 |

強み:

| 点 | 理由 |
|:---|:---|
| 測定設計へ落ちる | `τ_χ` と Context Rot onset の比較ができる |
| CM 介入と接続する | DA / Summary / KLN の差を carrier law 差として読める |
| toy model 化しやすい | token/chunk は離散なので有限モデルで試せる |

弱点:

| 点 | 理由 |
|:---|:---|
| `c_eff` が物理速度ではない | throughput speed の比喩になりやすい |
| `h_ab` が恣意的になりうる | metric を固定しないと速度が動く |
| `T^X` が未定義 | Chebyshev 方向を evidence manifold でどう作るかが課題 |

#### Hyphē の最小解釈

Hyphē 系は、boot⊣bye を `χ` 制御として観測する面である。C3c の本命というより、`X -> Θ` を memory/retrieval に移すための工学的検証面である。

最小候補:

```text
θ_H(x,t) := p(m | q_t, thread_state_t, handoff)
```

ここで `m` は memory slot、`q_t` は現在の問い合わせ、`handoff` は前セッションから持ち込まれた圧縮記憶である。

この場合:

| 量 | 解釈 |
|:---|:---|
| `Δ_t(x)` | 必要記憶と取得記憶の semantic separability |
| `C_t(x)` | retrievable useful memory flow |
| `h_ab` | embedding metric + temporal distance + slot topology |
| `T^X_a` | retrieval が最も詰まる bottleneck 方向 |
| `c_eff` | 有用記憶が現在の推論へ届く有効速度上限 |

強み:

| 点 | 理由 |
|:---|:---|
| boot⊣bye と直接接続する | bye は高 `χ` 軌道の切断、boot は低 `χ` 再初期化として測れる |
| handoff residual を測れる | `χ_init^{next}` を観測指標にできる |
| 内部実験に近い | 物理実験より早く toy validation ができる |

弱点:

| 点 | 理由 |
|:---|:---|
| `Θ` が設計依存 | retrieval backend と embedding choice に依存する |
| Level 1 carrier の意味が弱い | 物理 carrier ではなく memory flow なので、C3c への寄与は間接的 |
| `K^{ab}` が工学 proxy になりやすい | principal tensor と呼ぶには定義の節度が要る |

#### T-XII-C3c-1 の暫定結論

| 系 | C3c への役割 | 採用度 |
|:---|:---|:---|
| Bucher optics | `H_perp -> K -> c_eff` の物理較正面 | 高 |
| AgentSwing | `X -> Θ` と `τ_χ` 予測性の離散 toy 面 | 中 |
| Hyphē | boot⊣bye 介入と residual `χ` の工学面 | 中 |

結論として、C3c の本命は Bucher optics である。AgentSwing と Hyphē は C3c そのものの証明ではなく、pullback layer と `χ` 制御の離散版を育てる補助面として扱う。

次に必要なのは T-XII-C3c-2、すなわち Bucher optics 上で `H_perp` の最小定義を作ることである。ここで初めて `H_perp_ab ∝ h_ab` の等方的 sector と scalar `f(tr H_perp, ...)` の関係を検査できる。

### T-XII-C3c-2

`H_perp` の最小定義を作り、`H_perp_ab ∝ h_ab` の等方的 sector で scalar `f(tr H_perp, ...)` に落ちることを確認する。

**状態**: Bucher optics に限定した初回定義。正本記号ではなく、C3c 用の作業定義である。

SOURCE:

- Paper V は `P^{ij}=|T|^2_g g^{ij}-T^iT^j` を `T`-射影演算子として導入し、`P^{ij}∇_i∇_jΦ` を場の方程式に入れる。
- Paper XII §2.7 は `θ: X -> M` による pullback layer をすでに要求している。
- Paper XII §5.3 第4段は、hBN 微小構造と Level 1 有効速度上限の相関を見る観測線を置いている。

INFERENCE:

- Bucher optics で C3c を育てるなら、`H_perp` は `X` 上の二階微分ではなく、`θ_B: X -> Θ_B` を通じて引き戻された統計多様体側の T-射影 Hessian として始めるのが安全である。
- ただし、実験 proxy では `X` 上の局所量として扱う必要があるため、最終的には `θ_B^*H_perp` を hBN 画像平面上の tensor field として読む。

#### 定義候補 1: 統計多様体側

Bucher local state manifold を `Θ_B` とし、その上に Paper I/V と同型の構造を置く。

```text
(Θ_B, g_B, T_B, Φ_B)
```

ここで:

| 記号 | 作業解釈 |
|:---|:---|
| `g_B` | local optical state distribution 上の Fisher 型計量 |
| `T_B` | local state manifold の Chebyshev 形式、またはその物理 proxy |
| `Φ_B` | 光場・媒質状態の忘却ポテンシャル |
| `P_B^{ij}` | `T_B` 方向を除く射影演算子 |

Paper V 型の射影:

```text
P_B^{ij} := |T_B|^2_{g_B} g_B^{ij} - T_B^i T_B^j
```

統計多様体側の T-射影 Hessian:

```text
H_B^{perp,ij} := P_B^{ik} P_B^{jl} ∇_k∇_l Φ_B
```

この形の利点は、Paper V の `P^{ij}∇_i∇_jΦ` と直接接続できること。欠点は、`Θ_B` と `Φ_B` の具体化がまだ重いこと。

#### 定義候補 2: probe space 側への引き戻し

`θ_B: X -> Θ_B` を使い、hBN 画像平面上へ引き戻す。

```text
H^perp_ab(x,t)
  := (dθ_B)_a^i (dθ_B)_b^j H_B^{perp}_{ij}(θ_B(x,t))
```

ここで `a,b` は probe space `X` の添字、`i,j` は local state manifold `Θ_B` の添字である。

直観的には、これは「hBN 画像平面上の各点で、忘却場の二階構造が carrier にどの方向性を与えるか」を表す。

#### 定義候補 3: 実験 proxy 版

実験では `Θ_B` を完全に作れない可能性が高い。その場合、まず以下の proxy で始める。

```text
H^perp_ab(proxy)
  := Π_a^c Π_b^d ∇_c∇_d Φ_B^X
```

ここで:

| 記号 | 作業解釈 |
|:---|:---|
| `Φ_B^X(x,t)` | hBN 画像平面上で推定される forgetting potential proxy |
| `Π_a^b` | material / dispersion の主軸に基づく横方向射影 |
| `∇_c∇_d` | `h_ab` に関する二階微分 |

`Π` はまだ `P_X` の代用品である。Paper V の `T`-射影が未構成の段階で、物理実験側の anisotropy axis を使って暫定的に作る。

この proxy は理論正本ではないが、二背景 toy model と §5.3 第4段の観測線には使える。

#### 等方的 sector

`H^perp_ab` が probe metric `h_ab` に比例するとき、

```text
H^perp_ab = κ_H h_ab
```

と書ける。このとき trace は

```text
tr_h H^perp = h^{ab}H^perp_ab = d_X κ_H
```

であり、`d_X = dim X` である。したがって

```text
κ_H = (1/d_X) tr_h H^perp
```

となる。

この sector でのみ、C3c の scalar slogan は次のように読める。

```text
c_eff = f(tr_h H^perp, α_eff, λ, material parameters, ...)
```

つまり本文の `c_{L1}=f(∇²Φ,...)` は、厳密には

```text
c_eff = f(Spec(H^perp), α_eff, λ, ...)
```

の等方的縮約である。

#### 異方的 sector

異方的 sector では `H^perp_ab` は複数の固有値を持つ。

```text
Spec(H^perp) = {κ_1, κ_2, ..., κ_d}
```

このとき `c_eff` は scalar trace ではなく、スペクトル不変量に依存させる。

候補:

| 依存量 | 意味 |
|:---|:---|
| `λ_max(H^perp)` | 最速方向を決める |
| `tr(H^perp)` | 平均的な曲がり |
| `det(H^perp)` | cone 体積の proxy |
| anisotropy ratio `λ_max/λ_min` | cone の歪み |

C3c の証明では、最初から `tr` だけに潰さない。`Spec(H^perp)` を保持したまま `K^{ab}` へ渡す。

#### Bucher optics での最小模型

最小模型では、hBN 画像平面を 2 次元とし、`H^perp` を対角形で置く。

```text
h_ab = diag(1, 1)
H^perp_ab = diag(κ_parallel, κ_perp)
```

等方的背景:

```text
κ_parallel = κ_perp = κ
```

異方的背景:

```text
κ_parallel != κ_perp
```

この二背景で `K^{ab}` が `H^perp` に spectral faithful に依存するなら、`c_eff` はずれる。

```text
Spec(H^perp_1) != Spec(H^perp_2)
  -> Spec(K_1) != Spec(K_2)
  -> c_eff(S_1) != c_eff(S_2)
```

これは C3c の完全証明ではない。だが、「二背景で `c_eff` がずれる」ための最小反例候補を作る。

#### T-XII-C3c-2 の暫定結論

`H_perp` は次の二層で扱う。

| 層 | 定義 | 用途 |
|:---|:---|:---|
| 理論層 | `H_B^{perp,ij}=P_B^{ik}P_B^{jl}∇_k∇_lΦ_B` | Paper V との接続 |
| 実験 proxy 層 | `H^perp_ab(proxy)=Π_a^cΠ_b^d∇_c∇_dΦ_B^X` | Bucher/hBN の最小模型 |

本文に戻すなら、最初に出すべき形は scalar `∇²Φ` ではない。

```text
c_eff = f(Spec(H^perp), α_eff, λ, ...)
```

その上で、等方的 sector のみ

```text
c_eff = f(tr_h H^perp, α_eff, λ, ...)
```

へ縮約する。

### T-XII-C3c-3

`K^{ab}` の公理系を 4 条件に絞り、Bucher optics 限定の最小 constitutive theorem として書く。

状態:

```text
T-XII-C3c-3 = working theorem candidate
public theorem = no
target system = Bucher optics first
```

#### SOURCE

この節で SOURCE と呼べるのは次である。

| SOURCE | 内容 |
|:---|:---|
| Paper V Prop. 2.2.4 | `P^{ij}=|T|_g^2 g^{ij}-T^iT^j` が T-射影演算子であり、`P^{ij}∇_i∇_jΦ` が忘却場の T-射影ラプラシアンを作る |
| Paper V §5.5 | 逆伝播子の運動項に `P^{ij}q_iq_j` が入る |
| Paper XII §5.3 第4段 | Bucher 光学系で、hBN 微小構造と Level 1 有効速度上限の相関を見る計画がある |
| T-XII-C3c-2 | `H^perp` は T-射影 Hessian の pullback / proxy として作業定義された |

ここから `K^{ab}` が自動的に出るわけではない。`K^{ab}` は、この SOURCE 群を carrier 方程式へ接続するための INFERENCE 層である。

#### 作業命題 C3c-K

> **C3c-K（仮称: spectral constitutive theorem）**
> Bucher optics に対応する probe space `X_B` 上で、計量 `h`, T-射影 Hessian `H^perp`, 有効忘却強度 `α_eff`, 質量項または安定化項 `λ`, carrier の基準速度 `c_0` が与えられるとする。
> このとき、admissible な Level 1 carrier system について、principal tensor `K^{ab}` を
>
> ```text
> K = C_S(h, H^perp, α_eff, λ, material parameters)
> ```
>
> として構成する constitutive map `C_S` が存在する。`C_S` が hyperbolicity, positivity, covariance, spectral fidelity を満たすなら、carrier の有効速度上限 `c_eff(S)` は `Spec(H^perp)` に依存する。

これは C3c の完全証明ではない。ここで得るのは、「`H^perp` から cone を作るなら最低限この形でなければならない」という橋の仕様である。

#### Carrier law の最小形

Level 1 carrier field `u` は、次の principal part を持つと置く。

```text
L_S u
  := ∂_t^2 u
     - K^{ab}_S(x,t) ∇_a∇_b u
     + lower order terms
```

ここで速度 cone を決めるのは lower order terms ではなく `K^{ab}` である。したがって C3c の証明対象は `u` の全運動方程式ではなく、principal tensor `K^{ab}` の構成で足りる。

#### Constitutive map の最小候補

`H^perp` を `h` で一つの endomorphism に直す。

```text
A^a_b := h^{ac} H^perp_cb
```

`A` は `h` に関して自己随伴な作業対象である。`K` は、`A` のスペクトル関数として作る。

```text
K^a_b
  := c_0^2 δ^a_b
     + ℓ_H^2 η(α_eff, λ, material parameters) r(A)^a_b

K^{ab} := h^{ac} K^b_c
```

各記号の役割:

| 記号 | 役割 |
|:---|:---|
| `c_0` | carrier system の基準速度 |
| `ℓ_H` | Hessian response を速度次元へ変換する長さ scale |
| `η` | `α_eff`, `λ`, material parameters に依存する応答係数 |
| `r(A)` | `A` に作用する spectral response function |

`r` は最初から特定しない。ただし次の条件を置く。

| 条件 | 意味 |
|:---|:---|
| `r(0)=0` | `H^perp=0` のとき基準 cone に戻る |
| spectral | `r(A)` は `A` の固有空間を保つ |
| operating-band injective | 実験で見る帯域では、異なる `Spec(A)` を同じ応答へ潰さない |
| bounded response | `K` が正性を失わない範囲に応答を保つ |

この候補の利点は、`∇²Φ` を scalar に潰さず、方向ごとの応答を保持する点である。

#### 4 条件

##### 1. Hyperbolicity

`K` は `h` に対して正の範囲に収まる必要がある。

```text
0 < δ h^{ab}ξ_aξ_b
  <= K^{ab}ξ_aξ_b
  <= M h^{ab}ξ_aξ_b
```

これにより principal symbol は

```text
σ(L_S)(ω,ξ) = -ω^2 + K^{ab}ξ_aξ_b
```

となり、characteristic relation

```text
ω^2 = K^{ab}ξ_aξ_b
```

が速度 cone を持つ。

##### 2. Positivity

`c_eff` は実数で、かつ有限でなければならない。

```text
c_eff^2(S)
  := sup_{ξ ≠ 0}
       K^{ab}ξ_aξ_b / h^{ab}ξ_aξ_b
```

これは `h^{-1}K` の最大固有値である。

```text
c_eff^2(S) = λ_max(h^{-1}K)
```

したがって positivity は、速度上限が測定量として取り出せるための条件である。

##### 3. Covariance

座標を変えても、同じ carrier cone を表す必要がある。

```text
(h, H^perp, α_eff, λ)
  -> K
```

は tensorial に作る。つまり、probe space の座標変換で `h` と `H^perp` が pullback されると、`K` も同じ変換則で pullback される。

この条件がないと、`c_eff` は背景の性質ではなく座標の副産物になる。

##### 4. Spectral fidelity

C3c に必要なのは、`H^perp` の差が `K` の差へ残ることである。

```text
Spec(A_1) != Spec(A_2)
  and η != 0
  and r separates the operating band
  -> Spec(h^{-1}K_1) != Spec(h^{-1}K_2)
```

この条件が C3c の心臓である。hyperbolicity と positivity だけなら、`K=c_0^2 h^{-1}` でも満たせる。その場合、carrier cone は存在するが、忘却場から導出されていない。

#### 棄却台帳

| 候補 | 判定 | 理由 |
|:---|:---|:---|
| `K=c_0^2 h^{-1}` | 棄却 | carrier cone は出るが `H^perp` 依存が消える |
| `K=(c_0^2+η tr H^perp)h^{-1}` | 等方的 sector 限定 | scalar trace だけでは異方性を消す |
| `K=c_0^2h^{-1}+ηH^perp` | 保留 | 直感的だが正性を壊しうる |
| `K=c_0^2I+ℓ_H^2ηr(A)` | 採用候補 | spectral fidelity と正性を同時に管理できる |

#### C3c-K から C3c への接続

上の構成が通ると、C3c は次の形に弱化して読める。

```text
Spec(H^perp_1) != Spec(H^perp_2)
  -> Spec(K_1) != Spec(K_2)
  -> c_eff(S_1) != c_eff(S_2)
```

この列は `true c` の不在を直接証明しない。証明するのは、Level 1 carrier の有効速度上限が、忘却場の Level 2 構造へ感度を持つという点である。

#### Bucher optics での測定対応

| 理論量 | Bucher/hBN proxy |
|:---|:---|
| `H^perp` | hBN 微小構造と光場から作る T-射影 Hessian proxy |
| `Spec(H^perp)` | 主軸方向ごとの curvature / anisotropy index |
| `K` | polariton envelope の群速度テンソル |
| `c_eff` | 観測帯域での最大群速度 |

この対応が成立すれば、§5.3 第4段は単なる相関観測ではなく、C3c-K の spectral fidelity を打診する実験になる。

#### 崩壊条件

| 崩壊条件 | 何が壊れるか |
|:---|:---|
| `η=0` | `K` が `H^perp` に反応しない |
| `r` が観測帯域で定数 | `Spec(H^perp)` の差が消える |
| `K` が正性を失う | carrier law が安定した速度 cone を持たない |
| 観測される群速度テンソルが微小構造と無相関 | Bucher optics は C3c-K の支持面にならない |
| すべての admissible carrier system が同じ `K` へ潰れる | C3c は Level 1 構造依存性として成立しない |

#### T-XII-C3c-3 の暫定結論

`K^{ab}` は、`H^perp` から直接足し算で作るよりも、`A=h^{-1}H^perp` の spectral response として作る方がよい。

最小式は次で保持する。

```text
K^a_b
  = c_0^2 δ^a_b
    + ℓ_H^2 η(α_eff, λ, material parameters) r(A)^a_b
```

この式なら、hyperbolicity / positivity / covariance / spectral fidelity の 4 条件を同じ場所で管理できる。C3c の証明は、この constitutive map が実験 proxy と理論 SOURCE の両方に耐えるかどうかに集約される。

### T-XII-C3c-4

二背景反例を作る。最初は連続物理系でなくてよい。有限次元 toy model で `Spec(H_perp)` が異なり、`c_eff` がずれることを示す。

状態:

```text
T-XII-C3c-4 = finite-dimensional witness
public theorem = no
physical fit = no
purpose = show that spectral C3c-K can separate two Level 1 backgrounds
```

#### SOURCE

この節の SOURCE は、前節までに置いた作業構成だけである。

| SOURCE | 内容 |
|:---|:---|
| T-XII-C3c-2 | `H^perp` は scalar trace ではなく spectrum を保持して扱う |
| T-XII-C3c-3 | `K` は `A=h^{-1}H^perp` の spectral response として作る |
| Paper XII §5.3 第4段 | 物理系で最終的に見たいのは Level 1 有効速度上限の構造依存性 |

この toy model は Bucher データへの適合ではない。`H^perp -> K -> c_eff` の列が、少なくとも有限次元では破綻せずに動くことを確認する witness である。

#### 設定

probe space を 2 次元に落とす。

```text
X = R^2
h = I_2
A := h^{-1}H^perp = H^perp
```

応答関数は bounded かつ単調な spectral function として置く。

```text
r(A) := tanh(A/κ)
```

ここで `κ>0` は curvature scale であり、`tanh` は固有値ごとに作用する。速度 tensor は T-XII-C3c-3 の候補に従い、

```text
K = c_0^2 I_2 + γ r(A)
γ := ℓ_H^2 η
```

とする。`c_0>0`, `γ>0` とし、観測帯域では `A` を半正定値に限る。

このとき `K` の固有値は

```text
λ_i(K) = c_0^2 + γ tanh(a_i/κ)
```

である。`a_i` は `A` の固有値である。

#### 二背景

同じ trace を持つ二つの背景を選ぶ。

```text
S_iso:
  A_1 = diag(κ/2, κ/2)
  Spec(A_1) = {κ/2, κ/2}
  tr(A_1) = κ

S_aniso:
  A_2 = diag(0, κ)
  Spec(A_2) = {0, κ}
  tr(A_2) = κ
```

両者は `tr(A)` が同じである。したがって scalar trace だけを見る模型では、この二背景は区別されない。

#### 速度上限

`c_eff^2` は `K` の最大固有値で読む。

```text
c_eff^2(S) = λ_max(K)
```

`S_iso` では

```text
K_1 = diag(
  c_0^2 + γ tanh(1/2),
  c_0^2 + γ tanh(1/2)
)

c_eff^2(S_iso)
  = c_0^2 + γ tanh(1/2)
```

`S_aniso` では

```text
K_2 = diag(
  c_0^2,
  c_0^2 + γ tanh(1)
)

c_eff^2(S_aniso)
  = c_0^2 + γ tanh(1)
```

`tanh(1) > tanh(1/2)` なので、

```text
c_eff(S_aniso) > c_eff(S_iso)
```

となる。

#### 何が示されたか

この witness が示すのは次である。

| 示されたこと | 意味 |
|:---|:---|
| `tr(A_1)=tr(A_2)` でも `c_eff(S_1)≠c_eff(S_2)` | scalar `∇²Φ` だけでは速度上限を支えきれない |
| `Spec(A_1)≠Spec(A_2)` が `Spec(K_1)≠Spec(K_2)` へ残る | spectral fidelity の最小実例になる |
| `K_i` は正定値 | hyperbolicity / positivity を壊さずに差が出る |
| 速度差は最大固有値から出る | `c_eff` は cone の方向依存性を読む量である |

#### 何がまだ示されていないか

| 未証明 | 理由 |
|:---|:---|
| Bucher optics がこの `r(A)=tanh(A/κ)` に従うこと | これは witness 用の応答関数であり、実験適合ではない |
| `γ` の物理値 | `ℓ_H` と `η` はまだ測定・校正されていない |
| 真空光速の非普遍性 | ここで動かしたのは Level 1 有効速度上限である |
| 任意の carrier system への拡張 | この witness は 2 次元 finite model に限る |

#### 棄却台帳

| 候補 | 判定 | 理由 |
|:---|:---|:---|
| `A_1=0`, `A_2=diag(0,κ)` | 棄却 | 速度差は出るが、trace 差でも説明できる |
| `r(A)=A` | 保留 | 差は出るが、大きな負固有値で正性を壊しうる |
| `r(A)=tanh(A/κ)` | 採用 | bounded response と spectral separation を同時に満たす |
| 同じ trace の二背景 | 採用 | scalar trace 版の限界を同時に示せる |

#### T-XII-C3c-4 の暫定結論

有限次元 witness では、

```text
same tr(H^perp)
different Spec(H^perp)
  -> different Spec(K)
  -> different c_eff
```

が成立する。

したがって C3c の最小橋は、`c_eff=f(tr H^perp,...)` ではなく、

```text
c_eff = f(Spec(H^perp), α_eff, λ, material response, ...)
```

として保持するのがよい。この形なら、同じ scalar 曲率量を持つ二背景でも、carrier cone の形が違えば Level 1 有効速度上限がずれる。

### T-XII-C3c-5

§5.3 第4段へ戻すための実験 proxy 定義表を作る。

状態:

```text
T-XII-C3c-5 = experimental proxy ledger
public theorem = no
target paragraph = Paper XII §5.3 stage 4
claim tested = spectral fidelity of C3c-K
```

#### SOURCE

| SOURCE | 内容 |
|:---|:---|
| Paper XII §5.3 第4段 | Bucher 光学系で、hBN の層数・欠陥密度・キャビティ厚と Level 1 有効速度上限の関係を見る |
| T-XII-C3c-2 | `H^perp` は T-射影 Hessian の pullback / proxy として扱う |
| T-XII-C3c-3 | `K` は `A=h^{-1}H^perp` の spectral response として構成する |
| T-XII-C3c-4 | `tr(H^perp)` が同じ二背景でも、`Spec(H^perp)` が違えば `c_eff` はずれる witness がある |

#### INFERENCE

§5.3 第4段の観測線は、次のように読み替える。

```text
hBN microstructure
  -> Φ_B^X proxy
  -> H^perp proxy
  -> Spec(H^perp)
  -> K_proxy
  -> c_eff proxy
```

ここで測る `c_eff` は真空光速ではない。Bucher/hBN 系における polariton envelope / carrier package の Level 1 有効速度上限である。

#### Proxy 定義表

| 理論量 | 実験 proxy | 作り方 | 判定で見るもの |
|:---|:---|:---|:---|
| `S` | hBN 背景 | 層数・欠陥密度・キャビティ厚・局所異方性を持つ測定領域 | 二背景比較の単位 |
| `x∈X_B` | 画像平面座標 | hBN 上の 2D coordinate | `Φ`, `H^perp`, `K` を同じ座標へ載せる |
| `h_ab` | 画像平面 metric | pixel scale と試料幾何から固定 | Hessian と速度 tensor の基準 |
| `Φ_B^X` | 忘却ポテンシャル proxy | intensity deficit / phase singularity density / material disorder map のいずれか | 欠如・不均一性の scalar field |
| `Π` | T-射影 proxy | carrier dispersion の主軸、または群速度 tensor の低速/高速主軸から推定 | 力を生む方向だけを残す |
| `H^perp_ab` | T-射影 Hessian proxy | `Π_a^c Π_b^d ∇_c∇_d Φ_B^X` | Level 2 構造 |
| `A^a_b` | mixed curvature operator | `h^{ac}H^perp_cb` | spectrum を読む対象 |
| `Spec(H^perp)` | curvature spectrum | `λ_max`, `λ_min`, `tr`, anisotropy ratio | scalar trace 版との分離 |
| `K_proxy` | carrier speed tensor | polariton envelope / carrier front の方向別群速度から推定 | Level 1 carrier cone |
| `c_eff` | 有効速度上限 | `λ_max(K_proxy)^{1/2}` または方向別群速度の上側 envelope | C3c-K の観測 target |

#### `Φ_B^X` proxy の候補

`Φ_B^X` はまだ正本定義ではない。候補を 3 つに分ける。

| 候補 | 定義 | 強み | 弱み |
|:---|:---|:---|:---|
| intensity deficit | `Φ_I=-log((I+ε)/(I_ref+ε))` | 光場の欠如を直接拾う | carrier intensity と混ざりやすい |
| phase defect density | 位相特異点・位相巻き込みの局所密度 | Bucher の暗点/特異点に近い | smoothing scale に敏感 |
| material disorder | 欠陥密度・層厚・キャビティ厚から作る構造 map | 微小構造との対応が明確 | 光場の欠如そのものではない |

初回は 3 候補を併走させる。どれか一つを本文の定義に昇格させるのは、`K_proxy` との対応を見てからでよい。

#### 測定手順

| Step | 操作 | 出力 |
|:---|:---|:---|
| 1 | hBN 領域を背景 `S_i` として切り出す | `S_i` |
| 2 | 層数・欠陥密度・キャビティ厚を記録する | microstructure vector `m_i` |
| 3 | 光場または材料 map から `Φ_B^X` 候補を作る | `Φ_I`, `Φ_phase`, `Φ_mat` |
| 4 | smoothing scale を固定し Hessian を推定する | `∇∇Φ_B^X` |
| 5 | `Π` で T-射影する | `H^perp` |
| 6 | spectrum を読む | `tr`, `λ_max`, `λ_min`, anisotropy |
| 7 | carrier front / envelope から方向別群速度を推定する | `K_proxy` |
| 8 | `c_eff` を取り出す | `max velocity envelope` |
| 9 | `Spec(H^perp)` と `c_eff` の関係を検査する | C3c-K support / failure |

#### 判定模型

最初に比べる模型は 3 つでよい。

| 模型 | 説明 | C3c への意味 |
|:---|:---|:---|
| `M0` | `c_eff` は microstructure controls だけで説明される | C3c-K には届かない |
| `M1` | `c_eff` は `tr(H^perp)` だけで説明される | scalar 版まで届く |
| `M2` | `c_eff` は `Spec(H^perp)` または anisotropy を要する | spectral C3c-K を支持 |

T-XII-C3c-4 の witness に対応する勝ち筋は `M2 > M1` である。つまり、trace が同程度の領域を比べても、anisotropy が違うと `c_eff` が変わるかを見る。

#### Gate

| Gate | 通過条件 | 失敗時の扱い |
|:---|:---|:---|
| G0 coordinate alignment | `Φ_B^X`, `H^perp`, `K_proxy` が同じ `X_B` 上に載る | 測定設計をやり直す |
| G1 scale stability | smoothing scale を変えても `Spec(H^perp)` の順位が反転しない | `Φ_B^X` proxy を保留 |
| G2 carrier separability | null front と carrier envelope の速度が分けて測れる | C3c ではなく C1/C2 検証へ戻す |
| G3 trace-matched separation | `tr(H^perp)` 近接・anisotropy 差ありの二背景で `c_eff` がずれる | spectral C3c-K の支持 |
| G4 control survival | 層数・欠陥密度・キャビティ厚を入れても `Spec(H^perp)` 項が残る | C3c-K 支持線として扱える |

#### 崩壊条件

| 観測 | 判断 |
|:---|:---|
| `K_proxy` が `Spec(H^perp)` と無関係 | C3c-K は Bucher/hBN では支持されない |
| `tr(H^perp)` だけで `c_eff` が説明できる | scalar 縮約に留める |
| `Φ_B^X` 候補ごとに結論が反転する | 忘却ポテンシャル proxy が未安定 |
| microstructure controls だけで速度差が消える | C3c ではなく材料分散の話に戻す |
| null front と carrier envelope が分離不能 | XII の C1/C2 測定線も弱くなる |

#### §5.3 へ戻す候補文

本文へ戻すなら、第4段は `∇²Φ` 直書きではなく、次の形へ差し替える。

```text
Bucher の光学系において、hBN の層数・欠陥密度・キャビティ厚により、
T-射影された忘却場の二階構造 H^perp の spectrum が変化し、
その spectrum が polariton envelope の方向別群速度 tensor、
ひいては Level 1 有効速度上限 c_eff と相関するかを調べる。
ここで測定する c_eff は真空光速ではなく、当該 Level 1 carrier system の有効速度上限である。
```

この文なら、C3c を「`c=f(∇²Φ)` の直接証明」としてではなく、`H^perp -> K_proxy -> c_eff` の実験 proxy として置ける。

---

## 9. Carry-forward

このノートの持ち越し先:

| 持ち越し先 | 反映内容 |
|:---|:---|
| Paper XII 本文 | まだ反映しない。`XII-P1` の培養面として保持 |
| Paper XII meta | 将来、C3c の Gauntlet / Kalon 再判定に使う |
| 統一記号表 | `H_perp`, `K^{ab}`, `c_eff` が安定した後に追加 |
| §5.3 実験計画 | 第4段の測定量を `H_perp -> K -> c_eff` に精密化 |

---

## 10. 最小結論

C3c の証明は、`∇²Φ` という scalar から `c` を直接出すことではない。

最小の正しい形は次である。

```text
Φ の T-射影 Level 2 幾何
  -> Level 1 carrier の principal tensor K
  -> characteristic cone
  -> c_eff
```

この列が立つなら、C3c は比喩ではなくなる。
この列が立たない限り、C3c は Paper XII の野望であって、本文の定理ではない。
