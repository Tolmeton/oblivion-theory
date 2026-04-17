# QM における H^2_Θ 最小インスタンス

**作成日**: 2026-04-14  
**役割**: Paper II `§3.4.6 Coherence Defect Lemma` の canonical surface (`H^2_{\Theta}`) に対し、最初に叩くべき具体例を QM に固定するための計算ノート。  
**結論の水準**: **probe / calculation note**。Paper II 本文の一般 theorem 化はまだ行わない。

---

## 0. 何をやるか

やることは限定する。

1. QM の相空間平行移動群 `V = R^2` 上に、非自明な 2-cocycle があることを最小計算で示す  
2. それが Paper II の `H^2_{\Theta}` canonical surface の**第一候補**であることを確認する  
3. ただし、これをもって「すべての CPS 圏で `H^2_{\Theta} ≠ 0`」とは言わない

つまりここで欲しいのは、一般定理ではなく

> **QM には少なくとも、Coherence Defect Lemma を担いうる古典的な 2-cocycle class が実在する**

という最小の存在証拠である。

---

## 1. 最小モデル

Paper II の QM インスタンスは

- `f = x̂`
- `g = p̂`
- `h = [x̂, p̂] = iℏ`

という Face Lemma triple を持つ。

Coherence Defect の最小候補を作るには、作用素環そのものへ突っ込むより、まず **位相空間の平行移動群**

```text
V := R^2
u = (x, p), v = (x', p')
u + v = (x + x', p + p')
```

を取るのが最短である。

この `V` は可換群であり、局所 forgetting law の mismatch があるなら、それは group 2-cocycle として最も見えやすい。

---

## 2. 2-cocycle の候補

`V = R^2` 上の交代双線形形式

```text
ω(u, v) := 1/2 (x p' - p x')
```

を考える。

これは位相空間の標準シンプレクティック形式の離散化そのものである。

直感:

- `x` だけでも `p` だけでもこの値は出ない
- 2つの方向を同時に見たときだけ nonzero になる
- したがって、これは「単一 face の law」ではなく「face の貼り合わせで初めて出るねじれ」に対応する

---

## 3. cocycle 条件

Paper II の `d^1 Θ(f,g) = Θ(g) - Θ(g∘f) + Θ(f)` に合わせ、加法群 `V` 上の 1-cochain `λ : V → R` に対し

```text
(d^1 λ)(u, v) = λ(v) - λ(u + v) + λ(u)
```

と置く。

同様に 2-cochain `ω` に対する 2-cocycle 条件は

```text
(d^2 ω)(u, v, w)
 = ω(v, w) - ω(u + v, w) + ω(u, v + w) - ω(u, v)
```

で与えられる。

ここで `ω` は双線形だから

```text
ω(u + v, w) = ω(u, w) + ω(v, w)
ω(u, v + w) = ω(u, v) + ω(u, w)
```

である。これを代入すると

```text
d^2 ω
= ω(v,w) - [ω(u,w)+ω(v,w)] + [ω(u,v)+ω(u,w)] - ω(u,v)
= 0
```

となる。

したがって

```text
ω ∈ Z^2(V; R)
```

である。

---

## 4. なぜ coboundary ではないか

ここが最小核である。

任意の 1-cochain `λ : V → R` に対し、`V` が可換群であることから

```text
(d^1 λ)(u, v)
= λ(v) - λ(u + v) + λ(u)
= λ(u) - λ(v + u) + λ(v)
= (d^1 λ)(v, u)
```

すなわち **任意の coboundary は対称** になる。

一方、上で定めた `ω` は

```text
ω(v, u) = -ω(u, v)
```

を満たす **交代的** 2-cochain である。

対称な 2-cochain と交代的な 2-cochainは、`ω = 0` の場合を除いて一致しえない。したがって

```text
ω ∉ B^2(V; R) = im(d^1)
```

である。

ゆえに

```text
[ω] ≠ 0 ∈ H^2(V; R)
```

が従う。

この一点で、QM には **局所 law を global law に畳み込めない非自明 class の最小模型** があることがわかる。

---

## 5. Heisenberg 群との接続

この `ω` を使うと、`V = R^2` の中心拡大

```text
H = R^2 × R
```

に群法

```text
(u, s) · (v, t) = (u + v, s + t + ℏ ω(u, v))
```

を入れられる。

これは Heisenberg 群の実形である。

意味:

- `ω = 0` なら拡大は split し、中心項はただの飾りになる
- `[ω] ≠ 0` なら拡大は split せず、中心項は本物の障害物になる

この中心項が量子力学では **非可換性の実在** として観測される。

Paper II の記号へ戻すと、

- `carry defect` = 局所的に現れる mismatch の representative
- `H^2_{\Theta}` = その mismatch が再定義で消えるかどうかを決める class

であり、QM ではその class が「消えない」側へ振れている候補になる。

---

## 6. [x̂, p̂] = iℏ との接続

作用素レベルでは

```text
[x̂, p̂] = iℏ
```

である。

Weyl 形式に移すと、位相空間平行移動の projective 乗法則に中心位相が乗り、その位相の指数の中身がちょうど上の `ω(u,v)` になる。

したがって `ℏ` はここで

