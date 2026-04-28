# Codex 委託 brief: Predictions_Descend Round 7 — G-η 完全形式化

## 目的

論文 `Predictions_Descend_理解関手の普遍的限界.md` v0.8 §3.6.1 で骨格固定された **5 分野横断 5C2 = 10 ペアの natural transformation $\eta_{i,j}$** を、commutative diagram + naturality verification + Yoneda coherence の三段階で **完全形式化** する。Round 6 (Claude 単独) で達成した「第 1 階の骨格」を「第 2 階以降の categorical 証明」に押し上げ、各ペアの type (a)/(b)/(c) を SOURCE 裏付け付きで確定する。

## 背景

### 本論文の位置づけ

`Predictions_Descend_理解関手の普遍的限界.md` (本体 v0.8 / メタデータ v1.8 / 946 行 + Round 6 追記) は忘却論シリーズの **番外編 standalone**。投稿先は **Ergo (哲学本命) または Compositionality (圏論本命候補)** で並列検討中。Round 7 完了が公開条件。

核主張 C1 (主要関心): 「**理解関手 $L \dashv R$ は構造保存軸では同型に接近しうるが、値非保存軸では同型不到達**。理解と予測は随伴対であり、5 分野 (情報幾何 IG / ゲージ理論 Gauge / 統計力学 Stat / 数論 Num / FEP) でこの随伴構造が共通して現れる」(構成的命題 70%)。

§3.6.1 は C1 の最大の支柱である「**5 分野同型は単なる類比ではなく、natural transformation で結ばれる関手的同型である**」を担う。

### Round 6 (2026-04-26) で達成した骨格

10 ペア全てに対し以下の **第 1 階の骨格** が固定済み:

1. **共通 base 圏 $\mathcal{C}$** の暫定提示
2. **対応 $\eta_{i,j}$** の核となる射の言語化
3. **対応の type 暫定判定** ((a) natural isomorphism / (b) natural transformation / (c) lax/partial correspondence)
4. **不変量の対応** ($|\text{Ker}(\eta_{\text{unit},i})|$ の関係)

達成度 honest 較正 (Codex Bridge レビュー反映済):

| Pair | 対応 | 達成水準 | Type (暫定) | SOURCE 強度 |
|:---|:---|:---|:---|:---|
| 1 IG × Gauge | Fisher 計量 ↔ Yang-Mills 曲率 | 構造的類似 [仮説 60%] | (c) lax/partial | 中候補 |
| 2 IG × Stat | Legendre 双対 (Hessian 同型) | Round 4 骨格 + 標準帰結 | (a) natural iso 候補 | 強候補 |
| 3 IG × Num | 対数微分 ↔ successor 階層 | 構造的類似 [仮説 60%] | (c) lax 候補 | 弱 |
| 4 IG × FEP | Fisher = VFE Hessian | 標準帰結 + Mayama 補強 | (a) natural iso 候補 | 強候補 |
| 5 Gauge × Stat | Wick 回転 (path integral) | 物理学標準帰結 | (b) natural transformation 候補 | 中候補 |
| 6 Gauge × Num | ホロノミー ↔ winding number | 構造的類似 [仮説 55%]、abelian 限定 | (c) lax/partial | 弱 |
| 7 Gauge × FEP | 接続 ↔ belief update flow | 中候補 (active inference) | (b) natural transformation 候補 | 中候補 |
| 8 Stat × Num | 分配関数漸近 ↔ Peano 指数 | 構造的類似 (asymp enum) | (c) lax/partial | 弱 |
| 9 Stat × FEP | VFE 減少定理 (同形) | 強 (HGK 内部 + Mayama) | (a) natural iso 候補 | 強 |
| 10 Num × FEP | successor depth ↔ 階層誤差 | 構造的類似 [仮説 55%] | (c) lax/partial | 弱 |

### Codex Bridge レビュー (2026-04-26) で指摘済の Risk

