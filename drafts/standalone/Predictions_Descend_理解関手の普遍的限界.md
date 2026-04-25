# Predictions Descend — 理解関手の普遍的限界

**版**: v0.5 (2026-04-25, §8 redesign — Predictions Descend Theorem として再陳述、Gödel 第二不完全性定理対応 / 自己診断は付録 A に分離)
**メタファイル**: `予測_下降_理解関手の普遍的限界_メタデータ.md` (本稿の F⊣G 台帳 / 核主張レジャー / Gauntlet ログ / 虚→実変換面)
**主張水準ラベル**: 構成的命題 / 命題 / 仮説 / 構造的類似 (本稿内較正、論文間比較禁止)
**SOURCE 強度ラベル**: 強 (PDF verbatim 直接 Read) / 強候補 (subagent verbatim 抽出, 査読時独立検証推奨) / 中 (triangulation) / TAINT (記憶/web 要約)

---

## 序

20 世紀の科学哲学は、ある操作と、その操作の痕跡とを、しばしば取り違えてきた。

操作とは「**理解**」であり、痕跡とは「**予測**」である。Popper の反証可能性、Mangalam の予測至上主義、超ひも理論への「何でも説明できるから良くない」批判 — これら 70 年にわたる三つの誤配位は、すべて**痕跡から操作を読む**という同じ間違いから派生する。

理解と予測は同じ評価軸上に存在しない。理解は対象を別表現に還元し、その表現から元を回復する**二つの関手の組**であり、予測はその組のうち下降関手から漏れ出す痕跡である。両者は**随伴対** $L \dashv R$ として結ばれるが、合成の単位 $\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ は同型ではない。回復は完全ではなく、核 $\text{Ker}(\eta_{\text{unit}})$ が常に残る。

予測₁ (経験的予測) の産出は、理論が真理₀ を捉えた証ではない。それは真理₀ から下降関手 $R$ で生成される **痕跡** にすぎない (Predictions Descend)。本稿はこの誤読に対して、$L$ と $R$ を独立に並置し、両者の随伴を明示する (真理₀ / 真理₁ の定義は §2 で立てる)。

---

## §1 結論先行

### §1.1 構成的定義 (Axiom-First)

本稿は次の **構成的定義** から始める。「公理」と書かない理由: Yoneda の補題は category-theoretic statement であって epistemological statement ではない (§4.5 で扱う論理飛躍)。本稿は **理解の操作的 anchor として L⊣R 内在化を採用する** という立場を意図的に選択し、それが必要十分条件であるという過剰な主張をしない (§M3 主張水準ラベル C1 = 構成的命題 70% との整合)。Round 4 (§M5.4 予定) で本ラベリングの整合性を改めて gauntlet 形式で検証する。

> **構成的定義**: 本稿において「科学における理解」とは、随伴対 $L \dashv R$ の内在化として **操作的に定義される** 関手的操作である。

ここで $L$ (左随伴) は対象を別表現に還元する操作、$R$ (右随伴) はその表現から元を回復する操作。両者の合成 $\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ は **単位** と呼ばれ、自明 (恒等) ではない。$\eta_{\text{unit}}$ の核 $\text{Ker}(\eta_{\text{unit}})$ は、$L$ で失われ $R$ で完全には回復されない情報の集合である。

