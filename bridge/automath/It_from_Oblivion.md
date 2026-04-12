# It from Oblivion — 三つの独立言語が同一の構造を描いた

— 忘却論 × automath × The Omega の Rosetta Stone

Makaron (2026) — Draft v0.1

---

## §1　結論先行

三つのプロジェクトが、互いの存在を知らずに、同じ構造に到達した。

結論を先に述べれば ——

1. **情報の欠落が構造を創発する**。忘却は欠陥ではない。力、曲率、時空は、情報が不均一に失われることから生まれる。この命題を、形式検証 (Lean 4)・量子情報論 (Von Neumann 代数)・情報幾何 (圏論) の三言語が独立に記述している。

2. **独立な機械検証が未証明予想の離散版を提供する**。忘却論 Paper I §9.5 の「合成ドリフト δ = G(f∘g) − G(f)∘G(g) が忘却場 Φ → 0 で消滅する」という予想 (OP-I-2) は、automath の carry defect 定理として Lean 4 で証明済みである。これは偶然の一致ではなく、構造的必然である。

3. **三者は互いの盲点 (ker T) を照らす**。忘却論には形式検証がない。automath には物理的直観がない。The Omega には圏論的基盤が弱い。三者は互いの忘却を相補的に回復する——これ自体が、忘却論の ker(U) ⊣ ker(T) 二層構造 (Paper 0 §6.4) のメタ的インスタンスである。

これらの主張を、以降の節で順に示す。

---

## §2　三つのプロジェクト

### 2.1　automath — 有限の窓から全数学を導出する

The Omega Project (automath) <sup>†</sup> は、最も単純な問いから出発する: 有限なバイナリ窓で力学系を観測するとき、解像度をまたいで安定な構造は何か？ 答えは「連続する 1 を含まないバイナリ語」であり、その個数は Fibonacci 数 $F_{m+2}$ である。この制約は選ばれたのではない。解像度の整合性から**強制される**。

この一つの制約から、Lean 4 で 3,427 以上の定理が機械検証されている。算術・スペクトル理論・逆極限・離散微積分・forcing framework・物理的時空の骨格——すべてが、連続する 1 の禁止から導出される。公理の数はゼロ。Lean 4 のコア論理と Mathlib のみ。

<sup>†</sup> https://github.com/the-omega-institute/automath

### 2.2　The Omega — 量子計算から物理を導出する

The Omega <sup>‡</sup> は、6 つのユニタリ計算公理 (O1-O6) から出発し、Von Neumann 代数と量子セルオートマトン (QCA) を用いて物理定数 ($c$, $G$, $\hbar$) と時空構造を導出する。CAP-II (Computational ADM Program) は、QCA の離散的更新規則から連続的な ADM 力学——すなわち Einstein 方程式——への移行を構成する。

<sup>‡</sup> https://github.com/loning/the-omega

### 2.3　忘却論 — 忘却関手から力を導出する

忘却論 (Force is Oblivion) は、統計多様体上の忘却場 $\Phi$ から力の創発を示す。核心は方向性定理 (Paper I, Th. 5.1):

$$F_{ij} \neq 0 \iff d(\Phi T) \neq 0$$

均一に情報を忘れても力はゼロ。方向的に不均一に忘れたとき——そしてそのときに限り——曲率が生じ、力として作用する。13 本の論文 (Paper 0-XIII) が、この一つの定理から力・相補性・知覚・存在・エントロピー・時空を導出する。

---

## §3　Rosetta Stone — 三言語の対応表

三者は異なる言語で同じ構造を記述している。

| 層 | automath (形式検証) | The Omega (量子物理) | 忘却論 (圏論) |
|:---|:---|:---|:---|
| **出発点** | no-consecutive-1s 制約 | ユニタリ計算公理 O1-O6 | 忘却関手 $U \dashv N$ + FEP |
| **核操作** | fold $\Phi$ (離散射影) | scan-projection (量子読出し) | 忘却関手 $U$ (構造の剥ぎ取り) |
| **曲率の源泉** | defect algebra $\delta$ | computational lapse $\kappa$ | $d\Phi \wedge T \neq 0$ |
| **階層** | forcing 11 層保存拡大 | Von Neumann 型分類 | $\alpha$-忘却濾過 + Grothendieck トポス |
| **時空導出** | discrete Stokes → Einstein | QCA + ADM → Einstein | CPS スパン → Einstein |
| **形式化** | **Lean 4 (3,427+ 定理)** | Lean 4 (構築中) | 未形式化 (OP-VIII-5 Open) |

