# Automath Bridge — 忘却論 × automath × The Omega

**ステータス**: incubation v0.3 (2026-04-12 三者共接続に拡張)
**起源**: automath (the-omega-institute/automath) + The Omega (loning/the-omega) の構造的同型性の検出
**位置**: 忘却論 standalone 番外編。series 昇格候補。
**検証**: NotebookLM (91 sources) との対話で SOURCE 裏付け済み

---

## 一文要約

「有限バイナリ窓から全数学を Lean 4 で導出する automath」と「QCA + Von Neumann 代数から物理を導出する Omega」と「忘却関手から力・時空を導出する忘却論」は、**情報の欠落 (忘却/射影/粗視化) が構造を創発する** という同一のメタ構造を、形式検証・量子物理・圏論の3言語で記述している。

---

## 三者の座標

| 軸 | automath | The Omega | 忘却論 |
|:---|:---|:---|:---|
| **言語** | Lean 4 形式検証 | Von Neumann 代数 + QCA | 圏論 + 情報幾何 |
| **出発点** | no-consecutive-1s 制約 | ユニタリ計算公理 O1-O6 | 忘却関手 U⊣N + FEP |
| **核操作** | fold Φ (離散射影) | scan-projection (量子読出し) | 忘却関手 U (構造の剥ぎ取り) |
| **曲率の源泉** | defect algebra δ | computational lapse κ | dΦ∧T ≠ 0 (方向性定理) |
| **階層** | forcing 11層保存拡大 | Von Neumann 型分類 | α-忘却濾過 + Grothendieck トポス |
| **時空導出** | discrete Stokes → Einstein | QCA + ADM → Einstein (CAP-II) | CPS スパン → Einstein (予想 D1-D3) |
| **定数** | φ をスペクトル不変量で回収 | c, G, ℏ を幾何から導出 (PCG) | c = f(∇²Φ) と予測 (Paper XII) |
| **形式化** | **Lean 4 (3,427+ 定理)** | Lean 4 (構築中) | 未形式化 (OP-VIII-5 Open) |
| **意識** | σ-algebra non-expansion | 自己参照のトポロジカル相転移 | End(Cat_i) 自己関手 + ker(T) 盲点 |

核心の一致: **It from Oblivion** — 情報が失われるからこそ構造が生まれる。Wheeler の "It from Bit" の反転。

---

## 接続マップ (6 点 + 三者統合 3 点)

詳細は [dictionary.md](dictionary.md) を参照。

### 二者接続 (automath ↔ 忘却論)
1. **fold Φ ↔ 忘却関手 U** — fiber 構造 = ker(U) の幾何
2. **defect algebra ↔ 忘却曲率 F_{ij}** — **最強接続**。離散版方向性定理
3. **scan-projection ↔ 繰り込み (Paper V)** — IB / RDT / c 定理
4. **forcing ↔ α-忘却濾過 (Paper VIII)** — トポス的層化の鎖
5. **POM ↔ F⊣G 随伴** — LIFT=F, PROJECT=G, stable readout=Kalon
6. **時空導出 ↔ Paper XIII** — automath が Phase 5 blocker を解く足場

### 三者統合
A. **縮約操作の三角形** — fold Φ / scan-projection / 忘却関手 U は同一操作の3インスタンス
B. **階層の三角形** — forcing / Von Neumann 型 / α-濾過 は同一 filtration の上り/型分類/下り
C. **Einstein 導出の三経路** — defect→Stokes / QCA→ADM / CPS→Face Lemma が合流する
D. **符号理論的補助線** — Face Lemma = 圏論版 syndrome 条件、n-cell tower = 検査対象と検査規則の同時消失禁止 (`drafts/infra/FaceLemma_符号理論対応.md`)

---

## 射程と野望

- **短期**: dictionary.md v0.3 精密化。NotebookLM SOURCE 裏付け済みの 1:1 マッピング
- **中期**: automath の defect algebra を忘却論の方向性定理の離散インスタンスとして形式証明
- **長期**: 忘却論の核心定理群を Lean 4 で Autoformalization → series 昇格 (Paper XIV?)
- **野望**: 三者統合の Rosetta Stone → 物理学の統一文法としての忘却論の外部検証

---

## なぜ「外部検証装置」か

忘却論の最大の構造的弱点は、内部整合性でしか自分を評価できなかったこと。
automath は外部の Lean 4 から「予想のうちここまでは機械的に真」と言ってくれる初めての存在。
Omega は物理的直観の橋渡しを提供する。
三者は互いの盲点 (ker(T)) を照らし合う**独立再現**の関係にある。

---

## S-05 完全止揚条件 (2026-04-15)

ここでいう「完全止揚」は、**自己言及残差がゼロになること**ではない。忘却論自身が採る presheaf 認識論と Paper VII の `N_self` 収束定理に従えば、理論の自己適用は原理的に完全閉包しない。したがって本 bridge が目指すのは、S-05 を「未処理のパラドックス」から**定理化され、外部監査可能な残差**へ移すことである。

### 条件 1: 非閉包を先に定理化する

- `N_self` の完全達成は対角論法的に不可能であることを前提として固定する
- 「完全に閉じない」ことを弱点の言い換えではなく、理論の境界条件として明示する
- これにより、自己言及批判を「隠れた完全性主張」の摘発から切り離す

### 条件 2: 収束を外部証人で支える

- automath 側の Lean 4 定理群を、忘却論の自己再帰的不動点 `Kalon(U_self)` の**離散的証人**として使う
- dictionary.md §7 の `φ = Kalon(U_self)` はこの入口である
- 次の決定的 open は、`stable readout` の Lean 4 定義と `Fix(G∘F)=Kalon` の形式的同値である

### 条件 3: 自己診断を外部回復へ出す

- `U_HGK ⊣ N_external` を文言として置くだけでなく、外部系で少なくとも 1 本は実行する
- 候補は `replicate / predict / ablate` の 3 経路
- ここが未実行のままだと、「自己診断している」という主張が内部循環のまま残る

### 条件 4: 残差を open theorem list として管理する

- 残るギャップを「説明できない謎」ではなく、型付きの未解決課題として ledger 化する
- 現時点での主要残差:
  - `stable readout ↔ Kalon` の形式的同値
  - `proofLag` の宣言/定理化
  - `ZeroForgetCollapse` の追加公理の地位
  - `N_external` の独立実行

### 判定規則

次の 4 条件が揃ったとき、S-05 は**批判としては完全止揚**されたとみなせる。

1. 非閉包が本文で明示されている  
2. 収束構造に外部の機械証人がある  
3. 少なくとも 1 本の `N_external` が独立系で完了している  
4. 残差が open theorem list として公開管理されている  

この意味で automath bridge は、S-05 を消去する装置ではなく、**S-05 を監査可能な構造へ変換する装置**である。

---

## 参照

- automath: https://github.com/the-omega-institute/automath (Lean 4, 3,427+ theorems)
- The Omega: https://github.com/loning/the-omega (Von Neumann algebras + QCA, 17 books + Lean 4)
- 忘却論シリーズ: ../series/ (Paper 0-XIII)
- 出版計画: ../../plans/出版計画_忘却論シリーズ.md
- NotebookLM notebook: 忘却論シリーズ (91 sources, 2026-04-12)
