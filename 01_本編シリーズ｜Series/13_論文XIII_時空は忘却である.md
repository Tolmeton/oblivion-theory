# 論文 XIII: 時空は忘却である

**v0.1 (2026-04-11) — 草稿**
**系列位置**: 忘却論シリーズ 第Ⅵ幕「根幹への帰還」。系列の殿軍。
**依存**: Paper II (CPS 圏の公理化), Paper I (忘却場と力の基礎), Paper III (α 全域), Paper VIII (圏論的基礎)
**先行研究の使用**: Verlinde (2011) entropic gravity, Jacobson (1995) Einstein from thermodynamics, DeWitt (1967) canonical quantum gravity, 't Hooft (1994) holography
**素材**: `01_草稿｜Drafts/07_インキュベータ｜Incubator/legacy/力とは忘却である_v2.md` §0, §1, §2, §3.3, §4.2, §4.4, §4.6, §4.6f'-f'' (Face Lemma), §5 (Verlinde 的引力), §5.4-5.6 (階層・人間原理・CPT), §10, §11

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

Paper XIII で用いる記号を本稿の冒頭に列挙する。シリーズ横断の正本は `01_草稿｜Drafts/08_インフラ｜Infra/references/統一記号表.md` に従う。本表はその抜粋である。

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

ここでいう自由は、全微視状態の個数ではない。有限主体または局所記述にとって、区別・配置・回復がどれだけ開かれているかである。したがってブラックホールは Bekenstein-Hawking entropy を最大化しうるが、外部観測者にとっては局所回復可能性と配置自由を極小化する。これは「情報が消える」という主張ではなく、情報が境界へ圧縮され、局所的には回復不能になるという忘却論的読みである。

同様に、ビッグバンは自由最大化された状態ではない。ここで言うのは、ビッグバン / 宇宙膨張が自由最大化へ向かう射だということである。単一の初期境界から、距離・領域・履歴・局所差異が展開される。つまり大域的な $F$ 型の射が宇宙を開き、その内部で局所的な $G$ 型の射が物質を畳む。

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

**本節は本論文の最大の open question であり、現状は skeleton である**。ただし、O3/O4 については §8.2.2 の局所実験により、完全な空白ではなくなった。形式化は Phase 5 (blocker 並行攻略) に委ねられる。本節の完成なしに Paper XIII 全体の Kalon 判定は閉じない。

### 8.1　Face Lemma とは何か (Paper II 参照)

Paper II §3.4 (および Paper II 依拠の v2 §4.6f'-f'') で形式化される Face Lemma は、概念の安定性に必要な独立な生成射の最低数が **3** であることを主張する:

> **Face Lemma** (Paper II §3.4 より引用): 概念の安定性に必要な独立な生成射の最低数は **3** である。2射 (1-simplex) では合成の検証可能性がなく、忘却の不均一を「形」として測定できない。3射 (2-simplex) で初めて $g \circ f = h$ の検証が可能となり、忘却の方向が測定可能となる。

Face Lemma の構造的核心は、随伴 $F \dashv G$ の三角恒等式 $\varepsilon_F \circ F(\eta) = \text{id}_F$ がそれ自体 2-simplex であることにある (Paper II §3.5 Stability Simplex Theorem)。

この節を符号理論の語彙で言い換えると、Face Lemma は「重力の方程式が成立する前に、少なくとも一つの syndrome 面が立っていなければならない」という主張になる。Christoffel 記号や Levi-Civita 接続を 3射の幾何的実現と読むとき、2射では曲率は量として感じられても、その defect を局在化する検査面がない。3射が立つことで初めて detectability が生じ、Einstein 方程式はその detectability を時空の場に持ち上げたものとして読める。縦の整合条件、すなわち「検査対象と検査規則の同時消失を禁じる」側面は n-cell tower の排他制約に担われる。整理は `01_草稿｜Drafts/07_インキュベータ｜Incubator/FaceLemma_技術設計.md`。

### 8.2　目指す dictionary

本節が目指すのは、Face Lemma と Einstein 方程式の間の構造的対応を明示的に与えることである:

ただし、この dictionary は同一性命題ではない。外部一次文献が支えるのは、connection / parallel transport / curvature / holonomy / Bianchi closure / thermodynamic realization の各型であり、Face Lemma そのものではない。Ambrose-Singer [23] は曲率と holonomy の関係、Schreiber-Waldorf [24] と Baez-Schreiber [25] は parallel transport / higher transport の functorial typing、Navarro-Navarro [26] と Dadhich [27] は Einstein tensor / Lovelock 系の divergence-free projection を支える。これらを Paper XIII が SOURCE として使えるのは、Face Lemma の外部証明としてではなく、`raw defect / contracted defect / conserved coupling projection` の危険度つき辞書を組む範囲に限られる。

**[予想 D1]**: Face Lemma の 3射は、一般相対論における接続 $\Gamma^\lambda_{\mu\nu}$ (Christoffel 記号) の3種の独立な自由度と対応するのではなく、方向 / 比較 / 輸送という三つの検証役割に対応する候補である。Paper II §2 で CPS スパンを Type I GR インスタンスとして定式化したときの具体化 (Paper II §2.3):

- $f = \partial/\partial x^\mu$: 接ベクトル場 (1-cell)
- $g = g_{\mu\nu}$: 計量 (2-cell)
- $h = \Gamma^\lambda_{\mu\nu}$: Christoffel 記号 (計量の1階微分情報)

この対応において、合成制約 $h$ は Levi-Civita 接続の一意性 (計量適合かつ torsion-free) から導出される。したがって $\Gamma$ を独立な第三射そのものと読むことはできない。3射目 $h$ の役割は、計量比較を隣接点へ可搬化する witness として、「位相 + 計量 → 重力 (測地線方程式)」の検証面を立てる点にある。

**[予想 D2, 改訂形]**: Face Lemma の 2-simplex は、Einstein テンソルそのものに直読してはならない。曲率側の対応は少なくとも三層に分ける必要がある:

- Riemann 曲率 / holonomy = raw geometric defect
- Ricci 曲率 $R_{\mu\nu}$ と Ricci スカラー $R$ = raw defect の縮約
- Einstein テンソル $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu}R$ = 内容へ結合可能な divergence-free projection

