# α_I → α_III formal bridge — 下書き

**v0.1 (2026-04-21)**
**正本パス**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/incubator/α_I_α_III_formal_bridge_草稿.md`
**型**: bridge note
**昇格先**: `drafts/リファレンス/統一記号表.md` / Paper III-VIII-XII bridge / appendix
**failure condition**: `α_I` と `α_III` の橋が座標アーティファクト以上の内容を持たない、または `sgn(α_III)` の後段読解を支えられない場合は統一記号表へ昇格しない。

本文書は、Paper I の `α_I` と Paper III の `α_III` のあいだに置ける**最小の formal bridge** を先に固定するための内部草稿である。狙いは「完全証明」ではなく、どこまでが SOURCE で、どこからが推論かを切り分けたうえで、系列統制面で使える橋の spine を先に作ることにある。

---

## §0. 目的と境界

### 0.1 目的

1. `α_I` と `α_III` がともに `ℝ` 値の連続パラメータであることを明示し、見かけの定義域衝突を解く
2. Paper I の結合項 `(α_I/2)ΦT_i` を、Paper III の `α`-接続族から見た**テンソル的内容**として読み替える
3. `sgn(α_III)` を独立パラメータではなく、`α_I = α_III` の**後段読解**として位置づける

### 0.2 境界

本文書はまだ次をしない。

- `α_I → α_VIII` の橋を与えない
- `α_eff`, `α_CPS` までを含む全鎖統一を与えない
- Paper III の anti-copy / 反-Markov 公理を Paper I 単独から導出しない
- 座標アーティファクトを完全に消した厳密証明をまだ与えない

---

## §1. SOURCE 固定点

### 1.1 Paper I 側で固定してよいこと

**SOURCE**

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文I_力としての忘却_草稿.md` §2.2, §3.2, §3.3
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文I_力としての忘却.meta.md`

**固定点**

1. `α_I ∈ ℝ` は連続パラメータとして導入される
2. 忘却接続は
   `A_i := ∂_iΦ + (α_I/2)ΦT_i`
   で与えられる
3. 忘却曲率は
   `F_{ij} = (α_I/2)[d(ΦT)]_{ij}`
   で与えられる
4. Paper I §2.2 は
   `Γ_i^(α) - Γ_i^(0) = -(α/2)T_i + (座標アーティファクト)`
   を明示し、`T_i` を `α`-接続の Levi-Civita からの逸脱の**テンソル的内容**として読んでいる

### 1.2 Paper III 側で固定してよいこと

**SOURCE**

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文III_Markov圏の向こう側_草稿.md` 冒頭, §2.2, §2.4

**固定点**

1. `α_III ∈ ℝ` は Amari の `α`-接続パラメータとして導入される
2. `α_III > 0` は `m`-接続 / Markov / bosonic 側、`α_III < 0` は `e`-接続 / anti-Markov / fermionic 側、`α_III = 0` は臨界点である
3. Paper III 自身が「Paper I-II を `α > 0` の特殊ケースとして位置づける」と宣言している
4. したがって Paper III は、少なくとも意図の上では `α_I` を別種パラメータとしては扱っていない

### 1.3 系列統制面ですでに固定されたこと

