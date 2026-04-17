# Face Lemma の符号理論的再読

**役割**: Face Lemma と Coherence Defect Lemma を、Hamming / LDPC / erasure decoding の語彙で再読するための共通正本。  
**目的**: 「安定」「検出可能」「整合欠損的」「修復可能」を、曖昧な形容ではなく、忘却論内部の冗長性条件として再定義する。  
**canonical surface**: 2026-04-14 現在、Coherence Defect Lemma の主表示は chain 側の `H_2^{coh}` ではなく、cochain 側の `H^2_{\Theta}` に置く。

---

## 0. 一文核

Face Lemma は **圏論版 syndrome 条件** であり、Coherence Defect Lemma は **局所 forgetting law の大域持ち上げ障害** を測る次段補題である。`carry defect` はその局所 representative、`H^2_{\Theta}` は座標変換で消えない class として読む。

---

## 1. 二つの軸

忘却論では、誤り検出構造を少なくとも二つの軸に分けて見なければならない。

| 軸 | 忘却論で見ているもの | 符号理論での直感 |
|:---|:---|:---|
| **横** | 同一階層の中で別ルート比較ができるか | syndrome / parity check |
| **縦** | その比較機構がそもそも定義可能か | data bit と check bit の同時消失禁止 |

Face Lemma は主に横軸の最小条件を与える。  
Coherence Defect Lemma は、その横軸で立った複数の比較面に書かれた局所法則が、**大域的に一つの law へ貼り合わさるか**を測る。  
n-cell tower の排他制約は、これらの検査機構が意味を失わないための縦条件を与える。

---

## 2. Hamming / LDPC / Face Lemma / Coherence Defect Lemma / n-cell tower 対応表

| 観点 | Hamming | LDPC | Face Lemma | Coherence Defect Lemma | n-cell tower |
|:---|:---|:---|:---|:---|:---|
| **主役** | 少数のパリティ検査式 | 疎な多数の検査式ネットワーク | 3射が閉じる 2-simplex | 局所 forgetting law の 2-cocycle class | $U_n$ 系列の縦依存 |
| **冗長性の担体** | 検査ビット | Tanner graph 的な多重拘束 | 第3の射 $h$ | `carry defect` とその class $H^2_{\Theta}$ | 下位層を前提に上位層が立つこと |
| **何を比べるか** | 受信語と検査式 | 局所整合の束 | $g \circ f$ と $h$ | 局所 law が大域 1-cochain に吸収されるか | $U_n$ が消した対象を $U_{n+1}$ が必要とするか |
| **検出信号** | syndrome $\neq 0$ | unsatisfied checks | 合成ドリフト / carry defect / 曲率 | non-trivial coherence-defect class $[\omega_{\Theta}] \in H^2_{\Theta} \neq 0$ | 上位検査の定義域消失、または欠損の露出 |
| **主な果実** | 局所検出 | 分散局在化と反復修正 | 最小 detectability | structural non-globalizability / topological residual | 検査機構の可定義性 |
| **壊れ方** | 検査ビットも失うと silent error | trapping set / check erasure | 2射に退化すると方向が見えない | face ごとの law はあるが一つの global law に閉じない | $U_n$ と $U_{n+1}$ が同時活性だと定義不能 |
| **位置づけ** | 最小の誤り検出模型 | 分散拘束模型 | 最小の構造検出模型 | 最小の整合欠損測度 | 検出模型の存在条件 |

---

## 3. なぜ Hamming より LDPC に近いか

Hamming は Face Lemma の局所模型として非常に良い。  
だが忘却論が必要とするのは、単一の三角形ではなく、**複数の face が重なったときに何が起こるか**である。

したがって対応は次のように読むのが自然である。

- **Hamming** = Face Lemma の最小検出模型
- **LDPC** = 多数の Face Lemma を貼り合わせた分散拘束模型
- **Coherence Defect Lemma** = その貼り合わせが一つの global law に閉じるのか、obstruction / topological residual を残すのかを分ける補題
- **n-cell tower** = それらの検査面が意味を持つための縦の依存台帳

