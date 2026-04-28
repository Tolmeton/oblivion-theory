# calculations リファクタ分類台帳

作成日: 2026-04-26

この台帳は、`calculations/` 配下の文書を削除なしで分類し、後続の統合・移動・削減を安全に進めるための作業入口である。

正本ディレクトリ:

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations`

## 0. 判定核

`calculations/` は公開シリーズの入口ではなく、計算ノート、証明パッチ、数値実験レポート、SOURCE ledger を置く補助面である。現状は 73 本の Markdown と 6 本の Python、1 本の JSON が混在しており、補助面としては過密である。

削減の方向は妥当。ただし、本文・meta から donor として参照されている文書、外部 commit / Lean source / 数値証拠を含む文書、実験スクリプトと対になっている文書は、統合先と参照修復ができるまで削除しない。

## 1. 分類ラベル

| ラベル | 意味 | 後続処理 |
|:--|:--|:--|
| A: source ledger | SOURCE、外部 commit、Lean 行番号、数値表、反証履歴を保持する文書 | 残す。統合する場合も SOURCE 部分を失わない |
| B: dossier merge | 同一主題の連作で、1 本の dossier にまとめると scan path が短くなる文書 | 統合候補。統合後に旧文書を削減候補へ移す |
| C: relocation candidate | 計算面より `drafts/リファレンス/`, `plans/`, `materials` などが自然な文書 | 移動候補。移動前に参照を全修復 |
| D: scratch / intermediate | 作業ログ、横断スキャン、パッチ案、精読ログ | 要約抽出後に退避・削除候補 |
| E: executable package | `.py` / `.json` と対になった再実行可能な計算単位 | スクリプトと出力を一体で保持 |

## 2. 優先統合クラスター

| 優先 | 目標 dossier | 現在の対象 | 判定 | 理由 |
|:--|:--|:--|:--|:--|
| P0 | `automath_dossier` | automath / Problem 10 / q5 / q6q7 / q10 / Issue #38 / sector parity / SF 由来 | A+B | 外部 source と donor 解釈が濃く、参照数も多い。最初に正本化する価値が高い |
| P0 | `H2Theta_selector_dossier.md` | QM / FTC / selector / CPS 内在化 / package 弱化 / weakpackage 反例 | A+B | 作成済み。Paper II meta から連続参照される 6 本を、削除なしで 1 本の圧縮面へ束ねた |
| P1 | `C6_P6_dossier` | C6 Path A/B/C/統合/差分、`_p6_intermediate/` | B+D | 旧名参照が多い。統合と参照修復を同時に行う必要がある |
| P1 | `忘却場_数値計算_dossier` | Phase2、2D、αΘ、αc、Θ、界面、第二の力、収束改善、CPS 場理論 | B | 数値計算の系列が分散している。統合で大幅に減る |
| P1 | `PaperVIII_6.7.14_dossier` | accumulation law、Route A、証明圧、η/Ep/boundary | B | 6.7.14 周辺の分析面が複数文書に分裂している |
| P2 | `Face補題_dossier` | Face 補題の証明修正、ホモロジー厳密化 | A+B | proof patch と厳密化を二重管理している |
| P2 | `AgentSwing_dossier` | AgentSwing 接続、不可逆性予測 | B+C | Paper X / experiments 側へ接続するほうが自然 |
| P2 | `CPS_YM_Gauge_dossier` | CPS-Gauge、CPS-YM、CW、三未踏、CPSspan | A+B | Paper V donor 群。本文/meta 反映後に統合できる |

## 3. ファイル別分類

### 3.1 automath / Paper XIV / Problem 10 系

| 分類 | ファイル | 処理 |
|:--|:--|:--|
| A | `構想_automath_第一障害可視化閾値.md` | automath 系の hub。保持 |
| A | `考察_automath_Kq定義_noe.md` | K_q ontology annex。保持し、dossier に吸収 |
| A | `考察_automath_Problem10_reduction_map.md` | Problem 10 reduction map。保持し、dossier に吸収 |
| A | `調査_問題十エー_積分_持ち上げ.md` | integral lift Iteration 2。保持し、dossier に吸収 |
| E | `計算_問題十エー_積分_持ち上げ.py` | 上記の計算スクリプト。文書と対で保持 |
| A | `考察_自動数学_セクター_偶奇_診断.md` | sector parity diagnostic。保持し、dossier に吸収 |
| A | `調査_automath_q5符号反転とPaperIII_Z2接続.md` | q=5 source ledger。保持 |
| A | `調査_automath_q6q7_probe.md` | q=6/7 proxy。保持。ただし proxy であることを dossier で明示 |
| E | `計算_automath_q67_probe.py` | q=6/7 probe script。保持 |
| A | `調査_自動数学_キュー10_スペクトル_周期性.md` | q=10 spectral 判定。保持し、棄却 ledger として残す |
| A | `調査_自動数学_課題三八_監査吸収.md` | Issue #38 吸収。保持 |
| A | `調査_エスエフ_符号_反転_由来.md` | SF sign flip 由来。保持 |
| E | `計算_エスエフ_符号_反転_由来.py` | SF sign flip script。保持 |
| B | `提案_エスエフ_調査結果の_遊学_反映_草稿群_ルーカス_整列_双対_路線.md` | 反映案。dossier の proposal 節へ統合 |
| B | `調査_automath_H1H2H3固化メモ.md` | 返信前メモ。要点だけ dossier へ吸収 |
| B | `考察_自動数学_全問_外部_ルーカス_障害.md` | 未投稿内部メモ。dossier に吸収し、外向き判断を明示 |

### 3.2 H2Theta / Paper II selector 系

| 分類 | ファイル | 処理 |
|:--|:--|:--|
| A+B | `H2Theta_selector_dossier.md` | 2026-04-26 作成。6 本の索引兼圧縮正本候補。旧文書はまだ削除しない |
| A+B | `計算_QM_H2Theta最小インスタンス.md` | QM 側の非自明候補。dossier へ統合 |
| A+B | `計算_FTC_H2Theta対照例.md` | FTC 側の対照例。dossier へ統合 |
| B | `計算_H2Theta_selector条件面.md` | selector 条件面。dossier の中核へ |
| B | `計算_H2Theta_selector_CPS内在化条件.md` | CPS 翻訳面。dossier へ統合 |
| B | `計算_H2Theta_selector_package弱化テスト.md` | package 弱化。dossier へ統合 |
| B | `計算_H2Theta_selector_weakpackage反例探索.md` | 反例探索。dossier の failure mode 節へ |

### 3.3 C6 / P6 / 統一表 系

| 分類 | ファイル | 処理 |
|:--|:--|:--|
| B | `考察_シー六_力学的導出_経路エー.md` | Path A。C6 dossier へ |
| B | `考察_シー六_力学的導出_経路ビー.md` | Path B。C6 dossier へ |
| B | `考察_シー六_力学的導出_経路シー.md` | Path C。C6 dossier へ |
| B | `考察_シー六_力学的導出_統合.md` | 統合判定。C6 dossier の正本候補 |
| B | `考察_シー六_版零_2_1_提案_差分.md` | v0.2.1 差分。採否だけ残して統合 |
| E | `計算_シー六_転送_変分_探査.py` | C6 probe script。保持 |
| C+D | `_p6_intermediate/エフ_1_統一表_版0_2_修正_提案_ジー_3_混成路線.md` | 中間提案。要約後に削減 |
| D | `_p6_intermediate/ピー六_ソース_台帳.md` | source ledger だが孤立。C6/P6 dossier へ吸収 |
| D | `_p6_intermediate/根拠付け_候補の横断スキャン結果.md` | 横断スキャン。要約抽出後に削減 |
| D | `_p6_intermediate/論文二_全体_走査.md` | Paper II scan。必要な negative findings だけ残す |

### 3.4 忘却場 / 数値計算 系

| 分類 | ファイル | 処理 |
|:--|:--|:--|
| B | `Phase2_計算レポート統合版.md` | 統合版だが周辺文書と再統合 |
| B | `計算_2D完全解_忘却場.md` | 数値 dossier へ |
| B | `計算_αΘ結合系2D解.md` | 数値 dossier へ |
| B | `計算_αc界面の直接生成.md` | 数値 dossier へ |
| B | `計算_カテゴリカル分布上のΘ.md` | 数値 dossier へ |
| B | `計算_界面の幅とエネルギー.md` | 数値 dossier へ |
| B | `計算_第二の力の局在形状.md` | 数値 dossier へ |
| B | `計算_収束改善.md` | Phase2 修正提案を数値 dossier へ |
| B | `計算集約_CPS場理論.md` | 数値 dossier の集約候補 |
| E | `β_λブリッジ検証.py` | script。関連 report と対で保持 |

### 3.5 Paper VIII / 6.7.14 / 基礎公理 系

| 分類 | ファイル | 処理 |
|:--|:--|:--|
| B | `考察_PaperVIII_6.7.14_accumulation_law最小公理_lys.md` | Paper VIII dossier へ |
| B | `考察_PaperVIII_6.7.14_routeA_作用原理導出_lys.md` | Paper VIII dossier へ |
| B | `考察_PaperVIII_6.7.14_証明圧固定_lys.md` | Paper VIII dossier へ |
| B | `考察_論文八_6_7_14_エータ_イーピー_境界独立性_詳析.md` | Paper VIII dossier へ |
| B | `考察_eta_Ep区別_lys.md` | Paper VIII dossier か記号表へ |
| B | `考察_basefiber公理_lys.md` | Paper VIII dossier か記号表へ |
| B | `考察_theta_alpha累積公理_lys.md` | Paper VIII dossier か記号表へ |
| B | `考察_Deltad_alpha弱対応_lys.md` | Paper VIII dossier か記号表へ |

### 3.6 CPS / Gauge / YM / Paper V 系

| 分類 | ファイル | 処理 |
|:--|:--|:--|
| A+B | `構成_CPS-Gauge関手.md` | Paper V donor。CPS/YM/Gauge dossier へ |
| A+B | `計算_CPS-YM関手構成.md` | Paper V donor。CPS/YM/Gauge dossier へ |
| A+B | `計算_CW導出_UΘ.md` | Paper V donor。CPS/YM/Gauge dossier へ |
| B | `計算_三未踏踏破.md` | donor 要素だけ抽出して統合 |
| B | `考察_CPSspan_Bridge対応表_lys.md` | CPS/YM/Gauge dossier か記号表へ |
| B | `証明_sectoralA_canonical_liftとlocal_full.md` | sectoralA dossier へ |
| B | `証明_sectoralA_evπのfaithful性.md` | sectoralA dossier へ |
| B | `考察_sectoralA_補題束の足場.md` | sectoralA dossier の導入へ |

### 3.7 Paper I / Face / CM / AgentSwing 系

| 分類 | ファイル | 処理 |
|:--|:--|:--|
| A | `CKA_KLブリッジ.md` | Paper I donor。保持。実験 script 側の旧小文字参照も確認 |
| A+B | `Face補題_証明修正.md` | Face 補題 dossier へ |
| A+B | `Face補題_ホモロジー厳密化.md` | Face 補題 dossier へ |
| A+B | `証明_CM戦略の圏論的定式化.md` | Paper X donor。保持し、CM dossier 化 |
| B | `調査_AgentSwing忘却Hyphē接続.md` | AgentSwing dossier へ |
| B | `予測_AgentSwing不可逆性テーゼ.md` | AgentSwing dossier へ |

### 3.8 参照・提案・精読・その他

| 分類 | ファイル | 処理 |
|:--|:--|:--|
| C | `構成_忘却論定数辞書_版零_1.md` | `drafts/リファレンス/` 候補。計算面から移す前に参照修復 |
| C | `構成_オイラー等式_注釈版_版零_1.md` | 注釈・構成面。定数辞書と統合候補 |
| C | `構成_オイラー等式_忘却論散文版_版零_1.md` | 散文版。注釈版へ吸収候補 |
| C | `リファレンス_シーシーエルと化学の構造対応.md` | `drafts/リファレンス/` または Materials 候補 |
| C | `計算_化学的同型_忘却の元素論.md` | 化学対応 dossier にまとめる |
| C | `統一表_場と要素_メモ.md` | 記号表・対応表へ吸収 |
| C | `調査_圏論的基礎における存在.md` | Materials / reference 候補 |
| C | `SUPO消化記録_2025-10_2026-03-25.md` | research digest。calculations から移す候補 |
| C | `発表戦略_忘却関手の射影.md` | `plans/` 候補 |
| D | `精読_精読台帳.md` | 精読 ledger。要約抽出後に退避 |
| D | `精読レポート_論文I_II_III.md` | 精読 report。反映済みなら削減 |
| D | `論文II_v1.2_パッチ.md` | patch document。本文/meta 反映確認後に削減 |
| E | `problem12_h3plus_refit.md` / `problem12_h3plus_refit.py` / `problem12_h3plus_refit.json` | 一体の実行パッケージとして保持 |

## 4. 参照修復キュー

外部文書から `calculations/` への参照には、旧英字名・旧ローマ字名・旧日本語化前後の混在が残っている。統合や削除より先に、少なくとも以下を解決する。

| stale 参照 | 現行候補 |
|:--|:--|
| `calculations/考察_C6_力学的導出_統合.md` | `calculations/考察_シー六_力学的導出_統合.md` |
| `calculations/考察_C6_力学的導出_PathA.md` | `calculations/考察_シー六_力学的導出_経路エー.md` |
| `calculations/考察_C6_力学的導出_PathB.md` | `calculations/考察_シー六_力学的導出_経路ビー.md` |
| `calculations/考察_C6_力学的導出_PathC.md` | `calculations/考察_シー六_力学的導出_経路シー.md` |
| `calculations/構成_忘却論定数辞書_v0.1.md` | `calculations/構成_忘却論定数辞書_版零_1.md` |
| `calculations/考察_automath_sector_parity_diagnostic.md` | `calculations/考察_自動数学_セクター_偶奇_診断.md` |
| `calculations/考察_自動数学_ケーキュー定義_認識.md` | `calculations/考察_automath_Kq定義_noe.md` |
| `calculations/考察_自動数学_問題十_縮約_写像.md` | `calculations/考察_automath_Problem10_reduction_map.md` |
| `calculations/調査_Problem10a_integral_lift.md` | `calculations/調査_問題十エー_積分_持ち上げ.md` |
| `calculations/計算_Problem10a_integral_lift.py` | `calculations/計算_問題十エー_積分_持ち上げ.py` |
| `calculations/調査_sf_sign_flip_由来.md` | `calculations/調査_エスエフ_符号_反転_由来.md` |
| `calculations/提案_sf_lucas_aligned_反映drafts.md` | `calculations/提案_エスエフ_調査結果の_遊学_反映_草稿群_ルーカス_整列_双対_路線.md` |
| `calculations/調査_automath_q10_spectral_periodicity.md` | `calculations/調査_自動数学_キュー10_スペクトル_周期性.md` |
| `calculations/cka_kl_bridge.md` | `calculations/CKA_KLブリッジ.md` |
| `calculations/sap_20260421_arithmetic_euler_sigma.md` | `calculations/精読_精読台帳.md` または `calculations/精読レポート_論文I_II_III.md`。要確認 |
| `calculations/_p6_intermediate/F1_unified_modification_proposal.md` | `calculations/_p6_intermediate/エフ_1_統一表_版0_2_修正_提案_ジー_3_混成路線.md` |
| `calculations/_p6_intermediate/Paper2_full_scan.md` | `calculations/_p6_intermediate/論文二_全体_走査.md` |

## 5. 削減手順

1. この台帳を入口にして、P0 の `automath_dossier` と `H2Theta_selector_dossier` から作る。
2. 参照修復キューを解消する。旧名参照が残っている間は削除しない。
3. dossier に吸収した旧文書には、削除前に「吸収先」「吸収日」「残した SOURCE 範囲」を記録する。
4. `.py` / `.json` と対になっている文書は、再実行単位として保持する。文書だけ削って script を孤立させない。
5. `_p6_intermediate/` は最後に処理する。中間 scan の negative findings は、C6/P6 dossier に抽出してから削る。

## 6. 現時点の削減目標

Markdown 73 本を、最終的には以下の active surface へ圧縮する。

| surface | 目標本数 |
|:--|:--|
| automath dossier + source ledgers | 3-5 |
| H2Theta selector dossier | 1-2 |
| C6/P6 dossier | 1-2 |
| 忘却場数値計算 dossier | 1-2 |
| PaperVIII 6.7.14 dossier | 1 |
| Face 補題 dossier | 1 |
| CPS/YM/Gauge dossier | 1-2 |
| AgentSwing / CM dossier | 1-2 |
| reference / plans / materials への移動 | 5-8 |
| scratch/intermediate 退避または削除 | 残さない |

目標は「情報を捨てる」ことではなく、SOURCE と donor の射を保ったまま、入口の数を減らすことである。