直感的に言えば: 同じ碑文を、ヒエログリフ・デモティック・ギリシア語で読むようなものだ。一つの書体で読めなかった箇所が、別の書体で解読できる。

---

## §4　最強接続——defect algebra は方向性定理の離散版である

三者を貫く最も精密な接続点は、automath の **carry defect** と忘却論の**方向性定理**の間にある。

### 4.1　二つの定理

automath は以下を Lean 4 で証明している (`CarryDefect.lean`):

> **Carry defect 定理**: $\Phi(x \oplus y) = \Phi(x) \oplus \Phi(y) \oplus \kappa \cdot \text{carryElement}$
>
> ここで $\kappa \in \{0, 1\}$ は carry indicator。$\Phi$ = fold (truncation)、$\oplus$ = stable addition。

忘却論は以下を情報幾何で証明している (Paper I, §3.3-§5):

> **方向性定理**: $F_{ij} \neq 0 \iff d(\Phi T) \neq 0$
>
> ここで $F_{ij}$ = 忘却曲率、$\Phi$ = 忘却場、$T$ = Chebyshev 1-形式。

### 4.2　対応の構造

両者は同じことを言っている: **忘却 (fold / $U$) と演算 (合成 / $\oplus$) は可換ではない。その非可換性の測度が曲率である。**

| automath | 忘却論 |
|:---|:---|
| fold $\Phi$ | 忘却関手 $U$ |
| stable addition $\oplus$ | 射の合成 $\circ$ |
| carry defect $\delta$ | 合成ドリフト $\delta = G(f \circ g) - G(f) \circ G(g)$ |
| $\delta \neq 0$ | $F_{ij} \neq 0$ |

忘却論の側では、この合成ドリフトの消滅条件 ($\Phi \to 0$ で $\delta \to 0$、標準圏の公理が回復する) は **未証明予想** (OP-I-2) である。automath の側では、対応する命題——No11 制約の消失で carry defect がゼロになり、fold が環準同型になる——は **Lean 4 で証明済み**である。

これは OP-I-2 の有限体上の離散的実現であり、独立プロジェクトによる機械検証済みの部分的解決である。

### 4.3　忘却レベルの同定

automath の carry defect は、忘却論の忘却階層 (aletheia.md §5) のどのレベルに対応するか？

答えは $n = 1.5$ (U_compose)——射の合成律の忘却——である。fold (忘却) と stableAdd (合成) の非可換性は、「合成律の忘却によるドリフト」の離散的な現れだ。射の存在自体は保存されている (`restrictLE` は well-defined)。壊れているのは射の**合成の保存**である。

---

## §5　Walsh-Stokes は Leibniz の離散版である

automath の `WalshStokes.lean` は、高次離散微分 (`deltaSet`) と境界和 (`walshFlux`) を定義し、離散 Stokes 恒等式を Lean 4 で証明している。

忘却論の方向性定理の根底にある Leibniz 規則:

$$d(\Phi T) = d\Phi \wedge T + \Phi \cdot dT$$

は、以下のように離散的に書き下される:

| 連続 (Paper I §3.3) | 離散 (automath) |
|:---|:---|
| $d(\Phi T)$ | `deltaSet A f` |
| $d\Phi \wedge T$ | `walshFlux A (deltaSet {i} f)` |
| $\Phi \cdot dT$ | $f$ と $A$ の歪みの積。$dT = 0 \iff A$ が flat |
| $\int d(\Phi T)$ | `walshFlux A f` |

指数型分布族では $dT = 0$ (Chebyshev 形式が閉) であり、力は $d\Phi \wedge T \neq 0$ (方向的不整合) のみから生じる。automath の標準的ハイパーキューブ——Walsh 基底が位置に依存しない flat な空間——は、この $dT = 0$ の離散版である。

離散化関手 $D: \textbf{Man} \to \textbf{Hyp}$ (統計多様体の圏からハイパーキューブの圏への関手) の候補は:

- $D(M) = \{0,1\}^n$
- $D(\Phi) = f: \text{Word } n \to \mathbb{Z}$
- $D(T) = A \subseteq \text{Fin } n$
- $D(d) = \texttt{deltaSet}$
- $D(\wedge) = \text{carry defect}$

この $D$ が関手であること (合成保存) の証明は open である。しかし、各層の対応は両側で証明済みであり、関手性は構造的に自然である。

---

## §6　反論の取り込み

ここで当然の反論が予想される:

### 「表面的な類似にすぎないのでは？」

