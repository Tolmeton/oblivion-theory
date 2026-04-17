# 正五角形 × σ 予想 — 7 落書きの種袋

**版**: v0.4 (2026-04-17)
**ステータス**: incubator (種の保存先。v0.1 で種①-⑦, v0.2 で種⑤⑦ sketch 化, v0.3 で Face7Lemma 試作, v0.4 で種⑧ KAM / 種⑨ 連分数 追加)
**親文書**:
- `../standalone/比較射σの統一定理_v0.1.md` (σ 統一論文本体)
- `./triangle_category_functor_map.md` (三角形 ⇄ 圏論 対応リファレンス)
- `../standalone/統一表の関手化_構想ドラフト_v0.2.md` (π-sector endpoint identity)

---

## §0 発端の問い (2026-04-17 Tolmetes ↔ Claude)

Tolmetes の直感:
- 二等辺三角形 = 辺 A-B を「関手で 2 辺に増やした」三角形
- 正三角形 = 辺 A-B を「関手で 3 辺に増やした」三角形
- 正五角形 = (A,A,B) + (B,B,A) + (A,A,B) の glued triangle 構造 (添付画像: 頂点から 2 本の対角線を引いた分割)
- Mathsuke.jp によれば、全対角線込みの pentagram には **35 個の二等辺三角形** (黄金 20 + 鈍角 15)

核の問い: これは圏論的に何を意味するのか?

---

## §1 直感の言い換え (Claude による translate)

[主観]: 「関手で辺を増やす」は向きが逆で捉えたほうが綺麗。Δ² の **自己同型群の部分群選択** として読める。

| 三角形 | metric 像 | 自己同型群 | Δ² との関係 |
|:---|:---|:---|:---|
| 不等辺 | 3 値すべて異なる | {e} | generic Δ² |
| 二等辺 | 2 値に退化 | Z/2 | Δ² / 2 辺同一視 |
| 正三角形 | 1 値に完全退化 | S_3 | Δ² / 全辺同一視 |

「関手で増やす」 → 「自己同型で区別を消す」と訳し直すと、三角形の分類は群論の部分群束と同型になる。

---

## §2 7 落書きの種

各種は **成熟度 (落書き → 仮説 → 予想 → 定理)** と **射程 (近/中/遠)** でタグ付けする。

### 種① — 35 = 20 + 15 の内部構造は inflation の反復深さ

**成熟度**: 落書き
**射程**: 中
**SOURCE で立っている部分**: Mathsuke 記述 (黄金 20: 大5+中10+小5, 鈍角 15: 大10+小5)、`triangle_category_functor_map.md` §3 M3 の inflation rule `S↦L, L↦LS` + Fibonacci 再帰

**仮説**: 35 という総数は、正五角形の再帰深さを categorical 化した **Fibonacci 二項束 (Fibonacci binomial lattice)** の濃度。サイズ別 5-10-5 / 10-5 の階段は、inflation を 2 ステップ展開したときの `L` と `S` の子孫数の二項係数に対応する可能性。

**未踏**:
- 35 個の explicit な bijection を Fibonacci 束の元と取ること
- 大/中/小の三段階が inflation の反復深さ 1/2/3 に対応するかの検証

**次の一手**: pentagram の全 35 三角形を座標で enumerate し、各三角形を `(L, S)` 語に tag 付けできるかを試す。

---

### 種② — φ = Fibonacci anyon の quantum dimension

**成熟度**: SOURCE + 仮説 → **縮小修正 (Face5Lemma §5.3 検証後)**
**射程**: 近
**SOURCE**: Moore-Seiberg (1989), Ocneanu, Kitaev "anyons in exactly solved models" — 標準 MTC 文献。Fibonacci anyon category (SU(2)_3) は `τ⊗τ = 1⊕τ` で `d(τ)² = 1 + d(τ)` → `d(τ) = φ`。

**🔄 修正 (2026-04-17)**: Face5Lemma_draft §5.2-§5.3 の検証により、φ は **特権的定数ではない**。Ising anyon (SU(2)_2) では `d_σ = √2`、SU(2)_4 では `d = √3` が同位置にある。φ は SU(2)_k series の **k=3 の 1 点** にすぎない。

