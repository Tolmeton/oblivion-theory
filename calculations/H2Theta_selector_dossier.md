# H2Theta selector dossier

作成日: 2026-04-26

役割: Paper II C4 (`H^2_{\Theta}` / Coherence Defect Lemma) の calculations 面に分散していた 6 文書を、削除なしで 1 本の索引兼圧縮正本候補へ束ねる。

対象ディレクトリ:

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations`

## 0. 判定核

`H^2_{\Theta}` は、「忘却 law に drift があるか」ではなく、局所 law のずれが大域的な付け替えで消えるか、消えない class として残るかを分ける selector surface である。

現時点の C4 は二重構造を持つ。

| 面 | 状態 |
|:--|:--|
| QM branch | Heisenberg 中心拡大を使う partial theorem branch。`H^2_{\Theta}` の最小非自明 witness |
| 一般 CPS branch | selector / lift / weak-package / guard-probe まで揃った conjectural canonical surface |

この dossier は、後者の conjectural branch を管理するための圧縮面である。本文を theorem に押し上げる文書ではない。

## 1. SOURCE roster

| 層 | source file | この dossier での役割 |
|:--|:--|:--|
| probe | `計算_QM_H2Theta最小インスタンス.md` | QM を残差側 / nontrivial side の witness として固定 |
| contrast | `計算_FTC_H2Theta対照例.md` | FTC を貼合側 / trivial side の witness として固定 |
| selector | `計算_H2Theta_selector条件面.md` | FTC/QM の差を selector の十分条件へ上げる |
| lift | `計算_H2Theta_selector_CPS内在化条件.md` | 外部語を CPS 公理語へ翻訳する |
| weak package | `計算_H2Theta_selector_package弱化テスト.md` | full package から必要な芯を削り出す |
| guard | `計算_H2Theta_selector_weakpackage反例探索.md` | 弱化しすぎた場合の failure mode と guard を固定 |
| meta sync | `drafts/series/論文II_相補性は忘却である.meta.md` | C4 の主張水準・統合履歴・著者決定面 |

## 2. 6 層スタック

| layer | 入力 | 変換 | 持ち越し |
|:--|:--|:--|:--|
| L1 probe | QM の中心拡大 | 交代双線形 2-cocycle が coboundary で消えないことを最小模型で読む | QM = 残差側 |
| L2 contrast | FTC の可縮区間模型 | forgetting law が global potential 由来の exact 1-cochain に落ちることを読む | FTC = 貼合側 |
| L3 selector | QM / FTC pair | 「drift の有無」ではなく「大域再定義で消えるか」を判定面にする | Candidate A/B |
| L4 CPS lift | 外部語 `contractible patching` / `alternating witness` | CPS-globalization atlas / CPS-obstruction witness へ翻訳 | Lift A/B |
| L5 weak package | full package | support-locality / generator-face sufficiency / witness-relative visibility で弱化 | Weak Lift A'/B' |
| L6 guard | A'/B' の弱化結果 | false trivialization / false obstruction を分離し guard を足す | Weak Lift A''/B'' |

この順番が重要である。QM と FTC は単なる例ではなく、selector の両極を作る probe pair である。

## 3. 二極の意味

| front-stage name | technical side | witness | 読み |
|:--|:--|:--|:--|
| 貼合側 | trivial side | FTC | 局所 law が global potential に吸収され、`[ω_{\Theta}] = 0` と読める |
| 残差側 | nontrivial side | QM | defect の交代成分が gauge で消えず、class 候補を残す |

重要なのは、FTC が「簡単だから消える」のではなく、貼合の整合が十分にあるから消えること。QM が「量子だから残る」のではなく、交代成分が coboundary で吸収されないから残ること。

## 4. 記号と最小定義

Paper II meta で固定済みの主定義:

```text
Z^2_Theta = ker d^2
B^2_Theta = im d^1
H^2_Theta = Z^2_Theta / B^2_Theta
```

直観:

局所的には足し合わせられる忘却 law がある。だが、その局所 law を全体の一つの law として貼り合わせようとしたとき、貼り合わせのずれが残る場合がある。その残りが `H^2_{\Theta}` の見ている面である。

## 5. Candidate chain

### 5.1 Selector Candidate A/B

| side | 条件 | 読み |
|:--|:--|:--|
| A: globalizable side | global potential + contractible patching | local mismatch は大域 1-cochain に吸収される |
| B: obstructed side | alternating witness + central extension | coboundary が対称成分しか殺せず、交代成分が残る |

この段階では CPS 内部語ではない。FTC/QM pair から抽出した外部条件面である。

### 5.2 Candidate Lift A/B

| side | CPS 内部語 | 読み |
|:--|:--|:--|
| Lift A | CPS-globalization atlas + zero holonomy | 貼合側を CPS 公理語で読む |
| Lift B | CPS-obstruction witness + irreducible orientation | 残差側を CPS 公理語で読む |

未定義の残り:

| 未定義面 | 必要な決定 |
|:--|:--|
| section の一般形 | CPS 内で局所 section をどう読むか |
| holonomy の一般形 | `CPS2 + CPS5` から中心的 drift 差をどう抽出するか |
| additive witness の一般形 | どの reduction を admissible witness と呼ぶか |
| faithful on defect support | defect が立つ support だけを見る条件をどう書くか |

### 5.3 Weak Lift A'/B'

| side | 弱化後の候補 | 削ったもの |
|:--|:--|:--|
| A' | support-local re-lift + generator-face zero holonomy | full cover / all faces |
| B' | support-local faithful witness + anti/symmetric separation | global faithful / full additive category / central extension 必須性 |

弱化の方向は正しいが、裸の A'/B' は弱すぎる。

### 5.4 Guarded Weak Lift A''/B''

| side | guard | 防ぐ failure |
|:--|:--|:--|
| A'' | support-saturated + triple-overlap-consistent + gauge-stable | generator hole / overlap deficiency / support instability |
| B'' | coboundary-conservative + boundary-closed + refinement-stable | witness artifact / boundary leakage / anti-symmetric projection failure |

FTC local model は A'' の guard probe を通る。QM minimal model は B'' の guard probe を通る。

## 6. 文書ごとの圧縮

### 6.1 QM minimal instance

SOURCE file:

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_QM_H2Theta最小インスタンス.md`

