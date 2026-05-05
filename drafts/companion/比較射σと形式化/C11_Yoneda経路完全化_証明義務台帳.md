# C11 Yoneda 経路完全化 — 証明義務台帳

**作成日**: 2026-05-02
**親稿**: `比較射σの統一定理_v0.6.md`
**役割**: 別稿 A「Yoneda 経路完全化」を、証明本文へ入る前の足場として固定する。

---

## 0. Direction Reception

**方向**: C11 `Yoneda universal representation` を sketch-level から proof-level へ引き上げる。
**派生**: `/kop.deepen` 相当。同じ σ 論文の中核を深く踏む。
**撤退条件**: 次のいずれかを満たしたら停止し、本文修正ではなく台帳更新へ戻る。

| 条件 | トリガー | 停止後の扱い |
|:--|:--|:--|
| SOURCE 不足 | Gurski 2013 Ch 15 の本文取得または精読ができない | `#22a.i` は章メタデータ確認済み・本文未精読として固定し、Lack 2002 codescent route へ迂回 |
| 証明義務過拡張 | C11 以外の Phase II / FEP / Paper XIII へ逸れる | 別稿 B-D へ差し戻し |
| 商構成不明 | spherical coherence quotient が generator を潰す可能性を除去できない | `#22a.ii` を未解決に戻す |
| AFT 条件未充足 | pseudomonadicity / solution set / cofibrant replacement のいずれかを明示できない | `#22a.iii` を sketch-level のまま維持 |

---

## 1. First Contact

### 1.1 prior

親稿 v0.6 は、5 context を同一 Yoneda 関手の evaluation として束ねている。C11 の残 gap は本文内では限定済みであり、別稿 A はその残 gap を proof-level に変換するだけでよい。

### 1.2 observation

親稿の §VI / §VIII / §A / §D.1 は、C11 の未踏領域を次の 5 点に絞っている。

| ID | 親稿上の呼称 | 問題の中身 |
|:--|:--|:--|
| `#22a.i` | Gurski 2013 Ch 15 direct SOURCE | weak spherical / tricategory coherence の直接根拠を取得する |
| `#22a.ii` | 商構成 well-definedness | spherical coherence quotient が walking signature を崩さないことを示す |
| `#22a.iii.a` | pseudomonadicity condition | BKP 1989 の条件を σ 論文固有の 2-monad へ specialize する |
| `#22a.iii.b` | solution set condition | Lack 2010 bicategorical AFT の biuniversal arrow 条件を満たす |
| `#22a.iii.c` | cofibrant replacement 整合 | Lack 2007 model structure 経由で weak/strict の移行を制御する |

### 1.3 prediction error

想定より狭かった点: C11 の未解決は「Yoneda の補題そのもの」ではない。未踏は、Yoneda を使うための **舞台生成**、つまり `SignTower` / `weak spherical 2-cat` / `F_sph ⊣ U` の existence and coherence 側に集中している。

想定より豊かだった点: `#22a.i` と `#22a.ii` は Gurski / polygraph / model-structure の 2 経路に分岐できる。片方が詰まっても、もう片方で足場を維持できる。

---

## 2. Anchor

### 2.1 証明義務 ledger

