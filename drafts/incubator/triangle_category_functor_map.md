# 三角形（幾何）⇄ 圏論 対応リファレンス

**版**: v4.1 (2026-04-17)
**ステータス**: 公式リファレンス（純粋対応表）+ §3.bis 正五角形への射程拡張 (Strong + Analogy)
**核フレーミング**: 三角形 = 計量付き 2-圏的 2-単体 / 長さ = metric enrichment / 角 = phase

> 開発過程の Integrity Verdict / 棄却台帳 / Source Ledger は `triangle_category_functor_map_development_log.md` に分離。

---

## §0  一目でわかる対応

```
三角形                    圏論
─────────────────────────────────────
頂点            ↔  0-cell (対象)
辺              ↔  1-cell (射)
面 (内部)       ↔  2-cell (2-morphism)
長さ ℓ          ↔  metric enrichment d: Hom → [0,∞]
角 θ            ↔  phase / turning: ∂ → S¹
三角不等式      ↔  合成則 d(A,C) ≤ d(A,B) + d(B,C)
```

無向辺は「互いに逆向きの 1-cell の対」として扱う。

---

## §1  関手の骨組み

### walking triangle Δ²

三角形の抽象データを担う最小の 2-圏。**3 対象 + 3 生成射 + 1 非自明 2-cell**：

```mermaid
graph LR
    A -->|f| B
    B -->|g| C
    A -->|h| C
```

2-cell `σ: g∘f ⇒ h` が面を塗る。圏論標準用語では **walking X** = 構造 X を普遍的に実現する最小の圏 (Street / Leinster / nLab)。

| walking X | 対象 | 生成データ |
|:---|:---|:---|
| walking arrow `[1]` | 2 | `f: 0→1` |
| walking composition | 3 | `f, g, g∘f` |
| walking 2-cell | 2 | `f,g: 0⇉1`, `α: f⇒g` |
| **walking triangle Δ²** | **3** | **`f,g,h` + `σ: g∘f ⇒ h`** |

`Δ²` は walking arrow / walking composition / walking 2-cell を同時に普遍的に含む。

### 関手 𝓕: Δ² → 𝒟

```
𝓕: Δ²  →  𝒟

    3 対象 A,B,C  ↦  𝒟 の対象
    3 射 f,g,h    ↦  𝒟 の射
    2-cell σ      ↦  𝒟 の 2-cell  σ: 𝓕(g)∘𝓕(f) ⇒ 𝓕(h)
    合成と恒等を保存
```

**universal property**: 任意の 2-圏 `𝒟` の中の「三角形パターン」は `Δ²` からの 2-関手と一対一対応する。

### L0–L4 実在化ラダー

domain は常に `Δ²`、**変化するのは codomain のみ**：

| L | codomain | ここで初めて言えること |
|:---|:---|:---|
| L0 | 純粋 2-圏 | 頂点・辺・面 |
| L1 | Lawvere 計量豊穣 2-圏 | 辺の長さ、三角不等式 |
| L2 | S¹ 作用付き 2-圏 | 内角・外角・境界 holonomy |
| L3 | Euc² 幾何 2-圏 | 中線・重心・内心・外心・内接/外接円 |
| L4 | dagger / Hilbert 2-圏 | 三平方 |

### 自己同型関手

自己同型 `𝓕: Δ² → Δ²` は **対称群 S₃** (3 回転 + 3 鏡映)。「辺のつながりを壊さない変換」の group-theoretic 表現。

---

## §2  基本対応表

13 項目を **最小前提 L 層 / 形式化候補 / 前提を落とすと壊れる点 / 強度** で整理。

