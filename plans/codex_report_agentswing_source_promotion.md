# AgentSwing SOURCE 昇格レポート — 2026-04-26

## §1 成果核

Paper X 側で Paper X 本文要約に留まっていた AgentSwing 参照を、arXiv source TeX/PDF 由来の SOURCE へ昇格した。対象は Appendix case study、aligned context-management results、strategy-transition matrix である。

編集対象は `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/agentswing_ref_data.yaml` のみ。Paper X 本体は触っていない。

## §2 SOURCE

| 対象 | SOURCE |
|:---|:---|
| arXiv record | `https://arxiv.org/abs/2603.27490` |
| arXiv source | `https://arxiv.org/e-print/2603.27490` |
| aligned results | `table/01_aligned_results.tex` |
| case studies | `table/03_app_cast.tex` |
| transition matrices | `pic/transition_matrix_1x3.pdf` |
| appendix description | `sections/8_appendix.tex` |
| public GitHub probe | `https://github.com/Alibaba-NLP/DeepResearch` |

## §3 昇格内容

| 面 | 旧状態 | 新状態 |
|:---|:---|:---|
| Case 1 | Paper X embedded summary | arXiv TeX の Mando case に修正。Turn 23 で `$tupid Young` clue、KLN 選択、Turn 31 で `Mando` answer。 |
| Case 2 | Paper X embedded summary | arXiv TeX の live-crickets case に修正。PDF extraction loop 後に DA 選択、alternative endpoint で `live crickets` answer。 |
| Table 2 | Paper X 要約由来値 | `table/01_aligned_results.tex` の exact counts / eta / rho / Pass@1 / average turns に置換。 |
| Figure 9 | Paper X の近似値 | `transition_matrix_1x3.pdf` の vector labels から 3x3 exact matrix を抽出。 |
| 未取得 flags | 原典 PDF 未取得 | arXiv source は取得済み。raw per-turn logs / plotting CSV / implementation は未取得へ更新。 |

## §4 検証

```bash
curl -L --fail --silent --show-error https://arxiv.org/e-print/2603.27490 -o /tmp/agentswing_2603_27490_source
tar -xf /tmp/agentswing_2603_27490_source -C /tmp/agentswing_src
pdftotext -bbox-layout /tmp/agentswing_src/pic/transition_matrix_1x3.pdf /tmp/transition_bbox.html
```

TeX 表は `table/01_aligned_results.tex` と `table/03_app_cast.tex` を直接読んだ。Figure 9 は `pdftotext -bbox-layout` でラベルと座標を取り、3 つの 3x3 matrix として復元した。

## §5 残余

AgentSwing の raw per-turn experiment logs と評価 JSON はまだ無い。arXiv source にも public GitHub `Alibaba-NLP/DeepResearch` main branch probe にも、AgentSwing named module / raw log は見つからなかった。

したがって OP-X-6 はまだ「実測完了」ではない。今回の到達は、Paper X の引用土台を `Paper X embedded summary` から `AgentSwing arXiv source` へ上げた段階である。

## §6 次

次の実化操作は、更新済み `agentswing_ref_data.yaml` を入力にして Drift 合成レポートを再計算すること。旧 `codex_report_handoff_drift.md` は、旧 YAML の Table 2 値を前提にしているため stale として扱う。