重要なのは、LDPC 類比の果実を repair 一辺倒で読まないことである。  
比較面が多いほど復元しやすくなることもあるが、逆に**局所 law の束だけが残って global law に閉じない**なら、それは修復の入口ではなく障害物である。

---

## 4. 四概念の再定義

### 4.1 安定 `stable`

忘却論において安定とは、

> **部分忘却の後でも、縦に定義可能性が残り、横に少なくとも一つの非退化 2-simplex が残る状態**

である。

これは「壊れない」という意味ではない。  
むしろ、「壊れてもまだ比較面が残る」という意味である。

### 4.2 検出可能 `detectable`

検出可能とは、

> **残存する独立経路比較によって、欠損が defect として非零に露出する状態**

である。

符号理論的には syndrome が立つことに対応する。  
Face Lemma では、これは 3射があり $g \circ f$ と $h$ を突き合わせられることに対応する。

### 4.3 整合欠損的 `coherence-defective`

整合欠損的とは、

> **各 face では局所 forgetting law が書けても、それらが大域的には一つの 1-cochain に吸収されない class が残る状態**

である。

Paper II の本文と揃えるため、主表示は cochain 側に置く。  
対象 $x$ に対し

```text
C^1_nd(St(x);k) --d^1--> C^2_nd(St(x);k) --d^2--> C^3_nd(St(x);k)
Z^2_Θ(x) := ker(d^2)
B^2_Θ(x) := im(d^1)
H^2_Θ(x) := Z^2_Θ(x) / B^2_Θ(x)
```

とすると、

- `ω_Θ` = 局所 forgetting law の mismatch を表す 2-cocycle representative
- `B^2_Θ` = 1-cochain の再定義で吸収できる mismatch
- `[ω_Θ] ≠ 0 ∈ H^2_Θ` = 吸収できない整合欠損 class が残る

を意味する。

直感的には、「各三角形の上では話が合っているが、三角形どうしを貼ると一つの世界像に閉じない」状態である。これが **structural non-globalizability** であり、相補性の非可消な残差を与える。

### 4.4 修復可能 `recoverable`

修復可能とは、

> **残存する複数の face と右随伴 $N$ により、失われた構造を一意または収縮的に再構成できる状態**

である。

重要なのは、**`H^2_{\Theta} = 0` だけでは recoverable と言えない** ことである。  
`H^2_{\Theta} = 0` が与えるのは、局所 mismatch が cochain の再定義で吸収できることだけである。実際の修復には、

- face の重なりによる局在化
- n-cell tower による縦の可定義性
- 右随伴 $N$ の decoder 条件

が追加で必要になる。

`localizable` はこのうち最初の条件を指す operational な概念であり、現時点では本文の canonical 四分法にはまだ上げず、`drafts/infra/FaceLemma_修復可能性設計.md` で管理する。

---

## 5. 関係式

四概念の関係は次のように読む。

```text
stable              = 比較面がまだ立っている
detectable          = その比較面に欠損が実際に現れる
coherence-defective = 局所 law の mismatch が class として残る
recoverable         = 現れた欠損から元の構造を戻せる
```

したがって:

- 安定でも、欠損が盲点方向に落ちれば未検出でありうる
- 検出できても、`[\omega_{\Theta}] \neq 0` なら構造的に修復不能でありうる
- `H^2_{\Theta} = 0` でも、decoder 条件がなければ recoverable とは言えない

`detectable → recoverable` を直結させないことが、このノートの核心である。

---

## 6. 忘却は bit-flip か erasure か

この対応を使うとき、忘却は bit-flip より **erasure** に近い。

- bit-flip: 値が別の値に化ける
- erasure: 値や関係が「そこにあったはずだが欠けた」状態になる

