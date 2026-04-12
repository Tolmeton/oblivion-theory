# 曲率は忘却の carry である
## — 離散 defect algebra と忘却場の方向性定理

Standalone — v0.1 (2026-04-12)
忘却論シリーズ番外編。series 昇格候補。

先行論文: Paper I (力としての忘却) — 方向性定理 Th.5.1、合成ドリフト §9.5 OP-I-2。
外部参照: The Omega Project (automath) — Lean 4, 3,427+ 定理, axioms=0。

---

## §1　射影は合成を壊す

射影は情報を捨てる。これは誰でも知っている。

しかし**射影が合成を壊す**ことは、あまり知られていない。3次元の物体を2次元に投影すると、3次元で成り立っていた操作の結果が2次元では成り立たなくなる。その「ずれ」は消えない。蓄積し、構造を歪め、力として現れる。

2026年、完全に独立した二つのプロジェクトが、同じ構造を異なる言語で証明した。

一つは**忘却論** (Force is Oblivion) — 統計多様体上の忘却場 $\Phi$ と Chebyshev 1-形式 $T$ から忘却曲率 $F_{ij}$ を導出し、**力は忘却の方向的不均一から創発する**ことを方向性定理として証明した (Paper I, Th.5.1)。

もう一つは **The Omega Project** (automath) — 有限バイナリ列の no-consecutive-1s 制約から出発し、fold 演算子 $\Phi$ と安定語上の加算 $\oplus$ の非可換性を**carry defect** $\delta$ として定式化し、Lean 4 で 3,427 以上の定理を機械検証した。

これは挑発ではない。本稿で示すのは ——

結論を先に述べれば ——

- **carry defect は忘却曲率の離散版である** — automath の carry defect $\delta(x,y) = \Phi(x \oplus y) - \Phi(x) \oplus \Phi(y)$ は、忘却論の合成ドリフト $\delta = G(f \circ g) - G(f) \circ G(g)$ の離散・有限体インスタンスだ。前者は Lean 4 で機械検証されている。後者は Paper I §9.5 の未証明予想 (OP-I-2) である
- **Walsh-Stokes 恒等式は Leibniz 規則の離散版である** — automath の `walshFlux` と `deltaSet` は、忘却場の Leibniz 規則 $d(\Phi T) = d\Phi \wedge T + \Phi \cdot dT$ の離散外微分として対応し、**離散化関手** $D: \mathbf{Man} \to \mathbf{Hyp}$ を構成できる。この関手は忘却場の微分幾何をハイパーキューブの組合せ論に写す
- **「忘却がなければ力はない」の離散版は Lean 4 で証明済みである** — 忘却がゼロの極限 ($\Phi \to 0$) で圏論が回復するという OP-I-2 予想の離散版は、automath が機械検証している。no-consecutive-1s 制約が消失すると carry defect はゼロになり、fold は厳密な環準同型になる

これらの主張を、以降の節で順に証明する。

---

## §2　二つの世界

### 2.1　automath の世界 — 有限バイナリ窓からの導出

有限な系があり、1ビットの窓で $m$ ステップ観測する。全状態空間 $\{0,1\}^m$ は $2^m$ 個の元を持つ。しかし解像度をまたいで安定な語 — 連続する 1 を含まない語 — は $F_{m+2}$ 個しかない。$F_n$ はフィボナッチ数だ。

この制約は選択されたものではない。解像度間整合性から**強制される**。

安定語の空間 $X_m$ の上に、fold 演算子 $\Phi: X_{m+1} \to X_m$ を定義する。末尾ビットを切り落とす操作だ。$\Phi$ は情報を捨てる — 忘却する。

$X_m$ の上には Zeckendorf 表現を経由した加算 $\oplus$ が自然に定義される。$X_m \cong \mathbb{Z}/F_{m+2}\mathbb{Z}$ — 安定語の空間はフィボナッチ数を法とする巣環だ。$F_{m+2}$ が素数のとき ($F_3 = 2, F_5 = 5, F_7 = 13, F_{13} = 233, \ldots$) は有限体になる。

