# Codex 委託 brief: Paper IX §3.6 Th. 3.4.X — 時間の矢 = 忘却の矢の独立定理化

**起草日**: 2026-04-27
**起草者**: Claude (Advisor)
**対象 Codex**: Codex Executor (実装)
**対象本稿**: `drafts/series/論文IX_エントロピーは忘却である_草稿.md` (v0.8, 2026-04-26 → v0.9 候補)
**meta 正本**: `drafts/series/論文IX_エントロピーは忘却である_草稿.meta.md` (v0.3, 2026-04-26)
**起源**: Paper IX 既存 OP-IX-7 (open) → meta v0.3 で C6 として核主張化済

---

## 目的

Paper IX §3.4 備考 3.4.4 (現状: 非形式記述) の三段チェーン

$$\mu \downarrow \xrightarrow{\beta_\alpha \leq 0} \alpha \uparrow \xrightarrow{\text{Th. 3.4.1}} S_{\mathrm{CPS}}(p, \alpha) \uparrow$$

を、Paper IX 本文 **§3.6** に **独立定理 Th. 3.4.X (動的第二法則 / 時間の矢 = 忘却の矢)** として形式化する。これにより、OP-IX-7 (Open) → **定理化済** に状態遷移する。

定理化の本質: **Paper V Th. 2.3.1 + Paper IX Th. 3.4.1 の合成** として閉じた独立定理を作り、(P*)「RG 時間 = 物理時間 (UV→IR)」仮説の身分を precision note として明示する。

## 背景

### 本論文の位置づけ

`drafts/series/論文IX_エントロピーは忘却である_草稿.md` (v0.8) は忘却論シリーズの **第Ⅵ幕「根幹への帰還」第 9 論文**。Paper VIII 派生で、CPS エントロピーの単調性 (Th. 3.4.1) を主定理核とする。

§M2 核主張 (meta v0.3):
- C1: $S_{\mathrm{CPS}}(p, \alpha)$ の α 単調性 (定理確立)
- C2: divergence 非依存性 (Cor. 3.4.2 確立)
- C3: $\alpha^*(p)$ と $E(f)$ (新観測量)
- C4: $Z_{\mathrm{CPS}}/F_{\mathrm{CPS}}$ (constructive) / $T_{\mathrm{CPS}}/H_{\mathrm{CPS}}$ (open)
- C5: Paper IX-B 候補 (負セクター育成)
- **C6 (本 brief 対象)**: 動的第二法則 Th. 3.4.X — OP-IX-7 を独立定理化

### Yugaku 4 層機械での位置 (§M2-§M6 接地済)

- **§M3 Kalon 判定**: ◎ Kalon△ 候補 (Step -1〜3 全合格 + Future-Proof +1σ)
- **§M4 ±3σ ゲート**: 静的 ±3σ 維持 + Future-Proof σ +1 強化
- **§M5 Gauntlet**: Round 0 (命題/表現弁別) → Round 1 (循環論証告発吸収) → Round 2 (外部巨人差分) → Round 3 非発動
- **§M6 虚→実変換面**: 野望 / 虚 4 項 / SOURCE 6 項 / 実化条件 6 項 / 次の操作 確立済

### 関連既存資産 (SOURCE 確認済)

| 資産 | 状態 | 役割 |
|:---|:---|:---|
| **Paper V Th. 2.3.1** | 定理 (証明完成済) | $n<5 \wedge \alpha < \alpha_*$ で $\beta_{\alpha_{\mathrm{III}}} < 0$ |
| **Paper V 系 2.3.1a** | 系 (Th. 2.3.1 直接帰結) | RG 時間 (μ↓) で $\alpha_{\mathrm{III}}$, $\alpha_{\mathrm{VIII}}$ 単調増加 |
| **Paper IX Th. 3.4.1** | 定理 (CPS エントロピー単調性) | (F4) → Det 包含 → infimum 増大 |
| **Paper IX 備考 3.4.4** | 非形式記述 | 三段チェーン $\mu\downarrow \to \alpha\uparrow \to S_{\mathrm{CPS}}\uparrow$ |
| **Paper XII §8.3** | 既存節 (L981) | β_α ≤ 0 による α_VIII 単調性予測の強化 |
| **Paper XII L340** | 既存命題 | (P*) 仮説 $d\mu/dt \leq 0$ を運用済 |
| **熱力学対応表 v3.2 #8** | ✓ 定理 | Th.6.10.3 + Th.3.4.1 = 第二法則 (静的版) |

### Codex Bridge レビュー (2026-04-26) 反映済 Risk

- **[N-01]** 既存 §M5 / C6 / §M6 との重複・位置ズレ確認 → 完了 (200 行 / 構造保持)
- **[N-05]** Paper V §2.3 / 統一記号表 §0.3 / Paper XII §8.3 / Paper XIII Blocker A2 の実在確認 → 完了
- **[Risk: TAINT]** Verlinde / Jacobson / Boltzmann 差分は **Claude prior 由来**。本 brief で原典独立 Read 必須