忘却論の $U_n$ は、多くの場合「値を反転する」より「構造を落として定義域を痩せさせる」作用である。  
したがって符号理論対応の主戦場は、Hamming 距離より **erasure decoding** の側にある。

Coherence Defect Lemma の `H^2_{\Theta}` も、この erasure 的読みとよく噛み合う。そこでは「値が変わった」のではなく、「局所 law はあるが、それを global law へ貼り合わせる糊が欠けている」と読むからである。

---

## 7. Face Lemma と n-cell tower の接続

両者の接続は次の一文に圧縮できる。

> Face Lemma は「検査面が立つ最小条件」を与え、Coherence Defect Lemma は「その面上の局所法則が global law に閉じるかどうか」を与え、n-cell tower は「その検査面と法則が意味を持ち続けるために隣接層を同時に失ってはならない条件」を与える。

言い換えれば:

- **Face Lemma** = 横の detectability
- **Coherence Defect Lemma** = 横の non-globalizability
- **n-cell tower 排他性** = 縦の definability

両者がそろって初めて、忘却は単なる崩壊ではなく「検出可能で、しかも一つの global law に畳み込めない残差を持ちうる構造変形」として読める。

---

## 8. 論文内での推奨文言

論文本文で短く言うなら、次の文が核になる。

> Face Lemma は圏論版 syndrome 条件であり、3射は欠損を露出させる最小の検査面である。Coherence Defect Lemma は、各 face では書ける forgetting law が、大域的には一つの 1-cochain に貼り合わさらないことを測る。

少し長く言うなら、次でもよい。

> 安定とは、部分忘却の後でも別ルート比較が残ることであり、検出可能とはその比較に欠損が defect として現れることであり、整合欠損的とは局所 forgetting law の mismatch が class として残ることであり、修復可能とは残存する複数の face と右随伴によって欠損を再構成できることである。

---

## 9. Negativa

このノートでまだ主張しないことを固定する。

1. Face Lemma 自体を holes の定理へ置き換えない
2. `H^2_{\Theta} \neq 0` の一般非自明性を、すべての CPS 圏については主張しない
3. `H^2_{\Theta} = 0` から recoverability を直結しない
4. `carry defect` と class `[\omega_{\Theta}]` を混同しない
5. `H^2` torsion を既視感・違和感・未決の問いへ直接読む強い意識解釈は本文へ上げない
6. `localizable` をまだ canonical 四分法へ昇格させない

---

## 10. 開いた課題

1. **`H^2_{\Theta} \neq 0` の最小インスタンスを QM で構成できるか**
2. **FTC を non-obstructed な対照例として一般形まで持ち上げられるか**
3. **右随伴 $N$ を decoder と読むための収縮条件をどう定式化するか**
4. **LDPC/Tanner graph に対応する「face の貼り合わせ圏」をどう定義するか**
5. **`localizable` と `coherence-defective` の階層差を本文へ上げるべきか**
6. **`carry defect` と `H^2` class の automath bridge をどう書くか**

現段階では、detectability までは強く言える。  
Coherence Defect Lemma は `H^2_{\Theta}` を主表示とする **conjectural surface** として本文へ上げられる。  
recoverability は今後の open problem として扱うのが正確である。

**2026-04-14 進捗**: QM 第一候補については `calculations/計算_QM_H2Theta最小インスタンス.md` を追加した。そこでは `V=\mathbb{R}^2` 上の標準シンプレクティック 2-cocycle を用いて、`carry defect` の representative と `H^2_{\Theta}` の class を分ける最小計算を固定している。ただしこれは existence probe であり、本文主張の昇格ではない。

**2026-04-15 進捗**: FTC 対照例として `calculations/計算_FTC_H2Theta対照例.md` を追加した。そこでは可縮な区間上の FTC 最小模型で、forgetting law `Θ` が global potential `Λ` から来る exact 1-cochain であり、obstruction class `[ω_Θ]` が立たないことを固定した。これにより

```text
QM  = obstructed candidate
FTC = non-obstructed contrast
```

