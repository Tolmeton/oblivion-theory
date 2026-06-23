# C11 Yoneda 経路完全化

**副題**: weak spherical 2-category における SignTower 表現定理
**版**: v0.5 T_sph preliminary table
**日付**: 2026-05-02
**親稿**: `比較射σの統一定理_v0.6.md`

---

## Abstract

比較射 `σ: g∘f ⇒ h` は、親稿 `比較射σの統一定理_v0.6` において、Paper I wedge / signed oblivion / Stasheff tower / BridgeDat / FEP blanket sector の 5 context に現れる単一 Yoneda 関手値として定式化された。しかし親稿で残された C11 の技術的 gap は、Yoneda 補題そのものではなく、Yoneda evaluation を載せる舞台、すなわち weak spherical 2-category と signed Stasheff tower の自由生成・商構成・非崩壊に集中している。

本稿は C11 の proof companion として、walking signed triangle と signed Stasheff tower を weak spherical 2-category 上で生成する自由-忘却随伴 `F_sph ⊣ U` を明示し、比較射 σ が `Hom_{SignTower}(K_n, -)` の evaluation として表現されるための証明義務を分解する。特に、Gurski 2013 Ch 15 の direct SOURCE、BKP 1989 の pseudomonadicity、Lack 2010 の bicategorical adjoint functor theorem、Lack 2007 の cofibrant replacement を、C11 の 5 つの未解決義務 `#22a.i`, `#22a.ii`, `#22a.iii.a-c` に対応させる。

本稿の主張は、σ 論文の思想的射程を広げることではない。目的は、親稿 v0.6 の「5 context Yoneda 自動同値」を sketch-level から proof-level へ上げるために、どの定理がどの証明義務を支えるかを固定することである。

---

## 1. Claim

**主張 C11-Y**: 適切に定義された weak spherical 2-category の 2-圏 `Sph2Cat` と、その signed Stasheff tower 部分 `SignTower` に対し、walking signed triangle `S_triangle` および walking `(n-1)`-associator signature `S_n` からの自由生成は、忘却 2-関手 `U` の左随伴 `F_sph` を持つ。したがって、各 weak spherical 2-category object `X` について、比較射 σ の signed coherence data は

```text
Hom_{SignTower}(K_n, X)
```

の値として表現される。

この命題が成立するとき、親稿 v0.6 の 5 context は、個別の橋ではなく、同一 Yoneda 関手 `Hom_{SignTower}(K_n, -)` の異なる evaluation として読むことができる。

---

## 2. Theorem Statement

**定理 C11.1 (SignTower 表現定理, proof-obligation form).**
`S_triangle` を 3 つの 0-cell、3 つの生成 1-cell `f, g, h`、および 1 つの生成 2-cell `σ: g∘f ⇒ h` を持つ walking signed triangle signature とする。`S_n` を walking `(n-1)`-associator signature とする。`Sph2Cat` を weak spherical 2-category と spherical 2-functor からなる 2-圏とし、`U: Sph2Cat → Sig` を underlying signature を返す忘却 2-関手とする。

もし次の 5 条件が満たされるなら、

| 条件 | 内容 |
|:--|:--|
| C11.1-a | Gurski 型 coherence theorem が、対象の weak spherical / tricategorical coherence に適用できる |
| C11.1-b | spherical coherence quotient が `source-target`, `arity`, `framing` を保存し、生成子 σ を潰さない |
| C11.1-c | 対応する 2-monad `T_sph^pseudo` が BKP 1989 の pseudomonadicity 条件を満たす |
| C11.1-d | Lack 2010 の bicategorical AFT に必要な biuniversal arrow / solution set 条件が成立する |
| C11.1-e | Lack 2007 型 cofibrant replacement が weak presentation と strict presentation の間で σ と σ* を保存する |

`U` は左 biadjoint `F_sph` を持ち、`K_n := F_sph(S_n)` と置ける。このとき任意の `X ∈ Sph2Cat` について、

```text
Hom_{SignTower}(K_n, X)
```

は `X` 内の signed `(n-1)`-associator coherence data を表現する。特に `n=3` では、`K_3 = F_sph(S_triangle)` により、比較射 `σ: g∘f ⇒ h` は `Hom_{SignTower}(K_3, X)` の evaluation として得られる。

---

## 3. Proof Obligations

