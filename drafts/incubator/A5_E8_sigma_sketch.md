# A_5 × E_8 × σ Sketch — σ の対称階梯と格子埋込

**v0.2 (2026-04-17)** — Face7Lemma_draft v0.1 による A_5 requirement 反証の反映
**ステータス**: incubator sketch / 遠仮説段階 / SOURCE と思弁を分離 / 仮説 β 反証済
**役割**: σ の "full coherence" が要求する対称群の階梯を、S_3 → D_5 → A_5 → (E_8 格子) として読み、McKay 対応と Fibonacci anyon を経由して forgetting 論との接続を試みる。**ただし Face7 検証で「σ の三軸分離 = A_5 要求」仮説は反証**。A_5 の意義は σ の自動同型ではなく、**φ が独立に現れる代数的領域** に再配置される。
**親文書**:
- `./pentagon_sigma_conjecture.md` 種⑤ (本スケッチの上位動機)
- `./Face5Lemma_draft.md` (先行例: 種③ の sketch 化パターン)
- `../standalone/比較射σの統一定理_v0.1.md` (σ 統一論文本体)
- `../infra/リファレンス/triangle_category_functor_map.md` §3.bis 三軸分離

**試作の目的**: σ の住処を Δ² (S_3 対称) から正五角形 (D_5) まで伸ばす議論が pentagon_sigma_conjecture.md §6 と triangle_map §3.bis の 3 軸分離で固まりつつある。この階梯が A_5 まで届くか、そして A_5 から McKay 対応経由で E_8 格子まで届くかを、命題化前段階で整理する。

---

## §0 一文核 (試作)

**SOURCE (既知部分)**:
- A_5 (5 次交代群) は 60 元の有限単純群で、正 12 面体 / 正 20 面体の回転対称群に同型 [SOURCE: 古典群論, Humphreys]
- binary icosahedral group `2I` (A_5 の binary cover, 位数 120) は McKay 対応で extended E_8 Dynkin diagram に対応する [SOURCE: McKay 1980]
- A_5 の 2 つの 3 次元既約表現の指標に黄金比 φ が現れる [SOURCE: 標準指標表, Isaacs "Character Theory"]

**INFERENCE (試作中の核)**:
σ の自己同型群の階梯 S_3 (Δ², 6 元) → D_5 (正五角形, 10 元) → A_5 (正 20 面体, 60 元) は、次元が上がるごとに σ が閉じる必要な対称度が上がる経路として読める。A_5 で止まるのか、さらに上がるのかは Face7 lemma (未試作) が決めうる問題。

**OPEN**:
A_5 ↔ E_8 の McKay 接続を σ 論文の forgetting 論に翻訳するためには、「E_8 の roots が忘却濾過の何に対応するか」という未命題の橋が要る。本試作は橋の候補を羅列するにとどまる。

---

## §1 対称群の階梯

### S_3 → D_5 → A_5 の次元上昇

Δ² (三角形) の自己同型群は S_3 = {恒等, 3 回転, 3 鏡映} = 6 元。
正五角形の自己同型群は D_5 = {恒等, 4 回転, 5 鏡映} = 10 元。
正 20 面体 / 正 12 面体の回転群は A_5 = 60 元 (向き保存のみ)。鏡映込みで正 20 面体群 = A_5 × Z/2 の 120 元。

階梯の意味:
- S_3: 3 頂点を任意に置換 (対称度 = 全置換)
- D_5: 5 頂点を巡回的に置換 (対称度 = 巡回 + 鏡映)
- A_5: 12 面 = 20 頂点 = 30 辺を 3D 回転で置換 (対称度 = 有限単純群最小非可換)

**仮説 (α)**: σ の住処の次元を上げていくと、自己同型群は生成自由度を保ったまま **複雑化** する:
- S_3: 生成自由度 1 (転位 1 個で生成)
- D_5: 生成自由度 2 (回転 + 鏡映)
- A_5: 生成自由度 2 (2 つの回転の合成で全群生成) かつ非可解