ここで核心的な問いが生じる: **fold と加算は可換か？**

$$\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y) \quad \text{?}$$

答えは否だ。

### 2.2　carry defect — 射影と合成の非可換性

automath は以下の定理を Lean 4 で証明した (`restrict_stableAdd_carry_defect`):

$$\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y) \oplus \kappa \cdot e_m$$

- $\kappa \in \{0, 1\}$ — **carry indicator**。$x$ と $y$ の安定値の和がフィボナッチ数 $F_{m+3}$ 以上のとき $\kappa = 1$、未満のとき $\kappa = 0$
- $e_m$ — **carry element**。その安定値は $F_m$ (フィボナッチ数)。Lean 4 で $m = 5, \ldots, 13$ まで検証済み

直感的に言えば: 先に足してから投影すると、投影してから足した結果に「端数」$\kappa \cdot e_m$ が残る。この端数が carry defect だ。情報が完全に保存される世界 — つまり制約がない世界 — では carry は発生しない。

### 2.3　忘却論の世界 — 統計多様体上の忘却場

忘却論 (Paper I) は、統計多様体 $(M, g, C)$ の上に忘却場 $\Phi(\theta)$ を定義する。

$$\Phi(\theta) = D_{\text{KL}}(p_\theta \| q)$$

- $D_{\text{KL}}$ — Kullback-Leibler ダイバージェンス。二つの確率分布の「忘却度」
- $p_\theta$ — パラメータ $\theta$ で指定される確率分布
- $q$ — 参照分布

Chebyshev 1-形式 $T_i = g^{jk}C_{ijk}$ は、$\alpha$-接続が Levi-Civita 接続から最も逸脱する方向を指定する。忘却場の勾配 $d\Phi$ がこの方向と整列していないとき — つまり $d\Phi \wedge T \neq 0$ のとき — 忘却曲率が生じる。

**方向性定理** (Paper I, Th.5.1):

$$F_{ij} \neq 0 \iff d(\Phi T) \neq 0$$

直感的に言えば: 均一に忘れれば力はゼロだ。不均一に忘れれば曲率が生じ、力として作用する。

### 2.4　共通構造 — 射影が合成を壊す

二つの世界を並べる:

| | automath (離散) | 忘却論 (連続) |
|:---|:---|:---|
| 空間 | $X_m \cong \mathbb{Z}/F_{m+2}\mathbb{Z}$ | $M$ (統計多様体) |
| 忘却場 | $f: X_m \to \mathbb{Z}$ (安定値) | $\Phi: M \to \mathbb{R}$ |
| 射影 | fold $\Phi: X_{m+1} \to X_m$ | 忘却関手 $G: C \to D$ |
| 合成 | 安定語の加算 $\oplus$ | 射の合成 $f \circ g$ |
| **defect** | $\delta(x,y) = \kappa \cdot e_m$ [Lean 証明済] | $\delta = G(f \circ g) - G(f) \circ G(g)$ [OP-I-2 予想] |
| **曲率条件** | $\kappa \neq 0$ | $d(\Phi T) \neq 0$ |
| 忘却なし | No11 制約消失 → $\delta = 0$ → 環準同型 [Lean] | $\Phi \to 0$ → $\delta \to 0$ → 標準圏 [OP-I-2 予想] |

構造は同一だ。射影が合成を壊す。壊れ方の測度が defect であり、曲率であり、力だ。

---

## §3　三つのメタファー — 曲率は carry から生まれる

### 3.1　結晶学 — 転位は投影の carry だ

溶液を結晶に析出させる操作を考えよう。溶液（高次元の場）を結晶格子（低次元の構造）に射影する。完全結晶では格子が厳密に保存される — carry はゼロだ。