| # | 幾何 | 圏論対応 | 最小前提 | 形式化候補 | 壊れる点 | 強度 |
|:---|:---|:---|:---|:---|:---|:---|
| ① | 内角 | 頂点での局所 turning / phase | L2 | θ: 頂点 → S¹ | L2 なしでは角は射の並びに退化 | Medium |
| ② | 外角 | 境界 holonomy | L2 | holonomy: ∂Δ → S¹ | 境界 holonomy 不定義 | Medium |
| ③ | 辺の長さ | metric 豊穣化 Hom | L1 | d: Hom → [0,∞] | 純粋圏では内在しない | **Strong** |
| ④ | 中線 | 頂点 → 対辺中点 object の canonical arrow | L3 affine | 中点 canonical arrow | 計量だけでは中点一意ならず | Analogy |
| ⑤ | 角の二等分線 | 局所 phase を等分する方向射 | L3 affine + L2 | turning を等分する射 | 対辺との交点保証消失 | Analogy |
| ⑥ | 内心 | 3 辺への等距離普遍対象 | L3 Euc | 辺距離 equalizer | 実現なしでは等距離比較不能 | Analogy |
| ⑦ | 外心 | 3 頂点への等距離普遍対象 | L3 Euc | 頂点距離 equalizer | 同上 | Analogy |
| ⑧ | 重心 | 3 頂点の等重み barycenter | L3 affine | weighted colimit | affine 平均構造に依存 | Analogy |
| ⑨ | 辺と角の大小 | 長さと対向 turning の単調対応 | L3 (余弦定理) | c² = a²+b²−2ab·cos C | 一般計量では余弦定理等号不成立 | Medium |
| ⑩ | 三角形成立条件 | 三角不等式 = 合成則 | L1 | d(A,C) ≤ d(A,B) + d(B,C) | 合成が距離として読めない | **Strong** |
| ⑪ | 内接円 | 内心中心の side-distance level set | L3 Euc | 辺距離一定軌跡 | 円形は Euclidean 平面特有 | Analogy |
| ⑫ | 外接円 | 外心中心の vertex-distance level set | L3 Euc | 頂点距離一定軌跡 | 球面では小円、双曲面では超曲線 | Analogy |
| ⑬ | 三平方 | ‖u+v‖² = ‖u‖² + ‖v‖² (u⊥v) | L4 内積 | dagger / Hilbert | metric のみでは直交性不足 | **Strong** |

### 強度ラベル

- **Strong**: 圏論言語で直接書き下せる構造命題（L1-L2 の enrichment だけで閉じる）
- **Medium**: 追加構造が入れば構造命題、欠けると比喩
- **Analogy**: L3 以上の実現を要する設計的対応

---

## §2.bis  metric 退化と自己同型の随伴

§1 末尾の自己同型 `Aut(Δ²) = S_3` は、L1 metric 豊穣を加えると metric 像の退化度に応じて縮退する。「二等辺 = 1 辺を複製した三角形」という素朴直観は、圏論的には **metric 関手 `d: {f,g,h} → [0,∞]` の fiber が粗くなる degeneration** として読む。関手の domain 側で辺を増やすのではなく、codomain 側の metric が退化することで対称性が拡大する。

### 退化度 ↔ Stab の対応

| 三角形 | `d` の像 | Stab ⊆ S_3 | &#124;Stab&#124; |
|:---|:---|:---|:---|
| 不等辺 | 単射 (3 値独立) | `{e}` | 1 |
| 二等辺 | 2-to-1 fiber を 1 つ持つ | `Z/2` | 2 |
| 正三角形 | 定数 (3-to-1 fiber) | `S_3` | 6 |

随伴的読み:

```
d の fiber 粗さ  ⟺  S_3 軌道の融合度  ⟺  Aut の大きさ
```

### walking 派生の明示

| walking X | 対象数 | 追加制約 | Stab |
|:---|:---|:---|:---|
| scalene (= `Δ²`) | 3 | なし | `{e}` |
| **isosceles** | 3 | `d(f)=d(g)` | `Z/2` |
| **equilateral** | 3 | `d(f)=d(g)=d(h)` | `S_3` |

これらは `Δ²` 上の metric 制約による quotient で得られ、`§1` の L0→L1 昇格 (純粋 2-圏 → 計量豊穣) でのみ意味を持つ。L0 では辺の区別が長さを持たないので退化そのものが定義できない。

---

## §3  4 機械メタ構造

幾何三角形の対応を支える **4 つの独立装置**。各機械は固有の入力・内部規則・出力を持つ自律的な圏論的機構。

| 機械 | 入力 | 内部規則 | 出力 |
|:---|:---|:---|:---|
| **M1 回転機械** | θ ∈ ℝ | `ρ: θ ↦ 回転行列 / e^(iθ)` | S¹ 上の点、cos/sin |
| **M2 交代和機械** | chain complex | `χ = Σ(−1)ᵏ cₖ` | 不変量 χ ∈ ℤ |
| **M3 再帰スペクトル機械** | 再帰 endomorphism | 特性方程式の対角化 | 固有値 (φ, ψ) |
| **M4 exactness 機械** | 3 対象 + 3 射 | TR1–TR4 + shift [1] | distinguished triangle |

### M1: 回転機械

入力 `θ ∈ ℝ` → 出力 回転表現。

```mermaid
graph LR
    R["ℝ (加法)"] -->|exp·i| S1["S¹ (乗法)"]
    S1 -->|ρ| Rot["SO(2) 回転行列"]
```

