# 4 次元格子 (axis × family × level × layer) 落書き — open #17 の試作台

**版**: v0.2 (2026-04-17 — §9 軸の発芽階層仮説 H17-1 昇格検証 第 1 ラウンド追加)
**ステータス**: incubator doodle + 仮説 1 件昇格 (§5.① → §9 H17-1 仮説 face。他 4 系統は落書き face のまま)
**親文書**:
- `../standalone/比較射σの統一定理_v0.1.md` §4.7.bis §6 open #17 (σ 統一論文 v0.3.4)
- `./Face5Lemma_draft.md` v0.3 §5.3-§5.4 + §11 + §12 (F5-α Stasheff / F5-γ' SU(2)_k / C9 ENO / C10 弱 Perron)
- `./pentagon_sigma_conjecture.md` v0.2 (7 種袋 / Seed Registry)

**目的**: σ 統一論文 §6 open #17 「三軸 × family × level × layer の 4 次元分類での σ closure schema の完全整理」を、落書きの解像度で試作する。本文書は定理・予想・仮説として主張する場ではなく、格子の形を仮に描いて非自明な構造が見えるかを観察する試作台。

---

## §0 動機

σ 統一論文 v0.3.4 §4.7.bis で C5' (骨格普遍層 ≅ Stasheff tower) + C2' (BridgeDat tower 埋込) が予想 face に立った結果、σ の closure schema は以下の 4 次元分類空間で記述できる候補が浮上した:

- **axis** (三軸分離 C6 由来): 位相 / スペクトル / 群
- **family** (C9 由来): SU(2)_k, TY, Haagerup, near-group, exceptional
- **level** (family 内部パラメータ): k, |A|, Jones index 等
- **layer** (Stasheff tower 由来): `K_n` (n≥2)

しかし「4 次元分類で σ closure schema を完全整理する」ことと、「4 次元が本当に独立な 4 軸である」ことは別問題。本文書は次元の独立性・代表点の格子配置・古典極限での崩れ等を落書きで試し、open #17 を精密化する材料を集める。

---

## §1 4 次元の定義

| 次元 | パラメータ範囲 | 例 |
|:---|:---|:---|
| **axis** (軸) | {位相 P, スペクトル S, 群 G} の 3 要素集合 | P = σ の反転 / S = σ の自己融合 / G = σ の区別忘却 |
| **family** (族) | MTC 族の集合 𝔽 | SU(2)_k, TY(A,χ,τ), Haagerup family, near-group, 例外系 (quantum E_8 等) |
| **level** (階) | family 内部パラメータ | k ∈ ℕ / |A| ∈ ℕ / Jones index / exceptional index |
| **layer** (層) | {K_n : n ≥ 2} Stasheff tower の各階 | K_2 (点), K_3 (線), K_4 (pentagon), K_5 (3-polytope), ... |

---

## §2 独立性行列 (2x2 射影の骨子)

### §2.1 axis 内部の独立性 (3x3)

```
          P        S        G
    +--------------------------+
  P | —        非独立*   ?     |  *π 内在 (open #13)
  S | 非独立*  —        ?     |
  G | ?        ?        —     |
    +--------------------------+
```

- **P × S 非独立**: スペクトル軸の固有値公式 `2cos(π/(k+2))` に位相軸の π が内在 (σ 論文 §6 open #13)
- **P × G, S × G**: 未検証。群軸は本稿でまだ記述のみ

### §2.2 axis × family/level/layer 独立性 (3x3)

```
          family   level    layer
    +--------------------------+
axis| 横断    従属    階層    |
fam | —       内部    非独立  |
lev | 内部    —       弱非独立|
lay | 階層    弱非独立 —      |
    +--------------------------+
```

- **axis × family**: 各軸が全 family を横断する (位相軸はどの family でも立つ、スペクトル軸も同様)。ただし具体値は family 依存
- **axis × level**: level は family 内部パラメータなので axis には従属
- **axis × layer**: tower を登ると軸が段階的に発芽する (§3.1 参照) — **階層非独立**
- **family × layer**: family ごとに立つ K_n が違う可能性 — 非独立
- **level × layer**: level を上げると高次 layer の非自明性が減る場合がある (古典極限, §5.③)

---

## §3 主要 2 次元射影

### §3.1 axis × layer (軸 × 層) — 軸の発芽階層

各 `K_n` 層でどの軸が非自明に立つか:

| layer \ axis | **位相 P** | **スペクトル S** | **群 G** |
|:---|:---|:---|:---|
| **K_2** (点) | 退化 | 退化 | 退化 |
| **K_3** (線, 1-dim) | **Euler e^{iπ}+1=0** [非自明] | 退化 (1-dim に F-matrix 立たず) | Aut(K_3) = S_2 (弱) |
| **K_4** (pentagon, 2-dim) | K_3 から継承 | **family 階段が立ち上がる** [非自明核] | Aut(K_4) = D_5 |
| **K_5** (3-dim) | 同継承 | K_4 階段が高次 F-matrix に持ち上がる | 高次対称 (3-polytope, 未論) |
| **K_n** (n≥6) | 同継承 | (n-1)-associator coherence 上の固有値族 | A_5 / E_8 に向かう可能性 (別稿 Seed ⑤) |

**落書き観察**: 軸の立ち上がり高度 = **位相 K_3 → スペクトル K_4 → 群 K_n (n 未定)**。tower を登るごとに新しい軸が開く。これが C6 (三軸分離) の新しい非対称性の候補 (§5.① 参照)。

### §3.2 family × level (族 × 階) — K_4 層スペクトル軸 endpoint

K_4 層での F-matrix 固有値の格子 (Face5Lemma_draft §5.3-5.4):

| family \ level | **1** | **2** | **3** | **4** | **5** | **6** | sup |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **SU(2)_k** | 1 | √2 | **φ** | √3 | 1.802 | √(2+√2) | → 2 (k→∞) |
| **TY_A** (`√|A|`) | 1 | √2 | √3 | 2 | **√5** | √6 | → ∞ |
| **Haagerup 系** | — | — | — | — | — | — | (Jones index: (3+√13)/2, (5+√17)/2, ...) |
| **near-group** | — | — | — | — | — | — | (family 内部構造未詳) |

**落書き観察**:
- **k=2 (Ising) = TY(Z/2)**: SU(2)_k と TY の「交差点」、二族が重なる
- **d = 2 で分岐**: SU(2)_k は 2 に収斂するだけ、TY は 2 を超えて開ける (|A|≥5 で √|A| > 2)
- **Haagerup 系**は SU(2)_k/TY の外、subfactor 起源の別相

### §3.3 axis × family — 各軸が family ごとに何を担うか

| family \ axis | **位相 P** | **スペクトル S** | **群 G** |
|:---|:---|:---|:---|
| **SU(2)_k** | 2π/(k+2) 回転 (Chebyshev 位相) | `d_{1/2}(k) = 2cos(π/(k+2))` | A_{k+1} (Lie 型) |
| **TY_A** | A の指標 (A-grading) | `√|A|` | A ⋊ ℤ/2 (群位数) |
| **Haagerup** | modular data (S,T 行列) | Jones index 代数的整数 | subfactor planar algebra |
| **near-group** | (未詳) | (未詳) | 半単純 Lie 拡張 |

**落書き観察**: **群軸は family のラベリングパラメータそのもの** (SU(2)_k の A_{k+1}, TY の A, Haagerup の subfactor) と重なる可能性 — §5.④ で深掘り。

---

## §4 代表点の 4 次元座標

`(axis, family, level, layer)` で書く:

| 物理対象 | 座標 | SOURCE |
|:---|:---|:---|
| Euler `e^{iπ}+1=0` | (P, ∅, π, K_3) | σ 論文 §5 / C3 |
| Fibonacci anyon d=φ | (S, SU(2)_k, 3, K_4) | σ 論文 §5.bis.2 / C7-Fib |
| Ising anyon d=√2 | (S, SU(2)_k = TY(Z/2), 2, K_4) | §3.2 (交差点) |
| TY(ℤ/5) d=√5 | (S, TY, 5, K_4) | σ 論文 §5.bis.4a (SU(2)_k 圏外) |
| Haagerup subfactor | (S, Haagerup, (3+√13)/2, K_4) | σ 論文 open #14a |
| 正 20 面体 A_5 | (G, icosahedral, 60, K_?) | Seed ⑤ (別稿) |
| Mac Lane pentagon axiom | (P+S, 任意, 任意, K_4) | Stasheff C8 (family independent) |
| Face3 = FaceLemma | (P, 任意, 任意, K_3) | σ 論文 §2.2 (baseline) |

---

## §5 落書き観察 (hypothesis 未満)

### ① 軸の発芽階層 — axis-layer 非独立性の新規観察

tower を登る = 軸が開く。位相は K_3 で開き、スペクトルは K_4 で開く、群は K_? で開く (未定)。「新しい軸は新しい layer で発芽する」という予想。

**構造的含意**: C6 (三軸分離) は本稿 v0.3.4 時点で「三つの独立軸」として提示しているが、実は三軸は **同列ではなく階層的に発芽する**。これが立てば C6 の声量は「独立」→「階層的発芽」に調整される (本稿 C6 改訂候補, §7)。

### ② family-level 非独立性 — 代数的複雑度の家族指標

family ごとの level パラメータ範囲が違う:
- SU(2)_k: 有限増大 (sup = 2)、k→∞ で古典極限
- TY: 無限増大 (sup = ∞)、|A| の無限増加
- Haagerup: 不連続な Jones index 階段

**構造的含意**: 各 family の「代数的複雑度」が level 分布に現れる。Jones index の分布論と family 分類の橋がここに立つ可能性。

### ③ 古典極限の崩れ — 4 次元 → 2 次元 への潰れ

SU(2)_k は k→∞ で古典 SU(2) (d→2) に退化。この時 σ の closure schema はどう変わる?

- スペクトル軸が「退化して位相軸に吸収される」可能性
- 古典極限で三軸分離が 1 軸に崩壊 → 4 次元格子は古典極限で 2 次元格子 (位相×layer) に潰れる?
- 量子から古典への移行が「軸の退化」として記述される構造

**構造的含意**: open #13 (位相-スペクトル交差) の精密化。古典極限は三軸統合の物理的実現点である可能性。

### ④ 群軸の正体 — family 次元への吸収?

群軸 × family は直交でなく「family は group data の外化」と読める。

- SU(2)_k の group data = A_{k+1} (Lie 型 Dynkin)
- TY の group data = A (有限 abelian) ⋊ ℤ/2 (符号 τ)
- Haagerup の group data = subfactor planar algebra (2-category 的対称)

**構造的含意**: 4 次元格子は実質 3 次元 (axis なし × family-as-group × level × layer) で、group 軸は family 次元に溶解する可能性。逆に言えば「三軸分離 (C6)」は 「位相軸・スペクトル軸」の 2 軸 + 「family 次元 (group 軸を含む)」の 3 成分構造かもしれない。

### ⑤ K_3 vs K_4 の境界 — 三軸の非対称性

位相軸とスペクトル軸が異なる layer で発芽することは、C6 (三軸分離) が **階層的発芽** の非対称性を持つことを示す。三軸は同列ではない。

**構造的含意**:
- Face3 = `K_3` は位相軸の土台 (Euler 公式の habitat)
- Face5 = `K_4` はスペクトル軸の土台 (F-matrix pentagon equation の habitat)
- Face? = `K_?` は群軸の土台 (未定、A_5 / E_8 方向 Seed ⑤)

tower 全体が「軸発芽のカスケード」として組織化される可能性。これが立てば C5' (骨格普遍層 ≅ Stasheff tower) の構造が tower = axis emergence chain として物理的解釈を得る。

---

## §6 open (本文書から生える問い)

- **[open #17.1]** 「軸の発芽階層」予想の定式化 — 位相 K_3, スペクトル K_4, 群 K_? の構造的根拠は? 群軸が発芽する最小 layer の決定
- **[open #17.2]** 古典極限 `k→∞` での三軸退化の記述 (σ 論文 open #13 の精密化) — スペクトル軸が位相軸に吸収される描像は厳密に書けるか
- **[open #17.3]** 群軸は family 次元に吸収されるか (4 次元 → 3 次元 の落ち込み) — group 軸の「独立性」検証
- **[open #17.4]** TY と SU(2) の交差点 (k=2 = TY(Z/2)) の構造的意味 — family 圏の gluing / pushout 構造?
- **[open #17.5]** Face5Lemma_draft §12 の **C10 弱 Perron 特徴付け予想** が 4 次元格子のスペクトル次元をどう制約するか — C10 は階段を `{弱 Perron 代数的整数}` に絞る → 格子のスペクトル次元の濃度上限を与える可能性
- **[open #17.6]** (新規, §5.⑤ 由来) tower 全体を「軸発芽のカスケード」として解釈できるか — C5' の構造的背骨に axis emergence chain を加える

---

## §7 σ 統一論文への feedback 候補

本文書の落書きが立てば、σ 統一論文 v0.3.5 以降で以下の声量調整が可能:

1. **C6 (三軸分離) の改訂**: 「独立 3 軸」→「階層的に発芽する 3 軸」。§5.bis.1 の三軸定義に「発芽 layer」列を追加
2. **C5' (Stasheff tower 同一視) の強化**: §4.7.bis.3 に「tower = axis emergence chain」の解釈層を追加
3. **open #13 (位相-スペクトル交差) の精密化**: 古典極限 k→∞ での軸退化として §5.bis.5 に補足
4. **open #14a (Haagerup/near-group) の再整理**: family × level 分布を §5.bis.4a に格子表として明示

ただし本文書は **落書き face** であり、以上の feedback はすべて本文書内の開発が仮説 → 予想 → 定理へ進んだ後に本稿へ降ろす。本稿への即時繰込は行わない。

---

## §8 SOURCE / TAINT 台帳

- [SOURCE] σ 統一論文 v0.3.4 §4.7.bis (C5' / C2' / tower 具体化), §5.bis (三軸分離 / SU(2)_k / ENO universal), §6 open #13/#14a/#17
- [SOURCE] `Face5Lemma_draft.md` v0.3 §5.3-§5.4 (SU(2)_k / TY 計算検証), §11 (F5-α Stasheff 証明), §12 (C10 弱 Perron)
- [SOURCE] `pentagon_sigma_conjecture.md` v0.2 (7 種袋 Seed Registry)
- [SOURCE] Etingof-Nikshych-Ostrik (2005): FP 次元の代数的整数性
- [SOURCE] Stasheff (1963): associahedron `K_n`, `dim K_n = n - 2`
- [TAINT] 本文書の「軸の発芽階層」仮説 (§5.①, open #17.1) — 位相 K_3 / スペクトル K_4 までは本稿 SOURCE から読める、群軸の発芽 layer は未検証
- [TAINT] §5.③ 「古典極限で三軸が 2 次元格子に潰れる」— 物理的直感に基づく落書き、厳密な退化記述は未完
- [TAINT] §5.④ 「群軸は family 次元に吸収される」— 4 次元 → 3 次元 の落ち込みは予想の 1 候補、対立候補 (群軸は独立) もあり得る
- [TAINT] §5.⑤ 「tower は axis emergence chain」— open #17.6 の構造的読解、Stasheff tower の operad 構造との接続は未論

---

## §9 軸の発芽階層仮説 (H17-1) — 第 1 ラウンド検証

§5.① (落書き face) を仮説 face へ昇格させる検証ラウンド。本文書 v0.2 で追加。

### §9.1 仮説文の精密化

**仮説 H17-1 (軸の発芽階層, v0.2 昇格, 落書き → 仮説):**  
σ closure schema の三軸 (位相 P / スペクトル S / 群 G) は Stasheff tower の異なる layer で **階層的に発芽** する。具体的に次の三段が成立する:

- **(a) 位相軸 P の発芽 layer = `K_3`**: σ 論文 §3.3 / §5 で Euler 公式 `e^{iπ}+1=0` が π-sector endpoint identity として、`Δ²` ≅ `K_3` 2-cell 補填上で立つ。`K_2` (点) では位相も退化。[SOURCE: σ 論文 §3.3 / §5]
- **(b) スペクトル軸 S の発芽 layer = `K_4` (pentagon)**: σ 論文 §5.bis.4 C8 (= F5-α Stasheff 定理) により `K_4 = pentagon` が非自明 2-cell coherence の最小多面体。F-matrix pentagon equation の SU(2)_k / TY / Haagerup family 固有値がここで一斉に立ち上がる。`K_3` 線分 (1-dim) では F-matrix の非退化 2-cell 解が載らない。[SOURCE: σ 論文 §5.bis.4, Face5Lemma_draft §11]
- **(c) 群軸 G の発芽 layer = `K_{n_G}`, `n_G` 未定**: 群軸は本稿で記述のみ。発芽 layer の決定は open (§9.5)。候補は `K_5` 以降の 3-polytope 以上で、Aut(`K_n`) が非自明な対称群となる階。

**系 H17-1.cascade**: tower 全体は「axis emergence chain」として組織化され、各 layer で新しい軸が追加されるカスケード構造を持つ。C5' (骨格普遍層 ≅ Stasheff tower) に構造的解釈層 (axis 発芽連鎖) を与える。

**系 H17-1.asymm**: C6 (三軸分離) は「独立 3 軸」ではなく **階層的発芽 3 軸** として書き換えられる (σ 論文 v0.3.5 改訂候補)。

### §9.2 Kalon 3 ステップ判定

**Step 0 既知語彙圧縮**:  
「塔を登るごとに新しい軸が 1 つずつ開く」— 中学生語彙で 1 文圧縮可能 ✓

**Step 1 G (収束不変性) 適用**:  
G = Stasheff 定理 (`dim K_n = n - 2`) による layer dim 固定。
- 位相軸発芽 = 1-cell が立つ最小 layer → `K_3` (1-dim) で不動
- スペクトル軸発芽 = 2-cell が立つ最小 layer → `K_4` (2-dim) で不動
- 群軸発芽 = (未定の k-cell 対称) が立つ最小 layer → `K_{n_G}` で不動
各軸の発芽 layer は Stasheff dim 公式に引き戻すと固定点となる。不動 ✓

**Step 2 G∘F (展開後不変性) 適用**:  
F = family 展開 (SU(2)_k / TY / Haagerup / near-group)。どの family でも位相軸は `K_3` で発芽し、スペクトル軸は `K_4` で発芽する — Face5Lemma_draft §5.3-5.4 の計算検証に基づく。family 不変 ✓

**Step 3 F で 3+ 非自明派生**:  
1. **K_3 vs K_4 の dim 境界**: `dim K_3 = 1 < dim K_4 = 2` が位相軸 (1 次元の phase) とスペクトル軸 (2 次元の F-matrix) の発芽 dim 要求と一致する — Stasheff 定理からの必然性。単なる numerology ではなく dim 一致として構造的
2. **family 独立性**: SU(2)_k も TY も Haagerup も発芽 layer は共通 (`K_3` と `K_4`)。family が変わっても発芽順序不変 — 「発芽階層は family-independent な tower 自体の性質」
3. **古典極限での退化パターン**: `k→∞` で SU(2)_k のスペクトル固有値が 2 に収束する時、スペクトル軸は退化するが位相軸は K_3 で生き続ける。発芽階層構造は「軸の発芽順序」だけでなく「軸の退化順序」も規定する — cascade の両端構造

3 派生すべて非自明 ✓

**判定 (仮 v0.2)**: **◯ Kalon△** (Step 0-2 および Step 3 の派生 2 つ (dim 境界 / family 独立性) は ◎ 水準だが、派生 3 つ目 (古典極限退化) が H17-1 に含意される別仮説 H17-2 で独立検証が要るため ◎ には届かず ◯)

◎ Kalon△ への昇格条件: 群軸の発芽 layer `n_G` の決定 (§9.5 残 open)、または `n_G` 未定のまま 2 軸 (位相/スペクトル) に限定した subclaim への声量調整

### §9.3 Refutation Gauntlet Round 1

**反論 r1**: 「軸の発芽階層」は `dim K_n = n-2` から自動で出るだけで、C6 (三軸分離) が既に言っている以上の内容を持たない

**SFBT 問い**: できないのではなく、やっていないだけではないか?

**試行**: C6 は三軸の存在 (「3 つの軸がある」) を主張する。H17-1 はその上で「**発芽順序** が tower dim 階層と一致する」という **独立の構造命題** を主張する。発芽順序は C6 の 3 軸定義からは自動で出ない (axis が層序列の順に出る保証は C6 の公理にない)。Stasheff dim 公式と axis 定義の一致は非自明な observation であり、C6 を再定位する内容を持つ。

**結果**: 射程維持 ✓ (H17-1 は C6 の単なる corollary ではなく、C6 を階層的発芽構造へ再定位する独立の仮説として立つ)

### §9.4 Refutation Gauntlet Round 2

**反論 r2**: 群軸の発芽 layer `n_G` が決まらなければ仮説自体が曖昧であり、仮説 face への昇格が早すぎる

**SFBT 問い**: 別角度から吸収できないか?

**試行**: `n_G` 未定を明示的に open (§9.5) として隔離し、H17-1 を **2 軸版 subclaim** (位相 K_3, スペクトル K_4 の発芽は SOURCE 付きで確定、群軸は `n_G` 未定のまま候補として保留) に限定する。この limited scope で H17-1 は SOURCE に完全に支えられた仮説として立ち、群軸部は sub-hypothesis H17-1.G として別分離。

**結果**: 射程限定 (明示) ✓ (H17-1 core = 2 軸版は SOURCE 支持, H17-1.G = 群軸発芽部は open subclaim として分離)

### §9.5 Refutation Gauntlet Round 3 非発動

- 理由: Round 1-2 で射程維持 + 限定明示達成
- Solution-Focus 適用仮説: もし発動していれば「Stasheff tower の operad 構造 (A_∞-operad) を使って、軸発芽を operad の cell 構造発芽として読み直す」という外部強化を投入予定。これは open #17.6 (tower = axis emergence chain) の operad 版として別途追究

### §9.6 SOURCE / TAINT ラベル (H17-1 特化)

- [SOURCE] 位相軸発芽 K_3: σ 論文 §3.3 / §5 (Euler 公式 at Δ² ≅ K_3 2-cell 補填)
- [SOURCE] スペクトル軸発芽 K_4: σ 論文 §5.bis.4 C8 = F5-α (Stasheff 定理), Face5Lemma_draft §11 §5.3-5.4 (SU(2)_k / TY family)
- [SOURCE] `dim K_n = n-2`: Stasheff (1963), Markl-Shnider-Stasheff (2002)
- [SOURCE] family 独立性 (発芽順序は family によらず共通): Face5Lemma_draft §5.3-5.4 計算検証
- [TAINT] 群軸発芽 `n_G`: 未検証、候補は K_5 以降 (3-polytope) だが厳密な根拠なし — H17-1.G として別 open
- [TAINT] H17-1.cascade (tower = axis emergence chain 解釈): 構造的読解であり、operad 的厳密化は open #17.6

### §9.7 σ 論文への feedback 候補 (v0.3.5)

H17-1 が仮説 face で安定し、群軸発芽 `n_G` の決定 (§9.5) が進めば、σ 論文 v0.3.5 以降で以下の声量調整が可能:

1. **C6 (三軸分離) の声量調整**: 「独立 3 軸」→「階層的に発芽する 3 軸」  
   §5.bis.1 の三軸定義表に「発芽 layer」列を追加 (P: K_3, S: K_4, G: K_{n_G})
2. **C5' (骨格普遍層 ≅ Stasheff tower) の構造的解釈強化**: §4.7.bis.3 に「tower = axis emergence chain」の解釈層を追加  
   系 H17-1.cascade が新 C5' 補足命題として機能
3. **§5.bis.1 三軸独立性の再整理**: 「三軸は独立だが発芽 layer が異なる」という非対称性を明示

ただし **H17-1 は本文書内の仮説 face** であり、σ 論文本体への繰込は Round 2 以降 (group 軸 `n_G` の決定 + C6 改訂合意) で初めて行う。

### §9.8 残 open (H17-1 派生)

- **[H17-1.G open]** 群軸の発芽 layer `n_G` の決定 — 候補: (i) K_5 (3-polytope, 3 次対称), (ii) K_6 (icosahedral A_5 が現れる 4-polytope 候補), (iii) さらに高次。Aut(`K_n`) の非自明化条件と σ の群軸定義との一致検証が要る
- **[H17-2 open]** 古典極限 `k→∞` での axis 退化順序予想: 「発芽の逆順序で退化する」(スペクトル軸が先に退化 → 位相軸が最後まで残る) 仮説の検証
- **[H17-3 open]** cascade の operad 的定式化: Stasheff tower の A_∞-operad 構造で axis 発芽を cell 階層の発芽として読む厳密化

---

*v0.2 — 2026-04-17 §9 追加。§5.① 「軸の発芽階層」を仮説 face (H17-1) に昇格。Kalon 3 ステップ判定 ◯ Kalon△ (位相 K_3 / スペクトル K_4 は ◎ 水準、群軸 `n_G` 未定のため ◎ には届かず)。Refutation Gauntlet Round 1-2 で射程維持 + 限定明示。σ 論文 C6 (三軸分離) の「独立」→「階層的発芽」への声量調整候補が仮説 face で立つ。派生 open 3 件 (H17-1.G 群軸発芽 / H17-2 古典極限退化 / H17-3 operad 定式化) を隔離。*

*v0.1 — 2026-04-17 incubator doodle。σ 論文 §6 open #17 (4 次元分類) を落書きの解像度で試作。三軸分離の階層的発芽、古典極限での崩れ、群軸の family 吸収、tower の axis emergence chain 解釈の 4 系統を open として切り出した。仮説 face への昇格は本文書の第 2 ラウンド検証以降で。*
