# H^2_Θ selector package 弱化テスト

**作成日**: 2026-04-15  
**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_H2Theta_selector_CPS内在化条件.md` で導入した `CPS-globalization atlas` と `CPS-obstruction witness` が強すぎる package になっていないかを試験する。  
**結論の水準**: **weakening note / theorem candidate surface**。必要十分条件はまだ主張しない。

---

## 0. 何を削りたいのか

直前の lift note では、selector を CPS 内部語へ持ち上げるために次の package を置いた。

- `CPS-globalization atlas + zero holonomy`
- `CPS-obstruction witness + irreducible orientation`

これらは安全だが、まだ強すぎる可能性がある。  
もし過剰なら、本文へ上げた瞬間に

> 「FTC と QM に合わせて後付けで作った package ではないか」

という反論を招く。

したがって今やるべきことは、

> **selector に本当に必要な芯だけを残し、飾りの条件を削ること**

である。

---

## 1. 弱化の guiding principle

`H^2_{\Theta}` が見ているのは、圏全体ではない。  
見ているのは

- 照合面が実際に立つ部分
- その面上で現れる defect
- その defect が gauge で消えるかどうか

だけである。

したがって次の原則が立つ。

### 原則 A: support-locality

判定に不要な領域の data は削ってよい。  
必要なのは **defect support** とその近傍だけである。

### 原則 B: generator-face sufficiency

zero / nonzero の判定に必要なのは、全 2-simplex ではなく  
`B_1^{ver}` や defect support を生成する **基底的な照合面** だけでよい。

### 原則 C: witness-relative visibility

nontriviality を示すのに必要なのは、圏全体での faithful 性ではなく、  
**その defect が見えている範囲で faithful** であれば足りる可能性が高い。

---

## 2. trivial side の弱化

### 2.1 何が強すぎたか

`CPS-globalization atlas` では、

- `K` 全体を覆う chart
- 各 chart での local section
- 全ての照合面での zero holonomy

を要求していた。

だが `[ω_Θ]=0` を示すために必要なのは、通常そこまで多くない。

### 2.2 弱化 1: full cover → defect-support cover

`K` 全体を覆う必要はない。  
必要なのは、`ω_Θ` が非自明になりうる face を含む部分だけである。

したがって

```text
{U_i} covers K
```

は、

```text
{U_i} covers supp(ω_Θ)
```

へ弱化できる候補がある。

FTC では実際、primitive を考えるべきなのは区間全体というより、積分を比較する path support で十分である。

### 2.3 弱化 2: global local-sections → support-local sections

左随伴由来の section も、圏全域で要るとは限らない。  
必要なのは、support 上で局所 law を re-lift できることだけである。

したがって

> 「対象全体で局所 section がある」

は、

> **「defect support の近傍で局所 section がある」**

へ弱化できる候補がある。

### 2.4 弱化 3: all faces → generating faces

zero holonomy を全ての 2-simplex に課すのも強すぎる。  
`ω_Θ` の zero/nonzero は線形だから、生成系で消えていれば十分な可能性が高い。

したがって

> **全照合面で zero holonomy**

は、

> **`B_1^{ver}` あるいは defect support を生成する face 集合 Σ_x で zero holonomy**

へ弱化できる候補がある。

### 2.5 Weak Lift A'

以上をまとめると、trivial side の候補 package は次まで削れる。

> **Weak Lift A'.**  
> ある対象 `x` に対し、defect support を覆う局所 chart と support-local section があり、さらに生成的照合面集合 `Σ_x` の上で zero holonomy が成り立つなら、`[ω_Θ](x)=0` を示すには十分である可能性が高い。

ここで残っている芯は、

- 同一起源
- 局所再構成
- 架橋
- 生成 face 上での zero holonomy

の 4 つだけである。

---

## 3. nontrivial side の弱化

### 3.1 何が強すぎたか

`CPS-obstruction witness` では、

- `K_x` 全体への witness functor
- witness 上での faithful 性
- additive target
- irreducible orientation

を要求していた。

だが nontriviality を示すのに本当に必要なのは、

> **対称 coboundary と向き付き defect を見分けられるだけの視界**

である。

### 3.2 弱化 1: global faithful → faithful on defect support

圏全体や `K_x` 全体で faithful である必要はない。  
必要なのは、defect が住んでいる支持の上で射を混同しないことだけである。

したがって

> **witness 全域で faithful**

は、

> **defect support 上で faithful**

へ弱化できる候補がある。

### 3.3 弱化 2: additive category 全体 → additive image only

target が巨大な加法圏である必要もない。  
必要なのは、witness の像の上で

- 和が定義できる
- 対称成分と交代成分を比較できる

ことだけである。

したがって

> **加法的 target category**

は、

> **witness image 上の局所加法構造**

へ弱化できる候補がある。

### 3.4 弱化 3: central extension は必須ではない

中心拡大は非常に強い witness だが、必須とは限らない。  
本体は `ω` が gauge で消えないことだから、

- central extension は **一つの十分 witness**
- それ以外の alternating witness でもよい

と読む方が自然である。

### 3.5 弱化 4: full orientation package → orientation modulo symmetric coboundaries

必要なのは「向き」があること一般ではなく、

> **その向き付き defect が、対称な coboundary と同一化できない**

ことだけである。

したがって irreducible orientation 条件は、

> **witness image 上で、defect の交代成分が対称 coboundary へ落ちない**

という形まで削れる。

### 3.6 Weak Lift B'

以上をまとめると、nontrivial side の候補 package は次まで削れる。

> **Weak Lift B'.**  
> ある対象 `x` に対し、defect support 上で faithful な witness があり、その像の上で defect の交代成分が対称 coboundary に吸収されないなら、`[ω_Θ](x)≠0` を示すには十分である可能性が高い。

ここで残っている芯は、

- support-local faithful
- A/B 二脚の区別
- 向き付き defect
- 対称 coboundary との非同一化

の 4 つだけである。

---

## 4. 何を削れなかったか

弱化しても、まだ削れない芯がある。

### 4.1 trivial side で削れないもの

1. **架橋の存在**  
   比較写像がなければ patching そのものが定義不能
2. **support 上の局所再構成**  
   再構成がなければ `Θ` を globalize する意味がない
3. **生成 face 上の zero holonomy**  
   これが消えなければ trivialization は崩れる

### 4.2 nontrivial side で削れないもの

1. **defect support 上の可視性**  
   witness がそこで射を混同したら class 判定不能
2. **A/B 二脚の向きの分離**  
   これがないと交代性が読めない
3. **対称 coboundary との差の保持**  
   ここが消えると obstruction は単なる gauge artifact に戻る

---

## 5. FTC と QM に対する再判定

この弱化版で両極を読み直すと、FTC/QM はより自然になる。

### FTC

FTC に必要なのは、

- path support 近傍で primitive が取れること
- 比較すべき生成 face で積分差が閉じること

だけである。

したがって `CPS-globalization atlas` の full package は過剰で、  
**Weak Lift A' で十分そうだ** という見通しが立つ。

### QM

QM に必要なのは、

- シンプレクティック defect が見える support 上で faithful な witness
- 交代成分が対称 coboundary に吸収されないこと

だけである。

したがって central extension は便利だが、  
**Weak Lift B' の方が canonical surface に近い**。

---

## 6. 次の theorem candidate

弱化後の theorem candidate は次の形になる。

### Weak Lift Candidate A'

`support-local re-lift + generator-face zero holonomy`
→ `[ω_Θ]=0`

### Weak Lift Candidate B'

`support-local faithful witness + anti/symmetric separation`
→ `[ω_Θ]≠0`

この形なら、FTC/QM に過剰適合した package から一歩離れられる。

---

## 7. まだ言ってはいけないこと

1. Weak Lift A' / B' が必要条件でもあるとは言わない  
2. 生成 face の選び方が canonical だとはまだ言わない  
3. support-local faithful が常に構成できるとは言わない  
4. FTC/QM 以外のドメインでも同じ弱化が通るとはまだ言わない  
5. この弱化テストだけで本文補注へ直行しない

---

## 8. 次の一手

次にやるべきことは 2 つである。

1. **weak package の反例探索**  
   2026-04-15 時点で `calculations/計算_H2Theta_selector_weakpackage反例探索.md` を追加し、`Weak Lift A' / B'` の false trivialization / false obstruction を分けて記述した。現時点の読みでは、裸の `A' / B'` は弱すぎるため、`A'' / B''` の guard 付き版まで上げて扱うのが安全である

2. **本文侵入の最小化**  
   もし guard probe を通るなら、本文には full package でなく guarded weak package 名だけを補注で入れる方が Kalon である

私の判断では、まだ 1 が先だ。  
いまは package を足す段階ではなく、**削っても壊れない芯に必要な guard を見切る段階**にある。
