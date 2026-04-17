# origin/main 移行面

## 0. 基線

- ローカル研究面: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion`
- ローカル比較基準: `40e4e190b9d1b98fdbdab0f75d9479a4f0e4d552`
- リモート比較基準: `origin/main @ 9ed4e156354d8b35c6560f99f4e5fa68fd8f2dde`
- 共通祖先: なし
- 含意: 現在の `main` をそのまま `origin/main` に push する道はない。先に別 branch に上げ、そこで統合面を作る必要がある。

## 1. 差分の圧縮像

| 面 | `origin/main` | ローカル `HEAD` | 観測 |
|:--|:--|:--|:--|
| 公開契約面 | `README.md` `README.ja.md` `LICENSE` | `README.md` `.gitignore` | `README.md` は改変、`README.ja.md` と `LICENSE` はローカルに無い |
| 論文シリーズ | `papers/series/` 17 files | `drafts/series/` 25 files | remote の 17 題は全てローカルに対応物がある。ローカル側に meta と論文 XIV が増えている |
| 単発論文 | `papers/standalone/` 6 files | `drafts/standalone/` 27 files | remote の 6 題は全てローカルに対応物がある。`automath_bridge/` と補助草稿群がローカルのみ |
| 研究補助面 | なし | `calculations/` 53, `plans/` 21, `drafts/incubator/` 15, `drafts/infra/` 16 | remote には存在しない研究母体 |
| 実験面 | なし | `experiments/` 3202 files | 研究データとベンチ結果が公開面を圧倒している |
| 大型ベンダ面 | なし | `experiments/experiments/` 3108 files | 旧埋め込み Git を実体化した `swe-bench/experiments` 系コーパス |

差分集計:

- `HEAD` tracked files: 3365
- `origin/main` tracked files: 26
- tree diff: `A 3352 / D 13 / M 1 / R 12`

## 2. rename として回収できた公開面

Git が 90% 以上の類似として拾えたものは次の 12 本。

- `origin/main:papers/series/論文0_忘却の忘却_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文0_忘却の忘却_草稿.md`
- `origin/main:papers/series/論文III_Markov圏の向こう側_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文III_Markov圏の向こう側_草稿.md`
- `origin/main:papers/series/論文IV_なぜ効果量は小さいか_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文IV_なぜ効果量は小さいか_草稿.md`
- `origin/main:papers/series/論文IX_エントロピーは忘却である_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文IX_エントロピーは忘却である_草稿.md`
- `origin/main:papers/series/論文I_力としての忘却_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文I_力としての忘却_草稿.md`
- `origin/main:papers/series/論文VII_知覚は忘却である_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VII_知覚は忘却である_草稿.md`
- `origin/main:papers/series/論文V_繰り込みは忘却である_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文V_繰り込みは忘却である_草稿.md`
- `origin/main:papers/standalone/エッセイ_理解と予測の随伴.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/エッセイ_理解と予測の随伴.md`
- `origin/main:papers/standalone/レター_Inoué定理との合流_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/レター_Inoué定理との合流_草稿.md`
- `origin/main:papers/standalone/四則演算は忘却の選択である_たたき台.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/四則演算は忘却の選択である_たたき台.md`
- `origin/main:papers/standalone/抽象化の忘却的定式化_v1.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/抽象化の忘却的定式化_v1.md`
- `origin/main:papers/standalone/類推的自由エネルギー_草稿.md` → `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/類推的自由エネルギー_草稿.md`

## 3. 手動統合が必要な面

### 3.1 公開契約面

- `origin/main:LICENSE`
- `origin/main:README.ja.md`
- `origin/main:README.md` ← ローカルにも `README.md` はあるが内容が異なる

### 3.2 同題だが rename しきれなかった論文面

次の remote ファイルは、同題のローカルファイルは存在するが類似度 90% を超えず、自動 rename になっていない。

- `origin/main:papers/series/論文II_相補性は忘却である.meta.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文II_相補性は忘却である.meta.md`
- `origin/main:papers/series/論文II_相補性は忘却である_草稿.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文II_相補性は忘却である_草稿.md`
- `origin/main:papers/series/論文VIII_存在は忘却に先行する.meta.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する.meta.md`
- `origin/main:papers/series/論文VIII_存在は忘却に先行する_草稿.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md`
- `origin/main:papers/series/論文VI_行為可能性は忘却である_草稿.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VI_行為可能性は忘却である_草稿.md`
- `origin/main:papers/series/論文XIII_時空は忘却である_草稿.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XIII_時空は忘却である_草稿.md`
- `origin/main:papers/series/論文XII_速度は忘却である.meta.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XII_速度は忘却である.meta.md`
- `origin/main:papers/series/論文XII_速度は忘却である_草稿.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XII_速度は忘却である_草稿.md`
- `origin/main:papers/series/論文XI_プロンプトは忘却である_草稿.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.md`
- `origin/main:papers/series/論文X_ContextRotは忘却である_草稿.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文X_ContextRotは忘却である_草稿.md`
- `origin/main:papers/standalone/反証可能性は死んだ_エッセイ.md` ↔ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/反証可能性は死んだ_エッセイ.md`

