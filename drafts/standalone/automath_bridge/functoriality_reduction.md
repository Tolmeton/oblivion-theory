# 関手の合成保存 open problem の再定式化

作成: 2026-04-14  
対象: automath bridge の Open 1 「離散化関手 D の合成保存」

## 0. 結論

現行の open problem は、ひとつの問いに見えて実際には三層に分かれている。

1. **射の合成としての関手性**  
   これは product Bernoulli / coordinate projection の部分圏に限れば、すでに strict に閉じる。

2. **外微分との両立 (chain-map 性)**  
   これは cubical chart と multilinear observable に制限すれば、`deltaSet` が混合偏微分の cell 積分と一致することで閉じる。

3. **加法・合成との両立 (monoidal coherence)**  
   ここが未解決の核であり、ordinary functor の問題ではなく、carry defect を 2-cell に持つ **lax monoidal / defect-bearing bridge** の問題として立てるべきである。

したがって「D は functor か?」という問いは粗すぎる。  
正確には:

> **strict 1-functor 部分は既にある。未解決なのは monoidal coherence を担う defect 2-cell の同定である。**

---

## 1. SOURCE: automath 側で既に閉じているもの

### 1.1 制限写像の strict functoriality

automath には既に

```lean
theorem restrict_functorial
```

があり、これは

\[
\operatorname{restrict}_{m_1 \leftarrow m_2}
\circ
\operatorname{restrict}_{m_2 \leftarrow m_3}

=

\operatorname{restrict}_{m_1 \leftarrow m_3}
\]

を与える。  
つまり「粗視化そのものの合成」は Lean で証明済みである。

対応箇所:

- `Omega/Folding/Defect.lean`, `restrict_functorial`
- `Omega/Folding/Defect.lean`, `restrictLE_comp`

### 1.2 defect の 2-cocycle 形

automath にはさらに

```lean
theorem globalDefect_compose
```

があり、global defect が三解像度の合成に対して xor-cocycle として振る舞う:

\[
D_{m \leftarrow n}

=

D_{m \leftarrow k} \circ \operatorname{restrict}_{k \leftarrow n}
\;\oplus\;
\operatorname{restrict}_{m \leftarrow k}(D_{k \leftarrow n})
\]

これは「失敗がランダムに散る」のではなく、**合成法則を持った 2 段のデータ**であることを意味する。

対応箇所:

- `Omega/Folding/Defect.lean`, `globalDefect_compose`
- `Omega/Folding/Defect.lean`, `globalDefect_poincare_band`
- `Omega/Folding/CarryDefect.lean`, `restrict_stableAdd_carry_defect`

---

## 2. full `Man -> Hyp` 定式化の問題点

現行の D は

\[
D : \mathbf{Man} \to \mathbf{Hyp}
\]

と書かれているが、この書き方には少なくとも二つの未固定量がある。

### 2.1 chart の未固定

一般の statistical manifold から hypercube への写像には、少なくとも

- どの局所座標を使うか
- どの cell 分割を採るか
- `T` の方向をどの離散座標集合 `A` に送るか

が必要である。  
これらを固定しない限り、D は定義不足である。

### 2.2 observable class の未固定

`deltaSet` は Boolean lattice 上の交代和であり、自然に噛み合うのは

- cubical cochain
- multilinear function
- product Bernoulli family の cylinder observable

のような「座標ごとに分離できる」関数族である。  
一般の滑らかな関数全体に一気に延長するのは過剰であり、ここで open problem が膨張している。

---

## 3. strict 部分: `CubeExp_proj -> Hyp_proj`

### 3.1 部分圏の定義

以下の部分圏を取る。

#### `CubeExp_proj`

- **対象**: 有限集合 `I` で添字づけられた product Bernoulli family  
  \[
  M_I := (\Delta^1)^I
  \]
- **射**: 座標忘却
  \[
  \pi_{J \subseteq I} : (\Delta^1)^I \to (\Delta^1)^J
  \]

#### `Hyp_proj`

- **対象**: Boolean cube
  \[
  \{0,1\}^I
  \]
- **射**: automath の restriction
  \[
  \operatorname{restrict}_{J \subseteq I} : \{0,1\}^I \to \{0,1\}^J
  \]

### 3.2 strict functor

このとき

\[
D_{\mathrm{proj}}(M_I) := \{0,1\}^I,
\qquad
D_{\mathrm{proj}}(\pi_{J \subseteq I}) := \operatorname{restrict}_{J \subseteq I}
\]

と置けば、`restrict_functorial` により

\[
D_{\mathrm{proj}}(\pi_{K \subseteq J} \circ \pi_{J \subseteq I})

=

D_{\mathrm{proj}}(\pi_{K \subseteq J})
\circ
D_{\mathrm{proj}}(\pi_{J \subseteq I})
\]

が成り立つ。

### 3.3 帰結

**ordinary composition の意味での関手性は、この部分圏では既に解けている。**

従って issue reply で言うべき「core open problem」は、少なくともこの strict 部分そのものではない。

---

## 4. chain-map 部分: `d` と `deltaSet` の対応

### 4.1 観測量の制限

各 `M_I = (\Delta^1)^I` 上の観測量を multilinear function

\[
f(x)
=
\sum_{S \subseteq I} c_S \prod_{i \in S} x_i
\]

に制限する。  
これは product Bernoulli family の cylinder observable の線形包に対応する。

### 4.2 face 上の有限差分

