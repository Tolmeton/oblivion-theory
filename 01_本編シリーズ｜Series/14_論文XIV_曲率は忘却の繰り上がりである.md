# 曲率は忘却の繰り上がりである — 離散 defect algebra と忘却場の方向性定理

Paper XIV — v0.2 (2026-05-05) — 忘却論 (Force is Oblivion) シリーズ

外部橋渡しの companion 面: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/曲率は忘却の繰り上がりである_草稿.md` (v0.3, 2026-04-13)

概要. 射影は合成を壊す。三次元の物体を二次元に射影すれば、三次元で成立していた演算は二次元では成立しなくなる。その「ズレ」は消えない。蓄積し、構造を歪め、力として現れる。2026年、二つの独立プロジェクトが同じ構造を異なる言語で証明した。忘却論 (Paper I) は統計多様体上の忘却場 Φ と Chebyshev 1-形式 T から忘却曲率 F_{ij} を導出し、力は忘却の方向的不均一から創発されることを方向性定理として証明した。The Omega Project (automath) は有限バイナリ列の no-consecutive-1s 制約から出発し、fold 演算子 $\Phi_{\mathrm{fold}}$ と加算 ⊕ の非可換性を carry defect δ として形式化し、Lean 4 で 3,427 以上の定理を機械検証した。本稿は両者の構造的対応を、定理・schema・open・supporting evidence を切り分けつつ示す。carry defect は方向性定理の有限・離散 obstruction model として閉じ、Walsh-Stokes 側は cubical cochain level での discrete Stokes target として閉じる。「忘却なしに力なし」の離散鎖は Lean 4 で証明済みである。他方、連続側の composition drift と defect 2-cell の同定は Open C に残る。さらに、黄金比 φ は外部からの輸入ではなく、n-cell tower の公理的複雑度の成長率として忘却論の内部に存在する。本稿でその proof spine として先に固定するのは Route D — Pauli 排他律 (e_x ∧ e_x = 0) が公理の加法的成長を強制し、Fibonacci 再帰を生むという線 — である。ここで本稿が先に押すのは tower 全体の具体列ではなく、seed に依存しない漸近主張 `growth rate = φ` である。Route A は離散証人、Route C は容量系、Route B は Kalon 読みとして働く。φ は忘却の文法の成長率である。

先行論文との関係: Paper I (力としての忘却) — 方向性定理 Th.5.1、合成ドリフト §9.5 OP-I-2。Paper V (繰り込みは忘却である) — c 定理、β 関数。Paper VIII (存在は忘却に先行する) — α-忘却濾過。Paper III (Markov 圏の向こう側) — Z₂ 次数付き構造、Pauli 排他律。Paper VI (行為可能性は忘却である) — G∘F 結晶化、Kalon。Paper IX (エントロピーは忘却である) — CPS エントロピー単調性。
外部参照: The Omega Project (automath) — Lean 4, 3,427+ theorems, axioms=0.

> **記号規約.** 本稿では Paper I の忘却場を $\Phi: M \to \mathbb{R}$、automath 側の fold 演算子を $\Phi_{\mathrm{fold}}: X_{m+1}\to X_m$ と書き分ける。旧稿で automath fold を bare $\Phi$ と書いた箇所は、系列横断では $\Phi_{\mathrm{fold}}$ と読む。

---

## §1　射影は合成を壊す

射影は情報を捨てる。誰でも知っている。

だが、**射影が合成を壊す**ことは、はるかに過小評価されている。三次元の物体を二次元に射影すれば、三次元で成立していた演算は二次元では成立しなくなる。その「ズレ」は消えない。蓄積し、構造を歪め、力として現れる。

2026 年、二つの完全に独立したプロジェクトが、同じ構造を異なる言語で証明した。

一方は**忘却論** (Force is Oblivion) — 統計多様体上の忘却場 $\Phi$ と Chebyshev 1-形式 $T$ から忘却曲率 $F_{ij}$ を導出し、**力は忘却の方向的不均一から創発される**ことを方向性定理として証明した (Paper I, Th.5.1)。

他方は **The Omega Project** (automath) — 有限バイナリ列の no-consecutive-1s 制約から出発し、fold 演算子 $\Phi_{\mathrm{fold}}$ と加算 $\oplus$ の安定語上での非可換性を **carry defect** $\delta$ として形式化し、Lean 4 で 3,427 以上の定理を機械検証した。

これは挑発ではない。本稿が示すのは ——

結論を先に述べれば ——

1. **carry defect は忘却曲率の有限・離散 obstruction model である** — automath の carry defect $\delta(x,y) = \Phi_{\mathrm{fold}}(x \oplus y) - \Phi_{\mathrm{fold}}(x) \oplus \Phi_{\mathrm{fold}}(y)$ は、忘却論の合成ドリフト $\delta = G(f \circ g) - G(f) \circ G(g)$ の有限・離散側に現れる nonsplit witness である。Lean 4 で閉じているのは projection / restriction に沿った discrete defect cocycle の層までであり、連続側の composition drift と defect 2-cell の同一視は Paper I §9.5 の Open C に残る

2. **Walsh-Stokes 側は cubical cochain level の discrete Stokes target を与える** — automath の `walshFlux` と `deltaSet` は忘却場の Leibniz 規則 $d(\Phi T) = d\Phi \wedge T + \Phi \cdot dT$ に向かう離散外微分対応を与える。ここで閉じるのは、$\Delta^n$ と `Man_No11` を足場にした cubical / multilinear / boundary-face observable 上の chain-map surface である。$\mathbf{Man}$ 全体への拡張は open である

3. **OP-I-2 の離散鎖は Lean 4 で強く支持される** — no-consecutive-1s 制約が消えると carry defect は消え、fold は厳密な環準同型へ戻る。だが連続側では $\delta = 0 \Rightarrow \mathrm{Hom}_\Phi \in \{0,1\}$ は既存公理だけでは出ない。ここには追加公理 `ZeroForgetCollapse` と、離散から連続へのリフトが残る

4. **黄金比 $\varphi$ は忘却論の内部に存在する** — ただし本稿で proof spine として先に固定するのは Route D である。Pauli 排他律 ($e_x \wedge e_x = 0$) が公理の加法的成長を強制し、$|A(n)| = |A(n-1)| + |A(n-2)|$ (Fibonacci 再帰) を生む。ここで直接に押すのは tower 全体の具体列ではなく、seed 非依存の漸近主張 `growth rate = \varphi` である。Route A はその離散証人、Route C は容量版の系、Route B は Kalon 読みである。$\varphi$ は忘却の文法の成長率である

これらの主張を、以降の節で順に示す。

### 1.1 主張境界 ledger

| 層 | 本稿で押す内容 | SOURCE / donor | 本稿でまだ押さない内容 |
|:---|:---|:---|:---|
| Theorem A | `CubeExp_proj` と `Man_No11` 実装包絡における projection / restriction の strict functoriality | D5 | $\mathbf{Man}$ 全域での strict functor completion |
| Theorem B | `d \mapsto \mathrm{deltaSet}`, `\int \mapsto \mathrm{walshFlux}` の cubical cochain level chain-map | D7 | 一般 smooth function 全体への chain-map 拡張 |
| Schema C1 | carry defect を方向性定理の finite discrete obstruction model として読む | D5-D6 | 連続側 composition drift と discrete defect cocycle の equality |
| Open C | lax monoidal coherence の defect 2-cell 同定 | §5.3, D9 | completed theorem としての連続側橋 |
| Supporting evidence | q=5 anomaly, `e_2(A_5)=11`, 符号反転 donor は C1 の数値的補助証拠 | D4 | Theorem A/B/Open C の proof spine そのもの |

---

## §2　二つの世界

### 2.1 automath の世界 — 有限バイナリ窓からの導出

有限系を、1-bit 窓で $m$ ステップ観測する。

全状態空間 $\{0,1\}^m$ は $2^m$ 個である。

だが、解像度をまたいで安定な語、すなわち連続する 1 を含まない語は、$F_{m+2}$ 個しかない。$F_n$ は Fibonacci 数である。

この制約は選ばれたのでない。解像度間整合性が強制する。

安定語空間 $X_m$ 上で、fold 演算子 $\Phi_{\mathrm{fold}}: X_{m+1} \to X_m$ を定める。末尾 bit を切り捨てる。$\Phi_{\mathrm{fold}}$ は情報を捨てる。忘却する。

$X_m$ には Zeckendorf 表現による自然な加算 $\oplus$ がある。$X_m \cong \mathbb{Z}/F_{m+2}\mathbb{Z}$ である。安定語空間は Fibonacci 数を法とする商環である。$F_{m+2}$ が素数なら ($F_3 = 2, F_5 = 5, F_7 = 13, F_{13} = 233, \ldots$)、有限体になる。

ここで問うべきは一つである。fold と加算は可換か。

$$\Phi_{\mathrm{fold}}(x \oplus y) = \Phi_{\mathrm{fold}}(x) \oplus \Phi_{\mathrm{fold}}(y) \quad \text{?}$$

答えは否である。

### 2.2 carry defect — 射影と合成の非可換性

automath は次の定理を Lean 4 で証明する (`restrict_stableAdd_carry_defect`)。

$$\Phi_{\mathrm{fold}}(x \oplus y) = \Phi_{\mathrm{fold}}(x) \oplus \Phi_{\mathrm{fold}}(y) \oplus \kappa \cdot e_m$$

- $\kappa \in \{0, 1\}$ — **キャリー指標 (carry indicator)**。$x$ と $y$ の安定値の和が Fibonacci 数 $F_{m+3}$ に達するか超えるとき $\kappa = 1$ である。それ以外では $\kappa = 0$ である
- $e_m$ — **キャリー要素 (carry element)**。その安定値は $F_m$ である。Lean 4 で $m = 5, \ldots, 13$ が検証済みである

直感的に言えば: 先に足してから射影すると、先に射影してから足す場合と比べて、$\kappa \cdot e_m$ という「余り」が残る。この余りが carry defect である。情報が完全保存される世界、すなわち制約のない世界では、carry は生じない。

### 2.3 忘却論の世界 — 統計多様体上の忘却場

忘却論 (Paper I) は、統計多様体 $(M, g, C)$ 上に忘却場 $\Phi(\theta)$ を定義する。

$$\Phi(\theta) = D_{\text{KL}}(p_\theta \| q)$$

- $D_{\text{KL}}$ — **Kullback-Leibler ダイバージェンス (Kullback-Leibler divergence)**。二つの確率分布のあいだの「忘却度」である
- $p_\theta$ — パラメータ $\theta$ が定める確率分布
- $q$ — 基準分布

Chebyshev 1-形式 $T_i = g^{jk}C_{ijk}$ は、$\alpha$-接続が Levi-Civita 接続から最もずれる方向を指定する。忘却場の勾配 $d\Phi$ がこの方向と揃わないとき、すなわち $d\Phi \wedge T \neq 0$ のとき、忘却曲率が生じる。

**方向性定理** (Paper I, Th.5.1):

$$F_{ij} \neq 0 \iff d(\Phi T) \neq 0$$

直感的に言えば: 一様に忘れれば力はゼロである。不均一に忘れれば曲率が立ち上がる。それが力として働く。

### 2.4 共通構造 — 射影は合成を壊す

二つの世界を並べる。

| | automath (離散) | 忘却論 (連続) |
|:---|:---|:---|
| 空間 | $X_m \cong \mathbb{Z}/F_{m+2}\mathbb{Z}$ | $M$ (統計多様体) |
| 忘却場 | $f: X_m \to \mathbb{Z}$ (安定値) | $\Phi: M \to \mathbb{R}$ |
| 射影 | fold $\Phi_{\mathrm{fold}}: X_{m+1} \to X_m$ | 忘却関手 $G: C \to D$ |
| 合成 | 安定語加算 $\oplus$ | 射の合成 $f \circ g$ |
| **defect** | $\delta(x,y) = \kappa \cdot e_m$ [Lean 証明済み] | $\delta = G(f \circ g) - G(f) \circ G(g)$ [OP-I-2 予想] |
| **曲率条件** | $\kappa \neq 0$ | $d(\Phi T) \neq 0$ |
| ゼロ忘却 | No11 制約が消滅 → $\delta = 0$ → 環準同型 [Lean] | $\Phi = 0 \Rightarrow \ker(G)=\{0\} \Rightarrow \delta = 0$ は押せるが、$\delta = 0 \Rightarrow \mathrm{Hom}_\Phi \in \{0,1\}$ には `ZeroForgetCollapse` が必要 [Open] |

構造は同一である。射影は合成を壊す。壊れ方の尺度が defect であり、曲率であり、力である。

ここでいう不均一と曲率は、別々の対象を比喩的に対応させたものではない。状態の差が、比較の向きや合成の順序に依存して残るとき、その同じ差分構造を、状態の記述では不均一と呼び、幾何学の記述では曲率と呼ぶ。

Paper I では、この同一性は $F_{ij} = (\alpha/2)[d(\Phi T)]_{ij}$ として書かれる。すなわち、$d(\Phi T)$ は忘却の方向的不均一であり、同時に、それが曲率テンソル $F_{ij}$ として測られる。

したがって、不均一が曲率に似ているのではない。不均一が、幾何学的に書かれたものが曲率である。

---

## §3　三つのメタファー — 曲率は繰り上がりから生まれる

### 3.1 結晶学 — 転位は射影の carry である

溶液から結晶を析出させる操作を考える。高次元の溶液場を、低次元の結晶格子へ射影する。完全結晶では格子は厳密に保たれる。carry はゼロである。

だが実結晶には **転位 (dislocation)** がある。原子配置は局所的にずれる。格子の合成法則は壊れる。転位は結晶内に曲率を作る。転位密度は結晶強度を定める物理的な力である。

$$\text{perfect crystal} \leftrightarrow \kappa = 0, \quad \text{dislocation} \leftrightarrow \kappa = 1$$

これは比喩ではない。Paper VI が示した通り、忘却関手 $G$ の結晶化随伴 $F \dashv G$ において、$\text{Fix}(G \circ F)$ は Kalon である。固定点からのずれが曲率を生む。carry element $e_m$ は、離散結晶における転位の量的表現である。

### 3.2 地図学 — Mercator 歪みは carry である

球面から平面への地図射影を考える。Mercator 射影は角度を保つ。面積を歪める。球面上の二点 A と B の距離を足してから射影した値は、各距離を射影してから足した値と一致しない。

$$P_{\mathrm{map}}(d_A + d_B) \neq P_{\mathrm{map}}(d_A) + P_{\mathrm{map}}(d_B)$$

この差が Mercator の面積歪みである。赤道近傍では ($\kappa = 0$) 歪みは小さい。極付近では ($\kappa = 1$) 歪みは巨大になる。Greenland が Africa より大きく見える。その像が、射影と合成の非可換性を直接に可視化する。

### 3.3 会計学 — 丸めは carry である

複数通貨の集計を考える。三通貨で報告された利益を先に集計してから円換算する場合と、各項目を先に円換算してから集計する場合では、結果が一致しない。丸め誤差が生じる。

$$P_{\mathrm{acct}}(\text{aggregate}) \neq P_{\mathrm{acct}}(\text{item 1}) + P_{\mathrm{acct}}(\text{item 2}) + P_{\mathrm{acct}}(\text{item 3})$$

この丸め誤差は、通貨が統一されない限り消えない。通貨統一 = ゼロ忘却 = ゼロ carry である。複数の「物差し」がある限り、射影の丸めは構造的に避けられない。

三つのメタファーの数学的対応を示す。

| メタファー | 射影 | 合成 | carry | 曲率 |
|:---|:---|:---|:---|:---|
| 結晶 | 溶解 → 析出 ($G$) | 格子合成 | 転位 | 結晶応力 |
| 地図 | 球面 → 平面 | 距離加算 | 面積歪み | Gaussian curvature |
| 会計 | 円換算 | 通貨集計 | 丸め誤差 | 為替差損益 |
| automath | fold $\Phi_{\mathrm{fold}}$ | $\oplus$ | $\kappa \cdot e_m$ | defect ≠ 0 |
| 忘却論 | $G$ | $f \circ g$ | $\delta$ | $F_{ij} \neq 0$ |

---

## §4　Walsh-Stokes と Leibniz — 離散化関手の構成

### 4.1 忘却曲率の Leibniz 分解

Paper I §3.3 では、忘却曲率は次の Leibniz 規則から導かれる。

$$F_{ij} = \frac{\alpha}{2}[d(\Phi T)]_{ij} = \frac{\alpha}{2}[(d\Phi \wedge T) + \Phi \cdot dT]_{ij}$$

- $d\Phi \wedge T$ — **方向的不整合項 (directional misalignment term)**。忘却の勾配が Chebyshev 形式と揃わない
- $\Phi \cdot dT$ — **Chebyshev ねじれ項 (Chebyshev torsion term)**。Chebyshev 形式そのものが閉じていない

指数型族では $dT = 0$ が恒等的に成り立つ。ゆえに力の生成は、方向的不整合 $d\Phi \wedge T \neq 0$ に全て還元される (Paper I, Cor. 5.1.1)。

### 4.2 automath の Walsh-Stokes

automath の `WalshStokes.lean` は、ハイパーキューブ $\{0,1\}^n$ 上の離散外微分を定義する。

$$\text{deltaSet}(A, f, w) = \sum_{B \subseteq A} (-1)^{|B|} f(\text{flip}(B, w))$$

- $A \subseteq \text{Fin}(n)$ — 微分する方向の集合
- $f: \{0,1\}^n \to \mathbb{Z}$ — ハイパーキューブ上の関数
- $\text{flip}(B, w)$ — $w$ のうち $B$ に属する bit を反転する

**Walsh フラックス (Walsh flux)** は境界上の離散積分である。

$$\text{walshFlux}(A, f) = \sum_{w \in \text{BoundaryWords}(A)} \text{deltaSet}(A, f, w)$$

Lean 4 で検証された性質:

- `deltaBit_comm`: 単一座標微分は可換である。連続系の $\partial_i \partial_j = \partial_j \partial_i$ に対応する
- `walshFlux_insert`: bit 挿入に対する再帰分解である。離散 Stokes 恒等式の具体形である

### 4.3 Leibniz 規則の離散描像

二つの世界の対応を示す。

| 連続系 (Paper I §3.3) | 離散系 (automath) |
|:---|:---|
| $d(\Phi T)$ | $\text{deltaSet}(A, f)$ |
| $d\Phi \wedge T$ (方向的不整合) | $\text{walshFlux}(A, \text{deltaSet}(\{i\}, f))$ |
| $\Phi \cdot dT$ (ねじれ) | $f \cdot d_{\text{discrete}}A$. $dT = 0 \iff A$ は平坦である (standard basis) |
| 指数型族 $dT = 0$ → 力は $d\Phi \wedge T$ のみから生じる | 標準ハイパーキューブ → 力は carry のみから生じる |

Walsh 基底は位置 $w$ に依存しない。ゆえに離散 Chebyshev torsion は恒等的にゼロである。automath の世界は「離散指数型族」に対応する。

### 4.4 離散化 bridge の三層分解 — strict / chain-map / Open C

上の対応は、単一の「$D: \mathbf{Man}\to\mathbf{Hyp}$ は関手か」という問いでは粗すぎる。2026-04 の再定式化では、問題は strict 1-functor 部分、chain-map 部分、lax monoidal coherence の defect 2-cell 同定に分かれる [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/関手の合成保存問題_再定式化.md L8]。

> **構造的対応** (schema $D$). $D$ は、統計多様体の幾何をハイパーキューブ側へ対応づける局所的な構造対応である。少なくとも $D(M)=\{0,1\}^n$, $D(\Phi)=f$, $D(T)=A\subseteq\mathrm{Fin}(n)$, $D(d)=\mathrm{deltaSet}$, $D(\wedge)=\mathrm{carry\ defect}$ という対応を持つ [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/形式化仕様書.md L27]。

1. **定理 (Theorem A: strict 1-functor 部分)**. `CubeExp_proj`、すなわち product Bernoulli family $M_I=(\Delta^1)^I$ と座標忘却 $\pi_{J\subseteq I}$ からなる部分圏では、$D_{\mathrm{proj}}(\pi_{J\subseteq I})=\mathrm{restrict}_{J\subseteq I}$ と置くことで ordinary composition の strict functoriality が成り立つ [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/関手の合成保存問題_再定式化.md L120]。Lean 側の witness は `restrict_functorial` である [Lean: restrict_functorial in Omega/Folding/Defect.lean]。旧稿の「$D$ が厳密に関手なのは `Man_No11` に限定したときである」という観察は、ここでは「Theorem A は `CubeExp_proj` 上で成立し、`Man_No11` はその strictness を保持する実装包絡である」と読む [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/三者対応辞書.md L394]。

2. **定理 (Theorem B: chain-map 部分)**. 観測量を multilinear observable / cubical cochain に制限すると、`deltaSet` は混合偏微分の cell 積分に一致する。したがって $d\mapsto\mathrm{deltaSet}$ と $\int\mapsto\mathrm{walshFlux}$ は、単なる類推ではなく cubical cochain のレベルで実定理に落ちる [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/関手の合成保存問題_再定式化.md L180]。この層が閉じるのは、一般の滑らかな関数全体ではなく、cubical / multilinear / boundary-face 版に限られる [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/関手の合成保存問題_再定式化.md L245]。

3. **予想 (Open C: lax monoidal coherence の defect 2-cell 同定)**. 残る核心は、ordinary functoriality ではなく、加法・合成・composition drift まで含めた monoidal coherence である。automath 側では `restrict_stableAdd_carry_defect` と `globalDefect_compose` が defect 2-cell を担い、bridge の型は strict functor だけでなく lax monoidal functor / pseudofunctor として読む必要がある [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/関手の合成保存問題_再定式化.md L255] [Lean: globalDefect_compose in Omega/Folding/Defect.lean] [Lean: restrict_stableAdd_carry_defect in Omega/Folding/CarryDefect.lean]。bridge essay も、忘却関手を lax functor として読み、laxity/compositor が carry defect と忘却曲率の対応点であると明記している [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/曲率は忘却の繰り上がりである_草稿.md L99]。

したがって、本稿の主張は「$\mathbf{Man}$ 全域で離散化関手が完成した」ではない。正確には、strict 1-functor 部分と chain-map 部分は閉じ、残る未解決核が defect 2-cell の連続側同定へ縮約された、である。**合成保存**: ordinary composition としての合成保存は Theorem A の範囲で閉じ、monoidal coherence としての合成保存は Open C に残る。完全な open は §5.3 で Open C として整理する。

ここで q=5 anomaly や `e_2(A_5)=11` の donor は、C1 を補強する**supporting evidence**ではあっても、Theorem A/B/Open C の proof spine ではない。本稿の spine は projection functoriality / cubical chain map / defect 2-cell open の三層で立て、q=5 donor は数値的補助証拠として外周に留める。

---

## §5　ゼロ忘却極限 — OP-I-2 の現在地

### 5.1 予想 OP-I-2 の修正

Paper I §9.5 は次の景色を提示した。

> **圏論 = $\Phi \to 0$ 極限** — 方向性定理より $F_{ij} = (\alpha/2)[d(\Phi T)]_{ij}$ である。ゆえに $\Phi \to 0$ 極限では忘却曲率は消える。合成ドリフト $\delta = G(f \circ g) - G(f) \circ G(g)$ もゼロへ行く。$\ker(G) = \{0\}$ となる。Hom 空間は $[0,1]$ から $\{0,1\}$ へ退化する。これは標準圏の公理に他ならない。

直感は正しい方向を向いている。だが 2026-04-14 の形式化検証は、ここに二つの切断面があることを示した。

第一に、

$$F = 0 \;\centernot\Rightarrow\; \Phi = 0$$

である。均一忘却 $\Phi = \mathrm{const} \neq 0$ では $d\Phi = 0$ だから力は消える。だが忘却そのものは残る。したがって「力なし」と「忘却なし」は同じ命題ではない。

第二に、

$$\delta = 0 \;\centernot\Rightarrow\; \mathrm{Hom}_\Phi \in \{0,1\}$$

である。OP-I-2 の核心は、いまや次の一方向鎖として読むべきである。

$$\Phi = 0 \Rightarrow \ker(G)=\{0\} \Rightarrow \delta = 0$$

ここまでは押せる。だが最後の

$$\delta = 0 \Rightarrow \mathrm{Hom}_\Phi \in \{0,1\}$$

は既存公理だけでは出ない。ここに追加公理 `ZeroForgetCollapse` が要る。

Euclid 幾何と Riemann 幾何の比喩はまだ生きている。壊れたのは比喩ではない。壊れたのは、「ゼロ曲率なら自動的に Boolean に落ちる」という未証明の飛躍である。

### 5.2 automath が与える離散的証拠

automath の世界では、no-consecutive-1s 制約が laxity の源である。制約があると carry defect が立ち上がる。制約を外すと carry defect は消える。fold は strict に戻る。

no-consecutive-1s 制約が消えると、全ての語が安定になる。$X_m = \{0,1\}^m$ となる。fold $\Phi_{\mathrm{fold}}$ は単なる bit 切り捨てになり、加算 $\oplus$ は通常の mod 加算へ戻る。このとき carry defect を生む Fibonacci 閾値は拘束力を失う。

$$\kappa = 0 \quad \text{for all } x,y$$

したがって fold は厳密な準同型へ戻る。

$$\Phi_{\mathrm{fold}}(x \oplus y) = \Phi_{\mathrm{fold}}(x) \oplus \Phi_{\mathrm{fold}}(y)$$

離散側が示しているのは、「制約が compositor を生み、その制約の消失が strictness を回復する」という骨格である。これは OP-I-2 の方向を強く支持する。だが、それだけで連続側の $[0,1]$-豊穣が自動的に $\{0,1\}$-豊穣へ崩壊するとは言えない。

| ゼロ忘却の論点 | automath が与えるもの |
|:---|:---|
| $\Phi = 0$ に対応する極限は何か | No11 制約の trivial 化 |
| $\ker(G)=\{0\}$ は起こるか | 全語が stable になり、制約起源の核が消える |
| $\delta = 0$ は起こるか | carry defect が消え、fold が strict に戻る |
| Boolean 回復は自動か | 離散相では strict 化が見える。連続側の Boolean 崩壊は別問題として残る |

離散証明は連続証明の代用品ではない。離散証明は、連続側で何を証明しなければならないかを切り分ける装置である。

### 5.3 連続版への持ち上げ — Open C と三つの実装路線

OP-I-2 の連続極限リフトは、`関手の合成保存問題の再定式化` (2026-04) で問題位相が 1 段下がった。1-functor 部分と chain-map 部分は閉じた (Theorem A / B, §4.4)。残る open は **Open C: lax monoidal coherence の defect 2-cell 同定** に縮約される。すなわち合成ドリフト $\delta$ を Čech 型 2-cocycle $\kappa$ として連続側で同定する課題である [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/関手の合成保存問題_再定式化.md L22] [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/関手の合成保存問題_再定式化.md L313]。

Open C は単一の問題だが、3 つの独立な実装路線を持つ:

ただし、**continuous recipient の順序**は並列同格ではない。本稿が first recipient として採るのは **Čech 型 2-cocycle** である。これは defect 2-cell を obstruction class として最小限に受ける器だからである。**central extension** はその非分裂性を algebraic に読む第二表現であり、**gerbe 的障害**は branchwise completion を与える第三表現である。逆に composition drift $\delta$ 自体は受け皿ではなく、これらの器へ同一視されるべき連続側の現象である。

1. **路線 1 (Dual citizenship 採用の橋梁公理)**: `ZeroForgetCollapse` を **A+B Dual citizenship 構造** で採用し (d)→(e) を局所固定する。これは `\delta=0` から Boolean 回復が自動ではないというギャップを、橋梁公理として明示的に塞ぐ路線である [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/三者対応辞書.md L166]。**射程明示** (2026-04-27 第三次更新): 「Boolean 化」の意味を 3 軸 (Hom 集合の濃度 / 値 / 存在 indicator) に分解した結果、ZFC は 2 解釈下で異なる地位を持つ — **解釈 A (V-enriched [0,1] base 文脈)** では独立公理 (反例 min合成圏が有効、派生候補は **2 経路 ((a) Lawvere Boolean topos / (c) HoTT)** に縮約。(d) Smithe Bayesian lens 合成は /noe+ L3 で **派生不能 (Closed)** 確定 — Kleisli morphism collapse は base monoidal V を変えない enriched category theory 標準事実 + Paper II §7.5 インデックス圏不一致 (Poly vs (ℝ,≤)) の二重防御) / **解釈 B (Set existence indicator 文脈)** では Paper IX §3.5(ii) からの派生定理候補 (Mor(C_α)(I,X) = ∅ なら indicator 0、≠ ∅ なら indicator 1)。同一 ZFC が 2 解釈下で並列保持される (Yugaku Definition Surface Protocol)。**Boolean 化 3 軸 ↔ 派生候補 ↔ 解釈の 3:3 対応構造**: (i) 濃度↔3.1 Lawvere↔解釈 A / (ii) 値↔3.4 Smithe (Closed)↔解釈 A / (iii) indicator↔3.3 HoTT + 3.2 Paper IX↔解釈 A or B。詳細は `三者対応辞書.md` §7.5 OT-S05-3 + OP-S05-3.1〜3.4。

2. **路線 2 (極限戦略)**: $\{0,1\}^{\mathbb{N}}$ を固定 ambient profinite として、$\lambda$-依存弱*連続測度族 $\mu_\lambda$ を構成する。これは $X_\infty(\lambda)$ 自体を動かす案ではなく、期待値の連続変形を問う路線である [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/三者対応辞書.md L196] [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/三者対応辞書.md L208]。

3. **路線 3 (関手 debt)**: `Discretizable` + `DescendsToCube` typeclass を付与した $\mathbf{Man}$ 上の射クラスへ拡張し、Strategy B (逆極限経由) で `discretize_functorial` の sorry を剥がす。これは full $\mathbf{Man}$ 上の無条件 strict functor 化ではなく、descent data を持つ射への拡張である [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/三者対応辞書.md L357] [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/三者対応辞書.md L394] [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/形式化仕様書.md L86]。

これらは Open C を閉じるために**並行して**進める実装課題であり、互いの代用品ではない。だが recipient と strategy は区別すべきである。Open C 自体の連続側受け皿は、第一に Čech 2-cocycle、第二にその非分裂性を読む central extension、第三に branchwise completion を与える gerbe 的障害、の順で読むのが最も混線が少ない [SOURCE: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/01_草稿｜Drafts/02_伴走｜Companion/automath_bridge/形式化仕様書.md L78]。composition drift $\delta$ は受け皿ではなく、そこへ同一視されるべき連続側の現象である。

本稿が与えるのは完成証明ではない。完成証明の設計図である。Open C を 3 路線に分けずに「離散版が真だから連続版も真だ」と言うなら、それは前進ではない。問題位相の 1 段下げ (関手 → lax monoidal) を見ないふりしただけである。

### 5.4 Landauer 的熱散逸 — 曲率そのものではなく物理的観測像

ここで、物理的計算における Landauer 的熱散逸を、本稿の忘却曲率と直結させる誘惑が生じる。だが同一視してはならない。Landauer の原理が与えるのは、忘却が物理的消去として実装されるときの最小熱価格である [9]。一方、本稿の曲率は、その忘却が合成と可換でないときの構造的 defect を測る。Bennett が示したように、計算そのものは可逆な履歴保存として実装できる [10]。熱価格が必然化するのは、計算ではなく、保存された区別を本当に消去する局面である。

したがって、熱散逸は曲率そのものではない。熱散逸は忘却射 $G$ の非単射性に対する scalar cost であり、曲率は $G$ の非可換性に対する obstruction である。$G$ が一様な消去なら、消去価格はありえても曲率は立たない。これは §5.1 の注意、すなわち $F = 0$ は $\Phi = 0$ を含意しない、という区別と同じである。

逆に、$G$ が合成順序に依存して異なる区別を潰すなら、二つの経路

$$G(f \circ g) \qquad \text{and} \qquad G(f) \circ G(g)$$

は同じ忘却価格を持つとは限らない。このとき合成ドリフト

$$\delta_G(f,g) = G(f \circ g) - G(f) \circ G(g)$$

は、Landauer 的には「どの順で忘れるか」によって消去される履歴・区別・fiber が変わることを意味する。熱力学的に観測されうるのは、曲率そのものではなく、同じ defect を物理的消去過程へ実装したときに現れうる経路依存的な cost gap である。すなわち Landauer は Open C を閉じる第四路線ではない。Open C が同定しようとしている defect 2-cell を、物理的消去過程へ写したときに現れる熱力学的観測像である。

外部実験は本稿命題を実証するものではなく、scalar erasure baseline / 実装依存 cost / feedback 会計を分ける donor として使う。Bérut et al. は一ビット消去の scalar baseline を与えるに留まる [11]。Gavrilov-Bechhoefer、Dago-Bellon、Ciampini et al. は、消去費用がポテンシャル非対称性、有限時間、慣性、初期非平衡資源に依存することを示す donor である [12-15]。Toyabe / Koski 系は feedback と mutual information の熱力学会計であり、erasure curvature の直接測定ではない [16-18]。よって C6 が言えるのは、合成順序に依存する忘却が物理的消去へ実装された場合、その差分が経路依存的な消去価格として観測されうる、までである。

---

## §6　collision kernel — 忘却論の新しいスペクトル不変量

**定義 6.0.1 (collision kernel).** 各 $m$ について $d_m(x) := |\Phi_{\mathrm{fold}}^{-1}(x)|$ を fold fiber の衝突多重度とする。$q \geq 2$ に対し、モーメント和

$$S_q(m) := \sum_{x \in X_m} d_m(x)^q$$

が有限階の線形漸化式を満たすとき、その companion operator $A_q$ とスペクトル不変量 $(\mathrm{tr}(A_q), \det(A_q))$ の組を **collision kernel** $K_q^{\mathrm{coll}}$ と呼ぶ。これは現段階では automath 側で定義済みの離散不変量であり、忘却論側の RG 不変量への輸入は §6.2 の仮説に留める。

### 6.1 moment sum と companion matrix

automath は、fold の fiber 構造に対する **モーメント和 (moment sum)** $S_q(m) = \sum_{x \in X_m} d_m(x)^q$ を定義し、それが線形漸化式を満たすことを証明する。

$S_2$ の漸化式は次である。

$S_2(m+3) = 2 S_2(m+2) + 2 S_2(m+1) - 2 S_2(m)$

この漸化式を支配する 3×3 の **コンパニオン行列 (companion matrix)** $A_2$ は次である。

$$A_2 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & 2 & 2 \end{pmatrix}, \quad \text{tr}(A_2) = 2, \quad \det(A_2) = -2$$

$S_3$ と $S_4$ に対してもコンパニオン行列が定義され、Lean 4 で次が証明されている。

$$\text{tr}(A_q) = 2, \quad \det(A_q) = -2 \quad \text{for } q = 2, 3, 4$$

### 6.2 普遍不変量の忘却論的解釈

忘却論の Paper V (繰り込みは忘却である) は、$\beta$-関数と忘却場のスケール不変性を定式化した。だが、fiber 構造上のモーメント和に対応する概念は持たない。

tr = 2, det = -2 という普遍不変量は、忘却論への新しい輸入である。

解釈仮説を置く。忘却場 $\Phi(\theta, \mu)$ のスケール $\mu$ に沿う fiber 分布のモーメント和 $S_q(\mu)$ を定義する。そのコンパニオン行列のスペクトルを、忘却場の **繰り込み群不変量 (renormalization group invariant)** とみなす。もしこの不変量が、忘却論の枠内でも tr = 2, det = -2 を与えるなら、それは忘却の **普遍性類 (universality class)** の代数的表現である。

この仮説の検証は今後に残す。

---

## §7　反論と展望

### 7.1 「離散版は連続版の証明ではない」

その通りである。有限体上の定理は、統計多様体上の定理を含意しない。

だが、この反論に対しては三つの反駁が立つ。

**第一: 格子ゲージ理論の先例 (Wilson 1974)**。連続ゲージ理論 (Yang-Mills) の離散版としての格子ゲージ理論には、50 年の主流物理学の蓄積がある。格子上の plaquette action は、連続曲率 tensor $F_{\mu\nu}$ の離散版である。両者は連続極限で接続する。automath の carry defect と忘却論の忘却曲率 $F_{ij}$ の関係は、Wilson 格子の plaquette と Yang-Mills の $F_{\mu\nu}$ の関係と構造同型である。ここで言う「離散版」は、全域定理というより、連続版の**局所的な離散模型**としての資格を持つ、という意味である。

**第二: 圏論的単体 $\Delta^n$ の橋**。Paper I Appendix B は、圏論的単体 $\Delta^n$、すなわち離散確率分布上で、方向性定理の具体計算を完了した。$\Delta^n$ 上の Chebyshev 1-形式は $T_i = 1 - (n+1)p_i$ である。指数型族ゆえに $dT = 0$ が成り立つ。一様分布 $(1/3, 1/3, 1/3)$ では $F_{12} = 0$ である。非対称点 $(0.15, 0.15, 0.70)$ では $F_{12} = -2.728$ である。$\Delta^n$ は $\{0,1\}^n$ の統計多様体への持ち上げの自然候補である。各 bit 位置を Bernoulli 確率変数と読めば、安定語 (No11 制約) は Bernoulli 積空間の制約付き部分多様体に対応する。carry defect は、この部分多様体上で方向性定理を有限・離散 obstruction model として可視化する witness である。

**第三: Baez–Stay (2009) の「Rosetta Stone」方法論**。異なる圏のあいだの構造的類似そのものが、数学的対象である。自然変換である。automath と忘却論の対応を自然変換として構成すること、それが離散化関手 $D$ の関手性を証明することに他ならない。Baez–Stay は、物理学・位相・論理・計算の対応を、「単なる比喩」としてでなく、「関手的対応」として定式化した。本稿の第一主張も同じ方法論に従う。

二つの独立理論が、互いを知らずに、同じ構造を独立導出した。この事実は、その構造が偶然でなく必然であることの強い証拠である。離散版の存在は、連続版証明の設計図を与える。

### 7.2 「構造対応は偶然かもしれない」

対応が一つだけなら、偶然を排除できない。だが本稿が示した対応は次の六つである。

1. carry defect $\leftrightarrow$ composition drift
2. walshFlux $\leftrightarrow$ boundary integral
3. deltaSet $\leftrightarrow$ exterior derivative
4. carry indicator $\leftrightarrow$ curvature condition
5. fold の関手性 $\leftrightarrow$ coarse-graining の半群性
6. ゼロ忘却極限 $\leftrightarrow$ 標準圏の回復

六つの独立対応が同時に成り立つ確率は、各偶然確率の積である。

### 7.3 「忘却論に黄金比 $\varphi$ がないのは致命的である」

逆である。$\varphi$ は最初から忘却論の内部にあった。連続極限では見えなかっただけである。$\varphi$ は格子現象だからである。離散的な自己参照再帰の収束率だからである。既存公理系の内部から $\varphi$ へ至る線は四本ある。だが四本は同格ではない。本稿で証明の主線として採るのは Route D である。Route A は離散証人、Route C は容量系、Route B は事後的な Kalon 読みである。先に閉じるべきは spine であって、修辞ではない。

**Route A (Discrete witness): 反 Markov セクターの成長率としての $\varphi$**

Paper III (Markov 圏の向こう側) は、$\alpha < 0$ セクターが $\mathbb{Z}_2$ 次数付き反可換構造を持つことを確立した。anti-copy nilpotency $e_x \wedge e_x = 0$ は、Pauli 排他律の圏論的翻訳である (Paper III §3.1(D))。同一の構造単位が隣接位置を占めることを禁じる。

$m$ 個の格子点を持つ 1 次元離散格子で、この隣接排他を課すと、許される配置数はちょうど $F_{m+2}$ になる。Fibonacci 数である。漸近成長率は $\varphi = (1+\sqrt{5})/2$ である。

これは automath の no-consecutive-1s 制約そのものである。黄金比は、$\alpha < 0$ セクターにおける、最小の fermionic exclusion の下で生き残る構造の成長率である。だがここで得られるのは C3-core そのものではなく、同じ排他則が離散格子上で何を生むかを示す**離散証人**である。

**Route B (Interpretive reading): 溶解-結晶化随伴の Kalon としての $\varphi$**

自己参照方程式 $\varphi = 1 + 1/\varphi$ は固定点方程式である。Paper VI の言語で次を定める。

- $F$ (dissolution): $x \mapsto x + x_{n-1}$ — 自由度を一つ加える (Fibonacci 再帰)
- $G$ (crystallization): $x \mapsto x_n / x_{n-1}$ — 比への射影 (fold)

すると $\text{Fix}(G \circ F) = \varphi$ である。Kalon の三属性は満たされる。

1. **Fix**: $\varphi = 1 + 1/\varphi$ (自己参照固定点) ✓
2. **Generative**: $\varphi$ は Fibonacci 数列、黄金螺旋、Penrose tiling, ... を生成する (3+ の非自明導出) ✓
3. **Self-referential**: 定義が自分自身を含む ✓

$\varphi$ は、fold-unfold cycle の Kalon である。忘却と回復が完全につり合う点である。だがこれは $\varphi$ の**出現を導出する線**ではない。出現した $\varphi$ を `Fix(G∘F)` と読めることを示す**解釈層**である。

**Route C (Entropic corollary): 排他下の容量上限としての $\log \varphi$**

Paper IX (エントロピーは忘却である) は、CPS エントロピー単調性定理 (Th. 3.4.1) を証明した。$S_{\text{CPS}}(p, \alpha)$ は $\alpha$ に対して単調増加する。制約のない 1-bit 容量は $\log 2$ である。隣接排他 (no-consecutive-1s) を課すと、容量は $\log \varphi$ に下がる。golden-mean shift の位相エントロピーである。automath はこれを `topological_entropy_eq_log_phi` として機械検証している。

$\log \varphi$ は、最小 fermionic 制約の下での情報ボトルネック容量である。したがって Route C は C3-core の**容量版の系**であり、排他制約が growth rate だけでなく capacity をも $\log \varphi$ へ押し下げることを示す。

**Route D (Core theorem): Pauli 排他律は n-cell tower に Fibonacci 成長を強制する**

忘却関手の n-cell tower (Paper 0 §2.0, Alētheia §3)

$$U_{\text{arrow}}(1) \leq U_{\text{compose}}(1.5) \leq U_{\text{depth}}(2) \leq \cdots \leq U_{\text{self}}(\omega)$$

には、nilpotency が強制する内部 Fibonacci 構造がある。本稿の C3 の proof spine はここにある。

**Lemma F2.1a** (grade の一意性). 各公理 $a$ には、ただ一つの cell grade が割り当てられる。すなわち $a$ が直接に量化する構造の次元は一意であり、同じ公理が同時に二つの cell 次元に属することはない。

*Reason.* n-cell tower の各段は異なる型の構造を対象にする。1.5-cell の合成律、2-cell の自然変換、3-cell の豊穣整合性は、それぞれ別の型を量化する。異なる型に対する命題は、型安全性のもとで定義的に区別される。したがって grade は well-defined である。

**Lemma F2.1b** (役割の非重複). 同一公理は、「直接前提」(grade $n-1$) と「coherence 条件」(grade $n-2$) を同時に担えない。

*Reason.* grade が異なるだけでなく、同じ構造単位が tower の隣接位置を二重占有することになるからである。これは anti-copy nilpotency $e_a \wedge e_a = 0$ (Paper III §2.3, §3.1(D)) に反する。公理は一つの仕事にしか使えない。

**Proposition F2.1** (排他は加法性を強制する). $A(n)$ を、$n$-cell を定義するために新たに必要な独立公理集合とする。このとき:

$$A(n) = A(n-1) \sqcup A(n-2) \quad \text{(disjoint union)}$$

したがって $|A(n)| = |A(n-1)| + |A(n-2)|$ である。Fibonacci 再帰である。

*Proof sketch.* 各層 $n$ は、二つの公理プールから公理を引く。$A(n-1)$ は直接前提である。関係づけられる構造そのものである。$A(n-2)$ は coherence 条件である。合成法則が成り立つための条件である。Alētheia の証明 (Proof 1–7) は、この二層依存を確立している。

補題 F2.1a により、公理の grade は一意である。補題 F2.1b により、同一公理が grade $n-1$ と grade $n-2$ の役割を兼任することはできない。ゆえに $A(n-1)$ と $A(n-2)$ は非交差であり、各層の新公理数は足し算になる。

ゆえに $A(n-1) \cap A(n-2) = \varnothing$ である。和は互いに素である。$\square$

*なぜ tensor product ($\times$) でなく disjoint union ($+$) なのか。* enrichment に現れる tensor product $\text{Hom}(B,C) \otimes \text{Hom}(A,B)$ (Paper III §2.4, Proof 3) は、**インスタンス空間 (instance space)**、すなわち具体的射の空間に作用する。これに対し、公理数 $|A(n)|$ は、instance 数ではなく、独立条件の数を測る。nilpotency は、公理を単一役割に固定する。ゆえに成長は加法になる。インスタンス空間は乗法的に増えうる。だが文法、すなわち公理数は Fibonacci 的に増える。

**Corollary F2.2** (seed 非依存の漸近率). 正の初期値 $|A(1)|, |A(1.5)| > 0$ が与えられ、命題 F2.1 の Fibonacci 再帰が以後の階層で成り立つならば、

$$\lim_{n \to \infty} \frac{|A(n)|}{|A(n-1)|} = \varphi$$

である。特に、seed の確定は tower 全体の**具体列**を与えるためには必要だが、`growth rate = \varphi` という**漸近主張**には不要である。

*Reason.* Fibonacci 型線形漸化式の漸近比は、特性方程式 $x^2 = x + 1$ の正の根 $\varphi$ に収束する。seed は係数を決めるが、支配根は変えない。$\square$

以上で C3-core の骨格は

> 排他性  
> grade 分離  
> `A(n)=A(n-1)\sqcup A(n-2)`  
> Fibonacci  
> seed-free asymptotic growth rate = `\varphi`

の順に定まる。Route A はこの core の離散証人、Route C はその容量版の系、Route B は得られた $\varphi$ を Kalon と読む解釈である。

**黄金比は忘却の文法の seed 非依存の成長率である。**

これが連続定式化 (Paper I) に現れなかったのは、離散的な公理計数構造が連続極限で溶けるからである。格子ゲージ理論の格子間隔が、連続極限で消えるのと同じである。automath は格子上にとどまる。だから $\varphi$ を直接に見る。

**C3-core の残る proof debt.**

1. **`ℤ_2 \to \mathbb{N}` の次数拡張** — Paper III の反可換構造を、n-cell tower の grade へどう持ち上げるか。補題 F2.1c の内部構成が要る。  
2. **seed の確定** — `|A(1)|`, `|A(1.5)|` を実際に数え、再帰を tower 全体の具体列へ落とす必要がある。これは Corollary F2.2 の漸近主張とは別の debt である。  
3. **連続極限リフト** — 「連続では見えないだけ」を slogan で終えず、なぜ公理計数が微分幾何へ溶けるかの橋を作る必要がある。

Lean 4 による autoformalization は、この三件が見えた後の **verification layer** である。本体ではない。先に spine を閉じ、その後に機械検証へ渡す。

### 7.4 展望

- **C3-core (proof spine)**: Route D を recurrence / seed-free asymptotic / concrete-sequence の三層に分ける。先に閉じるべきは命題 F2.1 と系 F2.2 であり、その後に `ℤ_2 \to \mathbb{N}` の次数拡張、seed `|A(1)|, |A(1.5)|` の確定、連続極限リフトを潰す
- **C3 verification layer**: C3-core の recurrence と系 F2.2 を Lean 4 へ落とし、その後で具体列と連続リフトを追加する。autoformalization は proof debt の代用品ではなく、閉じた spine の検証器である
- **C2 (forcing $\leftrightarrow$ $\alpha$-filtration)**: automath の 11-layer conservative extension と、忘却論の $\alpha$-忘却濾過 (Paper VIII) の対応を精密化する。layer 数の不一致 (11 vs. 8) を解く正規化写像を構成する
- **三者統合**: automath の Rosetta Stone (Lean 4) × The Omega (Von Neumann algebras + QCA) × 忘却論 (category theory + information geometry) を統合する。三つの独立言語が同じ構造を記述するなら、その構造こそが物理学の文法である
- **対称性は非対称世界の特殊解として読める** (Tolmetes 2026-05-08): §2.4 共通構造の対応表は、対称的世界 (carry indicator $\kappa = 0$ / Levi-Civita 接続 $\alpha = 0$) を非対称世界 ($\kappa = 1$ / $\alpha \neq 0$) の特殊解として読み返す射影を含意する。Paper VIII が派生する $|F| = g_{\mathrm{eff}} \cdot |T|_g$ は忘却曲率テンソル $F_{ij}$ にノルム射影 (= 方向情報の忘却) を適用して導出されるため、ニュートン力学は忘却論が自身の方向情報を忘却した像として位置づけられる。本稿ではこれを **carry defect の存在論的射影 (existential reading)** と呼び、C4 の射程 (Paper I C5 を物理的同一視に折りたたむ overclaim の禁止) を保ったまま支線として記録する

---

## §8　結語

忘却なしに力はない。carry なしに曲率はない。そして、忘却の文法が成長する率が $\varphi$ である。

完全結晶には転位がない。単一通貨には丸め誤差がない。全情報を保存する系は力を生まない。これらは個別例である。より深い命題は次である。**射影は合成を壊し、Pauli 排他律が、その壊れ方の蓄積速度を規定する。**

automath が Lean 4 で証明したのは、この命題の有限・離散側の obstruction witness と strict / chain-map 部分である。忘却論が統計多様体上で予想したのは、その連続側の方向性定理と Open C の橋である。両プロジェクトは互いを知らずに、同じ構造の異なる層を独立に導いた。

これは偶然ではない。

黄金比 $\varphi$ が連続定式化に現れなかったのは、それが不要だからでない。格子現象だからである。忘却の階層の各公理は、ただ一つの構造役割しか担えない (Pauli 排他律: $e_x \wedge e_x = 0$)。この事実が、公理数を各層で加法的に成長させる。$|A(n)| = |A(n-1)| + |A(n-2)|$ である。Fibonacci である。成長率が $\varphi$ である。ここで seed が未確定でも壊れないのは、本稿の主張が tower の具体列ではなく、その seed 非依存の漸近比にかかっているからである。連続極限では、公理計数は微分幾何へ溶け、$\varphi$ は消える。格子ゲージ理論の連続極限で、格子間隔が消えるのと同じである。

本稿で直接に閉じる spine は Route D のうち recurrence と seed-free asymptotic corollary までである。Route A はその離散証人であり、Route C は容量としての系であり、Route B は得られた $\varphi$ を Kalon として読む。順序を誤ってはならない。先に証明を閉じ、その後に意味を読む。

automath は格子上にとどまる。だから $\varphi$ を見る。忘却論は早く連続極限へ進みすぎた。だから $\varphi$ を見落とした。両者の橋渡しが、その欠落を回復する。

射影は合成を壊す。壊れ方が曲率を生む。壊れ方の文法が成長する率は黄金比である。各記憶行為は、ちょうど一つの影を落とすからである。同じ公理を二度は使えないからである。

忘却なしに力はない。力なしに構造はない。構造なしには、何も起こらない。

情報が完全保存される世界では、何も起こらない。忘却に最小量子がある世界では、起こることの文法は黄金比で成長する。

---

## 参考文献

- [1] Makaron (2026a). 力としての忘却 — 統計多様体上の場の方程式. Paper I, v1.5. 忘却論シリーズ.
- [2] The Omega Institute (2026). automath — An auditable theory compiler. GitHub: the-omega-institute/automath. Lean 4, 3,427+ theorems.
- [3] Amari, S. (2016). *Information Geometry and Its Applications*. Springer.
- [4] Makaron (2026b). 行為可能性は忘却である — Coherence Invariance 定理と G∘F 結晶化の普遍性. Paper VI. 忘却論シリーズ.
- [5] Makaron (2026c). 繰り込みは忘却である. Paper V. 忘却論シリーズ.
- [6] Makaron (2026d). 存在は忘却に先行する — 容器/内容の cell 次元論と CPS0' の米田的導出. Paper VIII. 忘却論シリーズ.
- [7] Wilson, K. G. (1974). Confinement of quarks. *Physical Review D*, 10(8), 2445–2459. https://doi.org/10.1103/PhysRevD.10.2445
- [8] Baez, J. C., & Stay, M. (2009). Physics, topology, logic and computation: A Rosetta Stone. arXiv:0903.0340. https://arxiv.org/abs/0903.0340
- [9] Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183–191. https://doi.org/10.1147/rd.53.0183
- [10] Bennett, C. H. (1973). Logical reversibility of computation. *IBM Journal of Research and Development*, 17(6), 525–532. https://doi.org/10.1147/rd.176.0525
- [11] Bérut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider, R., & Lutz, E. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*, 483, 187–189. https://doi.org/10.1038/nature10872
- [12] Gavrilov, M., & Bechhoefer, J. (2016). Erasure without work in an asymmetric double-well potential. *Physical Review Letters*, 117, 200601. https://doi.org/10.1103/PhysRevLett.117.200601
- [13] Dago, S., Pereda, J., Barros, N., Ciliberto, S., & Bellon, L. (2021). Information and thermodynamics: Fast and precise approach to Landauer's bound in an underdamped micro-mechanical oscillator. *Physical Review Letters*, 126, 170601. https://doi.org/10.1103/PhysRevLett.126.170601
- [14] Dago, S., & Bellon, L. (2022). Dynamics of information erasure and extension of Landauer's bound to fast processes. *Physical Review Letters*, 128, 070604. https://doi.org/10.1103/PhysRevLett.128.070604
- [15] Ciampini, M. A., Wenzl, T., Konopik, M., Thalhammer, G., Aspelmeyer, M., Lutz, E., & Kiesel, N. (2021). Experimental nonequilibrium memory erasure beyond Landauer's bound. arXiv:2107.04429. https://arxiv.org/abs/2107.04429
- [16] Toyabe, S., Sagawa, T., Ueda, M., Muneyuki, E., & Sano, M. (2010). Experimental demonstration of information-to-energy conversion and validation of the generalized Jarzynski equality. *Nature Physics*, 6, 988–992. https://doi.org/10.1038/nphys1821
- [17] Koski, J. V., Maisi, V. F., Pekola, J. P., & Averin, D. V. (2014). Experimental realization of a Szilard engine with a single electron. *Proceedings of the National Academy of Sciences*, 111(38), 13786–13789. https://doi.org/10.1073/pnas.1406966111
- [18] Koski, J. V., Maisi, V. F., Sagawa, T., & Pekola, J. P. (2014). Experimental observation of the role of mutual information in the nonequilibrium dynamics of a Maxwell demon. *Physical Review Letters*, 113, 030601. https://doi.org/10.1103/PhysRevLett.113.030601
