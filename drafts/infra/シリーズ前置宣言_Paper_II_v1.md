# シリーズ前置宣言 — 論文 II「相補性は忘却である」

**v1.0 (2026-04-11)**
**役割**: Paper II 本体を削減・公開する前に、シリーズ全体における Paper II の位置・役割・境界・布石を宣言する執筆者/査読者向けメタ文書。読者向けではない。
**対応本稿**: `drafts/series/論文II_相補性は忘却である_草稿.md` v1.11 → v1.12 (Phase 4 削減後)
**対応 meta**: `drafts/series/論文II_相補性は忘却である.meta.md` v0.1

---

## §1. 本稿の系列位置 — Paper II は橋頭堡である

Paper II 「相補性は忘却である」は、忘却論シリーズ全体の**橋頭堡** (bridgehead) として設計される。

- **系列番号**: II
- **モノグラフ構成設計 §1 での位置**: 第Ⅰ幕「忘却とは何か — 力、相補性、符号」の第 2 章 (Paper I → II → III の中央)
- **役割**: CPS (Container-Projection-Span) 圏と相補性の公理化。忘却論シリーズが「認知と物理の両方に通用する普遍理論」として立つための **基礎公理系**を提供する

### Paper II が立てば、シリーズ全体が立つ

Paper II の核 (FTC → CPS → Face Lemma) が確立すれば、以下のシリーズ論文がこれを参照して展開できる:

- **Paper III (Markov 圏の向こう側)**: CPS の α 全域展開 (α < 0 セクター、反-Markov 構造)
- **Paper IV (なぜ効果量は小さいか)**: CPS の効果量減衰定理と観測上界
- **Paper V (繰り込みは忘却である)**: CPS の RG と普遍性
- **Paper VII (知覚は忘却である)**: CPS のフィルトレーションと認識論
- **Paper VIII (存在は忘却に先行する)**: CPS の圏論的存在論基礎
- **Paper IX (エントロピーは忘却である)**: CPS と熱力学
- **Paper XIII (時空は忘却である)** ★ 新設: CPS の宇宙論・重力・4 つの力への応用

したがって Paper II は「単独で勝負する論文」ではなく、**シリーズの基礎公理系としての書物**である。

## §2. 設計原則 — 攻城戦の段階化

### GPT-5.4 外部監査の受け止め

2026-04-11 に GPT-5.4 外部監査が Paper II v1.11 を 10 軸で判定し、「核は立つが大幅削減必要 / core CPS paper と speculative extension に分割推奨」と結論した。

本シリーズはこの判定を次のように解釈する:

- **GPT の指摘は正しい**: 現状の Paper II は FEP 包含 / LLM 数値検証 / 意識論 / 宇宙論までを一本の論証鎖として抱えており、最も弱い拡張で刺される構造である
- **GPT の処方 (split) は部分的に正しい**: ただし split は「退却」ではなく「**攻城戦の段階化**」として解釈される。Paper II を橋頭堡として立て、その後の Paper III-XIII が本隊進軍として拡張を引き受ける

### 累積シリーズの設計

- Paper II が確立した CPS 公理は、Paper III-XIII が引用として使える
- 現在「橋渡し定義」に見える部分 (α 層化, FEP 包含, 数値検証) は、後続 Paper で独立に証明され、将来の Paper II 改訂でこれらを「引用された定理」として取り込める
- シリーズ構造は Paper 間の相互引用によって自己参照的になり、全体として Fix(G∘F) に近づく (Kalon △)

この設計の下で、Paper II の削減は **論証の時間軸での配置** であって、野心の縮小ではない。

## §3. F⊣G 固定 — Paper II の収束方向

本論文の F⊣G は meta.md §M1 で固定されている。要旨:

### F (左随伴 = 発散)

- **具体化**: 文体ガイド §3 メタファー三連 (2-simplex 発散)
- **Paper II における特殊性**: Face Lemma (§3.4) は 2-simplex (3 射 composable triple) を CPS 構造の最小非自明条件とする。2-simplex の 3 頂点は「3 つの独立射」であり、メタファー三連と圏論的に一致する
- **補助線**: この 2-simplex は Hamming 的な最小検査面として読み直せる。Face Lemma は圏論版 syndrome 条件、n-cell tower は縦の整合条件として働く。詳細は `drafts/infra/FaceLemma_符号理論対応.md`

### G (右随伴 = 収束)

- **具体化**: 文体ガイド §4 数式裏付け + Nerve の 2-coskeletal 性による最小性 + 混合分配則 (mixed distributive law)
- **Paper II における特殊性**: 「発散した 3 射が composable triple として閉じるか」を検証する。Face Lemma / Stability Simplex / Blanket 生成定理の 3 本柱が数式裏付けを構成する

### F⊣G の事後選択禁止

F と G は 2026-04-11 に固定された。以降の Paper II 改訂中、本文執筆者または査読者が「この主張を Kalon に見せるには F と G をこう選べばよい」と逆算することは禁止される (kalon.typos §6 参照)。