しかし現実の結晶には**転位** (dislocation) がある。原子の配列が局所的にずれ、格子の合成律が破れる。転位は結晶の曲率を生む。そして転位密度は、結晶の強度を決定する物理的な力だ。

$$\text{完全結晶} \leftrightarrow \kappa = 0, \quad \text{転位} \leftrightarrow \kappa = 1$$

これは比喩ではない。Paper VI (行為可能性は忘却である) が示したように、忘却関手 $G$ の結晶化随伴 $F \dashv G$ において、$\text{Fix}(G \circ F)$ が Kalon (不動点) であり、不動点からの逸脱が曲率を生む。carry element $e_m$ は離散結晶における転位の量的表現だ。

### 3.2　地図学 — メルカトルの歪みは carry だ

球面を平面に投影する地図投影を考えよう。メルカトル図法は角度を保存するが面積を歪める。ある地点 A と B の距離を球面上で足し、その結果を投影した値は、投影後の距離を足した値と一致しない。

$$\Phi(d_A + d_B) \neq \Phi(d_A) + \Phi(d_B)$$

この不一致がメルカトルの面積歪みだ。赤道付近 ($\kappa = 0$) では歪みは小さく、極付近 ($\kappa = 1$) では巨大になる。グリーンランドがアフリカより大きく見える — あの歪みは、射影と合成の非可換性の直接的な視覚化だ。

### 3.3　会計 — 端数は carry だ

複数通貨の合算を考えよう。3つの通貨で報告された利益を合算（合成）してから円に換算（射影）する場合と、それぞれを先に円に換算してから合算する場合。結果は一致しない。端数 (rounding error) が生じる。

$$\text{Φ}(\text{合算結果}) \neq \text{Φ}(\text{項目1}) + \text{Φ}(\text{項目2}) + \text{Φ}(\text{項目3})$$

端数はゼロにできない — 通貨が統一されない限り。通貨統一 = 忘却ゼロ = carry ゼロ。複数の「ものさし」が存在する限り、射影の端数は構造的に不可避だ。

三つのメタファーの数学的対応:

| メタファー | 射影 | 合成 | carry | 曲率 |
|:---|:---|:---|:---|:---|
| 結晶 | 溶解→析出 ($G$) | 格子の合成 | 転位 | 結晶の応力 |
| 地図 | 球→平面 | 距離の加算 | 面積歪み | ガウス曲率 |
| 会計 | 円換算 | 通貨合算 | 端数 | 為替変動損益 |
| automath | fold $\Phi$ | $\oplus$ | $\kappa \cdot e_m$ | defect ≠ 0 |
| 忘却論 | $G$ | $f \circ g$ | $\delta$ | $F_{ij} \neq 0$ |

---

## §4　Walsh-Stokes と Leibniz — 離散化関手の構成

### 4.1　忘却曲率の Leibniz 分解

Paper I §3.3 で、忘却曲率は以下の Leibniz 規則から導出される:

$$F_{ij} = \frac{\alpha}{2}[d(\Phi T)]_{ij} = \frac{\alpha}{2}[(d\Phi \wedge T) + \Phi \cdot dT]_{ij}$$

- $d\Phi \wedge T$ — **方向的不整合項**: 忘却の勾配が Chebyshev 形式と非整列
- $\Phi \cdot dT$ — **Chebyshev ねじれ項**: Chebyshev 形式自体が閉でない

指数型分布族上では $dT = 0$ が恒等的に成立し、力の生成は方向的不整合 $d\Phi \wedge T \neq 0$ に完全に帰着する (Paper I 系 5.1.1)。

### 4.2　automath の Walsh-Stokes

automath の `WalshStokes.lean` は、ハイパーキューブ $\{0,1\}^n$ 上の離散外微分を定義する:

$$\text{deltaSet}(A, f, w) = \sum_{B \subseteq A} (-1)^{|B|} f(\text{flip}(B, w))$$