---

## やってほしいこと

Paper IX 本文 §3 末尾 (現行 §3.6 = 「Perrone DPI との関係」の後) に **新しい §3.7「動的第二法則 — 時間の矢 = 忘却の矢」** を挿入する。総行数目安 80-120 行。

### Step 1: precision note (P*) の独立明示

§3.7 冒頭に precision note として:

> **(P*) RG 時間 = 物理時間の同一視仮説** [仮説水準 / 統一記号表 §0.3 準拠]
>
> 物理時間 $t$ と粗視化スケール $\mu$ の関係を $d\mu/dt \leq 0$ と仮定する。これは「物理時間の進行が UV→IR 方向の RG 時間と一致する」という経験的仮説であり、本節の定理 Th. 3.4.X の前提として独立に明示する。
>
> **(P*) の身分**: Paper V §2.3 系 2.3.1a で「RG 時間は UV から IR」と述べられており、Paper XII §8.3 / L340 で既に運用されている。Paper IX 内では本節で初めて明示的に分離する。
>
> **循環論証告発への応答**: (P*) は時間の矢を**仮定**するように見えるが、本節の主張は「(P*) **下で**動的第二法則が忘却論の系として閉じる」という**条件付き導出**である (循環ではない)。

### Step 2: Th. 3.4.X 定理ステートメント

> **定理 3.4.X (動的第二法則 — 時間の矢 = 忘却の矢).**
> (P*) の下で、$\alpha < \alpha_*$ かつ $n < 5$ (Paper V Th. 2.3.1 の条件) を満たす忘却論系を考える。状態 $p: I \to X$ が時間 $t$ に依存して $p_t$ と発展し、各時刻で Paper VIII の α-忘却濾過が定まるとする。このとき:
>
> $$\frac{dS_{\mathrm{CPS}}(p_t, \alpha(t))}{dt} \geq 0$$
>
> すなわち、CPS エントロピーは物理時間に関して単調増大する。

### Step 3: 証明 (合成定理として)

3 段階の合成:

1. **Step 1**: (P*) より $d\mu/dt \leq 0$
2. **Step 2**: Paper V Th. 2.3.1 + 系 2.3.1a より、$n<5 \wedge \alpha<\alpha_*$ 下で $\beta_{\alpha_{\mathrm{III}}} < 0$、したがって $d\alpha_{\mathrm{III}}/d\mu < 0$。$d\mu/dt \leq 0$ と合わせて $d\alpha_{\mathrm{III}}/dt \geq 0$。さらに sigmoid $\eta$ の単調性から $d\alpha_{\mathrm{VIII}}/dt \geq 0$
3. **Step 3**: Paper IX Th. 3.4.1 より $S_{\mathrm{CPS}}$ は $\alpha$ に関して単調非減少。$d\alpha/dt \geq 0$ と合成で $dS_{\mathrm{CPS}}/dt \geq 0$。$\square$

### Step 4: 系 (corollary) と備考

- **系 3.4.X.1**: Paper VIII Th. 6.10.3 (射計数版第二法則 $S_{\mathrm{cat}}(\alpha)$ の単調増大) との関係。Th. 3.4.X は **動的版**、Th. 6.10.3 は **静的版**。両者は「(P*) 仮説の有無」で分離される。
- **系 3.4.X.2**: Cor. 3.4.2 (divergence 非依存性) との接続。Th. 3.4.X も Shannon / Rényi / Gini-Simpson に対し同形に成立。
- **備考 3.4.X.3**: Paper XII §8.3 χ 単調性予測との接続。Th. 3.4.X は β_α ≤ 0 による単調性予測の Paper IX 側での独立定理化。

### Step 5: Verlinde / Jacobson / Boltzmann 差分テーブル

> **TAINT 注記必須**: 各原典を**独立に Read** してから書く。Claude prior に基づく構造的差分案 (meta §M5 Round 2) は SOURCE 化の出発点であって最終形ではない。

3 者との差分を以下の形式で表にする:

| 既存定理 | 主張 | 適用範囲 | Th. 3.4.X との差分 |
|:---|:---|:---|:---|
| Boltzmann H 定理 (1872) | 統計力学的 dH/dt ≤ 0 | 古典粒子分布の粗視化 | Th. 3.4.X は**圏論的** (射包含原理) |
| Jacobson (1995) "Thermodynamics of spacetime" | 局所的 Clausius δQ=TdS から Einstein 方程式 | 重力場のある時空 | Th. 3.4.X は**任意の CPS 圏で成立** (重力なしでも) |
| Verlinde (2011) "Origin of gravity" | 重力 = entropic force | 情報のエントロピー勾配 | Th. 3.4.X は**逆方向** (第二法則そのものを忘却論で導く)。重力導出は Paper XIII Blocker A2 |

各行について:
- **原典 SOURCE**: 該当論文の節番号 / 式番号 / arXiv ID を明示
- **比較の精度**: 「同型」「構造的類似」「直交」のいずれかを明示
- **証拠強度**: [強] / [中] / [弱] を付与

