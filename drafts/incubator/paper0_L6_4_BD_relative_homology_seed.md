# Paper 0 L6.4-B/D 相対ホモロジー補題 seed

| 項目 | 内容 |
|:---|:---|
| **状態** | incubator / appendix seed |
| **型** | proof seed |
| **昇格先** | Paper 0 appendix / `論文0_忘却の忘却_草稿.meta.md` |
| **failure condition** | L6.4-C が独立 cycle の供給を支えられない場合、本 seed は条件付き補題に留め、C5 の証明核としては昇格しない |
| **親稿** | `drafts/series/論文0_忘却の忘却_草稿.md` v0.15 |
| **作成日** | 2026-04-26 |
| **対象** | Paper 0 §6.4 L6.4-B / L6.4-D |
| **役割** | C5「不完全性の幾何学的起源」のうち、証明側成長上界と相対ホモロジー昇格だけを独立に温める |

---

## 0. 一文核

L6.4-B/D は、C5 全体の最難関ではない。ここで示すべきことは、証明可能部分から来る cycle が有限に制御され、しかも全文空間側に閉じられない cycle が残るなら、その差は相対ホモロジーとして非零に立つ、という条件付き補題である。

本 seed は L6.4-C の核心、すなわち「意味側の独立 cycle が Lawvere に依存せず十分に供給される」ことは証明しない。そこは別 seed に分ける。

---

## 1. 記法衛生

本文 §6.4 では形式体系を `T` と書いているが、Paper 0 全体では Chebyshev 1-形式も `T` と書く。混線を避けるため、本 seed では形式体系を `\mathcal T` と書く。

| 記号 | 意味 |
|:---|:---|
| `\mathcal T` | 無矛盾な形式体系 |
| `L(\mathcal T)` | Lindenbaum-Tarski 代数。文を証明可能同値で割った Boolean 代数 |
| `P(\mathcal T)` | 証明可能文のフィルタ |
| `L_{\le n}(\mathcal T)` | L6.4-A seed の cofinal schedule による文空間の有限近似 |
| `P_{\le n}(\mathcal T)` | L6.4-A seed の cofinal schedule による証明可能部分の有限近似 |
| `N(-)` | 半順序集合の nerve |
| `k` | 係数体。相対ホモロジー / コホモロジーはまず `k` 係数で扱う |

---

## 2. L6.4-B: 証明側成長上界

**主張候補.** `P_{\le n}(\mathcal T)` は証明コードで生成される有限集合である。したがって `N(P_{\le n}(\mathcal T))` は有限単体複体であり、

```text
rank_k H_1(N(P_{\le n}(\mathcal T)); k)
  <= dim_k C_1(N(P_{\le n}(\mathcal T)); k)
  <= # comparable pairs in P_{\le n}(\mathcal T)
  <= |P_{\le n}(\mathcal T)|^2
```

が成り立つ。

**本文への注意.** 以前の「rank は `|P_n(T)|` 以下」という形は強すぎる可能性がある。証明可能候補としては、まず `1-simplex` 数による上界、すなわち `|P_{\le n}|^2` 程度の多項式上界に弱める方が安全である。C5 に必要なのは、証明側の `H_1` が証明列挙で制御されることなので、線形上界である必要はない。

**証明骨格.**

1. 長さ `\le n` の証明コードは有限個である。
2. その結論集合 `P_{\le n}(\mathcal T)` も有限個である。
3. 有限 poset の nerve の `H_1` の rank は、1-chain 群の次元を超えない。
4. 1-chain 群の次元は nerve の辺数、すなわち比較可能 pair 数で抑えられる。
5. 比較可能 pair 数は高々 `|P_{\le n}|^2` である。

**L6.4-A との接続.** `L_{\le n}` と `P_{\le n}` は、`drafts/incubator/paper0_L6_4_A_filtration_seed.md` の二重 filtration を cofinal schedule で単一添字化したものとして読む。本文用には、式複雑度と証明長を同一視しない。

---

## 3. L6.4-D: 相対ホモロジー昇格

**主張候補.** 有限近似または適切な極限で、包含

```text
nu: N(P_{\le n}(\mathcal T)) -> N(L_{\le n}(\mathcal T))
```

が誘導する写像

```text
nu_*: H_1(N(P_{\le n}(\mathcal T)); k)
      -> H_1(N(L_{\le n}(\mathcal T)); k)
```

が全射でないなら、

```text
H_1(N(L_{\le n}(\mathcal T)), N(P_{\le n}(\mathcal T)); k) != 0
```

が従う。係数体 `k` 上では、有限次元または適切な局所有限条件のもとで

```text
H^1(N(L_{\le n}(\mathcal T)), N(P_{\le n}(\mathcal T)); k) != 0
```

へ双対化できる。

**証明骨格.** pair `(X,A) = (N(L_{\le n}), N(P_{\le n}))` の長完全列を見る。

```text
H_1(A;k) --i_*--> H_1(X;k) --j_*--> H_1(X,A;k) --partial--> H_0(A;k)
```

`i_*` が全射でないなら、`H_1(X;k)` の中に `im(i_*)` に入らない class がある。その class の `j_*` 像は exactness により非零でなければならない。よって `H_1(X,A;k) != 0`。

**極限での注意.** 各 `n` で非零でも、極限で class が消える可能性がある。したがって本文へ昇格するには、次のいずれかが必要である。

| 選択 | 必要条件 | 効果 |
|:---|:---|:---|
| 有限段階主張 | ある十分大きい `n` で非零 class を示す | 局所版 C5 |
| cofinal 主張 | 非零 class が cofinal な `n` で持続する | 永続的位相障害 |
| persistent homology 版 | filtration 上の barcode として nontrivial interval を示す | 実験・計算に接続しやすい |

---

## 4. L6.4-C への接続

L6.4-B と L6.4-D だけでは C5 は成立しない。必要なのは、L6.4-C が与える非全射性である。

```text
rank im(H_1(N(P_{\le n})) -> H_1(N(L_{\le n})))
  < rank H_1(N(L_{\le n}))
```

を Lawvere の不動点定理に依存せず示せるなら、L6.4-D により相対ホモロジー class が立つ。

ここでの核心は、「証明可能部分が足りない」ことではなく、「証明可能部分では閉じられない cycle が意味空間側に残る」ことである。単なる濃度差では弱い。cycle として閉じ、かつ `P_{\le n}` からの像で潰れないことを示す必要がある。

---

## 5. 失敗条件

| 失敗 | 影響 |
|:---|:---|
| filtration が自然でない | L6.4-A に戻る。B/D は条件付き補題に留まる |
| `N(L_{\le n})` の cycle が nerve choice に依存しすぎる | 位相的障害ではなくモデル依存の人工物へ降格 |
| L6.4-C が Lawvere なしに立たない | 「対角論法から独立した第二証明」は保留 |
| `H^1` class が極限で消える | 有限段階障害に留まり、大域障害とは言えない |

---

## 6. 次の作業

1. L6.4-C を別 seed に切り出す。ここだけが Lawvere 非依存化の本丸である。
2. L6.4-B を本文用には `|P_{\le n}|^2` 上界で維持する。線形上界は使わない。
3. L6.4-D を appendix に入れる場合、長完全列の 5 行証明で足りる。
4. A/B/D の seed 記法を、本文 §6.4 の単一添字 `n` と矛盾しないように同期する。