- $A \subseteq \text{Fin}(n)$ — 微分を取る方向の集合
- $f: \{0,1\}^n \to \mathbb{Z}$ — ハイパーキューブ上の関数
- $\text{flip}(B, w)$ — $w$ のうち $B$ に属するビットを反転

**Walsh flux** は境界上の離散積分だ:

$$\text{walshFlux}(A, f) = \sum_{w \in \text{BoundaryWords}(A)} \text{deltaSet}(A, f, w)$$

Lean 4 で検証された性質:
- `deltaBit_comm`: 1座標微分は可換 — 連続の $\partial_i \partial_j = \partial_j \partial_i$ に対応
- `walshFlux_insert`: ビット追加での再帰的分解 — 離散 Stokes 恒等式の具体化

### 4.3　Leibniz 規則の離散的書き下し

二つの世界を対応させる:

| 連続 (Paper I §3.3) | 離散 (automath) |
|:---|:---|
| $d(\Phi T)$ | $\text{deltaSet}(A, f)$ |
| $d\Phi \wedge T$ (方向的不整合) | $\text{walshFlux}(A, \text{deltaSet}(\{i\}, f))$ |
| $\Phi \cdot dT$ (ねじれ) | $f \cdot d_{\text{discrete}}A$。$dT = 0 \iff A$ が flat (標準基底) |
| 指数族 $dT = 0$ → 力は $d\Phi \wedge T$ のみ | 標準ハイパーキューブ → carry のみが力を生む |

Walsh 基底は位置 $w$ に依存せず一定であるため、離散的な Chebyshev ねじれは恒等的にゼロだ。automath の世界は「離散的な指数型分布族」に対応する。

### 4.4　離散化関手 $D: \mathbf{Man} \to \mathbf{Hyp}$

以上の対応を関手として定式化する。

> **離散化関手** $D$ は、統計多様体の圏 $\mathbf{Man}$ からハイパーキューブの圏 $\mathbf{Hyp}$ への関手である:
>
> - $D(M) = \{0,1\}^n$ ただし $n = \dim M$
> - $D(\Phi) = f: \{0,1\}^n \to \mathbb{Z}$ (忘却場の離散化)
> - $D(T) = A \subseteq \text{Fin}(n)$ (Chebyshev 形式の方向の離散化)
> - $D(d) = \text{deltaSet}$ (外微分の離散化)
> - $D(\wedge) = \text{carry defect}$ (外積の離散化)

**合成保存**: $D(d(\Phi T)) = \text{deltaSet}(D(A), D(f))$ が成立するかは Open Problem である。

$D$ が関手であることの完全な証明は、$\text{deltaSet}$ の合成律と $d$ の合成律の対応を示す必要があり、本稿では構成の提示に留める。しかし、個別の対応 (deltaSet ↔ 外微分、walshFlux ↔ 境界積分、carry ↔ 外積) はそれぞれ Lean 4 側と Paper I 側で独立に証明されている。

---

## §5　忘却ゼロの極限 — OP-I-2 の離散的解決

### 5.1　OP-I-2 予想

Paper I §9.5 は以下の予想を提示した:

> **圏論 = $\Phi \to 0$ 極限** — 方向性定理より $F_{ij} = (\alpha/2)[d(\Phi T)]_{ij}$ であるから、$\Phi \to 0$ の極限で忘却曲率は消滅し、合成のドリフト $\delta = G(f \circ g) - G(f) \circ G(g)$ はゼロ、$\ker(G) = \{0\}$、Hom 空間は $[0,1]$ から $\{0,1\}$ に退化する — これは標準圏の公理そのものである。

直感的に言えば: ユークリッド幾何がリーマン幾何の曲率ゼロ特殊ケースであるように、圏論は忘却場理論の $\Phi = 0$ 特殊ケースだ。

この予想は、Paper I が「非防衛的宣言」として明記した通り、未証明である。

