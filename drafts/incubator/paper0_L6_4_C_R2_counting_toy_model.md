# Paper 0 L6.4-C R2 counting toy model

| 項目 | 内容 |
|:---|:---|
| **状態** | incubator / technical proof toy |
| **型** | proof seed support |
| **親 seed** | `drafts/incubator/paper0_L6_4_C_independent_cycle_seed.md` |
| **親稿** | `drafts/series/論文0_忘却の忘却_草稿.md` v0.17 |
| **作成日** | 2026-04-29 |
| **対象** | L6.4-C / R2 有限段階 counting route |
| **判定** | 素朴な full Boolean poset nerve は cycle を保持しない。C-2 は proper-part nerve / relative nerve / cover nerve へ移す必要がある |
| **failure condition** | proper-part / relative / cover のいずれでも proof gap を自然に表せない場合、R2 route は C5 の証明核ではなく探索メモへ降格する |

---

## 0. 一文核

R2 counting route の最初の toy model は、L6.4-C にとって有益だが、素朴な形では失敗する。有限 Boolean poset 全体の nerve は最小元または最大元で cone になるため、独立文から作った 1-cycle は homology class として残らない。

したがって L6.4-C の cycle 実現は、`L_{\le a}` 全体の order nerve ではなく、少なくとも次のいずれかへ移す必要がある。

```text
proper-part nerve:
  N(L_{\le a} \setminus {0,1})

relative nerve:
  N(L_{\le a}) / N(P_{\le a,b})

cover nerve:
  証明可能部分が覆えない semantic patches の nerve
```

---

## 1. toy model の設定

`m` 個の互いに独立な文クラスを、有限 Boolean algebra `B_m` の atom として近似する。

```text
B_m = P({1,...,m})
```

順序は包含である。`0 = emptyset`, `1 = {1,...,m}` とする。

証明可能部分は、`r <= m` 個の atom から生成される部分 Boolean algebra `B_r`、またはその filter 近似として置く。

```text
P_toy = < e_1, ..., e_r >
L_toy = B_m
```

この toy model の目的は、`m > r` の counting gap が homology gap を自動的に生むかを調べることである。

---

## 2. full Boolean poset nerve は失敗する

有限 poset `B_m` には最小元 `0` と最大元 `1` がある。poset の order complex / nerve は、最小元を頂点にもつ cone として潰れる。

```text
N(B_m) is contractible
```

したがって

```text
H_1(N(B_m); k) = 0
```

である。これは L6.4-C にとって重要な negative result である。

**結論.** `L_{\le a}` を full Lindenbaum poset としてそのまま nerve に送るだけでは、Boolean algebra の独立性は 1-cycle として見えない。`0` または `1` が cone point になり、cycle 候補を埋める。

---

## 3. Boolean square もそのままでは足りない

2 atom の Boolean square

```text
0 < A < A∨B > B > 0
```

は見た目には菱形だが、full poset としては `0` と `A∨B` を含む。したがって order nerve は cone 的に潰れ、非自明な `H_1` を与えない。

`{A,B}` だけを残す proper part は 2 点であり、これは `S^0` に相当する。ここにも `H_1` はない。

```text
proper(B_2) = B_2 \setminus {0,1}
            = {A, B}
H_1(N(proper(B_2)); k) = 0
```

**判定.** L6.4-C の C-2 に必要な最小 model は Boolean square ではない。

---

## 4. 最小の 1-cycle は proper Boolean 3

`B_3` の proper part

```text
B_3^\circ = B_3 \setminus {0,1}
```

は、3 個の atom と 3 個の coatom を持つ。order nerve は 6-cycle になる。

```text
{1} < {1,2} > {2} < {2,3} > {3} < {1,3} > {1}
```

これは `S^1` に相当し、

```text
H_1(N(B_3^\circ); k) = k
```

を与える。

**正の候補.** 独立文クラスが少なくとも 3 方向あり、かつ `0/1` を cone point として除去するなら、意味側に 1-cycle を作る toy model が立つ。

---

## 5. counting gap の形

`m` 個の意味側 atom があるとき、proper Boolean subalgebra の 3 atom 選択ごとに `B_3^\circ` 型の 1-cycle 候補が出る。

```text
semantic cycle candidates ~ C(m,3)
```

証明可能部分が `r` 個の atom 方向しか生成しないなら、同型の候補は高々

```text
proof-side cycle candidates ~ C(r,3)
```

である。

`m > r` なら候補数には差が出る。ただし、これはまだ homology の非全射性ではない。異なる triple が同じ homology class を表す可能性があり、また `L_{\le a}` 内の 2-simplex で埋まる可能性がある。

**R2 の使い方.** counting は C-1 の候補生成には使えるが、C-3 の非到達性は別に証明する必要がある。

---

## 6. L6.4-C への更新

この toy model から、L6.4-C seed の C-2 を次のように修正する。

| 旧い候補 | 判定 | 新しい候補 |
|:---|:---|:---|
| Boolean square | `H_1` を出さない | 捨てる |
| full Boolean poset nerve | cone で contractible | 捨てる |
| proper Boolean 3 nerve | `S^1` を出す | 第一候補 |
| relative nerve | 証明側を潰した差分を見る | 第二候補 |
| cover nerve | semantic patches の覆えない穴を見る | 第三候補 |

本文へ戻すなら、`N(L(T))` という表記は危険である。少なくとも次のどれを意味するかを明示しなければならない。

```text
N^\circ(L_{\le a})
  = N(L_{\le a} \setminus {0,1})

N(L_{\le a}, P_{\le a,b})
  = relative nerve / pair

N(\mathcal U_{\le a})
  = cover nerve of semantic patches
```

---

## 7. 次の作業

1. `B_3^\circ` cycle を L6.4-C seed の C-2 の第一候補へ昇格する。
2. C-3 では、`P_{\le a,b}` が対象 triple の atom/coatom をすべて含まない場合に、同じ `H_1` class を代表できない条件を書く。
3. 本文 §6.4 の `N(L(T))` は、将来 `proper / relative / cover` のどれかに明示的に分岐させる。
4. R2 が失敗した場合は R3 Stone duality / cover nerve route へ移る。