```
ρ(θ) = | cos θ   -sin θ |       e^(iθ) = cos θ + i sin θ
       | sin θ    cos θ |
```

- **sin, cos** = 回転表現の **行列要素**
- **tan** = `cos θ ≠ 0` 上の **射影座標** (派生量、主役ではない)
- **π** = `ℝ → S¹` の **周期化商** (θ ∼ θ + 2π)
- **e** = 指数写像の **規格化定数** (加法 → 乗法)

**オイラー等式** `e^(iπ) + 1 = 0` = 一般法則 `e^(iθ₁)·e^(iθ₂) = e^(i(θ₁+θ₂))` の **半回転特殊化**。

### M2: 交代和機械

入力 chain complex → 出力 Euler 標数。

```mermaid
graph LR
    C3 -->|∂| C2
    C2 -->|∂| C1
    C1 -->|∂| C0
    chain["chain complex C•"] -->|"Σ(−1)ᵏ cₖ"| chi["χ ∈ ℤ"]
```

- 三角形: V=3, E=3, F=1 → `χ = 3 − 3 + 1 = 1` (2-disk)
- 四面体: V=4, E=6, F=4 → `χ = 2` (球面)
- 一般: `χ = Σₖ (−1)ᵏ cₖ`

本体は **chain complex の交代和**。多面体公式 `V − E + F = 2` はその 3 次元特殊化。

### M3: 再帰スペクトル機械

入力 再帰 endomorphism (Q-matrix) → 出力 固有値。

```
| F_{n+1} |   | 1  1 | | F_n     |        Q = | 1 1 |
|         | = |      | |         |            | 1 0 |
| F_n     |   | 1  0 | | F_{n−1} |
```

```mermaid
graph LR
    inflate["inflation S→L, L→LS"] -->|linearize| Q["Q-matrix"]
    Q -->|diagonalize| spec["spectrum (φ, ψ)"]
```

特性方程式 `λ² − λ − 1 = 0` の根:

- **φ = (1 + √5)/2** ≈ 1.618 = **支配的成長モード** (Perron-Frobenius)
- **ψ = (1 − √5)/2** ≈ −0.618 = **従属的補正モード**

inflation rule `S ↦ L, L ↦ LS` が symbolic dynamics 側表現 (詳細は Appendix B)。

### M4: exactness 機械

入力 3 対象 + 3 射 → 出力 distinguished triangle。

```mermaid
graph LR
    X -->|f| Y
    Y -->|g| Z
    Z -->|h| X1["X[1]"]
```

公理 TR1–TR4 + shift functor `[1]`。homological functor は long exact sequence を生む。

**decategorification**:

```
K₀(𝒟) 上で  [Y] − [X] − [Z] = 0        (distinguished triangle より)
χ(X) = Σᵢ (−1)ⁱ [Hⁱ(X)]  が additive  (derived category 上)
```

### M2 ⇄ M4: decategorification 橋

```
     M2 (χ)                  M4 (K₀)
  ┌─────────┐  decategorify  ┌─────────┐
  │ 幾何側   │ ←──────────→  │ 圏論側   │
  │ 不変量   │                │ 不変量   │
  └─────────┘                └─────────┘
```

M2 ↔ M4 軸が「**幾何三角形**」と「**exact triangle**」を、名前の一致ではなく **decategorified invariant** として結ぶ主線。M1 は M4 の基礎 (回転群が shift を代替する局面)、M3 は M2 の動力学化 (交代和を時間発展で読む局面) として M2 ↔ M4 軸に寄り添う。

---

## §3.bis  正五角形 — Fibonacci inflation の幾何実装

§3 M3 の inflation rule `S ↦ L, L ↦ LS` と Q-matrix は symbolic / 線形代数で記述される抽象規則。**正五角形はこれを平面幾何で具現する標準例**。

### 3 分割

正五角形の辺長 `s`、対角線長 `d` は `d/s = φ`。1 頂点から 2 本の対角線を引くと 3 三角形に分割される:

| 位置 | 辺の組 | symbolic | 角 | 三角形型 |
|:---|:---|:---|:---|:---|
| 両脇 (2 個) | `(s, s, φs)` | `(S, S, L)` | 36°-36°-108° | 鈍角二等辺 |
| 中央 (1 個) | `(φs, s, φs)` | `(L, S, L)` | 72°-36°-72° | 黄金二等辺 |