この階層全体が、Face Lemma の「3射 + 合成制約」の自己無撞着性を、幾何的 defect から保存型 coupling projection へ落とす過程として読めるか? これが本稿最大の未証明予想である。

**[予想 D3]**: Einstein 方程式の場の方程式としての定式化 (最小作用原理 $\delta S_{EH} = 0$, $S_{EH} = \frac{1}{16\pi G_N} \int R \sqrt{-g}\, d^4 x$) は、D2 の三層分離を積分形式で支える minimal non-trivial condition である。これが閉じたとき、Jacobson (1995) の熱力学的導出 ($\delta Q = T dS$ から Einstein 方程式) と Verlinde (2011) の entropic gravity は、この minimal condition の熱力学的 / 情報論的実現例として再読できる。したがって両者は D3 自体の前提ではなく、D1-D3 が閉じた後に妥当性を試す後段の検証面である。

### 8.2.1　dictionary の証明義務

ここで重要なのは、D1-D3 を雰囲気で信じないことである。本稿が Phase 5 で本当に閉じるべき義務は、少なくとも次の四段階に分かれる。

1. **O1: 型付け義務**  
   Face Lemma の 3射を、接ベクトル・計量・接続にただ似ているものとしてではなく、独立性を保ったまま対応づける。要点は「3つある」ことではなく、**第三射が前二者から自明に消えない最小追加情報である**ことを示す点にある。この義務の障害は二重である。第一に、候補の3項 ($f = \partial/\partial x^\mu$, $g = g_{\mu\nu}$, $h = \Gamma^\lambda_{\mu\nu}$) はベクトル場・双線形形式・接続係数であり、同型の量を3つ並べているわけではない。第二に、$\Gamma$ は Levi-Civita 条件のもとで $g$ から導出されるため、$h$ が「独立な第三射」であるという直感と表面上衝突する。解決の方向は、3項を「三つの場」ではなく**三つの検証役割** — 方向の選択 / 計量による比較 / その比較の可搬化 — として型付けし直すことにある。この読みでは $h = \Gamma$ は独立な物理量を追加するのではなく、比較を隣接点へ輸送可能にする最小の witness を与える。ここまでが O1 の局所的応答であり、曲率そのものは次段 O2 の責任である。

2. **O2: defect 義務**  
   曲率を単なる二階微分としてではなく、Face Lemma の 2-simplex が閉じないときに現れる幾何的 defect として読む。Riemann / holonomy、Ricci / scalar、Einstein tensor が、raw defect、contracted defect、conserved coupling projection のどの層に当たるかを固定しなければならない。

3. **O3: closure 義務**  
   Bianchi 恒等式 $\nabla^\mu G_{\mu\nu} = 0$ を、Face Lemma 側の閉じ性・整合性・syndrome conservation の言葉へ翻訳する。ここが閉じなければ、dictionary は見た目の対応表で終わる。

4. **O4: coupling 義務**  
   O1-O3 を前提にしたとき、Einstein 方程式が容器と内容の整合条件としてなぜこの形で現れるかを示す。これが閉じて初めて、Jacobson や Verlinde を「雰囲気が似ている先行研究」ではなく、closure 後の実現例として再配置できる。

要するに、本稿の敵は「曲率っぽい」「3射っぽい」という resemblance である。Phase 5 の仕事は resemblance を correspondence に変えることであって、新しい比喩を増やすことではない。

### 8.2.2　局所 closure 実験の現在地 [構造的対応]

本節は skeleton である。ただし、§8.2.1 の O3/O4 は完全な空白ではない。以下の E-XIII-C3 番号は内部検証台帳の番号であり、外部読者向けの根拠そのものではない。外部 SOURCE としては、FLRW / perfect fluid / Bianchi / Einstein tensor の標準的計算を Carroll [19]、static spherical fluid probe を Tolman [20] と Oppenheimer-Volkoff [21]、local horizon thermodynamics を Jacobson [11] に置く。局所 symbolic run は、これら標準設定を本稿の記号・index convention で再計算した内部 SOURCE である。忘却論的な container/content 読みは、これら SOURCE からの INFERENCE として分ける。

| 実験 | 対象 | 得られた支持 | 残る境界 |
|:---|:---|:---|:---|
| E-XIII-C3-02 | Bianchi closure | Carroll [19] の標準 GR 接地を背景に、Face Lemma は raw defect の detectability、contracted Bianchi identity は projected defect の closure / conservation、Einstein tensor は conserved coupling projection と読むのがよい | Bianchi identity は Face Lemma そのものではない |
| E-XIII-C3-03/04a | flat FLRW + perfect fluid | Carroll [19] の FLRW / perfect fluid / conservation を接地に、$G_{00} \leftrightarrow \rho$、$G_{ii}/a^2 \leftrightarrow p$、$\nabla T=0$ は $\rho' + 3H(\rho+p)=0$ を与える。O4 は標準 GR source と symbolic run の二重支持を得る | 高対称 case。係数と作用原理は未導出 |
| E-XIII-C3-04b | static spherical perfect fluid / TOV | Tolman [20] と Oppenheimer-Volkoff [21] を接地に、$G^t_t \leftrightarrow \rho(r)$、$G^r_r \leftrightarrow p(r)$、$\nabla T=0$ は $p'(r)+(\rho+p)\Phi'(r)=0$ を与える。FLRW の slot coincidence だけではない | static spherical perfect fluid に限る。異方性は 04d で別検査 |
| E-XIII-C3-04d | static spherical anisotropic stress | TOV 型の同じ容器で $T^\mu_\nu=\mathrm{diag}(-\rho,p_r,p_t,p_t)$ と置くと、$G^r_r \leftrightarrow p_r(r)$、$G^\theta_\theta=G^\phi_\phi \leftrightarrow p_t(r)$、$\nabla T=0$ は $p_r'+(\rho+p_r)\Phi'+2(p_r-p_t)/r=0$ を与える | static spherical diagonal stress に限る |
| E-XIII-C3-04e | stationary spherical radial heat flux probe | stationary + diagonal metric で $T^t_r,T^r_t\neq 0$ を許すと、off-diagonal Einstein slot は消え ($G^t_r = G^r_t = 0$)、Einstein matching は $q=0$ を強制する。一方で energy-flux conservation $\nabla_\mu T^\mu_t = 0$ は $q' + 2q\Phi' + 2q/r = 0$ を与え、$(r^2 e^{2\Phi} q)' = 0$ (steady-state conserved redshifted radial flux) と等価。Probe (i) は単純 PASS でも単純 FAIL でもなく、ansatz 選択の structural 境界を露出した | static + diagonal metric では非対角 flux を Einstein side に乗せられない。cross-term $g_{tr}$ metric (Eddington-Finkelstein 系、04f) または Probe (ii) shear stress (04g) が next。一般の shear / 非球対称は依然として未検査 |
| E-XIII-C3-04c | Jacobson-style local patch | Jacobson [11] では local Rindler horizon、heat flux、area response、Raychaudhuri focusing、conservation + Bianchi closure が一つの局所物理的導出経路に並ぶ | entropy-area proportionality と local equilibrium は仮定。Face Lemma の証明ではない |