| ID | 証明義務 | 必要 SOURCE | 現状態 |
|:--|:--|:--|:--|
| `#22a.i` | Gurski 2013 Ch 15 の direct SOURCE を取得し、coherence theorem の適用範囲を確定する | Gurski 2013 Ch 15 | SOURCE 候補取得済み、未精読 |
| `#22a.ii` | spherical coherence quotient が generator を潰さないことを示す | Gurski 2013 / Dupont 2019 / Lack 2007 | 代替経路候補あり、未計算 |
| `#22a.iii.a` | `T_sph^pseudo` の pseudomonadicity 条件を示す | BKP 1989 | SOURCE 候補取得済み、未特殊化 |
| `#22a.iii.b` | Lack 2010 bicategorical AFT の solution set / biuniversal arrow 条件を示す | Lack 2010 / Lack 2007 companion | SOURCE 候補取得済み、未特殊化 |
| `#22a.iii.c` | cofibrant replacement が σ, σ*, coherence cells を保存することを示す | Lack 2007 | SOURCE 候補取得済み、未特殊化 |

### 3.1 外部関連論文対応表

現時点の探索では、`C11 Yoneda 経路完全化`、`SignTower`、`walking signed triangle`、`weak spherical 2-category` と σ 論文の 5 context をそのまま扱う既存論文は見つかっていない。したがって本稿は既存定理の再掲ではなく、次の既存結果を C11 用の証明義務へ配線する proof-companion として置く。

| 文献 | C11 での役割 | 対応義務 | SOURCE 状態 |
|:--|:--|:--|:--|
| Nick Gurski, *Coherence in Three-Dimensional Category Theory*, Ch.15 "A general coherence result" | weak / tricategorical coherence の直接候補。舞台生成に必要な coherence theorem の適用範囲を読む | `#22a.i`, `#22a.ii` | Cambridge Core PDF 候補取得済み、定理番号未精読 |
| R. Blackwell, G. M. Kelly, A. J. Power, *Two-dimensional monad theory* | pseudo algebra / strict algebra / inclusion の 2-monad 側を支える | `#22a.iii.a` | PDF 候補取得済み、`T_sph^pseudo` への特殊化未計算 |
| Stephen Lack, *A 2-categories companion* (arXiv:math/0702535) | 2-categories / bicategories / formal category theory / 2-dimensional universal algebra の基盤整理 | `#22a.iii.b` | arXiv 候補取得済み、AFT 条件抽出未了 |
| Stephen Lack, *Homotopy-theoretic aspects of 2-monads* | cofibrant replacement と flexible / strict presentation の移行を扱う | `#22a.iii.c` | 出版情報・PDF 候補取得済み、σ 保存の確認未了 |
| Nick Gurski, *An algebraic theory of tricategories* | tricategory の代数的定義と coherence 背景。Ch.15 が足りない場合の補助線 | `#22a.i`, `#22a.ii` | PDF 候補取得済み、補助扱い |
| Richard Garner and Nick Gurski, *The low-dimensional structures formed by tricategories* | tricategory から低次元構造が形成される経路の補助 | `#22a.ii` | arXiv 候補取得済み、補助扱い |
| *Gray-categories model algebraic tricategories* | algebraic tricategory と Gray-category の modern follow-up | `#22a.i`, `#22a.ii` | arXiv 候補取得済み、補助扱い |
| Benjamin Dupont, *Rewriting modulo isotopies in pivotal linear (2,2)-categories* | spherical / pivotal quotient の non-collapse を polygraph rewriting で攻める代替経路 | `#22a.ii` | arXiv 候補取得済み、代替扱い |

### 3.2 探索後の判断

完全一致する先行論文が見つかっていないため、本稿の価値は「未発見の Yoneda 補題を証明すること」ではなく、既存の coherence / 2-monad / AFT / cofibrant replacement の結果を、σ 論文固有の `SignTower` 舞台生成へ接続することにある。

この接続で最も危険なのは、外部文献名を並べただけで `F_sph ⊣ U` の存在を装うことである。次の実化操作は、各文献から C11 に必要な条件だけを抜き、`S_triangle`, `S_n`, `T_sph^pseudo`, `K_n` へ特殊化することである。

### 3.3 Gurski Ch.15 抽出試行

Cambridge Core の章ページから、Gurski Ch.15 は `A general coherence result`、pp.244-272、DOI `10.1017/CBO9781139542333.016` であることを確認した。Cambridge frontmatter から、Ch.15 の内部構成は `15.1 Weak codescent objects` と `15.2 Coherence for pseudo-algebras` であることを確認した。

ただし、Cambridge の `citation_pdf_url` は現時点で PDF 本文ではなく HTML を返し、定理本文のテキスト抽出はできていない。したがって、以下は proof claim ではなく、C11 に接続すべき SOURCE 抽出候補である。

