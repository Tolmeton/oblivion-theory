# H^2_Θ selector weak-package 反例探索

**作成日**: 2026-04-15  
**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_H2Theta_selector_package弱化テスト.md` で得た `Weak Lift A' / B'` が弱すぎて selector を壊していないかを調べ、必要なら最小 guard を抽出する。  
**結論の水準**: **counterexample surface / guard extraction note**。一般反例の存在はまだ証明しないが、破綻様式を固定する。

---

## 0. 何を反例と呼ぶか

弱化の判定で怖いのは、二種類の誤判定である。

### 0.1 A 側の誤判定

`Weak Lift A'` が成り立つので

```text
[ω_Θ] = 0
```

だと読んだが、実際には class が残っていた、という場合である。

これは

> **false trivialization**

である。

### 0.2 B 側の誤判定

`Weak Lift B'` が成り立つので

```text
[ω_Θ] ≠ 0
```

だと読んだが、実際には global coboundary として消えていた、という場合である。

これは

> **false obstruction**

である。

この note の仕事は、この二種類の壊れ方を明示し、  
`Weak Lift A' / B'` に何を足せば壊れにくくなるかを決めることである。

---

## 1. Weak Lift A' の壊れ方

`Weak Lift A'` は

> `support-local re-lift + generator-face zero holonomy`

だけで `[ω_Θ]=0` へ行こうとする。  
だが、これではまだ三つの穴がある。

### 1.1 A-1: generator hole failure

生成 face 集合 `Σ_x` が、局所比較のための生成系ではあっても、  
**cohomology class を殺すのに必要な 2-face 全体を張っていない** 可能性がある。

直感的にはこうだ。

- 基底三角形では全部 drift が閉じている
- だが、それらを貼った殻全体では閉じていない
- したがって局所 zero は見えても global triviality は出ない

これは「線形生成」と「class を消す生成」が同じではないことを意味する。

したがって、単なる `generator-face sufficiency` では弱い。  
必要なのは、

> **support-saturated generating family**

である。

つまり `Σ_x` は defect support の 2-dimensional shell を見失わない生成系でなければならない。

### 1.2 A-2: overlap deficiency failure

support-local section が存在しても、  
chart の重なりが pairwise 比較しか持たず、triple overlap の整合が抜けていると、

- 各 face 上では zero holonomy に見える
- だが貼り合わせ全体では Čech 的な 2-障害が残る

ということが起こりうる。

要するに、

> **pairwise closure は global closure を保証しない**

したがって trivial side には、

> **triple-overlap consistency**

が要る。

### 1.3 A-3: support instability failure

`supp(ω_Θ)` を gauge 後の representative で取ると、  
support 自体が取り方で動いてしまう。

すると、

- ある gauge では support-local trivialization がある
- 別の gauge ではその support の外側に defect がにじむ

ということが起こりうる。

したがって `support-locality` は、裸では弱い。  
必要なのは、

> **gauge-stable support**

である。

### 1.4 A 側の暫定 guard

以上から、`Weak Lift A'` に足すべき最小 guard は次の三つになる。

1. `Σ_x` が **support-saturated** である
2. atlas が **triple-overlap consistent** である
3. support が **gauge-stable** である

これをまとめて、trivial side の改訂版を次のように置く。

> **Weak Lift A'' (guarded).**  
> ある対象 `x` に対し、gauge-stable defect support を覆う support-local atlas があり、support-saturated generating face 集合の上で zero holonomy が triple-overlap consistent に成り立つなら、`[ω_Θ](x)=0` を示す候補として保持できる。

これはまだ theorem ではない。  
だが `A'` よりははるかに壊れにくい。

---

## 2. Weak Lift B' の壊れ方

`Weak Lift B'` は

> `support-local faithful witness + anti/symmetric separation`

だけで `[ω_Θ]≠0` へ行こうとする。  
だがこちらも三つの誤判定を抱える。

### 2.1 B-1: witness artifact failure

witness が defect support 上で faithful でも、  
その witness が **coboundary を coboundary として保存しない** なら、