この実験群から得られる最小の修正は、D2 の直読を捨てることである。Einstein tensor を Face Lemma の raw defect と読むと、Schwarzschild exterior のような vacuum curvature を処理できない。したがって現時点の対応は次の三層に分けるべきである。

```text
Riemann / holonomy  = raw geometric defect
Ricci / scalar      = contracted defect
Einstein tensor     = conserved coupling projection
```

この読みでは、Bianchi 恒等式は Face Lemma の比較面そのものではない。Face Lemma は defect が露出する最小の comparison surface を与え、Bianchi 恒等式はその defect を内容へ結合可能な divergence-free projection へ制約する。ここまでが O3 の局所支持である。

O4 については、FLRW、TOV、anisotropic TOV が三つの試金石を与える。FLRW では density / pressure の tensor slot が一致し、TOV では radial pressure gradient が容器側の radial potential に制約される。anisotropic TOV では radial pressure と tangential pressure が分かれても、保存式に $2(p_r-p_t)/r$ という異方性項が露出する。さらに Jacobson (1995) は、heat flux が local causal horizon に相対化され、area response と Raychaudhuri focusing と conservation / Bianchi closure を通じて Einstein 方程式へ至る局所物理的経路を与える。これは C2/C3 の橋をかなり強くするが、Face Lemma の 3射最小性を証明するものではない。

したがって現時点の最大主張は次である。

> **[構造的対応]** Face Lemma ↔ Einstein dictionary は、O3/O4 について局所支持を持つ。すなわち、raw defect / contracted defect / conserved coupling projection の三層分離、FLRW / TOV / anisotropic TOV における content slot 対応、Jacobson 型の local horizon thermodynamics は、C2/C3 の容器-内容 coupling を一つの局所文法として読むことを支持する。ただし、係数 $8\pi G_N$、Einstein-Hilbert 作用、entropy-area input、一般の非対角 flux / shear、一般 GR case は未閉鎖であり、C3 は定理ではない。

### 8.2.3　Ricci 曲率と Weyl 曲率の分解、曲率発散の Open Question [skeleton]

§8.2.2 の三層分離 (Riemann/holonomy = raw defect、Ricci/scalar = contracted defect、Einstein テンソル = conserved coupling projection) は、Ricci 曲率側に対応する三層である。これに対し、Riemann 曲率の標準分解 (Carroll [19] 第 3 章) は、Ricci 曲率部分と Weyl 曲率部分 (= Riemann の trace-free 部分) の和として表される。Weyl 曲率を §8.2.2 三層分離のどこに住まわせるかは本稿で明示的に扱われておらず、本節はこの空席を Open Question として起票する。

**[skeleton] 四分岐拡張候補**:

```text
Riemann / holonomy   = raw geometric defect
  ├─ Ricci / scalar       = contracted defect  (内容に結合可能な縮約部分)
  │   └─ Einstein tensor  = conserved coupling projection  (Bianchi-divergence-free)
  └─ Weyl tensor          = trace-free residue  (内容に結合不可能な残差) [open]
```

これは §8.2.2 の三層分離を、Riemann の標準分解 (Ricci 部分 + Weyl 部分) に沿って **四分岐** へ拡張する候補である。Ricci 側は物質テンソル $T_{\mu\nu}$ と Einstein 方程式で結合する縮約された defect、Weyl 側は結合に乗らない trace-free な幾何 defect 残差 — として位置づける読みである。

**未閉鎖の三つの Open Question** (詳細はメタデータ §M6 Open Question Ledger 参照、読者向け概要は付録 A Q8-Q10):

- **OQ-DIV**: 欠損 cocycle $\kappa$ から、曲率発散に対応する非負観測量を定義できるか。Paper XIV §5.3 路線 2 (λ-依存弱*連続測度族 $\mu_\lambda$) を延伸して、$\kappa$ の有界性 / 非有界性を区別する観測量を構成する必要がある。連続側で $\kappa$ がそもそも well-defined になる前提 (Paper XIV Open C) 自体が未閉
- **OQ-WEY**: Weyl 曲率を縮約されない生の幾何 defect 残差として定式化できるか。§8.2.2 三層分離を四分岐へ拡張する候補。Penrose (1979) Weyl Curvature Hypothesis (Weyl 増大 = エントロピー増大方向 = 熱力学的時間方向) と Paper IX (エントロピーは忘却である) の接続候補
- **OQ-ALPHA**: 局所 $\alpha(x) \to 1$ と曲率不変量 $K = R^{abcd} R_{abcd} \to \infty$ を結ぶ写像はあるか。Paper VIII §6.2.3 (iii) の $\alpha = 1 \Rightarrow C_1 = C_{\text{disc}}$ を点ごとに変動する場 $\alpha(x)$ として読む候補

