# H^2_Θ selector の CPS 内在化条件

**作成日**: 2026-04-15  
**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/計算_H2Theta_selector条件面.md` で外部語として置いた `contractible presentation` と `additive / abelian presentation` を、Paper II の CPS 公理語へ持ち上げるための条件面を固定する。  
**結論の水準**: **lift note / theorem candidate surface**。必要十分条件はまだ主張しない。

---

## 0. 何を持ち上げたいのか

selector 条件面では、二つの外部語を使った。

- trivial side: `global potential / contractible patching`
- nontrivial side: `alternating witness / central extension`

だが Paper II の本文語は、FTC や QM の個別言語ではなく CPS の公理語で組まれている。

したがって次に必要なのは、

> **外部 presentation の条件を、CPS1 / CPS2 / CPS5 / Face Lemma の内部語へ翻訳すること**

である。

この note の仕事は、その翻訳面を固定することにある。

---

## 1. 外部語と内部語の対応表

まず最短の対応を置く。

| 外部語 | CPS 内部での読み |
|:---|:---|
| global potential | 同一起源 `C_D` 上の 0-cochain |
| contractible patching | 左随伴で作った局所 section が zero holonomy で貼り合わさる atlas |
| additive / abelian presentation | faithful な witness functor が加法的 target に落ちること |
| central extension | 架橋自然変換の周りで split しない defect witness |
| alternating witness | 照合面上の向き付き defect が gauge で消えないこと |

要するに、外部語の本体は「presentation」ではない。  
本体は、

- **局所再構成が大域へ閉じるか**
- **閉じない向き付き defect が faithful に見えるか**

である。

---

## 2. trivial side の CPS 内在化

### 2.1 CPS-globalization atlas

対象 `x` に対し、`Ξ(x)` あるいはその照合面支持 `K ⊂ St(x)` 上で、次の data を持つとする。

```text
G_x = ( {U_i}, {s_i}, {τ_ij}, {c_ij} )
```

ここで

- `{U_i}` は `K` を覆う局所 chart
- `s_i` は一方の脚 `U_A` または `U_B` に対する**局所 section**
- `τ_ij` は overlap 上の比較写像
- `c_ij` はその比較写像が誘導する drift 差

である。

これを **CPS-globalization atlas** と呼ぶ。

### 2.2 各成分の内部語

この data は CPS 公理語では次のように読む。

1. `{U_i}` が同じ `C_D` の局所 chart であること  
   = **CPS1 同一起源**
2. `s_i` が局所再構成として存在すること  
   = Layer 1 条件 (2) の **左随伴**
3. `τ_ij` が別脚どうしの比較写像として存在すること  
   = **CPS2 架橋**
4. `c_ij` が局所 drift 差として定義でき、しかも mask によって壊れないこと  
   = **CPS5 マスク**の下での中心的差分

つまり `contractible patching` の内実は、

> **同一起源からの局所再構成が、架橋写像の周りで holonomy を残さずに貼り合わさる**

ことにある。

### 2.3 Zero holonomy 条件

各非退化 2-simplex `σ = (f,g,h)` に対し、overlap 差分が

```text
c_jk - c_ik + c_ij = 0
```

を満たすとする。

これは外部語では patching cocycle の消滅だが、CPS 内部では

> **照合面を一周しても再構成 drift が閉じる**

という意味になる。

Face Lemma の言葉で言えば、

- `B_1^{ver}(x) ≠ 0` により照合面は立つ
- その面上の bridge holonomy が zero

なので、局所 law は大域 law に閉じる。

### 2.4 Candidate Lift A

したがって、次の十分条件候補が得られる。

> **Candidate Lift A.**  
> ある対象 `x` が `CPS-globalization atlas` を持ち、全ての照合面で zero holonomy 条件を満たすなら、その対象の局所 forgetting law は大域 1-cochain に吸収され、`[ω_Θ](x)=0` である。

FTC の最小模型はこの lift の witness として読める。

---

## 3. nontrivial side の CPS 内在化

### 3.1 CPS-obstruction witness

今度は対象 `x` に対し、

```text
W_x = ( A_x, Φ_x, β_x, ω_x )
```

という data を考える。

ここで

- `A_x` は加法的 target
- `Φ_x : K_x -> A_x` は `K_x ⊂ St(x)` からの witness functor
- `β_x` は A/B 両脚の向きを区別する pairing
- `ω_x` はその pairing から得られる defect 2-cochain

である。

これを **CPS-obstruction witness** と呼ぶ。

### 3.2 各成分の内部語

この data は次の内部条件へ翻訳される。

1. `Φ_x` が異なる射を潰さない  
   = Layer 1 条件 (1) **faithful**
2. `Φ_x` が A/B の二脚を distinct directions として保つ  
   = Layer 1 条件 (4)(5) **非同型 + CPS 経由**
3. `β_x` が照合面の向きを読める  
   = Face Lemma によって立った 2-simplex の**向き付き比較**
4. `ω_x` がその向き付き比較から作られる  
   = `d^1Θ` の witness

ここで重要なのは、additive presentation を圏全体に要求しないことである。  
必要なのは

> **照合面支持の上に faithful な加法的 witness が一つあること**

だけである。

### 3.3 Irreducible orientation 条件

さらに、`ω_x` が

- 向きを反転すると符号を反転し
- gauge redefinition から来る coboundary は対称にしか見えず
- `Φ_x` がその差を faithful に保つ

とする。

このとき、

> **向き付き defect は gauge で消せない**

ので、`[ω_Θ](x) ≠ 0` の witness になる。

### 3.4 Candidate Lift B

したがって、次の十分条件候補が得られる。

> **Candidate Lift B.**  
> ある対象 `x` が `CPS-obstruction witness` を持ち、その witness 上で defect が irreducible orientation 条件を満たすなら、`[ω_Θ](x) ≠ 0` である。

QM の最小模型はこの lift の witness として読める。

---

## 4. FTC と QM の再配置

この note を通すと、FTC と QM は外部例ではなく、CPS 内部で次のように再配置される。

| ドメイン | CPS 内部での位置 |
|:---|:---|
| FTC | `CPS-globalization atlas` の witness |
| QM | `CPS-obstruction witness` の witness |

したがって、selector の違いは

- FTC が解析だから trivial
- QM が量子だから nontrivial

なのではない。

違いは、

> **局所再構成が zero holonomy で閉じる package を持つか**  
> **faithful な向き付き defect witness を持つか**

にある。

これでようやく selector が Paper II の内部語へ近づく。

---

## 5. 何がまだ未定義か

ここでの最大の正直さは、未定義を隠さないことだ。

### 5.1 `section` の一般形

FTC では primitive を section と読めた。  
だが一般 CPS ドメインでは、左随伴の値を「局所 section」と読むための site / cover 構造がまだ書かれていない。

### 5.2 `holonomy` の一般形

FTC では定数差でよかった。  
だが一般 CPS では、何を中心的 drift 差と呼ぶかを `CPS2 + CPS5` から抽出する必要がある。

### 5.3 `additive witness` の一般形

QM では `R^2` や Heisenberg 群へ落とせた。  
だが一般 CPS ドメインで、どの reduction が witness として admissible かはまだ決まっていない。

### 5.4 `faithful on the defect support`

圏全体で faithful でなくても、照合面支持の上では faithful であれば十分かもしれない。  
この局所 faithful 条件をどこまで弱められるかは未検証である。

---

## 6. theorem candidate の形

現段階で safely 書ける theorem candidate は次の二段である。

### Lift Theorem Candidate A

`CPS-globalization atlas + zero holonomy`  
→ `local law globalizes`  
→ `[ω_Θ]=0`

### Lift Theorem Candidate B

`CPS-obstruction witness + irreducible orientation`  
→ `defect survives every gauge redefinition visible to the witness`  
→ `[ω_Θ]≠0`

この形なら、まだ必要十分とは言っていない。  
だが「何を formalize すべきか」は明確になる。

---

## 7. Paper II への翻訳

Paper II に戻すと、C4 は次の三層に分けて読むのが最も強い。

1. **canonical surface**: `H^2_{\Theta}`
2. **selector surface**: trivial side / nontrivial side の十分条件
3. **lift surface**: その十分条件を CPS 公理語で言い直す package

いま追加したのは 3 である。

これにより、C4 は少なくとも

> 「QM と FTC の例がある」

だけの conjecture ではなく、

> 「どの内部条件を formalize すれば二例の差が論文内部の言葉で書けるか」

まで進んだ。

---

## 8. Negativa

ここでまだ主張しないことを固定する。

1. `CPS-globalization atlas` と `CPS-obstruction witness` が必要条件でもあるとは言わない  
2. 一般 CPS 圏に site / topology が既に備わっているとは言わない  
3. 任意の C4 対象に additive witness reduction が存在すると仮定しない  
4. zero holonomy を recoverability と同一視しない  
5. この note だけで本文 `§3.4.6` を theorem へ昇格させない

---

## 9. 次の一手

次にやるべきことは 2 つに絞られる。

1. **lift package の反例探索と guard 抽出**  
   2026-04-15 時点で `calculations/計算_H2Theta_selector_package弱化テスト.md` を追加し、full package を `support-locality` と `generator-face sufficiency` に沿って削った。さらに `calculations/計算_H2Theta_selector_weakpackage反例探索.md` を追加し、`Weak Lift A' / B'` の false trivialization / false obstruction を分けて検査した。以後の課題は、guard 付き版 `A'' / B''` が FTC / QM で自然に満たされるかを probe することにある

2. **本文侵入の最小形を決める**  
   `§3.4.6` に 1-2 行の補注として package 名だけ入れるか、それとも calculations + meta のまま保持するか

私の判断では、まだ前者の反例探索をやるべきだ。  
本文へ入れる前に、weak package が本当に壊れにくいかを確かめた方が強い。
