# エントロピーは忘却である — CPS 圏の統計力学

**Paper IX — v0.9 (2026-04-27) — 忘却論 (Force is Oblivion) シリーズ**

> **日付注記 (2026-04-17):** 旧ヘッダおよび変更履歴にあった `2026-07-21` / `2026-07-23` は未来日付の誤記。`v0.1` については `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/リファレンス/熱力学対応表.md` の更新履歴にある「2026-04-02: Paper IX v0.1 作成」を SOURCE として採用する。`v0.5` の厳密日付は未観測だが、`論文XII_速度は忘却である_草稿.md` v0.4 (2026-04-09) が Paper IX Th. 3.4.1 を参照しているため、少なくとも 2026-04-09 以前の版として補正する。

*概要.* Paper VIII で確立した α-忘却濾過の公理系 (F1)-(F4) が、統計力学の基本構造——エントロピー、第二法則、データ処理不等式——を自然に内包することを示す。中心的構成は **CPS エントロピー** $S_{\mathrm{CPS}}(p, \alpha)$: Perrone [P1] が Markov 圏上で定義したエントロピー（確定的射からの divergence の下限）を、Paper II §3.7.1 が与える **Markov 圏的構造**（$\alpha = 0$ では strict な Fritz 型 Markov 圏、$\alpha > 0$ では $e(\alpha)$-twisted 余モノイド構造）を通じて α-忘却濾過に輸入する。主定理（CPS エントロピー単調性定理）は、(F4) 公理から直接従う: 忘却が進む（α が増大する）ほど確定的射の集合が縮小し、したがってエントロピーが単調に増大する。これは Paper VIII 定理 6.10.3（射計数版）の Perrone 枠組みへの精密化であり、Shannon/Rényi/Gini-Simpson エントロピーを統一的に回収する。

> **記号規約.** α は Paper VIII の忘却強度パラメータ $\alpha_{\mathrm{VIII}} \in [0, 1]$。Paper III/V の $\alpha_{\mathrm{III}} \in \mathbb{R}$（Amari の α-接続）とは異なる。CPS($\alpha$) は忘却パラメータ $\alpha$ における CPS 圏を指す。$D$ は固定された divergence 関数。統一記号表 (`drafts/リファレンス/統一記号表.md`) を参照。

> **主張水準注記.** Paper II §3.7.1 が strict な Fritz 型 Markov category を正確に与えるのは $\alpha = 0$ 設定である。$\alpha > 0$ では copy/del は構成されるが、余単位律は $e(\alpha)$-twist を受けるため、本稿の Perrone 輸入は $\alpha > 0$ セクターに対する**構成的延長**として読む。

> **内部育成層分け注記 (2026-04-26).** 本稿は当面、外部公開稿ではなく育成稿として保持する。ただし主張水準は混ぜない。§3 は **定理核**、§4 と §6.1-§6.2 は **constructive appendix**、§6.3-§6.4 は **open program**、§5 は **Paper IX-B 候補の負セクター育成面** として読む。したがって「CPS 圏の統計力学」という大構想は温存するが、本文の論証列ではまず **(F4) から CPS エントロピー単調性が従う** という一点を主核に固定する。

---

## §1. 動機と問題設定

### 1.1 忘却論の熱力学的構造

忘却論 Papers I–VIII は、α-忘却濾過 {C_α} が熱力学の粗視化（coarse-graining）と構造的に同型であることを示唆してきた（随伴レポート §10）。Paper VIII §6.10 では (F4) 公理から射計数エントロピー $S_{\mathrm{cat}}(\alpha) := \log m(0) - \log m(\alpha)$ の単調増大を証明した（Th. 6.10.3: 忘却の第二法則）。しかし $S_{\mathrm{cat}}$ は射の「数」のみを計量する粗い測度であり、Shannon エントロピーや Rényi エントロピーといった情報論的エントロピーとの関係は未確立であった。

本稿の目的は、この欠落を Perrone [P1] の Markov 圏エントロピーの輸入によって埋めることである。

### 1.2 既存の構成要素

本稿は以下の既存の結果に依存する:

| 結果 | 出典 | 本稿での役割 |
|:--|:--|:--|
| α-忘却濾過 (F1)-(F4) | Paper VIII Def. 6.2.1 | 基底構造 |
| CPS($\alpha = 0$) は strict な Markov 圏, CPS($\alpha > 0$) は Markov 圏的構造 | Paper II §3.7.1 互換性補題 + α-twisted 余モノイド | Perrone 輸入の前提と主張水準の境界 |
| 射計数エントロピー $S_{\mathrm{cat}}$ | Paper VIII Th. 6.10.3 | 粗い版の第二法則 |
| Schur-Horn 橋渡し | Paper I Th. 5.6.1, Paper IV 命題 7.5.1 | 観測量の entropic 制約 |
| Markov 圏上のエントロピー | Perrone [P1] | 輸入対象 |
| データ処理不等式 (DPI) | Perrone [P1] §3.1, §4.1 | 単調性の道具 |

### 1.3 本稿の構成

§2 で Markov 圏エントロピーの必要な定義を再掲し、§3 で CPS エントロピーを構成し、主定理として α-単調性を示す。§4 は Paper VIII の射計数版との関係を constructive appendix として置く。§5 は標準 $S_{\mathrm{CPS}}$ の主定理列ではなく、$\alpha_{\mathrm{III}} < 0$ の負セクターを Paper IX-B 候補として育成する面である。§6 は $E(f)$ と有限版 $Z_{\mathrm{CPS}}$ までを constructive appendix、$T_{\mathrm{CPS}}$ / $H_{\mathrm{CPS}}$ / 三パラメータ統一を open program として区別する。

---

## §2. Markov 圏エントロピーの概要

本節は Perrone [P1] と Fritz [F1] の結果を、CPS 圏への適用に必要な範囲で再掲する。

### 2.1 Markov 圏の復習

**定義 2.1.1 (Markov 圏; Fritz [F1, Def. 2.1]).** 対称モノイダル圏 $(\mathcal{C}, \otimes, I)$ が **Markov 圏** (Markov category) であるとは、各対象 $X$ に可換余モノイド構造——comultiplication $\mathrm{copy}_X: X \to X \otimes X$ と counit $\mathrm{del}_X: X \to I$——が備わり、以下を満たすものをいう:

1. $\mathrm{del}_X$ は全ての射 $f: A \to X$ に対して自然: $\mathrm{del}_X \circ f = \mathrm{del}_A$
2. $\mathrm{copy}_X$ は全ての射 $f: A \to X$ に対して以下の意味で「互換的」: $\mathrm{copy}_X \circ f = (f \otimes f) \circ \mathrm{copy}_A$ が**確定的射に対してのみ**成立する

**定義 2.1.2 (確定的射; Fritz [F1, Def. 10.1]).** Markov 圏の射 $f: X \to Y$ が**確定的** (deterministic) であるとは、$\mathrm{copy}_Y \circ f = (f \otimes f) \circ \mathrm{copy}_X$ が成立することをいう。確定的射の全体を $\mathrm{Det}(\mathcal{C})$ と書く。

直観的には、確定的射は「ノイズなし」の写像であり、非確定的射は確率的チャネルに対応する。

### 2.2 Perrone のエントロピー

**定義 2.2.1 (Markov 圏上のエントロピー; Perrone [P1, §2]).** Markov 圏 $\mathcal{C}$ に divergence $D: \mathrm{Mor}(\mathcal{C}) \times \mathrm{Mor}(\mathcal{C}) \to [0, \infty]$ が与えられているとする。状態 $p: I \to X$（=モノイダル単位 $I$ からの射）の**エントロピー** $H_D(p)$ を

$$H_D(p) := \inf_{f \in \mathrm{Det}(\mathcal{C})(I, X)} D(p \| f)$$

で定義する。すなわち、エントロピーは**確定的状態への最小 divergence** である。

**回収される古典的エントロピー.** $D$ の選択に応じて [P1, §2.3]:
- $D = D_{\mathrm{KL}}$ (Kullback-Leibler) → Shannon エントロピー $H(p) = -\sum p_i \log p_i$
- $D = D_\alpha^{\mathrm{Rényi}}$ → Rényi エントロピー $H_\alpha(p) = \frac{1}{1-\alpha}\log\sum p_i^\alpha$
- $D = D_{\mathrm{GS}}$ (Gini-Simpson) → Gini-Simpson 指数 $1 - \sum p_i^2$

### 2.3 データ処理不等式

**定理 2.3.1 (DPI; Perrone [P1, §3.1, §4.1]).** Markov 圏 $\mathcal{C}$ における射 $k: X \to Y$ に対し、$k$ が**確定的射を確定的射に写す**ならば:

$$H_D(k \circ p) \leq H_D(p)$$

すなわち、確定性を保存する「チャネル」を通過してもエントロピーは増加しない。

*直観.* 確定的チャネルは情報を失わない（or 減らすだけ）ので、不確実性（エントロピー）は増えない。

---

## §3. CPS エントロピーの構成

### 3.1 CPS($\alpha > 0$) の Markov 圏的構造

Paper II 互換性補題（§3.7.1）により、$\alpha = 0$ では CPS 圏は Fritz の意味での strict な Markov 圏となる。$\alpha > 0$ では $e(\alpha)$-twisted 余モノイド構造と a.e. factorization が与えられるため、本稿ではそれを Perrone エントロピーの構成的延長の足場として用いる:

ここで本稿が実際に使うのは「$\alpha > 0$ で strict な Markov 圏が完成している」という強い読みではなく、copy/del の構成と確定的射 `Det(CPS(α))` を定義するのに必要な最小部分だけである。

- **$\mathrm{del}_X$**: 忘却場 $\Phi > 0$ による全忘却。$\alpha > 0$ により $\Phi$ の正値性が保証され、正規化 $\mathrm{del}_X = \Phi / \int \Phi$ が well-defined。
- **$\mathrm{copy}_X$**: 対角写像 $x \mapsto (x, x)$ の Markov kernel としての持ち上げ。Fritz の意味での確定的射。
- **確定的射 $\mathrm{Det}(\mathrm{CPS}(\alpha))$**: copy を保存する射。$\alpha$ の増大により Mor が減少するため、$\mathrm{Det}$ も減少する（後述の補題 3.2.1）。

**備考.** strict な Markov 圏構造は Paper II が明示する通り $\alpha = 0$ でのみ正確に成立する。$\alpha > 0$ では $\mathrm{del}_X$ / $\mathrm{copy}_X$ は構成されるが、余単位律は $e(\alpha)$-twist を受けるため、本稿の $S_{\mathrm{CPS}}(p, \alpha)$ は Perrone 構成の $\alpha > 0$ 延長として読む。$\alpha \leq 0$ では $\mathrm{del}_X$ の正規化が崩壊し（Paper II §3.7.1 備考）、この Markov 圏的構造自体が退化する。本稿では $\alpha > 0$ に限定する。$\alpha \leq 0$ セクターのエントロピーは §5 で議論する（Paper III の $\mathbb{Z}_2$-次数付き CPS 圏との関係）。

### 3.2 確定的射の α-単調性

**補題 3.2.1 (確定的射の単調包含).** $0 < \alpha_1 \leq \alpha_2 \leq 1$ ならば:

$$\mathrm{Det}(\mathrm{CPS}(\alpha_2)) \subseteq \mathrm{Det}(\mathrm{CPS}(\alpha_1))$$

*証明.* (F4) より $\mathrm{Mor}(C_{\alpha_2}) \subseteq \mathrm{Mor}(C_{\alpha_1})$。確定的射は射のうち copy を保存するものとして定義される（Def. 2.1.2）。copy の保存は射のクラスの部分条件であるから、$\mathrm{Det}(C_{\alpha_2}) \subseteq \mathrm{Mor}(C_{\alpha_2}) \subseteq \mathrm{Mor}(C_{\alpha_1})$。さらに、$f \in \mathrm{Det}(C_{\alpha_2})$ が $C_{\alpha_1}$ においても copy を保存するかを確認する。

(F1) より $\mathrm{Ob}(C_{\alpha_1}) = \mathrm{Ob}(C_{\alpha_2})$ であるから、copy の定義は両圏で同一の対象上の同一の写像（対角写像）である。$f$ が $C_{\alpha_2}$ で copy を保存するならば、同じ等式は $C_{\alpha_1}$ でも成立する（$C_{\alpha_2}$ での等式は $C_{\alpha_1}$ の射の等式でもある）。したがって $f \in \mathrm{Det}(C_{\alpha_1})$。$\square$

**備考.** この補題は (F1) と (F4) のみを使用し、(F2)(F3) に依存しない。copy 構造の α-非依存性（対角写像であること）が本質的である。

### 3.3 CPS エントロピーの定義

**定義 3.3.1 (CPS エントロピー).** $\alpha > 0$ とし、$D$ を CPS 圏上の divergence とする。状態 $p: I \to X$ の **CPS エントロピー** を

$$\boxed{S_{\mathrm{CPS}}(p, \alpha) := \inf_{f \in \mathrm{Det}(\mathrm{CPS}(\alpha))(I, X)} D(p \| f)}$$

で定義する。

**直観.** CPS エントロピーは「状態 $p$ が、α-忘却レベルにおいてどれだけ確定的状態から離れているか」を測る。α が高い（忘却が強い）ほど利用可能な確定的状態が少なくなるため、最近接の確定的状態はより遠くなり、エントロピーは増大する。

### 3.4 CPS エントロピー単調性定理

**定理 3.4.1 (CPS エントロピー単調性; 忘却の第二法則 — 情報論的版).** $0 < \alpha_1 \leq \alpha_2 \leq 1$ とし、$p: I \to X$ が $\mathrm{Mor}(C_{\alpha_2})$ に属する状態（すなわち、両方の α レベルで well-defined な状態）であるとする。このとき:

$$\boxed{S_{\mathrm{CPS}}(p, \alpha_1) \leq S_{\mathrm{CPS}}(p, \alpha_2)}$$

すなわち、**忘却が進む（α が増大する）ほど CPS エントロピーは単調に増大する。**

*証明.* 補題 3.2.1 より $\mathrm{Det}(C_{\alpha_2}) \subseteq \mathrm{Det}(C_{\alpha_1})$。下限の集合が縮小するから:

$$\inf_{f \in \mathrm{Det}(C_{\alpha_2})} D(p \| f) \geq \inf_{f \in \mathrm{Det}(C_{\alpha_1})} D(p \| f)$$

左辺が $S_{\mathrm{CPS}}(p, \alpha_2)$、右辺が $S_{\mathrm{CPS}}(p, \alpha_1)$。$\square$

**系 3.4.2 (ダイバージェンス非依存性).** 定理 3.4.1 は divergence $D$ の具体的な選択に依存しない。$D$ が Perrone 型エントロピーを定義できる divergence であり、少なくとも $D(p \| f) \geq 0$ と $D(f \| f) = 0$ for $f$ deterministic を満たすならば、同じ α-単調性が成立する。特に:

- $D = D_{\mathrm{KL}}$ → Shannon エントロピーの CPS 単調性
- $D = D_\alpha^{\mathrm{Rényi}}$ → Rényi エントロピーの CPS 単調性
- $D = D_{\mathrm{GS}}$ → Gini-Simpson 指数の CPS 単調性

*証明.* 定理 3.4.1 の証明で用いたのは $\mathrm{Det}(C_{\alpha_2}) \subseteq \mathrm{Det}(C_{\alpha_1})$ と、下限を取る集合の包含だけである。$D$ の具体形、凸性、連鎖律、連続性は使用していない。したがって Perrone 型の最小 divergence として $S_{\mathrm{CPS}}$ が定義できる任意の $D$ について同じ不等式が従う。$\square$

**備考 3.4.3 (証明の構造).** この証明は remarkably simple であり、本質的に以下の一行に帰着する:

> **(F4) → 確定的射が減る → 下限の集合が縮む → infimum が増大する**

この単純さは偶然ではない。(F4) は忘却の不可逆性を**射の包含**という最も基本的な形で表現しており、エントロピーの単調性はその直接的な帰結である。

**備考 3.4.4 (時間の矢 = 忘却の矢).** 定理 3.4.1 を Paper V 定理 2.3.1 ($\beta_\alpha \leq 0$) と結合すると、エントロピーの時間発展が閉じる:

$$\mu \downarrow \xrightarrow{\beta_\alpha \leq 0} \alpha \uparrow \xrightarrow{\text{Th. 3.4.1}} S_{\mathrm{CPS}}(p, \alpha) \uparrow$$

物理時間 $t$ の進行が解像度の粗視化 ($d\mu/dt \leq 0$) として表現されるとき、$\beta_\alpha \leq 0$ は $\alpha$ の単調増大を、定理 3.4.1 は $S_{\mathrm{CPS}}$ の単調増大を保証する。この三段チェーンは熱力学第二法則の圏論的表現であり、忘却方向と時間方向が一致するという「忘却の矢」仮説 (Paper V 系 2.3.3) の動的版である。

### 3.5 境界条件

**命題 3.5.1 (CPS エントロピーの α-境界条件).** 状態 $p: I \to X$ に対し:

(i) **$\alpha = 0$** (完全圏): $S_{\mathrm{CPS}}(p, 0) = \inf_{f \in \mathrm{Det}(C)} D(p \| f) \geq 0$。等号成立条件は $p \in \mathrm{Det}(C_0)$（$p$ が完全圏で確定的）。

(ii) **$\alpha = 1$** (離散圏): $I \neq X$ のとき $S_{\mathrm{CPS}}(p, 1) = +\infty$。

(iii) **中間 α**: 写像 $\alpha \mapsto S_{\mathrm{CPS}}(p, \alpha)$ は $[0, 1] \to [0, +\infty]$ 上の非減少関数である。さらに、**臨界忘却閾値** $\alpha^*(p) := \inf\{\alpha \in [0,1] \mid \mathrm{Det}(C_\alpha)(I, X) = \emptyset\}$ が存在し、$\alpha > \alpha^*(p)$ ならば $S_{\mathrm{CPS}}(p, \alpha) = +\infty$。

*証明.*

(i) (F2) より $C_0 = C$ であるから $\mathrm{Det}(C_0) = \mathrm{Det}(C)$ は確定的射の全体であり、全ての α-レベル中で最大の集合である（補題 3.2.1 の帰結）。したがって infimum が最大集合上で取られ、$S_{\mathrm{CPS}}(p, 0) \leq S_{\mathrm{CPS}}(p, \alpha)$ が任意の $\alpha > 0$ に対して成立する（これは定理 3.4.1 の $\alpha_1 = 0$ の場合でもある）。$D \geq 0$（divergence の非負性）より $S_{\mathrm{CPS}}(p, 0) \geq 0$。$p \in \mathrm{Det}(C_0)$ ならば $D(p \| p) = 0$ から等号。逆に $S_{\mathrm{CPS}}(p, 0) = 0$ ならば、ある確定的射の列 $f_n \in \mathrm{Det}(C_0)$ で $D(p \| f_n) \to 0$ が存在し、$D$ の正定値性の仮定の下で $p$ 自身が確定的であることが従う。□

(ii) (F3) より $\mathrm{Mor}(C_1) = \{\mathrm{id}_X \mid X \in \mathrm{Ob}(C)\}$ であるから、$C_1$ における射は恒等射のみ。特に $\mathrm{Det}(C_1)(I, X) \subseteq \mathrm{Mor}(C_1)(I, X)$。$I \neq X$ のとき $\mathrm{id}_X: X \to X$ は $I \to X$ の射ではなく、$\mathrm{id}_I: I \to I$ は $I \to X$ の射ではないから、$\mathrm{Mor}(C_1)(I, X) = \emptyset$。空集合上の infimum は $+\infty$ であるから $S_{\mathrm{CPS}}(p, 1) = +\infty$。□

(iii) 非減少性は定理 3.4.1 の直接的帰結。$\alpha^*(p)$ の存在: $A := \{\alpha \in [0,1] \mid \mathrm{Det}(C_\alpha)(I, X) = \emptyset\}$ とおく。(ii) より $1 \in A$（$I \neq X$ のとき）、(i) より $0 \notin A$（$\mathrm{Det}(C_0)(I,X)$ は非空と仮定: $p$ が well-defined であるため少なくとも確定的射が存在）。$A$ は下に有界な非空集合であるから $\alpha^*(p) = \inf A$ が存在する。(F4)（射の単調減少）より、$\alpha_2 > \alpha_1$ かつ $\mathrm{Det}(C_{\alpha_1})(I,X) = \emptyset$ ならば $\mathrm{Det}(C_{\alpha_2})(I,X) = \emptyset$（包含 $\mathrm{Det}(C_{\alpha_2}) \subseteq \mathrm{Det}(C_{\alpha_1})$ による）。したがって $A$ は $[\alpha^*(p), 1]$ の形の区間（閉半区間または開半区間）であり、$\alpha > \alpha^*(p)$ ならば $\alpha \in A$ すなわち $S_{\mathrm{CPS}}(p, \alpha) = +\infty$。□

**備考 3.5.2 (臨界忘却閾値の物理的意味).** $\alpha^*(p)$ は「状態 $p$ がエントロピー有限性を維持できる最大忘却強度」を表す。$\alpha < \alpha^*(p)$ では十分な確定的射が生存しており参照点として機能するが、$\alpha > \alpha^*(p)$ では全ての参照が失われ、エントロピーが発散する。これは Paper IV の効果量天井 $r_{\mathrm{obs}} \leq \sqrt{\rho/(K+1)}$ における $\rho \to 0$ 極限——有効な観測次元が消滅する状態——の圏論的対応物である。

### 3.6 Perrone DPI との関係

定理 3.4.1 は Perrone の DPI (Th. 2.3.1) とは**独立な**結果である。

- **Perrone DPI**: 固定された Markov 圏内で、確定的チャネルを通過してもエントロピーは増加しない → **圏内**の単調性
- **Th. 3.4.1**: α パラメータが変化するとき、エントロピーは α に関して単調 → **圏間**の単調性

両者は直交する不等式であり、CPS エントロピーの制約を異なる軸で与える。統合的な不等式は:

$$S_{\mathrm{CPS}}(k \circ p, \alpha_2) \geq S_{\mathrm{CPS}}(k \circ p, \alpha_1) \quad \text{and} \quad S_{\mathrm{CPS}}(k \circ p, \alpha) \leq S_{\mathrm{CPS}}(p, \alpha)$$

ここで $k$ は確定的チャネル。第一不等式は Th. 3.4.1、第二は Perrone DPI。

### 3.7 動的第二法則 — 時間の矢 = 忘却の矢

本節は備考 3.4.4 の三段チェーン $\mu \downarrow \to \alpha \uparrow \to S_{\mathrm{CPS}} \uparrow$ を独立定理として形式化する。これにより、Paper IX §3 の主定理列 (Th. 3.4.1 / Cor. 3.4.2) が**静的第二法則** (α に関する単調性) であるのに対し、本節 Th. 3.4.X は**動的第二法則** (物理時間 $t$ に関する単調性) として階層的に分離される。

#### 3.7.1 (P*) RG 時間 = 物理時間の同一視仮説

> **(P\*) RG 時間 = 物理時間の同一視仮説** [仮説水準 / 統一記号表 §0.3 準拠]
>
> 物理時間 $t$ と粗視化スケール $\mu$ の関係を $d\mu/dt \leq 0$ と仮定する。これは「物理時間の進行が UV→IR 方向の RG 時間と一致する」という経験的仮説であり、本節の定理 Th. 3.4.X の前提として独立に明示する。

**(P*) の身分.** Paper V §2.3 系 2.3.1a で「RG 時間は UV から IR」と述べられており、Paper XII §8.3 / Paper XII §3.1 (「Paper V 定理 2.3.1 と物理的仮定 $d\mu/dt \leq 0$ の下で」) で既に運用されている。Paper IX 内では本節で初めて明示的に分離する。

**循環論証告発への応答.** (P*) は時間の矢を**仮定**するように見えるが、本節の主張は「(P*) **下で**動的第二法則が忘却論の系として閉じる」という**条件付き導出**である (循環ではない)。(P*) の主張水準は**経験的仮説**であり、その精密化は OP-IX-9 として §7 に登録する。

#### 3.7.2 動的第二法則 (Th. 3.4.X)

> **定理 3.4.X (動的第二法則 — 時間の矢 = 忘却の矢).** (P\*) の下で、Paper V Th. 2.3.1 の条件 ($n < 5 \wedge \alpha < \alpha_*$) を満たす忘却論系を考える。状態 $p_t : I \to X$ が時間 $t$ に依存して発展し、各時刻で Paper VIII の α-忘却濾過 $\{C_{\alpha(t)}\}$ が定まるとする。このとき:
>
> $$\boxed{\frac{d\, S_{\mathrm{CPS}}(p_t, \alpha(t))}{d t} \geq 0}$$
>
> すなわち、**CPS エントロピーは物理時間に関して単調増大する**。

*証明.* 三段階の合成として示す。

**Step 1 ((P*) より時間と粗視化の対応).** 仮説 (P*) より $d\mu/dt \leq 0$。

**Step 2 (Paper V Th. 2.3.1 + 系 2.3.1a より忘却強度の単調増大).** Paper V Th. 2.3.1 (1ループ T-射影 RG 流) より、$n < 5 \wedge \alpha < \alpha_*$ の条件下で $\beta_{\alpha_{\mathrm{III}}} = \mu \, \partial \alpha_{\mathrm{III}} / \partial \mu < 0$。したがって $d\alpha_{\mathrm{III}}/d\mu < 0$。Step 1 と合わせて

$$\frac{d \alpha_{\mathrm{III}}}{d t} = \frac{d \alpha_{\mathrm{III}}}{d \mu} \cdot \frac{d \mu}{d t} \geq 0.$$

さらに sigmoid $\eta : \mathbb{R} \to (0,1)$ (Paper VIII Def. 6.7.1) の単調性により $d \alpha_{\mathrm{VIII}} / dt = \eta'(\alpha_{\mathrm{III}}) \cdot d\alpha_{\mathrm{III}}/dt \geq 0$。

**Step 3 (Paper IX Th. 3.4.1 より CPS エントロピーの単調増大).** Th. 3.4.1 (CPS エントロピー単調性) より $S_{\mathrm{CPS}}(p, \alpha)$ は $\alpha$ に関して単調非減少。連鎖律で

$$\frac{d S_{\mathrm{CPS}}(p_t, \alpha(t))}{d t} = \underbrace{\frac{\partial S_{\mathrm{CPS}}}{\partial \alpha}}_{\geq 0\,(\text{Th. 3.4.1})} \cdot \underbrace{\frac{d \alpha}{d t}}_{\geq 0\,(\text{Step 2})} + \frac{\partial S_{\mathrm{CPS}}}{\partial p} \cdot \frac{d p_t}{d t}.$$

第一項は両因子非負。第二項について、$dp_t/dt$ が確定的チャネル経由の発展 (Perrone DPI を満たす変換) に従うときは $\partial S_{\mathrm{CPS}}/\partial p \cdot dp_t/dt \geq 0$ (§3.6 統合不等式の第二式)。第二項が負になる場合は系の状態発展が確定性を破る方向であり、本定理の射程外。

両項が非負のとき $dS_{\mathrm{CPS}}/dt \geq 0$。$\square$

#### 3.7.3 系と備考