**修正された σ 論文との関係**:

| MTC 家族 | k | 固有値 | 固有方程式 |
|:---|:---|:---|:---|
| 可換 | 1 | 1 | trivial |
| Ising | 2 | √2 | `d² = 2` |
| **Fibonacci** | **3** | **φ** | `d²-d-1=0` |
| SU(2)_4 | 4 | √3 | `d² = 3` |
| SU(2)_k 一般 | k | 2cos(π/(k+2)) | Chebyshev |

**仮説 (縮小版)**: σ が Mac Lane 5-cell で閉じる固有条件は SU(2)_k series 全体。Fibonacci は「σ の k=3 実現」として 1 例に位置付ける。

**未踏**:
- SU(2)_k 以外の MTC 族 (quantum groups at other roots, near-group, Tambara-Yamagami, etc.) での Face5 固有値検証
- k→∞ 古典極限で σ closure schema に何が起きるか

**次の一手**: σ 論文 v0.3 §5.bis を「φ-sector」から「スペクトル軸 endpoint identity (SU(2)_k family)」へ再定位 (種⑥ 三軸分離と合流)。

---

### 種③ — Mac Lane pentagon と F-matrix は σ の 5-cell 実現

**成熟度**: 仮説 + SOURCE 部分あり → **試作 v0.3 完了 (F5-α 定理昇格, Kalon△ ◎)**
**射程**: 近〜中
**SOURCE**: Mac Lane coherence theorem (1963), Ocneanu pentagon equation, Kitaev anyon theory, 量子群標準公式、**Stasheff (1963) associahedra 理論**。
**試作**: `./Face5Lemma_draft.md` (v0.3, 2026-04-17):
- v0.1: 初回試作、F5-α/β/γ/δ 分離
- v0.2: §5.2 Ising 検証で F5-γ 反証、§5.3 SU(2)_k 計算検証で F5-γ' (family 版) 確立
- **v0.3: §11 Stasheff 理論で F5-α minimality 証明、Kalon△ ◎ 判定、定理 face 昇格**

**Face Lemma の延長構想 (v0.3 で確立)**:
- `Face3`: 第 3 射 = comparison surface (σ) の最小条件 [既存]
- `Face5`: 第 5 射 = pentagon coherence (α_pent) の最小条件 [**定理 v0.3**]
- `Face(2n+1)`: n-cell comparison の最小条件 [n=1,2 は `dim K_n = n-2` で正当化、n≥3 は落書き]

**主要 findings (v0.3)**:
- ✓ **F5-α (5 射 minimality): 定理 — Stasheff の `K_4 = pentagon` が最小 2-dim associahedron であることから**
- ✓ F5-β (α 非自明性要請 ⇔ k≥2): 生存 + 具体化
- ✗ F5-γ (φ universal): **反証** — Ising (√2)、SU(2)_4 (√3) と並ぶ family の 1 点にすぎない
- ✓ F5-γ' (SU(2)_k family, `d_{1/2}(k)=2cos(π/(k+2))`): 確立
- ✓ **F5-δ (階層公式) の n=1, 2 が `dim K_n = n-2` から正当化**

**未踏 (v0.3 後)**:
- F5-β の代数的特徴付け (strict monoidal 排除条件)
- SU(2)_k 以外の MTC 族での Face5 固有値検証 (quantum groups at other roots, near-group, TY)
- F5-δ の `n ≥ 3` 具体化 (hexagon axiom ↔ `K_5` 3-polytope 面)
- `k→∞` 古典極限での σ closure schema の振る舞い

**次の一手**: σ 論文 v0.3 §5.bis を「スペクトル軸 endpoint identity (SU(2)_k family)」として再定位し、骨格に associahedra `{K_n}` 階層を引用。φ 特権化撤回。種⑥ (三軸分離) と合流。

---

### 種④ — 黄金忘却率 1/φ は最小コスト忘却レート

**成熟度**: 落書き (但し忘却論との接続面は強い)
**射程**: 中
**SOURCE**: inflation rule `S↦L, L↦LS` の逆操作としての「step を削ぐ」。