### A_5 の特別性

A_5 は "最小の非可換有限単純群"。これが σ の full coherence を担う理由の候補:
- 可換群 (cyclic, dihedral の可換成分) は σ の位相軸のみを実現
- 非可換でも可解 (S_3, D_5, D_n etc.) は σ のスペクトル軸の一部を実現
- 単純非可換は σ の三軸すべてを実現する最小の場

[仮説 (β)] **✗ 反証済 (v0.2, 2026-04-17)**: 「σ の三軸分離を完全に要求する場 = 非可解単純群 = 最小が A_5」は Face7Lemma_draft v0.1 §12 で反証された。K_5 associahedron の自動同型群は linear order 反転で D_2 止まりであり、**A_5 を自然に含まない**。「σ の対称性 = K_n の対称性」という前提が暗黙に置かれていた誤り。

[修正仮説 (β')]: A_5 は σ の "自動同型候補" ではなく、**A_5 指標表に φ が現れる独立領域** として σ と接続する。K_n associahedron の自動同型とは別チャンネル。

### 階梯の次段候補 (参考、仮説 β 反証後は優先度低下)

A_5 の上にある単純非可換群:
- A_6 = 360 元, A_7 = 2520 元, ..., 一般 A_n (n ≥ 5)
- PSL(2, 7) = 168 元 (Fano 平面対称性)
- Mathieu 群 M_11, M_12, M_22, M_23, M_24 (sporadic の入口)

[OPEN 修正]: σ が A_5 で Face5 を閉じるという主張自体が仮説 β 反証で弱まった。A_6 や PSL(2,7) への階梯の意義は現状不明。ただし A_n character table での φ 発現パターンの調査は独立の価値あり。

---

## §2 A_5 の既約表現と φ の発現

### 既約表現の次元

A_5 は 5 つの共役類を持ち、5 つの既約表現を持つ (共役類数 = 既約表現数)。次元は:

**1, 3, 3, 4, 5**

検算: 1² + 3² + 3² + 4² + 5² = 1 + 9 + 9 + 16 + 25 = 60 = |A_5| ✓

[SOURCE: 標準指標表, Isaacs or James-Liebeck]

### 指標表の φ 値

A_5 の共役類代表: `e, (12)(34), (123), (12345), (13524)`
(位数 1, 2, 3, 5, 5 — 5-cycle は 2 つの共役類に分裂する)

2 つの 3 次元表現 χ_1, χ_2 の 5-cycle 共役類での指標:

| 表現 | χ(12345) | χ(13524) |
|:--|:--|:--|
| χ_1 (3 次元) | (1 + √5) / 2 = **φ** | (1 - √5) / 2 = **1 - φ** |
| χ_2 (3 次元) | (1 - √5) / 2 = **1 - φ** | (1 + √5) / 2 = **φ** |

[SOURCE: A_5 character table, standard reference]

**これが黄金比が A_5 に "すでに埋め込まれている" 理由**。Perron-Frobenius でも Fibonacci 量子次元でも Q-matrix 固有値でもなく、**A_5 の群表現論そのものの指標値** として φ が現れる。

### σ との接続 [仮説]

pentagon_sigma_conjecture.md 種②③ で確立した SU(2)_k family の固有値 `d_{1/2}(k) = 2cos(π/(k+2))` は k=3 で φ。A_5 の 3 次元表現指標も同じ数値を返す。

[仮説 (旧)] ✗ **反証済**: 「σ が A_5 対称性を要求すること = full coherence が A_5 既約表現テンソル積分解」。Face7Lemma §12 で K_5 自動同型群が A_5 を含まないことが示された。A_5 と σ の接続は automorphism 経由では成立しない。

[修正仮説 (現行)]: SU(2)_3 MTC の量子次元 φ と A_5 指標表の φ は、**同じ数値を別経路で返す 2 つの独立現象** の可能性が高い。表現論的同型性は未確認。σ 論文は SU(2)_3 経路 (Face5 で既に固まっている) を主、A_5 経路を参考として扱うべき。

[OPEN]: SU(2)_3 ⇔ A_5 の表現論的対応の精査。Temperley-Lieb at q = e^{iπ/5} が A_5 と関わる経路があるか [要 SOURCE 確認]。

---

## §3 McKay 対応: A_5 ↔ extended E_8

### McKay correspondence (briefly)

[SOURCE: McKay (1980) "Graphs, singularities, and finite groups"]

有限部分群 Γ ⊂ SU(2) に対し、Γ の既約表現 {V_i} と 2 次元自然表現 V の tensor product decomposition
$$V_i \otimes V = \bigoplus_j a_{ij} V_j$$
から得られる有向グラフ (McKay graph) は、対応する extended Dynkin diagram と一致する。

| Γ (SU(2) の有限部分群) | 位数 | 対応 extended Dynkin |
|:--|:--|:--|
| Cyclic Z/n | n | Ã_{n-1} |
| Binary dihedral 2D_n | 4n | D̃_{n+2} |
| Binary tetrahedral 2T | 24 | Ẽ_6 |
| Binary octahedral 2O | 48 | Ẽ_7 |
| **Binary icosahedral 2I** | 120 | **Ẽ_8** |

A_5 は 2I / {±1} の quotient。この意味で A_5 も E_8 Dynkin diagram と深く接続する。

### E_8 格子の基本事実

[SOURCE: Conway-Sloane "Sphere Packings, Lattices and Groups", Chap. 4]:
- E_8 は 8 次元の even unimodular lattice (最小次元の偶自己双対格子)
- 最短 root 数 = 240 (最小ノルム = 2)
- Coxeter number h = 30
- Weyl group 位数 = 696,729,600 = 2^14 · 3^5 · 5² · 7
- E_8 ⊃ F_4 ⊃ G_2 ⊃ SU(2)_3 ⊃ ... の chain が存在

### A_5 ↔ E_8 の幾何的実在

[SOURCE: Coxeter (1973) "Regular Complex Polytopes"]:
正 20 面体 (icosahedron) の 12 頂点は E_8 格子の特定 8 次元スライスに埋め込める。より詳細には:
- H_4 (正 120-cell / 正 600-cell の対称群, 位数 14,400) は E_8 の Coxeter plane 射影 (8D → 4D) で現れる
- H_4 ⊃ H_3 = 正 20 面体群 (A_5 × Z/2 = 120 元)

この "H_n hierarchy in E_8" は非結晶的準結晶の数学的裏付けとなり、ペンローズタイルや 5-fold 準結晶と E_8 を結ぶ [SOURCE: Levitov-Rokhsar (1988), Moody-Patera (1993)]。

[仮説 (遠)]: σ 論文の forgetting 濾過 `E_b(θ)` が θ ∈ [0, π] で 120 段階の離散化を許す場合、binary icosahedral の 120 元と同型の構造を成すかもしれない。その場合 McKay 対応経由で E_8 格子が自動的に立ち上がる。

---

## §4 Fibonacci anyon と E_8 の接続 (warning: 仮説鎖)

[SOURCE: 既知 MTC 事実]:
- Fibonacci anyon = SU(2)_3 MTC = G_2 level 1 MTC (central charge c = 14/5) [Slingerland-Bais 2001]
- E_8 at level 1 (E_8 WZW) は 1 個の primary field のみ、c = 8 [chiral boson, minimal model]

[参考 (要検証)]: Fibonacci anyon と E_8 の関係は複数の経路で示唆される:
- E_8 ⊃ G_2 の branching rule
- E_8 level 1 の coset として G_2 level 1 (= Fibonacci) が出るかどうか — c(E_8) - c(G_2) = 8 - 14/5 = 26/5 (rational だが整数でない)
- non-integer central charge coset は通常 unitary ではない

[主観]: この接続は文献上明瞭には確立していない。Kitaev (2006) "Anyons in exactly solved models" と Nayak et al. (2008) "Non-Abelian anyons" の review articles に当たるべき。本 sketch では "接続候補が存在する" とだけ記録し、SOURCE 確認は後続タスク。

### σ 論文のどこに効くか (試作)

Fibonacci anyon (種② で SU(2)_3 として登場) が E_8 chiral theory と構造的に接続するなら、σ が Face5 で閉じた時の eigenvalue φ は "E_8 から落ちてくる系列の k=3 段階" として読める可能性。

[遠仮説]: σ 論文の π-sector (`e^{iπ}+1=0`) と φ-sector (F-matrix pentagon eq) の二つは、**E_8 の Coxeter number 30 の 2 分割 (15 + 15)** から落ちてくる "最も簡単な 2 つの成分" かもしれない。

この思弁は SOURCE が遠すぎるため、現段階では独立 sketch として残し、σ 論文本体には入れない。

---

## §5 σ 論文への射程 [遠仮説 / 主観]

### 射程案 1: 「σ は E_8 型忘却の minimum realizer」

[遠仮説・高リスク]: σ の三軸 (対称・スペクトル・位相) が A_5 対称性下で揃うとき、σ は E_8 格子を generating data とする forgetting system の "最小実現者" となる。形式的には:

- 対称軸: A_5 ⊂ 2I ↔ Ẽ_8 Dynkin
- スペクトル軸: A_5 指標の φ 値 = Ẽ_8 root system の golden 方向
- 位相軸: Weyl(E_8) の Coxeter 元が Coxeter number 30 で閉じる → σ_\text{coh}(θ = 2π/30) の自然単位

これが立てば、σ は単なる "比較の 2-cell" から "E_8 格子上の最小 holonomy" に昇格する。

### 射程案 2: より慎ましやかな着地 → ✗ 反証

[仮説 (旧)] ✗ **反証済 (v0.2)**: 「A_5 対称性を σ の "3 軸揃い条件" として命題化」。Face7Lemma §12 で K_5 の自動同型群が A_5 を持たないことから、本案も弱体化。A_5 を "σ coherence の要求対称性" とする立論は成立しない。

[代替案 2']: A_5 は σ の対称性要求の場ではなく、**φ が代数的に現れる独立データ源**。σ 論文での言及は「SU(2)_3 の量子次元 φ と A_5 指標値 φ の数値一致を指摘する脚注」にとどめる。命題化は控える。

### 射程の選択 [主観]

案 1 は刺激的だが SOURCE が薄い (E_8 との接続は仮説の連鎖)。案 2 は控えめだが、Face5 → A_5 の接続ならば Face5 lemma の自然延長として現実的に書ける。v0.x では **案 2 から着手**、将来に案 1 を育てる。

### μ-retreat 警告 (v0.2 で適用)

[ラベル: ±3σ 検査]: 案 2 の反証 (v0.2) が "大きすぎるから穏当に" の μ-retreat でないかの自己検査:
- 案 2 の反証は **仮説鎖の弱点発見** (K_5 自動同型 vs σ 対称性の混同) に基づく → 健全
- 案 1 (E_8 射程) への直接影響はない (E_8 は McKay 経路で独立) → 案 1 は open で保留
- 案 2' (脚注化) への縮小は、**前提 SOURCE を増やさず主張を弱める** 方向 → 健全な撤退

案 1 E_8 射程が完全に落ちたわけではない: A_5 requirement が σ automorphism として落ちても、A_5 指標表の φ は McKay 経由で E_8 root system の golden 方向と接続する独立経路が残る。ただしこの経路は SOURCE 希薄で、本 v0.2 では open のまま。

この仕分けは pentagon_sigma_conjecture.md §4 priority list に反映済。

---

## §6 Open 問題リスト (v0.2 更新)

1. **[形式化、継続]** A_5 の 3 次元既約表現の指標値 φ と Fibonacci anyon の quantum dimension φ の関係を明示化 — 表現論的同型か数値的一致か (新) Temperley-Lieb at q=e^{iπ/5} との接続調査
2. ✓ **[完了 2026-04-17]** Face5 → Face7 lemma の試作 → `Face7Lemma_draft.md` v0.1 で検証。A_5 requirement は K_5 自動同型群との矛盾で反証 (§12)
3. **[橋 (遠)]** E_8 の 240 roots と σ の忘却濾過 `E_b` の具体的 bijection 候補 (A_5 automorphism 経路が落ちた今、McKay 経由が唯一の候補)
4. **[遠仮説検証]** σ = E_8 型最小 holonomy 案 (§5 案 1) の SOURCE 拡充。Kitaev / Nayak レビューの精読
5. **[後方接続]** pentagon_sigma_conjecture.md 種② で縮小した φ 特権化撤回を、A_5 経由で一部復元できるか (A_5 では φ は特権的) — ただし independent channel で
6. **[幾何]** 正 20 面体の H_3 対称性と E_8 の H_4 対称性の関係。ペンローズタイルとの接続経路
7. **[v0.2 新設]** A_5 不変 fusion category (or A_∞-圏) の具体例探索。σ の automorphism が A_5 である圏が存在するかは独立 open

---

## 付録: SOURCE / TAINT 台帳

- [SOURCE] A_5 階梯: Humphreys "Finite Group Representations"
- [SOURCE] A_5 指標表: Isaacs "Character Theory of Finite Groups", James-Liebeck "Representations and Characters of Groups"
- [SOURCE] McKay 対応: McKay (1980), Slodowy "Simple Singularities and Simple Algebraic Groups" (1980)
- [SOURCE] Binary icosahedral ↔ E_8: Coxeter (1973) "Regular Complex Polytopes"
- [SOURCE] E_8 格子: Conway-Sloane (1988) "Sphere Packings, Lattices and Groups"
- [SOURCE] H_4 ⊂ E_8: Moody-Patera (1993), Levitov-Rokhsar (1988)
- [SOURCE 要確認] E_8 WZW / G_2 level 1 / Fibonacci: Kitaev (2006) "Anyons in exactly solved models", Nayak et al. (2008) "Non-Abelian anyons and topological quantum computation"
- [TAINT] σ の三軸分離が A_5 で完全化するという命題 (射程案 2)
- [TAINT] E_8 roots と忘却濾過の直接対応 (射程案 1)
- [TAINT] 「σ は E_8 型最小 holonomy」という射程案 1
- [TAINT] Fibonacci ↔ E_8 の coset 接続の詳細

---

*v0.2 — 2026-04-17 Face7Lemma_draft v0.1 §12 による A_5 requirement 反証を反映。仮説 β (σ の三軸分離を要求する最小場 = A_5) は K_5 associahedron の自動同型群との矛盾で落下。修正仮説 β' (A_5 は φ の独立現れ領域) に再配置。射程案 2 は案 2' (脚注化) に縮小、案 1 (E_8 までの遠射程) は McKay 経由で独立に保留。SOURCE 部分 (A_5 指標表の φ、McKay 2I ↔ Ẽ_8) は不変。μ-retreat ではなく健全な仮説鎖弱点発見による撤退。*

*v0.1 — 2026-04-17 pentagon_sigma_conjecture.md 種⑤ から切り出し。SOURCE 部分 (A_5 階梯、A_5 指標表、McKay 対応) と仮説 (σ との接続、E_8 射程案) を明示分離。案 2 (A_5 止め) を近い作業面、案 1 (E_8 まで) を遠い保存面として仕分け。*
