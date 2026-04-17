# codex 結果: P5 bug 確定 + 数値検証拡張 (梁6 Phase B)

**計算日**: 2026-04-xx  
**元ファイル**: codex_brief_liang6_phaseB_reproducibility.md + codex_report_liang6_phaseB_reproducibility.md

---

## §タスク

論文I v1.4 の **P5 line 1108「κ = 9Φ_c/(2θ₀²) — 検証済 (1.4×10⁻¹⁰)」**の真偽確定 + カテゴリカルシンプレックス Δⁿ での dT=0 数値検証 + 非指数型分布族での dT≠0 反例。

---

## §結果

### P5 bug: 確定

**判定: P5 の「検証済 (1.4×10⁻¹⁰)」は bug。**

| 要素 | 実態 |
|:---|:---|
| `1.4×10⁻¹⁰` の出所 | `oblivion_field_gaussian.py` line 195-209 の **F₁₂ 有限差分誤差**。κ とは無関係 |
| κ の扱い | 同 line 233-239 で **計算して print するだけ**。assert も期待値比較もない |
| 論文 P5 行の実位置 | v1.4 では line 1078 (brief の「line 1108」は古い offset) |
| κ の導出箇所 | line 676-684 に derivation sketch あり → 式自体はソースを持つ |
| 記号対応 | θ_c=0, σ=1 の特殊化のみで一致。一般式の検証ではない |

**修正案**: P5 の「数値的 / 検証済 (1.4×10⁻¹⁰)」→「解析的 / 予測 (未検証)」に降格。

### 新規スクリプト (実行検証済み)

**categorical_simplex_dT_check.py**

```
$ python categorical_simplex_dT_check.py
overall max|dT| = 0.000e+00
OK: categorical simplex verifies dT = 0 for n = 2, 3, 4.
```

→ Δ², Δ³, Δ⁴ の全 sample 点で dT = 0 を機械精度で確認。論文 §5.4 / Appendix B の主張を数値裏付け。

**non_exponential_dT_counterexample.py** (Student t 族 (ν, γ))

```
$ python non_exponential_dT_counterexample.py
OK: Student t family gives a non-trivial dT != 0 counterexample.
|dT| = 3.27e-1 〜 9.41e-1 (複数点で検証)
```

→ 非指数型分布族で dT≠0 を定量化。「dT=0 は指数型分布族に特有」の主張を数値裏付け。

### 論文本体への反映

論文本体は**未編集** (梁4 Phase 2 と並行稼働中のためコンフリクト回避)。  
diff 提案のみ: P5 修正案 + §5.4 line 260 付近追記 + Appendix B 1-2 行追記 + Student t 反例の新設節。

### 追加で発見した問題

**図ファイルの provenance 不整合**:
- 論文 §4.5 line 193-194 は `fig1_oblivion_field.png`, `fig2_curvature_F12.png` を参照
- 現行 `oblivion_field_gaussian.py` が生成するのは `oblivion_curvature.png`, `alpha_dynamics.png` のみ
- `fig1_*`, `fig2_*` は旧版スクリプトの残骸または手動コピーの可能性 → flag として保留