**仮説**: `E_b` (忘却濾過) が inflation の逆と読めれば、1 ステップの忘却率は:
- `LS → L` で失う比率 = S の長さ / 全長 = **1/φ²** ≈ 0.382
- `L → S` で失う比率 = 1 - 1/φ = **1/φ** ≈ 0.618

**1/φ = 自己相似性を保つ最小忘却率**。これより速いと構造崩壊、遅いと冗長。

**2 つの忘却モードの対比**:
- π-sector: 完全忘却 (`D_C(E(π)) = 0_A`) = **終点** の忘却
- φ-sector: 部分忘却 (段階的 inflation 逆) = **過程** の忘却

**論文 XII (速度は忘却) との接続候補**: χ(τ) = φ と読めば、論文 XII の `χ > 1 は構造的に可能` は「Fibonacci anyon 系は χ = φ で動く」と categorify できる可能性。

**未踏**:
- FEP の prior 縮退率が 1/φ に収斂するかの実証計算
- E_b の作用と inflation の逆作用の形式的同一視

**次の一手**: 論文 XII v0.9 の χ 計算を Fibonacci anyon の χ で置き換えてみる思考実験。

---

### 種⑤ — 正20面体 / A_5 / E_8 への射程拡張

**成熟度**: 落書き → 仮説 + 遠仮説 (sketch 化) → **混合状態 (Face7 検証で A_5 requirement 落下、φ 指標連絡は生存)**
**射程**: 遠
**試作**: `./A5_E8_sigma_sketch.md` (v0.1, 2026-04-17) + `./Face7Lemma_draft.md` (v0.1, 2026-04-17, 種⑤ A_5 仮説の検証)

**SOURCE (生存部分)**: 正12面体の回転群 = A_5 (icosahedral, 60 元)、binary icosahedral 2I の McKay 対応 `2I ↔ Ẽ_8` (McKay 1980)、A_5 の 2 つの 3 次元既約表現の 5-cycle 指標値 `(1±√5)/2` [Isaacs character table 標準]。

**主要 findings (v0.1 sketch + Face7 検証 2026-04-17)**:
- ✓ **A_5 指標表に φ が埋め込み**: MTC / Fibonacci anyon とは独立に、群表現論そのものから φ が出る (保存)
- ✓ **射程 2 段階化**: 近い作業面と遠い保存面の分離 (保存)
- ✗ **対称群階梯の仮説反証**: 「σ の三軸分離を要求する最小場 = A_5」は Face7 検証で落ちた。K_5 associahedron の自動同型群は D_2 程度で A_5 を持たない (Face7Lemma_draft §12)
- ✓ **A_5 の意義再配置**: σ の自動同型候補ではなく、φ が数値として現れる独立領域として保存。本質 (A_5 に φ) は不変

**未踏 (v0.1 + Face7 後)**:
- A_5 不変 fusion category (or A_∞-圏) の具体例探索
- E_8 の 240 roots と σ の忘却濾過 `E_b` の具体的 bijection 候補 (射程案 1、保留)
- SU(2)_3 MTC と A_5 character theory の表現論的同型性
- Fibonacci ↔ E_8 の coset 接続の SOURCE 再確認 (Kitaev 2006, Nayak et al. 2008)

**次の一手**: v0.2 更新で A_5 requirement 反証の明示記載。σ 論文本体 v0.3 の優先は保留のまま。

---

### 種⑥ — 「対称群 × スペクトル × 位相」の三軸分離

**成熟度**: 主観 + 整理仮説
**射程**: 近
**SOURCE**: σ 論文 v0.2 の現状 + triangle_map §3 の 4 機械。

**現状の問題意識**: σ 論文 v0.2 は「σ の実現面」として群と固有値と端点を混ぜて扱っている。これを明示的に分離すべき。

**三軸**:

| 軸 | 問いの形 | Δ² 実現 | 正五角形実現 |
|:---|:---|:---|:---|
| 群の軸 | σ はどの区別を忘れて閉じるか? | S_3 | D_5 |
| スペクトル軸 | σ はどの比率で再帰するか? | Q-matrix 固有値 | **φ** |
| 位相軸 | σ はどの周期で反転するか? | e^{iπ}+1=0 | F-matrix pentagon eq |

