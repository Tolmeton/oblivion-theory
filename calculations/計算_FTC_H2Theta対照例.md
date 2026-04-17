# FTC における H^2_Θ 非障害の対照例

**作成日**: 2026-04-15  
**役割**: Paper II `§3.4.6 Coherence Defect Lemma` の canonical surface (`H^2_{\Theta}`) に対し、FTC を **non-obstructed side** として固定するための計算ノート。  
**結論の水準**: **probe / contrast note**。Paper II 本文の一般 theorem 化はまだ行わない。

---

## 0. 何をやるか

QM では、局所 forgetting law の mismatch が nontrivial class を残しうる候補が立った。  
FTC 側では逆に、最小模型ではその mismatch が **global law に吸収される** ことを示したい。

ここで欲しいのは次の一点である。

> **FTC の最小模型では、Drift はあっても `H^2_{\Theta}` の obstruction にはならない。**

これが立つと、

- QM = obstructed candidate
- FTC = non-obstructed contrast

という pair が初めて揃う。

---

## 1. 最小モデル

FTC の基本舞台として、**可縮な区間**

```text
I = [a,b] ⊂ R
```

を取る。

対象は点 `x ∈ I`、射は向き付き区間

```text
γ_xy : x → y
```

と読む。  
直感的には、「点から点へどれだけ量が積み上がったか」を記録する path category の最小模型である。

ここで `h : I → R` を連続関数とし、その原始関数 `F` を取る:

```text
F'(x) = h(x)
```

FTC の核心は

```text
∫_x^y h(t)dt = F(y) - F(x)
```

である。

---

## 2. 大域 0-cochain から生まれる forgetting law

各点に値を割り当てる 0-cochain

```text
Λ(x) := F(x)
```

を考える。

このとき、各射 `γ_xy` に対し 1-cochain

```text
Θ(γ_xy) := ∫_x^y h(t)dt
```

を定めると、FTC により

```text
Θ(γ_xy) = Λ(y) - Λ(x)
```

となる。

つまり FTC の forgetting law は、この最小模型では最初から

```text
Θ = d^0 Λ
```

という **global potential 由来の exact 1-cochain** になっている。

ここが QM との最初の分岐点である。  
QM では mismatch が 2-cocycle class 候補へ上がるが、FTC の最小模型では law 自体がすでに global potential から来ている。

---

## 3. 2-cocycle は立つか

Paper II の向きに合わせて、合成可能な 2-step

```text
x --γ_xy--> y --γ_yz--> z
```

に対し

```text
(d^1 Θ)(γ_xy, γ_yz)
 = Θ(γ_yz) - Θ(γ_xz) + Θ(γ_xy)
```

を考える。

FTC による区間積分の加法性から

```text
Θ(γ_xz) = Θ(γ_xy) + Θ(γ_yz)
```

なので、

```text
(d^1 Θ)(γ_xy, γ_yz) = 0
```

である。

したがって、FTC の最小模型では

```text
ω_Θ := d^1 Θ = 0
```

であり、

```text
[ω_Θ] = 0 ∈ H^2_Θ
```

となる。

言い換えると、局所 forgetting law は存在するが、それは **大域 law にきれいに持ち上がる**。  
照合面は立っても、埋め戻せない殻は残らない。

---

## 4. 積分定数 C はなぜ obstruction ではないか

ここが最重要である。

FTC には確かに

```text
∫ ∘ d = id + C
```

という Drift がある。  
だがこの `C` は、QM の中心拡大におけるような nontrivial class ではない。

`C` の意味は、

- 原始関数は定数だけずらしても同じ微分を与える
- したがって primitive の選択には gauge freedom がある
- しかし区間 `I` では基点を一つ固定すれば、その自由度は大域的に吸収できる

ということである。

つまり FTC で失われるのは

> **埋め戻せない大域障害**

ではなく、

> **基点選択で吸収できる gauge ambiguity**

である。

この意味で、FTC の Drift は Face Lemma の detectability を支えていても、Coherence Defect Lemma の obstruction までは上がらない。

---

## 5. 局所 primitive の貼り合わせで見る

別の言い方をしておく。

区間 `I` を開集合 `U_i` で被覆し、各 `U_i` 上で primitive `F_i` を取るとする。  
すると重なり `U_i ∩ U_j` 上で

```text
F_j - F_i = c_ij
```

は定数になる。

可縮な区間では、この定数差は三重重なりでも

```text
c_jk - c_ik + c_ij = 0
```

を満たし、しかも一つの基点を固定すれば全部吸収できる。

直感的には、

- 局所 primitive の間に「ずれ」はある
- だがそのずれは patch ごとの定数差にすぎない
- 三角形どうしを貼っていっても、新しいねじれ class は生まれない

ということである。

だから FTC 側では、local law は global law に閉じる。

---

## 6. Paper II への翻訳

この計算から言えるのは次の 3 点である。

