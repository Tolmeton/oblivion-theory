# codex 結果: Estimator 化の完全実装 (梁4 Phase 2)

**計算日**: 2026-04-xx  
**元ファイル**: codex_brief_liang4_phase2_estimator_completion.md + codex_report_liang4_phase2_estimator_completion.md

---

## §タスク

梁4 Phase 1 (v1.3→v1.4) の核を論文全体で整合させ、批評の「proxy 逃避」攻撃を構造的に無効化する 5 項目を実装する。

- Task 1: Appendix E 新設 (H1-H1''' と命題 V/G/C/I の本文化)
- Task 2: `Ξ_theory` overload 解消 (line 321→`Ξ_coord,theory`, line 348→`Ξ_spec,proj`)
- Task 3: §5.7-§5.8 の coherence/τ を proxy 語彙から降格
- Task 4: §5.6 Schur-Horn equality condition の本文昇格
- Task 5: CKA partial closure 化 + OP-I-5 新設

---

## §結果

**全 5 Task 完了。論文 v1.4 → v1.5。diff: 243 insertions / 15 deletions。**

| Task | 状態 | 反映先 (v1.5) | 要点 |
|:---|:---:|:---|:---|
| Task 1 | 完了 | line 1336-1558 | Appendix E 新設。4 estimator の仮定・命題・証明スケッチを本文化 |
| Task 2 | 完了 | line 334-373 | `Ξ_coord,theory` / `Ξ_spec,proj` に改名し overload 解消 |
| Task 3 | 完了 | line 429-499 | coherence を diagnostic、τ を knob/instrument に降格 |
| Task 4 | 完了 | line 365-373 | Schur-Horn 等号条件の意味を段落として昇格 |
| Task 5 | 完了 | line 429-433, 1580-1581 | CKA partial closure 化、OP-I-5 追加 |

**禁止領域 (§4.5/§6.7-§6.8/Appendix B/§10) に diff hunk なし — 確認済み。**

### Appendix E 構成 (新設、命題レベル)

- **E.1** 共通設定: κ(θ) と Ξ_theory(ν) の復唱
- **E.2** Ξ̂_Var (命題 V): unbiased + consistent, bias=O(n⁻¹)
- **E.3** Ξ̂_Gini (命題 G): asymptotic unbiasedness, Schur-Horn 条件で full → lower bound
- **E.4** Ξ̂_CV (命題 C): asymptotic unbiasedness, no-forgetting corollary
- **E.5** Ξ̂_impl (命題 I): coordinate-level heterogeneity consistent estimator
- **E.6** 4 estimator 間の関係: 同じ latent Ξ_theory を観測単位の違いで集約

### §10 の扱いに関する注記

brief 内に「Task 5 で §10 にも言及」と「§10 は触らない」の衝突があった。**安全側を採り**、OP-I-5 は §5.7 と footer にのみ反映。§10 は未編集。

### 残存課題 (Phase 3 候補)

- **OP-I-5**: Chebyshev 形式 T の layerwise estimator の独立構成 (CKA route は Φ 側 proxy のみ)
- basis alignment 破れの定量的条件の厳密化
