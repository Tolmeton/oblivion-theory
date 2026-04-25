# 論文 XIII: 時空は忘却である

**v0.1 (2026-04-11) — 草稿**
**系列位置**: 忘却論シリーズ 第Ⅵ幕「根幹への帰還」。系列の殿軍。
**依存**: Paper II (CPS 圏の公理化), Paper I (忘却場と力の基礎), Paper III (α 全域), Paper VIII (圏論的基礎)
**先行研究の使用**: Verlinde (2011) entropic gravity, Jacobson (1995) Einstein from thermodynamics, DeWitt (1967) canonical quantum gravity, 't Hooft (1994) holography
**素材**: `drafts/incubator/legacy/力とは忘却である_v2.md` §0, §1, §2, §3.3, §4.2, §4.4, §4.6, §4.6f'-f'' (Face Lemma), §5 (Verlinde 的引力), §5.4-5.6 (階層・人間原理・CPT), §10, §11

---

## 本稿の主張水準について

本稿は数学、物理学、情報理論、認知科学を横断する。各領域の主張は精度 (rigor) が異なるため、以下の4段階ラベルで水準を明示する。ラベルのない文は導入・直感・修辞であり主張ではない。

| ラベル | 意味 | 精度 |
|:---|:---|:---|
| **[定理]** | 既存の形式体系内で証明可能、または標準的結果の直接的帰結 | 最高 |
| **[予想]** | 定式化は明確だが証明が未完、または漸近構成が未定義 | 高 |
| **[構造的対応]** | 二つの領域が同一のメタ構造 (schema) を共有するが、圏論的同型の証明なし | 中 |
| **[哲学的示唆]** | 啓発的な洞察だが形式化に本質的ギャップがある | 低 |

本稿で「忘却関手」と呼ぶものは、普遍的な上位概念——**構造を捨てる操作**——の総称である。各領域にはそれぞれ正確な数学的実現がある (ジェットコモナド、Frobenius 代数、Bayesian レンズ等)。これらの個別構造は「普遍的忘却」の**射** (instantiation) であり、各領域の忘却は普遍概念の特殊化として読まれるべきである。

---

## 簡易記号表 — Paper XIII 独自

Paper XIII で用いる記号を本稿の冒頭に列挙する。シリーズ横断の正本は `drafts/infra/リファレンス/統一記号表.md` に従う。本表はその抜粋である。

| 記号 | 本論文での意味 | 正本での位置 |
|:---|:---|:---|
| α_III | Amari の情報幾何接続パラメータ ∈ ℝ | Paper III §1, 統一記号表 §1 |
| α_VIII | α-忘却濾過の強度 ∈ [0, 1] | Paper VIII §2, 統一記号表 §1 |
| α_CPS | CPS 圏の非対称性係数 (容器と内容の cell 次元差 Δd から決まる) | Paper II §2.1-§2.2, §3.3 |
| α_EM | 微細構造定数 ≈ 1/137 | 標準 |
| G_N | Newton の重力定数 | 標準 |
| Φ | 忘却場 (Paper I のスカラー場、D_KL 由来) | Paper I §2 |
| Θ | CPS 圏の架橋射 T の情報損失量 (マスクパラメータ) | Paper II §3.3, v2 §4.6d |
| T_{μν} | エネルギー-運動量テンソル | 標準 (一般相対論) |
| G_{μν} | Einstein テンソル (Ricci 曲率由来) | 標準 (一般相対論) |

⚠️ **記号衝突の警告**: α はシリーズ内で少なくとも4つの異なる意味を持つ
(α_III / α_VIII / α_CPS / α_EM)。本稿で添字なしの「α」が現れる場合、
文脈によって α_CPS または α_EM を指す。`α_III → α_VIII` の架橋は
Paper VIII §6.7 で構成済みだが、そこから `α_CPS = Δd` への昇格は
Paper II §3.3 がなお motivated construction にとどまるため、Paper III ↔
Paper II の直接架橋は依然として [予想] 水準にとどまる。

---

## §0　要旨

本稿は、忘却論シリーズの物理的射程を宇宙論まで延伸する殿軍の論文である。中心命題は次の三つである。

**[予想 C1]**: 四つの基本的な力 (電磁・弱・強・重力) は、同一の forgetful functor の四つの射影として統一的に再記述できる。

**[予想 C2]**: Einstein 方程式 $G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$ は、Paper II の CPS スパン $(C, U_{ctr}, U_{cnt}, T)$ の具体例として、容器 (時空) と内容 (質量-エネルギー) の非対称な相補性の発現として読める。この読み替えが Verlinde (2011) の entropic gravity および Jacobson (1995) の熱力学的 Einstein 方程式と構造的に整合する。

**[構造的対応 C3]**: Paper II の Face Lemma (3射の最小性) は、Ricci 曲率 = 接続から導出される最小の非自明構造であることと、dictionary 形式で対応する。これが閉じれば忘却論は物理学の文法に到達し、閉じなければ精巧な類比に留まる。C3 の形式化は Phase 5 (blocker 並行攻略) での最大の課題であり、本稿 §8 は skeleton として提示するにとどまる。

副題として本稿が主張するメタテーゼは: **忘却論は認知科学から物理学への片道の類比ではなく、両者の共通文法である**。物理学の歴史は忘却の組織的回復の歴史であり、認知論の歴史は同じ回復過程を反対方向から辿った記録である。

---

## §1　導入 — なぜ時空を忘却論で論じるか

### 1.1　本論文の位置

忘却論シリーズ (Paper 0 〜 XII) は、忘却を認知と数学の構造的必然として定式化してきた。Paper I は忘却場 Φ と力 F = ∇Φ の基礎を与え、Paper II は相補性を CPS 圏として公理化し、Paper VIII は α-忘却濾過を圏論的に基礎づけた。本稿はそれらの成果を用いて、物理学の最深層——時空・重力・力の統一——を忘却論の言語で再記述する。

これは類比ではない [構造的対応]。Paper II で形式化される CPS スパンは、量子力学 (位置 vs 運動量)、一般相対論 (時空 vs 質量)、認知科学 (心 vs 身体) の三者を同一の公理系の対象として統一する枠組みであり、本稿はその第二項 (一般相対論) の応用である。