- **Risk 1 (commutativity 表現)**: 「non-iso component で commutativity が破れる natural transformation」は誤り。Natural transformation $\eta: F \Rightarrow G$ は **全 component で naturality square が commute する**。component が iso でないなら natural isomorphism ではないが natural transformation 自体は成立。「commutativity が破れる」は別概念 (lax/partial correspondence) を指す。Round 7 では type (a)/(b)/(c) を **SOURCE 付きで確定** すること
- **Risk 2 (Pair 1 同型主張過剰)**: Fisher 計量 (symmetric 2-tensor) と Yang-Mills 曲率 (antisymmetric 2-form) は symmetric/antisymmetric の差が本質的、構造同型ではない。Round 7 では **どこまでが類似でどこからが同型か** を Yoneda coherence 経由で精密に切り分けること
- **N-01/N-05 警告**: §3.6 / §M5.4 / §M6 既存記述との grep/search 整合確認は Round 6 で省略された。Round 7 で **既存反論との整合監査** を含めること

## やってほしいこと

各ペアについて、以下の **6W3H 形式** で commutative diagram + naturality verification + Yoneda coherence を完成させる。

### 6W3H 仕様 (各ペア共通)

| 項目 | 内容 |
|:---|:---|
| **What** | natural transformation $\eta_{i,j}: F_i \Rightarrow F_j$ の commutative diagram (全 component の naturality square を明示) |
| **Why** | type (a)/(b)/(c) のどれに該当するかを **証明または反例** で確定。Round 6 暫定判定の修正があれば honest に書く |
| **Who** | 一次 SOURCE 文献 (Amari 1985 / Cencov 1972 / Friston 2010 / Polyakov 1987 / Mac Lane CWM / Riehl Category Theory in Context 等) と該当箇所 (定理番号 / ページ / 式番号) を必ず明示 |
| **Where** | 共通 base 圏 $\mathcal{C}$ の正確な定義 (presheaf 圏 $\text{Set}^{\mathcal{D}^{\text{op}}}$ への Yoneda 埋め込みを含む) |
| **When** | naturality square が commute する条件と、commute しない反例 (type (b)/(c) の場合) |
| **Whom** | iso component と non-iso component の分類 (構造保存軸 / 値非保存軸) |
| **How** | Yoneda 埋め込み $y: \mathcal{C} \to \text{Set}^{\mathcal{C}^{\text{op}}}$ を経由した coherence theorem の適用 (Mac Lane CWM III.2 + Riehl §2.2 Theorem 2.2.4) |
| **How much** | 達成水準を [強候補 / 中候補 / 構造的類似 仮説 X%] で再較正 (Round 6 暫定値からの上下を明示) |
| **How long** | 完全形式化までの残ギャップ (Round 8 以降の課題) |

### Pair 単位の達成基準

各ペアにつき以下を満たすこと:

1. **Commutative diagram の描画**: 標準的な category theory diagram 記法 (TikZ-cd 風 ASCII art または LaTeX で markdown 内に埋め込み可な形式)。component, naturality square, base 圏の関手矢印を全て明示
2. **Naturality verification**: 各 component $\eta_{i,j,c}: F_i(c) \to F_j(c)$ が任意の morphism $f: c \to c'$ で $F_j(f) \circ \eta_{i,j,c} = \eta_{i,j,c'} \circ F_i(f)$ を満たすことを **計算または定理参照** で証明。type (b) なら全 component で commute (一般 morphism)、type (c) なら commute しない反例を 1 つ以上提示
3. **Yoneda coherence の適用**: 各 $F_i$ が representable functor $\text{Hom}(-, X_i)$ への自然変換に分解できるかを Yoneda 補題 (Mac Lane III.2 / Riehl §2.2.4) で確認。分解できれば natural isomorphism の候補、できなければ lax/partial に確定
4. **Type 確定**: 上記 1-3 の結果から (a)/(b)/(c) のいずれかに **SOURCE 付きで** 確定。Round 6 暫定判定との差を明示
5. **§3.6 / §M5.4 / §M6 整合監査**: 該当ペアに関する既存記述を grep/search で抽出し、Round 7 結論との **記号衝突 / 命題不整合 / 用語不一致** がないかをチェック。問題があれば §M5 (Gauntlet ログ) または §M6 (虚→実変換面) への追記事項として報告

### 優先順位

10 ペアを以下の優先度で処理する (Round 6 SOURCE 強度に比例):

- **P0 (強候補)**: Pair 2 (IG × Stat) / Pair 4 (IG × FEP) / Pair 9 (Stat × FEP)
  - これらが type (a) natural isomorphism として確定すれば C1 主張水準は 70% → 75%+ に昇格しうる
