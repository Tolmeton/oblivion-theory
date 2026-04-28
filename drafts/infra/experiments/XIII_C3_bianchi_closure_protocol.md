# E-XIII-C3-02 Protocol

**日付**: 2026-04-26
**skill**: `/pei` L2
**派生**: bare `/pei`。反証条件を前に置く MVP 型の文書実験として実行する。
**対象**: Paper XIII C3 / §8.2.1 O3
**問い**: contracted Bianchi identity `∇^μG_{μν}=0` を、stress-energy conservation を前提輸入せずに、Face Lemma 側の closure / syndrome conservation として翻訳できるか。

---

## S-0 / S-05 Source Intake

**SOURCE**

| source | 用途 |
|:---|:---|
| `drafts/series/論文XIII_時空は忘却である_草稿.md` §8 | O1-O4 と D1-D3 の現在形 |
| `drafts/リファレンス/FaceLemma.md` | Face Lemma の reader-facing 正本 |
| `drafts/incubator/FaceLemma_技術設計.md` | syndrome / coherence-defect / closure の backstage 正本 |
| `drafts/infra/experiments/XIII_C3_result.md` | E-XIII-C3-01 の prior result |
| `drafts/series/論文XIII_時空は忘却である.meta.md` §M5 / §M6 | C3 の現在状態 |

**TAINT / 要昇格**

標準 GR 事実としての contracted Bianchi identity、Schwarzschild exterior、FLRW case は、現段階では局所実験の background として使う。投稿耐性を持たせるには、次段で標準 GR source または symbolic calculation ledger に昇格させる。

[CHECKPOINT S-0/S-05]

---

## P-0 Prolegomena

**実験空間**

この実験は O3 だけを見る。Einstein 方程式の導出、係数 `8πG_N`、Jacobson / Verlinde の再読解、C1 四力統一、C4 `(3+1)` 発生は扱わない。

**仮説ソース**

E-XIII-C3-01 の結果:

```text
Riemann/holonomy = raw defect
Ricci/scalar = contracted defect
Einstein tensor = conserved coupling projection
```

この分割のうち、最後の `conserved coupling projection` が O3 で支えられるかを試す。

**盲点チェック**

| category | risk | 理由 |
|:---|:---:|:---|
| 実験設計 | LOW | O3 だけに閉じ、O4 以後を切り離している |
| 測定方法 | MED | 記号計算ではなく文書上の role-mapping 実験である |
| 確証バイアス | MED | C3 を救いたい方向の prior があるため、反証条件を明示する |
| スコープ | LOW | `G_{μν}` の役割選択に限定する |
| 可逆性 | LOW | 草稿本文を編集せず、実験 artifact と meta の状態台帳だけを更新する |

**ρ₀**: 3/5

[CHECKPOINT P-0/5]

---

## P-1 Experiment Protocol Design

**XYZ 仮説**

`Face Lemma = detectability`、`curvature = raw transport defect`、`contracted Bianchi = divergence-free projection` と三層に分ければ、`G_{μν}` は raw defect ではなく、Face 側で露出した syndrome を内容へ結合可能にする conserved projection として選ばれる。

**成功基準**

| id | success condition |
|:---|:---|
| S1 | raw curvature defect と `G_{μν}` を分離できる |
| S2 | `∇^μG_{μν}=0` を `∇^μT_{μν}=0` の輸入なしに geometry-side closure として読める |
| S3 | Face 側での役割が「syndrome projection の保存 / closure」として明示できる |
| S4 | O3 を O4 coupling や Einstein 方程式の導出と混同しない |

**反証条件**

| id | falsifier |
|:---|:---|
| F1 | Bianchi identity を GR の既知事実として反復するだけで、Face 側の役割が出ない |
| F2 | `∇^μT_{μν}=0` を先に仮定しないと `G_{μν}` の role が立たない |
| F3 | Riemann/holonomy と `G_{μν}` の差を説明できず、Schwarzschild exterior separator に再び落ちる |
| F4 | O3 から Einstein 方程式全体や係数まで言ってしまう |

**判定閾値**

MVP matrix の 5 probe のうち 4 probe 以上が S1-S4 と整合し、F1-F4 の hard fail が 0 なら、O3 は **role-level support** とする。1 hard fail でも出た場合、O3 は skeleton のまま維持する。

**ρ₁**: 4/4

[CHECKPOINT P-1/5]

---

## P-2 MVP Design

**実験タイプ**

文書実験 / role-mapping probe。数学的証明ではなく、C3 を次の証明実験へ進めるかを決める最小実験である。

**手順**

1. Face Lemma 側の階層を `detectability / closure / recoverability` に分ける。
2. GR 側の階層を `Riemann/holonomy / Ricci-scalar / Einstein tensor / stress-energy` に分ける。
3. 5 probe matrix で、`G_{μν}` が raw defect ではなく conserved projection として選ばれるかを見る。

**MVP チェック**

| criterion | result |
|:---|:---|
| 最小性 | O3 のみを検査するため、これ以上小さくすると `G_{μν}` の役割選択が見えない |
| 情報性 | pass なら O4 へ進む、fail なら C3 を skeleton に留めるため EIG は高い |
| 速度 | 文書実験として 1 turn で完了可能 |
| 可逆性 | 本文を直接編集しない |
| 独立性 | C1/C4 と独立に判定する |

**Skin-in-the-Game**

| result | action |
|:---|:---|
| 支持 | meta の C3 状態を O3 role-level support へ更新し、次を O4 coupling probe に置く |
| 棄却 | §8 の D2' 以上の強化を止め、C3 を skeleton として温存する |
| 不明 | 標準 GR source / symbolic calculation ledger を先に作る |

**ρ₂**: 5/5

[CHECKPOINT P-2/5]

---

## P-3 Execution

実行 artifact:

- `drafts/infra/experiments/XIII_C3_bianchi_closure_matrix.md`
- `drafts/infra/experiments/XIII_C3_bianchi_closure_result.md`

**環境**

```text
workspace: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion
mode: local document experiment
date: 2026-04-26
```

[CHECKPOINT P-3/5]

---

## P-4 Harvest

**判定**: 支持。ただし theorem-level closure ではなく role-level support。

**Surprise**

| axis | value |
|:---|:---|
| 方向 | 予測より一段低いが、棄却ではない |
| 大きさ | MED |
| 種類 | 型誤差 |

**学び**

1. `Bianchi = Face Lemma そのもの` では強すぎる。
2. Face Lemma は raw defect の detectability を与え、Bianchi はその defect を内容へ結合可能な conserved projection へ落とす closure 条件として読むべきである。
3. O3 は O4 の前提を作るが、O4 を代替しない。

**ρ₃**: MED

[CHECKPOINT P-4/5]

---

## PeQS

| dimension | status |
|:---|:---:|
| Domain Defined | PASS |
| Hypothesis Falsifiable | PASS |
| MVP Designed | PASS |
| Data Recorded | PASS |
| Surprise Harvested | PASS |
| Model Updated | N/A |

**総合**: 5/5 PASS

**次**: E-XIII-C3-03 として O4 coupling probe を切る。FLRW または Jacobson-style local patch を使い、`G_{μν}` と `T_{μν}` の等号が容器/内容整合として読めるかを試す。