中央の `(L, L, S)` は inflation rule `L ↦ LS` の 1 ステップ像 (L を L と S に拡張したときの辺比対応)。両脇の `(S, S, L)` は `S ↦ L` 側の双対像。3 三角形を組み合わせた正五角形は **inflation rule の 1 段階を空間に刻んだ図形**。

### φ の発現

M3 Q-matrix `[[1,1],[1,0]]` の主固有値 `φ = (1+√5)/2` は、文字個数ベクトル `(#L, #S)` の Perron-Frobenius 支配モード。**正五角形の対角線は `L`、辺は `S`** に対応するので、`d/s = φ` は抽象主モード比が幾何に射影された形。古典的には相似と二次方程式 `x² − x − 1 = 0` から出るが、圏論骨格では Q-matrix の対角化として読める。

### pentagram の 35 三角形

5 本すべての対角線を引くと pentagram が得られ、内部に **35 個の二等辺三角形** (黄金型 20 + 鈍角型 15) が現れる。これは inflation rule の反復適用を平面に展開した自己相似構造で、対角線の交点に現れる小五角形が `1/φ²` スケールで nest する。

- golden (36°-72°-72°): 20 個 (大 5 + 中 10 + 小 5)
- obtuse (36°-36°-108°): 15 個 (大 10 + 小 5)

`φ² = φ + 1` (Fibonacci 恒等式) の空間版が pentagram の自己相似 nest、と読める。

### M3 との対応

| M3 (抽象) | §3.bis (幾何) |
|:---|:---|
| `S ↦ L, L ↦ LS` | 対角線/辺の長さ対応 |
| Q-matrix 主固有値 `φ` | `d/s = φ` |
| `n → ∞` 漸近 | pentagram 自己相似 nest |
| inflation step | 1 頂点からの 2 対角線分割 |

pentagon は inflation rule の **最低次元な平面実装**。球面三角形 (Appendix A.2) が曲率付き実現なら、pentagon は **再帰付き実現**。

### 3 軸分離 — closure schema の独立軸

Δ² と P₅ を並べると、**三つ組の閉じ方 (closure schema)** が 3 つの独立軸に分離できることが見える。§1 自己同型関手節 (S₃) は 3 軸の 1 つ (対称軸) にすぎない。

| 軸 | 数学的対象 | Δ² での実現 | P₅ での実現 | 強度 |
|:---|:---|:---|:---|:---|
| **対称軸** (辺の区別消失) | 自己同型群 | S₃ (3! = 6 元) | D₅ (10 元) | Strong |
| **スペクトル軸** (自己相似比) | 固有値 | 正三角形で 1 に退化 | **φ, 1/φ** (Q-matrix 対角化) | Strong (§3 M3) |
| **位相軸** (端点で閉じる) | 周期化商 | `e^{iπ}+1=0` (半周回) | F-行列 pentagon equation | Analogy |

**読み**: Δ² ではスペクトル軸と位相軸が退化または自明化 (正三角形では固有値 1 のみ、位相は S¹ の任意点で閉じる) するため、1 軸で閉じるように見える。P₅ では 3 軸すべてが非自明に立つ。

- **対称 → スペクトル**: S₃ が退化しない (正三角形にならない) と D₅ が立ち、D₅ の不変量として Q-matrix 固有値 φ が出てくる
- **スペクトル → 位相**: φ が F-行列の成分として現れると、その F-行列が満たす pentagon equation が位相軸の非自明実現を担う
- **位相 → 対称**: pentagon equation の解を要求する coherence が、結果として D₅ および A₅ (正 20 面体群) の対称性を選ぶ

[Open] 位相軸の Mac Lane pentagon coherence 解と Fibonacci anyon F-行列との接続は、本リファレンスの射程を超える。σ 統一論文または incubator `pentagon_sigma_conjecture.md` で育てる対象。

---

## §4  exact triangle との境界

**同名警告**: 幾何三角形は triangulated category の exact triangle ではない。

| 幾何の三角形 | exact triangle |
|:---|:---|
| 3 頂点・3 辺・1 面 | 3 対象 + 3 射、最後は `Z → X[1]` |
| 平面内で閉じる | shift を介して閉じる |
| 長さ・角度が主役 | exactness・cohomology が主役 |
| 面積をもつ | long exact sequence を生む |
| metric + phase 要 | TR1–TR4 + shift 要 |

両者が共有するのは「**三つ組の閉じ方 (closure schema)**」というメタ構造のみ。具体的接続は §3 M2 ⇄ M4 の decategorification 橋 (`χ ↔ K₀`) 経由。

**誤読回避**: 「triangle という名前が同じだから対応する」ではなく、「`K₀` / Euler characteristic 経由の decategorification が、幾何の交代和不変量と圏論の exactness 不変量を同一視する」という経路だけが構造命題。

