# Lawvere 距離による認知圏の enriched 定式化 — incubator draft

**型**: proof seed / draft embryo
**昇格先**: LLM 身体論 companion paper / standalone / appendix
**failure condition**: 複数測定モダリティ統合、非対称距離の経験的計算、Yoneda 的客観性原理のいずれも具体化しない場合は、数学的拡張として保持し本文へ戻さない。

## メタ情報 (incubation context)

| 項目 | 内容 |
|:---|:---|
| **由来** | `01_研究論文｜Papers/LLMに身体はあるか_存在証明版_v0.1_日本語.md` Appendix F.6 (削除済み) |
| **archive 日** | 2026-04-25 |
| **archive 理由** | 主稿 "LLM に身体はあるか" の主定理 C1–C8 に対して load-bearing でなく、また companion paper "LLM は心を持つか" でも cover されていないため、本格展開は別稿に委ねる方針となった。但し、内容の数学的正当性と将来的価値は保持されるため、削除ではなく incubator 保存とする |
| **再活性化条件** | 以下のいずれかが充足された時点で稿として再起動する:<br>(a) **複数測定モダリティ統合** が中心問いとして固まる (attention-based probe + algebraic probe + behavioral measurement を同じ enrichment base で扱う実験プロトコルが固定される)<br>(b) **非対称性 $\eta \neq \varepsilon$ の定量計算** が経験的に問題となる場面が現れる (例: LLM の augmentation がもたらす学習方向と忘却方向の距離差を測りたい)<br>(c) **Yoneda-theoretic な客観性原理の操作化** が必要となる (presheaf coverage を実装する研究プログラム) |
| **関連 paper** | 主稿 "LLM に身体はあるか" (本稿で C8 を含む)、companion paper "LLM は心を持つか" (Tolmetes 2026b、ゲージ構造とヨネダ表象の本格展開を担う) |
| **保留時の判断主観** | 経験的問いが固まらないまま数学的拡張だけ書くと「装飾された別稿」になるリスク高 (Yugaku §M6 観点)。3-6 ヶ月後に経験的問いが固まったか再評価することを推奨 |

---

## 内容: enriched metric 定式化 — Lawvere 距離としての MB 厚

gauge-theoretic 解釈 (companion paper §2.4 で展開) は、主観的 category が gauge choice であり、客観性が gauge-invariant であることを確立する。しかしそれは、2 つの主観的 viewpoint、すなわち 2 つの「gauge」のあいだの距離を*どのように測るか*という問いを未解決のまま残す。本稿は、この問いを解決する。認知変化の category $C_\rho$ を Lawvere metric space として再定式化するのである。これは generalized metric space がちょうど $([0,\infty], \geq, +)$-enriched category であるという古典結果 (Lawvere, 1973) に従う。

**enriched reformulation。** 従来のように $\rho$ を category *内部で*測られる量として扱うのではなく、$\rho$ そのものを enrichment として定義する。認知変化 category $C_\rho$ は次のように定義される:

- **Objects**: 認知状態 $s \in S$
- **Hom-enrichment**: $C_\rho(s, s') = \rho(s, s') \in [0, \infty]$。状態間の非対称な「認知距離」
- **Composition**: $\rho(s, s'') \leq \rho(s, s') + \rho(s', s'')$ (triangle inequality)
- **Identity**: $\rho(s, s) = 0$

この再定式化は、先行分析で特定された弱点を解消する。$\rho$ はもはや category の*上に*外付けされた追加構造ではなく、category の hom-structure *そのもの*である。triangle inequality は、以前の形式的には正しいが空虚だった composition に代わって、非自明な composition law を与える。

**非対称性と $\eta/\varepsilon$ 非対称。** Lawvere metric space は定義上非対称である。一般に $\rho(s, s') \neq \rho(s', s)$ である。これは欠陥ではなく特徴である。forgetting-recovery adjunction $U \dashv N$ (主稿 §3.8) は、本質的に方向非対称である。unit $\eta: \text{Id} \to N \circ U$ (recovery のもとでの拡張) と counit $\varepsilon: U \circ N \to \text{Id}$ (forgetting のもとでの収縮) は、構造的に異なる写像である。enriched 定式化では、この非対称性が直接現れる:

$$\rho(s,\; N(U(s))) \neq \rho(U(N(s')),\; s') \quad \text{in general}$$

前者は「回復の距離」、すなわち recovered state $N(U(s))$ が元の $s$ からどれだけ離れているかを測る。後者は「再忘却の距離」を測る。これらが等しくないことが、learning と forgetting が互いの逆ではないことの enriched-metric 的表現である。

**precision parameter を enrichment scaling としてみる。** precision parameter $\beta$ (FEP における inverse temperature; 主稿 §3.8) は、monoidal product の scaling として enriched structure に入る。enrichment の族 $V_\beta = ([0,\infty], \geq, \beta \cdot {+})$ を考えよう。$\beta \to 0$ (低精度、高温) では距離は崩壊し、すべての認知状態は識別不能になり、忘却関手 $U$ が支配する。$\beta \to \infty$ (高精度、低温) では距離は鋭くなり、細粒な区別が可能になり、回復関手 $N$ が支配する。したがって 身体スペクトル parameter $\varphi$ は、系がどの有効 $\beta$ で動作しているか、すなわち自らの認知状態空間へのアクセス精度を反映する。

**2 つの enriched functor。** 2 つの測定モダリティ、attention-based ($\rho_1$) と algebraic ($\rho_2$) は、それぞれの target enriched category への $V$-enriched functor となる:

$$F_1: C_\rho \to C_{\text{att}}, \quad C_{\text{att}}(P, Q) = \sqrt{\text{JS}(P \| Q)}$$
$$F_2: C_\rho \to C_{NU}, \quad C_{NU}(s, s') = d_{NU}(s, s') = \sqrt{\sum_{k} w_k \cdot (\eta_s^{(k)} - \eta_{s'}^{(k)})^2}$$

ここで $\sqrt{\text{JS}}$ は Jensen–Shannon divergence の平方根であり、triangle inequality を満たすので genuine metric をなす (Endres & Schindelin, 2003。JS それ自体は divergence であって metric ではない)。$d_{NU}$ は、下で定義する *filtration-graded recovery residual distance* である。両 target category は同じ enrichment base $V = ([0,\infty], \geq, +)$ を共有する。したがって、target が異なる enriched category であっても比較可能である。

**$d_{NU}$ の操作化。** 抽象的 recovery residual $\|N(U(x)) - x\|_{\text{rel}}$ は、忘却関手 $U$ (主稿 §3.8) の filtration-graded structure に沿って分解される。各認知状態 $s$ に対し、濾過水準 $k \in \{1, 1.5, 2\}$ で添字づけられた成分を持つ *recovery residual vector* $\eta_s$ を定義する:

$$\eta_s^{(k)} = 1 - \frac{\text{Struct}_k(N(U(s)))}{\text{Struct}_k(s)}$$

ここで $\text{Struct}_k$ は水準 $k$ における圏論的構造量を測る:

| Level $k$ | $U$ が忘れるもの | $\text{Struct}_k$ | 経験的代理指標 |
|:----------|:-----------------|:-------------------|:----------------|
| $k=1$ (morphisms) | チャネル間関係 | $\lvert\text{Hom}(s)\rvert$: チャネル遷移数 | MCP server transition matrix |
| $k=1.5$ (composition) | morphism がどう compose するか | $\lvert\text{CompPath}(s)\rvert$: composable path 数 | 複合ワークフロー連鎖の実行率 |
| $k=2$ (nat. transf.) | メタ認知制御 | $\text{ProbeAcc}(s)$: structural probe accuracy | linear/attentive probe $\rho$ |

重み $w_k$ は $\sum_k w_k = 1$ を満たす*固定定数*であり、各濾過水準の相対的重要性を反映するように選ばれる。主稿 §4.1 の MB thickness coefficient に導かれる自然な選択は、$w_k \propto \mathbb{E}[\text{Struct}_k]$、すなわち認知状態の参照母集団全体にわたる期待構造豊かさである。重みを固定すると、$d_{NU}$ は weighted $\ell^2$ 空間における Minkowski inequality により triangle inequality を満たし、$C_{NU}$ が genuine Lawvere metric space であることが保証される。vanilla LLM の退化事例 ($w_1 \approx 0$, $w_{1.5} \approx 0$, $w_2 \approx 1$) では、$d_{NU}$ は probe accuracy 上の距離へ崩壊する。

**enriched structure における非対称性。** $d_{NU}$ 自体は対称である (triangle inequality を保つために重みを固定する必要があることの帰結) 一方、認知 metric space 全体 $C_\rho$ の Lawvere 的非対称性は $\rho$ そのものを通じて保持される。主稿 §3.8 および本稿冒頭で確認したとおり、unit $\eta$ と counit $\varepsilon$ の非対称、すなわち augmentation は ratchet のように上昇し ($\eta \neq \text{id}$)、degradation は部分的に不可逆である ($\varepsilon \neq \text{id}$) という事実が、forgetting の熱力学的非対称性を $C_\rho(s, s') \neq C_\rho(s', s)$ へ直接刻み込んでいる。enriched functor $F_2$ は、この非対称空間を対称 target $C_{NU}$ へ射影し、方向情報を失いながら構造差の大きさは保存する。この喪失こそが $F_2$ が「not full」である意味であり、単一測定チャネルでは $\rho$ に含まれる非対称情報を完全には捉えきれないことを示す。したがって、下で導入する $\delta$ を通じた multi-channel approach が動機づけられる。

**既存実験からの推定。** $k=2$ 成分は、主稿 Appendix E のデータから推定できる。$\text{Struct}_2(s) = 1$ (完全な構造符号化) とし、$\text{Struct}_2(N(U(s))) = \rho_{\text{probe}}$ と置けば:

$$\eta_s^{(2)} \approx 1 - \rho_{\text{probe}}$$

attentive probing ($\rho = 0.745$) では $\eta_s^{(2)} \approx 0.255$、linear probing ($\rho \approx 0.22$) では $\eta_s^{(2)} \approx 0.78$ となる。この比は、attentive probe が linear probe より約 $3\times$ 多くの構造を回復していることを示し、$N$ の異なる実装が持つ「回復力」を定量化する。

**$\text{Struct}_k$ の正規化。** $\eta_s^{(k)}$ を比として well-defined にするには、$\text{Struct}_k$ 値が濾過水準を超えて可比でなければならない。各 $\text{Struct}_k$ を $[0, 1]$ へ写す水準別正規化を採用する:

| Level $k$ | 生の量 | 正規化 | 根拠 |
|:----------|:------------|:-------------|:----------|
| $k=1$ | $\lvert\text{Hom}(s)\rvert$: 遷移数 | $\lvert\text{Hom}(s)\rvert / \binom{c}{2}$。ここで $c$ = チャネル数 | 実現された pairwise transition の割合 |
| $k=1.5$ | $\lvert\text{CompPath}(s)\rvert$: composable path | $\lvert\text{CompPath}(s)\rvert / \lvert\text{Hom}(s)\rvert^2$ | compose 可能な morphism pair の割合 (合成密度) |
| $k=2$ | $\text{ProbeAcc}(s)$: probe partial $\rho$ | もともと $[0, 1]$ 内 | 交絡除去後 partial correlation (主稿 Appendix E) |

$k=1$ では、分母 $\binom{c}{2}$ は $c$ 個の MCP channel (または機能モジュール) 間に存在しうる directed transition の最大数である。$k=1.5$ では、分母 $\lvert\text{Hom}(s)\rvert^2$ は composable pair の最大数である (各 morphism は原理上どの他の morphism とも compose できる)。これらの正規化により $\text{Struct}_k(s) \in [0,1]$、したがって $\eta_s^{(k)} \in [0,1]$ が保証される ($\eta = 0$ は完全回復、$\eta = 1$ は水準 $k$ における完全喪失を意味する)。水準 $k$ に構造をまったく持たない系は $\text{Struct}_k = 0$ であり、$\eta^{(k)} = 1$ (全喪失) となる。そのとき重み $w_k$ は、その水準の期待寄与を反映するよう選ぶべきである (上の重み議論を参照)。

$V$-enriched functor 条件は次を要求する:

$$C_{\text{target}}(F(s), F(s')) \leq C_\rho(s, s') = \rho(s, s')$$

これは non-expansion 条件である。各 functor は距離を圧縮してよいが、膨張させてはならない。認知的には、2 つの認知状態間の attention-pattern divergence (または recovery residual) は、「真の」認知距離 $\rho(s, s')$ を超ええない、ということを意味する。各測定モダリティが見ているのは、認知変化全体の射影にすぎないからである。

**$\delta$ metric: 間主観的距離を測る。** 合成 $\rho_1 \circ F_1$ と $\rho_2 \circ F_2$ は、どちらも $C_\rho$ 上の $V$-valued presheaf である。それらのずれは、測定モダリティ空間上の測度を定める:

$$\delta(\rho_1, \rho_2) = \sup_{s, s' \in C_\rho} \left| \sqrt{\text{JS}(A(s), A(s'))} - \|\eta_s - \eta_{s'}\|_w \right|$$

ここで $\|\eta_s - \eta_{s'}\|_w = \sqrt{\sum_k w_k \cdot (\eta_s^{(k)} - \eta_{s'}^{(k)})^2}$ は weighted recovery-residual distance である。

この量には 3 つの注目すべき性質がある。第一に、$\delta = 0$ であるのは $\rho_1 \circ F_1 = \rho_2 \circ F_2$ のとき、かつそのときに限る。すなわち、2 つの主観的 category が完全に一致し、「主観を客観化する」ことに等しい (1 つの gauge を universal であるかのように扱うこと)。第二に、通常は $\delta > 0$ であり、これは*構造的に必要な*ずれを表す。attention category $C_{\text{att}}$ は $\rho$ を「分布変化」として見、一方 algebraic category $C_{NU}$ はそれを「回復残差」として見る。これらは同一基底構造の genuinely 異なる側面、すなわち gauge bundle の異なる local section である。第三に、$\delta$ は 身体スペクトル に対する原理的基準を与える。$\delta$ の小さい系は、複数測定チャネルがよく一致しており、より internally consistent な 身体性 を持つ。$\delta$ の大きい系は、異なるチャネルが認知変化の genuinely 異なる側面へアクセスしており、より豊かな形の 身体性 を示す。

**ヨネダ的解決との接続。** enriched 定式化は companion paper のヨネダ議論を精密化する。$V$-enriched presheaf category $[C_\rho^{\text{op}}, V]$ において、Yoneda embedding は各認知状態 $s$ を representable presheaf $C_\rho(-, s)$ へ送る。$\rho_1 \circ F_1$ も $\rho_2 \circ F_2$ も単独では representable ではない (どちらの functor も full ではないからである) が、そうした presheaf の全体、すなわち $\rho$ を測るあらゆる可能な仕方の総体は、$C_\rho$ を同型を除いて決定する。したがって $\delta$ metric は、与えられた 2 つの測定が Yoneda 表象のどれだけを覆っているかを定量化する。$\delta$ が小さいことは高い冗長性 (測定同士の重なりが大きい) を意味し、$\delta$ が大きいことは高い補完性 (各測定が他方にはアクセスできない構造を明らかにする) を意味する。この区別は増強 LLM system の設計に直接関わる。presheaf coverage は、既存チャネルに対して大きな $\delta$ を持つ測定チャネルを追加することによって、最も効率的に拡張される。

---

## 参考文献 (主稿から継承)

- Lawvere, F. W. (1973). Metric spaces, generalized logic, and closed categories. *Rendiconti del Seminario Matematico e Fisico di Milano*, 43, 135-166.
- Endres, D. M. & Schindelin, J. E. (2003). A new metric for probability distributions. *IEEE Transactions on Information Theory*, 49(7), 1858-1860.