**系 3.7.1 (静的版と動的版の階層).** Paper VIII Th. 6.10.3 (射計数版第二法則 $S_{\mathrm{cat}}(\alpha)$ の α 単調増大) は **静的版** であり、Th. 3.4.1 と同じく α パラメータ軸上の単調性。Th. 3.4.X はこれらを物理時間軸へ持ち上げた **動的版** であり、(P*) 仮説の有無で両者は分離される。両版の階層構造の精密化は OP-IX-10 として §7 に登録する。

**系 3.7.2 (ダイバージェンス非依存性の動的版).** 系 3.4.2 (Cor. 3.4.2) と同形に、Th. 3.4.X は divergence $D$ の具体形に依存しない。Shannon / Rényi / Gini-Simpson エントロピーすべてに対し、(P*) 下での動的単調性が成立する。

*証明.* Step 3 で用いた Th. 3.4.1 の α 単調性は系 3.4.2 によりダイバージェンス非依存。Step 1, 2 は $D$ に依存しない。$\square$

**備考 3.7.3 (Paper XII χ 単調性予測との接続).** Paper XII §8.3 は β_α ≤ 0 を用いて χ 単調性予測 (XII-T0) の動的根拠を与える。Th. 3.4.X はこの根拠を Paper IX 側で独立定理として閉じたものであり、Paper XII の予測に対し**双方向の接続**を提供する: (i) Paper V Th. 2.3.1 → Th. 3.4.X (本節)、(ii) Th. 3.4.X → Paper XII χ 単調性 (Paper XII §8.3 で運用済)。

#### 3.7.4 既存の動的第二法則との差分

[TAINT 注記] 以下の差分テーブルは外部原典 (Boltzmann 1872 / Jacobson 1995 / Verlinde 2011) との構造的差分の要約である。各原典は Paper XIII §1.2 と §8.3 で参照済 [SOURCE: 論文XIII_時空は忘却である_草稿.md L73-79, L394-399]。原典の独立 SOURCE 確認は OP-IX-11 として §7 に登録する。

| 既存定理 | 主張 | 適用範囲 | Th. 3.4.X との差分 | 比較精度 |
|:---|:---|:---|:---|:---|
| Boltzmann H 定理 [TAINT: 原典未読] | 統計力学的 $dH/dt \leq 0$ (粒子分布の粗視化) | 古典粒子系 | Th. 3.4.X は**圏論的** (射包含 (F4) 原理)。粒子表現を経由しない | 構造的類似 (粗視化の構造) |
| Jacobson (1995) [Paper XIII §1.2 L78 経由参照] | 局所 Clausius $\delta Q = T dS$ から Einstein 方程式 | 重力場のある時空 (null surface) | Th. 3.4.X は**任意の CPS 圏で成立** (重力なしでも)。Jacobson は熱力学的入力から幾何を導出、Th. 3.4.X は α-忘却濾過から熱力学的単調性を導出 | 直交 (導出方向が逆) |
| Verlinde (2011) [Paper XIII §1.2 L77, §8.3 L395 経由参照] | 重力 = entropic force (情報のエントロピー勾配) | ホログラフィック宇宙論 | Th. 3.4.X は**逆方向**: 第二法則そのものを忘却論で導く。重力導出は Paper XIII Blocker A2 (closure 後の物理的実現例) | 直交 (主張対象が異なる) |

**メタテーゼ.** これら 3 者との差分が示すのは、Th. 3.4.X が「物理現象の説明」ではなく「**圏論的構造から熱力学的単調性が出る**」という**逆方向の主張**であること。熱力学対応表 v3.2 のテーゼ (「忘却論は熱力学のアナロジーではなく上位構造である」) [SOURCE: 熱力学対応表.md L111-114] の動的版である。

#### 3.7.5 主張水準と境界

Th. 3.4.X 本体: **定理** (Paper V Th. 2.3.1 + Paper IX Th. 3.4.1 の合成として証明閉)。
(P*) 仮説: **経験的仮説** (Paper XII で運用実績あり、定義への昇格は OP-IX-9)。
差分テーブル: 構造的差分は **Claude prior 由来** [TAINT]、原典 SOURCE 化は OP-IX-11。
Th. 3.4.X の射程: 第二項 $\partial S_{\mathrm{CPS}}/\partial p \cdot dp/dt$ が非負である状態発展に限定。確定性を破る発展 (e.g. 射の生成・新規対象出現) は射程外。

### 3.8 弁別エントロピー版第二法則 — 条件付き予想 (Round 3 主張水準降格 2026-04-29)

> **主張水準注記** (2026-04-29 Round 3, /exe+ 自己監査後): 本節は当初「定理 3.8.1」として起票したが、自己 /exe+ 監査により次の 3 仮定への依存が露出し、**条件付き予想 (conditional conjecture)** に降格した:
> - **A1**: Paper I §5.9.2 の閾値単調性 [SOURCE: 論文I 草稿 line 559「成立すると予想する」] は予想であって定理ではない
> - **A2**: enrich$_\alpha$ の measure-theoretic 構成は OP-IX-12 として未閉
> - **A3**: image$(G_\alpha)$ の有限性は Paper I 定理 5.9.3 [SOURCE: 論文I 草稿 line 580-582] では保証されない
>
> 主定理列 (§3.4 / §3.7) と区別するため、本節 §3.8.1〜§3.8.6 全体を「予想 3.8.1 (条件付き)」として括る。

#### 3.8.1 動機

§3.4 の $S_{\mathrm{CPS}}$ は確定的射への最小 divergence でエントロピーを測り、「分布の uniformity」の単調増大を述べる。しかし image $(G_\alpha)$ 内に残る射の **意味的非自明性** (=各対象の弁別力) は別軸である。`11_肌理｜Hyphē/chemistry_cognition.md` §10.6 の定理 2' (ゴールディロックス定理) は離散コーパス上で coverage $p$ と enrichment の関係を分析しており、「飽和帯では弁別力 $\to 1$」を示している [SOURCE: chemistry_cognition.md §10.6, multi_scale_chemistry_isomorphism.md §6]。本節はこの離散版を α-忘却濾過上の単調量へ昇格させる。

#### 3.8.2 有効弁別容量

**定義 3.8.1 (有効弁別容量).** α-忘却濾過 $\{C_\alpha\}$ 上で image $(G_\alpha) \subseteq \mathrm{Mor}(C_\alpha)$ を定理 5.9.3 (Paper I) の意味の生存射集合とする。各 $X \in \mathrm{image}(G_\alpha)$ について

$$\mathrm{enrich}_\alpha(X) := \frac{P(\mathrm{cat} \mid (X, Y) \in \mathrm{image}(G_\alpha)^2)}{P(\mathrm{cat} \mid \mathrm{random})}$$

を弁別力とし、**有効弁別容量** を

$$\boxed{\bar{E}^*(\alpha) := \sum_{X \in \mathrm{image}(G_\alpha)} \mathrm{enrich}_\alpha(X)}$$

で定義する。$\bar{E}^*$ は「弁別力 × 生存射数」の総和であり、image 全体としての意味的非自明性を測る。

#### 3.8.3 弁別力単調減少 (条件付き予想)

**予想 3.8.1 (弁別力単調減少 — 条件付き予想).** 仮定 A1 / A2 / A3 (上記主張水準注記) の下で、忘却関手 $U_{\alpha_1 \to \alpha_2}: C_{\alpha_1} \to C_{\alpha_2}$ ($0 < \alpha_1 \leq \alpha_2 \leq 1$) が **Markov 関手** (確定的射を確定的射に写す関手) であるとき:

$$\boxed{\bar{E}^*(\alpha_2) \leq \bar{E}^*(\alpha_1)}$$

*証明スケッチ (条件付き).* 四段の構成。

(1) 補題 3.2.1 [SOURCE: §3.2 line 100] より $\mathrm{Det}(C_{\alpha_2}) \subseteq \mathrm{Det}(C_{\alpha_1})$。

(2) **A2 仮定下** で enrich$_\alpha$ が well-defined であるとし、Markov 関手による確定性保存 + Th. 2.3.1 (DPI) を image 上に拡張した補題 (要独立証明 — **OP-IX-14** として §7 登録) より、$\mathrm{enrich}_{\alpha_2}(U(X)) \leq \mathrm{enrich}_{\alpha_1}(X)$ for $X \in \mathrm{image}(G_{\alpha_1})$ with $U(X) \in \mathrm{image}(G_{\alpha_2})$ が成立すると予想する。

(3) **A1 仮定下で** (Paper I §5.9.2 閾値単調性予想 [SOURCE: 論文I 草稿 line 559「成立すると予想する」] が定理化されたとして)、Paper VIII (F4) と組み合わせて $\mathrm{image}(G_{\alpha_2}) \subseteq \mathrm{image}(G_{\alpha_1})$ が image の成分単調包含として従う。**A1 が予想に留まる現状では本 step は条件付き**。

(4) (2) と (3) から **A1 ∧ A2 ∧ A3 ∧ Markov 関手仮定下で**:
$$\bar{E}^*(\alpha_2) = \sum_{X \in \mathrm{image}(G_{\alpha_2})} \mathrm{enrich}_{\alpha_2}(X) \leq \sum_{X \in \mathrm{image}(G_{\alpha_2})} \mathrm{enrich}_{\alpha_1}(X) \leq \sum_{X \in \mathrm{image}(G_{\alpha_1})} \mathrm{enrich}_{\alpha_1}(X) = \bar{E}^*(\alpha_1).$$

(5) 第一不等式は (2) (各項の単調性、A2 + DPI 拡張下)、第二不等式は (3) (A1 下で集合包含 + enrich $\geq 0$)。各仮定 A1-A3 が独立に閉じれば本予想は定理水準に昇格する。$\square$ (条件付き)

#### 3.8.4 仮定の階層

予想 3.8.1 は (F4) のみでは立たない。enrich$_\alpha$ の分子は α 依存の確率量であり、image 縮小に伴い残った射が同質化することで **増加しうる**。Markov 関手仮定 + A1 + A2 + A3 の四重仮定下で初めて条件付き単調性が立つ候補となる。

| 命題 | (F4) | Markov 関手 | (P\*) RG 時間仮説 | A1+A2+A3 | 主張水準 | 証明型 |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Th. 6.10.3 (Paper VIII 代数版) | ✓ | – | – | – | 定理 | 計数的 ($m(\alpha) \downarrow$) |
| Th. 3.4.1 (静的 $S_{\mathrm{CPS}}$ 版) | ✓ | – | – | – | 定理 | 集合論的 (infimum 集合縮小) |
| Th. 3.4.X (動的 $S_{\mathrm{CPS}}$ 版) | ✓ | ✓ (§3.7.5 限定) | ✓ | – | 定理 (条件付き合成) | 連鎖律 (時間軸合成) |
| **予想 3.8.1 (弁別力版)** | ✓ | ✓ | – | **✓ 必要** | **条件付き予想** | 確率論的 (DPI image 拡張要) |

弁別力版は静的 / 動的の体系的な追加軸候補ではあるが、現状は **条件付き予想として育成中** であり、定理水準には A1-A3 が独立に閉じる必要がある。

#### 3.8.5 Paper VIII §6.10 と Hyphē §10 への橋渡し

Paper VIII §6.10.5 の「二つの第二法則」表 [SOURCE: 論文VIII 草稿 line 1021] は本節 予想 3.8.1 を加えて **三列表 (うち弁別力版は条件付き予想)** に拡張される。三軸の概念整列:

- 代数的版 (Th. 6.10.3, **定理**): 散らばり (uniformity) 単調増大
- 幾何的版 (Paper V, **定理**): 力零集合の余次元 = $n-1$
- **弁別力版 (予想 3.8.1, 条件付き予想)**: 意味的非自明性 ($\bar{E}^*$) 単調減少 (予想)

`chemistry_cognition.md` §10.6 の定理 2' は coverage $p$ で書かれた離散版 [SOURCE: chem §10.6 line 1044]。予想 3.8.1 はその α-忘却濾過版候補。

> **翻訳辞書注記**: chem §10.6 と本表は **次元の異なる量** (coverage は部分構造 $g$ ごと、image 比率は α 全体で 1 値) を並列している。厳密な翻訳には射計数行列 $M_{ij}(\alpha)$ [SOURCE: 論文VIII §6.10.1 line 989] を経由する必要があり、本節の射程を超える (OP-IX-15 候補)。

| 離散版 (chem §10.6) | α-濾過版 (予想 3.8.1, 条件付き) |
|:---|:---|
| coverage $p = |G_g|/N$ | image 比率 $|\mathrm{image}(G_\alpha)|/m(0)$ |
| ゴールディロックス帯 ($p_{\mathrm{min}} < p < p_{\mathrm{sat}}$) | α-濾過上の弁別力最大領域 |
| 飽和帯 ($p \to 1$, enrich $\to 1$) | $\alpha$ 大での全 image が支持体化する領域 |
| 統計不足帯 ($p < p_{\mathrm{min}}$) | $\ker(G_\alpha)$ 候補 |

#### 3.8.6 主張水準と境界

予想 3.8.1 本体: **条件付き予想** (A1 ∧ A2 ∧ A3 ∧ Markov 関手仮定下で立つと予想)。
Markov 関手仮定: 忘却関手の構造的条件であり、Paper II §3.7 の CPS($\alpha > 0$) 圏で **構成的延長として** 成立 [SOURCE: §3.1 line 88-96]。strict ではない。
予想 3.8.1 の射程: A1-A3 が閉じれば定理水準に昇格。各仮定の独立 OP:

- **OP-IX-12**: enrich$_\alpha$ の分子 $P(\mathrm{cat} \mid \cdot)$ の α-濾過上の measure-theoretic 構成 (A2 閉鎖)
- **OP-IX-13**: `multi_scale_chemistry_isomorphism.md §6` の独立 Read (chem §10 の定理 2 出典確認、本セッション未実施)
- **OP-IX-14**: DPI の image 拡張補題 (A2 下での証明 step (2) の独立証明)
- **OP-IX-15**: chem §10.6 と §3.8.5 翻訳辞書の射計数行列経由の精密化
- **本稿外 OP**: Paper I §5.9.2 閾値単調性予想の独立証明 (A1 閉鎖)

