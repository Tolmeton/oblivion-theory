# E-XIII-C3-03 Protocol

**日付**: 2026-04-26
**skill**: `/pei` continuation, L2
**対象**: Paper XIII C3 / §8.2.1 O4
**問い**: FLRW の最小 case で、`G_{μν}` と `T_{μν}` の等号を、容器/内容の非対称整合条件として読めるか。

---

## S-0 / S-05 Source Intake

**SOURCE**

| source | 用途 |
|:---|:---|
| `drafts/series/論文XIII_時空は忘却である_草稿.md` §2.2 | Einstein 方程式を容器/内容の非対称射影として読む C2 |
| `drafts/series/論文XIII_時空は忘却である_草稿.md` §8.2.1 | O1-O4 の proof obligations |
| `drafts/series/論文VIII_存在は忘却に先行する_草稿.md` §3.4 / §5.1-§5.2 | 成立場/居住状態/規定射と `F=mg` 的な容器/内容動力学 |
| `drafts/infra/experiments/XIII_C3_bianchi_closure_result.md` | O3: `G_{μν}` = conserved coupling projection |
| `drafts/infra/experiments/XIII_C3_case_matrix.md` | FLRW を O4 probe として残した prior |

**今回 SOURCE 化したもの**

| source | 用途 |
|:---|:---|
| `drafts/infra/experiments/XIII_C3_flrw_symbolic_ledger.md` | flat FLRW metric に対する Einstein tensor / divergence / perfect fluid conservation の symbolic run |

**TAINT / 要昇格**

FLRW metric と perfect fluid stress-energy の選択は標準 GR 背景であり、この実験では symbolic ledger によって局所 SOURCE 化する。ただし投稿水準では、標準 GR textbook または論文参照で補強する。

[CHECKPOINT S-0/S-05]

---

## P-0 Prolegomena

**実験空間**

O4 coupling だけを見る。ここでは Einstein 方程式の完全導出、係数 `8πG_N` の値、宇宙定数 `Λ`、曲率パラメータ `k`、Jacobson / Verlinde は扱わない。flat FLRW metric と perfect fluid を最小 probe とする。

**仮説ソース**

E-XIII-C3-02 の結果:

```text
Einstein tensor = conserved coupling projection
```

O4 では、この projection が内容側 `T_{μν}` と同じ slot に入り、容器の形が内容量に固定されるかを見る。

**盲点チェック**

| category | risk | 理由 |
|:---|:---:|:---|
| 実験設計 | MED | FLRW は高対称 case なので、一般 GR の証明にはならない |
| 測定方法 | LOW | symbolic run で tensor components と divergence を直接出す |
| 確証バイアス | MED | C3 を進めたい prior があるため、hard fail 条件を先に置く |
| スコープ | LOW | O4 の coupling slot だけを見る |
| 可逆性 | LOW | 本文編集なし。artifact と meta 更新のみ |

**ρ₀**: 3/5

[CHECKPOINT P-0/5]

---

## P-1 Experiment Protocol Design

**XYZ 仮説**

flat FLRW metric で計算した `G_{μν}` が、perfect fluid `T_{μν}` と同じ diagonal slot に入り、`G_{00}` が内容密度 `ρ`、`G_{ii}` が圧力 `p` の slot と対応し、かつ `div G=0` が `div T=0` の conservation slot を要求するなら、O4 は少なくとも一つの GR インスタンスで container/content consistency として読める。

**成功基準**

| id | success condition |
|:---|:---|
| S1 | `G_{μν}` が FLRW symmetry の下で `T_{μν}=diag(ρ,p a^2,p a^2,p a^2)` と同じ diagonal slot に落ちる |
| S2 | `G_{00}` が scale factor の一階情報、`G_{ii}` が一階/二階情報を持ち、内容密度/圧力の二つの slot を区別できる |
| S3 | `div G=0` と `div T=0` が同じ conservation condition に接続する |
| S4 | 結果を `G=T` の完全導出や係数の導出と誤認しない |

**反証条件**

| id | falsifier |
|:---|:---|
| F1 | FLRW で `G_{μν}` が perfect fluid `T_{μν}` と同じ slot に入らない |
| F2 | `G_{μν}` が内容側の `ρ,p` を区別できない |
| F3 | `div G=0` から内容側 conservation slot が出ず、O3 と O4 が切れる |
| F4 | O4 が通ったことにして C1/C4 または係数 `8πG_N` まで拡張してしまう |

**判定閾値**

symbolic ledger で S1-S3 が観測され、F1-F4 の hard fail が 0 なら **O4 local support**。ただし `flat FLRW only` なので theorem-level closure ではなく、single-instance support とする。

**ρ₁**: 4/4

[CHECKPOINT P-1/5]

---

## P-2 MVP Design

**実験タイプ**

symbolic calculation + role-mapping probe。

**手順**

1. flat FLRW metric `diag(-1,a(t)^2,a(t)^2,a(t)^2)` から `G_{μν}` を計算する。
2. mixed divergence `∇_μG^μ_ν` を計算する。
3. perfect fluid `T_{μν}=diag(ρ,p a^2,p a^2,p a^2)` の mixed divergence を計算し、conservation slot を比較する。
4. `G_{μν}=κT_{μν}` と置いた場合に、container-side equations が content density / pressure の slot にどう写るかを role-mapping する。

**MVP チェック**

| criterion | result |
|:---|:---|
| 最小性 | flat FLRW + perfect fluid だけ。O4 の最小 case |
| 情報性 | pass なら C3 が一例で O4 へ進む。fail なら C3 は O3 で止まる |
| 速度 | 1 symbolic run |
| 可逆性 | artifact-only |
| 独立性 | C1/C4 を使わない |

**Skin-in-the-Game**

| result | action |
|:---|:---|
| 支持 | C3 §M6 を O4 local support へ更新し、次を source promotion / non-FLRW stress test に置く |
| 棄却 | C3 は O3 role-level support までで停止 |
| 不明 | textbook source と symbolic check の拡張を先に行う |

**ρ₂**: 5/5

[CHECKPOINT P-2/5]

---

## P-3 Execution

実行 artifact:

- `drafts/infra/experiments/XIII_C3_flrw_symbolic_ledger.md`
- `drafts/infra/experiments/XIII_C3_flrw_coupling_matrix.md`
- `drafts/infra/experiments/XIII_C3_flrw_coupling_result.md`

**環境**

```text
workspace: /home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion
python: python
sympy: 1.14.0
metric: flat FLRW diag(-1, a(t)^2, a(t)^2, a(t)^2)
date: 2026-04-26
```

[CHECKPOINT P-3/5]

---

## P-4 Harvest

**判定**: O4 local support。

**Surprise**

| axis | value |
|:---|:---|
| 方向 | 予測通り。ただし射程は flat FLRW に限定 |
| 大きさ | LOW |
| 種類 | 精度誤差 |

**学び**

1. FLRW では `G_{00}` が content density slot、`G_{ii}` が pressure slot に対応する形で出る。
2. `div G=0` と perfect fluid の `div T=0` は同じ conservation slot に入り、O3 から O4 への橋になる。
3. ただしこれは `G=κT` の係数導出ではなく、container/content consistency の一例である。

**ρ₃**: LOW

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

**次**: E-XIII-C3-04。`flat FLRW` の高対称性を越え、source promotion と non-FLRW stress test を行う。候補は `(a)` 標準 GR source ledger、`(b)` Schwarzschild interior / TOV、`(c)` Jacobson-style local patch。