| 候補 | SOURCE から確認できたこと | C11 への使い道 | 状態 |
|:--|:--|:--|:--|
| G15-1: weak codescent objects | Ch.15.1 の主題が weak codescent objects である | `#22a.ii` の quotient / non-collapse を codescent 側から検査する入口 | 章構成 SOURCE のみ。定理本文未取得 |
| G15-2: coherence for pseudo-algebras | Ch.15.2 の主題が pseudo-algebra coherence である | `T_sph^pseudo` を pseudo-algebra と見て、strict / weak presentation の移行を検査する入口 | 章構成 SOURCE のみ。定理本文未取得 |
| L02-1: Lack 2002 codescent route | Lack 2002 は strict `T`-algebra から pseudo / lax `T`-algebra への包含を扱い、十分条件の下で左随伴と、pseudo algebra が strict one と同値になる条件を与える | Gurski Ch.15 本文未取得時の代替足場。`#22a.iii.a-c` を「包含の左随伴」「unit equivalence」「strictification preserves σ」へ分解する | open abstract SOURCE あり。C11 特殊化は未計算 |

この時点で採る作戦は、Gurski Ch.15 を「存在確認済みだが本文未精読」として保持し、Lack 2002 を実際に読める codescent 経路として先に特殊化することである。

### 3.4 Lack 2002 route extraction

Lack 2002 `Codescent objects and coherence` は、C11 にとって Gurski Ch.15 の代替ではなく、Gurski Ch.15 を読む前に `T_sph^pseudo` 側の必要条件を明確化する足場である。ScienceDirect / Macquarie の一次メタデータと本文プレビューから、C11 に使うべき抽出点は次の 3 点に絞る。

| 抽出点 | Lack 2002 での役割 | C11 への変換 | 未証明条件 |
|:--|:--|:--|:--|
| L02-A: inclusion has left adjoint | strict `T`-algebra から pseudo / lax `T`-algebra への包含に左随伴を与える十分条件を扱う | `U_s: Sph2Cat_strict -> Sph2Cat_pseudo` の包含反対向きに、pseudo presentation を strict presentation へ戻す reflection を置く | `T_sph` が Lack の仮定を満たすこと |
| L02-B: unit components are equivalences | pseudo algebra が strict one と同値になる coherence theorem の第二段を扱う | weak spherical presentation と strict SignTower presentation の間で σ の表現値が同値として保たれることを狙う | unit equivalence が `σ`, `σ*`, framing を保存すること |
| L02-C: codescent preservation condition | base 2-category が codescent objects を持ち、`T` がそれを保存する場合に strictification の構成を支える | `Sph2Cat` またはその signature/presentation 圏に codescent object があり、`T_sph` がそれを保存するかを検査する | coinserter / coequifier の存在と保存、または代替の flexible-colimit 条件 |

この抽出により、C11 の `F_sph ⊣ U` はいきなり主張する対象ではなく、次の検査列へ分解される。

| C11 検査 | 対応 |
|:--|:--|
| `T_sph` の定義 | `S_triangle`, `S_n`, spherical coherence operations を生成する 2-monad として定義する |
| strict / pseudo / lax algebra の分離 | strict presentation, weak spherical presentation, lax quotient presentation を混同しない |
| left adjoint の存在 | Lack 2002 の inclusion/reflection 型左随伴を C11 に特殊化する |
| σ 保存 | unit equivalence または strictification が `source-target`, `arity`, `framing` を潰さないことを別義務にする |

### 3.5 `T_sph` preliminary table

親稿 v0.6 は `T_sph` という 2-monad をまだ直接定義していない。現時点で SOURCE として使えるのは、親稿 §III.2-4 と §D.1.3-1.6 に置かれた walking signature、weak spherical 2-圏、SignTower、非崩壊不変量である。したがって以下は完成定義ではなく、Lack 2002 の 3 検査に代入するための `T_sph` 候補表である。

| 層 | `T_sph` に入る生成データ | 親稿 SOURCE | Lack 2002 検査での役割 | 未決 |
|:--|:--|:--|:--|:--|
| 0-cell operations | `S_triangle` の 3 objects、`S_n` の associahedral vertices / faces | 親稿 §III.4, §D.1.3 | codescent object の underlying object data | `S_n` の signature-level object list を明文化する |
| 1-cell operations | `f:0->1`, `g:1->2`, `h:0->2`、および `K_n -> K_{n+1}` face inclusion | 親稿 §III.3-4, §D.1.3 | strict / pseudo algebra の carrier morphisms | face inclusion を operation と見るか morphism of algebras と見るか |
| 2-cell operations | `σ: g∘f => h`、canonical dual `σ*`、pentagon identity 2-cell `α_5`、一般 `(n-1)`-associator coherence cells | 親稿 §III.3-5, §D.1.3 | pseudo algebra の coherence data | `σ*` を generated operation とするか pivotal closure の結果とするか |
| equations | source-target matching、associator coherence、pivotal double-dual、zigzag / snake、left-right trace equality | 親稿 §III.2, §D.1.4-1.6 | `T_sph` algebra laws。strict / pseudo / lax の分岐点 | どの equations を strict、どれを invertible 2-cell に弱めるか |
| quotient / preservation | source-target、arity、framing の 3 不変量保存 | 親稿 §III.4, §D.1.6 | unit equivalence と strictification が σ を潰さないための check | Lack 2002 の unit equivalence に 3 不変量保存をどう載せるか |
| ambient colimits | coinserter / coequifier または flexible-colimit 代替 | Lack 2002 / Lack 2007 / BKP 1989 | codescent preservation condition | `Sph2Cat` 側で存在・保存を未確認 |