| 義務 | 必要 SOURCE | 親稿内 SOURCE | 受理条件 | 最初の作業 |
|:--|:--|:--|:--|:--|
| `#22a.i` | Gurski 2013 Ch 15 | §D.1.7 | Ch 15 の命題番号・定理名・適用範囲を直接確認する | 現状は章メタデータと節構成のみ確認。本文 PDF は HTML 返却 |
| `#22a.ii` | Gurski 2013 / Lack 2002 / Dupont 2019 / Lack 2007 | §D.1.5-1.7 | spherical coherence quotient が `source-target / arity / framing` を保存する | Lack 2002 route を `left adjoint / unit equivalence / codescent preservation` の 3 検査へ分解済み |
| `#22a.iii.a` | BKP 1989 | §III.4, §D.1.8 | `T_sph^pseudo` が BKP の 2-dimensional monad 条件を満たす | monad, strict algebra, pseudo algebra, inclusion を定義する |
| `#22a.iii.b` | Lack companion (arXiv:math/0702535) / bicategorical AFT 経路 | §D.1.3, §D.1.8 | forgetful pseudo-functor に biuniversal arrow がある | walking signature からの universal arrow を図式化する |
| `#22a.iii.c` | Lack 2007 2-monads | §D.1.7-1.8 | weak spherical 2-cat から strict presentation への cofibrant replacement が σ を保存する | `σ`, `σ*`, coherence cells の保存表を作る |
| `#22a.T1` | 親稿 §III.2-4 / §D.1.3-1.6 + Lack 2002 | §III.4, §D.1.3-1.6 | `T_sph` preliminary table が 2-monad presentation を成す | `σ*` が生成 operation か derived cell かを決める |
| `#22a.T2` | 親稿 weak spherical 2-圏定義 | §III.2, §D.1.4 | pseudo `T_sph`-algebra が weak spherical 2-category と一致する | strict / pseudo / lax presentation を分離する |
| `#22a.T3` | Lack 2002 unit equivalence + 親稿 3 不変量 | §III.4, §D.1.6 | strictification/unit equivalence が `σ`, `σ*`, source-target / arity / framing を保存する | 3 不変量を unit equivalence に載せる |

### 2.2 後続が歩ける最小成果物

次に作るべき成果物は、証明本文ではなく **C11 proof obligation map** である。構成は以下で足りる。

| 節 | 内容 |
|:--|:--|
| §1 | Claim: C11 が証明すべき命題を 1 文で固定 |
| §2 | Objects: `Sig`, `Piv2Cat`, `Sph2Cat`, `SignTower` の最小定義 |
| §3 | Walking signature: `S_triangle`, `S_n`, `F_sph(S_triangle)`, `K_n` |
| §4 | AFT route: BKP → Lack 2010 → Lack 2007 の役割分担 |
| §5 | Non-collapse route: source-target / arity / framing の保存 |
| §6 | 未取得 SOURCE: Gurski 2013 Ch 15 と代替経路 |
| §7 | `T_sph` table: operations / equations / coherence cells の列挙 |
| §8 | `#22a.T1-T3`: 2-monad presentation / pseudo algebra 一致 / σ 保存 |

### 2.3 AY

| 種別 | 新しい射 |
|:--|:--|
| epistemic | C11 の問題を「Yoneda」から「舞台生成と coherence」へ再配置できる |
| epistemic | `#22a.i`, `#22a.ii`, `#22a.iii.a-c` を別個の proof obligation として追える |
| pragmatic | 次の /ene で `C11_Yoneda経路完全化_草稿.md` を書ける |
| pragmatic | Gurski 2013 が取れない場合でも Path A/B の代替経路を維持できる |

AY = 4。

---

## 3. Momentum Check

**撤退条件**: CLEAR。現時点では新規本文へ進まず、台帳で足場を築く範囲に留まっている。
**勢い判定**: 意図的。既踏の本文統合ではなく、親稿が open として残した C11 proof-level gap への first contact である。

**次の一歩**: `C11_Yoneda経路完全化_草稿.md` §3.5 の `T_sph` preliminary table を起点に、`#22a.T1` を処理する。具体的には `σ*` が生成 operation なのか pivotal closure の derived cell なのかを決め、operations / equations が 2-monad presentation を成すかを見る。Gurski 2013 Ch 15 は章メタデータと節構成まで SOURCE 化できたが、本文定理は未取得なので proof claim に使わない。

---

## 4. Working Memory

`$direction`: C11 を sketch-level から proof-level へ引き上げる。
`$terrain`: 未踏は Yoneda 補題ではなく、weak spherical 2-cat / SignTower / AFT の舞台生成。
`$anchor`: `#22a.i`, `#22a.ii`, `#22a.iii.a-c`, `#22a.T1-T3` の 8 義務 ledger。
`$discovery`: 完全一致論文は現時点では未発見。Gurski Ch.15 は目次上まさに weak codescent / pseudo-algebra coherence へ向かっているが、本文未取得。Lack 2002 route は `left adjoint / unit equivalence / codescent preservation` の 3 検査を与える。別稿 A は、`T_sph` preliminary table から `#22a.T1` を先に潰すのが最短。