---

## Appendix A — Worked Examples

### A.1  3-4-5 直角三角形 (L1 + L3 + L4 のフル実装)

- **L1 metric**: `d(A,B) = 3, d(B,C) = 4, d(A,C) = 5`。三角不等式 `5 ≤ 3 + 4` ✓
- **L3 Euclidean**: 座標 `A = (0,0), B = (3,0), C = (0,4)`。重心 `G = (1, 4/3)`。内心・外心・内接円半径 `r = 1`・外接円半径 `R = 5/2` が一意に決まる
- **L4 Hilbert**: `3² + 4² = 5²` (三平方)。ベクトル形 `‖u+v‖² = ‖u‖² + ‖v‖²` が `u ⊥ v` で成立

**要点**: 内積実現の典型。L0–L4 ラダーのすべての層が同時に走る標準例。

### A.2  球面三角形 (L1 + L2 + L3')

- **L2 phase**: 内角和 `> π`。外角 holonomy の積分は **Gauss-Bonnet** で球面曲率に一致
- **L3' 球面幾何**: 外接「円」は球面上の **小円**。余弦定理は球面版:
  ```
  cos(c/R) = cos(a/R) cos(b/R) + sin(a/R) sin(b/R) cos C
  ```
- 平面三角形の余弦定理 `c² = a² + b² − 2ab cos C` は `R → ∞` 極限で回復

**要点**: 曲率付き実現の典型。「角 = turning」「辺 = metric」の読みが Euclidean 直感から独立に機能することを示す。

---

## Appendix B — Fibonacci Inflation Rule

§3 M3 の symbolic dynamics 側表現。

### inflation rule

```
S ↦ L
L ↦ LS
```

初期文字列 `L` から反復:

```
Step 0: L                     (長さ 1)
Step 1: LS                    (長さ 2)
Step 2: LSL                   (長さ 3)
Step 3: LSLLS                 (長さ 5)
Step 4: LSLLSLSL              (長さ 8)
Step 5: LSLLSLSLLSLLS         (長さ 13)
```

各ステップの文字列長が Fibonacci 数列 `1, 2, 3, 5, 8, 13, ...`。`#L / #S` 比は `n → ∞` で `φ` に収束 (Perron-Frobenius 支配モード)。

### Q-matrix 表示

inflation rule を文字個数ベクトル `(#L, #S)` に作用させると:

```
| #L_{n+1} |   | 1  1 | | #L_n |
|          | = |      | |      |
| #S_{n+1} |   | 1  0 | | #S_n |
```

これは §3 M3 の Q-matrix そのもの。**Q-matrix は inflation rule の線形代数的影**。

**読み**: φ と ψ は単なる数値ではなく、**生成規則を対角化したときのスペクトル不変量**。`n-cell tower` の有効構成数が Fibonacci 再帰に従う現象は、この inflation rule と同一構造。

---

## 用語索引

| 用語 | 節 | 定義 |
|:---|:---|:---|
| walking triangle `Δ²` | §1 | 三角形データを普遍実現する最小 2-圏 |
| L0–L4 ラダー | §1 | codomain の enrichment 階層 (純粋 → 計量 → phase → Euc → Hilb) |
| 最小前提 | §2 | 各対応が成立するための最小 L 層 |
| 4 機械 (M1–M4) | §3 | 回転 / 交代和 / 再帰スペクトル / exactness の独立装置 |
| decategorification 橋 | §3 | `χ ↔ K₀` 経由の幾何⇄圏論接続 |
| closure schema | §4 | 幾何 triangle と exact triangle が共有するメタ構造 |
| Perron-Frobenius | §3 M3 / App B | 正値行列の支配的固有値定理 |
| 正五角形 `P₅` / pentagram | §3.bis | inflation rule の幾何実装、35 個 isosceles の自己相似 nest |
| 3 軸分離 (対称/スペクトル/位相) | §3.bis | closure schema を自己同型群・固有値・周期化商の 3 独立軸に分解 |

---

*v4.1 — 2026-04-17 §3.bis に「3 軸分離」節を追補。対称 (S₃/D₅) / スペクトル (φ) / 位相 (e^{iπ}/pentagon eq) の独立軸を明示。v4.0 骨格は不変。*
*v4.0 — 公式リファレンス版。v3.2 以前の全記録 (Integrity Verdict / 棄却台帳 / Source Ledger / 設計過程メタノート) は `triangle_category_functor_map_development_log.md` に保存。*