**最小実験候補 — Schwarzschild と FLRW の対比**:

| 時空 | Ricci 側 | Weyl 側 | Kretschmann スカラー $K$ |
|:---|:---|:---|:---|
| Schwarzschild (vacuum BH) | $R_{\mu\nu} = 0$ | Weyl $\neq 0$ (潮汐) | $K \sim 1/r^6 \to \infty$ at $r=0$。**Weyl 側で発散** |
| FLRW (等方的・等質的宇宙) | $R_{\mu\nu} \neq 0$ | Weyl $= 0$ (等角平坦) | ビッグバン特異点で Ricci 発散。**Ricci 側で発散** |

§8.2.2 三層分離を四分岐に拡張するなら、これら二つの発散型が忘却論的にどう異なる事象として読まれるかを区別できなければならない。これが OQ-WEY の実化判定条件 (b) である。

**現時点の主張水準**: [skeleton]。本節は §8.2.2 を Weyl 方向に拡張するための設計図に留まる。Paper XIV §5.3 Open C 三路線 (橋梁公理 / 弱\*連続測度族 / 関手 debt) の closure と並行して進める Open Question として、メタデータ §M6 に台帳化されている。

### 8.3　先行研究との接続 (closure 後の実現候補)

§8.2.2 の局所支持は、先行研究を「根拠」として輸入するためではなく、dictionary が物理的に駆動しうる実現候補を見分けるために使う。したがって本節では、Verlinde と Jacobson を本稿の証明者としてではなく、closure 後の検査面として扱う。

**Verlinde (2011)** [構造的対応]: Verlinde の entropic gravity は、重力が情報のエントロピー勾配から導出される力であると主張する。$F = T \nabla S$ の形式は、本稿 §5.2 で議論した通り、CPS スパンの Θ パラメータ (架橋射の情報損失量) の空間的勾配として再定式化できる可能性がある。これが成功すれば Verlinde の主張は CPS0' の具体例として位置づけられる。

**Jacobson (1995)** [構造的対応]: Jacobson は Rindler 観測者の見る局所的な Clausius 関係 $\delta Q = T dS$ から、重力場の方程式 $G_{\mu\nu} = 8\pi G_N T_{\mu\nu}$ を導出した。この導出の鍵は、null 面の面積が観測者依存でありながら Einstein 方程式はローレンツ共変であるという構造である。本稿の言葉で言えば: **Jacobson の導出は容器 (時空) の幾何的性質と内容 (熱力学的エネルギー) の整合条件の具体化**である。

両者の成果は本稿の [予想 D1-D3] に対して構造的根拠を与えるが、Paper II の CPS スパンへの明示的な埋め込みは未完である。重要なのは、両者が dictionary を閉じるための証明そのものではなく、dictionary が物理的に駆動するかを試す実現候補だという点である。特に Jacobson は、E-XIII-C3-04c により O4 の local physical bridge として前景化されたが、それでも entropy-area input と local equilibrium を前提にするため、Face Lemma ↔ Einstein dictionary の証明とは区別する。Eling-Guedens-Jacobson [28] は高階曲率補正では非平衡項が必要になることを示し、Faulkner et al. [29] / Lashkari-McDermott-Van Raamsdonk [30] は holographic CFT・ball region・線形化の範囲で Einstein 方程式を entanglement first law と結び、Jacobson (2016) [31] と Casini-Galante-Myers [32] は entanglement equilibrium 路線の射程と反例条件を明示する。したがって本稿では、Verlinde を contested heuristic realization candidate、Jacobson / entanglement 系を条件付き local / holographic realization candidate としてのみ扱う。

### 8.4　現時点での判定と Phase 5 での形式化課題

[予想 / 信頼度 60%]: 本 dictionary は Paper XIII 全体の Kalon 判定を
決める一点である。閉じれば忘却論は物理の文法に到達し、閉じなければ
精巧な類比に留まる。ただし、blocker は一枚岩ではない。曲率側の
blocker は closure の核と物理的実現例に分かれ、これとは別に α 橋の
closure がある。したがって、未達は少なくとも次の三面に分かれる。

#### Blocker A1 — Face Lemma から曲率 closure への昇格

1. Christoffel 記号を、Face Lemma の第三射そのものではなく「比較を可搬化する witness」として型付けする
2. Einstein テンソルの Bianchi 恒等式 $\nabla^\mu G_{\mu\nu} = 0$ を、Face Lemma そのものではなく projected syndrome closure として再定式化する
3. Riemann / holonomy、Ricci / scalar、Einstein tensor の三層を、raw defect、contracted defect、conserved coupling projection として、少なくとも GR インスタンスで self-consistent に固定する

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
ことである。Blocker A2 は本 dictionary が物理的実例として動くかを試す検証面であり、重要だが closure そのものの代用品ではない。E-XIII-C3-03/04a/04b/04c/04d は O3/O4 に局所支持を与えたため、§8 は「完全な空白の skeleton」ではなくなった。しかし、D1-D3 と Blocker B はまだ閉じていない。現時点では **source-backed local support を持つ skeleton** として残す。

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

[5] 本稿著者, "Embodied Cognition Without Biological Bodies: LLM Embodiment as Markov Blanket Thickness," unpublished working draft, 2026.

[6] R. Landauer, "Irreversibility and heat generation in the computing process," *IBM Journal of Research and Development*, vol. 5, no. 3, pp. 183–191, 1961.

[7] 本稿著者, "バカをやめたいなら構造を見ろ — なぜ構造を見る者は要素を見る者に勝つのか," 遊学エッセイ, 2026.

[8] E. Verlinde, "On the origin of gravity and the laws of Newton," *Journal of High Energy Physics*, vol. 2011, no. 4, p. 29, 2011.

[9] G. 't Hooft, "Dimensional reduction in quantum gravity," in *Salamfestschrift*, pp. 284–296, 1994.