この table から C11 の次の作業は、`T_sph` を「spherical coherence を自由に足す 2-monad」として直ちに断定することではない。まず、上の各層を strict / pseudo / lax の 3 presentation に分ける。

| presentation | 意味 | C11 での使用 |
|:--|:--|:--|
| strict `T_sph`-algebra | associator / pivotal / trace laws を strict equations として持つ presentation | Lack 2002 の strict side。計算しやすいが、Stasheff の weak 性を吸収しすぎる危険がある |
| pseudo `T_sph`-algebra | associator / pivotal / trace laws を coherent invertible 2-cells として持つ presentation | C11 の本命。weak spherical 2-category と SignTower を載せる |
| lax `T_sph`-algebra | quotient / degeneration を許す presentation | non-collapse 検査用。σ が潰れる経路を検出する |

したがって `T_sph` table の直後に置くべき証明義務は、`T_sph` の存在主張ではなく、次の 3 つである。

| 新義務 | 内容 | 失敗時 |
|:--|:--|:--|
| `#22a.T1` | 上表の operations / equations が 2-monad presentation を成すこと | `T_sph` ではなく generators-and-relations sketch に戻す |
| `#22a.T2` | pseudo `T_sph`-algebra が親稿の weak spherical 2-category と一致すること | C11 の舞台名を `Sph2Cat` から別名に下げる |
| `#22a.T3` | strictification/unit equivalence が `σ`, `σ*`, source-target / arity / framing を保存すること | `F_sph ⊣ U` を proof-level へ上げない |

---

## 4. Why This Is a Standalone Paper

本稿が単独論文として成立するのは、親稿の結論を繰り返すからではない。親稿の主張は「5 顔は同一 Yoneda 関手値である」という統一定理であり、本稿の主張は「その Yoneda 関手値を許す舞台をどう生成し、何を確認すれば proof-level になるか」である。

したがって本稿の独立性は次の 3 点にある。

| 独立性 | 内容 |
|:--|:--|
| 技術的独立性 | weak spherical 2-category / SignTower / AFT の舞台生成に主題を限定する |
| 反駁可能性 | 5 つの proof obligation のどれかが失敗すれば、C11 は proof-level へ昇格しない |
| 親稿への貢献 | 成功すれば親稿 v0.6 の `5 context Yoneda 自動同値` が sketch-level から proof-level へ上がる |

---

## 5. SOURCE / TAINT

| 区分 | 内容 |
|:--|:--|
| SOURCE | 親稿 `比較射σの統一定理_v0.6.md` §VI.6, §VIII.3, 付録 §A, 付録 §D.1 |
| 外部 SOURCE 候補 | Gurski 2013 Ch 15, Lack 2002 codescent objects, BKP 1989, Lack companion, Lack 2007 2-monads, Gurski algebraic tricategories, Garner-Gurski 2007, Gray-categories model algebraic tricategories, Dupont 2019 |
| 確認済み SOURCE | Cambridge Core chapter metadata: Gurski Ch.15 title / DOI / pp.244-272。Cambridge frontmatter: Ch.15.1 `Weak codescent objects`, Ch.15.2 `Coherence for pseudo-algebras`。Macquarie page: Lack 2002 abstract and bibliographic data。ScienceDirect page: Lack 2002 の theorem-schema / codescent preservation 条件 |
| 未精読 SOURCE | Gurski Ch.15 の定理本文、BKP / Lack / Dupont の定理番号・仮定・C11 への特殊化条件 |
| TAINT | 「C11 と完全一致する既存論文はない」という探索結果。検索語依存のため、断定ではなく現時点の未発見として扱う |

---

## 6. Next Step

次に行うべきことは証明本文を書くことではない。`#22a.T1` として、上の operations / equations が本当に 2-monad presentation を成すかを確認する。最初の作業は `σ*` の身分を決めること、すなわち生成 operation なのか、pivotal closure から出る derived cell なのかを分けることである。