の pair が calculations 面で揃った。ただし FTC の全 de Rham 一般化まではまだ主張しない。

**2026-04-15 selector 進捗**: `calculations/計算_H2Theta_selector条件面.md` を追加した。そこで、

- trivial side: `global potential / contractible patching`
- nontrivial side: `alternating witness / central extension`

という十分条件の二極を theorem candidate surface として固定した。まだ必要十分条件ではないが、`H^2_{\Theta}` を単なる存在/不存在ではなく **selector** として読む足場ができた。

**2026-04-15 lift 進捗**: `calculations/計算_H2Theta_selector_CPS内在化条件.md` を追加した。そこで、

- `contractible presentation` → `CPS-globalization atlas + zero holonomy`
- `additive witness` → `CPS-obstruction witness + irreducible orientation`

という翻訳を固定し、selector の十分条件を FTC/QM の外部語ではなく CPS1 / CPS2 / CPS5 / Face Lemma の内部語へ寄せた。ただし package 条件の最小性はまだ未検証である。

**2026-04-15 weak-package 進捗**: `calculations/計算_H2Theta_selector_package弱化テスト.md` を追加した。そこで、

- trivial side を `support-local re-lift + generator-face zero holonomy`
- nontrivial side を `support-local faithful witness + anti/symmetric separation`

まで削れる見通しを立てた。これにより selector の芯は `full package` ではなく `support-locality` と `generator-face sufficiency` にある、という読みが前面に出た。ただし弱化しすぎていないかの反例探索はまだ未了である。

**2026-04-15 counterexample 進捗**: `calculations/計算_H2Theta_selector_weakpackage反例探索.md` を追加した。そこで、`Weak Lift A'` は false trivialization、`Weak Lift B'` は false obstruction を起こしうることを failure mode として固定し、minimal guard を抽出した。現時点の最小候補は、

- trivial side: `support-saturated + triple-overlap-consistent + gauge-stable`
- nontrivial side: `coboundary-conservative + boundary-closed + refinement-stable`

という guarded weak package である。したがって次の blocker は「weak package の有無」ではなく、FTC/QM 上で `A'' / B''` の guard probe が自然に通るかどうかである。

**2026-04-15 guard-probe 進捗**: FTC note と QM note にそれぞれ `A'' / B''` の guard probe を追加した。FTC では `gauge-stable support` と `triple-overlap consistency` が local primitive patching の側から自然に通り、QM では `coboundary-conservative witness` と `refinement-stable anti/symmetric separation` が symplectic 2-cocycle の側から自然に通ることを固定した。これにより FTC/QM pair は単なる `trivial / nontrivial` ではなく、

- `FTC = guarded non-obstructed side`
- `QM = guarded obstructed side`

として読める段階に進んだ。したがって次の blocker は guard そのものの有無ではなく、`A'' / B''` を本文語へ圧縮するかどうかの判断へ移る。

**2026-04-17 naming 進捗**: front-stage / backstage の二層語彙を固定した。読者向けの本文語は

- `FTC = 貼合側`
- `QM = 残差側`

とし、`§3.4.6` では `H^2_{\Theta}=0` の側を「局所 law が一つに貼り合わさる側」、`[\omega_{\Theta}] \neq 0` の側を「局所整合の残差 class が残る側」として読む。これに対し calculations / meta の防衛面では guarded package `A'' / B''` を backstage 名として保持する。以後、front-stage では pair 語、backstage では guard 条件という二層運用で行く。

---

## 11. 次の足場

recoverability を open problem のまま宙づりにせず、次の踏み込み先を固定したノートとして `drafts/infra/FaceLemma_修復可能性設計.md` を置く。

そこでは、

- 単一 face では detectability 止まりであること
- face の重なりが localizability を与えること
- `H^2_{\Theta}` が non-globalizability を測ること
- n-cell tower の縦条件が recoverability の可定義性を支えること
- 右随伴 $N$ を decoder と読むための条件

を、段階差として分離している。
