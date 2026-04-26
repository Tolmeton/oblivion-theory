# P-V.6 強結合 benchmark 計画 v1

```typos
#prompt pv6-strong-coupling-benchmark-plan
#syntax: v8
#depth: L2

<:role: Paper V §6.8.4 実験 III を実行面に落とした benchmark 設計書 :>
<:goal: γ_Φ ≈ 0.86 の残余乖離が、FRG 截断誤差なのか、Paper IV 側の観測量定義なのか、スケール比 R の較正誤差なのかを判別する :>

<:context:
  - [file] /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文V_繰り込みは忘却である_草稿.md
  - [file] /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文V_繰り込みは忘却である.meta.md
  - [file] /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/14_忘却｜Lethe/EXPERIMENTS.md
  - [file] /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/14_忘却｜Lethe/experiments/exp0_structural_precision/exp0_design.yaml
  - [file] /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/14_忘却｜Lethe/experiments/exp2_cps0/exp2_design.yaml
  - [file] /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/14_忘却｜Lethe/experiments/oblivion_field_gaussian.py
/context:>
```

**確定日**: 2026-04-14  
**対象**: Paper V §6.8.4 実験 III  
**結論**: first cut は **Monte Carlo**、BMW は **昇格条件付き second phase**

**実行契約**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/experiments/P-V.6_強結合MCベンチマークプロトコル.md`

---

## 1. 何を解く実験か

解くべき問いは 1 つである。

> **γ_Φ ≈ 0.86 の残余乖離は、理論の truncation error なのか、それとも Paper IV 側の観測量定義 / スケール比 R / 可観測化の問題なのか。**

ここで BMW を最初に切ると、FRG 系列の内側を 1 段深くするだけになる。  
それでは「DE2 が足りない」のか「理論外の観測面がずれている」のかを分離できない。

したがって、**最初に必要なのはより深い solver ではなく、理論系列の外側に置かれた基準線**である。  
この役を担えるのが Monte Carlo である。

---

## 2. BMW ではなく MC から切る理由

| 観点 | MC first | BMW first | 判定 |
|:---|:---|:---|:---|
| benchmark 性 | FRG 系列の外側に基準線を置ける | FRG 系列の内側を延長するだけ | MC |
| 現在資産 | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/14_忘却｜Lethe/experiments` に実験設計の型がある | repo 内に BMW 実装資産は実質ない | MC |
| 失敗時の読解性 | 「DE2 で足りる / 足りない」を外部から判定できる | 失敗しても truncation と observable の混線が残る | MC |
| 実装コスト | 格子化と有限サイズ scaling に集中すればよい | 連続運動量依存 vertex の実装が必要 | MC |
| 次の一手の明確さ | MC が DE2 を超えたら BMW へ昇格できる | BMW 実装後も外部基準線がない | MC |

**決定**:

- **Phase 0-1 は MC**
- **BMW は Phase 2**
- **BMW の役割は benchmark ではなく、MC が示した残差の担い手を同定すること**

---

## 3. 判定ロジック

### 3.1 まず固定する比較面

比較する量は必ず同一面にそろえる。

- 1-loop
- 2-loop Padé
- LPA'
- DE2
- Monte Carlo
- 必要時のみ BMW

同一面とは、**同じ $n$、同じ observable 定義、同じ $\gamma_\Phi$ 変換規約**で比較するという意味である。  
この整列を壊すと、solver 比較が observation design 比較へ崩れる。

### 3.2 判定分岐

| 観測結果 | 読み | 次の一手 |
|:---|:---|:---|
| MC が DE2 と同程度で、両者とも 0.86 から遠い | FRG 截断ではなく Paper IV 側の可観測化が主因 | observable / R / calibration を再点検 |
| MC が DE2 を系統的に上回り、0.86 側へ寄る | truncation error が主因 | BMW へ昇格 |
| MC を再現できるのが momentum-dependent solver のみ | 運動量依存性が本質 | BMW を本命化 |
| MC 自体が安定せず finite-size drift が大きい | benchmark 面が未成熟 | lattice 設計を修正して再試行 |

---

## 4. 実験設計

### Phase 0: MC pipeline の基準化