- witness image では交代 defect が残って見える
- だが元の圏では global 1-cochain に吸収できる

ということが起こりうる。

つまり witness が強すぎると、

> **見えてはいけない障害を人工的に作る**

したがって必要なのは、単なる faithful ではなく、

> **coboundary-conservative witness**

である。

ここで conservative とは、「元で消えるものを像で偽の非零にしない」という意味である。

### 2.2 B-2: boundary leakage failure

faithful 性を support の内部だけで課すと、  
境界で起きる cancellation が見えないことがある。

すると、

- support の中では nontrivial に見える
- だが support の境界まで含めると coboundary として消える

ということが起こりうる。

したがって `support-local faithful` は、

> **boundary-closed support faithful**

まで強める必要がある。

### 2.3 B-3: anti/symmetric projection failure

交代成分と対称成分の分離も、  
projection の取り方に依存するだけなら危うい。

ある quotient や image でだけ alternating part が残り、  
refinement するとそれが対称 coboundary へ戻るなら、

それは class ではなく presentation artifact である。

したがって必要なのは、

> **refinement-stable anti/symmetric separation**

である。

### 2.4 B 側の暫定 guard

以上から、`Weak Lift B'` に足すべき最小 guard は次の三つになる。

1. witness が **coboundary-conservative** である
2. faithful 性が **boundary-closed support** 上で成り立つ
3. anti/symmetric separation が **refinement-stable** である

これをまとめて、nontrivial side の改訂版を次のように置く。

> **Weak Lift B'' (guarded).**  
> ある対象 `x` に対し、boundary-closed defect support 上で faithful かつ coboundary-conservative な witness があり、その像での anti/symmetric separation が refinement-stable なら、`[ω_Θ](x)≠0` を示す候補として保持できる。

これもまだ theorem ではない。  
だが `B'` の「local witness が見えたから即 obstruction」という短絡は外せる。

---

## 3. 反例探索の暫定結論

ここまでで言えることは明確である。

### 3.1 `Weak Lift A' / B'` は裸のままでは弱い

弱化そのものは正しかった。  
full package はやはり重すぎた。

だが、その削り方をそのまま theorem candidate にするのは危ない。  
理由は、

- A 側では false trivialization
- B 側では false obstruction

の両方が起こりうるからである。

### 3.2 ただし full package に戻る必要はない

必要なのは「元に戻すこと」ではなく、

> **最小限の guard を足して weak package を guarded package にすること**

である。

これにより selector の芯は依然として

- support-locality
- generator-face sufficiency
- witness-relative visibility

に置ける。  
ただしその各語は、guard 付きで読まれなければならない。

### 3.3 いまの最小候補

現時点の最小候補は次の二つである。

- `Weak Lift A''` = support-saturated + triple-overlap-consistent + gauge-stable trivial side
- `Weak Lift B''` = coboundary-conservative + boundary-closed + refinement-stable nontrivial side

これが、weak package の次の canonical 候補である。

---

## 4. まだ主張しないこと

1. `A'' / B''` が必要十分条件であるとは言わない  
2. 上の failure mode が exhaustive だとは言わない  
3. FTC/QM 以外の具体圏で既に `A'' / B''` を満たすとは言わない  
4. guard の各語 (`support-saturated`, `coboundary-conservative`, `refinement-stable`) の一般定義を本文へ上げない  
5. この note だけで本文 `§3.4.6` に補注を入れない

---

## 5. 次の一手

次にやるべきことは、一般証明ではなく **guard probe の同期** である。

1. 2026-04-15 時点で FTC note に `A''` の guard probe を追加し、FTC local model では `gauge-stable / support-saturated / triple-overlap-consistent` が自然に通ることを固定した  
2. 同日、QM note に `B''` の guard probe を追加し、QM 最小模型では `boundary-closed / coboundary-conservative / refinement-stable` が自然に通ることを固定した  
3. 次に決めるべきなのは、`A'' / B''` を guarded selector の canonical 名として残すか、それともさらに短い本文語へ圧縮するかである

私の判断では、いま本文へ上げる名前はまだない。  
guard probe は通ったが、本文侵入はその後でよい。
