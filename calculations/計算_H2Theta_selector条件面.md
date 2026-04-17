# H^2_Θ selector 条件面

**作成日**: 2026-04-15  
**役割**: QM と FTC の pair を、単なる並置ではなく `H^2_{\Theta}` の **selector surface** として読むための条件面を固定する。  
**結論の水準**: **calculation / theorem candidate surface**。必要十分条件はまだ主張しない。

---

## 0. 何を分けたいのか

いま calculations 面には 2 つの極がある。

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_QM_H2Theta最小インスタンス.md`
  - nontrivial class の**候補**
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_FTC_H2Theta対照例.md`
  - trivial class の**対照**

ここで次に必要なのは、「なぜ QM は nontrivial side に寄り、FTC は trivial side に寄るのか」を分ける**条件面**である。

欲しいのは theorem の完成ではなく、少なくとも次の 2 極を同じ言語で言い分けることだ。

> **どんなとき local law は global law に吸収されるか**  
> **どんなとき local law は nontrivial class を残しうるか**

---

## 1. 基本量

Paper II の canonical surface に合わせ、局所 forgetting law を 1-cochain

```text
Θ ∈ C^1
```

とし、その defect を

```text
ω_Θ := d^1 Θ ∈ C^2
```

で測る。

直感は単純である。

- `Θ` = 各辺で書ける局所 law
- `ω_Θ` = 三角形を一周したときに残る mismatch
- `[ω_Θ] ∈ H^2_Θ` = その mismatch が「座標の付け替え」で消えるか、消えない class として残るか

selector の仕事は、この `[ω_Θ]` が

- `0` に落ちる側
- `0` に落ちない側

を見分けることにある。

---

## 2. trivial side へ落ちる十分条件

### 2.1 Global potential 条件

もし局所 law `Θ` が、ある global 0-cochain `Λ` から

```text
Θ = d^0 Λ
```

と書けるなら、

```text
ω_Θ = d^1 Θ = d^1 d^0 Λ = 0
```

となる。

これは最も強い trivialization 条件である。  
局所 law が最初から一つの global potential の差分として書けるなら、nontrivial class は立たない。

### 2.2 Contractible patching 条件

global potential が最初から見えていなくても、

- 対象が contractible presentation を持つ
- 各 patch では primitive が取れる
- patch 間の差が定数ずれに留まり
- その定数ずれが基点固定で吸収できる

なら、局所 law は大域 law に貼り合わさる。

このとき `[ω_Θ]` は still trivial side へ落ちる。

FTC の最小模型はこの型である。

---

## 3. nontrivial side を示す十分条件

### 3.1 Alternating witness 条件

逆に、ある additive / abelian presentation に落としたとき defect が

```text
ω ∈ Z^2
```

として見え、しかも

1. `ω` が本質的に **交代的** である  
2. その presentation では `im(d^1)` に入る coboundary が **対称** にしかなれない

なら、

```text
ω ∉ im(d^1)
```

である。

したがって `[ω] ≠ 0` が従い、local law は global law に吸収されない。

この条件の核心は、

> **defect の向き付き成分が、どんな gauge redefinition でも消えない**

ということである。

QM の最小模型はこの型である。

### 3.2 Central extension witness 条件

同じことを別の語で言えば、

- `ω = 0` なら拡大は split する
- `[ω] ≠ 0` なら拡大は split しない

という中心拡大の言葉で読める。

すると selector の nontrivial side は

> **局所 law の mismatch が、中心項として本当に残るか**

で判定できる。

QM の Heisenberg 例はこの witness を与える。

---

## 4. FTC と QM の位置

この条件面で見ると、FTC と QM の差は次の 1 行に圧縮できる。

| ドメイン | selector の効き方 |
|:---|:---|
| FTC | local law が global potential に吸収される |
| QM | defect の交代成分が gauge で消えず class 候補を残す |

したがって selector は、「Drift があるかないか」を見ているのではない。

見ているのは、

> **その Drift が大域的再定義で吸収される型か、吸収されない型か**

である。

この一点で FTC と QM が分かれる。

---

## 5. theorem candidate の核

いま safely 言えるのは、必要十分ではなく**十分条件の二極**だけである。

### Selector Candidate A (globalizable side)

もし局所 forgetting law `Θ` が contractible presentation 上で global potential から来るか、少なくとも patching cocycle が吸収可能なら、

```text
[ω_Θ] = 0
```

である。

### Selector Candidate B (obstructed side)

もし局所 defect が additive / abelian presentation 上で irreducible な alternating witness を持ち、その presentation で coboundary が対称にしかなれないなら、

```text
[ω_Θ] ≠ 0
```

である。

この 2 本が、現段階の selector surface である。

---

## 6. まだ theorem ではない理由

ここで止める理由は明確だ。

1. `contractible presentation` を一般 CPS ドメインへどう持ち上げるかが未定義  
2. `additive / abelian presentation` への reduction functor をまだ書いていない  
3. FTC と QM は両極の witness だが、その中間型をまだ分類していない  
4. selector 条件が必要条件でもあるかは未検証

したがって、これは theorem ではなく

> **どの条件を formalize すれば selector theorem に育つかを示す条件面**

である。

---

## 7. Paper II への翻訳

この note を通すと、Paper II `§3.4.6` の読みは次のように sharpen される。

- Face Lemma は照合面の最小条件を与える
- Coherence Defect Lemma は、その面上の law が globalize するかを問う
- `H^2_{\Theta}` は「有無」より「型」を分ける selector として読む

つまり C4 の価値は、

> **QM のような nontrivial class 候補を許す**

ことだけでなく、

> **FTC のような trivial side を同じ言語で切り分けられる**

ことにもある。

---

## 8. Negativa

ここでまだ主張しないことを固定する。

1. これを selector theorem の完全形とは呼ばない  
2. FTC/QM の二例から一般必要十分条件を引き出したとは言わない  
3. `H^2_{\Theta}=0` を recoverability と同一視しない  
4. `additive presentation` の存在を任意の CPS 圏で仮定しない  
5. representative と class を混同しない

---

## 9. 次の一手

次の blocker は 2 つに絞られる。

1. **selector 条件の lift**  
   2026-04-15 時点で `calculations/計算_H2Theta_selector_CPS内在化条件.md` を追加し、`contractible presentation` を `CPS-globalization atlas + zero holonomy`、`additive witness` を `CPS-obstruction witness + irreducible orientation` へ翻訳した。以後の課題は、この package 条件をどこまで弱めても selector が保たれるかを調べることにある

2. **本文への侵入点の選定**  
   selector surface を Paper II 本文へ補注として入れるか、calculations + meta に留めるか

いまは前者の package 弱化テストを先にやる方が強い。  
本文に入れるなら、「何が trivialize し、何が obstruct するか」の語に加え、「どの lift 条件が本当に必要か」まで整理されている必要がある。