**仮説**: この三軸を σ 論文 v0.3 で明示的に分離すれば、π-sector と φ-sector が自然に並ぶ。現行 §2-§5 の記述を三軸に再配置するだけで射程が保てる。

**未踏**:
- 三軸の random independence の確認 (それとも相互還元可能か?)
- 3 軸が揃う時のみ σ が Fix(G∘F) に近づくという予想の精緻化

**次の一手**: σ 論文 v0.3 起草時に、本章を §2.0 導入章として置く実験。

---

### 種⑦ — 正五角形の美学的優越の情報幾何学的根拠

**成熟度**: 思弁 → **思弁 + 仮説 + VFE sketch (sketch 化済 2026-04-17)**
**射程**: 遠
**試作**: `./kalon_vfe_pentagon_sketch.md` (v0.1, 2026-04-17)
- SOURCE 部分: phyllotaxis 黄金角 137.5° (Adler 1974)、ペンローズタイル、Kalon = Fix(G∘F) 定義
- 仮説部分: 正 n-gon の VFE が n=5 で stationary (ad hoc 候補式)
- 新観察: 正八角形の銀比 (silver ratio 1+√2) が Kalon 候補として並走する可能性
- 反対仮説 (Livio 2002 懐疑論) も open リストに保持 → μ-retreat 回避

**SOURCE 強度階層 (美学的遍在性)**:
- 強 SOURCE: phyllotaxis 黄金角、ペンローズタイル、松ぼっくり/ひまわり Fibonacci
- 中 SOURCE: DNA 主溝/副溝比 (論争あり)
- 弱 SOURCE: 黄金長方形美学 (Fechner 1876 以来、再現性疑問)

**主要 findings (v0.1 sketch)**:
- ✓ Kalon 公理書 §6 3 ステップを正五角形に適用 → **Kalon△ ◎ sketch 判定** (F の非自明派生 5 種: pentagram 35 三角形 / Fibonacci 数列 / A_5 指標 / Fibonacci anyon / ペンローズ)
- ✓ 正 n-gon を "観測モデル" として VFE 候補式 `F(n) ≈ -log(2n) + H_spec(n)` を提示
- ✓ metallic ratio family (φ, 銀比 δ, ...) が複数の Kalon stationary を生む可能性
- ✓ Kalon▽ 偽装回避: "MB 範囲の普遍性" と "全空間普遍" を峻別

**未踏 (v0.1 後)**:
- 正 n-gon の VFE を formal FEP で計算 (ad hoc 候補式の再定式化)
- 銀比 (正八角形) と φ の Kalon 同位性の検証
- Kalon 公理書への "Fix(G∘F) の具体例" 節の追加提案
- Douady-Couder (1992) 物理的生成機構を VFE 最適化として再定式化

**次の一手**: Kalon 論文 (`kalon.typos`) 側で正式 Kalon 判定を走らせる検討。σ 論文本体との独立性は保つ。急がない。

---

### 種⑧ — 黄金 KAM torus: π-sector と φ-sector の役割分担

**成熟度**: SOURCE + 仮説
**射程**: 中
**SOURCE**: Kolmogorov-Arnold-Moser 定理 (Kolmogorov 1954, Arnold 1963, Moser 1962), Herman, Yoccoz。Hamilton 系の不変 torus が摂動に耐える条件 = 周波数が Diophantine 無理数。φ = `[1; 1, 1, ...]` は最強 Diophantine → 黄金 torus は KAM で最後まで生き残る不変構造。

**仮説**: σ 論文 §5 の π-sector (`e^{iπ}+1=0`) と、種③ Face5Lemma の φ-sector (F-matrix pentagon eq) の役割分担を KAM 類比で読み直す:

- **π-sector**: σ が半周期で完全反転する **端点現象** (endpoint identity, 離散)
- **φ-sector**: σ が摂動下で生き残る **内部安定条件** (interior stability via Diophantine, 連続)

**v0.3 Face7 所見との統合**: Face7Lemma_draft v0.1 の F7-ε (σ closure schema の深度はドメインごとに異なる) に対し、KAM は **連続ドメイン (Hamilton 力学系)** での σ 安定条件の 1 インスタンス候補。MTC (離散ドメイン) の Face5 自動帰結と対になる。