- **P1 (中候補)**: Pair 5 (Gauge × Stat) / Pair 7 (Gauge × FEP) / Pair 1 (IG × Gauge, Risk 2 反映済)
  - これらが type (b) natural transformation として確定すれば C1 主張水準は据え置きで 70% を **honest に正当化**
- **P2 (弱、構造的類似仮説 55-60%)**: Pair 3 (IG × Num) / Pair 6 (Gauge × Num) / Pair 8 (Stat × Num) / Pair 10 (Num × FEP)
  - これらは type (c) lax/partial に確定する公算が高い。確定できれば「3 分野同型 (IG/Stat/FEP) + 数論は構造的類似」として C1 を honest に縮小再構成

### 想定される出力ボリューム

10 ペア × (各 6W3H + commutative diagram + naturality verification + Yoneda coherence + 整合監査) で、見積り **5,000-10,000 行規模**。Claude 単独では実行不可能なので Codex executor 委譲。1 ペアあたり数日、全体で 1-2 週間規模。

## 参照すべき一次 SOURCE

### 圏論基礎

- Mac Lane, S. (1998) "Categories for the Working Mathematician" 2nd ed., Springer GTM 5
  - III.2 Yoneda lemma
  - V.6 General Adjoint Functor Theorem (GAFT)
  - V.8 Special Adjoint Functor Theorem (SAFT)
- Riehl, E. (2017) "Category Theory in Context", Dover
  - §2.2 Theorem 2.2.4 (Yoneda)
  - §3.5 Theorem 3.5.5 (limits and colimits)

### 情報幾何

- Amari, S. (1985) "Differential-Geometrical Methods in Statistics", Springer LNS 28
- Amari, S. (2016) "Information Geometry and Its Applications", Springer
- Cencov, N. N. (1982) "Statistical Decision Rules and Optimal Inference", AMS Translations

### ゲージ理論

- Polyakov, A. M. (1987) "Gauge Fields and Strings", Harwood
- Itzykson, C. & Drouffe, J.-M. (1989) "Statistical Field Theory", Cambridge

### 統計力学

- Goldenfeld, N. (1992) "Lectures on Phase Transitions and the Renormalization Group", Addison-Wesley

### FEP

- Friston, K. (2010) "The free-energy principle: a unified brain theory?" Nature Reviews Neuroscience 11, 127-138
- Mayama, K. et al. (2025) "Empirical bridge between IIT and FEP" arxiv 2510.04084 (本体 §6.1 で完全 PDF 統合済)

### 既存内部 SOURCE

- 本体 §3.6 (5 分野同型表)
- 本体 §3.6.1 (Round 6 10 ペア骨格)
- 本体 §M5.4 (Round 4 で IG × Stat / IG × Gauge の 2 ペア骨格)
- 本体 §M6 (虚→実変換面、現在まだ虚な点)
- 論文 III §曲率テンソル定義 (Pair 1 で参照)
- aletheia §1 L99-L107 (Pair 9 で参照)

## 出力形式

**ファイル**: `plans/codex_report_pd_g_eta_round7.md` (本 brief と同じディレクトリに書き出す)

**構造**:

```markdown
# Codex 報告: Predictions_Descend Round 7 — G-η 完全形式化

## §0 サマリー

- 処理ペア数: 10/10 (または部分達成なら何ペアまで)
- Type 確定: (a) X ペア / (b) Y ペア / (c) Z ペア
- C1 主張水準への影響: [上昇 / 据え置き / 下降] — Round 6 70% → Round 7 X%
- 既存記述との不整合検出: N 件 (詳細は §11)

## §1 Pair 1: IG × Gauge — [type 確定]

### 1.1 6W3H
- What: ...
- Why: ...
- (略)

### 1.2 Commutative diagram

[ASCII art or LaTeX cd diagram]

### 1.3 Naturality verification

[計算または定理参照]

### 1.4 Yoneda coherence の適用

[Mac Lane III.2 / Riehl §2.2.4 への参照]

### 1.5 Type 確定 + SOURCE

- Type: (c) lax/partial
- SOURCE: Amari (1985) §X.Y / Polyakov (1987) §A.B / ...
- Round 6 暫定 [仮説 60%] からの差: 据え置き / 上昇 / 下降

### 1.6 残ギャップ (Round 8 以降)

...

## §2-§10 Pair 2-10

(同形式)

## §11 §3.6 / §M5.4 / §M6 整合監査

- 検出した記号衝突: ...
- 検出した命題不整合: ...
- 推奨される本体修正案: ...

## §12 C1 主張水準への影響

- Round 6 構成的命題 70% の根拠: ...
- Round 7 後の再較正: ...
- Ergo / Compositionality 投稿時の防衛可能性評価: ...
```