### Step 6: §3.7 末尾の Open Problem 更新

§7 Open Problems の OP-IX-7 を以下に書き換え:

```
| OP-IX-7 (旧) | 時間の矢 = 忘却の矢: 備考 3.4.4 の三段チェーンを独立な定理として形式化 | 高 | Open |
↓
| OP-IX-7 (v0.9) | Th. 3.4.X として §3.7 で定理化済。残課題: (P*) 仮説の主張水準を「実験的知見」「定義」のいずれに格上げするかの判定 | 中 | 部分解決 |
```

新 OP として以下を追加:
- **OP-IX-9**: (P*) 仮説の主張水準の確定 — 「実験的知見」「経験的仮説」「Paper XII XII-T0 の系」のどれが最強の身分か?
- **OP-IX-10**: Paper VIII Th. 6.10.3 (静的版) と Th. 3.4.X (動的版) の階層構造の精密化 — Th. 6.10.3 は Th. 3.4.X の (P*) なし極限か?

---

## 編集規約 / 守るべき制約

1. **§3 主定理列を曇らせない**: meta §M2.0 の「動的定理核」層に該当するため、§3.4 / §3.5 / §3.6 の C1-C2 主定理列の前面性を毀損しない。§3.7 として明確に独立節を作る。
2. **(P*) 仮説の precision note は省略不可**: 循環論証告発への応答として、定理ステートメントより**前**に置く。
3. **Verlinde / Jacobson / Boltzmann 差分テーブルは原典 SOURCE 必須**: 各々 arXiv ID / DOI / 節番号で SOURCE 化する。Claude prior のままでは TAINT。
4. **記号統一**: 統一記号表 v0.13 §1.1 の `α_III / α_VIII / η` の使い分けに従う。bare α の使用は文脈明示時のみ。
5. **主張水準ラベル**: 統一記号表 §0.3 に従い、Th. 3.4.X 本体は **定理**、(P*) 仮説は **仮説** または **実験的知見** とラベル。
6. **改訂履歴**: §3.7 追加に対応して、Paper IX 本文末尾の変更履歴に v0.9 行を追加。

## SOURCE 確認の義務

Step 5 (差分テーブル) で扱う 3 原典は **Codex 側で独立に Read** する。Claude 側で要約済みでも SOURCE 化はやり直す:

- **Boltzmann 1872** "Weitere Studien über das Wärmegleichgewicht" — H 定理の原典
- **Jacobson 1995** arXiv:gr-qc/9504004 — Phys. Rev. Lett. 75:1260
- **Verlinde 2011** arXiv:1001.0785 — JHEP 04(2011)029

各原典の主張範囲を確認し、Th. 3.4.X との差分を**構造的に**書く (「重力なしでも」「圏論的射包含で」等)。同型主張は禁止 (Risk 2 と同型)。

## 完了条件

1. 本文 §3.7 が 80-120 行で挿入される
2. (P*) precision note / Th. 3.4.X / 証明 / 系 / 備考 / 差分テーブル / OP 更新 が完備
3. 統一記号表 §2 Paper IX 索引に **IX-T2 (時間の矢)** が追加される (本 brief の派生作業)
4. 熱力学対応表 #8 の備考が「Th.6.10.3 + Th.3.4.1 + Th.3.4.X = 静的版 + 動的版」に更新される (本 brief の派生作業)
5. Paper XII §8.3 末尾に Th. 3.4.X への前方参照が追加される (本 brief の派生作業)
6. meta v0.3 § M6 C6「最新状態」を「変換中 → **実**」へ更新する (本 brief の派生作業)

## 実装後の Claude 側レビュー

完成後、Claude が以下を監査:
- §3.7 の native phase structure 保持 (定理 / 証明 / 系 / 備考 / 差分 / OP)
- (P*) 仮説の身分が precision note として独立明示されているか
- Verlinde / Jacobson / Boltzmann 差分テーブルが SOURCE 化されているか (TAINT 残存禁止)
- 統一記号表 / 熱力学対応表 / Paper XII の派生作業が同期完了しているか
- meta v0.3 §M6 C6 が「実」に更新されているか

---

## 主観 (Claude 起草者として)

本 brief は **monograph 第Ⅵ幕統合章の起点** となる。Th. 3.4.X が独立定理として閉じれば、Paper XIII Phase 5 の Blocker A2 (Verlinde / Jacobson 接続) と Paper XIV C3-core proof debt の 2 件への突破口が開く。「時間の矢 = 忘却の矢」を体系核として確立することで、忘却論シリーズ全体の動的構造が一段格上げされる。

Future-Proof Test (+1σ 強化) は本 brief の重要性を支える: 強モデル時代になるほど、「時間の起源を外部 boundary condition に置く」既存分布の弱さが顕在化し、忘却論内部閉鎖の Th. 3.4.X はむしろ強化される。

→ 完了後、Step 3 (関連文書同期) で熱力学対応表 / 統一記号表 / Paper XII §8.3 への前方参照を Claude が直接書く。