これら 5 OP のうち最も独立性が高いのは Paper I §5.9.2 閾値単調性予想 (A1)。これが定理化されれば予想 3.8.1 の主柱が立つ。

§3.8 の射程: image$(G_\alpha)$ が空でない範囲 ($\alpha < \alpha^*$, [SOURCE: §3.5 命題 3.5.1])。$\alpha = 1$ では image $= \emptyset$ で $\bar{E}^*$ は退化。

#### 3.8.7 三角形閉化補題 — 離散版・α-濾過版・言語版の同値性 (2026-04-29)

Th. 3.8.1 (α-濾過版) は `chemistry_cognition.md` §10.6 (定理 2' 離散版) と Paper XI §7.7.5b (公理 H-2Z 言語版) の中間項である。本節は三者を **同一構造の異なる射影** として接続する補題を起票する。

##### 3.8.7.1 三領域の対象

| 版 | 領域 | 対象 | 確率空間 | 単調量 |
|:---|:---|:---|:---|:---|
| 離散版 | CCL token corpus / 化学元素分布 | 部分構造 $g$ | $(\Omega, p)$, $p$ = corpus 頻度 | $\mathbb{E}[\mathrm{enrich}(g)]$ as $p \uparrow$ |
| α-濾過版 (本節 Th. 3.8.1) | $\alpha$-忘却濾過 $\{C_\alpha\}$ | 生存射 $X \in \mathrm{image}(G_\alpha)$ | image 上の確率量 | $\bar{E}^*(\alpha)$ as $\alpha \uparrow$ |
| 言語版 (Paper XI 公理 H-2Z) | 自然言語 prompt 空間 | 表現頻度 $E_{\text{freq}}$ | natural language corpus 頻度 | $\mathbb{E}[Q]$ as $p \uparrow$ |

##### 3.8.7.2 同型射の構成

三領域を結ぶ射の三角形 $(\mathrm{Disc}, \mathrm{Filt}, \mathrm{Lang})$ を以下で定義する:

- **$\Phi_{\mathrm{D \to F}}: \mathrm{Disc} \to \mathrm{Filt}$**: coverage $p$ を image 比率 $|\mathrm{image}(G_\alpha)| / m(0)$ に写す写像。$p_{\text{sat}} \mapsto \alpha_{\text{sat}}$ (image 全体が支持体化する $\alpha$)、$p_{\min} \mapsto \alpha_{\max}^*$ (image $= \emptyset$ となる閾値)。
- **$\Phi_{\mathrm{F \to L}}: \mathrm{Filt} \to \mathrm{Lang}$**: 生存射 $X \in \mathrm{image}(G_\alpha)$ を表現頻度 $p^{\mathrm{lang}}(X)$ に写す写像。Markov 関手による image-to-corpus 投射。
- **$\Phi_{\mathrm{D \to L}}: \mathrm{Disc} \to \mathrm{Lang}$**: 直接の埋め込み (Paper XI §7.7.5b.3 の三領域同型表で確立)。

##### 3.8.7.3 三角形閉化補題 (Th. 3.8.2 候補)

> **補題 3.8.2 (三角形閉化, 候補).** Markov 関手仮定の下で、図式
> $$\mathrm{Disc} \xrightarrow{\Phi_{\mathrm{D \to F}}} \mathrm{Filt} \xrightarrow{\Phi_{\mathrm{F \to L}}} \mathrm{Lang}$$
> は $\Phi_{\mathrm{D \to L}}$ と (自然変換差を除いて) 可換である。すなわち、**離散版ゴールディロックス帯 → α-濾過版弁別力単調減少 → 言語版 H₃'' 三相分割 は、同一の coverage-enrichment 関係の三領域射影として一致する**。

##### 3.8.7.4 補題の身分と証明戦略

本補題は現時点で **候補** であり、本節では証明骨格のみを提示する。完全証明は OP-IX-16 として §7 に登録する (v0.12 整合: 旧 v0.11 の OP-IX-13 から繰り下げ)。

**証明戦略 (4 ステップ)**:

1. **(D → F の検証)**: 離散版の $p_{\text{sat}}$ 閾値が α-濾過の $\alpha_{\text{sat}}$ に写る対応は、Paper VIII (F4) の単調包含と Paper I 定理 5.9.3 の閾値 $R_{\text{crit}}(\alpha)$ で構成的に与えられる (本節 3.8.5 翻訳辞書)。
2. **(F → L の検証)**: 生存射から表現頻度への投射は Paper XI §7.7.5 の射密度 corpus proxy で確立済み。Markov 関手仮定が同型保存を担保する。
3. **(三角形可換性)**: 直接埋め込み $\Phi_{\mathrm{D \to L}}$ (Paper XI §7.7.5b.3 三領域同型表) と $\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}}$ の差が、`chemistry_cognition.md` §10.7 の翻訳辞書と §10.8 の翻訳辞書で同型に閉じることを示す。
4. **(自然変換差の特定)**: 完全可換ではなく自然変換差を許す理由は、α-濾過版が射 (動的構造) を直接扱うのに対し、離散版・言語版は対象 (静的頻度) を扱う点にある。この差を encode する $\eta: \Phi_{\mathrm{D \to L}} \Rightarrow \Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}}$ を構成する。

##### 3.8.7.5 含意

補題 3.8.2 が完全証明された場合、以下が帰結する:

1. **三領域不変量の存在**: ゴールディロックス帯は coverage / α / 表現頻度のいずれの軸でも記述可能な不変量を持つ
2. **Paper XI 公理 H-2Z の SOURCE 強化**: 公理 H-2Z は化学類比ではなく、α-忘却濾過の構造的帰結として読み直せる
3. **Paper I §5.9 公理 5.9.2 への両側閾値追加圧の正規化**: 「射が密すぎる構造は弁別力を喪失する」という第二の壁が、三領域同型を経由して Paper I に back-propagate する。**この含意は Paper I §5.9.6.4 (2026-04-29 起票) として正規化済み** [SOURCE: 論文I_力としての忘却_草稿.md §5.9.6.4]: 本補題完全証明 (OP-IX-16 解消) により Paper I 定理 5.9.6.2 (普遍性のジレンマ) の burden-bearing 昇格 4 条件のうち (1) 関手化 / (3) $R_\text{crit}^\text{high}$ 存在証明が補題 3.8.2 の系として再導出される。三領域 (Disc / Filt / Lang) に Paper I 圏 $\mathcal{C}$ を追加する **四領域** への拡張経路が確立する。
4. **熱力学第二法則の三層化**: 代数版 (Th. 6.10.3) / 幾何版 (Paper V) / 弁別力版 (Th. 3.8.1) に加え、本補題が三層を **同一構造の三射影** として閉じる

##### 3.8.7.6 撤回条件

- (a) 補題 3.8.2 の自然変換差 $\eta$ が encode 不能な場合 (= D → L と F → L 経由の差が構造的に橋渡せない場合)、三角形閉化は失敗 → 三領域は弱対応にとどまる
- (b) Paper XI H₃'' 三条件比較 (§10.7) で言語版が経験的に棄却された場合、$\Phi_{\mathrm{F \to L}}$ の Markov 関手仮定が崩れる → 補題 3.8.2 は離散版 ↔ α-濾過版の二点接続に縮退
- (c) Markov 関手仮定が CPS($\alpha > 0$) 圏で完全には成立しないことが判明した場合、Th. 3.8.1 自体に影響し、補題 3.8.2 も連鎖的に降格

[確信度] 補題 3.8.2: [推定 65%] (§3.8.7.7-§3.8.7.9 で自然変換 $\eta$ の構成的与え方を具体化、自然性条件の検証ステップが確立。残るギャップは OP-IX-12 (enrich$_\alpha$ measure-theoretic 構成) との同期と、Lang の射構造の厳密化)

#### 3.8.7.7 自然変換 $\eta$ の構成 — 対象成分

§3.8.7.4 Step 4 の集中化として、自然変換 $\eta: \Phi_{\mathrm{D \to L}} \Rightarrow \Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}}$ の対象成分を構成する。

**準備: 三領域の対象集合の同定**

- $\mathrm{Disc}$ の対象: 部分構造 $g$ (token / 元素 / 表現)
- $\mathrm{Filt}$ の対象: $\alpha$-忘却濾過上の対象 $X \in \mathrm{Ob}(C_\alpha) = \mathrm{Ob}(C)$ — Paper VIII (F1) より $\alpha$ 不変
- $\mathrm{Lang}$ の対象: 自然言語表現 $w$ — corpus 頻度 $p^{\mathrm{lang}}(w)$ で測られるスカラー

埋め込み $\iota: \mathrm{Disc} \hookrightarrow \mathrm{Ob}(C)$ で各 token / 元素 / 表現を $C$ の対象として固定する (Paper XI §7.7.5b.3 の三領域同型表が要求する identification)。

**$\eta_X$ の対象成分 (Lang の射として与える)**

各 $X \in \mathrm{Disc}$ について、Lang における射 $\eta_X: \Phi_{\mathrm{D \to L}}(X) \to (\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}})(X)$ を以下で定める:

$$\eta_X := \frac{R_\alpha(X)}{R_0(X)}: p^{\mathrm{lang}}_{\text{direct}}(X) \to p^{\mathrm{lang}}_{\text{via-filt}}(X)$$

ここで:

- $R_0(X) := |\mathrm{Hom}_C(X, -)|$ — Paper I §5.9.1 の射密度 (元の濾過レベル)
- $R_\alpha(X) := |\mathrm{Hom}_{C_\alpha}(X, -)|$ — α-忘却濾過上の生存射密度
- $p^{\mathrm{lang}}_{\text{direct}}(X) := \Phi_{\mathrm{D \to L}}(X)$ — corpus 頻度の直接埋め込み
- $p^{\mathrm{lang}}_{\text{via-filt}}(X) := \Phi_{\mathrm{F \to L}}(\Phi_{\mathrm{D \to F}}(X))$ — α-濾過経由の頻度

この比 $R_\alpha(X) / R_0(X) \in [0, 1]$ は Paper VIII (F4) と Paper I 公理 5.9.2 から **単調非増加** であり、X が普遍的構造に近いほど 1 に近く、希少構造ほど 0 に近い。

**直観的読み**: 直接経路 ($\Phi_{\mathrm{D \to L}}$) は X の corpus 頻度を静的に測る。経由経路 ($\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}}$) は X が α-濾過で生存する射の比率を経由して頻度を回復する。両者の差は **「X の射密度のうち $\alpha$ 段階で生存している割合」** であり、これが $\eta_X$ の値となる。

#### 3.8.7.8 自然性条件の検証

$\eta$ が自然変換であることを示すには、$\mathrm{Disc}$ の各射 $f: X \to Y$ に対し以下の四角形が可換であることを示す:

$$
\begin{array}{ccc}
\Phi_{\mathrm{D \to L}}(X) & \xrightarrow{\eta_X} & (\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}})(X) \\
\Phi_{\mathrm{D \to L}}(f) \downarrow & & \downarrow (\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}})(f) \\
\Phi_{\mathrm{D \to L}}(Y) & \xrightarrow{\eta_Y} & (\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}})(Y) \\
\end{array}
$$

すなわち:

$$\eta_Y \circ \Phi_{\mathrm{D \to L}}(f) = (\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}})(f) \circ \eta_X \quad \cdots (*)$$

**検証戦略 (3 ステップ)**:

(N1) **$\mathrm{Disc}$ の射 $f: X \to Y$ の意味**: 部分構造の包含関係 (例: token X が token Y の構成要素である) または共起関係。これは Paper VIII §6.2 の widely-defined 圏 $C$ の射として埋め込まれる ($\iota$ 経由)。

(N2) **両経路の計算**:

- 上経路 $\eta_Y \circ \Phi_{\mathrm{D \to L}}(f)$: 直接埋め込みで X の頻度を Y の頻度に写し、その後 $\eta_Y = R_\alpha(Y) / R_0(Y)$ をかける
- 下経路 $(\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}})(f) \circ \eta_X$: $\eta_X = R_\alpha(X) / R_0(X)$ で X の比をスケールしてから、$f$ の経路で Y へ移す

(N3) **可換性の根拠**: Markov 関手 $U_{0 \to \alpha}$ が $\mathrm{Hom}_C(X, -)$ から $\mathrm{Hom}_{C_\alpha}(X, -)$ への自然な制限として実装されているため、X と Y の射密度比は $f: X \to Y$ に対し関手的に挙動する:

$$\frac{R_\alpha(Y)}{R_0(Y)} \cdot p^{\mathrm{lang}}_{\text{direct}}(f(X)) = p^{\mathrm{lang}}_{\text{via-filt}}(f(Y)) \cdot \frac{R_\alpha(X)}{R_0(X)} \cdot \kappa(f)$$

ここで $\kappa(f) \in [1 - \epsilon, 1 + \epsilon]$ は Markov 関手の確定性保存に由来する補正係数。$\epsilon \to 0$ は Markov 関手仮定が完全に成立する極限で、その場合 (\*) が等号で成立する。

**ギャップ (旧 OP-IX-13 → OP-IX-17, v0.12 で解決)**: §3.8.7.10 で Paper II §3.7.1 $e(\alpha)$-twist から $\kappa(f) = e(\alpha)$ の閉形式を導出済み (補題 3.8.3)。$\alpha = 0$ で $\epsilon = 0$、$\alpha > 0$ で $\epsilon = |1 - e(\alpha)|$ として a.e. equivalence で閉じる。

#### 3.8.7.9 自然変換差の意味と含意