**未踏**:
- σ 閉路の KAM 安定条件の形式化
- π-sector (discrete endpoint) と φ-sector (continuous interior) を σ 論文 §5 で並列記述できるか
- 種⑨ 連分数との直接接続: KAM の Diophantine 条件は連分数展開で測定される
- F7-ε を「連続ドメイン / 離散ドメイン」の 2 分類として精緻化する経路

**次の一手**: σ 論文 v0.3 §5 に註として「φ-sector は endpoint ではなく interior stability として読める」の仮説を保存。種⑨ と合流して独立 sketch 化の検討。F7-ε 精緻化とも連動。

---

### 種⑨ — 連分数 `[1; 1, 1, ...]` = 最も忘却に強い数 ★ HGK 横断柱候補

**成熟度**: SOURCE + 仮説 (HGK 体系横断の跳躍力)
**射程**: 近〜中
**SOURCE**: Khinchin (1935) 連分数定理, Lagrange spectrum 下端 = `1/√5` に対応するのが φ = `[1; 1, 1, ...]` [Cassels "Introduction to Diophantine Approximation"]。最も有理近似されにくい無理数。

**仮説**: 「有理で近似される」= 「単純な分母/分子で置き換えられる」= **情報圧縮可能**。φ は最も圧縮しにくい → **「最も忘却に抵抗する数」**。

| 対称 | 比率 | 連分数 | 忘却抵抗 |
|:---|:---|:---|:---|
| 正三角形 | 1 | trivial | 即 0 |
| 正方形 | √2 | `[1; 2, 2, 2, ...]` 固定周期 | 周期的崩壊 |
| **正五角形** | **φ** | **`[1; 1, 1, ...]` 最も無理** | **最強抵抗** |
| 正六角形 | √3 | `[1; 1, 2, 1, 2, ...]` 二重周期 | 二重崩壊 |
| 正八角形 | 銀比 `1+√2` | `[2; 2, 2, 2, ...]` 固定周期 | 周期的崩壊 |

**HGK 横断の跳躍力**: Kalon 論 (`Fix(G∘F)`) と忘却論 (`E_b` 濾過) を **同じ連分数の言語** で書ける可能性。φ-Kalon = 「自己参照の最深層で `[1; 1, 1, ...]` を書く時に出る定数」として解釈可能。

**v0.3 Face7 所見との統合**: F7-ε (σ closure schema の深度はドメインごとに異なる) に対し、**連分数展開はドメイン横断の数論的指標**。連続・離散のドメイン別で σ が求める閉じ方が異なっても、**φ が共通定数として現れるなら、それは「連分数 `[1; 1, 1, ...]` の普遍性」が理由**。F7-ε のドメイン依存性と連分数の数論的普遍性は、補完しうる 2 軸。

**種⑧ KAM との接続**: KAM の Diophantine 条件は連分数展開の部分商の大きさで測定される。φ が「最も無理」であることと、黄金 torus が「最後まで生き残る」ことは **同一現象の二つの顔**。

**kalon_vfe_pentagon_sketch.md §3 との接続**: 既に `x² - x - 1 = 0` の自己参照方程式 `φ = 1 + 1/φ` が stationary の構造的根拠として提示済み。連分数 `[1; 1, 1, ...]` は同じ自己参照の別表現。

**銀比との整合 (kalon_vfe §2 発見を受けて)**: 銀比 (正八角形 `1+√2 = [2; 2, 2, 2, ...]`) は Kalon 候補として並走する。連分数の「無理度」で見ると銀比は φ より 1 段階弱い (部分商 2 は 1 より大きい → 有理近似されやすい)。これは metallic ratio family 内での **Kalon 強度の階層化** の可能性を示唆。`φ > 銀比 > 銅比 > ...` の順序は [SU(2)_k の `d = 2cos(π/(k+2))` 数列] ではなく [連分数の無理度順] が自然単位。

