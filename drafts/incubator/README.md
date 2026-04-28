# 忘却論 incubator index

**状態**: internal staging / proof seed and bridge note index
**入口**: `drafts/リファレンス/忘却論オンボーディング.md` §2.3 / §8.5 / §11.5
**置き場所**: `drafts/incubator/`

## 目的

`drafts/incubator/` は未整理物の常置場ではない。本文に入れるにはまだ強すぎる、または未成熟だが、弱めて捨てるべきではない核を隔離し、主張水準・昇格先・失敗条件を見える形で育てる作業面である。

この面に置く文書は、最低限どの型かを明示する。

| 型 | 役割 | 昇格先 |
|---|---|---|
| proof seed | 証明課題や補題候補を本文から切り出したもの | `drafts/series/` の本文 / appendix / `.meta.md` |
| bridge note | 論文間の橋、記号間の橋、物理・工学への橋 | `drafts/series/`, `drafts/リファレンス/統一記号表.md`, `drafts/リファレンス/モノグラフ構成設計.md` |
| technical design | 実験・計算・証明補助の設計 | `calculations/`, `experiments/`, appendix |
| draft embryo | 公開候補になる前の草稿胚 | `drafts/standalone/` または対象 series |
| legacy | 旧版・前史・復活原則なしの履歴 | 原則として昇格しない |

## 昇格ゲート

incubator から外へ出す前に、以下を埋める。

| gate | 問い |
|---|---|
| 主張水準 | 定理 / 命題 / 補題 / 推定 / 仮説 / 予想 / 実験的知見のどれか |
| 昇格先 | series / standalone / リファレンス / infra / calculations / experiments のどれか |
| SOURCE | 本文・外部原典・計算結果のどれに支えられているか |
| failure condition | 何が示されたら降格・棄却するか |
| 依存関係 | どの paper / OP / 記号表項目に依存するか |
| 戻し方 | 本文へ戻すとき、どの節・appendix・meta に入れるか |

昇格先が決まらない文書は、本文へ戻さない。`drafts/incubator/` 内でも、冒頭に「未定」と明示する。

## 現行 index

| 文書 | 型 | 現在の読み | 次の昇格候補 |
|---|---|---|---|
| `paper0_L6_4_A_filtration_seed.md` | proof seed | Paper 0 L6.4-A。式複雑度と証明長の二重 filtration を固定する舞台 | Paper 0 appendix / §6.4 footnote |
| `paper0_L6_4_BD_relative_homology_seed.md` | proof seed | Paper 0 L6.4-B/D。証明側成長上界と相対ホモロジー昇格 | Paper 0 appendix |
| `paper0_L6_4_C_independent_cycle_seed.md` | proof seed | Paper 0 L6.4-C。意味側独立 cycle 供給を 4 小補題へ分解する未証明 seed | Paper 0 appendix / §6.4 footnote |
| `加速度は忘却境界の曲率である_橋梁ノート.md` | bridge note | Paper I と Paper XII の速度・加速度・力をつなぐ。primitive は `II(W)` | Paper XII patch / 統一記号表 |
| `α_I_α_III_formal_bridge_草稿.md` | bridge note | `α_I` と `α_III` の formal bridge 候補 | 統一記号表 / Paper III-VIII-XII bridge |
| `FaceLemma_技術設計.md` | technical design | Face Lemma の符号理論対応・修復可能性設計 | calculations / appendix |
| `Face5Lemma_draft.md` | draft embryo | Face Lemma 周辺の独立草稿候補 | standalone or Paper II appendix |
| `Face5Lemma_draft.meta.md` | meta | `Face5Lemma_draft.md` の共同台帳 | draft と同期 |
| `C4_整合担体.md` | bridge note | C4 周辺の整合担体候補 | 対象 paper meta で昇格判断 |
| `lawvere_enriched_metric_draft.md` | proof seed | Lawvere / enriched metric 側の形式化 seed | Paper 0 / standalone |
| `大規模言語モデルの潜在意識_メタデータ.md` | meta / draft embryo | LLM 潜在意識稿の台帳面 | 対象本文の所在確認後に判断 |
| `正五角形_かける_σ_予想_10_落書きの種袋.md` | draft embryo | σ 予想の種袋 | standalone / calculations |
| `第10章_統合章_忘却の先行性_草稿.md` | draft embryo | 統合章候補。モノグラフ線に近い | モノグラフ構成設計 |
| `論文XII_C3c橋梁ノート.md` | bridge note | Paper XII C3c 周辺の橋梁 | Paper XII meta / 本文 |
| `legacy/力とは忘却である_v2.md` | legacy | Paper I 前史 | 原則として復活させない |

## よくある事故

### 常置場化

未成熟文書を置いた後、型・昇格先・failure condition を書かずに放置する状態。
復旧: 本 README の index に行を追加し、文書冒頭へ型と昇格先を書く。

### proof seed の本文偽装

seed を本文へ戻すとき、未解決条件を消して定理のように見せる状態。
復旧: 主張水準を統一記号表 §0.3 に合わせ、失敗条件を本文または meta に残す。

### bridge note の記号汚染

橋梁ノート内の暫定記号を、統一記号表へ通さず series 本文へ持ち込む状態。
復旧: `drafts/リファレンス/統一記号表.md` と `drafts/リファレンス/系列横断_記号衝突台帳_2026-04-26.md` を確認する。

## 次の整理候補

1. 各 incubator 文書の冒頭に `型 / 昇格先 / failure condition` を足す。
2. Paper 0 L6.4-C seed の R2 counting route を toy model 化する。
3. `Face5Lemma_draft.md` と `FaceLemma_技術設計.md` の責務を分ける。
4. `第10章_統合章_忘却の先行性_草稿.md` をモノグラフ構成設計へ戻すか、独立 draft として保持するか決める。