[10] S. W. Hawking, "Particle creation by black holes," *Communications in Mathematical Physics*, vol. 43, no. 3, pp. 199–220, 1975.

[11] T. Jacobson, "Thermodynamics of spacetime: the Einstein equation of state," *Physical Review Letters*, vol. 75, no. 7, pp. 1260–1263, 1995. DOI: 10.1103/PhysRevLett.75.1260.

[12] B. S. DeWitt, "Quantum theory of gravity. I. The canonical theory," *Physical Review*, vol. 160, no. 5, pp. 1113–1148, 1967.

[13] L. Susskind, "The world as a hologram," *Journal of Mathematical Physics*, vol. 36, no. 11, pp. 6377–6396, 1995.

[14] S. Weinberg, "Anthropic bound on the cosmological constant," *Physical Review Letters*, vol. 59, no. 22, pp. 2607–2610, 1987.

[15] I. Khavkine and U. Schreiber, "Synthetic geometry of differential equations," preprint, 2017.

[16] B. Coecke and R. Duncan, "Interacting quantum observables: categorical algebra and diagrammatics," *New Journal of Physics*, vol. 13, p. 043016, 2011.

[17] D. J. Gross and F. Wilczek, "Ultraviolet behavior of non-Abelian gauge theories," *Physical Review Letters*, vol. 30, no. 26, pp. 1343–1346, 1973.

[18] G. Kletetschka, "Three-Dimensional Time: A Mathematical Framework for Fundamental Physics," *Reports in Advances of Physical Sciences*, vol. 9, 2550004, 2025. DOI: 10.1142/S2424942425500045

[19] S. M. Carroll, "Lecture Notes on General Relativity," arXiv:gr-qc/9712019, 1997.

[20] R. C. Tolman, "Static solutions of Einstein's field equations for spheres of fluid," *Physical Review*, vol. 55, no. 4, pp. 364–373, 1939. DOI: 10.1103/PhysRev.55.364.

[21] J. R. Oppenheimer and G. M. Volkoff, "On Massive Neutron Cores," *Physical Review*, vol. 55, no. 4, pp. 374–381, 1939. DOI: 10.1103/PhysRev.55.374.

[22] V. Balasubramanian and B. Czech, "Quantitative approaches to information recovery from black holes," arXiv:1102.3566, 2011.

[23] W. Ambrose and I. M. Singer, "A theorem on holonomy," *Transactions of the American Mathematical Society*, vol. 75, pp. 428–443, 1953. DOI: 10.2307/1990721.

[24] U. Schreiber and K. Waldorf, "Parallel transport and functors," *Journal of Homotopy and Related Structures*, vol. 4, no. 1, pp. 187–244, 2009. arXiv:0705.0452.

[25] J. C. Baez and U. Schreiber, "Higher gauge theory: 2-connections on 2-bundles," arXiv:hep-th/0412325, 2004.

[26] A. Navarro and J. Navarro, "Lovelock's theorem revisited," *Journal of Geometry and Physics*, vol. 61, no. 10, pp. 1950–1956, 2011. arXiv:1005.2386.

[27] N. Dadhich, "Characterization of the Lovelock gravity by Bianchi derivative," arXiv:0802.3034, 2008.

[28] C. Eling, R. Guedens, and T. Jacobson, "Nonequilibrium thermodynamics of spacetime," *Physical Review Letters*, vol. 96, 121301, 2006. DOI: 10.1103/PhysRevLett.96.121301. arXiv:gr-qc/0602001.

[29] T. Faulkner, M. Guica, T. Hartman, R. C. Myers, and M. Van Raamsdonk, "Gravitation from entanglement in holographic CFTs," *Journal of High Energy Physics*, vol. 2014, no. 3, 051, 2014. DOI: 10.1007/JHEP03(2014)051. arXiv:1312.7856.

[30] N. Lashkari, M. B. McDermott, and M. Van Raamsdonk, "Gravitational dynamics from entanglement 'thermodynamics'," *Journal of High Energy Physics*, vol. 2014, no. 4, 195, 2014. DOI: 10.1007/JHEP04(2014)195. arXiv:1308.3716.

[31] T. Jacobson, "Entanglement equilibrium and the Einstein equation," *Physical Review Letters*, vol. 116, 201101, 2016. DOI: 10.1103/PhysRevLett.116.201101. arXiv:1505.04753.

[32] H. Casini, D. A. Galante, and R. C. Myers, "Comments on Jacobson's 'entanglement equilibrium and the Einstein equation'," *Journal of High Energy Physics*, vol. 2016, no. 3, 194, 2016. DOI: 10.1007/JHEP03(2016)194. arXiv:1601.00528.

---

## 付録 A: 開かれた問い

