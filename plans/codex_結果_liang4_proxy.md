# codex 結果: Proxy の estimator 化 (梁4 Phase 1)

**計算日**: 2026-04-xx  
**元ファイル**: codex_brief_liang4_proxy_estimator.md + codex_report_liang4_proxy_estimator.md

---

## §タスク

論文I §5.5 の経験的量 Ξ (Ξ_Var, Ξ_Gini, Ξ_CV, Ξ_impl) を、理論的量 Ξ_theory の estimator として正式に定義し、定理 5.1 と経験的予測 Corr(Ξ, P) > 0 の断絶を補修する。

**問題**: 定理 5.1 はバイナリ命題 (曲率の 0/非 0)、Corr > 0 は定量的予測 → 跳躍が無証明。批評の「proxy 逃避」攻撃路を構造的に封じる。

---

## §結果

### 採用した理論核

**候補 (B) を採用**:

$$\kappa(\theta) := \|d(\Phi T)\|_g^2 = \frac{4}{\alpha^2}\|F\|_g^2$$

**理由**: 定理 5.1 のゼロ曲率条件をそのまま定量化。Appendix D line 1412-1441 のノルム分離と完全接続。

**experiment-level target** (§5.5 で必要な量):

$$\Xi_{\text{theory}}(\nu) := \operatorname{Var}_{u \sim \nu}[\kappa(\theta_u)]$$

`u` は turn (N=416) / trajectory (SWE-bench) / 6 座標 (HGK 実装) によって異なる。

### 4 estimator の定義

| estimator | 仮定 | 推定精度 | 備考 |
|:---|:---|:---|:---|
| Ξ_Var (N=416) | H1: 線形観測、i.i.d. ターン | bias=O(n⁻¹), var=O(n⁻¹) | unbiased + consistent |
| Ξ_Gini (SWE-bench) | H1': multiplicative 観測、lognormal | asymptotic unbiased | basis alignment 破れで lower bound に降格 |
| Ξ_CV (全保持対照) | H1'': lognormal、noise baseline 独立 | asymptotic unbiased | dΦ≈0 のとき Ξ_CV→0 (no-forgetting corollary) |
| Ξ_impl (229 CCL 式) | H1''': Bernoulli omission、6 座標 basis | coordinate-level consistent | basis alignment 破れで lower bound |

### SWE-bench N=500 全保持対照の再解釈

$$r(\Xi_{CV}, P) = -0.007, \quad p = 0.87$$

Fisher z 変換で予測帯域を計算: n=500 での SE = 1/√497 ≈ 0.045。
`r ∈ [-0.090, 0.076]` の 95% CI に -0.007 が含まれる。
→ 「ヌル結果」ではなく**境界条件の成功確認** (dΦ≈0 → Ξ→0 の予測と整合)。

### CKA・coherence の扱い

- **CKA-based Fisher ratio**: projected estimator として定義可能 (Φ 側 proxy) だが T 側の独立推定が欠ける → partial closure のみ
- **chunk coherence**: estimator ではなく G∘F 不動点の **post-distillation diagnostic**
- **τ**: proxy ではなく **experimental knob / instrument variable** (initial condition)

### SOURCE anomaly (検出)

現行草稿で `Ξ_theory` が 3 通りに overload:
- line 266: `Var(λ)` (experiment-level target)
- line 321: `Gini(p̄_1,...,p̄_6)` (coordinate-level theory)
- line 348: `Gini(spec(Σ))` (spectral lower bound)

→ 梁4 Phase 2 で `Ξ_coord,theory` / `Ξ_spec,proj` に改名して解消済み。