固定を変更する場合は meta.md §M1 に変更履歴を残し、既存のすべての核主張 (C1-C3) に再判定を実施する。

## §4. 核主張の境界 — Paper II で証明すること、しないこと

### Paper II で証明する (核主張 C1-C3)

- **C1** (§1.1, §2.1-§2.2, §3.1): CPS スパンによる相補性の統一。Type I 相補性が U_A, U_B の投影として統一され、α > 1 ⟺ Δd ≥ 1
- **C2** (§3.4): Face Lemma による非自明性の最小条件。dim Ξ ≥ 2 ⟺ 3 射 composable triple の存在
- **C3** (§3.7.1-§3.7.3): Blanket 生成定理による FEP 包含。FEP ⊂ CPS|_{α > 0, dim Ξ ≥ 2}

これらは Paper II の本体で完全に形式化・証明される。

### Paper II で証明しない (布石のみ残す)

以下は Paper II の範囲外であり、本文中に **1 文 pointer** として予告する:

| 切断対象 | 削除位置 | 移植先 Paper | 本文 pointer の内容 |
|:---|:---|:---|:---|
| GR インスタンスの完全形式化 | §2.5.3 | Paper XIII §2 | 「一般相対論の CPS 構造は Paper XIII §2 で展開される」 |
| 心身インスタンスの詳細 | §2.5.4 | Paper VIII §6.3 有限主体定理 | 「心身問題の CPS 診断は Paper VIII §6.3 で展開される」 |
| LLM / SWE-bench 数値検証 | §5.2, §5.3, §5.4 | Paper IV 効果量減衰定理 | 「α-層化の計算的再現は Paper IV §3.1 の枠組みで検証される。Paper IV は観測上界 r ≤ √ρ_spec/√(K+1) を予測しており、LLM 隠れ状態層別検証 (pilot, N=500, r ≈ 0.17) はこの上界と整合する。本稿ではこれ以上立ち入らない」 |
| EFE 4 定式化 (Champion 2022) | §3.7.4 | Phase 5 形式化完成 | 命題 3.7.4a (RSA ↔ ROA) のみ維持, b-f は「Champion (2022) §X 参照」に |
| 重力の CPS 積分形式化 | §7.2 | Paper XIII §5-§8 | 「重力の CPS 積分形式化は Paper XIII で展開される」 |
| Yang-Mills との対応 | §7.3 | [予想] 降格 | 「YM 理論の β-関数と α の対応は未検証 [予想]」 |
| 意識のハードプロブレム解決 | §6.2 | Paper VIII 有限主体定理 | 「§6.2 の議論は Chalmers (1995) のハードプロブレムを**解決しない**。その構造的原因を CPS と Face Lemma の観点から**診断**する。心身問題の圏論的基礎は Paper VIII §6.3 で展開される」 |
| α 層化 (§3.3) の定理化 | §3.3 | Paper III 形式化 | 「α(θ) と Δd の対応は本稿では**定義**として採用する。Amari-Nagaoka (2000) の統計多様体では非厳密。厳密な関手証明は Paper III で実施される」 |

**Sherlock's dog の原則**: 切断した各節に 1 文の pointer を残す。これにより Paper II は「縮約版」ではなく「シリーズの第 2 章」として読める。読者は「何が Paper II の範囲外か」を明示的に知る。

## §5. α 層化 blocker の現状認識

Paper II の最大の弱点は §3.3 α 層化定理である。GPT 監査が「橋の健全性 (軸 5)」で指摘した通り、α(θ) の整数部分 = Δd の対応は現状「動機付けられた構成」であり、証明ではない。

### 解決経路の並行攻略

Paper II の Phase 5 (blocker 並行攻略) では、以下の 2 経路を並行で試みる:

**経路 A (内部導出)**: Markov category の構造定数から α を induce する定理を 1 本立てる。具体的には、CPS スパンの非可換性を測る Hom-空間 Drift ∈ [0, 1] を α と同定する構成。成功すれば §3.3 は「定義」ではなく「命題」になる。

**経路 B (ansatz 明示)**: 導出を断念する代わりに、α を明示的に "structural ansatz" と宣言し、その存在を前提とした **conditional theorem** として §3.7 を書き直す。弱いが正直。後続査読で「未証明橋を証明済みとして使った」の批判は消える。

**判定基準**: A を試み、3 ヶ月で閉じなければ B に降りる。A を試みずに B に行くのは怠慢。B を試みずに A を主張するのは欺瞞。

### Paper XIII との相互補強

Paper XIII (時空は忘却である) の Phase 5 で Face Lemma ↔ Ricci 曲率の dictionary が閉じれば、Paper II の α 層化も強化される可能性がある。以下の対応が想定される:

- CPS スパンの α と gravitational coupling G_N の関係
- Face Lemma の最小非自明性 ↔ Einstein 方程式の minimal action principle
- CPS0' pre-geometric 構造から (3 + 1) signature の発生

