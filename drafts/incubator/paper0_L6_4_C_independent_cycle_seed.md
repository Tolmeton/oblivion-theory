# Paper 0 L6.4-C independent cycle supply seed

| 項目 | 内容 |
|:---|:---|
| **状態** | incubator / appendix seed |
| **型** | proof seed |
| **昇格先** | Paper 0 appendix / §6.4 footnote / `論文0_忘却の忘却_草稿.meta.md` |
| **failure condition** | Lawvere 非依存に `N(L_{\le a})` 側の独立 cycle と `N(P_{\le a,b})` からの非到達性を同時に示せない場合、C5 の「第二証明」主張は保留し、Lawvere 依存の位相的読解に留める |
| **親稿** | `drafts/series/論文0_忘却の忘却_草稿.md` v0.17 |
| **作成日** | 2026-04-29 |
| **対象** | Paper 0 §6.4 L6.4-C |
| **役割** | C5「不完全性の幾何学的起源」のうち、意味側に証明可能部分から閉じられない独立 cycle が供給されるかを、L6.4-A の二重 filtration 上で温める |

---

## 0. 一文核

L6.4-C が示すべきことは、単に「証明不能な文がある」ではない。L6.4-A の二重 filtration

```text
P_{\le a,b}(\mathcal T) subset L_{\le a}(\mathcal T)
```

の上で、`N(L_{\le a})` には 1-cycle が立ち、その homology class が `N(P_{\le a,b})` からの像では閉じられない、という非全射性である。

本 seed はこの非全射性をまだ証明しない。証明を 4 小補題へ分解し、どこが Lawvere 依存を再導入しやすいかを見える形にする。

---

## 1. 記法衛生

| 記号 | 意味 |
|:---|:---|
| `\mathcal T` | 有限アルファベット上の再帰的な証明体系 |
| `L_{\le a}(\mathcal T)` | 式複雑度 `<= a` の文クラスから作る有限 poset |
| `P_{\le a,b}(\mathcal T)` | `L_{\le a}` のうち、長さ `<= b` の証明から到達する文クラス |
| `N(-)` | poset の nerve |
| `k` | 係数体 |
| `i_{a,b}` | 包含 `N(P_{\le a,b}) -> N(L_{\le a})` |

本文の単一添字 `n` は、L6.4-A seed の cofinal schedule `s(n)=(a(n),b(n))` による略記として読む。

---

## 2. L6.4-C の補題候補

**補題候補 L6.4-C.** `\mathcal T` が `Q` を表現できる無矛盾な再帰的証明体系であるとする。適切な cofinal schedule `s(n)=(a(n),b(n))` に沿って、cofinal に多くの `n` で

```text
rank_k im(H_1(N(P_n(\mathcal T));k) -> H_1(N(L_n(\mathcal T));k))
  < rank_k H_1(N(L_n(\mathcal T));k)
```

が成り立つ。

この形が強すぎる場合の弱形は、ある `n` で非零の相対 class が立つ有限段階主張である。

```text
H_1(N(L_n(\mathcal T)), N(P_n(\mathcal T)); k) != 0
```

弱形は「局所的 proof gap」、強形は「永続的位相障害」を与える。

---

## 3. 4 小補題への分解

### C-1. 独立文供給

`L_{\le a}` の中に、証明可能同値で互いに潰れない文クラスの族を供給する。

必要なのは、単なる個数ではない。候補文が `P_{\le a,b}` の結論集合だけで生成される filter に吸収されないことが必要である。

**候補ルート.**

| ルート | 内容 | リスク |
|:---|:---|:---|
| R1 再帰論的分離 | r.e. な証明可能集合と、構文的に生成される文クラス全体の差を使う | 対角化を別名で再導入しやすい |
| R2 有限段階 counting | `L_{\le a}` の Boolean subalgebra の自由度と `P_{\le a,b}` の生成自由度を比較する | counting だけでは cycle 非到達にならない |
| R3 Stone duality 読解 | Lindenbaum 代数の有限近似を clopen 分割として読み、証明可能 filter の覆えない穴を見る | 位相語彙が強くなりすぎる |
| R4 proof-complexity gap | 短い式だが長い証明を要する族を使う | 外部定理依存が増える |

### C-2. cycle 実現

独立文クラスから、`N(L_{\le a})` の 1-cycle を構成する。

初期候補は Boolean square だった。