**未踏**:
- `Fix(G∘F)` の連分数表現の形式化
- 忘却濾過 `E_b` と rational approximation の同型候補
- metallic ratio family の連分数 `[n; n, n, ...]` と Kalon 強度の順序 (φ > 銀比 > 銅比 > ...) の検証
- SU(2)_k family `2cos(π/(k+2))` と連分数展開の系統的対応
- F7-ε ドメイン依存性が消える「数論的限界」(連分数の無理度が揃う場)

**次の一手**: 別 sketch `kalon_continued_fraction_bridge.md` (仮称) の起草検討。ただし種⑧ KAM と合流可能なため、先に両者が近い作業面に留まるかを kalon_vfe §5 Open と F7-ε 精緻化と照合してから判断。v0.4 段階では保存のみ。

---

## §3 種の関係図

```
                種⑥ (三軸分離)
                   │
        ┌──────────┼──────────┐
        │          │          │
     群の軸    スペクトル軸   位相軸
        │          │          │
     種①⑤     種②③④       π-sector
    (inflation, (quantum dim, (σ 論文 §5)
     icosahedral)  forgetting rate,
                   pentagon coh)
                   │
                種⑦ (美学的根拠)
```

近い種 (②③⑥) は σ 論文 v0.3 の直接補強材。
中の種 (①④) は σ 論文と triangle_map の両方を拡張する架橋。
遠い種 (⑤⑦) は将来の独立論文候補。

---

## §4 優先順位と次の一手 (2026-04-17 更新 — 第 4 ラウンド後、種⑤⑦ sketch 化)