> **局所 law の mismatch を scale する係数**

として現れる。

ただし、このノートの射程では

> **`ℏ` が `H^2_{\Theta}` の生成元そのものである**

とまではまだ言わない。ここで固定するのは、あくまで

> **`ℏ ω` が nontrivial class の最小候補を与える**

という水準までである。

---

## 7. Paper II への翻訳

この計算から、Paper II `§3.4.6` に対して次だけが言える。

1. `H^2_{\Theta}` という canonical surface は、少なくとも QM の古典的中心拡大の語彙と噛み合う
2. `coherence-defective` を「局所 forgetting law の大域持ち上げ障害」と読む方向には、具体的模型がある
3. Face Lemma (`im ∂_2`) と Coherence Defect Lemma (`H^2_{\Theta}`) を別層に分ける方針は、QM でも自然である

---

## 8. B'' guard probe

直前の反例探索 note では、nontrivial side を裸の `B'`

```text
support-local faithful witness + anti/symmetric separation
```

のままでは弱く、少なくとも

- `coboundary-conservative`
- `boundary-closed`
- `refinement-stable`

という guard を足した `B''` まで上げる必要があると読んだ。  
この節では、QM の最小模型がその guard を自然に満たすかを見る。

### 8.1 boundary-closed support

この note の最小模型では、defect は

```text
ω(u,v) = 1/2 (x p' - p x')
```

であり、`V = R^2` の加法構造全体の上で定義される。  
ここでは support は局所 patch の内部に閉じ込められておらず、最初から

> 位置と運動量の二方向を同時に含む全相空間方向

の上で閉じている。

したがって、B-2 型の

> support の内部では nontrivial に見えるが、境界を含めると消える

という leakage は、この最小模型では起こりにくい。  
QM 最小模型は `boundary-closed support` の probe として読める。

### 8.2 coboundary-conservative witness

この模型では witness を、まずは `V` 自身の加法群構造とその上の Weyl / Heisenberg projective law に取ればよい。

重要なのは、`V` が可換群であるため、

> 任意の coboundary は最初から対称

だという事実である。  
したがって witness 側で nontrivial に見えるためには、元の段階で既に「対称 coboundary に落ちない」ことが必要になる。

言い換えると、この最小模型の witness は

> 元で消えるものを、像で偽の交代 defect に化けさせない

という意味で `coboundary-conservative` に振る舞う。

### 8.3 refinement-stable anti/symmetric separation

`ω` は交代双線形形式であり、任意の線形 refinement や座標変換の下でも

- 交代性は交代性のまま
- 対称 coboundary は対称のまま

保たれる。

ここで問題にしている separation は、presentation の偶然ではなく、

> 双線形形式の対称/交代分解そのもの

に乗っている。  
したがって B-3 型の

> 粗い quotient では交代に見えるが、refinement すると対称へ戻る

という壊れ方は、この最小 QM 模型では起こりにくい。

### 8.4 QM での暫定判定

したがって、この note の射程に限れば QM は

> `Weak Lift B''` を自然に満たす nontrivial side の witness

として読める。

ここで大事なのは、

> QM だから非自明

なのではなく、

> support が境界漏れせず、witness が coboundary を偽造せず、anti/symmetric separation が refinement に耐える

から非自明候補として立つ、ということである。

この意味で QM は `B''` の **guard probe 合格例** になる。

front-stage の語彙では、QM は **残差側** と呼ぶ。  
ここで言いたいのは「難しい」ことではなく、**局所整合の残差が class として消えずに残る** ことの方である。

---

## 9. まだ言ってはいけないこと

ここで固定する negativa は強い。

1. これで `H^2_{\Theta} ≠ 0` が **すべての CPS 圏** で成り立つとは言わない
2. これで Paper II `§3.4.6` が theorem へ昇格したとは言わない
3. `ω` という representative と `[\omega]` という class を混同しない
4. `H^2_{\Theta} = 0` なら recoverable だ、とは言わない
5. `ℏ` をそのまま意識の torsion 読みへ飛ばさない

---

## 10. 何が進んだか

進んだのは 4 点である。

1. Phase 5 blocker の「第一候補」が QM で固定された
2. その候補が単なる連想ではなく、**対称 coboundary / 交代 cocycle** という最小計算で支えられた
3. automath bridge で `carry defect` と `class` を分ける方向の足場ができた
4. `Weak Lift B''` の guard が QM 最小模型で自然に読めることが見え、guard 付き nontrivial side が抽象語のままではなくなった

---

## 11. 次の一手

次にやるべきことは 2 つに絞られる。

1. **`A'' / B''` を本文語へ圧縮するか決める**  
   2026-04-15 時点で FTC/QM の両側で guard probe は通った。次は `boundary-closed` や `refinement-stable` のような calculation 語を、そのまま残すのか、あるいは本文用の短い語へ圧縮するのかを決める

2. **guarded selector を本文へどこまで上げるか決める**  
   `§3.4.6` 補注に 2 行で入れるか、meta と calculations に留めるかは、guard 名の圧縮ができるかどうかに依存する

ここで初めて、

> QM = 残差側  
> FTC = 貼合側

という比較面が立つ。