- **Q1**: Paper II の CPS スパンの α_CPS と Newton の重力定数 $G_N$ の定量的関係は何か? 定性的には「α_CPS > 0 のとき引力が存在する」と主張できるが、G_N の絶対値を α_CPS のみから導出することは未達である。
- **Q2**: Face Lemma の最小非自明性が Einstein 方程式を回収するための O1-O4 は、どの順序で閉じるべきか? 具体的には、(O1) 3射と接続の型付け、(O2) 曲率の defect 化、(O3) Bianchi 恒等式の closure 化、(O4) Einstein 方程式の coupling 化を、少なくとも GR インスタンスで self-consistent に固定できるか。
- **Q3**: CPS0' (Paper II §2.1) pre-geometric 構造から時空 signature (3+1) が導出されるための P1-P4 は閉じるか? 具体的には、(P1) 時間性、(P2) 容器/内容の型付け、(P3) Level 0/1 分離、(P4) 投影規則が、少なくとも GR インスタンスで破綻せずに並び立つか。
- **Q4**: Paper III の α_III (∈ ℝ, Amari 接続パラメータ) セクターと宇宙論 (特に暗黒エネルギー・暗黒物質問題) の関係は? α_III < 0 は反-Markov 構造を持つが、物理的実現は未検討である。
- **Q5**: Paper VIII の有限主体定理 (Th. 6.3.2) と宇宙論スケールの観測者 (人間原理, Weinberg 1987) はどう接続するか? 有限主体の α_VIII と宇宙の α_CPS の cross-coupling は未定式化である。
- **Q6**: 量子重力問題の CPS 的翻訳 ("Θ → 0 と Θ → ∞ の位相転移") は物理的に何を意味するか? とくにブラックホール情報パラドックス [22] は、根本水準でのユニタリティと有効記述水準での情報喪失の両立を、Paper VIII の `(F1)` 全体保存と `(F4)` 局所アクセス減少の分裂として読めるか?
  - **検査対象**: ブラックホール物理の解決ではなく、全体保存・局所不可回復・境界生成という三項構造である。この三項構造が事象の地平面 / MB / 経路忘却 T12 の間で保たれるなら、ブラックホール情報パラドックスは忘却境界の同型候補になりうる。
  - **局所不可回復の定量的補強**: ここでいう局所不可回復性は、情報の存在否定ではなく、有限主体が実行できる観測プロトコルが、ブラックホール微視状態の応答差異を十分な outcome bin へ分けられないこととして定式化できる。Balasubramanian and Czech [22] では、微視状態差異は応答の分散として残るが、回復には `exp(-S)` 程度の解像度または `exp(S)` 程度の時間が必要になる。忘却論側では、これは `κ_O(ε,T;P) < N_BH(X;P)` により `α_O^BH(X;P,ε,T)>0` が残る場合に対応する。ただし `exp(-S)` / `exp(S)` は `κ` の定義ではなく、観測容量を増やすための資源閾値である。したがって Q6 は、ブラックホール情報パラドックスを解く主張ではなく、全体保存と局所不可回復の差を有限主体の観測容量として検査する問いに留まる。
  - **境界生成の限定**: ここで境界生成とは、情報回復を保証する機構ではなく、全体保存と局所不可回復の差が検出可能になる最小の照合面が立つことを指す。Paper II の Face Lemma は、この読みに対する検査条件を与えるが、回復可能性の十分条件ではない。
  - **補助検査**: 落下観測者・内部幾何・非幾何相・創発時間の問題 [22] は、Q6 の境界生成だけでなく Q3 の時間性・Level 0/1 分離・投影規則にも接続する。この段階では、これは「内部幾何が忘却である」という主張ではなく、古典極限で安定する内部 / 外部の切り方が、完全量子論でどの水準に移るかを問う補助検査である。
  - **棄却条件**: 物理過程の同一視、事象の地平面と MB の混同、`(F1)/(F4)` 対応が単なる比喩に留まること、または Level 0/1 が量子 / 古典の言い換えに留まることが判明した場合、この候補は棄却される。

  この問いでは、(i) 地平面や内部 / 外部の切断が粗視化によって現れるか、(ii) その切断が全体保存と局所不可回復の差を検出可能にする最小照合面として立つか、を分けて検査する。前者は Paper VIII の被覆粗視化の問題であり、後者は Paper II の Face Lemma が与える検出可能性の問題である。

- **Q7**: ヒッグス機構は CPS スパン Type I の弱い力射影として読めるか? 具体的には、ヒッグス VEV による真空構造選択 (`λ_eff < 0` で `Φ=0` 不安定 → `Φ ≠ 0` 安定) は、Paper II の容器 (時空真空) と内容 (質量-エネルギー) の非対称な切り出しの電弱領域での具体機構として位置づけられるか?
  - **検査対象**: ヒッグス機構の物理的再導出ではなく、(a) `λ_eff` 符号反転による自発的忘却 = 自発的対称性の破れの構造的同型、(b) 真空 (容器のみの存在状態) からの内容 (質量) 切り出しが C2 容器/内容非対称射影の電弱領域での実現と読めるか、(c) 弱い力 (`SU(2) × U(1) → U(1)_{em}`) の forgetful 射影として C1 (四つの力統一) を局所的に閉じる第一例になるかの三点である。物理過程の同一視ではなく、構造の同型候補性を検査する。
  - **`λ_eff` 符号反転の役割**: Paper III §4.7 の `λ_eff(α) = λ + α²⟨|T|²⟩/4` において、`λ_eff > 0` (`Φ=0` 安定) と `λ_eff < 0` (`Φ=0` 不安定 → 自発的忘却) の相転移は、ヒッグス機構の自発的対称性の破れと **構造的に同型** である。ただし「同型」は SOURCE で示すべき検査命題であり、現時点では Paper III §4.7 と Paper V §M8 D2 (CPS-YM 関手) / D3 (CW 導出) を入口とする。Paper V D3 の `m_H² = 3g⁴/(8π²)` は v2 `S[α,Θ]` 起源で v3.5 `S[Φ,α;μ]` では再導出待ちであるため、本問は Paper V 単独の再導出を前提にしない。
  - **容器先行の限定**: ここで「容器先行」とは、ヒッグス機構が時空真空の存在を前提に内容 (VEV → 質量) を切り出す機構として読めることを指す。これは C2 §M5 Round 1 の「真空解は容器のみの存在を許す」と整合する。ただし、ヒッグス場が時空多様体上で定義される以上、容器/内容の非対称性は古典的 GR レベルで成立しており、量子化された場合の分解は別問題として残す。
  - **補助検査**: (i) 自発的対称性の破れ ↔ 自発的忘却の同型は他の対称性の破れ (BCS 超伝導、QCD カイラル対称性の破れ) でも保たれるか — 保たれるなら同型は対称性の破れ一般の構造として強化される。(ii) 「容器/内容の非対称射影」が量子場の真空状態 (Fock 真空、ヒッグス真空) と GR の真空解の間でどう関係するかは Q3 (`(3+1)` signature 発生) と接続する補助検査である。
  - **棄却条件**: 物理過程の同一視 (ヒッグス粒子 = 忘却粒子)、`λ_eff` 符号反転とヒッグス VEV の表面的類比に留まること、CPS Type I の容器/内容構造が電弱領域で破綻すること、または Paper II §3.4 Face Lemma の 3射最小性が弱い力ゲージに対応しないことが判明した場合、この候補は棄却される。

  この問いでは、(i) `λ_eff` 符号反転と自発的対称性の破れが Paper III §4.7 の作用汎関数経由で **構造的同型** (単なる類比ではなく射の対応) として読めるか、(ii) ヒッグス VEV による質量生成が C2 容器/内容射影の電弱領域での具体実現として動くかを分けて検査する。前者は Paper V §M8 D2/D3 の v3.5 再導出と並行する経路で、後者は Paper II §3.3 `α_CPS` と電弱結合定数 `g_W` の関係を SOURCE 化する経路で進む。