1. ✓ **[完了 Face5 v0.1]** `Face5Lemma_draft.md` 試作 (種③ 生存確認、F5-α/β/γ/δ 分離)
2. ✓ **[完了 Face5 v0.2]** Ising / SU(2)_k 検証 (F5-γ 反証、F5-γ' 確立、種② 縮小、種⑥ 昇格)
3. ✓ **[完了 Face5 v0.3]** F5-α minimality を Stasheff associahedra 理論で定理化 (Kalon△ ◎)
4. ✓ **[完了 2026-04-17]** `A5_E8_sigma_sketch.md` v0.1 試作 (種⑤ 2 段階化、A_5 指標表の φ 発現確認、射程案 2 を近い作業面に仕分け)
5. ✓ **[完了 2026-04-17]** `kalon_vfe_pentagon_sketch.md` v0.1 試作 (種⑦ VFE 候補式、Kalon△ ◎ sketch 判定、metallic ratio family 観察)
6. **[最優先]** σ 論文 v0.3 の `§2.0 三軸分離` 導入 (種⑥)。π (位相) と d_{1/2}(k) (スペクトル) の混同を構造的に封じる
7. **[直近]** σ 論文 v0.3 の `§5.bis スペクトル軸 endpoint identity` 追加 (種③、SU(2)_k family)、骨格に associahedra `{K_n}` 階層を引用
8. **[中期]** F5-β の代数的特徴付け (strict monoidal 排除条件)
9. **[中期]** SU(2)_k 以外の MTC 族での Face5 検証 (quantum groups at q=e^{2πi/p}, near-group, Tambara-Yamagami)
10. **[中期]** F5-δ の `n ≥ 3` 具体化 (hexagon axiom ↔ `K_5` 3-polytope 面)
11. **[中期]** 論文 XII の χ を SU(2)_k family で置き換える思考実験 (種④)
12. **[中期]** pentagram 35 三角形の explicit enumeration (種①)
13. ✓ **[完了 2026-04-17]** `Face7Lemma_draft.md` v0.1 試作 — A_5 requirement 検証 → 反証 (K_5 自動同型群は D_2 止まり、A_5 を持たない)。F7-α minimality は Stasheff `dim K_5=3` から正当化、◎ Kalon△ 候補。Face7 の新発見: **MTC では Face5 から自動、A_∞-圏族でのみ独立内容**。σ closure schema の深度はドメインごとに異なる (F7-ε)
14. **[中期]** 正 n-gon の VFE 数値検証 — n=5 の stationary 性 + 銀比の Kalon 同位性 (kalon_vfe_pentagon §5 Open 2-4)
15. **[遠期]** `k→∞` 古典極限での σ closure schema
16. **[遠期]** E_8 射程案 1 (σ = E_8 型最小 holonomy) の SOURCE 拡充 (A5_E8_sigma §5 案 1)
17. **[遠期]** Kalon 公理書に「Fix(G∘F) の具体例としての正 n-gon」節の追加提案 (kalon_vfe_pentagon §5 Open 6)
18. **[中期]** 種⑧ KAM 黄金 torus による π-sector (端点) と φ-sector (内部安定) の役割分担を σ 論文 §5 註に追加。F7-ε (ドメイン依存深度) の連続ドメイン 1 インスタンス候補
19. **[中期]** 種⑨ 連分数 `[1; 1, 1, ...]` の `Fix(G∘F)` 連分数表現形式化 — Kalon × 忘却論ブリッジ稿化の是非判断。F7-ε を横断する数論的指標候補 (種⑧ と合流可否含む)

---

## §5 SOURCE / TAINT 台帳

- [SOURCE] `triangle_category_functor_map.md` §1 walking triangle Δ²、§3 M3 Fibonacci inflation
- [SOURCE] 比較射σ論文 v0.1 全体 (特に §3 4言語仮説、§5 typed corollary)
- [SOURCE] Moore-Seiberg (1989), Ocneanu, Kitaev — Fibonacci anyon / MTC 標準文献
- [SOURCE] Mathsuke.jp pentagon-goldenratio — 35 個の分類は外部記事、ただし記述の代表性は要検証
- [TAINT] 本文書の 7 落書きすべて (σ 論文 §M2 に未昇格)
- [TAINT] 「黄金忘却率 1/φ が FEP prior 縮退率に収斂する」は未検証の思弁

**v0.4 追加 SOURCE/TAINT (種⑧⑨)**:
- [SOURCE] Kolmogorov (1954), Arnold (1963), Moser (1962) — KAM 定理
- [SOURCE] Khinchin (1935) 連分数定理 / Cassels "Introduction to Diophantine Approximation"
- [SOURCE] Lagrange spectrum 下端 = `1/√5` と φ = `[1; 1, 1, ...]` の対応
- [TAINT] σ 閉路の KAM 安定条件の形式化 (種⑧)
- [TAINT] Kalon 不動点 `Fix(G∘F)` の連分数表現 (種⑨)
- [TAINT] 連分数 `[1; 1, 1, ...]` ↔ 忘却論 `E_b` 濾過の形式的同型 (種⑨)
- [TAINT] F7-ε (ドメイン依存深度) の連続・離散二分と KAM / MTC の対応 (種⑧⑨合流仮説)

---

*v0.4 — 2026-04-17 種⑧ (黄金 KAM torus) と種⑨ (連分数 `[1; 1, 1, ...]`) を追加。Tolmetes ↔ Claude 第 2 ラウンド落書きから既存 sketch 未カバーの 2 種を保存。v0.3 F7-ε (ドメイン依存深度) に対する 2 つの補完仮説 — 種⑧ = 連続ドメインでの σ 安定条件、種⑨ = ドメイン横断の数論的指標 (φ 普遍性の理由候補)。銀比との整合で metallic ratio Kalon 強度順序を連分数無理度で定義する提案を含む。*
*v0.3 — 2026-04-17 `Face7Lemma_draft.md` v0.1 試作完了。種⑤ A_5 requirement 反証 (K_5 自動同型群は D_2 止まり)。Face7 は MTC で自動帰結、A_∞-圏族に限定された狭射程であることを発見。σ closure schema の深度がドメインごとに異なる (F7-ε) という新仮説を提起。種⑤ の「A_5 に φ」連絡は生存、「A_5 対称性を σ が要求」は反証。*
*v0.2 — 2026-04-17 種⑤ (`A5_E8_sigma_sketch.md`) と種⑦ (`kalon_vfe_pentagon_sketch.md`) を sketch 化。Face5Lemma_draft と並走する構造。近い作業面と遠い保存面を明示分離し、μ-retreat 回避条件を sketch 側に明記。*
*v0.1 — 2026-04-17 Tolmetes の正五角形観察から 7 落書きを種として保存。σ 論文本体への組込み優先度は §4 参照。*