## 制約

- **時間**: ハードリミットなし。質を優先。1 ペア数日 × 10 ペアで 1-2 週間規模を想定
- **言語**: 出力は **日本語**。数式 LaTeX、commutative diagram は ASCII art または LaTeX cd 形式
- **SOURCE 厳格**: 各定理 / 命題 / 式は **必ず一次 SOURCE のページ / 定理番号 / 式番号** を明示。「Amari によれば」だけでは不可、「Amari (1985) §3.4 Theorem 3.4 (p. 67) によれば」レベルまで降りる
- **記憶禁止**: 訓練データの記憶からの引用を **禁止**。実際に PDF / 書籍 / arxiv を Read した SOURCE のみ使用
- **推測禁止**: 「こうだろう」「たぶん」を書かない。確信度ラベル `[確信] 90%+ / [推定] 60-90% / [仮説] <60%` を必ず付与
- **honest calibration**: Round 6 暫定判定からの上昇 / 据え置き / 下降を **隠さず** 報告。下降が出た場合は §12 で C1 主張水準への影響を計算
- **Risk 1/2 完全反映**: Codex Bridge 2026-04-26 レビューで指摘済の Risk 1 (commutativity 表現) と Risk 2 (Pair 1 同型過剰) を全 10 ペアで再点検し、不正確な表現が残らないこと
- **Yugaku Style Discipline 適用**: 本体への反映時は外部読者標準語のみ使用 (HGK 内部用語禁止、"〜的" 逃避禁止、メタ宣言禁止)。報告自体は内部用 meta なので緩和

## 報告先

このファイルと同じディレクトリの `codex_report_pd_g_eta_round7.md` に書き出す。

完了後、本体 `Predictions_Descend_理解関手の普遍的限界.md` §3.6.1 への反映 (置換または増補) と、メタデータ `Predictions_Descend_理解関手の普遍的限界_メタデータ.md` §M9 step 16 (Round 7) の状態更新は **Claude (Tolmetes 確認後)** が実施する。Codex は本体・メタデータを直接編集しない。

## 補足

### Round 6 → Round 7 の役割分担

- Round 6 (Claude 単独): 第 1 階の骨格 (核となる対応 + type 暫定 + 不変量) を 10 ペア全てに固定
- Round 7 (Codex 委譲, 本 brief): 第 2 階の categorical 証明 (commutative diagram + naturality + Yoneda coherence + type 確定 + 整合監査)
- Round 8 (TBD): 残ギャップ (連続-離散境界 / 非平衡 dual / non-abelian 拡張等) の処理。本 Round 7 の残ギャップ報告で次の優先順位が決まる

### 投稿戦略への接続

Round 7 完了で C1 主張水準が 70% を honest に正当化できれば:

- **Ergo (哲学)**: 5 分野同型の relational ontology 解釈で投稿可。double-blind 匿名化必要
- **Compositionality (圏論)**: 10 ペア natural transformation 完全形式化で投稿可。arXiv math.CT 先行 + endorsement 必要
- 並列の場合は arXiv preprint 先行 → Ergo 査読中に Compositionality 検討の二段戦略

### 本 brief 自体の honest disclosure

本 brief は Claude が起票した。Codex は本 brief の指示に従って Round 7 を実行し、報告書を作成する。Round 7 結果が Round 6 暫定判定を **大幅に下方修正** する可能性 (例: 強候補と思われた Pair 4 が実は type (c) lax だった等) がある。その場合は honest に下方修正を報告し、§12 で C1 主張水準への影響を計算すること。「期待通りの結果を出す」ことではなく「実際に何が成立し何が成立しないかを確定する」ことが本 brief の目的である [Yugaku §M6 「罪は何が虚かを伏せたまま実を装うこと」]。