1. FTC の最小模型では `Θ` は global potential から来る exact 1-cochain であり、obstruction class は立たない  
2. したがって `∫∘d = id + C` の Drift を、そのまま `H^2_{\Theta} \neq 0` と読んではならない  
3. `H^2_{\Theta}` は「Drift があるかどうか」ではなく、「その Drift が大域的再定義で消えるかどうか」を分ける判定子として読むべきである

これで Paper II の reading は sharpen される。

- Face Lemma: 3射で照合面が立つ
- FTC: その面上の law は global potential に吸収される
- QM: その面上の law が nontrivial class 候補を残しうる

したがって `H^2_{\Theta}` は装飾ではなく、**FTC と QM を分ける selector** として働く。

---

## 7. A'' guard probe

直前の反例探索 note では、trivial side を裸の `A'`

```text
support-local re-lift + generator-face zero holonomy
```

のままでは弱く、少なくとも

- `support-saturated`
- `triple-overlap-consistent`
- `gauge-stable`

という guard を足した `A''` まで上げる必要があると読んだ。  
この節では、FTC の最小 local model がその guard を自然に満たすかを見る。

### 7.1 gauge-stable support

FTC の最小模型では、global potential は

```text
Λ(x) = F(x)
```

であり、gauge freedom は

```text
F \mapsto F + C
```

という定数ずらしに限られる。  
この操作は `Θ = d^0Λ` を全く変えない。

したがって FTC local model では、

> defect support は gauge で動くどころか、global potential を取った時点で空に潰れる

この意味で `gauge-stable support` は最も強く満たされる。

### 7.2 support-saturated generating family

FTC では comparison face は、順序付き triple

```text
x \to y \to z
```

の加法性だけで尽きる。  
区間 `I` は 1 次元で、任意の composable path はこうした ordered triple の貼り合わせに還元される。

したがって、ここでの生成 face は

> 比較面を作る face 全体そのもの

として取れてしまう。  
「生成系はあるが class を殺すのに足りない」という A-1 型の破綻は、この local FTC 模型では起きにくい。

### 7.3 triple-overlap consistency

局所 primitive を `F_i` と書くと、重なりでの差は

```text
F_j - F_i = c_ij
```

という定数になる。  
三重重なりでは

```text
c_jk - c_ik + c_ij = 0
```

が成り立つので、pairwise closure がそのまま triple closure に持ち上がる。

FTC local model では、A-2 型の

> pairwise では閉じるが、三重重なりで Čech 的障害が残る

という壊れ方は出ない。

### 7.4 FTC での暫定判定

したがって、この note の射程に限れば FTC は

> `Weak Lift A''` を自然に満たす trivial side の witness

として読める。

ここで重要なのは、FTC が「簡単だから trivial」なのではなく、

> global potential があり、support が gauge でぶれず、triple overlap でも patching が閉じる

から trivial だということである。

この意味で FTC は `A''` の **guard probe 合格例** になる。

front-stage の語彙では、FTC は **貼合側** と呼ぶ。  
ここで言いたいのは「障害がない」ことより、**局所 law が一つの global law に貼り合わさる** ことの方である。

---

## 8. まだ言ってはいけないこと

ここでも negativa は強い。

1. これで「すべての FTC 的状況で `H^2_{\Theta}=0`」とは言わない  
2. 可縮な区間ではなく、周期を持つ多様体や global de Rham 問題まで一気に一般化しない  
3. `H^2_{\Theta}=0` だから recoverable だ、とは言わない  
4. FTC の Drift `C` と Coherence Defect class を混同しない  
5. QM 側の nontrivial 候補が、これだけで本文 theorem に昇格したとは言わない

特に 2 は重要である。  
円周 `S^1` のように period が残る場面では、primitive の global existence 自体が崩れうる。  
このノートが扱うのは **FTC の最小 local model** であって、全 de Rham 文脈ではない。

---

## 9. 何が進んだか

進んだのは 5 点である。

1. `H^2_{\Theta}` に対する **trivial side** が FTC で固定された  
2. `∫∘d = id + C` の Drift と `H^2_{\Theta}` obstruction が別物だと明確になった  
3. QM note と対にして、`H^2_{\Theta}` が selector であるという読みに足場ができた  
4. Paper II の canonical surface を、存在候補だけでなく**対照候補**でも支えられるようになった
5. `Weak Lift A''` の guard が FTC local model では自然に満たされることが見え、guard 付き trivial side が抽象語のままではなくなった

---

## 10. 次の一手

次にやるべきことは 2 つである。

1. **`A'' / B''` を本文語へ圧縮するか決める**  
   2026-04-15 時点で FTC/QM の両側で guard probe は通った。次は `support-saturated` や `coboundary-conservative` のような calculation 語を、そのまま残すのか、あるいは本文用の短い語へ圧縮するのかを決める

2. **guarded selector を本文へどこまで上げるか決める**  
   いまは calculations + meta + infra に留めるのが安全だが、guard 名が圧縮できるなら、`§3.4.6` へ 1-2 行の補注を入れる余地が出る

ここで初めて、

> FTC = 貼合側  
> QM = 残差側

という比較面が立つ。
