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

## 参照

- automath: https://github.com/the-omega-institute/automath (Lean 4, 3,427+ theorems)
- The Omega: https://github.com/loning/the-omega (Von Neumann algebras + QCA, 17 books + Lean 4)
- 忘却論シリーズ: ../series/ (Paper 0-XIII)
- 出版計画: ../../plans/出版計画_忘却論シリーズ.md
- NotebookLM notebook: 忘却論シリーズ (91 sources, 2026-04-12)