要点:

| 面 | 内容 |
|:--|:--|
| model | `V = R^2` の相空間平行移動群 |
| cocycle | `ω(u,v)=1/2(xp' - px')` |
| 判定 | `d^2ω=0` かつ `ω` は `im d^1` に落ちない |
| Paper II 読み | QM は `H^2_{\Theta}` の nontrivial candidate |
| guard | B'' = coboundary-conservative / boundary-closed / refinement-stable |
| front-stage | 残差側 |

未主張:

`H^2_{\Theta} != 0` がすべての CPS 圏で成り立つとは言わない。QM だけで selector theorem も言わない。

### 6.2 FTC contrast

SOURCE file:

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_FTC_H2Theta対照例.md`

要点:

| 面 | 内容 |
|:--|:--|
| model | 可縮な区間の FTC local model |
| law | `Theta` が global potential 由来の exact 1-cochain として読める |
| 判定 | obstruction class `[ω_Theta]` は立たない |
| Paper II 読み | FTC は trivial side / contrast probe |
| guard | A'' = gauge-stable / support-saturated / triple-overlap-consistent |
| front-stage | 貼合側 |

未主張:

すべての FTC 的状況で `H^2_{\Theta}=0` とは言わない。`H^2_{\Theta}=0` と recoverability を同一視しない。

### 6.3 selector 条件面

SOURCE file:

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_H2Theta_selector条件面.md`

要点:

| 面 | 内容 |
|:--|:--|
| problem | なぜ FTC は trivial side、QM は nontrivial side に寄るのか |
| A | global potential / contractible patching |
| B | alternating witness / central extension |
| theorem status | theorem candidate surface |
| blocker | CPS への lift、中間型分類、必要条件検証 |

採用:

selector の一行圧縮は、「drift があるか」ではなく、「drift が大域的再定義で消えるか」を見ること。

### 6.4 CPS 内在化条件