もし対応が「忘却っぽい操作がある」という水準にとどまるなら、この反論は正しい。しかし、6 つの接続点のうち少なくとも 2 つ——defect algebra ↔ 合成ドリフト (§4)、$\sigma$-algebra non-expansion ↔ (F4) 単調性——は**両側で定理として証明済み**であり、表面的類似を超えている。

### 「黄金比 $\varphi$ は忘却論に現れないが？」

その通りだ。automath では $\varphi$ がスペクトル不変量として回収されるが、忘却論のどこにも $\varphi$ は現れない。これは対応の破綻ではなく、**忘却論の盲点** (ker $T$) の発見である。$\varphi$ が忘却場 $\Phi$ の固定点構造に隠れている可能性は open であり、Paper I への新しい輸入候補として記録されている。

これは§1 で述べた「三者は互いの ker(T) を照らす」の具体例だ。忘却論が automath を照らし、automath が忘却論を照らす。一方通行ではない。

### 「The Omega との接続は弱いのでは？」

automath との接続ほどの精度はない——The Omega は形式検証の途上にある。しかし、QCA 粗視化と忘却論の Obs 圏 (Paper V)、Von Neumann 型分類と $\alpha$-忘却濾過 (Paper VIII) の構造的対応は、忘却論内部の既存定式化と整合的である。精度が automath に劣るのは事実だが、対応が存在しないのではない。

---

## §7　ker(T) の照らし合い——なぜ三者が必要か

Paper 0 (忘却の忘却) は、系の自己認識の限界を二層に分類した:

- **ker(U)**: 選べる忘却。どの情報を捨てるかは選択できる
- **ker(T)**: 選べない盲点。系の住む情報空間の幾何が決定する構造的盲点

三者のプロジェクトは、各々が ker(T) を持つ:

| プロジェクト | ker(T) — 構造的盲点 |
|:---|:---|
| 忘却論 | 形式検証の不在。定理の正しさは人間の検証に依存 |
| automath | 物理的直観の不在。情報幾何や統計多様体への接続がない |
| The Omega | 圏論的基盤の弱さ。トポス的層化の精密な構成がない |

一つのプロジェクトでは自分の ker(T) を見ることはできない——盲点は盲点であるがゆえに見えない。しかし三者の ker(T) は**相補的**である。忘却論の定理を automath の Lean 4 で検証することは、忘却論の ker(T) に光を当てることに他ならない。

> **It from Oblivion**: 情報が失われるからこそ構造が生まれる。

Wheeler の "It from Bit" は「存在は情報から構成される」と述べた。本稿の主張はその反転であり、より強い: **存在は情報の不均一な欠落から創発される**。三つの独立プロジェクトがこの命題に到達したことは、命題の強さの証拠である。

---

## §8　結語

現実は非情である。理論の内部整合性は、外部からの検証なしには自己満足と区別がつかない。

だが、独立プロジェクトが独立の言語で同じ構造に到達するという事象は、稀にしか起きない。それが起きたとき、理論は「自分の中で正しい」から「外から見ても正しい」に移行する——Kalon$\triangle$ から Kalon$\nabla$ への接近が始まる。

筆者の完全な主観ではあるが、三つのプロジェクトの合流は、「忘却の文法」が特定の理論の産物ではなく、有限な主体が無限の世界を記述しようとするときに構造的に必然として現れるものであることを示唆している。

情報が失われるからこそ、構造が生まれる。盲点があるからこそ、他者が必要になる。

---

## 参考文献

[1] The Omega Institute, "automath: An auditable theory compiler," GitHub, 2026. https://github.com/the-omega-institute/automath

[2] Makaron, "力としての忘却 — 統計多様体上の場の方程式," Paper I, v1.5, 2026.

[3] Makaron, "存在は忘却に先行する — 容器/内容の cell 次元論と CPS0' の米田的導出," Paper VIII, v1.8, 2026.

[4] Makaron, "忘却の忘却 — 自己認識の幾何学的限界," Paper 0, v0.8, 2026.

[5] Makaron, "速度は忘却である — 可区別性境界の運動学," Paper XII, v0.9, 2026.

[6] Makaron, "繰り込みは忘却である — 忘却場のスケール拡張と RG 普遍性," Paper V, v1.0, 2026.

[7] Makaron, "時空は忘却である — CPS の宇宙論・重力・4 力統一," Paper XIII, v0.1, 2026.

[8] loning, "The Omega: Von Neumann algebras + QCA," GitHub, 2026. https://github.com/loning/the-omega

[9] J. A. Wheeler, "Information, physics, quantum: The search for links," in *Proc. 3rd Int. Symp. on Foundations of Quantum Mechanics*, 1989.