`A ⊆ I` と、`A` 上で 0 を取る boundary word `w` を取る。  
このとき automath の

\[
\delta_A f(w)
:=
\sum_{B \subseteq A} (-1)^{|B|}
f(\operatorname{flip}_B w)
\]

は、標準向きの `A`-cell 上の混合偏微分の積分に一致する:

\[
\delta_A\bigl(f|_{\{0,1\}^I}\bigr)(w)

=

(-1)^{|A|}
\int_{[0,1]^A}
\partial_A f\bigl(\iota_{A,w}(u)\bigr)\,du
\]

ここで `\iota_{A,w}` は `A` の座標だけを動かし、それ以外を `w` で固定する埋め込みである。

### 4.3 証明スケッチ

`g(u) := f(\iota_{A,w}(u))` とおけば、`g` は `|A|` 変数の multilinear function。  
1変数の基本定理

\[
g(1) - g(0) = \int_0^1 g'(t)\,dt
\]

を各座標に対して反復適用すると

\[
\sum_{B \subseteq A} (-1)^{|A|-|B|} g(1_B)

=

\int_{[0,1]^A} \partial_A g(u)\,du
\]

が出る。  
`deltaSet` の符号規約は `(-1)^{|B|}` なので、全体に `(-1)^{|A|}` が掛かる。

### 4.4 ここで何が解けたか

これは「D が `d` を `deltaSet` に送る」という主張の **cubical / multilinear / boundary-face 版**である。  
したがって少なくとも:

- `d` の離散 shadow が `deltaSet`
- `∫` の離散 shadow が `walshFlux`

という主張は、単なる類推ではなく cubical cochain のレベルで実定理に落ちる。

---

## 5. 本当に未解決なのはどこか

### 5.1 additivity / composition drift との両立

automath の本丸は

\[
\Phi(x \oplus y)
\neq
\Phi(x) \oplus \Phi(y)
\]

であり、その差が carry defect `κ` になることだった。  
これは `projection` の strict composition とは別問題である。

つまり未解決部分は

\[
D(x \oplus y)
\stackrel{?}{=}
D(x) \oplus D(y)
\]

あるいは連続側では

\[
D\bigl(G(f \circ g)\bigr)
\stackrel{?}{=}
D(G(f)) \circ D(G(g))
\]

という **monoidal coherence** にある。

### 5.2 したがって bridge の型は ordinary functor では足りない

automath 側の Lean 事実をそのまま読むと、橋は

- 1-morphism では strict
- monoidal coherence では defect 付き

である。  
よって期待すべき構造は

> **strict functor + defect 2-cell**

あるいは

> **lax monoidal functor / pseudofunctor**

である。

この 2-cell を automath 側では

- `restrict_stableAdd_carry_defect`
- `globalDefect_compose`

が担う。

### 5.3 向こうの issue 返信との一致

automath 側の返信では `κ` は

- non-trivial 2-cocycle
- `H²(G_m; Z/2Z)` のクラス
- central extension の非分裂性

として読まれている。  
これは本ノートの結論と整合する。  
すなわち、open problem の核は「1-functor を作ること」ではなく、

> **この 2-cocycle を連続側の drift / curvature とどう同一視するか**

にある。

---

## 6. PR に向けた最短の主張

現時点で PR/bridge 文書に載せるべき最短の主張は次である。

### Theorem A (strict part)

product Bernoulli family と coordinate projection からなる部分圏 `CubeExp_proj` 上で、  
candidate discretization `D_proj` は strict functor である。

Lean witness:

- `restrict_functorial`

### Theorem B (chain-map part)

multilinear observable に制限すると、`deltaSet` は mixed partial の cell 積分に一致する。  
したがって `d ↦ deltaSet`, `∫ ↦ walshFlux` は cubical cochain のレベルで正当化される。

### Open C (actual core)

一般の morphism / addition / composition drift に対して、bridge は strict monoidal ではなく defect-bearing であり、

\[
\text{obstruction class}
\quad
\leftrightarrow
\quad
\kappa
\]

の同定が core open problem である。

---

## 7. 実務上の次の一手

### 7.1 いま着手すべきこと

1. `Open 1` の名前を変更する  
   `関手性` ではなく  
   **「strict part は解決、defect 2-cell の連続側同定が未解決」**

2. Lean / 文書の証明ターゲットを二段に分ける  
   - `discretize_proj_functorial`
   - `deltaSet_mixed_partial_cell_formula`

3. continuous 側で 2-cocycle の受け皿を探す  
   候補:
   - composition drift `δ`
   - Čech 2-cocycle
   - central extension / gerbe 的障害

### 7.2 まだ言ってはいけないこと

以下はまだ言えない。

- full `Man -> Hyp` が canonical functor である
- `D` が一般の smooth morphism 全体で strict に compose する
- carry defect と curvature の完全同一性が既に証明された

言えるのは、

> **strict 部分は product Bernoulli / coordinate projection で閉じる。未解決部分は degree-2 obstruction に押し込められた。**

までである。

---

## 8. 付記: このノートの位置づけ

このノートは「open problem を解いた」報告ではない。  
だが、**何が既に解けていて、何が本当に未解決かを峻別した**という意味で、問題の位相を一段下げている。

今後の実質的な突破口は、

- ordinary functor を証明しようとすること

ではなく、

- carry / drift を coherence 2-cell として連続側に持ち上げること

にある。