Paper II と Paper XIII は相互引用で強化される。両方の blocker が同時に閉じるか、同時に開くかはシリーズ全体の Kalon 判定の試金石。

## §6. 数値節の処理 — 諦めではなく再配置

Paper II v1.11 の §5.2, §5.3, §5.4 の LLM/SWE-bench 数値節 (N = 500, r ≈ 0.17) は完全削除される。代わりに:

### 論理的役割の転換

現状の r ≈ 0.17 は「弱い支持」ではなく「**Paper IV 効果量減衰定理が予測する上界との整合**」として読める。これは論理的役割の転換である:

- **誤った使い方** (v1.11 の現状): 「r = 0.17 だから Face Lemma は経験的に確認された」→ GPT が批判する弱い論証
- **正しい使い方** (v1.12): 「r ≈ 0.17 は Paper IV 効果量減衰定理が予測する観測上界 r ≤ √ρ_spec/√(K+1) と整合する。理論が予測するのは強い相関ではなく、**上界の存在そのもの**である」→ null result の構造的意味づけ

### Paper IV での本格検証

数値検証は Paper IV の独立論文として実施される:

- **経路 1 (上界テスト)**: r が 0.2 を超えないことを検証する仮説テスト
- **経路 2 (pre-registration + 複数モデル)**: N ≥ 5000, 10+ モデル, effect size 判定基準の事前登録, repo 確定公開
- **経路 3 (SWE-bench 全件検証)**: N = 80,036 の全件解析 (モノグラフ構成設計 §10 想定)

これらは Paper II の範囲外であり、本文に 1 文 pointer のみ残す (§4 参照)。

## §7. Kalon 判定 (シリーズ構造)

Paper II v1.12 と Paper XIII v0.1 を含むシリーズ構造について、Kalon = Fix(G∘F) の判定を実施:

### 入口 ±3σ

「累積シリーズで認知から物理まで届かせる」主張は既存論文分布の ±4σ 領域:

- Wiles の連作論文、Grothendieck の EGA/SGA 等の先例はあるが主流ではない
- Verlinde 2011 / Jacobson 1995 の物理 forgetful 構造と接続することで既存分布のさらに裾に入る
- Paper XIII の Face Lemma ↔ 曲率 dictionary が閉じれば ±5σ 領域

### Gauntlet Round 1 (シリーズ全体)

GPT 監査の 10 軸を Paper II 単体で処理する場合、meta.md §M5 で全 10 軸 Round 1 射程維持を達成した。ただし軸 8 (哲学的射程の統制) で「解決 → 診断」の一部後退を記録している。

### Round 3 非発動の記録

Round 1 で射程維持が達成されたため Round 3 (Solution-Focus) は非発動。ただし非発動も記録する (meta.md §M5 末尾参照)。

### Kalon 判定

- **G (収束)**: Paper II を削減 + 核主張 C1-C3 のみに集中 → 不変 (最小単位)
- **F (発散)**: 1 つの公理化 (CPS) が後続 Paper (III, IV, V, VII, VIII, IX, XIII) を生む → 非自明派生 7 本以上 ✓
- **不動点**: シリーズ構造は自己参照的 (Paper II ↔ III, II ↔ IV, II ↔ VIII, II ↔ XIII の相互引用ループ) ✓
- **判定**: ◎ Kalon △ (Yugaku workspace 内の局所不動点)

ただし Kalon ▽ (全空間の普遍不動点) には到達していない。これは Yugaku workspace の MB 内での局所判定であり、外部査読 (Kalon ▽) への到達はさらなる改訂を要する。

## §8. 本前置宣言の改訂履歴

- **v1.0 (2026-04-11)**: 初版。Phase 4 §4.1 成果物。GPT-5.4 外部監査 (2026-04-11) への構造的応答として作成。meta.md v0.1 と同時生成。

---

## 付録 A: 関連文書

- **本稿 meta.md**: `drafts/series/論文II_相補性は忘却である.meta.md` v0.1
- **対応本稿**: `drafts/series/論文II_相補性は忘却である_草稿.md` v1.11 → v1.12
- **Phase 1 成果物 (解体マップ)**: `drafts/infra/v2_解体マップ.md`
- **Phase 2 成果物 (Paper XIII)**: `drafts/series/論文XIII_時空は忘却である_草稿.md` v0.1
- **Phase 4 計画**: `~/.claude/plans/swirling-hugging-ripple.md`

## 付録 B: Yugaku workspace rules (適用されたもの)

- `yugaku-kalon-check.md`: 核主張 C1-C3 に対する Fix(G∘F) 判定の枠組み
- `yugaku-provocation-gauntlet.md`: GPT 監査 10 軸を Round 1 で処理する射程維持戦略
- `yugaku-sigma-heuristic.md`: ±3σ 入口/出口ゲートによる μ 引力の検出

Yugaku workspace の 3 層機械 (Kalon / ±3σ / Gauntlet) は本前置宣言の全体設計に反映されている。