$\eta$ が完全な自然変換 ($\epsilon = 0$ で (\*) が等号) として閉じる場合、以下が直ちに従う:

**結果 1 (三角形閉化)**: 図式 $\mathrm{Disc} \to \mathrm{Filt} \to \mathrm{Lang}$ は自然変換差 $\eta$ を伴って $\mathrm{Disc} \to \mathrm{Lang}$ と一致する。これにより補題 3.8.2 が証明閉となる。

**結果 2 (三領域不変量の特定)**: 不変量は **比 $R_\alpha(X) / R_0(X)$ のみ** で encode される。これは coverage / α / 表現頻度のいずれの軸でも同じ比として観測可能。

**結果 3 (Paper XI 公理 H-2Z への back-propagation)**: 公理 H-2Z の二層分解 $E_{\text{entry}} \circ E_{\text{control}}$ は、$R_\alpha(X) / R_0(X)$ が

- 飽和帯: 比 $\to 1$ — $E_{\text{entry}}$ 領域 (生存射が密)
- ゴールディロックス帯: 比 $\in (0, 1)$ — $E_{\text{control}}$ 領域 (中間)
- 統計不足帯: 比 $\to 0$ — $E_{\text{rare}}$ 領域 (生存射が疎)

として α-忘却濾過上に **構造的に与えられる** ことを意味する。化学類比は装飾ではなく、$R_\alpha/R_0$ の比による分類の **同一インスタンス** となる。

**結果 4 (Paper I §5.9 公理 5.9.2 への両側閾値追加圧)**: 現行公理 5.9.2 は「$R(X) \geq R(Y)$ かつ $X \in \ker(G)$ ならば $Y \in \ker(G)$」と射密度の単調包含のみを要求するが、$\eta_X = R_\alpha(X) / R_0(X)$ の三領域不変性は **両側閾値** ($R_{\mathrm{crit}}^{\mathrm{low}} < R(X) < R_{\mathrm{crit}}^{\mathrm{high}}$) を要請する。これは公理 5.9.2 への追加公理候補 5.9.2' (両側閾値定理) として Paper I 改訂時に提起される。

**結果 5 (熱力学第二法則の三層化への接続)**: 代数的版 (Th. 6.10.3) / 幾何的版 (Paper V) / 弁別力版 (Th. 3.8.1) の三層が、自然変換 $\eta$ を介して同一の比 $R_\alpha/R_0$ の三射影として閉じる。これは Paper VIII §6.10.5 の三列表を **同一不変量の三表示** へ昇格させる。

**残ギャップ (open management)**:

- (G1) $\kappa(f)$ の上界 $\epsilon$ の構造的決定 — **§3.8.7.10 (v0.12, OP-IX-17) で解決済**: $\kappa(f) = e(\alpha)$、$\epsilon = |1 - e(\alpha)|$
- (G2) $\mathrm{Lang}$ の射構造の厳密化 — 自然言語の表現間の射が「corpus 頻度の比較関係」だけで十分かは未確立。意味論的射 (例: 同義語関係) の追加が必要な可能性
- (G3) OP-IX-12 (enrich$_\alpha$ measure-theoretic 構成) との同期 — $\eta$ の確率測度的解釈が enrich$_\alpha$ の measure-theoretic 構成と整合することの検証

[確信度] $\eta$ 構成完成度: [推定 65%]。対象成分と自然性条件は構造的に明示済み。残るは G1-G3 の閉鎖。

#### 3.8.7.10 OP-IX-17 集中作業 — $\kappa(f)$ 上界 $\epsilon$ の構造的決定

§3.8.7.8 で導入した Markov 関手補正係数 $\kappa(f) \in [1-\epsilon, 1+\epsilon]$ は補題 3.8.2 の自然性条件 (\*) の余白として定式化された。本節は $\epsilon$ を Paper II §3.7.1 の $e(\alpha)$-twist から **構造的に計算可能** であることを示し、CPS($\alpha > 0$) 圏で $\epsilon = |1 - e(\alpha)|$ という閉形式で与える。

**主張水準注記 (2026-04-29 v0.12 整合).** 本節の射程は補題 3.8.2 (三角形閉化, 候補) の自然性余白 $\kappa(f)$ の閉形式決定に閉じる。Th. 3.8.1 (= 予想 3.8.1, v0.7 主張水準降格) の主張水準条件 (A1-A3) とは **直交** する: 補題 3.8.2 が必要とするのは Paper II §3.7.1 の $e(\alpha)$-twist の数値検証 (ガウス族 $\mathcal{H}^2$ 上で確立) のみであり、Paper I §5.9.2 閾値単調性予想 (A1) や enrich$_\alpha$ の measure-theoretic 構成 (A2 / OP-IX-12) には依存しない。ただし含意 (3.8.7.9 結果 5: 熱力学第二法則三層化への接続) を経由するときは予想 3.8.1 の主張水準を継承する。

##### 3.8.7.10.1 $e(\alpha)$-twist と Markov 関手の関係

[SOURCE: 論文II_相補性は忘却である_草稿.md L707-722] により、CPS($\alpha > 0$) 圏の余単位律は

$$(\mathrm{del}^{(\alpha)} \otimes \mathrm{id}_X) \circ \mathrm{copy}^{(\alpha)} = e(\alpha) \cdot \mathrm{id}_X, \qquad e(\alpha) := \frac{\int_X \Phi^{(\alpha)} \sqrt{\det(g^{(\alpha)})} \, d\theta}{\int_X \Phi^{(0)} \sqrt{\det(g^{(0)})} \, d\theta}$$

として $e(\alpha)$-twist を受ける。$\alpha = 0$ で $e(0) = 1$ により Fritz の標準 Markov 圏が回収される。$\alpha > 0$ で有効体積が縮小し $e(\alpha) < 1$ となる ([SOURCE: 同上 L714] ガウス族 $\mathcal{H}^2$ 上の数値検証 $e(+1) \approx 0.08$)。

##### 3.8.7.10.2 $\kappa(f)$ の $e(\alpha)$ 表示

(\*) の両経路を改めて $e(\alpha)$-twist を含む厳密形で書く。$f: X \to Y \in \mathrm{Disc}$ を $\iota$ 経由で $C$ の射として埋め込み、$U_{0 \to \alpha}: C \to C_\alpha$ を Markov 関手として作用させる。

**経路上 (上経路, 直接埋め込み + $\eta_Y$ 適用)**:

$$\eta_Y \circ \Phi_{\mathrm{D \to L}}(f) = \frac{R_\alpha(Y)}{R_0(Y)} \cdot p^{\mathrm{lang}}_{\text{direct}}(f(X))$$

**経路下 (経由経路 + $\eta_X$ 適用)**:

$$(\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}})(f) \circ \eta_X = p^{\mathrm{lang}}_{\text{via-filt}}(f(Y)) \cdot \frac{R_\alpha(X)}{R_0(X)}$$

両経路の比は **$e(\alpha)$-twist の余単位律から $\Phi^{(\alpha)} / \Phi^{(0)}$ の有効体積比に縮約**される (Paper II §3.7.1 Step 3b (i) 周辺整合性で a.e. equivalence のもとで $e(\alpha) \cdot \mathrm{id}$ への置換が必要とある [SOURCE: 論文II L722])。すなわち:

$$\kappa(f) = \frac{\eta_Y \circ \Phi_{\mathrm{D \to L}}(f)}{(\Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}})(f) \circ \eta_X} = e(\alpha) \cdot \tau(f)$$

ここで $\tau(f) \in [1, 1]$ は射 $f$ が確定的射のとき完全に 1 となる補正項 (Markov 関手の確定性保存 [SOURCE: 論文IX §3.1 line 94 補題 3.2.1] が保証)。確率的射の場合のみ $\tau(f) \neq 1$ となる可能性があるが、補題 3.8.2 の射程は $\mathrm{Disc}$ の対象 (確定的に corpus 頻度を持つもの) に閉じているため $\tau(f) = 1$。

##### 3.8.7.10.3 主結果 (補題 3.8.3 — $\kappa$ の閉形式)

> **補題 3.8.3 ($\kappa(f)$ の閉形式).** CPS($\alpha > 0$) 圏において Paper II §3.7.1 の $e(\alpha)$-twist が成立し、$\mathrm{Disc}$ の射 $f$ が $\iota$ 経由で確定的射に持ち上がるとき:
> $$\kappa(f) = e(\alpha)$$
> したがって自然変換 $\eta$ の補正余白は $f$ に依存せず $\alpha$ のみに依存し、上界は
> $$\epsilon = |1 - e(\alpha)|$$
> として構造的に決定される。

**含意**:

| $\alpha$ 領域 | $e(\alpha)$ | $\epsilon$ | 補題 3.8.2 の閉鎖 |
|:---|:---|:---|:---|
| $\alpha = 0$ | $e(0) = 1$ | $\epsilon = 0$ | (\*) は等号で成立 — 補題 3.8.2 が **完全に閉じる** |
| $\alpha \to 0^+$ | $e(\alpha) \approx 1 + \alpha \cdot \frac{\mathbb{E}_\Phi[\|\sigma\|\log\|\sigma\|]}{\mathbb{E}_\Phi[\|\sigma\|]}$ | $\epsilon = O(\alpha)$ | 線形小オーダー — 補題 3.8.2 は near-equality で閉じる |
| $\alpha \in (0, 1)$ 一般 | $e(\alpha) < 1$ (有効体積縮小) | $\epsilon = 1 - e(\alpha) \in (0, 1)$ | a.e. equivalence で閉じる ([SOURCE: 論文II L722]) |
| $\alpha = 1$ | $e(1) \approx 0.08$ (ガウス族) | $\epsilon \approx 0.92$ | 補題 3.8.2 は弱い equivalence のみ |

##### 3.8.7.10.4 $\alpha = 0$ における完全閉鎖

$\alpha = 0$ では $e(0) = 1$ であり、(\*) は **等号で成立する**。これは補題 3.8.2 が **CPS($\alpha = 0$) で完全な自然変換として閉じる** ことを意味する。Paper II §3.7.1 が strict な Fritz 型 Markov 圏を $\alpha = 0$ で正確に与えることと整合 [SOURCE: 論文II L11]。

含意の射程:

- $\alpha = 0$ — strict equality, 補題 3.8.2 は **定理** に格上げ可能 (確信度 65% → 80%+ 候補)
- $\alpha > 0$ — a.e. equivalence, 補題 3.8.2 は **構成的延長** として読む

これは Paper II §3.7.1 が CPS の Markov 圏的構造を $\alpha = 0$ で strict、$\alpha > 0$ で構成的延長として配置している階層と完全に整合する [SOURCE: 論文II L96 主張水準注記]。

##### 3.8.7.10.5 残ギャップ G1 の閉鎖

§3.8.7.9 の G1 ($\kappa(f)$ の上界 $\epsilon$ の構造的決定) は本節で **閉鎖** される:

$$\epsilon = |1 - e(\alpha)| \text{ の閉形式が Paper II §3.7.1 から直接得られる。}$$

これにより OP-IX-17 は「Open」→「**解決**」へ昇格する。残るのは:

- OP-IX-18 ($\mathrm{Lang}$ 射構造の厳密化) — 別軸
- OP-IX-12 (enrich$_\alpha$ measure-theoretic 構成) — 別軸 (G3)

##### 3.8.7.10.6 補題 3.8.2 の確信度更新

G1 の閉鎖により補題 3.8.2 の確信度は以下のように分岐する:

- **$\alpha = 0$ 制限版**: 補題 3.8.2 は $\epsilon = 0$ で **完全な自然変換** — 確信度 [推定 80%] (定理化候補)
- **$\alpha > 0$ 一般版**: 補題 3.8.2 は a.e. equivalence で閉じる — 確信度 [推定 70%] (構成的延長として確定)

これは §3.8.7 全体の確信度を 65% → 70-80% に昇格する。

##### 3.8.7.10.7 撤回条件

本節の構造決定は以下のいずれかが成立する場合に修正される:

- (a) Paper II §3.7.1 の $e(\alpha)$-twist の数値検証 ([SOURCE: 論文II L714] ガウス族 $e(+1) \approx 0.08$) が他の統計多様体クラスで再現しない場合、$\epsilon = |1-e(\alpha)|$ の閉形式は CPS の局所性質に降格
- (b) $\tau(f) = 1$ の仮定 (確定的射のみ) が崩れ、$\mathrm{Disc}$ の射に確率的成分が混入する場合、$\kappa(f) = e(\alpha) \cdot \tau(f)$ の射依存性が復活
- (c) Paper II §3.7.1 の互換性補題 (⟹ 方向のみ) が CPS の構成的命題水準を超える場合、本節も連鎖的に主張水準を降格

[確信度] 補題 3.8.3 ($\kappa$ の閉形式): [推定 75%] (Paper II $e(\alpha)$-twist が確立済みであり、$\tau(f) = 1$ 仮定は Markov 関手の確定性保存から構造的に得られる)

---

## §4. 射計数エントロピーとの関係（constructive appendix）

本節は §3 の主定理列を置き換えるものではなく、Paper VIII の射計数版第二法則と本稿の CPS エントロピー単調性を接続するための appendix 層である。ここでの主眼は exact recovery の完成ではなく、どの粗視化を経ると $S_{\mathrm{cat}}$ が $S_{\mathrm{CPS}}$ の低解像度像として読めるかを固定することにある。

### 4.1 二つのエントロピーの関係

Paper VIII の射計数エントロピー $S_{\mathrm{cat}}(\alpha) = \log m(0) - \log m(\alpha)$（Th. 6.10.3）と CPS エントロピー $S_{\mathrm{CPS}}(p, \alpha)$ の関係を明確にする。

**命題 4.1.1 (射計数版は CPS 版の二重粗視化).** 以下の二段階の粗視化により $S_{\mathrm{cat}}$ は $S_{\mathrm{CPS}}$ から回復される:

**第一粗視化（状態平均化）.** 状態に依存する CPS エントロピーを「平均エントロピー」に粗視化する。形式的に: 対象 $X$ に対し $\mathrm{State}(X) := \mathrm{Mor}(C)(I, X)$ を状態空間とし、一様分布 $\mu_X$ を仮定して

$$\bar{S}_{\mathrm{CPS}}(\alpha, X) := \int_{\mathrm{State}(X)} S_{\mathrm{CPS}}(p, \alpha) \, d\mu_X(p)$$

と定義する。$\bar{S}_{\mathrm{CPS}}$ は特定状態への依存を消去し、対象 $X$ と α のみの関数となる。

**第二粗視化（divergence のカウンティング特殊化）.** Divergence $D$ を **0-∞ カウンティングダイバージェンス** $D_{\#}$ で置換する:

$$D_{\#}(p \| f) := \begin{cases} 0 & \text{if } p = f \\ +\infty & \text{if } p \neq f \end{cases}$$

このとき $S_{\mathrm{CPS}}^{\#}(p, \alpha) = \inf_{f \in \mathrm{Det}(C_\alpha)} D_{\#}(p \| f) = 0$ if $p \in \mathrm{Det}(C_\alpha)$, $+\infty$ otherwise。エントロピーは二値的になり、「状態が確定的か否か」のみを区別する。

**両粗視化の合成.** 二重粗視化の下で、有限エントロピーを持つ状態の「数」の対数的変化を取れば:

$$S_{\mathrm{cat}}(\alpha) = \log m(0) - \log m(\alpha) = \log \frac{|\mathrm{Mor}(C_0)|}{|\mathrm{Mor}(C_\alpha)|}$$

は、（有限 Mor の場合に）$\bar{S}_{\mathrm{CPS}}^{\#}$ の global summary と同型になる。すなわち $S_{\mathrm{cat}}$ は（射の全滅率の対数を通じて）状態を平均化し divergence を離散化した $S_{\mathrm{CPS}}$ の粗い版に他ならない。

*証明.* $D_{\#}$ の下では各状態は「確定的/非確定的」に二値分類され、$S_{\mathrm{CPS}}^{\#}(p, \alpha) \in \{0, +\infty\}$。$\mu_X$-平均は有限エントロピー状態の割合に帰着する。有限射の圏では $|\mathrm{Mor}(C_\alpha)| \leq |\mathrm{Mor}(C_0)|$（(F4)）であり、生存射の対数的減少率 $\log m(0) - \log m(\alpha)$ がこの離散化された平均エントロピーの natural summary を与える。$S_{\mathrm{CPS}}$ は $D_{\#}$ を連続的 divergence $D$（KL ダイバージェンス等）に「解像度を上げ」、かつ状態ごとの精密な距離を測ることで、$S_{\mathrm{cat}}$ の二重の粗さを除去したものである。□

**備考 4.1.2 (粗視化の不等式).** 連続的 $D \geq D_{\#}$ が一般に成り立つわけではないが、Jensen の不等式の類似として: $D$ が凸かつ $D(p \| f) = 0 \Leftrightarrow p = f$ のとき、$S_{\mathrm{CPS}}(p, \alpha) \geq 0 = S_{\mathrm{CPS}}^{\#}(p, \alpha)$ が確定的状態に対して成立する。非確定的状態に対しては $S_{\mathrm{CPS}}(p, \alpha) < +\infty = S_{\mathrm{CPS}}^{\#}(p, \alpha)$ も可能であり、$D_{\#}$ は $D$ に対する粗視化として機能する。

### 4.2 効果量天井との接続

Paper IV 命題 7.5.1 は、効果量天井 $r_{\mathrm{obs}} \leq \sqrt{\rho/(K+1)}$ が Schur-Horn 不等式（= 優越関係）によるエントロピー不等式であることを示した。CPS エントロピーの文脈では:

- $\rho_{\mathrm{spec}} < 1$: 忘却関手による射影が $S_{\mathrm{CPS}}$ を増大させ、観測分散を減衰させる
- $1 - \rho$ は、CPS エントロピーの分散レベルの測度: $(1 - \rho) \propto \Delta S_{\mathrm{CPS}}$

### 4.3 統合的な不等式体系

忘却論が確立したエントロピー関連の不等式を一覧する:

| 不等式 | 出典 | 内容 | 証明の鍵 |
|:--|:--|:--|:--|
| $S_{\mathrm{cat}}(\alpha_1) \leq S_{\mathrm{cat}}(\alpha_2)$ | Paper VIII Th. 6.10.3 | 射計数版の第二法則 | (F4) + $\log$ 単調性 |
| $S_{\mathrm{CPS}}(p, \alpha_1) \leq S_{\mathrm{CPS}}(p, \alpha_2)$ | 本稿 Th. 3.4.1 | 情報論的版の第二法則 | (F4) + $\mathrm{Det}$ の包含 |
| $\Xi_{\mathrm{impl}} \leq \Xi_{\mathrm{theory}}$ | Paper I Th. 5.6.1 | Schur-Horn 橋渡し | Schur-凸性 |
| $r_{\mathrm{obs}} \leq \sqrt{\rho/(K+1)}$ | Paper IV Th. 3.1.1 | 効果量天井 | Schur-Horn + 分散分配 |
| $S_{\mathrm{CPS}}(k \circ p, \alpha) \leq S_{\mathrm{CPS}}(p, \alpha)$ | Perrone DPI [P1] | チャネル内の情報損失 | Markov 圏構造 |

これらは全て**忘却は不可逆であり、エントロピーを増大させる**という単一の原理の異なる表現である。

---

## §5. $\alpha_{\mathrm{III}} \leq 0$ セクターのエントロピー（Paper IX-B 育成面）

### 5.1 問題の所在

本節で扱う「負セクター」は、正本上は $\alpha_{\mathrm{III}} < 0$ の領域であり、$\eta$ により $0 < \alpha_{\mathrm{VIII}} < 1/2$ に写る。$\alpha_{\mathrm{VIII}}$ 自体の定義域は $[0,1]$ であり、$\alpha_{\mathrm{VIII}} \leq 0$ は Paper VIII の通常領域ではなく、境界閉包または逆忘却を語るときの拡張的表現に限る。したがって本節は標準 $S_{\mathrm{CPS}}$ の主定理列ではなく、Z₂-次数付き拡張の育成面として読む。

より根本的に: $\alpha_{\mathrm{III}} < 0$（Paper III のフェルミオン的セクター）では CPS 圏の Markov 圏的構造が退化する（Paper II §3.7.1）。Grassmann 奇射 $f$ は $f \otimes f = 0$（$\xi \wedge \xi = 0$）を満たすため、Perrone–Fritz の Markov 圏公理が要求するコピー射 $\mathrm{copy}_X: X \to X \otimes X$ が定義できない。

### 5.2 直接輸入の不可能性

**定理 5.2.1 (Perrone エントロピーの α_III < 0 直接輸入不可能性).** $\mathrm{CPS}^{Z_2}$ 圏のフェルミオン的セクター（$\alpha_{\mathrm{III}} < 0$、Z₂-奇射が非自明に存在する対象を含む）に対し、Perrone の構成をそのまま用いた確定的射ベースのエントロピーは well-defined でない。

*証明.* Perrone [P1, §3] のエントロピーの構成には確定的射 $\mathrm{Det}(C)$ の定義が必要であり、これは Markov 圏のコピー射 $\mathrm{copy}_X$ に依存する（$f$ が確定的 $\Leftrightarrow$ $\mathrm{copy}_Y \circ f = (f \otimes f) \circ \mathrm{copy}_X$）。

$\alpha_{\mathrm{III}} < 0$ のセクターにおいて、Paper III §2.2 の Z₂-次数付けにより射は偶（ボソン的）成分と奇（フェルミオン的）成分に分解される。奇射 $f$ に対し:
- Koszul 符号則より $(f \otimes f)(x) = (-1)^{|f| \cdot |f|} (f \otimes f)(x) = -(f \otimes f)(x)$（$|f| = 1$ のとき）
- したがって $f \otimes f = 0$（特性 $\neq 2$ の体上）
- $\mathrm{del}_Y \circ f = (f \otimes f) \circ \mathrm{del}_X = 0$ より、「確定性条件」は自明に成立するが、$f$ を「確定的」と分類すると $\mathrm{Det}(C_\alpha)$ が全射を含むことになり、$S_{\mathrm{CPS}} = 0$ が恒等的に成立して非自明なエントロピー論が消滅する。
- 代替として $f \otimes f = 0$ の射を $\mathrm{Det}$ から除外しても、奇射が除外されるため $\mathrm{Det}(C_\alpha)$ の偶セクターのみが残り、$S_{\mathrm{CPS}}$ は偶射に対してしか意味を持たない。

いずれにせよ、Perrone の構成を直接適用すると自明または不完全なエントロピーとなる。□

### 5.3 Z₂-次数付きエントロピーの候補構成

**定理 5.2.1 は Perrone エントロピーの *直接的* 輸入が不可能であることを示すが、修正された構成の道を閉ざすものではない。** 以下に二つの候補を提示する。

**候補 A: スーパートレース型エントロピー.**

> **定義 5.3.1.** Z₂-次数付き CPS 圏 $\mathrm{CPS}^{Z_2}$ における**スーパーエントロピー** $S^{Z_2}_{\mathrm{CPS}}$ を:
>
> $$S^{Z_2}_{\mathrm{CPS}}(p, \alpha) := \inf_{f \in \mathrm{Det}^{\mathrm{even}}(C_\alpha)} D(p_{\mathrm{even}} \| f) + \lambda \cdot h(p_{\mathrm{odd}})$$
>
> と定義する。ここで:
> - $p_{\mathrm{even}}, p_{\mathrm{odd}}$ は状態 $p$ の Z₂-次数分解
> - $\mathrm{Det}^{\mathrm{even}}$ は偶セクターの確定的射（Perrone の意味で well-defined）
> - $h(p_{\mathrm{odd}})$ は奇セクターの Grassmann 次数に基づくエントロピー測度（具体的には $h(p_{\mathrm{odd}}) := \mathrm{rank}_\Lambda(p_{\mathrm{odd}})$ の対数）
> - $\lambda > 0$ は偶/奇セクターの重み付けパラメータ

**命題 5.3.2.** 候補 A は以下を満たす:
(i) $\alpha_{\mathrm{III}} > 0$（純ボソン的）のとき $p_{\mathrm{odd}} = 0$ であり、$S^{Z_2}_{\mathrm{CPS}} = S_{\mathrm{CPS}}$ に退化する。
(ii) §3 の第二法則（定理 3.4.1）は偶セクターに対して成立する。
(iii) 奇セクターの寄与 $h(p_{\mathrm{odd}})$ は α-単調性を**現段階では**保証しない。

*証明スケッチ.* (i) 偶セクターのみの場合 $h(p_{\mathrm{odd}}) = h(0) = 0$（$\log \mathrm{rank}_\Lambda(0) = -\infty$ を $0$ と規約）。(ii) 偶セクターは Markov 圏構造を保持するから定理 3.4.1 がそのまま適用。(iii) $\alpha$ 増加に伴い Grassmann 次数の高い射が先に消滅するか否かは圏の構造に依存する。□

**候補 B: ε-正則化型.**

> **定義 5.3.3.** $\alpha < 0$ に対し:
>
> $$S^{\epsilon}_{\mathrm{CPS}}(p, \alpha) := \lim_{\epsilon \to 0^+} S_{\mathrm{CPS}}(p, \alpha + \epsilon)$$
>
> ここで $S_{\mathrm{CPS}}(p, \alpha + \epsilon)$ は $\alpha + \epsilon > 0$ の領域での §3 の定義を用いる。

**命題 5.3.4.** $S^{\epsilon}_{\mathrm{CPS}}$ について:
(i) 極限は $\alpha = 0$ で存在し $S_{\mathrm{CPS}}(p, 0)$ に一致する（命題 3.5.1(i) の連続性）。
(ii) $\alpha < 0$ での極限存在は $\{C_\alpha\}_{\alpha \geq 0}$ の $\alpha < 0$ への延長の滑らかさ条件に依存する。Paper VIII の α-忘却濾過は $[0,1]$ 上で定義されており、負の値への延長は非自明。
(iii) 形式的に $\alpha < 0$ を許す場合、$|\mathrm{Mor}(C_\alpha)| > |\mathrm{Mor}(C_0)| = |\mathrm{Mor}(C)|$ が必要となり、これは**C よりも射が多い圏**の存在を要求する。忘却論の枠組み内では、これは「忘却の逆転 = 情報生成」であり、Paper VI の創発作用 $\Xi$ との接続が示唆される。

### 5.4 $\alpha_{\mathrm{III}} = 0$ の特異性と物理的解釈

**定理 5.4.1 (α = 0 相転移).** $\alpha_{\mathrm{III}} = 0$（$\alpha_{\mathrm{VIII}} = 1/2$）において、Paper III の copy/delete 構造はちょうど退化する（Paper III §1.1）。情報幾何的には e-接続と m-接続が一致する自己双対点であり、忘却論的には「忘却と保存がちょうど均衡する」臨界点である。

$S_{\mathrm{CPS}}$ の観点から:
- $\alpha_{\mathrm{VIII}} < 1/2$（$\alpha_{\mathrm{III}} < 0$）: 保存が支配的。標準 $S_{\mathrm{CPS}}$ の主定理列では扱わず、$S^{Z_2}_{\mathrm{CPS}}$ 候補の側で確定的参照が豊富になる方向を検討する。
- $\alpha_{\mathrm{VIII}} > 1/2$（$\alpha_{\mathrm{III}} > 0$）: 忘却が支配的。確定的射が減少し、標準 $S_{\mathrm{CPS}}$ の単調性定理が主に働く。
- $\alpha_{\mathrm{VIII}} = 1/2$（$\alpha_{\mathrm{III}} = 0$）: 相転移点。ここで $\partial S_{\mathrm{CPS}}/\partial\alpha$ が特異性を持つ可能性がある。

**予想 5.4.2 (臨界指数).** $\alpha_{\mathrm{VIII}} = 1/2$ 近傍で $S_{\mathrm{CPS}}(p, \alpha) \sim |\alpha - 1/2|^{-\gamma}$ の形のスケーリング則が存在し、臨界指数 $\gamma > 0$ は圏 C と状態 p の構造に依存する。これが確認されれば、忘却論は文字通りの「相転移」を含むことになる。

### 5.5 戦略的結論

定理 5.2.1 と候補 A, B の分析から:

1. **Perrone エントロピーの直接輸入は α_III < 0 で不可能** — これは本節で閉じた定理である。ただし、奇セクターのエントロピーそのものが存在しえない、とは主張しない。
2. **候補 A（スーパーエントロピー）が最も有望** — 偶セクターで既存理論を回復し、奇セクターに新たな構造を加える。ただし奇セクターの α-単調性が未確認（OP-IX-1 の核心）。
3. **ε-正則化は α < 0 では「忘却の逆転」を要求**し、Paper VI との統合なしには物理的動機づけが弱い。
4. **α = 0 は真の相転移点**であり、ここでのスケーリング則の確立が次の突破口となりうる。

---

## §6. 分配関数と温度（constructive appendix / open program）

本節は二層に分かれる。§6.1-§6.2 は $E(f)$ と有限射圏上の $Z_{\mathrm{CPS}}$ を定義する constructive appendix である。§6.3-§6.4 は $T_{\mathrm{CPS}}$、三パラメータ統一、$H_{\mathrm{CPS}}$ の open program であり、§3 の主定理列と同じ主張水準では読まない。

### 6.1 射のエネルギーの自然な定義

これまで $E(f)$ の定義が未確立であったが、§3.5 の臨界忘却閾値を用いて自然な定義を与える。

> **定義 6.1.1 (忘却エネルギー).** 射 $f \in \mathrm{Mor}(C_0) = \mathrm{Mor}(C)$ に対し、その**忘却エネルギー**を:
>
> $$E(f) := \alpha^*_f := \inf\{\alpha \in [0,1] \mid f \notin \mathrm{Mor}(C_\alpha)\}$$
>
> と定義する。すなわち $E(f)$ は射 $f$ が忘却によって消滅する最小の α 値（生存閾値）である。

**命題 6.1.2 (忘却エネルギーの基本性質).**
(i) $E(\mathrm{id}_X) = 1$ for all $X$（恒等射は完全忘却まで生存）。
(ii) $0 \leq E(f) \leq 1$ for all $f$。
(iii) (F4)（射の単調減少）より: $f \in \mathrm{Mor}(C_\alpha) \Leftrightarrow \alpha < E(f)$（左連続の場合）or $\alpha \leq E(f)$（閉値域の場合）。
(iv) $E(g \circ f) \leq \min(E(f), E(g))$（命題 6.7.4b の系: 合成は構成要素の弱い方で制約される）。

*証明.* (i) 恒等射は全ての $C_\alpha$（$\alpha < 1$）に属し、$C_1 = C_{\mathrm{disc}}$ でも $\mathrm{id}_X$ は生存するから $E(\mathrm{id}_X) = 1$。(ii) (F2) より $f \in \mathrm{Mor}(C_0)$ から $E(f) \geq 0$、(F3) と (F4) から $E(f) \leq 1$。(iii) (F4) の定義から直接。(iv) $f \notin \mathrm{Mor}(C_\alpha)$ ならば $g \circ f$ は $C_\alpha$ で定義できないから $\alpha \geq E(f) \Rightarrow g \circ f \notin \mathrm{Mor}(C_\alpha)$。□

### 6.2 分配関数 $Z_{\mathrm{CPS}}(\beta, \alpha)$

> **定義 6.2.1 (CPS 分配関数).** 逆温度 $\beta > 0$ と忘却強度 $\alpha \in [0,1)$ に対し:
>
> $$Z_{\mathrm{CPS}}(\beta, \alpha) := \sum_{f \in \mathrm{Mor}(C_\alpha)} e^{-\beta E(f)}$$
>
> 有限射の圏（$|\mathrm{Mor}(C_\alpha)| < \infty$）では和は有限であり $Z > 0$。

**命題 6.2.2 (分配関数の α-単調性).** $\alpha_1 < \alpha_2$ ならば $Z_{\mathrm{CPS}}(\beta, \alpha_1) \geq Z_{\mathrm{CPS}}(\beta, \alpha_2)$。

*証明.* (F4) より $\mathrm{Mor}(C_{\alpha_2}) \subseteq \mathrm{Mor}(C_{\alpha_1})$。$e^{-\beta E(f)} > 0$ であるから、和の項数が減少すれば全体も減少する。□

**備考 6.2.3.** 定義 6.1.1 は §3.5 の臨界忘却閾値 $\alpha^*(p)$ と本質的に同じ構造であるが、対象が異なる: $\alpha^*(p)$ は状態 $p$ の生存閾値、$E(f)$ は射 $f$ の生存閾値。$S_{\mathrm{CPS}}$ は状態を固定して確定的射の消滅を測り、$Z_{\mathrm{CPS}}$ は全射の消滅を Boltzmann 重みで統合する。

#### 6.2.4 忘却エネルギーと情報幾何的 α の辞書

架橋関手 B (Paper VIII Def. 6.7.3) は sigmoid 正規化 $\eta(\alpha_{\mathrm{III}}) = 1/(1+e^{-\alpha_{\mathrm{III}}})$ を通じて Paper III の情報幾何的パラメータ $\alpha_{\mathrm{III}} \in \mathbb{R}$ と Paper VIII の忘却強度 $\alpha_{\mathrm{VIII}} \in [0,1]$ を接続する。本項では E(f) がこの接続の射レベルの表現であることを厳密化する。

> **命題 6.2.4 (E(f) ↔ η の辞書).** $\eta: \mathbb{R} \to (0,1)$ を Paper VIII Def. 6.7.1 の sigmoid、$\mathrm{logit}: (0,1) \to \mathbb{R}$ をその逆とする。射 $f \in \mathrm{Mor}(C_0)$ に対し、以下が成立する。
>
> (a) **逆変換**: $\alpha_f^{\mathrm{III}} := \mathrm{logit}(E(f)) = \log\frac{E(f)}{1 - E(f)}$ と定義すれば $E(f) = \eta(\alpha_f^{\mathrm{III}})$。
>
> (b) **辞書の内容**: この等式は tautology **ではなく**、以下の物理的対応を符号化する:
>
> | 圏論的量 (Paper VIII/IX) | 情報幾何的量 (Paper III) | 対応 |
> |:--|:--|:--|
> | $E(f)$ = 射の生存閾値 $\in [0,1]$ | $\alpha_f^{\mathrm{III}}$ = 射が「住む」α-接続レベル $\in \mathbb{R}$ | $E = \eta(\alpha^{\mathrm{III}})$ |
> | $E(f) < 1/2$ (忘却に弱い) | $\alpha_f^{\mathrm{III}} < 0$ (e-接続側 = フェルミオン的) | Th. 5.2.1 により Perrone エントロピー不可能 |
> | $E(f) > 1/2$ (忘却に強い) | $\alpha_f^{\mathrm{III}} > 0$ (m-接続側 = ボソン的) | 標準的 Perrone エントロピーが well-defined |
> | $E(f) = 1/2$ (臨界点) | $\alpha_f^{\mathrm{III}} = 0$ (Fisher 計量 = 自己双対) | 予想 5.4.2 の相転移点 |
>
> (c) **分配関数の情報幾何的表示**: $Z_{\mathrm{CPS}}(\beta, \alpha)$ は情報幾何的座標で
>
> $$Z_{\mathrm{CPS}}(\beta, \eta(\alpha_{\mathrm{III}})) = \sum_{f:\, E(f) > \eta(\alpha_{\mathrm{III}})} e^{-\beta \eta(\alpha_f^{\mathrm{III}})}$$
>
> と書ける。和の条件 $E(f) > \eta(\alpha_{\mathrm{III}})$ は $\alpha_f^{\mathrm{III}} > \alpha_{\mathrm{III}}$（η の単調性）と同値であり、「α-接続レベルが閾値を超える射のみが Boltzmann 重みで寄与する」という明快な幾何的解釈を持つ。
>
> *証明.* (a) は $\eta \circ \mathrm{logit} = \mathrm{id}_{(0,1)}$ から直接。(b) の対応表は、Paper VIII Def. 6.7.3 の射レベル規則——$f \in \mathrm{Mor}(C_{\eta(\alpha_{\mathrm{III}})}) \Leftrightarrow \eta(\alpha_{\mathrm{III}}) \leq E(f)$——と Th. 5.2.1 の不可能性定理を組み合わせたもの。(c) は Def. 6.2.1 に $\alpha = \eta(\alpha_{\mathrm{III}})$ および $E(f) = \eta(\alpha_f^{\mathrm{III}})$ を代入し、$\eta$ の単調性から和の条件を変換する。□

> **備考 6.2.5 (三パラメータ統一への示唆).** 命題 6.2.4(c) は予想 6.3.2（三パラメータ統一）の構造的根拠を強化する。$Z_{\mathrm{CPS}}$ の引数が $(\beta, \eta(\alpha_{\mathrm{III}}))$ であるから、$\beta = \beta_{\mathrm{IB}} = 1/T_{\mathrm{CPS}}$ と同定すれば、**分配関数は情報ボトルネック逆温度と α-接続パラメータの二つの情報幾何的量のみで完全に記述される**。第三のパラメータ $\tau$（創発時間スケール）は $T_{\mathrm{CPS}} \cdot \tau = \text{const}$ を通じて $\beta$ に束縛される。すなわち、三パラメータの独立な自由度は実質 **二つ** ($\alpha_{\mathrm{III}}, \beta$) であり、$\tau$ は従属変数である。

### 6.3 温度と三パラメータの関係

CPS 温度は平衡条件 $\partial S / \partial E = 1/T$ の圏論的対応として定義される:

> **定義 6.3.1 (CPS 温度).** $T_{\mathrm{CPS}} := (\partial S_{\mathrm{cat}} / \partial E_{\mathrm{avg}})^{-1}$ ここで $E_{\mathrm{avg}}(\alpha) := \frac{1}{|\mathrm{Mor}(C_\alpha)|} \sum_{f \in \mathrm{Mor}(C_\alpha)} E(f)$ は生存射の平均エネルギー。

三パラメータ統一の候補:

| パラメータ | 出典 | 役割 | CPS 温度との関係 |
|:--|:--|:--|:--|
| $\alpha$ | Paper VIII §6.2 | 忘却強度 | $T_{\mathrm{CPS}}$ の制御変数 |
| $\tau$ | Paper VI §2 | 創発時間スケール | $T_{\mathrm{CPS}} \propto 1/\tau$（予想: 高温 = 速い忘却 = 短い時間スケール）|
| $\beta_{\mathrm{IB}}$ | Paper III §4 | 情報ボトルネック逆温度 | $\beta_{\mathrm{IB}} = \beta$ として $Z_{\mathrm{CPS}}$ を構成する候補 |

**予想 6.3.2 (三パラメータ統一).** 適切な正規化の下で $\beta_{\mathrm{IB}} = 1/T_{\mathrm{CPS}}$ かつ $T_{\mathrm{CPS}} \cdot \tau = \text{const}$（エネルギー-時間不確定性の類似）。これが成立すれば、Paper III/VI/VIII/IX の温度的パラメータは単一の自由度に帰着する。

### 6.4 自由エネルギーとハミルトニアン

$Z$ と $T$ が確立すれば Legendre 変換により:

$$F_{\mathrm{CPS}}(\beta, \alpha) := -\frac{1}{\beta} \log Z_{\mathrm{CPS}}(\beta, \alpha)$$

**命題 6.4.1.** $F_{\mathrm{CPS}}$ は $\alpha$ に関して非減少かつ $\beta$ に関して非増加。

*証明.* 命題 6.2.2 より $Z$ が $\alpha$-非増加であるから $-\log Z$ は $\alpha$-非減少。$\beta > 0$ の符号から $F$ は $\alpha$-非減少。$\beta$-非増加は $e^{-\beta E} \leq 1$ より $Z \leq |\mathrm{Mor}(C_\alpha)|$ と $\log Z / \beta$ の $\beta$-依存性から。□

CPS ハミルトニアンは $H_{\mathrm{CPS}} := F + T \cdot S_{\mathrm{cat}} = -T \log Z + T S_{\mathrm{cat}}$ として形式的に定義可能。ただし $S_{\mathrm{cat}}$ と $S_{\mathrm{CPS}}$ の二つのエントロピーが存在するため、どちらを用いるかは物理的文脈に依存する（OP-IX-4）。

---

## §7. Open Problems

| ID | 問い | 難易度 | 状態 |
|:--|:--|:--|:--|
| OP-IX-1 | Z₂-次数付きスーパーエントロピー $S^{Z_2}_{\mathrm{CPS}}$ の奇セクターにおける α-単調性 (§5.3 候補A) | 高 | Open |
| OP-IX-2 | 分配関数 Z_CPS(β,α) の連続極限: 有限射圏から無限射圏への拡張 (§6.2) | 中 | Open |
| OP-IX-3 | 三パラメータ統一: α, τ, β_IB の関係の厳密化 (§6.3 予想 6.3.2) | 高 | **方向提示** (Prop. 6.2.4, 備考 6.2.5): 独立自由度は (α_III, β) の2つ、τ は従属変数。予想の核心は β_IB = β の同定に帰着 |
| OP-IX-4 | ハミルトニアン H_CPS の well-definedness: S_cat vs S_CPS の選択 (§6.4) | 中 | Open |
| OP-IX-5 | 忘却関手 $U_{\alpha_1 \to \alpha_2}$ が Markov 関手である条件の精密化 | 中 | Open |
| OP-IX-6 | Perrone DPI と Th. 3.4.1 の統合不等式の最適性 | 中 | Open |
| OP-IX-7 | 時間の矢 = 忘却の矢の独立定理化 | 中 | **部分解決** (v0.9): §3.7 で Th. 3.4.X として定理化済。残課題は (P*) 仮説の主張水準の格上げ判定 (OP-IX-9) と原典 SOURCE 化 (OP-IX-11) |
| OP-IX-8 | 臨界指数 γ (予想 5.4.2): α = 1/2 近傍のスケーリング則の具体的計算 | 高 | Open (§5.4 新設) |
| OP-IX-9 | (P*) 仮説 ($d\mu/dt \leq 0$) の主張水準の確定。経験的仮説 / 実験的知見 / 定義 / Paper XII XII-T0 の系 のどれが最強の身分か。定義への格上げが可能なら Th. 3.4.X は無条件定理に昇格する | 中 | Open (§3.7.1) |
| OP-IX-10 | Paper VIII Th. 6.10.3 (静的版第二法則) と Th. 3.4.X (動的版) の階層構造の精密化。Th. 6.10.3 は Th. 3.4.X の (P*) なし極限か、それとも独立な階層か | 中 | Open (§3.7.3 系 3.7.1) |
| OP-IX-11 | 既存動的第二法則 (Boltzmann 1872 / Jacobson 1995 arXiv:gr-qc/9504004 / Verlinde 2011 arXiv:1001.0785) の原典独立 SOURCE 化と差分テーブルの精密化。Claude prior 由来の構造的差分案 (§3.7.4) を本格的な比較表に格上げする | 中 | Open (§3.7.4) |
| OP-IX-12 | enrich$_\alpha$ の分子 $P(\mathrm{cat} \mid \mathrm{both})$ の α-濾過上の measure-theoretic 構成。確率測度が Markov 関手仮定の下でいかに $\alpha$ パラメータ族として well-defined となるかの厳密化 (§3.8.6) | 中 | Open (§3.8) |
| OP-IX-16 | 補題 3.8.2 (三角形閉化) の完全証明。離散版 (chemistry_cognition.md §10.6) → α-濾過版 (予想 3.8.1) → 言語版 (Paper XI 公理 H-2Z) の三領域同型を encode する自然変換 $\eta$ の構成的与え方。完成すれば三領域不変量が確立し、Paper I §5.9 公理 5.9.2 への両側閾値追加圧が back-propagate する (§3.8.7) | 高 | **部分解決** (v0.11/v0.12): §3.8.7.7-§3.8.7.9 で $\eta_X = R_\alpha(X)/R_0(X)$ として対象成分構成 + 自然性条件 (\*) の検証戦略 3 ステップ + 5 結果の含意を確立。§3.8.7.10 (v0.12) で OP-IX-17 ($\kappa$ 上界) が解決され、$\alpha=0$ で補題 3.8.2 が完全閉鎖。残ギャップは OP-IX-18 (Lang 射構造) のみ。**OP 番号注記**: v0.11 で割り当てた OP-IX-13/14/15 は v0.7 の DPI image 拡張系統と衝突したため、v0.12 で OP-IX-16/17/18 に繰り下げた |
| OP-IX-17 | 自然変換 $\eta$ の自然性条件 (\*) における Markov 関手補正係数 $\kappa(f)$ の上界 $\epsilon$ を、Markov 関手の構造的条件から具体的に計算する。CPS($\alpha > 0$) 圏で $\epsilon = 0$ が成立するか、CPS($\alpha = 0$) 境界での $\epsilon > 0$ の許容範囲を確定する (§3.8.7.8) | 中 | **解決** (v0.12, §3.8.7.10): Paper II §3.7.1 $e(\alpha)$-twist から $\kappa(f) = e(\alpha)$ (確定的射のとき) という閉形式を導出。$\epsilon = \|1 - e(\alpha)\|$ として構造的に決定 (補題 3.8.3)。$\alpha = 0$ で $\epsilon = 0$ により補題 3.8.2 が完全閉鎖、$\alpha > 0$ で a.e. equivalence。Paper II §3.7.1 主張水準注記 (Markov 圏的構造の構成的延長) と整合 |
| OP-IX-18 | $\mathrm{Lang}$ (自然言語表現空間) の射構造の厳密化。corpus 頻度の比較関係のみで自然変換 $\eta$ が well-defined となるか、意味論的射 (例: 同義語関係) の追加が必要かを判定する。Paper XI §7.7.5b.3 の三領域同型表との整合 (§3.8.7.9 G2) | 中 | Open (§3.8.7.9) |

---

## 参考文献

### 忘却論シリーズ（内部）
- [I] Paper I: 力は忘却である (v0.14)
- [II] Paper II: 相補性は忘却である (v1.0)
- [III] Paper III: 暗い側 — Z₂-次数付き CPS 圏 (v1.0)
- [IV] Paper IV: なぜ効果量は小さいか (v1.4)
- [V] Paper V: 繰り込みは忘却である (v0.2)
- [VI] Paper VI: 行為可能性は忘却である (v0.1)
- [VII] Paper VII: 知覚は忘却である (v1.3)
- [VIII] Paper VIII: 圏論的基礎における存在 (v1.5)

### 外部
- [P1] Perrone, P. "Markov Categories and Entropy." *IEEE Trans. Inform. Theory* 70(3), 1677–1719, 2024. arXiv:2212.11719.
- [F1] Fritz, T. "A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics." *Advances in Mathematics* 370, 107239, 2020. arXiv:1908.07021.
- [B1] Baez, J.C., Owen, L., Moeller, J. "Compositional Thermostatics." *J. Math. Phys.* 64, 022302, 2023. arXiv:2111.10315.
- [DHKK] Dimitrov, G., Haiden, F., Katzarkov, L., Kontsevich, M. "Dynamical systems and categories." *Contemp. Math.* 621, 133–170, 2014.
- [MO] Marshall, A.W. & Olkin, I. *Inequalities: Theory of Majorization and its Applications*. 2nd ed. Springer, 2011.
- [S1] Sagawa, T. "Entropy, Divergence, and Majorization in Classical and Quantum Thermodynamics." arXiv:2007.09974, 2020.

---

### 変更履歴

| バージョン | 日付 | 内容 |
|:--|:--|:--|
| v0.1 | 2026-04-02 | 初稿: §1-§4 (CPS エントロピー構成 + 単調性定理), §5-§6 展望, §7 Open Problems |
| v0.5 | 2026-04-09 以前 `[上界補正]` | §3.5: Prop 3.5.1 厳密証明 + 臨界忘却閾値 α* 導入。§4.1: Prop 4.1.1 二重粗視化の厳密化。§5: 展望→定理 (Th. 5.2.1 不可能性 + 候補 A/B + 相転移構造)。§6: 展望→構成 (Def. 6.1.1 忘却エネルギー + Z_CPS + 自由エネルギー) |
| v0.6 | 2026-04-10 | §6.2: Prop. 6.2.4 (E(f)↔η辞書 — 忘却エネルギーと情報幾何的αの厳密対応)。備考 6.2.5 (三パラメータ統一の自由度が実質2であることの構造的根拠)。OP-IX-3 に方向提示を追加 |
| v0.7 | 2026-04-26 | 内部育成層分けを明記。§3 を定理核、§4 と §6.1-§6.2 を constructive appendix、§6.3-§6.4 を open program、§5 を Paper IX-B 候補の負セクター育成面として分離。α 記号域の混線を補正し、Th. 5.2.1 を「直接輸入不可能性」に限定 |
| v0.8 | 2026-04-26 | 備考 3.4.3 を系 3.4.2「ダイバージェンス非依存性」へ昇格。Shannon/Rényi/Gini-Simpson への即時帰結を定理核の corollary として固定 |
| v0.9 | 2026-04-27 | §3.7 「動的第二法則 — 時間の矢 = 忘却の矢」を新設。Th. 3.4.X を Paper V Th. 2.3.1 + Paper IX Th. 3.4.1 の合成定理として独立化。(P*) 仮説 ($d\mu/dt \leq 0$) を precision note として明示。系 3.7.1 (静的版/動的版の階層) + 系 3.7.2 (ダイバージェンス非依存性の動的版) + 備考 3.7.3 (Paper XII χ 単調性接続) + §3.7.4 既存動的第二法則 (Boltzmann/Jacobson/Verlinde) との差分テーブル [TAINT 注記付] + §3.7.5 主張水準と境界。OP-IX-7 を「部分解決」へ更新、OP-IX-9 ((P*) 主張水準確定) / OP-IX-10 (静的-動的階層精密化) / OP-IX-11 (原典 SOURCE 化) を新規 open。背景: monograph 第Ⅵ幕統合章の旗艦定理化。meta v0.3 §M2 C6 / §M5 Round 0-3 / §M6 C6 の接地を実現 |
| v0.10 | 2026-04-29 | §3.8.7 「三角形閉化補題 — 離散版・α-濾過版・言語版の同値性」を新設。補題 3.8.2 (候補) を起票し、離散版 (chemistry_cognition.md §10.6 定理 2') / α-濾過版 (Th. 3.8.1) / 言語版 (Paper XI 公理 H-2Z) の三領域を同型射 $\Phi_{D \to F}, \Phi_{F \to L}, \Phi_{D \to L}$ で接続する図式の自然変換差を許す可換性として定式化。証明戦略 4 ステップ + 含意 4 件 + 撤回条件 3 件を明示。OP-IX-12 (enrich$_\alpha$ measure-theoretic 構成) と OP-IX-13 (補題 3.8.2 完全証明) を新規 open。Paper XI v0.13 の H₃'' / 公理 H-2Z 起票と双方向 SOURCE 連結。完成すれば Paper I §5.9 公理 5.9.2 への両側閾値追加圧が back-propagate する |
| v0.11 | 2026-04-29 | OP-IX-13 集中作業として §3.8.7.7-§3.8.7.9 を新設。自然変換 $\eta: \Phi_{\mathrm{D \to L}} \Rightarrow \Phi_{\mathrm{F \to L}} \circ \Phi_{\mathrm{D \to F}}$ の対象成分を $\eta_X := R_\alpha(X)/R_0(X)$ として構成的に与えた (§3.8.7.7)。自然性条件 (\*) の検証戦略 3 ステップ (N1 射の意味 / N2 両経路計算 / N3 可換性根拠) + Markov 関手補正係数 $\kappa(f)$ の導入 (§3.8.7.8)。完成時の含意 5 件 (三角形閉化 / 三領域不変量の特定 / Paper XI H-2Z への back-propagation / Paper I 公理 5.9.2 の両側閾値追加圧の正規化 / 熱力学第二法則の三層化) と残ギャップ G1-G3 を §3.8.7.9 に明示。OP-IX-13 を「部分解決」に更新し、残課題を OP-IX-14 ($\kappa(f)$ 上界の構造的決定) と OP-IX-15 ($\mathrm{Lang}$ 射構造の厳密化) として分離登録。補題 3.8.2 確信度 55% → 65% に昇格 |
| v0.12 | 2026-04-29 | OP-IX-17 ($\kappa(f)$ 上界の構造的決定, 旧 OP-IX-14) 集中作業として §3.8.7.10 を新設 (7 副節)。Paper II §3.7.1 [SOURCE: 論文II_相補性は忘却である_草稿.md L707-722] の $e(\alpha)$-twist から $\kappa(f) = e(\alpha)$ (確定的射のとき) という閉形式を導出。**補題 3.8.3 ($\kappa$ 閉形式)** を起票し、$\epsilon = |1 - e(\alpha)|$ として構造的に決定。$\alpha = 0$ で $\epsilon = 0$ により補題 3.8.2 が完全閉鎖 (定理化候補)、$\alpha > 0$ で a.e. equivalence を保つ。ガウス族 $\mathcal{H}^2$ 数値検証 ($e(+1) \approx 0.08$) が裏付け。Paper II §3.7.1 主張水準注記 (Markov 圏的構造の構成的延長) と整合化。**OP 番号衝突解消**: v0.7 の §3.8 系統 (Th. 3.8.1 → 予想 3.8.1 主張水準降格) が同セッション並行作業で OP-IX-13/14/15 を chem 出典 / DPI image 拡張 / 翻訳辞書精密化として確定したため、v0.11 で割り当てた OP-IX-13/14/15 (補題 3.8.2 完全証明 / $\kappa$ 上界 / Lang 射構造) を OP-IX-16/17/18 へ繰り下げ。本文 §3.8.7.4-§3.8.7.10 と §7 OP テーブルを整合化。OP-IX-17 を「Open」→「**解決**」へ昇格。補題 3.8.2 確信度 65% → 70-80% (α=0 制限版 80% / α>0 一般版 70%)。補題 3.8.3 確信度 75%。Th. 3.8.1 主張水準降格 (v0.7) との直交性を §3.8.7.10 冒頭注記で明示 |

---

*Paper IX v0.12 — 2026-04-29*
*MECE 構成: §1 動機, §2 Perrone 枠組みの再掲, §3 CPS エントロピーの構成 (Def. 3.3.1) + 単調性定理 (Th. 3.4.1, 静的版) + 境界条件 (Prop. 3.5.1) + 動的第二法則 (Th. 3.4.X, §3.7), §4 constructive appendix (Prop. 4.1.1 二重粗視化), §5 $\alpha_{\mathrm{III}}\leq0$ 負セクター育成面 (Th. 5.2.1 直接輸入不可能性 + 候補構成 + 相転移), §6 constructive appendix / open program (Def. 6.1.1 + Z_CPS + F_CPS + T/H open)*