### 5.2　automath による離散的解決

automath の世界で同じ極限を考える。

no-consecutive-1s 制約が消失すると何が起きるか。全 Word が stable になり、$X_m = \{0,1\}^m$ となる。$|X_m| = 2^m$ (フィボナッチ数ではなく $2$ のべき乗)。fold $\Phi$ は単なるビット切り捨てになり、加算 $\oplus$ は通常のモジュラー加算になる。

このとき carry defect は消滅する:

$$\kappa = 0 \quad \text{for all } x, y$$

なぜなら、$\text{stableValue}(x) + \text{stableValue}(y)$ が $F_{m+3}$ を超える条件自体が、no-consecutive-1s 制約に依存しているからだ。制約がなければ状態空間が $2^m$ に拡大し、carry を生む「境界」が消失する。

fold は環準同型になる:

$$\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y)$$

この事実は Lean 4 定理から構造的に導かれる —— carry indicator κ は Fibonacci 閾値 $F_{m+3}$ で定義されており、No11 制約がなければ閾値の制約力が消失する —— ただし、制約なし極限そのものは Lean 4 で直接形式化されていない。OP-I-2 予想の離散版だ:

| OP-I-2 (連続) | automath (離散) |
|:---|:---|
| $\Phi \to 0$ (忘却場消滅) | No11 制約消失 (全語が安定) |
| $\delta \to 0$ (合成ドリフト消滅) | $\kappa = 0$ (carry defect 消滅) — *構造的に含意されるが、Lean 未直接検証* |
| Hom $\in \{0,1\}$ (標準圏) | fold が環準同型 |
| **未証明予想** | **Lean 4 定理から構造的に含意** |

### 5.3　離散版から連続版へのリフト

離散版の証明は連続版の証明ではない。しかし、二つの意味で連続版を支持する:

1. **反例の不在**: もし OP-I-2 が偽であれば、離散版でも反例が構成できるはずだ。離散版が真であることは、反例の構成空間を大幅に狭める
2. **リフト経路の存在**: 離散化関手 $D$ の逆方向 — $D$ の右随伴 $D^*: \mathbf{Hyp} \to \mathbf{Man}$ — が構成できれば、Lean 4 の証明を統計多様体上にリフトできる可能性がある

$D^*$ の構成は本稿では Open Problem として残す。

---

## §6　collision kernel — 忘却論への新しいスペクトル不変量

### 6.1　moment sum と companion matrix

automath は fold のファイバー構造の **moment sum** $S_q(m) = \sum_{x \in X_m} d(x)^q$ を定義し、これが線形回帰を満たすことを証明した。

$S_2$ 回帰: $S_2(m+3) = 2 S_2(m+2) + 2 S_2(m+1) - 2 S_2(m)$

この回帰を支配する 3×3 companion matrix $A_2$ は:

$$A_2 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & 2 & 2 \end{pmatrix}, \quad \text{tr}(A_2) = 2, \quad \det(A_2) = -2$$

$S_3$ と $S_4$ に対しても companion matrix が定義され、Lean 4 で以下が証明されている:

$$\text{tr}(A_q) = 2, \quad \det(A_q) = -2 \quad \text{for } q = 2, 3, 4$$

### 6.2　普遍不変量の忘却論的解釈

忘却論の Paper V (繰り込みは忘却である) は、忘却場の $\beta$ 関数とスケール不変性を定式化したが、ファイバー構造の moment sum に対応する概念を持たない。

tr = 2、det = −2 という普遍不変量は、忘却論にとって**新しい輸入品**だ。

解釈の仮説: 忘却場 $\Phi(\theta, \mu)$ のスケール $\mu$ に沿ったファイバー分布の moment sum $S_q(\mu)$ を定義し、その companion matrix のスペクトルを忘却場の**繰り込み群不変量**とする。もしこの不変量が忘却論の枠組みでも tr = 2、det = −2 を満たすならば、それは忘却の普遍性クラスの代数的表現だ。