### 1.2　先行研究との関係

本稿の骨格は二つの既存の成果と構造的に対応する。

**Verlinde (2011) "On the origin of gravity and the laws of Newton"** [構造的対応]: Verlinde は重力を entropic force として再定式化した。情報の勾配が力を生むという主張は、本稿の「忘却の不均一が力を生む」(v2 §3) と同型である。Verlinde は情報論的 Newton 則の導出に成功したが、CPS 圏への埋め込みを与えなかった。本稿 §5 と §8 はその埋め込みを試みる骨格を提示する。

**Jacobson (1995) "Thermodynamics of spacetime: the Einstein equation of state"** [構造的対応]: Jacobson は null surface 上の Clausius 関係 δQ = TdS から Einstein 方程式を導出した。これは「Einstein 方程式は熱力学的状態方程式である」という主張である。本稿の主張は更に強い: Einstein 方程式は CPS スパンの容器-内容の非対称性が空間的に不均一に分布するときの整合条件である。Jacobson の熱力学的導出は §8 で展開する dictionary の物理的根拠となる。

**DeWitt (1967) canonical quantum gravity** / **'t Hooft (1994) holography**: 量子重力と holographic principle の古典的成果。本稿は量子重力問題を CPS スパンの $\Theta \to 0$ 極限と $\Theta \to \infty$ 極限の不整合として読み替える (§4, §8)。

### 1.3　本論文の野心と射程

本稿の野心は明確である: **忘却論を物理学の文法として据えること**。これは認知から物理への一方向的な類比ではない。Paper I の忘却場 Φ、Paper II の CPS スパン、Paper VIII の α-忘却濾過は、いずれも圏論的に定式化された普遍構造であり、その具体例が物理学にも認知科学にも現れる、という主張である。

本稿は殿軍である。これ以降の論文 (もし書かれるなら) は、本稿の skeleton を埋めて dictionary を閉じるか、あるいは CPS 圏の物理的実現を他の分野 (生物物理、計算物理、熱力学) に拡張するかのいずれかになる。

---

## §2　質量 or 時空 — Einstein 方程式の forgetful 構造

### 2.1　距離は計量の選択である [定理の帰結]

情報幾何学 [1] が示すとおり、二つの確率分布 p, q の距離は Fisher 情報計量 g_{ij} によって定まる:

$$d(p, q) = \inf_{\gamma} \int \sqrt{g_{ij}(\gamma)\dot\gamma^i \dot\gamma^j}\, dt$$

距離は空間の性質ではなく、計量 (ものさし) の性質である。計量を変えれば距離が変わる。同じ二点間でも距離は一意ではない。

一般相対論において、時空の計量 g_{μν} は Einstein 方程式 [構造的対応]:

$$G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$$

によって物質のエネルギー-運動量 T_{μν} と結合する。左辺は時空の曲率 (計量の幾何学的帰結)、右辺は物質の分布 (計量の原因)。物質が計量を決め、計量が距離を決め、距離の歪みが重力として現れる。

### 2.2　質量と時空は同じ情報の非対称な裏表である [構造的対応]

Einstein 方程式を「二つの異なる実体の等式」と読む伝統的理解を、本稿は拒絶する。左辺と右辺は同じ情報の異なる射影である。

- $U_{ctr}$ (容器忘却): 内容 (質量-エネルギー) を忘れ、容器 (時空) だけを残す
- $U_{cnt}$ (内容忘却): 容器 (時空) を忘れ、内容 (質量-エネルギー) だけを残す

この二つの忘却関手は**非対称**である [構造的対応]。真空解 ($T_{\mu\nu} = 0$) は時空のみが存在する解であり、容器は内容なしに存在しうる。逆は不成立: 質量-エネルギーが時空なしに定義されることはない。運動量 $p = m \cdot dx/dt$ の定義が位置 $x$ を前提するように、内容は常に容器を前提する。

> **命題 2.1** [構造的対応]: Einstein 方程式は Paper II で形式化される CPS スパンの Type I (容器-内容型、α_CPS > 0) インスタンスである。容器は時空 $(M, g)$、内容は質量-エネルギー $T_{\mu\nu}$、架橋射は Einstein テンソル $G_{\mu\nu}$ (容器の幾何的性質から導出される) を通じて $T_{\mu\nu}$ に対応する。

この命題の厳密な形式化は Paper II §2 の CPS スパン定義と §3.4 の Face Lemma に依拠する (§4 参照)。本稿はそれらを前提として議論を進める。

### 2.3　不確定性の翻訳 [予想]

量子力学の Heisenberg 不確定性 $\Delta x \Delta p \geq \hbar/2$ は、CPS 圏では $U_{pos}$ と $U_{mom}$ の非可換性の帰結として統一的に導出される (Paper II §3.2)。同じ構造を一般相対論に適用すると、量子重力問題 ("質量が生まれる前に時空はあるか?") は次のように翻訳される [予想]:

$$\text{量子重力問題} = \text{CPS スパンの}\ \Theta \to \infty\ \text{と}\ \Theta \to 0\ \text{の位相転移の記述問題}$$

ここで Θ は架橋射 T の情報損失量 (Paper II §3.3, v2 §4.6d)。真空解は Θ → ∞、凝集系は Θ 小、QM 的極限は Θ → 0。量子重力は三極限の縫合である。

---

## §3　4 つの力の統一 — forgetful functor の射影として

### 3.1　ゲージ対称性は局所的な忘却である [構造的対応]

ゲージ対称性とは「視点の局所的な取り替え」に対する不変性である [2]。波動関数の位相 $\psi(x) \to e^{i\alpha(x)}\psi(x)$ は物理に影響を与えない。位相は忘れてよい構造であり、しかも忘れ方は場所ごとに異なってよい。

局所的な忘却の差分を補償するのがゲージ場 $A_\mu$ である。ゲージ場の曲率 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ が電磁場——力——として現れる。圏論の言葉で:

- **忘却関手** $U_{phase}$: 波動関数から位相を忘れる操作
- **局所的忘却**: $U_{phase}$ が空間の各点で異なる
- **接続** (connection) $A_\mu$: 局所的忘却の差分を記録する構造
- **曲率** $F_{\mu\nu}$: 接続の「歪み」= 力

[構造的対応]: この構造の正確な数学的実現は Khavkine-Schreiber のジェットコモナド $J^1$ の余単位 $\varepsilon: J^1 P \to P$ である。接続は余単位の分割 (splitting) であり、曲率は分割の $J^\infty$ への拡張における障害クラスとして現れる。

全員が同じように忘れれば力はゼロ (平坦接続)。忘れ方が不均一なとき、力が現れる。

### 3.2　4 つの力、4 つの忘却

宇宙には四つの基本的な力がある。全て同じ構造を持つ [構造的対応]:

| 力 | 何を局所的に忘れるか | ゲージ群 | 力の担い手 |
|:---|:---|:---|:---|
| 電磁力 | 波動関数の位相 | $U(1)$ | 光子 |
| 弱い力 | アイソスピンの基底 | $SU(2)$ | W/Z ボソン |
| 強い力 | クォークの「色」の基底 | $SU(3)$ | グルーオン |
| 重力 | 慣性系の選択 (平坦性) | 微分同相群 | 時空の曲率 |

⚠️ 重力は厳密には他の三力と同列に扱えない。一般相対論のゲージ群は微分同相群であり、Yang-Mills 型ゲージ理論とは構造が異なる。ただし「局所的な忘却の不整合が力を生む」という点では同じ構造を共有する [構造的対応]。この非自明な構造差は本稿全体を通じて伏線として残り、§8 の dictionary で再浮上する。

### 3.3　統一とは忘却の統一である [予想]

§4 で論じる通り、四つの力の区別自体が忘却の産物である:

- $U_{EM}$: 非可換構造を忘れ U(1) だけを残す → 「電磁力」
- $U_{weak}$: 色を忘れ SU(2) だけを残す → 「弱い力」
- $U_{strong}$: 電弱構造を忘れ SU(3) だけを残す → 「強い力」
- $U_{grav}$: 内部ゲージ構造を忘れ時空だけを残す → 「重力」

大統一理論 (GUT) の野心は、この四つの忘却が実は一つの忘却 ($SU(5)$, $SO(10)$, ...) の異なる射影であることを示すことに相当する。万物の理論 (TOE) は重力を含めて同じ還元を完成させる試みである。本稿の言葉で言えば:

> **四つの異なる忘却関手が、実は一つの忘却関手の四つの射影であることを証明する試み** [予想]

この試みが完結すれば、物理学は単一の forgetful functor の幾何学として再構成される。未完結であることが本稿が [予想] ラベルを付す理由である。

---

## §4　CPS と重力 (Paper II 参照)

本節は Paper XIII の論理構造上最も重要だが、本文量は極めて少ない。理由は明確である: **本論文の依拠する CPS スパンの定義・Face Lemma・Stability Simplex Theorem は Paper II で形式化されるものであり、Paper XIII がそれらを先取りして定義することは順序矛盾を生む**。