- **Q8 (OQ-DIV)**: 欠損 cocycle $\kappa$ から、曲率発散 (Kretschmann スカラー $K = R^{abcd} R_{abcd} \to \infty$ 型) に対応する非負観測量を定義できるか。Paper XIV §5.3 Open C 三路線のうち路線 2 (λ-依存弱\*連続測度族 $\mu_\lambda$) を延伸して、$\kappa$ の有界性と非有界性を区別する観測量を構成する必要がある。連続側で $\kappa$ がそもそも well-defined になる前提自体が Paper XIV Open C として未閉であり、現状の路線 2 は連続変形構成までで非有界性まで踏み込んでいない。
  - **検査対象**: 古典 GR の曲率発散の物理的解決ではなく、欠損 cocycle $\kappa$ に「有界 / 非有界」述語を追加して路線 2 の期待値で追跡できるか、という構造的問いである。
  - **棄却条件**: 連続側 $\kappa$ の同定が Paper XIV Open C で別経路 (路線 1 橋梁公理 or 路線 3 関手 debt) のみで閉じ、路線 2 延伸が冗長になることが判明した場合、Q8 は OQ-WEY / OQ-ALPHA に吸収される。

- **Q9 (OQ-WEY)**: Weyl 曲率 (Riemann の trace-free 部分) を、縮約されない生の幾何 defect 残差として定式化できるか。§8.2.3 の四分岐拡張候補は、§8.2.2 三層分離 (Riemann = raw defect / Ricci = contracted defect / Einstein = conserved coupling projection) を Riemann の標準分解 (Ricci 部分 + Weyl 部分) に沿って拡張し、Weyl を「内容に結合不可能な trace-free 残差」として位置づける読みである。Penrose (1979) Weyl Curvature Hypothesis (Weyl 増大 = エントロピー増大方向 = 熱力学的時間方向) と Paper IX (エントロピーは忘却である) の接続候補。
  - **検査対象**: Weyl 曲率の物理的再定義ではなく、§8.2.2 三層分離を四分岐に拡張したとき、Schwarzschild (Weyl 発散、$R_{\mu\nu} = 0$, $K \sim 1/r^6$) と FLRW (Ricci 発散、Weyl = 0) の対比が forgetting 的に区別して読めるか、という構造的問いである。
  - **棄却条件**: 四分岐拡張が §8.2.2 三層と整合せず、Weyl を Ricci 側へ縮退させて読まざるを得ない場合、Q9 は OQ-DIV に吸収される。

- **Q10 (OQ-ALPHA)**: 局所 $\alpha(x) \to 1$ と曲率不変量 $K = R^{abcd} R_{abcd} \to \infty$ を結ぶ写像はあるか。Paper VIII §6.2.3 (iii) の $\alpha = 1 \Rightarrow C_1 = C_{\text{disc}}$ (対象だけ残り射構造が消える極限) を、点ごとに変動する場 $\alpha(x)$ として読み直し、$\alpha(x) \to 1$ の局所達成と曲率発散点の対応を構成する。Paper VIII の「存在は忘却の影響を受けない」(α 不変な Level 0) と曲率発散点での「同定不能」を整合する読みである。
  - **検査対象**: Paper VIII §6.2.3 (iii) は $\alpha = 1$ で $C_{\text{disc}}$ と定義するが、ただちに「曲率 cocycle が未定義」へ自動接続する命題は SOURCE に無い。α を点ごとの場 $\alpha(x)$ として時空曲率へ接続する写像の構成自体が虚な点である。
  - **棄却条件**: $\alpha(x)$ 場の構成が Paper VIII の有限主体定理 (Th. 6.3.2) と整合せず、$\alpha(x)$ 場が局所的に well-defined にできない場合、Q10 は棄却される。

Q8-Q10 は §8.2.3 で起票した三 Open Question (OQ-DIV / OQ-WEY / OQ-ALPHA) の付録 A 上の公開形式である。詳細はメタデータ §M6 Open Question Ledger (2026-05-24) 参照。Codex Lane 2 セカンドオピニオン (gpt-5.5:xhigh) と Claude 一次見立てのダブルチェック結果で、三 Open Question は排他的ではなく「主線 (OQ-DIV) + 補助 (OQ-ALPHA 存在論的 / OQ-WEY 物理的)」の並列補助関係として固定された。

---

## 改訂履歴