```text
[0] < [A] < [A∨B] > [B] > [0]
```

ただし R2 toy model により、この候補はそのままでは失敗すると判定した。full Boolean poset の nerve は最小元または最大元で cone になり、Boolean square の proper part は 2 点にしかならない。最小の 1-cycle 候補は `B_3^\circ = B_3 \setminus {0,1}` の proper-part nerve である。

参照: `drafts/incubator/paper0_L6_4_C_R2_counting_toy_model.md`

**要件.**

| 要件 | 内容 |
|:---|:---|
| C2-a | cycle を作る文クラスが `L_{\le a}` に入る |
| C2-b | その cycle が full poset nerve ではなく、proper-part / relative / cover nerve 上で boundary として潰れない |
| C2-c | quotient によって構文上の差が証明可能同値へ潰れない |

### C-3. 証明像からの非到達

構成した cycle class が

```text
im(H_1(N(P_{\le a,b});k) -> H_1(N(L_{\le a});k))
```

に入らないことを示す。

ここが L6.4-C の本体である。`P_{\le a,b}` が小さい、というだけでは足りない。`P_{\le a,b}` の nerve から来る cycle が、対象 cycle と同じ homology class を代表できないことが必要である。

**証明候補.**

1. `P_{\le a,b}` の 1-skeleton が対象 cycle の少なくとも 1 辺を欠く。
2. 欠けた辺を `P_{\le a,b}` 内の別経路で補えない。
3. `L_{\le a}` 内では閉じているが、`P_{\le a,b}` 内では閉じない obstruction として残る。

### C-4. persistence / cofinality

有限段階で立った class が、次の filtration 段階で即座に消えるなら、局所的穴に留まる。大域的障害にするには、少なくとも cofinal な段階で class が残る必要がある。

**三段階の主張水準.**

| 水準 | 内容 | C5 への効き方 |
|:---|:---|:---|
| finite | ある `(a,b)` で非零 class がある | 局所的 proof gap |
| persistent | 非零 class が長い interval で残る | 計算可能な位相障害 |
| cofinal | cofinal に class が供給される | C5 Step 2 の強形 |

---

## 4. Lawvere 非依存性の検査

L6.4-C では、Lawvere を「踏み台」として使わない。したがって次を禁止する。

| 禁止 | 理由 |
|:---|:---|
| CCC の点全射非存在を仮定する | Step 1 に戻るだけで、第二証明にならない |
| ゲーデル文そのものを cycle source にする | 算術的対角を再導入する |
| 「独立文が無限にある」とだけ書く | cycle / 非到達 / persistence が抜ける |
| 濃度差だけで非全射を結論する | homology class の代表可能性を見ていない |

許されるのは、証明列挙の r.e. 性、有限構文、式複雑度、証明長、有限 poset の nerve、相対ホモロジーの長完全列である。

---

## 5. 現時点の主観

[主観] R2 の有限段階 counting は最初の足場として使えるが、それだけでは弱い。toy model の結果、full poset nerve は使えない。最も筋がよいのは、proper Boolean 3 の 1-cycle を候補生成に使い、C-3 で「証明像から同じ class を代表できない」ことを別に示す二段構えである。R1 は強力だが、対角化の別名になりやすいので、本 seed では第一選択にしない。

---

## 6. 失敗条件

| 失敗 | 影響 |
|:---|:---|
| `N(L_{\le a})` の自然な 1-cycle が構成できない | C5 Step 2 は Betti 数不等式ではなく比喩に留まる |
| cycle がすべて 2-simplex で埋まる | nerve choice を変更するか、poset ではなく cover nerve へ移る |
| 非到達性が濃度差にしか依存しない | homology 主張として弱い。C-3 に戻る |
| Lawvere またはゲーデル対角を暗黙に使う | 「第二証明」は撤回し、Lawvere の位相的読解へ降格する |
| class が filtration で即消滅する | 大域障害ではなく finite-stage obstruction として扱う |

---

## 7. 次の作業

1. `B_3^\circ` cycle を L6.4-C の C-2 第一候補として定式化する。
2. C-3 の「同じ homology class を代表できない」条件を、辺欠損・経路欠損・relative chain のどれで書くか決める。
3. 本文 §6.4 の `N(L(T))` を、proper-part / relative / cover のどれに分岐させるか判断する。
4. 成功しない場合でも、finite obstruction として Paper 0 appendix に戻せる最小形を残す。