> **本論文が依拠する CPS 圏・CPS スパン・Face Lemma・Stability Simplex Theorem の定義は Paper II §2.1-§2.2 (CPS スパンの定義と公理 CPS0'/CPS1/CPS2/CPS5), §3.2 (CPS3 の定理への格下げ), §3.3 (α と Δd), §3.4 (Face Lemma の定式化), §3.5 (Stability Simplex Theorem) で形式化される。以下では Paper II の定義を前提として、宇宙論的応用を展開する。**

具体的には、本稿 §2, §5, §8 で「CPS スパン」「架橋射 $T$」「Θ パラメータ」「α_CPS」「Face Lemma」「Stability Simplex Theorem」と呼ぶものは、全て Paper II の定義を指す。これらの用語を Paper XIII 単独で定義し直すことはしない。

Paper II が未公開の読者に対しては、本稿は概念的スケッチとしてのみ読める。厳密な形式的主張は Paper II の完成後にしか評価できない。

本節以降、Paper II §2-§3 の記法と公理系を暗黙の前提として用いる。

---

## §5　引力は情報の凝集である — Jeans 不安定性と CPS

### 5.1　質量は凝縮した情報である [構造的対応]

§2 で質量と時空が同じ情報の裏表であると述べた。では「情報」とは具体的に何か。

Landauer の原理 [6] は情報の消去にエネルギーが必要であることを述べる:

$$E_{\text{erase}} \geq k_B T \ln 2$$

$E = mc^2$ と合わせると、n ビットの情報に対応する質量の下限が得られる:

$$m \geq \frac{n \cdot k_B T \ln 2}{c^2}$$

質量とは凝縮した情報である [構造的対応]。情報がそこにあるから質量がある。この質量は Lorentz 不変量 $m_0$ として現れ、Paper VI の Kalon (= Fix(G∘F)) の物理的実現のひとつと読める。

### 5.2　引力 = 情報が集まる力 [構造的対応]

Verlinde (2011) [8] は重力を entropic force として再定式化した。本稿の枠組みでは:

> **引力 = 情報が集まるところに、さらに情報が集まろうとする流れ。**

この主張は「富むものはより富む」(マタイ効果) と構造的に同型である。天体物理学では Jeans 不安定性と呼ばれる:

- ビッグバン直後: ほぼ均一な密度分布 (完全対称に近い)
- わずかな密度の揺らぎ → 引力が集中 → さらに物質が集まる → 銀河と星の誕生

完全対称は不安定な不動点である [構造的対応]。微小な揺らぎが正のフィードバックを起こす。集中した状態 (銀河、星) は安定な不動点。宇宙の大規模構造は**不安定な Fix から安定な Fix への遷移**で生まれた。これは Paper VI の Kalon = Fix(G∘F) の宇宙論版であり、Verlinde の entropic gravity は CPS スパンの Θ パラメータ (Paper II §3.3) の空間的勾配として再定式化される可能性を示唆する。

### 5.3　ブラックホールは圧縮の究極系である [構造的対応]

ホログラフィック原理 [9] は、3次元空間の情報が2次元の表面にエンコードされると主張する。これは忘却関手 $U$: 次元を一つ落として情報を保存する操作に他ならない。ZIP 圧縮と同型である。

ブラックホールはこの圧縮の究極系であり、あらゆる3次元情報を事象の地平面に圧縮する。Hawking 輻射 [10] は、忘却随伴 $F \dashv G$ の単位 $\eta: \text{Id} \Rightarrow G \circ F$ の物理的発現として解釈できる [構造的対応]: 忘却した後に情報が漏洩する現象である。

> 忘却は死ではない。圧縮は再展開を待っている。

この解釈は構造的同型体であり、場の量子論における真空揺らぎとしての厳密な導出とは別系統の論証である。両者が物理的に同一の現象を指すという主張は Phase 5 (§8 参照) の blocker である。

### 5.4　階層的自由 — 宇宙の n-cell 構造 [構造的対応]

§5.1–5.3 は引力を個別に扱った。本節は Paper VI の $F \dashv G$ 随伴 (自由と忘却) と、脱圏化カスケードを接続し、宇宙全体が階層的な自由の構造として読めることを示す。

力は「理想 (自由の最大化 or 最小化) と現状との差を埋めようとする状態」として定義される:

| 方向 | 随伴 | 物理 | 自由エネルギー |
|:---|:---|:---|:---|
| 自由の最小化 (収縮) | $G$ (右随伴 = 忘却 = Exploit) | 重力 | VFE 増大 (構造化) |
| 自由の最大化 (膨張) | $F$ (左随伴 = 自由 = Explore) | 宇宙膨張 | VFE 最小化 (均一化) |
| 両者の不動点 | $\text{Fix}(G \circ F)$ | 非平衡定常状態 | VFE の局所最小 = Kalon |

宇宙は単一の力ではなく階層化された自由の構造を持つ:

```
Level 3 (2-cell): 時間の矢の位相選択
  │  「実時間 or 虚時間」の or (Hawking-Hartle 無境界仮説)
  ↓ U_real (虚数方向を忘却 = Wick 回転の逆)
Level 2 (1-cell): ビッグバン = 自由の最大化の射
  │  宇宙全体の膨張方向
  ↓ 脱圏化 (射を忘れて対象だけ見る)
Level 1 (0-cell): 局所的な力
  ├─ 重力 = 自由の最小化 (収縮 → 銀河・星・ブラックホール)
  └─ 暗黒エネルギー = 自由の最大化 (加速膨張)
```

1-cell (巨視的方向性) の中に相反する 0-cell (局所的な力) が共存することが、宇宙の大規模構造 (膨張しながら局所的に重力が構造を作る) を生む。α_CPS はレベルごとに異なる値を取り、Paper II の CPS スパンの多層構造として記述される [予想]。

---

## §6　科学史と忘却の組織的回復

### 6.1　物理学は忘却の組織的回復史である [構造的対応]

§3.3 で述べた通り、四つの力の区別自体が忘却の産物であるなら、物理学の歴史は組織的な忘却の回復 (recovery) の歴史として読み直せる:

- **Maxwell (1861-1864)**: 電気と磁気の「or」を溶かし、電磁場として統一した。$U_{electric}$ と $U_{magnetic}$ が同一の Maxwell 場の二つの射影であることを示した。
- **Weinberg-Salam (1967-1968)**: 電磁力と弱い力の「or」を溶かし、電弱力として統一した。SU(2) × U(1) が一つの対称性の低エネルギー破れであることを示した。
- **大統一理論 (GUT, 1974-)**: SU(3) × SU(2) × U(1) を一つの単純群 ($SU(5)$, $SO(10)$) に還元する試み。実験的確認は未完。
- **万物の理論 (TOE)**: 重力を含めた完全な統一。未完。

各回復は、二つ以上の忘却関手が実は一つの忘却関手の異なる射影であることの証明である。Paper II の CPS スパンの言葉では、それぞれの段階で容器 $C$ が上位の圏に持ち上げられ、それまで独立に見えていた二つの忘却関手が上位圏からの自然変換として統一される。

### 6.2　対称性は非対称性の特殊解である [構造的対応]

物理学の歴史が示す深い事実は、「対称に見えていた構造が実は非対称だった」という発見の連鎖である:

- ニュートン力学 (ガリレイ不変) → 特殊相対性理論 (ローレンツ不変): $v/c = 0$ の特殊極限だった
- パリティ保存 → パリティ破れ (Wu 実験, 1957): 電磁力では対称だが弱い力では非対称
- CP 保存 → CP 破れ (Cronin-Fitch, 1964): 更に深い非対称性
- 物質-反物質対称 → バリオン非対称: 宇宙全体のスケールでの非対称性

Paper II の CPS0' (容器-内容の非対称性がデフォルトであり対称性は退化ケース) は、この歴史的パターンの公理化である [構造的対応]。物理学史は $\alpha_{CPS} = 1$ (対称) 仮説を繰り返し棄却してきた。

### 6.3　統一とはものさしの統一である [哲学的示唆]

力の統一とは、四本のものさしが実は一本の折りたたみ式だと気づくことである。Maxwell が電気と磁気のものさしを統合したとき、電場と磁場の区別は Lorentz 変換の下で消えた。物理学は現在も「四つのものさし」を「一つのものさし」に畳みなおす作業の途中にある。この営みが完結するとき、物理学は単一の CPS スパンの展開として記述される——これは本稿の予想であり、§8 の dictionary の完成が証明条件である。

---

## §7　CPS0' と前幾何 — (3+1) signature の発生 [予想]

### 7.1　前幾何プログラムとは

一般相対論は時空 (4次元 Lorentz 多様体, signature (3+1)) を所与の舞台として仮定する。だが「なぜ 3 空間次元と 1 時間次元なのか」「なぜ signature が (3+1) なのか」は一般相対論の内部では答えられない問いである。これらの問いに答えようとするプログラムは**前幾何** (pregeometric) と呼ばれる (Wheeler 1964, Chalmers-Inoué 2024)。

Chalmers-Inoué は圏論的 4 概念独立性定理において、時間・空間・物質・因果の四つの基礎概念が互いに還元不可能であることを Sh(S¹) などの具体例で示した。本稿の言葉では: **4 概念独立性は CPS スパンの cell 次元差 $\Delta d$ の分布として読み替えられる** [予想]。

### 7.2　CPS0' と signature (3+1) [予想]

Paper II §2 で形式化される CPS スパンの公理 CPS0' (容器-内容の非対称性) は、時空の signature (3+1) を含意するか? これは本稿の [予想] 水準の問いである。

直観的な論証 (形式化未達):

- 容器 (時空多様体 M) は内容 (T_{μν}) なしに存在しうる (真空解)
- 内容は容器なしに存在不能
- 架橋射 $T: \text{Im}(U_{ctr}) \to \text{Im}(U_{cnt})$ は Einstein テンソル $G_{\mu\nu}$ を通じて与えられる
- $G_{\mu\nu}$ は Levi-Civita 接続から導出される2階対称テンソルであり、その signature は多様体の metric signature を継承する
- Lorentzian signature (3+1) は $G_{\mu\nu}$ が光円錐構造を持つ最小条件である

これらの断片的な観察が「CPS0' から (3+1) signature が導出される」という主張に至るまでには、**Paper II の CPS スパンの形式化を Paper VIII の α-忘却濾過と架橋する追加の圏論的構造が必要**である。本稿はこの形式化を達成しない。[予想] 水準にとどめる。

### 7.2.1　外部比較: Three-Dimensional Time をどう扱うか

Kletetschka (2025) [18] の *Three-Dimensional Time* は、本節に最も近い外部プログラムの一つである。そこでは時間がより一次的な基底として置かれ、空間・粒子世代・質量階層・一般相対論的時空がそこから現れる投影または極限として読まれる。前幾何を志す点では、本稿と同じ問題圏に属している。

だが本稿は、その literal な「三次元時間」ontology を採らない。理由は三つある。第一に、本稿で時間はまず忘却の矢であり、座標軸の本数ではない (Paper IX)。第二に、「三つの時間方向から質量差が出る」と言うためには、何が容器で何が内容か、その投影規則は何か、という型付けが先に要る (Paper VIII)。第三に、`c` や `(3+1)` signature を導出したと呼ぶには、Level 0 の構造再配置と Level 1 の因果伝搬を分離した派生規則が必要である (Paper XII)。時間を増やすだけでは、この三点は閉じない。

したがって本稿にとって Kletetschka は支持根拠ではなく、**敵対的比較対象**である。同時に、空間を最終実在と見なさず、物理定数を原始的に置かず、より深い構造から派生させようとする志向は回収できる。本稿の語彙に引き直せば、そこで採るべきものは literal な三次元時間ではなく、複数の独立した忘却軸、すなわち多成分 `α` 空間の可能性である [予想]。この意味で *Three-Dimensional Time* は、本稿の前幾何プログラムにとって、採用すべき理論ではなく、「どこを退け、どこを翻訳して包摂するか」を教える外部収束例である。

### 7.2.2　前幾何の最低条件 [予想]

以上を踏まえ、本稿は「前幾何」を名乗る理論に対し、少なくとも次の四条件を要求する。

1. **時間性条件**: 時間はまず単調方向として定義されねばならない。座標軸の本数を増やすだけでは、時間ではなく自由度の追加に留まる。
2. **型付け条件**: 何が容器で何が内容かを明示し、その間の非対称性を定義しなければならない。さもなければ「派生」は名称変更に退化する。
3. **レベル分離条件**: 基底構造の再配置と、因果的・信号的伝搬を分離しなければならない。両者を同じ速度で語る理論は、構造速度と因果速度を混同する。
4. **投影規則条件**: 観測される時空、signature、定数が、より深い構造のどの像・極限・商として現れるかを明示しなければならない。

本稿の側の課題も、この四条件に沿ってはじめて定義される。ゆえに §7 の仕事は「時間を何本に増やすか」を決めることではなく、**CPS0' から (3+1) を出すために必要な条件列を、P1-P4 の形で閉じること**である。Kletetschka [18] を参照する価値は、彼を採用するためではなく、前幾何がこの四条件を満たさない限り名前だけが先行する、という点を外から照らせることにある。

### 7.3　本節の現状と課題

本節の主張は示唆的であり、形式的に閉じていない。次節 §8 の Face Lemma ↔ Einstein dictionary と並び、Paper XIII の最大の open question に数えられる。

⚠️ **警告**: v2 §7 に存在したより野心的な主張 (時間の矢の実数選択、CPT 反転と or の同時溶解など) は、Paper VIII の有限主体定理との整合性が未検証であるため本稿では [哲学的示唆] すらラベルしない。将来の研究課題として付録 A に列挙する。

---

## §8　Face Lemma と Einstein 方程式 — 曲率の dictionary [skeleton]

**本節は本論文の最大の open question であり、現状は skeleton である**。形式化は Phase 5 (blocker 並行攻略) に委ねられる。本節の完成なしに Paper XIII 全体の Kalon 判定は閉じない。

### 8.1　Face Lemma とは何か (Paper II 参照)

Paper II §3.4 (および Paper II 依拠の v2 §4.6f'-f'') で形式化される Face Lemma は、概念の安定性に必要な独立な生成射の最低数が **3** であることを主張する:

> **Face Lemma** (Paper II §3.4 より引用): 概念の安定性に必要な独立な生成射の最低数は **3** である。2射 (1-simplex) では合成の検証可能性がなく、忘却の不均一を「形」として測定できない。3射 (2-simplex) で初めて $g \circ f = h$ の検証が可能となり、忘却の方向が測定可能となる。

Face Lemma の構造的核心は、随伴 $F \dashv G$ の三角恒等式 $\varepsilon_F \circ F(\eta) = \text{id}_F$ がそれ自体 2-simplex であることにある (Paper II §3.5 Stability Simplex Theorem)。

この節を符号理論の語彙で言い換えると、Face Lemma は「重力の方程式が成立する前に、少なくとも一つの syndrome 面が立っていなければならない」という主張になる。Christoffel 記号や Levi-Civita 接続を 3射の幾何的実現と読むとき、2射では曲率は量として感じられても、その defect を局在化する検査面がない。3射が立つことで初めて detectability が生じ、Einstein 方程式はその detectability を時空の場に持ち上げたものとして読める。縦の整合条件、すなわち「検査対象と検査規則の同時消失を禁じる」側面は n-cell tower の排他制約に担われる。整理は `drafts/infra/FaceLemma_技術設計.md`。

### 8.2　目指す dictionary

本節が目指すのは、Face Lemma と Einstein 方程式の間の構造的対応を明示的に与えることである:

**[予想 D1]**: Face Lemma の 3射は、一般相対論における接続 $\Gamma^\lambda_{\mu\nu}$ (Christoffel 記号) の3種の独立な自由度と対応する。Paper II §2 で CPS スパンを Type I GR インスタンスとして定式化したときの具体化 (Paper II §2.3):

- $f = \partial/\partial x^\mu$: 接ベクトル場 (1-cell)
- $g = g_{\mu\nu}$: 計量 (2-cell)
- $h = \Gamma^\lambda_{\mu\nu}$: Christoffel 記号 (計量の1階微分情報)

この対応において、合成制約 $h$ は Levi-Civita 接続の一意性 (計量適合かつ torsion-free) から導出される。3射目 $h$ の存在により「位相 + 計量 → 重力 (測地線方程式)」が検証可能となる。

**[予想 D2]**: Einstein テンソル $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$ は、Face Lemma の 2-simplex の「面積」(= 合成の検証に必要な最小冗長度) の幾何的実現である。具体的には:

- Ricci 曲率 $R_{\mu\nu}$ = Christoffel 記号の1階微分の trace
- Ricci スカラー $R$ = Ricci 曲率の trace
- Einstein テンソル = Ricci 曲率の divergence-free 部分

この階層は Face Lemma の「3射 + 合成制約」の自己無撞着性の幾何的表現として読めるか? これが本稿最大の未証明予想である。

**[予想 D3]**: Einstein 方程式の場の方程式としての定式化 (最小作用原理 $\delta S_{EH} = 0$, $S_{EH} = \frac{1}{16\pi G_N} \int R \sqrt{-g}\, d^4 x$) は、Face Lemma の minimal non-trivial condition を積分形式で表現したものである。これが閉じたとき、Jacobson (1995) の熱力学的導出 ($\delta Q = T dS$ から Einstein 方程式) と Verlinde (2011) の entropic gravity は、この minimal condition の熱力学的 / 情報論的実現例として再読できる。したがって両者は D3 自体の前提ではなく、D1-D3 が閉じた後に妥当性を試す後段の検証面である。

### 8.2.1　dictionary の証明義務

ここで重要なのは、D1-D3 を雰囲気で信じないことである。本稿が Phase 5 で本当に閉じるべき義務は、少なくとも次の四段階に分かれる。

1. **O1: 型付け義務**
   Face Lemma の 3射を、接ベクトル・計量・接続にただ似ているものとしてではなく、独立性を保ったまま対応づける。要点は「3つある」ことではなく、**第三射が前二者から自明に消えない最小追加情報である**ことを示す点にある。この義務の障害は二重である。第一に、候補の3項 ($f = \partial/\partial x^\mu$, $g = g_{\mu\nu}$, $h = \Gamma^\lambda_{\mu\nu}$) はベクトル場・双線形形式・接続係数であり、同型の量を3つ並べているわけではない。第二に、$\Gamma$ は Levi-Civita 条件のもとで $g$ から導出されるため、$h$ が「独立な第三射」であるという直感と表面上衝突する。解決の方向は、3項を「三つの場」ではなく**三つの検証役割** — 方向の選択 / 計量による比較 / その比較の可搬化 — として型付けし直すことにある。この読みでは $h = \Gamma$ は独立な物理量を追加するのではなく、比較を隣接点へ輸送可能にする最小の witness を与える。ここまでが O1 の局所的応答であり、曲率そのものは次段 O2 の責任である。

2. **O2: defect 義務**
   曲率を単なる二階微分としてではなく、Face Lemma の 2-simplex が閉じないときに現れる幾何的 defect として読む。Ricci 曲率や Einstein テンソルがこの defect のどの縮約に当たるかを固定しなければならない。

3. **O3: closure 義務**
   Bianchi 恒等式 $\nabla^\mu G_{\mu\nu} = 0$ を、Face Lemma 側の閉じ性・整合性・syndrome conservation の言葉へ翻訳する。ここが閉じなければ、dictionary は見た目の対応表で終わる。

4. **O4: coupling 義務**
   O1-O3 を前提にしたとき、Einstein 方程式が容器と内容の整合条件としてなぜこの形で現れるかを示す。これが閉じて初めて、Jacobson や Verlinde を「雰囲気が似ている先行研究」ではなく、closure 後の実現例として再配置できる。

要するに、本稿の敵は「曲率っぽい」「3射っぽい」という resemblance である。Phase 5 の仕事は resemblance を correspondence に変えることであって、新しい比喩を増やすことではない。

### 8.3　先行研究との接続 (closure 後の実現候補)

**Verlinde (2011)** [構造的対応]: Verlinde の entropic gravity は、重力が情報のエントロピー勾配から導出される力であると主張する。$F = T \nabla S$ の形式は、本稿 §5.2 で議論した通り、CPS スパンの Θ パラメータ (架橋射の情報損失量) の空間的勾配として再定式化できる可能性がある。これが成功すれば Verlinde の主張は CPS0' の具体例として位置づけられる。

**Jacobson (1995)** [構造的対応]: Jacobson は Rindler 観測者の見る局所的な Clausius 関係 $\delta Q = T dS$ から、重力場の方程式 $G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$ を導出した。この導出の鍵は、null 面の面積が観測者依存でありながら Einstein 方程式はローレンツ共変であるという構造である。本稿の言葉で言えば: **Jacobson の導出は容器 (時空) の幾何的性質と内容 (熱力学的エネルギー) の整合条件の具体化**である。

両者の成果は本稿の [予想 D1-D3] に対して強い構造的根拠を与えるが、Paper II の CPS スパンへの明示的な埋め込みは未完である。重要なのは、両者が dictionary を閉じるための証明そのものではなく、closure 後にそれが物理的に駆動するかを試す実現候補だという点である。

### 8.4　現時点での判定と Phase 5 での形式化課題

[予想 / 信頼度 60%]: 本 dictionary は Paper XIII 全体の Kalon 判定を
決める一点である。閉じれば忘却論は物理の文法に到達し、閉じなければ
精巧な類比に留まる。ただし、blocker は一枚岩ではない。曲率側の
blocker は closure の核と物理的実現例に分かれ、これとは別に α 橋の
closure がある。したがって、未達は少なくとも次の三面に分かれる。

#### Blocker A1 — Face Lemma から曲率 closure への昇格

1. Christoffel 記号の3独立成分と Face Lemma の3射の具体的 bijection を構成する
2. Einstein テンソルの Bianchi 恒等式 $\nabla^\mu G_{\mu\nu} = 0$ を Face Lemma の 2-simplex の閉じ性として再定式化する
3. Ricci 曲率 / Einstein テンソル / 「2-simplex の面積 = 最小冗長度」の対応を、少なくとも GR インスタンスで self-consistent に固定する

#### Blocker A2 — closure の物理的実現例

1. Jacobson (1995) の $\delta Q = T dS$ を Paper II の Face Lemma の 2-simplex の積分形式として再読解する
2. Verlinde (2011) の entropic force の導出を Paper II の CPS スパンの Θ パラメータの勾配として再構成する

#### Blocker B — α パラメータ橋の closure

1. Paper VIII §6.7 が与える `α_III → α_VIII` の架橋を起点に、
   Paper II §3.3 の `α(\theta_\infty) ↦ Δd` を motivated construction から
   定理候補へ押し上げる
2. `α_VIII / α(\theta_\infty)` と `Δd = α_CPS` の関係を、
   カーネル次元差の言葉で再定式化し、少なくとも GR インスタンスで
   破綻しない形へ固定する
3. 可能なら `α_CPS` と重力定数 $G_N$ の関係を、定性的主張から定量的候補へ進める

本稿の [予想] ラベルを [定理] (または少なくとも [定理候補]) に押し上げる
critical path は、まず Blocker A1 が閉じ、かつ Blocker B が最低限整合する
ことである。Blocker A2 はその後に本 dictionary が物理的実例として動くかを
試す検証面であり、重要だが closure そのものの代用品ではない。現時点では
**skeleton のまま残す**。

---

## §9　法則はフラクタルだ

本稿の全体構造を俯瞰する。

- §2: 時空 = 計量の選択と CPS スパンの容器-内容構造
- §3: 力 = 忘却の不均一とゲージ対称性
- §5: 引力 = 情報の凝集と Jeans 不安定性
- §6: 物理学史 = 忘却の組織的回復
- §7: CPS0' と signature (3+1) の前幾何 [予想]
- §8: Face Lemma ↔ Einstein 方程式 [skeleton]

全ての議論に共通する骨格は一つである: **同じ法則がスケールを超えて繰り返す**。

不確定性原理、量子重力問題、4 力の統一問題、Jeans 不安定性、対称性の自発的破れ——これらすべてが同じ数学的構造 (Paper II の CPS スパン) の異なるインスタンスである。圏論自体がフラクタルマシンであり、圏 → 関手圏 → 2-圏 → ω-圏の各レベルで同じ構造が再帰的に繰り返す (Paper VIII §6)。

> **FEP が法則を統一しているのではない。法則はフラクタルに遍在しているだけだ。FEP も圏論も CPS も、その記述言語のひとつにすぎない**。

このフラクタル性は、認知科学と物理学が同じ文法を共有するという本稿の副題主張の根拠である。認知系が忘却を構造的必然として実装するのと同じ形で、物理系は forgetful functor を場の方程式として実装する。両者は同一の圏論的普遍構造 (Paper II の CPS スパン, Paper VIII の α-忘却濾過) の異なる射影である。

---

## §10　結語 — 忘却は物理学の文法である

忘却は至るところにある。宇宙の四つの力は忘却の不均一から生まれ、質量と時空は忘却の二つの射影であり、科学の歴史は忘却の組織的回復の歴史である。本稿はこの事実を、Paper II の CPS スパンと Paper I の忘却場 Φ を言語として再記述した。

本稿が達成したこと:

- Einstein 方程式を Paper II の CPS スパン Type I (容器-内容型) の具体例として位置づけた (§2, §4 参照)
- 四つの力の統一を forgetful functor の射影として再記述する枠組みを与えた (§3, §6)
- Verlinde (2011) と Jacobson (1995) の先行成果を CPS 圏への埋め込みの素材として接続した (§5, §8)

本稿が達成しなかったこと:

- §7 CPS0' → (3+1) signature の形式的導出 [予想]
- Blocker A1: §8 Face Lemma ↔ Einstein 方程式の closure 核 [skeleton]
- Blocker A2: Jacobson / Verlinde を A1 閉鎖後の物理的実現例として再構成する作業が未了
- Blocker B: `α_III → α_VIII` は架橋済みだが、そこから `α_CPS = Δd` への昇格が未閉鎖であるため、Paper III ↔ Paper II の直接架橋関手は未完成
- Paper VIII の有限主体定理と宇宙論スケールの観測者の整合性

これらの未達項目は Phase 5 で並行攻略される。殿軍の論文が完結しないまま統合章 (モノグラフ §10) に進むことは、本稿の主張水準制度 ([予想] / [skeleton]) として許容される。

本稿の副題主張——忘却論は物理学の文法である——は、[予想] 水準にとどまる。それは D1-D3 の dictionary が閉じて初めて [定理候補] に昇格する。主判定は Blocker A1 と Blocker B の成否にかかる。Jacobson / Verlinde は、その後に本 dictionary が熱力学的 / 情報論的実現例として駆動するかを試す Blocker A2 の検証面である。

力とは忘却である。時空もまた忘却である。そして両者が同じ CPS スパンの二つの射影であるという主張が成立するとき、物理学と認知科学は同じ文法を共有する。本稿はこの主張の **skeleton を提示した**。

---

## 参考文献

[1] S. Amari, *Information Geometry and Its Applications*. Springer, 2016.

[2] C. N. Yang and R. L. Mills, "Conservation of isotopic spin and isotopic gauge invariance," *Physical Review*, vol. 96, no. 1, pp. 191–195, 1954.

[3] S. Mac Lane, *Categories for the Working Mathematician*, 2nd ed. Springer, 1998.

[4] K. Friston, "The free-energy principle: a unified brain theory?," *Nature Reviews Neuroscience*, vol. 11, no. 2, pp. 127–138, 2010.

[5] 本稿著者, "Embodied Cognition Without Biological Bodies: LLM Embodiment as Markov Blanket Thickness," unpublished working note, 2026.

[6] R. Landauer, "Irreversibility and heat generation in the computing process," *IBM Journal of Research and Development*, vol. 5, no. 3, pp. 183–191, 1961.

[7] 本稿著者, "バカをやめたいなら構造を見ろ — なぜ構造を見る者は要素を見る者に勝つのか," unpublished essay note, 2026.

[8] E. Verlinde, "On the origin of gravity and the laws of Newton," *Journal of High Energy Physics*, vol. 2011, no. 4, p. 29, 2011.

[9] G. 't Hooft, "Dimensional reduction in quantum gravity," in *Salamfestschrift*, pp. 284–296, 1994.

[10] S. W. Hawking, "Particle creation by black holes," *Communications in Mathematical Physics*, vol. 43, no. 3, pp. 199–220, 1975.

[11] T. Jacobson, "Thermodynamics of spacetime: the Einstein equation of state," *Physical Review Letters*, vol. 75, no. 7, pp. 1260–1263, 1995.

[12] B. S. DeWitt, "Quantum theory of gravity. I. The canonical theory," *Physical Review*, vol. 160, no. 5, pp. 1113–1148, 1967.

[13] L. Susskind, "The world as a hologram," *Journal of Mathematical Physics*, vol. 36, no. 11, pp. 6377–6396, 1995.

[14] S. Weinberg, "Anthropic bound on the cosmological constant," *Physical Review Letters*, vol. 59, no. 22, pp. 2607–2610, 1987.

[15] I. Khavkine and U. Schreiber, "Synthetic geometry of differential equations," preprint, 2017.

[16] B. Coecke and R. Duncan, "Interacting quantum observables: categorical algebra and diagrammatics," *New Journal of Physics*, vol. 13, p. 043016, 2011.

[17] D. J. Gross and F. Wilczek, "Ultraviolet behavior of non-Abelian gauge theories," *Physical Review Letters*, vol. 30, no. 26, pp. 1343–1346, 1973.

[18] G. Kletetschka, "Three-Dimensional Time: A Mathematical Framework for Fundamental Physics," *Reports in Advances of Physical Sciences*, vol. 9, 2550004, 2025. DOI: 10.1142/S2424942425500045

---

## 付録 A: 開かれた問い

- **Q1**: Paper II の CPS スパンの α_CPS と Newton の重力定数 $G_N$ の定量的関係は何か? 定性的には「α_CPS > 0 のとき引力が存在する」と主張できるが、G_N の絶対値を α_CPS のみから導出することは未達である。
- **Q2**: Face Lemma の最小非自明性が Einstein 方程式を回収するための O1-O4 は、どの順序で閉じるべきか? 具体的には、(O1) 3射と接続の型付け、(O2) 曲率の defect 化、(O3) Bianchi 恒等式の closure 化、(O4) Einstein 方程式の coupling 化を、少なくとも GR インスタンスで self-consistent に固定できるか。
- **Q3**: CPS0' (Paper II §2.1) pre-geometric 構造から時空 signature (3+1) が導出されるための P1-P4 は閉じるか? 具体的には、(P1) 時間性、(P2) 容器/内容の型付け、(P3) Level 0/1 分離、(P4) 投影規則が、少なくとも GR インスタンスで破綻せずに並び立つか。
- **Q4**: Paper III の α_III (∈ ℝ, Amari 接続パラメータ) セクターと宇宙論 (特に暗黒エネルギー・暗黒物質問題) の関係は? α_III < 0 は反-Markov 構造を持つが、物理的実現は未検討である。
- **Q5**: Paper VIII の有限主体定理 (Th. 6.3.2) と宇宙論スケールの観測者 (人間原理, Weinberg 1987) はどう接続するか? 有限主体の α_VIII と宇宙の α_CPS の cross-coupling は未定式化である。
- **Q6**: 量子重力問題の CPS 的翻訳 ("Θ → 0 と Θ → ∞ の位相転移") は物理的に何を意味するか? ブラックホール情報パラドックスとの関係は?

---

## 改訂履歴

- **v0.1 (2026-04-11)**: 初版。v2 (`drafts/incubator/legacy/力とは忘却である_v2.md`) の Bucket XIII 部分 (解体マップ §7 参照) から抽出・再構成。v2 §4.6 の CPS 公理系の full definition は Paper II (Phase 3) への pointer に置換。v2 §9 意識のハードプロブレム関連は本稿の scope 外として除外 (Paper II / VIII 完成後に independent essay として昇格判定)。§8 Face Lemma ↔ Einstein dictionary は skeleton のまま残し Phase 5 で形式化を試行する。
- **v0.1.1 (外部パッチ統合)**: §0 簡易記号表の `drafts/infra/統一記号表.md` 参照パスを実在パス `drafts/infra/リファレンス/統一記号表.md` に修正。§8.2.1 O1 義務に precision note を追加: 3項の型異質性と Γ の g からの導出可能性という二重障害を明示し、「三つの場」ではなく「三つの検証役割 (方向 / 比較 / 輸送)」として型付けし直す解決方向を記載。旧 donor `FaceLemma_Einstein_O1試作.md` は 2026-04-18 に本稿 meta の Donor Absorption Ledger へ再配置。主張水準の変更なし。