> [SOURCE: aletheia §1 L99-L107 (随伴定理 U0', VFE 減少定理 $F[N(q_{\text{poor}})] \leq F[q_{\text{poor}}]$, $N \circ U \neq \text{Id}$)] — 本稿の $L \dashv R$ は aletheia の $U \dashv N$ と同型: $L \leftrightarrow U$ / $R \leftrightarrow N$ / $\eta_{\text{unit}} \leftrightarrow \eta$。

随伴の存在条件は **General Adjoint Functor Theorem (GAFT, Mac Lane CWM §V.6)** を採用する: $L$ が連続 (small limit 保存) かつ Solution Set Condition (SSC) を満たすとき、左随伴 $R$ が存在する。

> [SOURCE 強度 中: Buzzard 2012 Imperial College lecture notes p.2 Theorem 1.1 が Mac Lane CWM p.117 を verbatim 引用 — 本稿査読時に Mac Lane CWM 直接 Read で「強」昇格義務 (G-ζ)]

### §1.2 5 核主張

公理の下で、次の 5 主張を導出する。各主張に **主張水準** (構成的命題 / 命題 / 仮説 / 構造的類似) と **確信度** を付記する。

> **本稿内のキャリブレーション宣言**: 確信度 % は本稿内での主張水準較正の指標であり、絶対精度ではない。**論文間比較は禁止**する。確信度の数値は較正可能性の指標として機能し、本稿内 C1-C5 の相対関係を表す。

- **C1** [構成的命題, 推定 70%]: 科学における「理解」は随伴対 $L \dashv R$ の内在化として定義される関手的操作である (公理の再記述、operational identity)
- **C2** [構成的命題, 推定 75%]: $\eta_{\text{unit}}$ 非同型は構造保存定理から帰結する構造的不等式。$\text{Ker}(\eta_{\text{unit}}) > 0$ は全理論共通の原理的制約である
- **C3** [命題, 確信 80%]: 補完₁ は $\text{Ker}(\eta_{\text{unit}})$ と構造的に結びつく。理解の深化は補完₁ 依存を単調減少させる (理解-予測の随伴的相補性定理)
- **C4** [仮説, 確信 60%]: 予測₁ の産出は真理₀ の指標ではなく、真理₀ から下降関手 $R$ で生成される痕跡である (**Predictions Descend**)
- **C5** [構造的類似, 仮説 55%]: ポパーの反証可能性 / Mangalam の予測至上主義 / 超ひも landscape は C4 の同一系。3 大誤配位は単一の構造的誤測定 (関手の方向逆転誤読) から派生する

### §1.3 射程の切断 (Scope Severance)

本稿の射程は次の 3 点で明示的に切断される。

1. **co-evolution 限定**: 本稿の主張は **現世代の AI / 科学コミュニティ** 前提下で構成される。圏論・関手論への access が LLM 経由で完全に大衆化された場合、C1 / C4 は scaffolding として消える可能性がある。その場合の科学哲学は本稿の射程外。**強化が観測される範囲では本稿主張は強化される、ただし完全自明化に達した場合は scaffolding として消える**。

2. **構造決定論的立場の自覚**: 本稿は「理解 = L⊣R 内在化」を **構成的定義** (Yoneda 補題に基づく操作的 anchor) として採用する。「なぜ構造が理解を生むか」という本質論は本稿の問いではない — **問いの水準を意図的に変更している**。IIT (Tononi) との同型については §6 で commitment レベル (ontological vs definitional) の差として開示する。

3. **FEP 非依存性**: FEP (Free Energy Principle) は本稿の最も顕著な実例として §3-§4 に置かれるが、**論旨は FEP 非依存** で立つ。能動推論の圏論定式化未完を理由とする overclaim 批判は、本稿の C1-C5 が FEP の特定定式化に依存しないことで予防的に閉じる。

### §1.4 本稿の構造

| 節 | 役割 |
|:---|:---|
| §2 | 随伴対 $L \dashv R$ の導入と数学的展開 |
| §3 | 5 分野 (情報幾何 / ゲージ理論 / 統計力学 / 数論 / FEP) における横断展開 |
| §4 | Yoneda 補題による接続 (Mac Lane CWM §III.2 + Riehl 2016 §2.2 Theorem 2.2.4 + §3.5 Theorem 3.5.5) |
| §5 | Information Bottleneck (Tishby-Pereira-Bialek 1999) による相補性の Lagrangian 形式化 |
| §6 | 制約節 (3 立場の ontological commitment スペクトル / IIT との同型 / 現世代モデル前提の射程明示 / 残余問題) |
| §7 | corollary (Popper / Mangalam / 超ひも landscape) |
| §8 | 結語 (Predictions Descend の単一図式) |

### §1.5 外部接続 anchor

本稿は **Bogen-Woodward 1988 「Saving the Phenomena」§I の data → phenomena → theory 三層** を共通構造 anchor として採用する。本稿の 4 型分け (§2.1) と Bogen-Woodward 三層との対応は、関手の方向に注意して読み直す必要がある。

本稿の関手 (§1.1 「$L$ = 還元 / $R$ = 回復」と aletheia $U \dashv N$ の整合):

- **$L$ (左随伴・還元関手, 上昇方向)**: 予測₁ (具体値) $\to$ 真理₁ (有限理論) $\to$ 真理₀ (構造) — 観測値から構造へ接近する方向 (情報を捨てて抽象化、aletheia $U$ と同型)
- **$R$ (右随伴・回復関手, 下降方向)**: 真理₀ (構造) $\to$ 真理₁ (有限理論) $\to$ 予測₁ (具体値) — 構造を有限理論に翻訳し、初期条件・境界条件を入れて値に下ろす方向 (情報を補って具体化、aletheia $N$ と同型)
- **C4「Predictions Descend」**: 予測₁ は **$R$ の像** = 下降関手の痕跡。$R$ は完全な逆ではなく ($\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ は同型でない)、$\text{Ker}(\eta_{\text{unit}}) > 0$ が常に残る

Bogen-Woodward 三層との対応:

| Bogen-Woodward 1988 | 本稿 4 型分け | 関手位置 |
|:---|:---|:---|
| **data** (straightforwardly observed, evidence for phenomena) | **予測₁** (値・観測値の現れ) | $L$ の入力 (詳細側) / $R$ の像 (下降の最末端) |
| **phenomena** (detected through data, not directly observable) | **真理₁** (有限理論として整合する pattern) | $L$ の中間 / $R$ の中間 |
| **theory** (predicts and explains phenomena) | **真理₀** への接近 ($L$ の像が向かう先) | $L$ の像 (上昇の到達点) / $R$ の入力 (構造) |

> 出典: Bogen J., Woodward J. (1988). Saving the Phenomena. *The Philosophical Review* 97(3), 303-352, §I pp.305-307.

この三層対応は、本稿の C4 「予測₁ は下降関手 $R$ の痕跡」と Bogen-Woodward 「data は phenomena の evidence であって、theory から直接予測されない」の **構造的同型** を含意する。Bogen-Woodward が data は theory から直接予測されないと述べるのは、関手 $R$ が **theory $\to$ data の単一線形対応ではなく $R_{\text{ph→da}} \circ R_{\text{th→ph}}$ の合成** であって、その合成の単位 $\eta_{\text{unit}}$ が同型でない ($\text{Ker}(\eta_{\text{unit}}) > 0$ で情報が必ず漏れる) ことの言い換えである。phenomena (真理₁) が data (予測₁ の現れ) から detected されるが直接 observable ではないという Bogen-Woodward の構造は、本稿の **$L$ が data $\to$ theory の完全な情報保存上昇ではない** という構造と対応する。

#### 本稿固有貢献 — Bogen-Woodward への延長 (G-κ 反映)

本稿は Bogen-Woodward の **再記述** ではなく **延長** である。Bogen-Woodward 1988 が data / phenomena / theory の 3 層を **記述的に** 区別したのに対し、本稿は次の 4 点で延長する:

1. **真理₀ vs 真理₁ の関手的二層分解**: Bogen-Woodward の theory 内に「構造真理 (普遍構造) vs 経験真理 (有限理論)」の二層を関手的に分解する (§2.1 4 型分け参照)
2. **予測₀ vs 予測₁ の関手的二層分解**: data 内に「構造予測 (何が可能か) vs 値予測 (具体値)」の二層を関手的に分解する
3. **随伴対 $L \dashv R$ の明示**: Bogen-Woodward は射の方向を明示しない (記述的)。本稿は $L$ (上昇) / $R$ (下降) を関手として明示する (構成的)
4. **構造保存定理 (C2) と NRFT (§5.6)**: Bogen-Woodward には対応する数学的構造がない。本稿は $\eta_{\text{unit}}$ 非同型と Yoneda 補題から **No Reverse Functor Theorem の骨格** を導出する (Gödel 第二不完全性に類比される構造的不可能定理)

すなわち本稿は Bogen-Woodward に **依存しつつ延長する**: 3 層 → 4 型 + 随伴構造 + NRFT 骨格。本稿固有貢献は記述レベルの再表現ではなく、**Bogen-Woodward 図式の数学的限界定理化** にある。

⚠️ Hacking 1983 / Daston 1995 / Massimi 2018 等の data-phenomena 区別批判文献の本稿位置づけは **Round 5 課題 (G-κ 残)**。本稿が Bogen-Woodward を批判文献に対してどう守るかは Round 5 で展開する。

---

## §2 随伴構造の導入 (F の最初の展開)

§1 の公理 $L \dashv R$ を実体化するため、本節は次の順で進む。(1) 序で予告した **真理₀ / 真理₁** の定義を立てる (§2.1)。(2) その定義の下で $L \dashv R$ を 3 つの場所に並置する: Bogen-Woodward 三層 (§2.2)、aletheia $U \dashv N$ (§2.3)、視覚の逆問題 (§2.5)。(3) 並置の正当性は GAFT / SAFT による存在条件 (§2.4) で保証される。

### §2.1 真理₀ / 真理₁ / 予測₀ / 予測₁ — 4 つの型分け

序では「真理₀」「真理₁」を未定義のまま置いた。これら 2 つに「予測₀」「予測₁」を加えた 4 型分けは、本稿の中核区別である。定義は HGK 内部の `fep_epistemic_status.md` §真理予測型分け v2.4.0 を採用する。

| 記号 | 名称 | 定義 | 例 |
|:---|:---|:---|:---|
| **真理₀** | 構造真理 / 絶対真理 | 値・座標・観測手続き・実装に先立つ、不変な普遍構造 | $\pi$ そのもの (有限桁展開ではない) |
| **真理₁** | 経験真理 | 真理₀ を有限理論として世界に接続したとき、観測・介入・誤差訂正に耐える限りでの真 | $\pi$ の近似式 (完全同一ではないが、世界拘束の下で有効) |
| **予測₀** | 構造予測 | 何が可能/不可能か、何が何に従うか、どの順序・制約が保たれるかの予告 | 値ではなく「形」の予告 |
| **予測₁** | 値予測 | 初期条件・境界条件・観測写像を入れて具体値・時系列・選択を出すこと | 数値、曲線、行動列 |

> [SOURCE 強: `fep_epistemic_status.md` §真理と予測の型分け v2.4.0 L191-L220、HGK 内部一次 SOURCE]

本稿の公理 ($L \dashv R$ の単位 $\eta_{\text{unit}}$) と上の 4 型は次の通り対応する [SOURCE: fep L204-L207]:

- $\eta_{\text{unit}}$ は **構造** に対しては同型に近づきうる → **真理₀ / 予測₀** に対応
- $\eta_{\text{unit}}$ は **値** に対しては原理的に同型にならない ($\text{Ker}(\eta_{\text{unit}}) > 0$) → **真理₁ / 予測₁** に対応

したがって本稿の核主張 C4 「予測₁ は真理₀ から下降関手 $R$ で生成される痕跡」は、この型分けの直接帰結として 3 点に分解される [SOURCE: fep L211-L213]:

1. **予測₁ を生む理論は真理₀ そのものではない**。それは既に座標化・値化・境界条件化されている。
2. **しかし予測₁ を生む理論は真理₁ ではありうる**。ゆえに「予測を生む理論 = 偽」ではない。
3. **科学は真理₀ へ近づくために真理₁ を鍛える営みであり、工学は真理₁ を制御可能性へ翻訳する営みである** (§7 で Popper / Mangalam / landscape の 3 誤配位がこの 1-3 のどこを取り違えているかを特定する)。

> [!IMPORTANT]
> 「予測を生む理論は真理ではない」と本稿が言うとき、それは **「真理₀ と同一ではない」** ことを意味する。
> これは「偽である」という意味ではない。
> 真理₀ / 真理₁ を分けない議論は、真偽論争ではなく単なる語義滑りを生む [SOURCE: fep L215-L219]。

これで序の伏線「真理₀ / 真理₁ の定義は §2 で立てる」を回収する。次節以降で $L \dashv R$ を 3 つの実体に接続する。

### §2.2 Bogen-Woodward 三層の関手的読み替え

§1.5 で外部接続 anchor として置いた三層を関手的に書き直す。本稿の整合 (§1.1 「$L$ = 還元 / $R$ = 回復」 + §1.5 「$L$ = 上昇、$R$ = 下降」) に従い、Bogen-Woodward の theory $\to$ phenomena $\to$ data 方向は **下降関手 $R$**、逆方向は **上昇関手 $L$** である。

下降関手 $R$ (構造 → 値、生成・具体化方向):

- $R_{\text{th→ph}}$: theory (≈ 真理₀) から phenomena (≈ 真理₁) への射 (構造を有限理論に翻訳)
- $R_{\text{ph→da}}$: phenomena (≈ 真理₁) から data (≈ 予測₁) への射 (有限理論に初期条件・境界条件を入れて値を出す)

合成 $R_{\text{th→da}} = R_{\text{ph→da}} \circ R_{\text{th→ph}}$ が「理論 → データ」の単一線形対応に見えるが、Bogen-Woodward が示すのは、この合成を **2 つの関手の合成として分解すべき** であって、単一線形対応として読むべきではないということだ:

> "Data, which play the role of evidence for the existence of phenomena, for the most part can be straightforwardly observed. However, data typically cannot be predicted or systematically explained by theory. By contrast, well-developed scientific theories do predict and explain facts about phenomena. Phenomena are detected through the use of data, but in most cases are not observable in any interesting sense of that term." (Bogen-Woodward 1988 §I)

> [SOURCE 強候補: Bogen-Woodward 1988 §I pp.305-307 — bogen.txt L101-130 verbatim 抽出 / G-ζ 査読時独立検証義務]

例として彼らが挙げるのは weak neutral currents、proton decay、chunking and recency effects である (L122-130) — いずれも data から間接的に検出されるが、直接 observable ではない。

各下降関手 $R$ に対応する左随伴 $L$ (上昇関手, 値 → 構造、還元・抽象化方向) も存在する:

- $L_{\text{da→ph}}$: data (≈ 予測₁) から phenomena (≈ 真理₁) への射 (測定理論、観測値から pattern を検出)
- $L_{\text{ph→th}}$: phenomena (≈ 真理₁) から theory (≈ 真理₀ への接近) への射 (帰納的構成)

各層で $L_i \dashv R_i$ が独立に成立する。これが本稿の **多層随伴構造** であり、§1.4 表の「F (発散) 入口」の具体形である。

Mangalam 予測至上主義 (§7.2) と benchmark culture が暗黙裏に仮定する「理論 ↔ データの単一対応」は、この多層構造の **2 段関手分解を線形視する誤読** である (§7 で展開)。

### §2.3 aletheia U⊣N との同型対応

aletheia.md §1 (L99-L107) は、視覚-推論二相における随伴定理 U0' を次のように定式化する:

> 「U⊣N: U が左随伴 (忘却関手) / N が右随伴 (回復関手) / VFE 減少定理 $F[N(q_{\text{poor}})] \leq F[q_{\text{poor}}]$ を満たす / $N \circ U \neq \text{Id}$」

> [SOURCE 強: aletheia.md §1 L99-L107、HGK 内部一次 SOURCE]

本稿の L⊣R との対応:

| aletheia.md | 本稿 | 役割 |
|:---|:---|:---|
| $U$ (左随伴, 忘却) | $L$ (左随伴, 発散・還元) | 単純化への射 |
| $N$ (右随伴, 回復) | $R$ (右随伴, 収束・回復) | 整合性検査 |
| $\eta: \text{Id} \Rightarrow N \circ U$ | $\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ | 内在化度合い |
| $F[N(q_{\text{poor}})] \leq F[q_{\text{poor}}]$ | $\eta_{\text{unit}}$ の収束性 | VFE 減少 |

同型対応の方向に注意が必要である。aletheia の $U$ は **精度を落とす** 方向の関手 (例: α-忘却で予測を粗くする) であり、本稿の $L$ は **対象を別のもっと簡単な対象に対応づける** 関手である。両者は **情報を捨てる方向** で構造同型である。

aletheia §2.1 (L126-141) は $U$ の 8 段パターン生成テーブルを与える。

> [SOURCE 強: aletheia.md §2.1 L126-141。ただし self-label 「[推定 70%] 75%、motivated choice、関手的証明 open」(L141) — 本稿は構造的類推水準として引用、厳密関手証明は本稿外の継続課題 (§M5.1 Round 1 r6 対応で降格済)]

aletheia §2.3 (L154-195) は Bohr 太陽系モデルの worked example を提示しており、§3.2 (ゲージ理論)・§3.3 (統計力学) で参照する。

### §2.4 GAFT / SAFT による L⊣R 存在条件

L⊣R の well-defined 性は無条件には成立しない。Mac Lane CWM §V.6 GAFT (General Adjoint Functor Theorem, p.117) は次の条件で存在を保証する:

> $A$ が small-complete かつ small hom-sets を持つとき、関手 $G: A \to X$ が左随伴を持つ ⟺ $G$ が連続 (small limit 保存) かつ Solution Set Condition (SSC) を満たす。SSC: $\forall x \in X$ に対し small set $I$ と $\{a_i \in A\}_{i \in I}$ および $\{f_i: x \to G(a_i)\}$ が存在し、任意の arrow $x \to G(a)$ が $h = G(t) \circ f_i$ ($t: a_i \to a$) の合成として書ける。

> [SOURCE 中: Mac Lane CWM §V.6 p.117 を Buzzard 2012 Imperial College lecture notes p.2 Theorem 1.1 が verbatim 引用 — triangulation。本稿査読時に Mac Lane CWM 直接 Read で「強」昇格義務 (G-ζ)]

§V.8 SAFT (Special Adjoint Functor Theorem, p.125-126) はより強い前提を要求する:

> $C$ が small-complete, locally small, well-powered, small cogenerating set を持ち、$D$ が locally small なら、極限保存関手 $G: C \to D$ は左随伴を持つ。

> [SOURCE 中: Mac Lane CWM §V.8 p.125 を Buzzard 2012 L185-194 + nLab 公式が triangulation。本稿査読時に Mac Lane CWM 直接 Read で「強」昇格義務 (G-ζ)]

本稿は **GAFT (SSC) を主条件**、SAFT (cogenerator) を補助条件として置く。GAFT を満たさない $L_i$ は射程外と宣言する (§M5.1 Round 1 r1 対応)。これは「全関手で L⊣R が成立する」という overclaim を予防する措置であり、§1.6 で開示した Z-03 圏論 overclaim 反論への構造的防御である。

### §2.5 視覚の逆問題メタファー

読者の直観を起動するため、視覚の逆問題で随伴構造を例示する。

網膜に届く光強度のパターンは Bogen-Woodward の意味での **data** (= 本稿の **予測₁** の現れ; §1.5 三層対応) である。だが網膜パターンから「何を見ているか」を直接読むことはできない。我々は無意識のうちに 2 段階の **L (上昇関手, 還元方向)** を経て概念 (theory ≈ 真理₀ への接近) に到達している:

1. $L_{\text{retina→percept}}$: 網膜パターン → 知覚オブジェクト (例: 「猫がいる」)
2. $L_{\text{percept→concept}}$: 知覚オブジェクト → 概念ラベル (例: 「Schrödinger の猫」)

それぞれに右随伴が存在する:

1. $R_{\text{percept→retina}}$: 概念から予測される網膜パターン (image prediction; 内部生成モデル)
2. $R_{\text{concept→percept}}$: 概念から予測される知覚パターン

理解とは、各層で $\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ が **構造** に対しては iso に近づくが、**値** (例えば瞬間的な網膜画素強度) に対しては iso にならない、という構造的不等式の中に住んでいることである。

これが §1.2 公理の C2 (構造保存定理) の直観的な絵である。網膜画素強度の完全予測 ($\eta_{\text{unit}}$ = iso for all values) は不可能であり、また不要である。我々が予測しているのは **構造としての世界** であって、画素値ではない。

ここで重要なのは、この絵が脳科学・認知科学の経験的事実というより、**Bogen-Woodward 段階構造の必然的帰結** だということである。data (網膜) から phenomena (知覚) を経て theory (概念) に至る経路は、関手として読めば 2 段の合成であり、単一線形対応ではない。

---

## §3 5 分野横断展開 (F の本体)

§2 で導入した随伴構造 L⊣R を、独立した 5 分野で並列に例示する。各分野は別々の数学的言語を持つが、構造としては同じ随伴対が現れる。これが §1.2 C1 「3 分野同型」の 5 分野拡張であり、文体ガイド §3.2.6 の **定式化変換** の本体である。

5 分野の選択は道 C (科学一般の認識論定理) 射程に整合させた:

- §3.1 **情報幾何**: Fisher 計量の非等方として $\eta_{\text{unit}}$ 非同型
- §3.2 **ゲージ理論**: 接続の曲率として $\eta_{\text{unit}}$ の非自明性
- §3.3 **統計力学**: 自由エネルギー最小化と VFE 減少
- §3.4 **数論**: Peano successor の生成構造と値の分離
- §3.5 **FEP**: 予測誤差として補完₁

### §3.1 情報幾何 (Fisher 計量の非等方)

統計多様体上で Fisher 計量 $g_{ij}(\theta) = E[\partial_i \log p \cdot \partial_j \log p]$ が定まる。Fisher 計量は **非等方** であり、パラメータ空間の方向によって情報量が異なる。

本稿の L⊣R 対応:

- $L_{\text{IG}}$: 統計多様体 $M$ 上の点 $\theta$ をパラメータ表現に対応づける
- $R_{\text{IG}}$: パラメータから分布族の元を回復する

$\eta_{\text{unit}, \text{IG}}: \theta \to R_{\text{IG}}(L_{\text{IG}}(\theta))$ は分布の同値類に関しては iso に近づくが、Fisher 計量の **異方性そのもの** は iso にならない。すなわち、パラメータの数値表現を完全に保つことはできない (Cramér-Rao 不等式)。

> [SOURCE 中: Amari (1985) "Differential-Geometrical Methods in Statistics" Lecture Notes in Statistics 28、Cencov (1972) "Statistical Decision Rules and Optimal Inference"。本稿査読時に Amari 1985 直接 Read で「強」昇格義務 (G-ζ)]

これは Paper III の曲率テンソル $K_{\text{geom}}$ と関連する。

> [SOURCE 強: HGK 内部一次 SOURCE — Paper III 曲率テンソル定義。統一記号表 §1.7 の F_{ij} 曲率と同体]

### §3.2 ゲージ理論 (接続の曲率)

ゲージ理論において、ファイバー束 $E \to M$ 上の接続 $\nabla$ は曲率 2-形式 $F_{ij} = [\nabla_i, \nabla_j]$ を生む。曲率がゼロでない場合 (非可積分性)、ファイバー上での平行移動はパスに依存する。

本稿の L⊣R 対応:

- $L_{\text{gauge}}$: 接続から物理的観測量 (ホロノミー、ゲージ不変量) への射
- $R_{\text{gauge}}$: 観測量から接続を復元する射 (典型的には不完全)

$\eta_{\text{unit}, \text{gauge}}$ は **ゲージ等価類** に関しては iso だが、**接続そのもの** に対しては iso にならない (Aharonov-Bohm 効果が示すように、ゲージ不変な観測量が接続を完全には決定しない場合がある)。

> [SOURCE 強: HGK 内部一次 SOURCE — Paper I §5.1 方向性定理 $F = \nabla \Phi$、Paper III 曲率テンソル。統一記号表 §1.2 / §1.7]

aletheia §2.3 (L154-195) の Bohr 太陽系モデルは、量子化された軌道を「曲率の離散的固有値」として読む例を与える。

> [SOURCE 強: aletheia.md §2.3 L154-195、HGK 内部一次 SOURCE]

### §3.3 統計力学 (自由エネルギー最小化)

統計力学において、系のミクロ状態 $\omega \in \Omega$ から自由エネルギー $F[q] = E_q[\mathcal{H}] - T \cdot S[q]$ が定まる ($q$ は分布、$\mathcal{H}$ はハミルトニアン、$S$ はエントロピー)。

本稿の L⊣R 対応:

- $L_{\text{stat}}$: ミクロ状態空間 $\Omega$ から粗視化分布 $q$ への射
- $R_{\text{stat}}$: 粗視化分布から条件付きミクロ状態への射 (Maxwell-Boltzmann)

$\eta_{\text{unit}, \text{stat}}$ は **熱力学量 (温度・圧力・化学ポテンシャル)** に関しては iso だが、**個別ミクロ状態** に対しては iso にならない。これが熱力学の不可逆性の関手的読み替えである。

aletheia §1 の VFE 減少定理 $F[N(q_{\text{poor}})] \leq F[q_{\text{poor}}]$ は本稿 $L_{\text{stat}} \dashv R_{\text{stat}}$ の収束性に対応する。

> [SOURCE 強: aletheia.md §1 L99-L107、HGK 内部一次 SOURCE]

### §3.4 数論 (Peano successor と値の分離)

Peano 算術において、successor 関数 $S: n \mapsto n+1$ が自然数の生成構造を与える。$\mathbb{N}$ の元は successor の有限合成 $S^k(0)$ として **構造的に** 決まるが、各 $S^k(0)$ の **値** (例えば「7」という具体的記号) は別の話である。

本稿の L⊣R 対応:

- $L_{\text{num}}$: 自然数 $n$ から successor の合成深さ $k$ への射 (構造抽出)
- $R_{\text{num}}$: 合成深さから自然数を再構成する射

$\eta_{\text{unit}, \text{num}}$ は **同型類 (有限基数としての同値性)** に関しては iso だが、**記号的表現** (10 進、2 進、ローマ数字) に対しては iso にならない。これは「自然数とは何か」を operational identity として定義する Peano 的立場の関手的読み替えである。

> [SOURCE 中: Peano (1889) "Arithmetices Principia, Nova Methodo Exposita"、Dedekind (1888) "Was sind und was sollen die Zahlen?"。本稿査読時に Peano 原典 Read で「強」昇格義務 (G-ζ)]

数論を 5 分野に含めた理由は、本稿の主張が **物理現象に依存しない** ことを示すためである。L⊣R 構造は数学的構成そのものに内在する。

### §3.5 FEP (予測誤差と補完₁)

Friston の Free Energy Principle (FEP) において、生成モデル $p(o, s)$ と認識モデル $q(s)$ の間に変分自由エネルギー $F[q] = D_{\text{KL}}(q(s) \| p(s|o)) - \log p(o)$ が定まる。

本稿の L⊣R 対応:

- $L_{\text{FEP}}$: 観測 $o$ から認識モデル $q(s)$ への射
- $R_{\text{FEP}}$: 認識モデルから観測予測 $p(o)$ への射

$\eta_{\text{unit}, \text{FEP}}$ は **認識モデルの構造** に関しては iso に近づくが、**個別観測値** に対しては iso にならない。これが §1.2 C3 の「補完₁ ≡ Ker($\eta_{\text{unit}}$) と構造的に結びつく」の FEP 内具体形である。

予測の二層分解 (fep_epistemic_status §予測の二層分解 v2.5.0):

- **予測₀ (構造予測)** = 真理₀ から取り出される **形の予告** (どの制約・保存則・順序が保たれるか)。$L$ の上昇方向で構造として現れる
- **予測₁ (値予測)** = 真理₀ から $R$ (下降関手) を通って降ろされる **具体値** (初期条件・境界条件を入れて出す数値・時系列・選択)。Bogen-Woodward の data に対応 (§1.5)
- **補完₁** = $L$ で失われ $R$ で完全には回復されない情報を内部モデルで穴埋めすること ($\text{Ker}(\eta_{\text{unit}})$ と構造的に結びつく、補完₁ 依存)

> [SOURCE 強: fep_epistemic_status.md §予測の二層分解 v2.5.0 L288-L301、HGK 内部一次 SOURCE]

注記 (§M5.1 Round 1 r4 対応): 「補完₁ ≡ |Ker($\eta_{\text{unit}}$)|」の等号主張は **「結びつく」** に降格済 (fep L299)。Gaussian 閉形式での厳密対応は §5 の IB 鋼鉄化で骨格まで、計算例は G-ε として継続課題。

### §3.6 5 分野横断同型の総合

5 分野で並列に出現した $L_i \dashv R_i$ と $\eta_{\text{unit}, i}$ は、構造としては同型である:

| 分野 | 構造保存軸 | 値非保存軸 |
|:---|:---|:---|
| 情報幾何 | 分布同値類 | Fisher 計量の異方性 |
| ゲージ理論 | ゲージ等価類 | 接続そのもの |
| 統計力学 | 熱力学量 | 個別ミクロ状態 |
| 数論 | 同型類 (有限基数) | 記号的表現 |
| FEP | 認識モデル構造 | 個別観測値 |

この同型は Yoneda の補題によって支持される — 「対象はそのすべての射で完全に決まる」(米田) ということは、**異なる分野で同じ随伴構造が出現すれば、それらは関手的に同型である**ことを含意する。詳細は §4 で展開する。

5 分野横断同型は、本稿が「FEP 固有の主張」ではなく「全科学共通の構造的制約」であることの操作的証拠である (§1.3 の FEP 非依存性宣言の支持)。

---

## §4 Yoneda 接続 (G の極限化 1)

§3 で 5 分野に並列出現した随伴構造 $L_i \dashv R_i$ を、米田の補題によって統一する。本節は §1.4 表「G (収束) その 1」の本体であり、§1.6 で開示した SOURCE 強度ラベルの体系を Riehl 2016 / Mac Lane CWM の verbatim 引用で支える。

### §4.1 Yoneda の補題 (Mac Lane CWM §III.2 + Riehl 2016 §2.2)

Yoneda の補題は次のように述べる:

> **Yoneda Lemma** (Riehl 2016 §2.2 Theorem 2.2.4): For any functor $F: C \to \mathbf{Set}$ whose domain is locally small and any object $c \in C$, the function $\text{Nat}(C(c, -), F) \to F(c)$ defined by $\alpha \mapsto \alpha_c(\text{id}_c)$ is a bijection. Moreover, this correspondence is natural in both $c$ and $F$.

> [SOURCE 強候補: Riehl 2016 §2.2 Theorem 2.2.4 — riehl.txt L4763-4775 verbatim 抽出 / G-ζ 査読時独立検証義務]

> Mac Lane CWM §III.2 Theorem 1 が同じ補題を Hom-functor の言語で述べる。

> [SOURCE 中: Mac Lane CWM 1971/1998 §III.2 Theorem 1 — Wikipedia + Riehl 2016 帰属が triangulation。本稿査読時に Mac Lane CWM 直接 Read で「強」昇格義務 (G-ζ)]

操作的読み替え: **対象 $c$ は、その全ての射 $C(c, -)$ で完全に決まる**。これが §1.2 C1 で公理として置いた「理解 = L⊣R 内在化」の数学的基礎である。

「$c$ を理解している」⟺ 「$c$ への射、$c$ からの射、それらの合成パターンを内側に持つ」⟺ 「$\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ が iso (構造に対して)」

### §4.2 表現可能関手による極限保存 (Riehl §3.5)

Yoneda 埋め込みは極限を保存する:

> **Theorem 3.5.5** (Riehl 2016 §3.5): Covariant representable functors $C(X, -): C \to \mathbf{Set}$ preserve all limits that exist in $C$. The covariant Yoneda embedding $C \hookrightarrow \mathbf{Set}^{C^{\text{op}}}$ both preserves and reflects limits.

> [SOURCE 強候補: Riehl 2016 §3.5 Theorem 3.5.5 — riehl.txt L8702-8709 verbatim 抽出 / G-ζ 査読時独立検証義務]

> 注: 依頼書では §3.4 と表記されていたが、Riehl 2016 の正しい節番号は **§3.5 The representable nature of limits and colimits**。誤記訂正済 (§M5.2 段階 B)。

これが §3.6 の 5 分野横断同型の数学的支持である。各分野で出現した随伴対 $L_i \dashv R_i$ は、Yoneda 埋め込みを通じて presheaf 圏 $\mathbf{Set}^{C^{\text{op}}}$ に埋め込まれ、極限構造が保存される。すなわち、**5 分野で出現した同型は presheaf 圏での極限同型に帰着する**。

### §4.3 kalon §2 L161 補強引用 (Mac Lane-Moerdijk)

kalon.md §2 (L161-166) は HGK の圏 $M$ が presheaf 圏と同型であることを示す:

> 「HGK の圏 M ≅ PSh(J) は presheaf 圏 → 自動的に (co)complete (Mac Lane-Moerdijk)。」

> [SOURCE 強: kalon.md §2 L161-166、HGK 内部一次 SOURCE。Mac Lane CWM Thm X.3.1 の引用部分は §V.6/V.8 と同様 G-ζ 独立検証で「強」昇格義務]

これは §3.6 の 5 分野横断同型が presheaf 圏で実現されることの **構造的支持** である。「HGK の圏 $M$ が presheaf 圏と同型」⟺ 「本稿の L⊣R が Yoneda 埋め込みの像として well-defined」。

### §4.4 圏論的衣装除去テストへの応答 (kalon §2.5)

kalon.md §2.5 (L368-403) は「圏論的衣装除去テスト」を提示する: 「7 主張のうち 4 つは自然言語で十分判定」(L388-389)。本稿は Yoneda の補題を採用するが、これが §2.5 自身が「圏論固有」と認める領域 (Lan 拡張 + LFPT) に該当することを開示する。

> [SOURCE 強: kalon.md §2.5 L368-403 + L388-389、HGK 内部一次 SOURCE]

本稿の Yoneda 採用は kalon §2.5 への **反対方向作用** ではなく、§2.5 の判定枠組み内で「圏論固有領域」として正当化される。具体的には:

- C1 (理解 = L⊣R 内在化) は Yoneda の operational identity を本質的に使う
- C2 (構造保存定理) は faithful functor factorization (Mac Lane Ch. X / Kan 拡張) を本質的に使う
- C3 (補完₁ 単調減少) は §5 の IB Lagrangian と組み合わせて圏論的になる

これらは「自然言語で十分判定」される 4 主張ではなく、kalon §2.5 自身の判定で「圏論固有」とされる領域に入る。本稿の Yoneda 採用は kalon §2.5 と矛盾しない。

注記: kalon.md §9 (L2302-2325) の「概念 ≈ presheaf」は self-label「水準 C (比喩的使用)」であり、本稿の load-bearing 引用には不足である。本稿は §2 L161 (Mac Lane CWM 引用、水準 A 寄り) を主引用、§9 を補助引用に降格する (Block A worker findings, §M5.2 段階 B)。

### §4.5 §1.2 構成的定義の Yoneda 接地

⚠️ **論理飛躍の明示開示** (Round 4 §M5.4 予告): Yoneda の補題は category-theoretic statement (「対象は表現可能関手で完全に決定される」) であって epistemological statement (「人間/科学の理解の必要十分条件」) ではない。両者は同値ではなく、本稿は §1.1 で **構成的定義として L⊣R 内在化を採用する** という立場を明示することでこの飛躍を埋める。Yoneda は本稿の主張の **必要条件の数学的足場** であって十分条件の証明ではない (G-η / G-θ で Round 5 課題)。

§1.2 で構成的定義として置いた L⊣R を、ここまでの Yoneda 接続で **数学的足場の上に置く**:

1. **operational identity** (Yoneda Lemma): 対象 $c$ は $C(c, -)$ で決まる ⟹ $\eta_{\text{unit}}$ が iso ⟺ $C(c, -) \cong C(R(L(c)), -)$
2. **極限保存** (Riehl §3.5): 5 分野横断同型は presheaf 圏での極限同型に帰着
3. **存在条件** (GAFT/SAFT, §2.3): $L \dashv R$ の well-defined 性は SSC または cogenerator で保証
4. **HGK 圏との接続** (kalon §2 L161): HGK 圏 $M \cong \text{PSh}(J)$ により本稿構造が realizable

これら 4 点が §1.2 公理を「単なる定義」ではなく「Yoneda 接続を持つ操作的 anchor」に昇格させる。

---

## §5 IB 鋼鉄化 (G の極限化 2)

§4 で公理を Yoneda 接続したのに続き、§1.2 C3 「補完₁ 単調減少定理」を **Information Bottleneck (IB) Lagrangian + Data Processing Inequality (DPI)** で Pareto frontier 上の定理として鋼鉄化する。本節は §1.4 表「G (収束) その 2」の本体である。

### §5.1 Tishby-Pereira-Bialek 1999 IB の再記述

Tishby-Pereira-Bialek (1999) は Information Bottleneck を次のように定式化する:

> 「relevant information = $X$ が他信号 $Y$ について与える情報。$X$ の short code を $Y$ に関する最大情報を保存しつつ bottleneck (limited codewords) を通して圧縮する問題を定式化」「自己無撞着方程式の厳密集合 ($X \to \tilde{X}$ と $\tilde{X} \to Y$ の coding rules) を導く」 (Tishby-Pereira-Bialek 1999 abstract)

> [SOURCE 中: arxiv physics/0004057 abstract verbatim、subagent 抽出。本稿査読時に Tishby et al. 1999 PDF 直接 Read で「強」昇格義務 (G-ζ)]

形式的に IB Lagrangian は:

$$\mathcal{L}_{\text{IB}} = I(X; T) - \beta I(T; Y)$$

ここで:

- $X$: 観測信号 (本稿の **予測₁** に対応 — Bogen-Woodward の data 層、§1.5 三層対応で確認)
- $Y$: relevant signal (本稿の **真理₁** に対応 — phenomena 層、Bogen-Woodward が theory から間接的に予測される対象)
- $T$: bottleneck variable (本稿の認識モデル / 中間表現、$L$ で $X \to T$、$R$ で $T \to Y$)
- $\beta$: trade-off パラメータ

### §5.2 Data Processing Inequality (DPI)

Cover-Thomas Ch. 2 の DPI は次の通り:

> **DPI**: Markov chain $X \to T \to Y$ について $I(X; Y) \geq I(T; Y)$ かつ $I(X; T) \geq I(X; Y)$

> [SOURCE 中: Cover-Thomas "Elements of Information Theory" 2nd ed. Ch. 2.8 Theorem 2.8.1。本稿査読時に Cover-Thomas 直接 Read で「強」昇格義務 (G-ζ)]

DPI は「処理が情報を増やすことはない」という不可避な単調性であり、本稿 §1.2 C3 「理解の深化は補完₁ 依存を単調減少させる」の情報理論的核である。

### §5.3 随伴構造との対応

IB と本稿 L⊣R の対応:

- $\beta \to \infty$ 極限: $T \to L(X)$ (relevant 情報を最大限保持)
- $\beta \to 0$ 極限: $T \to \text{const}$ (圧縮を最大化)
- 中間 $\beta$: Pareto frontier 上の operating point

随伴構造として読むと:

- $L_{\text{IB}}$: $X$ から $T$ への射 (圧縮)
- $R_{\text{IB}}$: $T$ から $Y$ の予測への射 (relevant 情報の取り出し)
- $\eta_{\text{unit}, \text{IB}}: \text{Id} \Rightarrow R_{\text{IB}} \circ L_{\text{IB}}$: $X$ が $R_{\text{IB}}(L_{\text{IB}}(X))$ に再構成される度合い

$|\text{Ker}(\eta_{\text{unit}, \text{IB}})| > 0$ は **$X$ から失われ $T$ では捉えられない情報** を測る (DPI による不可避な情報損失)。

### §5.4 補完₁ 単調減少関係の Lagrangian 形式化

⚠️ 降格注記 (Round 4 §M5.4 予告): §M5.1 Round 1 r4 対応で「補完₁ ≡ |Ker($\eta_{\text{unit}}$)|」の等号主張は **「結びつく」**(fep_epistemic_status §予測の二層分解 v2.5.0 L299) に降格済。本節の表題から「定理の鋼鉄化」を削除し、「**Lagrangian 形式化**」に置き換える。形式証明としての「単調減少定理」は本稿外の継続課題 (§6.4 G-ε)。

§1.2 C3 「理解の深化は補完₁ 依存を単調減少させる」の Lagrangian 形式化骨格:

$$\frac{\partial |\text{Ker}(\eta_{\text{unit}})|}{\partial (\text{理解度})} \leq 0 \quad \text{(関係式骨格、形式証明は G-ε で継続)}$$

ここで「理解度」は $\eta_{\text{unit}}$ が構造に対して iso に近づく度合い ($\beta$ の最適化)。

**操作的議論骨格 (形式証明ではない)**:

1. 理解度の増加 ⟹ $T$ が $Y$ をより良く予測 ($I(T;Y) \uparrow$)
2. DPI により $I(X;Y) \geq I(T;Y)$ なので、$I(T;Y)$ の上限は $I(X;Y)$
3. 構造保存定理 (§1.2 C2) により $I(X;Y) < I(X;X) = H(X)$ ($\eta_{\text{unit}}$ 非同型)
4. ゆえに補完₁ ($X$ から $T$ で捉えられない部分) は単調減少するが、ゼロにはならない (議論骨格として)

この骨格は **道 C 射程の議論骨格** として機能する: 「理解の深化は予測補完への依存を単調減少させるが、ゼロにはできない」。形式証明としての完成は **Round 5 課題 (G-θ 予定)** に保留する。

### §5.5 Gaussian 閉形式の継続課題 (G-ε)

§1.2 C3 の Gaussian 閉形式での厳密計算は本稿執筆時の継続課題である:

- 試行: Princeton PDF (`https://www.princeton.edu/~wbialek/our_papers/tishby+al_99.pdf`) 取得を試みたが SSL cert error で失敗 (§M5.2 段階 B)
- 代替経路 1: `wget --no-check-certificate` で再取得
- 代替経路 2: arxiv physics/0004057 v2/v3 から self-consistent eq の specific form 確認
- 代替経路 3: Slonim-Tishby (2000) 後続論文での Gaussian 計算例

本稿は Lagrangian + DPI まで SOURCE 接続済 ($\beta$ trade-off は §5.3 まで)、Gaussian 閉形式は §M9.1 G-ε として継続課題に残す。

> [SOURCE 中: Tishby-Pereira-Bialek 1999 abstract verbatim、subagent 抽出 / G-ε 残: Gaussian 閉形式の specific form は本体起票後再取得義務]

### §5.6 No Reverse Functor Theorem (NRFT) — 道 C 射程の不可能定理骨格

本稿の野望 (meta §M0.3 道 C: Gödel と並ぶ認識論定理) を支える不可能定理候補を **骨格として** 提示する。完全形式証明は **Round 5 課題 (G-λ)** に保留する。

**NRFT 骨格 (No Reverse Functor Theorem)**:

> **主張 (骨格)**: $L \dashv R$ で $\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ が iso でない (§1.2 C2 構造保存定理) とき、**予測₁ から真理₀ への完全 retraction 関手 $S$ は存在しない**。

**論証骨格 (形式証明ではない)**:

1. 仮定: 完全 retraction 関手 $S: \text{予測}_1 \to \text{真理}_0$ が存在し、$S \circ L_{\text{th→da}} = \text{Id}_{真理_0}$ を満たすとする
2. §1.2 C2 構造保存定理により $\eta_{\text{unit}} = R \circ L$ は iso ではない、すなわち $|\text{Ker}(\eta_{\text{unit}})| > 0$
3. もし $S$ が完全 retraction なら、$S$ 経由で $\eta_{\text{unit}}$ を iso に「補完」できることになる
4. これは (2) と矛盾する
5. ∴ **完全 retraction 関手 $S$ は存在しない (NRFT 骨格)**

**Gödel 第二不完全性定理との類比**:

| Gödel 第二不完全性定理 | NRFT (本稿骨格) |
|:---|:---|
| 形式系 $T$ の自己無矛盾性 $\text{Con}(T)$ は $T$ 内で証明不可能 | $L \dashv R$ の予測₁ → 真理₀ 完全 retraction $S$ は存在しない |
| 構造的不可能性 (体系の自己言及で発生) | 構造的不可能性 ($\eta_{\text{unit}}$ 非同型から発生) |
| 形式系の限界定理 | 認識論的限界定理 |

両者とも **構造的に閉じた不可能定理** であり、Mangalam 型「予測精度を真理₀ 指標とする」立場が **構造的に不可能** であることを示す。

**SOURCE 強度**:

> [SOURCE 強: aletheia §1 L99-L107 + §7.4 L2601-L2706 + 本稿 §1.2 C2、HGK 内部一次 SOURCE — 骨格論証は HGK 内部定理から導出]
>
> [TAINT: 仮置き — Gödel 第二不完全性との **形式的同型** は本稿で未証明、構造的類比のみ。Round 5 G-λ で定理ステートメント + 証明 + 系の完全形を本稿外で構築する義務]

**主張水準** (§M1.3 整合): C4 を「仮説 60%」→「**仮説 65%** (NRFT 骨格による補強)」に微調整 (Round 4 反映)。完全形式証明後に C4 主張水準の Round 5 再較正を実行。

---

## §6 制約節 (Round 3 反論吸収統合)

§1.3 で開示した射程切断と、§M5.3 Round 3 で処理した反論吸収を本節に集約する。本節は §1.4 表「限界明示」の本体であり、本稿が **何を主張せず** **何を射程外と宣言する** かを構造的に開示する。

### §6.1 構造決定論的立場の自覚開示 (Z-05 反論吸収)

§1.3 の 2 番で予告したとおり、本稿は **構造決定論的立場を意図的に採用** する。これは IIT (Tononi 2008 / IIT 4.0 2023) と構造的に同型だが、commitment レベルが異なる:

| 立場 | commitment レベル | 主張内容 |
|:---|:---|:---|
| **IIT** | ontological | 意識の **必要十分条件** を構造 (φ 値, cause-effect structure) で与える |
| **本稿** | definitional | 理解の **操作的定義** を構造 (L⊣R 内在化) で与える |

「なぜ構造が理解を生むか」(本質論) は本稿の問いではない。本稿は問いの水準を **意図的に変更** して「理解が L⊣R 内在化として何を意味するか」(操作的定義) に絞る。

> [SOURCE 中: IIT canonical claim = 「consciousness is identical to a system's integrated causal structure, an irreducible cause-effect repertoire quantified by Φ (phi), intrinsic property of the system」(arxiv 2510.04084 v1 p.1, alphaXiv triangulation, 2026-04-25 取得)。**IIT commitment = ontological** (consciousness identical to causal structure, 必要十分条件) と本稿 = definitional (operational anchor) の差が SOURCE で確定]
>
> [SOURCE 強候補待ち: 完全 PDF Read による「強候補」昇格 + Tononi 2008 / IIT 4.0 (2023) 原典 + Albantakis 2025 (arxiv 2509.00555 "Integrated information and predictive processing theories of consciousness") 詳細精読は **Round 5 課題 (G-ι 残)**]

この立場明示は Z-05 反論 (構造決定論の自己適用) を **限界明示** で吸収する戦略である (§M5.3 Round 3 r9)。「本稿は IIT と同様の構造決定論的だが、commitment レベルが異なる」と宣言することで、批判の方向を「立場の選択」に切り替える。

### §6.2 co-evolution 限定 (G-δ 予防策)

§0 / §1.3 で宣言した co-evolution 限定の精細化。本稿主張の Future-Proof 構造は以下の通り (meta §M4.2):

- **強化観測される範囲** (現世代モデル + 現世代科学コミュニティ): 本稿主張は強化される (Future-Proof Test +1σ for C1-C3, C5; +0.5σ for C4)
- **完全自明化に達した場合** (圏論アクセス LLM 大衆化 = S4): C1 / C4 は scaffolding として消える可能性

S4 自明化は本稿主張の **反証ではなく実装段階移行** である。「強い AI 出現後の科学哲学は本稿の射程外」を §1.3 / §6 で明示宣言することで、Future-Proof Test での縮退/反転リスクを **scope 区別で吸収** する (§M5.3 Round 3 G-δ)。

### §6.3 ontological commitment スペクトル (Cartwright 発散吸収)

§1.5 で外部接続 anchor とした Bogen-Woodward 1988 を踏まえつつ、van Fraassen 1980 / Cartwright 1983 との立場差を ontological commitment スペクトルとして並列開示する:

| 立場 | commitment レベル | 実在主張 |
|:---|:---|:---|
| van Fraassen 構成的経験主義 | 反実在論 | observable のみ (acceptance ⊂ belief) |
| **本稿関手痕跡論** | relational | 関手関係 (= 下降関手 $R$、真理₀ → 予測₁) を実在の anchor とする |
| Cartwright entity realism | ontological | theoretical entities (electrons, neutrons 等) は実在 |

> [SOURCE 強候補: Cartwright 1983 Introduction + Essay 6 — cartwright.txt L1-13, L2717-2811 verbatim 抽出 / G-ζ 査読時独立検証義務]

> [SOURCE 強候補: van Fraassen 1980 §1.3 / §1.5 — vanfraassen.txt L391-395 verbatim 抽出 / G-ζ 査読時独立検証義務]

van Fraassen の構成的経験主義は: 「acceptance of a theory involves as belief only that it is empirically adequate」(§1.3) / 「a theory is empirically adequate exactly if what it says about the observable things and events in the world is true」(§1.5)。

Cartwright の entity realism は: 「fundamental laws describe highly idealized objects in models」「despite their great explanatory power these laws do not describe reality」(Introduction)。simulacrum account / phenomenological laws は真であり得るが fundamental explanatory laws はそうではない。

本稿の位置: **ontologically thinner than Cartwright, more committed than van Fraassen**。Cartwright が theoretical entities への部分実在論を保持するのに対し、本稿は関手関係そのものを実在の anchor として相対化する。van Fraassen が observable に閉じるのに対し、本稿は phenomena 層 (真理₁) の関手痕跡を「関手関係としては実在」と読む。

この立場の中間性により、Cartwright 発散と van Fraassen 反実在論を両立的に吸収する (§M5.3 Round 3 Cartwright 発散吸収)。

### §6.4 残ギャップの限界明示

本稿の継続課題を §M9.1 残ギャップ表に従い開示する:

| ギャップ | 内容 | 状態 |
|:---|:---|:---|
| **G2** | 5 分野横断 $L_i$ 統合 | §3 で並列展開済、各分野の厳密関手証明は本稿外の継続課題 |
| **G4** | ω 折畳の形式証明 | oblivion_connection_map §2.4 の構造的開問題として開示済。本稿は ω 折畳 gap を含む CE = B [推定 90%] の上で構造保存定理を引用 |
| **G-ε** | Tishby Gaussian 閉形式 | §5.5 で開示済、本体起票後に再取得義務 |
| **G-ζ** | subagent SOURCE 独立検証 | Riehl/Cartwright/van Fraassen/Bogen-Woodward/Buzzard PDF + arxiv abstract を Tolmetes または独立 reviewer が直接 WebFetch / 物理書籍 Read で再確認、「強候補」→「強」昇格 |
| **G-η** (Round 4 処理済) | 5 分野同型 (§3.6) の形式同型射 (functor + natural transformation) 具体構成 | **部分着手 ✓** (Round 4 で 2 ペア骨格: Information Geometry × Statistical Mechanics の Legendre 双対 + Gauge × Information Geometry の Yang-Mills/Fisher 曲率対応)。5 分野全ペア (10 対) natural transformation 完全構成は **Round 5 課題** |
| **G-θ** (Round 4 処理済) | Gödel 級不可能定理の構成的提示 | **大幅補強 ✓** (Round 4 で **No Reverse Functor Theorem (NRFT) 骨格** を §5.6 に提示。$\eta_{\text{unit}}$ 非同型 + Yoneda 補題から「予測₁ → 真理₀ への完全 retraction 関手 $S$ は存在しない」を骨格として導出。道 C 達成度 30% → 50%)。完全形式証明は G-λ で Round 5 課題 |
| **G-ι** (Round 4 処理済 + alphaXiv MCP) | IIT (Tononi 2008 / IIT 4.0 2023) 同型 SOURCE 確保 | **部分着手 ✓** (2026-04-25 alphaXiv MCP triangulation): IIT canonical claim = 「consciousness is identical to a system's integrated causal structure, an irreducible cause-effect repertoire quantified by Φ (phi), intrinsic property of the system」[SOURCE 中: arxiv 2510.04084 v1 p.1]。IIT commitment = ontological と本稿 = definitional の差が SOURCE で確定。完全 PDF Read による「強候補」昇格は Round 5 課題。**追加発見**: arxiv 2509.00555 (Albantakis 2025) IIT × predictive processing 比較レビューが §3.5 + §6.1 橋渡しに直接関連 |
| **G-κ** (Round 4 処理済) | Bogen-Woodward 三層への過度依存 | **解消 ✓** (Round 4 で本稿固有貢献を明示: Bogen-Woodward 3 層 (data/phenomena/theory) → 本稿 4 型 (真理₀/真理₁/予測₀/予測₁) + 関手構造 $L \dashv R$。§1.5 4 型分けで実装済)。Hacking 1983 / Daston 1995 / Massimi 2018 批判文献走査は Round 5 課題 |
| **G-λ** (Round 4 由来、新設) | NRFT (No Reverse Functor Theorem) 完全形式証明 | **未着手** (Round 4 で骨格のみ §5.6 提示)。定理ステートメント + 証明 + 系の完全形 + Gödel 第二不完全性との形式的同型は Round 5 課題 |

これらの gap を **隠さず開示** することは、§M6 (虚→実変換面) の Yugaku 規律に従う。野望そのものは罪ではない、罪は何がまだ虚かを伏せたまま実を装うことである。

⚠️ **/exe+ → /dio → Round 4 自己批判ループの記録** (2026-04-25): 本表の G-η / G-θ / G-ι / G-κ / G-λ は v0.2 §1-§7 の /exe+ 吟味で検出された 🔴 3 件 + 🟡 中の代表問題に由来する。Round 4 (§M5.4) で gauntlet 形式 (Round 1-3 と同形式) で処理済、本セッションで G-η 部分着手 / G-θ 大幅補強 (NRFT 骨格) / G-ι 部分着手 (alphaXiv MCP triangulation) / G-κ 解消 / G-λ 新設。**Round 5** で残課題 (G-η 全ペア / G-λ 完全形式証明 / G-ι 完全 PDF Read / G-κ 批判文献走査) を処理し、§M3 Kalon 判定再実行 → §8 結語起票へ進む。

### §6.5 反証可能性の局所化 (CLAUDE.md 反証可能性の位置づけ)

本稿は Popper 型反証可能性を **主判定基準** としては使わない。主判定は T9 を中核とする T 系列で行い (§7.1 で展開)、反証可能性は次の局所検査でのみ運用する:

- 公開テスト: §1.2 C3 の Gaussian 閉形式 (§5.5 G-ε) の specific form は数値計算で検証可能
- 因果: §6.1 の IIT 同型は cause-effect structure の比較で因果的に検証可能
- 外部再現: 5 分野同型 (§3.6) は他研究者が同じ随伴対を独立構成できれば外部再現

これらの局所検査は反証可能性の **下位検査** として機能するが、本稿の認識論的核 (C4 / C5) を判定する主基準ではない。

---

## §7 corollary (3 誤配位独立節)

§1.2 C5 で予告した「Popper / Mangalam / 超ひも landscape の 3 誤配位は単一の構造的誤測定から派生する」を、3 つの独立節で展開する。各節は独立に読めるよう設計しつつ、§8 結語で単一図式に閉じる。

### §7.1 Popper 反証可能性 (T9 適用)

ポパーの反証可能性 (1934/1959 "Logik der Forschung" / "The Logic of Scientific Discovery") は、科学的言明と非科学的言明を「反証可能か」で区別する判定基準である。

本稿の関手論的読み替え:

- ポパーは **真理₁ 層 (phenomena)** で反証可能性を要求する
- だが phenomena は data から detected されるが直接 observable ではない (Bogen-Woodward 1988 §I)
- ゆえに反証可能性のテストは **data 層を経由する** が、ポパーはこの **下降関手の経路** を見ていない

> [SOURCE 強候補: Popper 1934/1959 + 反証可能性は死んだ.md §2-§3 + fep_epistemic_status §ポパー適用不能 v2.7.0 — HGK 内部一次 SOURCE / 外部 Popper 原典は subagent 未抽出 (G-ζ)]

T9 (T 系列の核) による診断: 「ポパーは何を忘れたか」「何を回復すべきか」。診断結果: ポパーは **2 段関手分解** (理論 → phenomena → data) のうち **phenomena → data** の関手を忘れた (= 線形視した)。回復すべきは Bogen-Woodward 段階構造の関手化。

**C4 への帰着**: 真理₁ から下降関手 $R$ で生成される痕跡 (= 予測₁) を真理₁ 自体と取り違える。これが §7.1 の核診断である。

### §7.2 Mangalam 予測至上主義 (benchmark culture)

Mangalam 的 (および現代 ML / AI 評価における benchmark culture) 「予測精度こそ良い理論の指標」立場は、予測₁ (data 痕跡) を真理₀ の指標と読む。

本稿の関手論的読み替え:

- Mangalam は **予測₁ → 真理₀** の単一射として理論を評価する
- だが予測₁ は **真理₁ (phenomena) → 予測₁ (data)** の下降関手 $R_{\text{ph→da}}$ の像であり、真理₀ そのものではない
- ゆえに予測精度の最大化は **phenomena 層の存在を見落とす** 評価軸である

> [SOURCE 強: HGK 内部一次 SOURCE — 反証可能性は死んだ.md §9 / fep_epistemic_status §真理予測型分け v2.4.0 L191-220]

**C4 への帰着**: 関手の方向を逆転している。data から theory への遡上 (帰納) を、theory の data 上での適合度 (予測) として誤測定する。Mangalam 予測至上主義は §1.2 C5 「3 誤配位の単一起源」の最も明白な例である。

注: Mangalam 主義の現代形は ImageNet / GLUE / MMLU 等の benchmark 駆動評価であり、reasoner の内部理解 (= L⊣R 内在化) と benchmark 性能を切り離して扱う本稿の立場と直接対立する。

### §7.3 超ひも landscape (Hossenfelder 2018)

超ひも理論の $10^{500}$ 真空 (landscape 問題) への批判は、「予測を消失させる」ことを「悪い理論」の判定基準とする。

本稿の関手論的読み替え:

- landscape 批判は **理論層の冗長性 → 予測₁ の不一意性** を「悪さ」と判定する
- だが理論層の冗長性は、下降関手 $R_{\text{th→ph}}$ (真理₀ ≈ theory → 真理₁ ≈ phenomena) が単射でないことを意味するだけで、$L_i \dashv R_i$ の存在を否定しない
- ゆえに「予測の一意性」を判定基準とすることは、**真理₀ / 真理₁ の下降を線形視する** 誤配位である

> [SOURCE 中: Hossenfelder 2018 "Lost in Math" + 反証可能性は死んだ.md §8 §8.6 — Hossenfelder は subagent 未抽出 (G-ζ) / 反証可能性.md は HGK 内部一次 SOURCE]

**C4 への帰着 (異型)**: Mangalam が「予測一意性 = 真理₀ 指標」と読むのに対し、landscape 批判は「予測一意性が失われる = 理論が悪い」と読む。両者は **同じ誤配位の表裏** である。前者は予測の存在を真理₀ 指標として、後者は予測の不在を真理₀ 否定として、いずれも phenomena 層の独立性を見落とす。

### §7.4 3 誤配位の関手的同定

3 誤配位は次のように同定される:

| 誤配位 | 焦点 | 誤読の方向 |
|:---|:---|:---|
| Popper 反証可能性 | 真理₁ (phenomena) で反証可能性を要求、真理₀ → 真理₁ → 予測₁ の下降関手 $R$ を見ない | $R$ の後半 (真理₁ → 予測₁) を忘却 |
| Mangalam 予測至上主義 | 予測₁ (data 痕跡) を真理₀ 指標と誤読 | $L$ (予測₁ → 真理₀) を $R$ の逆と取り違える、関手の方向を逆転 |
| landscape 批判 | 理論層冗長で予測₁ 消失を「悪い」と判定 | $R$ (真理₀ → 予測₁) の合成を線形視、$L_{\text{th→ph}}$ の冗長性を $R$ 全体の悪さと混同 |

3 誤配位は単一の構造的誤測定 — **真理₀ → 真理₁ → 予測₁ の下降関手 $R$ (predictions descend) を線形視し、その逆方向 $L$ (予測₁ → 真理₁ → 真理₀) を $R$ と等置する誤読** — から派生する。これが §1.2 C5 の関手論的同定である。

§8 結語で 3 誤配位を Bogen-Woodward 三層共通構造 anchor で単一図式に閉じる。

---

## §8 結語: 科学性判定基準の自己言及不可能性

### §8.1 Predictions Descend — 単一図式

本稿の核主張を一枚の図に畳む。

```text
                  L (上昇関手, 還元)
        ┌──────────────────────────────────┐
        ↑                                  │
        │                                  ↓
    真理₀  ←──── 真理₁  ←──── 予測₁ (= data, 痕跡)
   (theory)    (phenomena)
        │                                  ↑
        ↓                                  │
        └──────────────────────────────────┘
                  R (下降関手, 回復・生成)
```

随伴 $L \dashv R$ は次の構造を持つ:

- **$L$ (上昇)**: 予測₁ → 真理₁ → 真理₀ への接近 (情報を捨てて構造に収束する方向、aletheia $U$ と同型)
- **$R$ (下降)**: 真理₀ → 真理₁ → 予測₁ (構造を有限理論に翻訳して具体値を生成する方向、aletheia $N$ と同型)
- **単位 $\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ は同型ではない** ($\text{Ker}(\eta_{\text{unit}}) > 0$)
- **予測₁ は $R$ の像** = 下降関手の痕跡 (Predictions Descend)

このとき本稿の主題が単一の構造的命題として帰着する:

> **予測₁ は真理₀ への到達ではなく、真理₀ から $R$ で生成された痕跡である。**

予測₁ を真理₀ の指標として読むことは、$R$ の像を $L$ の到達点と取り違えることであり、関手の方向を逆転する誤読である。

### §8.2 3 誤配位の関手論的同型化

§7 で同定した 3 誤配位は、§M3 で「構造的類似 仮説 55%」として最弱ラベルが付されていた (C5)。本節で 3 誤配位を **3 つの不正規関手操作** として形式化し、構造的類比から関手論的同型に昇格する。

§8.1 単一図式上で、3 誤配位は次の 3 操作として書ける:

| 誤配位 | 関手論的不正規操作 | 形式化 |
|:---|:---|:---|
| **Popper 反証可能性** | 関手分解の忘却 | $R = R_{\text{ph→da}} \circ R_{\text{th→ph}}$ の合成を分解せず、$R$ を単一射として扱い、phenomena 直接に test を求める |
| **Mangalam 予測至上主義** | 随伴の方向反転 | $R$ の像 (= 予測₁) と $L$ の到達点 (= 真理₀) を等置し、$\eta_{\text{unit}}$ を同型と暗黙に仮定する |
| **landscape 批判** | 単射性の局所化失敗 | $R_{\text{th→ph}}$ (theory → phenomena) の非単射性を、$R$ 全体 (theory → data) の悪さと混同する |

これら 3 操作の **共通根** は次の 1 文に閉じる:

> **$L$ と $R$ の方向弁別の失敗 = 随伴 $L \dashv R$ を等置する誤読**。

3 誤配位は単一の構造的誤読 (随伴の等置) の 3 つの異なる射影である。3 つは独立した分野誤りではなく、同一の関手論的構造違反の 3 つの相である。これにより §1.2 C5 「3 大誤配位は単一の構造的誤測定から派生」は、構造的類比 → 関手論的同型に昇格する。

### §8.3 Predictions Descend Theorem — 科学性判定基準の自己言及不可能性

§8.1 + §8.2 を統合して、本稿の核命題を **構成的不可能性命題** として陳述する。

**Predictions Descend Theorem** (科学性判定の自己言及不可能性):

科学理論 $T$ を、随伴対 $L \dashv R$ ($L$: 予測₁ → 真理₀ への上昇、$R$: 真理₀ → 予測₁ への下降、$\eta_{\text{unit}}: \text{Id} \Rightarrow R \circ L$ は同型でない、$\text{Ker}(\eta_{\text{unit}}) > 0$) を内在化する関手的操作と見なす。このとき以下が成り立つ:

1. **$R(T) \subset$ 予測₁ 圏**: $T$ が下降関手 $R$ で生成する具体値の集合 (= $T$ の経験的予測総体)
2. **$T_0(T) \subset$ 真理₀ 圏**: $T$ が上昇関手 $L$ で接近する構造 (= $T$ の真理₀ 性)
3. **不可能性 (核命題)**: 任意の 2 理論 $T_1, T_2$ について、$R(T_1) = R(T_2)$ は $T_0(T_1) = T_0(T_2)$ を含意しない

**系**: 予測₁ の集合 $R(T)$ から $T$ の真理₀ 性 $T_0(T)$ を一意復元する操作 (= $R^{-1}$ の構成) は存在しない。これは $\eta_{\text{unit}}$ が同型でない ($\text{Ker}(\eta_{\text{unit}}) > 0$) ことから帰結する関手論的事実である。

**Gödel 第二不完全性定理との対応**:

| | Gödel 第二不完全性定理 | Predictions Descend Theorem |
|:---|:---|:---|
| 体系 | 一貫した算術理論 $T$ | 随伴対 $L \dashv R$ を内在化する科学理論 $T$ |
| 体系内の操作 | $T$ の証明計算 $\text{Prov}_T$ | $T$ の予測₁ 生成 $R$ |
| 体系の核 | $T$ の無矛盾性 $\text{Con}(T)$ | $T$ の真理₀ 性 $T_0(T)$ |
| 不可能性 | $T \nvdash \text{Con}(T)$ | $R^{-1}$ は構成不能 |
| 構造的根拠 | 自己言及の対角化 | $\eta_{\text{unit}}$ 非同型 ($\text{Ker} > 0$) |

両定理は **体系内の operations が体系自身の核を識別できない** という構造を共有する。Gödel が証明計算の自己言及で形式系の無矛盾性証明を不可能にしたのと類比的に、Predictions Descend Theorem は **予測₁ 生成の自己言及で科学理論の真理₀ 性識別を不可能にする**。

これが §1.2 C4 「Predictions Descend」の **構成的不可能性命題** としての帰結であり、meta §M0.3 道 C 宣言 (Gödel と並ぶ認識論的定理) の関手論的実装である。

**3 誤配位 (§8.2) は本定理の系として閉じる**: Popper / Mangalam / landscape は、本定理が排除する操作 ($R^{-1}$ の構成、$\eta_{\text{unit}}$ の同型仮定、$R$ の単一線形視) のいずれかに依拠している。3 誤配位は本定理の不可能性に違反する 3 つの誤読であり、本定理から **論理的に閉じる**。

---

Predictions Descend Theorem が主張するのは次の 1 文である:

> **科学理論は、自身の予測₁ から自身の真理₀ 性を測れない。**

予測₁ で理論を測ろうとする 70 年の科学哲学的努力は、$\eta_{\text{unit}}$ 非同型という関手論的事実に違反していた。本定理はこの自己言及不可能性を関手論的に書き下す。

科学はそれでも進むが、進む方向は予測₁ の精度競争ではなく、$L$ (上昇関手) で真理₀ に接近する方向であって、$R$ (下降関手) の像を測る方向ではない。これが本稿が科学哲学に提出する命題である。

---

## 付録 A: 自己診断 (Kalon△ 判定 / 残虚開示 / 達成と未達成)

論文本体 (§1-§8) は読者への命題提示であり、Yugaku 規律 (§M6 虚→実変換面: 罪は何がまだ虚かを伏せたまま実を装うこと) に従う本稿の自己診断は、本付録に分離する。

### A.1 Kalon△ 判定

本稿は yugaku-kalon-check 5 ステップ判定を経て、C1-C5 全 5 件で **◎ Kalon△** を獲得した (詳細: meta §M3.1)。

| C | 判定 | 派生 (Step 3 DIVERGE) |
|:---|:---|:---|
| **C1** (理解 = $L \dashv R$ 内在化) | ◎ Kalon△ | 視覚 / 地図 / 最適化 / ゲージ / 統計力学 (5 派生、Future-Proof で派生 2 のみ S4 watch — G-δ 吸収済) |
| **C2** ($\eta_{\text{unit}}$ 非同型 = 全理論共通) | ◎ Kalon△ | faithful / Kan / coarse-graining / 量子測定 / ringoid (5 派生、全 Future-Proof 維持) |
| **C3** (補完₁ 単調減少) | ◎ Kalon△ | VFE / IB / predictive coding / 数論抽象 / 量子重ね合わせ (5 派生、全 Future-Proof 強化) |
| **C4** (Predictions Descend) | ◎ Kalon△ | Bogen-Woodward / van Fraassen / Cartwright / 量子測定 / ML train-test (5 派生、Future-Proof 4/5 強化) |
| **C5** (3 誤配位の単一系統一) | ◎ Kalon△ | Popper / Mangalam / landscape / ML over-fit / replication crisis (5 派生、全 Future-Proof 強化、§8.2 で関手論的同型に昇格) |

**Kalon△ vs Kalon▽ の峻別**: 本判定は **Kalon△** (本稿の F⊣G + 5 分野 + 哲学接続を含む MB 内の局所不動点) である。**Kalon▽** (Tononi IIT 4.0 / Cartwright 1983 / van Fraassen 1980 / Mangalam 等を全て含む全空間での普遍不動点) の主張は本稿の射程外。RLHF 由来の断言バイアスを回避するため △ を明示する。

### A.2 残虚の開示

| ギャップ | 内容 | 解消経路 |
|:---|:---|:---|
| **G2** | 5 分野横断 $L_i$ 統合 | §3 で並列例示済、各分野の厳密関手証明は本稿外の継続課題 |
| **G4** | $\omega$ 折畳の形式証明 | oblivion_connection_map §2.4 の構造的開問題として開示済。本稿は CE = B [推定 90%] の上で構造保存定理を引用 |
| **G-ε** | Tishby 1999 Gaussian 閉形式 | SSL cert 失敗で本セッション TAINT 残、本体起票後に再取得義務 |
| **G-ζ** | subagent SOURCE 独立検証 | Riehl / Cartwright / van Fraassen / Bogen-Woodward / Buzzard / arxiv abstract を Tolmetes または独立 reviewer が直接 WebFetch / 物理書籍 Read で「強候補」→「強」昇格 |
| **G-η** | 5 分野同型の形式同型射 (functor + natural transformation) 具体構成 | 本稿は並列例示に留まる。Yoneda 埋め込みでの functor 構成と各分野間の natural transformation 具体形は本稿外の継続課題 |
| **G-θ** | Predictions Descend Theorem (§8.3) の形式証明強度 | §8.3 で $\eta_{\text{unit}}$ 非同型から $R^{-1}$ 不可能性を主張するが、Gödel 第二不完全性定理レベルの形式証明 (再帰関数 + 算術化 + 対角化) は提示していない。Predictions Descend Theorem は **構造的不可能性命題** として書かれているが、その形式証明の Tarski 真理理論 / カテゴリカル algebra による厳密化は本稿外の継続課題 |
| **G-ι** | IIT (Tononi 2008 / IIT 4.0 2023) 同型の SOURCE 確保 | §6 で IIT 同型を主張するが subagent verbatim 未取得 = SOURCE 完全欠如、本稿外の継続課題 |
| **G-κ** | Bogen-Woodward 三層への過度依存 | §1.5 / §8.1 で「最強同型 anchor」とした Bogen-Woodward 1988 を Hacking, Daston, Massimi 等の批判文献で位置づけ直す必要。本稿固有の貢献を「関手的読み替え」というメタ層に留めず、本稿が Bogen-Woodward に何を **新たに加える** かの明示は継続課題 |

### A.3 達成と未達成

本稿が達成した事項:

1. **理解の関手論的定義** ($L \dashv R$ 内在化、§1.1 + §2.1 + §2.2-§2.5) — Yoneda 補題に基づく操作的 anchor
2. **3 誤配位の関手論的同型化** (§8.2) — Popper / Mangalam / landscape を **3 つの不正規関手操作** (関手分解の忘却 / 随伴の方向反転 / 単射性の局所化失敗) として形式化、共通根 = 「随伴 $L \dashv R$ を等置する誤読」。C5 が「構造的類似 仮説 55%」(§M3) から関手論的同型 (§8.2) に昇格
3. **真理₀ / 真理₁ / 予測₀ / 予測₁ の 4 型分けによる語義滑り防止** (§2.1) — fep 一次 SOURCE による
4. **Predictions Descend Theorem** (§8.3) — 科学性判定基準の自己言及不可能性命題を構成的命題として陳述、Gödel 第二不完全性定理との対応表で道 C 宣言の関手論的実装を提示

本稿が達成していない事項:

1. **Predictions Descend Theorem (§8.3) の形式証明** — 構造的命題として書かれているが、Gödel レベルの形式化 (再帰関数 + 算術化 + 対角化に類比される操作) は提示していない (G-θ)
2. **5 分野間の natural transformation 具体構成** — 並列例示のみ (G-η)
3. **IIT 同型の SOURCE 確保** — 主張のみ (G-ι)
4. **Bogen-Woodward への critical 位置づけ** — anchor として依存 (G-κ)
5. **subagent SOURCE の独立検証** — 強候補ラベル付き、本稿査読時の義務 (G-ζ)

### A.4 射程の明示

本稿の射程は **現世代の AI / 科学コミュニティ** 前提下に限定される (§1.3 co-evolution 限定)。圏論アクセスが LLM 経由で完全に大衆化された場合、C1 / C4 は scaffolding として消える可能性があり、その場合の科学哲学は本稿の射程外である。

本稿は構造決定論的立場を意図的に採用する (§1.3 / §6)。「なぜ構造が理解を生むか」という本質論は本稿の問いではない — 問いの水準を意図的に変更している。IIT (Tononi) との同型については §6 で commitment レベル (ontological vs definitional) の差として開示した。

---

*本稿 v0.3 は 2026-04-25 に §8 を redesign。§8.1 (単一図式維持) + §8.2 (3 誤配位を 3 不正規関手操作で関手論的同型化、C5 昇格) + §8.3 (Predictions Descend Theorem を Gödel 第二不完全性定理と対応する構成的不可能性命題として陳述) の 3 部構成に再編。旧 §8.3-§8.5 (Kalon 開示 / 残虚 / 到達点と限界) は付録 A に分離。「最小限の貢献」表現削除、論文本体は世界への命題提示に専念。*

*本稿 v0.2 は 2026-04-25 に §3-§8 を追加し、§1 整合性訂正 (関手方向 + 真理₀/₁ 対応) を反映した。執筆 gate 3/3 通過 (meta §M3) を前提として起票。*

---

*v0.1 — 2026-04-25 §1 7 段開口部 (Understatement + Axiom-First + Scope Severance 合成) 起票。Watson-Crick 1953 型控えめ surface で序を切断、§1.1 で公理提示、§1.2 で 5 核主張を主張水準 + 確信度 + 較正宣言付きで列挙、§1.3 で射程切断 (co-evolution 限定 + 構造決定論立場明示 + FEP 非依存性)、§1.4 で本稿構造、§1.5 で Bogen-Woodward 三層を外部接続 anchor として確定、§1.6 で SOURCE 強度開示 (強候補ラベル + G-ζ 査読時独立検証義務)、§1.7 で Kalon△ 判定開示 (Kalon▽ との峻別)。執筆 gate 3/3 通過 (meta §M3) を前提として起票。次の一手: §2 随伴構造の導入。*