**SOURCE**

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/リファレンス/モノグラフ構成設計.md` §1.6
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/リファレンス/統一記号表.md` §1.1
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/アーティファクト/忘却論_逐次精査チェックポイントレポート.md` OP-48 周辺

**固定点**

1. `α_I / α_III / α_VIII / α_eff / α_CPS` の 5 変種が現在の系列主面である
2. 既存の formal bridge は `α_III ↔ α_VIII` に偏っており、`α_I → α_III` は未閉鎖である
3. `sgn(α_III)` は独立の α 種ではなく、`α_III` の読解層として扱う

---

## §2. 橋の直観

`α_I → α_III` の橋は、まず「別々の値域のあいだの写像」を作る話ではない。両者は最初から `ℝ` 上にいる。問題は**同じ連続値が、Paper I では局所幾何の結合強度として、Paper III では圏論的 sector を分ける接続パラメータとして読まれている**ことにある。

したがって最小橋は次の二段に分かれる。

1. **同一値の固定**  
   `α_III := α_I`
2. **読解層の追加**  
   `sgn(α_III)` により、その値が `Markov / critical / anti-Markov` のどこに属するかを読む

ここで大事なのは、`Z₂` 的な二値化は橋の入口ではなく**出口**だということである。入口はあくまで `ℝ` 値の連続パラメータである。

---

## §3. bridge の最小定義

### 3.1 記法

本稿では

- `≃_ten` = 「座標アーティファクトを捨てたテンソル的内容として一致する」

と書く。

### 3.2 読み替え写像

Paper I の局所データ

`(M, g, C, Φ, T; α_I)`

に対し、Paper III 側への**読み替え写像**

`R_{I→III}: (M, g, C, Φ, T; α_I) ↦ (M, g, C, ∇^(α_III), σ)`

を次で与える。

1. **値の同一視**
   `α_III := α_I`
2. **sector 読解**
   `σ := sgn(α_III)`
3. **結合項の読み替え**
   `Γ_i^(α_III) - Γ_i^(0) = -(α_III/2)T_i + (座標アーティファクト)`
   だから
   `(α_I/2)ΦT_i ≃_ten -Φ(Γ_i^(α_III) - Γ_i^(0))`
4. **したがって**
   `A_i = ∂_iΦ + (α_I/2)ΦT_i`
   は
   `A_i ≃_ten ∂_iΦ - Φ(Γ_i^(α_III) - Γ_i^(0))`
   と読める

### 3.3 意味

この写像が言っているのは、Paper I の `α_I` が「たまたま付いた係数」ではなく、**Levi-Civita 接続から `α`-接続へずれる量のテンソル的影**としてすでに書かれていた、ということである。

言い換えると:

- Paper I は `α` を**力の項に掛かる係数**として見せている
- Paper III は同じ `α` を**接続の向きを決める主軸**として見せている

両者は競合していない。見ている層が違うだけである。

---

## §4. 命題案

### 4.1 命題案 A

**命題案 A.** Paper I の `α_I` は、Paper III の `α_III` と同一の `ℝ` 値パラメータとして読める。Paper I の結合項 `(α_I/2)ΦT_i` は、`α_III`-接続と Levi-Civita 接続の差のテンソル的内容に対応する。したがって Paper I の正の `α_I` レジームは、Paper III の `α_III > 0` セクターの局所幾何学的前景化と読める。

**証明 spine**

1. Paper I も Paper III も `α ∈ ℝ` を採用している
2. Paper I §2.2 は `T_i` を `α`-接続の逸脱のテンソル的内容として明示している
3. よって Paper I の結合項は `α`-接続差の係数つき shadow と読める
4. Paper III の `sgn(α)` はその連続値に対する sector 読解であり、別の α 種ではない

**地位**

- SOURCE に強く支えられる
- ただし現時点では「読み替え命題」であり、まだ full formal proof ではない

### 4.2 命題案 B

**命題案 B.** `sgn(α_III)` は `α_I` から直接作る二次写像

`α_I ↦ α_III = α_I ↦ sgn(α_III)`

として読むべきであり、`α_I ↦ Z₂` を最初から一次写像とみなすべきではない。

**理由**

- Paper III 自身が `α_III ∈ ℝ` と書いている
- `α > 0 / α < 0 / α = 0` の三区分は、連続軸の上の sector 化である
- したがって `Z₂` は定義域ではなく、読解結果である

---

## §5. この bridge が閉じるもの / まだ閉じないもの

### 5.1 これで閉じるもの

1. `α_I` と `α_III` のあいだに「実数 vs Z₂」という偽の定義域衝突がある、という誤読
2. `sgn(α_III)` を独立の α 種として数える誤り
3. Paper III の「Paper I-II は `α > 0` の特殊ケース」という宣言の最小的な根拠づけ

### 5.2 まだ閉じないもの

1. `α_I < 0` を Paper I 本文の現行スコープでどう読むか
2. `F_{ij}` の符号と Paper III の `K_geom` / sector 判定を直接結ぶ定理
3. `α_I(θ)` の動力学場への昇格を、Paper III 側の点ごとの sector 遷移としてどう厳密化するか
4. `α_III → α_VIII` 以後を含む全鎖接続

---

## §6. Negativa

以下の読みは、現時点では採らない。

### 6.1 棄却 1

`α_III = sgn(α_I)` と最初から潰してしまう読み

**棄却理由**

- Paper III は `α_III` を `ℝ` 値として導入している
- 符号だけに潰すと、臨界点 `α = 0` の連続極限や強度比較が消える

### 6.2 棄却 2

`α_I → α_III` を sigmoid `η` で作る読み

**棄却理由**

- `η` は III↔VIII の橋としてすでに予約されている
- I→III は同じ `ℝ` 軸の再解釈であって、正規化写像ではない

### 6.3 棄却 3

`α_I` を `α_III` と無関係な別種パラメータとして固定する読み

**棄却理由**

- Paper I §2.2 がすでに `α`-接続差との関係を露出している
- Paper III 自身が I-II を `α > 0` 特殊ケースとして位置づけている

---

## §7. 次の実務

1. `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文I_力としての忘却_草稿.md` §2.2 または §3.2 に、`α_I` が `α_III`-接続差のテンソル的内容として読める旨の短い bridge note を差し込めるか確認する
2. `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文III_Markov圏の向こう側_草稿.md` 冒頭の notation caveat に、「Paper I の `α_I` は同じ `ℝ` 軸の局所幾何学的前景化である」と一文追加する
3. 系列統制面では、`α_I → α_III` を「値の同一視 + sector 読解 + テンソル的内容の一致」という 3 段橋で管理する

---

## §8. 現在の結論

`α_I → α_III` の formal bridge は、現段階では**新しい値域間写像の構成**ではなく、**同じ連続パラメータの層別読み替え**として書くのがもっとも筋がよい。

最小形は次の 3 行で尽きる。

1. `α_III := α_I`
2. `sgn(α_III)` は後段の sector 読解である
3. `(α_I/2)ΦT_i ≃_ten -Φ(Γ_i^(α_III) - Γ_i^(0))`

この 3 行が立てば、Paper I の `α` は Paper III の外にある孤立係数ではなく、すでに `α`-接続族の幾何学的影として読める。