SOURCE file:

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_H2Theta_selector_CPS内在化条件.md`

要点:

| 外部語 | CPS 内部語 |
|:--|:--|
| contractible patching | CPS-globalization atlas + zero holonomy |
| alternating witness | CPS-obstruction witness + irreducible orientation |

採用:

FTC / QM を外部例のまま置かず、CPS 内部での witness として再配置する。

未定義:

site / topology、holonomy の一般抽出、admissible witness、defect support faithful 条件。

### 6.5 package 弱化テスト

SOURCE file:

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_H2Theta_selector_package弱化テスト.md`

要点:

| principle | 意味 |
|:--|:--|
| support-locality | defect に関係する support だけを見る |
| generator-face sufficiency | 全 face ではなく生成 face で足りるかを見る |
| witness-relative visibility | witness に対して見える defect に限定する |

採用:

full package に戻らず、guard 付き weak package へ進む。

### 6.6 weak-package 反例探索

SOURCE file:

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_H2Theta_selector_weakpackage反例探索.md`

要点:

| side | failure mode | guard |
|:--|:--|:--|
| A' | generator hole / overlap deficiency / support instability | support-saturated / triple-overlap-consistent / gauge-stable |
| B' | witness artifact / boundary leakage / anti/symmetric projection failure | coboundary-conservative / boundary-closed / refinement-stable |

採用:

`A'' / B''` は現時点の canonical guarded package。ただし本文語としてはまだ重い。

## 7. Paper II meta との同期状態

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文II_相補性は忘却である.meta.md` では、C4 は次の状態で固定されている。

| 項目 | 状態 |
|:--|:--|
| C4 主張水準 | QM verified partial theorem branch + 一般 CPS conjectural branch |
| canonical surface | `H^2_{\Theta}` |
| missing intermediate object | 整合担体 (`coherence carrier`) |
| front-stage pair | 貼合側 / 残差側 |
| backstage package | A'' / B'' |
| 次 blocker | 整合担体を本文語へ出すか、infra + meta に留めるか |

エージェント推奨として meta に残っている判断は、現時点では **infra + meta に留める** 方向である。本文へ出すなら、`A'' / B''` ではなく `整合担体` だけを 1-2 行で出すのが最小侵襲。

## 8. Negativa

この dossier から、次を主張してはいけない。

| 禁止する読み | 理由 |
|:--|:--|
| 任意の CPS 圏で `H^2_{\Theta} != 0` | QM witness は一般形の証明ではない |
| `H^2_{\Theta}=0` なら recoverable | obstruction class と回復可能性は同一ではない |
| FTC/QM pair から必要十分条件が出た | 現状は十分条件候補と guard extraction |
| `A'' / B''` は必要十分条件 | guard は failure mode 対策であり完全分類ではない |
| guard の各語を本文定義へ上げる | 一般定義がまだ重く、本文の主張水準を押し上げる |
| C4 を Face Lemma の置換として読む | C4 は Face Lemma の隣に置く次段補題 |
| drift と obstruction を混同する | drift があっても FTC のように exact なら obstruction ではない |

## 9. 後続削減の扱い

この dossier ができた後も、元の 6 文書は直ちに削除しない。

次の順で処理する。

| 順 | 処理 | 条件 |
|:--|:--|:--|
| 1 | Paper II meta からこの dossier への参照を追加 | 旧 6 本への参照は当面残す |
| 2 | 6 本それぞれに `absorbed by dossier` の短い注記を入れるか判断 | SOURCE の損失がないことを確認 |
| 3 | 旧 6 本の削除候補化 | 本文・meta・README の参照が dossier 経由になった後 |
| 4 | C4 整合担体 note との接続確認 | `drafts/incubator/C4_整合担体.md` を読み直してから |

## 10. 次の一手

現時点で進めるなら、次はこの dossier を Paper II meta の C4 donor 統合欄に追記する。まだ旧 6 本を消さない。

推奨順:

```text
H2Theta_selector_dossier.md を meta に追加
-> 旧 6 本の参照を dossier 経由へ寄せる
-> 旧 6 本を削除候補に落とす
```