**目的**: MC 実装が既知 universality class を壊していないことを確認する。

**対象**:

- 3D Ising または scalar φ⁴ lattice

**測るもの**:

- $\eta$
- $\nu$
- 有限サイズ scaling の安定性

**通過条件**:

- 既知 benchmark からのずれが許容帯に入る
- lattice size を増やしたときの drift が単調に収束する
- error bar の見積りが再標本化で破綻しない

**ここで落ちた場合**:

忘却場 lattice へは進まない。  
以後の結果は solver discrimination ではなく、単に MC 実装の故障になる。

### Phase 1: T-射影忘却場の MC 本走査

**目的**: strong-coupling 領域に外部 benchmark を置く。

**走査点**:

- $n = 3.0$
- $n = 2.9$
- $n = 2.78$
- $n = 2.7$
- $n = 2.68$

**候補モデル**:

1. T-射影を持つ離散化忘却場 lattice
2. 合成統計多様体を離散化した effective model

選定原則は 1 つである。  
**Paper V の $\gamma_\Phi$ 定義へ最短距離で写せる方を採る。**

**測るもの**:

- $\eta(n)$
- $\gamma_\Phi(n)$
- 固定点の有無
- finite-size scaling collapse
- 誤差棒と系統誤差

**比較対象**:

- 1-loop
- 2-loop Padé
- LPA'
- DE2

### Phase 2: BMW 昇格

**起動条件**:

- MC が DE2 を明確に上回る
- 0.86 近傍への接近が DE2 では説明できない
- 差分が運動量依存の欠落として読むのが最も自然

**目的**:

- MC と DE2 の差分を、運動量依存 vertex の欠落として説明できるかを検証する

**注意**:

BMW は「より正しい benchmark」ではない。  
**MC が置いた benchmark を、FRG 側でどこまで回収できるかを見る追跡 solver** である。

---

## 5. 成果物面

新規に作るべき実装面は以下で固定する。

| 面 | 役割 |
|:---|:---|
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/strong_coupling_mc_reference.py` | Phase 0 の既知 benchmark 再現 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/strong_coupling_mc_scan.py` | Phase 1 の $n$ 走査 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/strong_coupling_compare.py` | 1-loop / Padé / LPA' / DE2 / MC / BMW の同一面比較 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/results_strong_coupling/phase0_reference.json` | 既知 benchmark の通過記録 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/results_strong_coupling/phase1_scan.csv` | $n$ 走査の主要値 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/results_strong_coupling/phase1_analysis.md` | 判定文書 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/strong_coupling_bmw.py` | Phase 2 起動後のみ着手 |

---

## 6. 実行順

1. Phase 0 の既知 benchmark を通す  
2. 同じ observable 変換で Phase 1 の MC 走査を行う  
3. DE2 と MC の差分を判定表に流し込む  
4. 差分が truncation error と読める場合にのみ BMW を起動する  

この順を崩して BMW から入ることは、**benchmark ではなく solver 開発を先にやる**ことを意味する。  
今回の目的は solver 開発そのものではなく、`γ_Φ ≈ 0.86` の残余乖離の帰属判定である。  
よって順序を固定する。

---

## 7. 棄却 ledger

詳細な失敗時帰属表は `drafts/infra/experiments/P-V.6_強結合MC_failure_ledger.md` を正本とする。ここでは、benchmark 計画時点で棄却済みの大枝だけを固定する。

- 棄却案 1: **BMW first**
  - 棄却理由: FRG 系列の内側だけを延長しても、Paper IV 側の observable / R / calibration の問題と切り分けられない
- 棄却案 2: **DE2 の外挿だけで 0.86 を採用**
  - 棄却理由: 外挿は benchmark ではない。0.651 は手掛かりだが、判決ではない
- 棄却案 3: **0.86 を 0.46 側に弱めて paper close**
  - 棄却理由: これは問題解決ではなく射程縮小である

---

## 8. 現時点の決定

> **実験 III の第一手は Monte Carlo である。**
>
> **BMW は、MC が DE2 を超えたときにのみ起動する。**

これにより、実験 III は「より高次の理論を作る試み」ではなく、  
**0.86 乖離の帰属を判定する benchmark 計画**として閉じる。