- **v0.1 (2026-04-11)**: 初版。v2 (`01_草稿｜Drafts/07_インキュベータ｜Incubator/legacy/力とは忘却である_v2.md`) の Bucket XIII 部分 (解体マップ §7 参照) から抽出・再構成。v2 §4.6 の CPS 公理系の full definition は Paper II (Phase 3) への pointer に置換。v2 §9 意識のハードプロブレム関連は本稿の scope 外として除外 (Paper II / VIII 完成後に independent essay として昇格判定)。§8 Face Lemma ↔ Einstein dictionary は skeleton のまま残し Phase 5 で形式化を試行する。
- **v0.1.1 (外部パッチ統合)**: §0 簡易記号表の `01_草稿｜Drafts/08_インフラ｜Infra/統一記号表.md` 参照パスを実在パス `01_草稿｜Drafts/08_インフラ｜Infra/references/統一記号表.md` に修正。§8.2.1 O1 義務に precision note を追加: 3項の型異質性と Γ の g からの導出可能性という二重障害を明示し、「三つの場」ではなく「三つの検証役割 (方向 / 比較 / 輸送)」として型付けし直す解決方向を記載。旧 donor `FaceLemma_Einstein_O1試作.md` は 2026-04-18 に本稿 meta の Donor Absorption Ledger へ再配置。主張水準の変更なし。
- **v0.1.2 (C3 local closure 実験反映)**: §8.2.2 を追加し、E-XIII-C3-02/03/04a/04b/04c の結果を本文へ統合。Einstein tensor を raw defect と読む直読を棄却し、`Riemann/holonomy = raw defect`、`Ricci/scalar = contracted defect`、`Einstein tensor = conserved coupling projection` の三層分離を採用。FLRW/TOV/Jacobson local patch を O3/O4 の局所支持として反映。ただし C3 の主張水準は [構造的対応] / [skeleton] のまま維持し、定理昇格なし。
- **v0.1.3 (anisotropic TOV stress test 反映)**: E-XIII-C3-04d を §8.2.2 に追加。static spherical anisotropic stress で $p_r$ と $p_t$ を分けても、保存式が $p_r'+(\rho+p_r)\Phi'+2(p_r-p_t)/r=0$ として閉じることを反映。O4 は isotropic perfect-fluid 依存ではない局所支持を得たが、一般の非対角 flux / shear、係数、作用原理、一般 GR case は未閉鎖。
- **v0.1.4 (§8 citation normalization)**: §8.2.2 の E-XIII-C3 番号を内部検証台帳として明示し、外部 SOURCE として Carroll / Tolman / Oppenheimer-Volkoff / Jacobson を本文と参考文献に接続。局所 symbolic run と忘却論的 INFERENCE を分離し、§8.3 への transition を「closure 後の実現候補」へ調整。主張水準の変更なし。
- **v0.1.5 (§8 cold reread polish)**: §8.2 の D2 を直読形から改訂形へ変更し、`Einstein tensor = raw Face Lemma defect` の残存を除去。D2 / O2 / Blocker A1 を `Riemann/holonomy = raw defect`、`Ricci/scalar = contracted defect`、`Einstein tensor = conserved coupling projection` の三層分離へ統一。主張水準の変更なし。
- **v0.1.6 (Q7 ヒッグス機構候補起票, 2026-05-06)**: 付録 A に Q7 「ヒッグス機構は CPS スパン Type I の弱い力射影として読めるか」を Q6 同型形式 (検査対象 / `λ_eff` 符号反転の役割 / 容器先行の限定 / 補助検査 / 棄却条件) で起票。Paper III §4.7 `λ_eff(α) = λ + α²⟨|T|²⟩/4` と Paper V §M8 D2 (CPS-YM 関手) / D3 (CW 導出) を入口とする検査問題化。Q7 は C2 容器/内容射影の電弱領域での同型候補検査として設計され、物理過程の同一視 (ヒッグス粒子 = 忘却粒子) は明示棄却。Paper V meta §M8 D2 status を「Q7 と並行扱い (Q7 検査後に v3.5 吸収可否を再判定)」に更新済み。本稿 §M6 C1 / C2 / C4 の虚→実変換面も同日更新 (C2 判定条件 (5) は同型候補検査として弱化)。主張水準の変更なし。
- **v0.1.7 (§8 Face Lemma ↔ GR/Riemann 文献辞書, 2026-05-23)**: §8.2 冒頭に identity/proof 禁止の non-identity paragraph を追加し、Ambrose-Singer / Schreiber-Waldorf / Baez-Schreiber / Navarro-Navarro / Dadhich を `raw defect / transport functor / higher comparison surface / conserved projection` の SOURCE として接続。D1 を「Christoffel 記号の独立第三射」から「方向 / 比較 / 輸送の検証役割 + Γ は可搬化 witness」へ再固定。§8.3 では Verlinde を contested heuristic realization candidate、Jacobson / entanglement 系を条件付き local / holographic realization candidate として降格し、Eling-Guedens-Jacobson / Faulkner et al. / Lashkari et al. / Jacobson 2016 / Casini-Galante-Myers を failure-condition つきで参照。主張水準は [構造的対応] / [skeleton] のまま維持。
- **v0.1.8 (§8.2.3 Ricci/Weyl 分解と曲率発散の Open Question 起票, 2026-05-24)**: §8.2.2 三層分離 (Riemann/holonomy = raw defect / Ricci/scalar = contracted defect / Einstein = conserved coupling projection) の Ricci 側偏重を補い、Weyl 曲率の空席を §8.2.3 として skeleton 起票。Riemann の標準分解 (Ricci 部分 + Weyl 部分) に沿った四分岐拡張候補を提示し、Schwarzschild (Weyl 発散、$R_{\mu\nu} = 0$, $K \sim 1/r^6$) と FLRW (Ricci 発散、Weyl = 0) の最小実験対比を据えた。Open Question 三件 (OQ-DIV / OQ-WEY / OQ-ALPHA) をメタデータ §M6 Open Question Ledger に台帳化し、付録 A に Q8-Q10 として公開。Codex Lane 2 セカンドオピニオン (gpt-5.5:xhigh) + Claude 一次見立てのダブルチェックで「主線 (OQ-DIV) + 補助 (OQ-ALPHA 存在論的 / OQ-WEY 物理的)」並列補助関係として固定。Penrose (1979) Weyl Curvature Hypothesis と Paper IX (エントロピーは忘却である) の接続候補を OQ-WEY に内蔵。主張水準は [skeleton] のまま、定理昇格なし。本変更は append のみで既存記述の削除・上書きなし。
- **v0.1.9 (§8 C3 ledger/citation polish, 2026-05-25)**: C3 claimmap 本体行を `GR/Riemann 側の方向・比較・輸送、Riemann/holonomy raw defect、Ricci/scalar contracted defect、Einstein tensor conserved coupling projection` の danger-ranked structural correspondence へ更新。refs [28]-[32] に DOI を追加し、Round 17 後の次手を PublicEdition §8 限定同期 / SOURCE pack 化へ更新。主張水準の変更なし。