## 4. ローカルだけにある増築面

### 4.1 シリーズ草稿の増築

`drafts/series/` の local-only は 8 files。

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文I_力としての忘却.meta.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.meta.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文V_繰り込みは忘却である.meta.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XIII_時空は忘却である.meta.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XIV_曲率は忘却の繰り上がりである.meta.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XIV_曲率は忘却の繰り上がりである_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.meta.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文X_ContextRotは忘却である.meta.md`

### 4.2 単発論文の増築

`drafts/standalone/` の local-only は 21 files。支配的なのは `automath_bridge/` 一式で、これは remote の現行公開面には存在しない。

主要な local-only:

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/T9自己診断反論マッピング.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.meta.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/automath_bridge/`

### 4.3 研究ワークベンチ

次は remote 公開面には現れない研究母体であり、`origin/main` に直送する面ではない。

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/plans/`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/incubator/`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/thermodynamic_correspondence_v3.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/Ξ計算_軌跡から不均一度.py`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/アーティファクト/`

注記:

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/experiments/` は 3108 files
- もともとは `https://github.com/swe-bench/experiments.git` の埋め込み Git だった
- Git メタデータは `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/.embedded-git-backups/experiments-experiments.git` に退避済み
- `.embedded-git-backups/` は `.gitignore` 済みで tracked ではない

## 5. 推奨移行プロトコル

### P1. まず branch を分ける

推奨:

- 現在の `HEAD` は research import 面として remote に新規 branch へ push する
- `origin/main` にはまだ触れない

安全な最初の一手:

```bash
git -C '/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion' \
  push origin HEAD:refs/heads/source-import-2026-04-17
```

### P2. 公開契約面を戻す

`origin/main` に残すべき最低限:

- `LICENSE`
- `README.ja.md`
- `README.md` の手動統合版

ここを戻さずに統合すると、公開 repo の法的・読者向け入口が壊れる。

### P3. `drafts` を source of truth とし、`papers` は投影面にする

推奨判断:

- source of truth は `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/`
- publish projection は `papers/series/` と `papers/standalone/`

理由:

- いまの `drafts/` には meta、増補、橋渡し草稿が混ざっている
- これを即 `papers/` に rename すると、研究母体と公開面の境界が消える
- 先に「公開するものだけを射影する」構造にした方が、以後の整理が一方向になる

### P4. 研究ワークベンチは main へ直送しない

非推奨:

- `experiments/` `calculations/` `plans/` `drafts/incubator/` `drafts/infra/` をそのまま `origin/main` に merge する

推奨:

- 研究面 branch を残す
- あるいは `research/` プレフィクスで隔離し、公開面とは別の README を置く

### P5. 手動統合対象を 3 束に分ける

1. 契約束: `README.md` `README.ja.md` `LICENSE`
2. canon 束: `papers/series/*` と `papers/standalone/*`
3. research 束: それ以外

この順に解くと、公開 repo の境界を壊さずに統合できる。

## 6. Negativa

採らない方がよい手:

- 現在の `main` を force push して `origin/main` を置換する
- 研究母体を削って remote の薄い形に合わせる
- `drafts/` を即座に `papers/` へ全面 rename し、source of truth を曖昧にする
- `experiments/experiments` を再び gitlink に戻す

## 7. 次の一手

最小コストで次にやるべきこと:

1. `source-import-2026-04-17` のような branch へ現在の `HEAD` を push する
2. `origin/main` 起点の統合 branch を別に切る
3. `LICENSE` と `README.ja.md` を戻す
4. `drafts -> papers` の publish projection ルールを決める
5. 研究面を main に入れるか、branch/prefix で隔離するかを決める
