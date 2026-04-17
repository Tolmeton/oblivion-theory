# codex 結果: g^(α) 計量族の文献調査 (梁5)

**計算日**: 2026-04-xx  
**元ファイル**: codex_brief_g_alpha_literature.md + codex_report_g_alpha_literature.md

---

## §タスク

論文I §6.7 の記号 `g^(α)` — α でパラメータ化された統計多様体上のリーマン計量族 — に文献的裏付けがあるかを確認する。

**問題**: Amari (2016) では α-接続 ∇^(α) は接続の族であって計量の族ではない。Čencov の定理 (1982) により統計多様体上の不変計量は Fisher 計量が (スケール倍を除き) 一意。つまり `g^(α)` は Amari の標準枠組みでは未定義の可能性が高い。

**調査対象**:
1. Shima (2007) *The Geometry of Hessian Structures*
2. Ay, Jost, Lê, Schwachhöfer (2017) *Information Geometry*
3. Calin–Udrişte (2014) *Geometric Modeling in Probability and Statistics*
4. Naudts (2011) 系 — q/φ 変形計量族
5. 近年 arXiv (2020–2026)

---

## §結果

**判定: NOT FOUND**

Amari-Čencov 以外で coherent な `g^(α)` 計量族は、調査範囲では確認できなかった。[確信: 高]

### 核心証拠

| 文献 | 確認箇所 | 確認内容 | 含意 |
|:---|:---|:---|:---|
| Ay et al. arXiv:1207.6736 | Thm. 2.10(2), Thm. 3.5 | 不変な二次形式は Fisher quadratic form の定数倍に限る | 不変性を保つ限り `g^(α)` なる別計量族の余地なし |
| Shima (2007) | Def. 2.1, Prop. 2.2 pp.14-15 | Hessian potential 由来の計量は確認。α 依存なし | Hessian 幾何でも `g^(α)` は未発見 |
| Calin–Udrişte (2014) | Ch. 8, pp. 223-255 | 「1つの metric + dual connection pair」の構図 | `α` で metric を動かす話ではない |
| Vigelis et al. arXiv:1511.01176 | Eq. (1), (13), (16) | φ-family から metric を定義するが、`α` は既に選ばれた metric 上の connection family に掛かる | `g^(α)` ではない |

### 近傍発見 (g^(α) にはならない)

- **Naudts 系 (q/φ 変形)**: generalized Fisher は存在するが α-family ではない
- **κ-thermostatistics (Wada–Scarfone 2015)**: κ で metric を動かすが α ではない
- **Newton 2024**: 2-parameter deformed manifold だが metric は Fisher-Rao 固定

### 結論と論文I への帰結

> `g^(α) := g^(0)` として Fisher 計量を固定し、`α` は connection/divergence 側だけに残す **Option C** が最も defensible。

論文I §6.7 の α-SAM は `g^(0)` (Fisher 計量) で再定式化する。