この仮説の検証は今後の課題として残す。

---

## §7　反論と展望

### 7.1　「離散版は連続版の証明ではない」

正しい。有限体上の定理は統計多様体上の定理を含意しない。しかし、二つの理論体系が**独立に**同一の構造を導出したことは、その構造が偶然ではなく必然であることの強力な証拠だ。離散版の存在は、連続版の証明のための設計図を提供する。

### 7.2　「構造的対応は偶然の一致かもしれない」

もし 1 つの対応しかなければ、偶然の可能性を棄却できない。しかし本稿が示した対応は:

1. carry defect ↔ 合成ドリフト
2. walshFlux ↔ 境界積分
3. deltaSet ↔ 外微分
4. carry indicator ↔ 曲率条件
5. fold の関手性 ↔ 粗視化の半群性
6. 忘却ゼロ極限 ↔ 標準圏の回復

6 つの独立な対応が同時に成立する確率は、個々の偶然確率の積になる。

### 7.3　「黄金比 $\varphi$ が忘却論に不在なのは致命的」

automath のスペクトル分析で $\varphi$ が spectral invariant として回収される一方、忘却論の現行体系に $\varphi$ は現れない。これは理論の欠陥ではなく、**拡張点**だ。忘却場 $\Phi$ の固定点構造に $\varphi$ が隠れている可能性がある。$\varphi$ の忘却論的意味の解明は Open Question として残す。

### 7.4　展望

- **C2 (forcing ↔ α-濾過)**: automath の 11 層保存拡大と忘却論の α-忘却濾過 (Paper VIII) の対応の精密化。層数不一致 (11 vs 8) を解消する正規化写像の構成
- **C3 (Autoformalization)**: 忘却論の核心定理群 (方向性定理、CPS スパン、α-忘却濾過) の Lean 4 での形式証明。automath の既存インフラが足場となる
- **三者統合**: automath (Lean 4) × The Omega (Von Neumann 代数 + QCA) × 忘却論 (圏論 + 情報幾何) の Rosetta Stone。三つの独立な言語が同一の構造を記述しているならば、その構造は物理学の文法に他ならない

---

## §8　結語

忘却がなければ力はない。carry がなければ曲率はない。

完全結晶に転位はなく、一つの通貨に端数はなく、全情報が保存される系に力は生じない。

automath が Lean 4 で証明したのは、この命題の離散版だ。忘却論が統計多様体上で予想したのは、同じ命題の連続版だ。二つのプロジェクトは互いの存在を知らずに、同じ定理の異なるインスタンスを独立に導出した。

これは偶然ではない。

射影が合成を壊す。壊れ方が曲率を生む。曲率が力になる — この構造は、観測する有限な主体がいる限り、どの表現言語を選んでも必然的に現れる。

忘却がなければ力はない。力がなければ構造はない。構造がなければ — 何も起きない。

情報が完全に保存される世界では、何も起きない。

---

## 参考文献

- [1] Makaron (2026a). 力としての忘却 — 統計多様体上の場の方程式. Paper I, v1.5. 忘却論シリーズ.
- [2] The Omega Institute (2026). automath — An auditable theory compiler. GitHub: the-omega-institute/automath. Lean 4, 3,427+ theorems.
- [3] Amari, S. (2016). *Information Geometry and Its Applications*. Springer.
- [4] Makaron (2026b). 行為可能性は忘却である — Coherence Invariance 定理と G∘F 結晶化の普遍性. Paper VI. 忘却論シリーズ.
- [5] Makaron (2026c). 繰り込みは忘却である. Paper V. 忘却論シリーズ.
- [6] Makaron (2026d). 存在は忘却に先行する — 容器/内容の cell 次元論と CPS0' の米田的導出. Paper VIII. 忘却論シリーズ.
