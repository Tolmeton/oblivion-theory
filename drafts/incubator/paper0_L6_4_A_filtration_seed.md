# Paper 0 L6.4-A filtration seed

| 項目 | 内容 |
|:---|:---|
| **状態** | incubator / appendix seed |
| **型** | proof seed |
| **昇格先** | Paper 0 appendix / §6.4 footnote / `論文0_忘却の忘却_草稿.meta.md` |
| **failure condition** | 式複雑度と証明長の二重 filtration が L6.4-B/D の比較舞台を作れない場合は、本文補題ではなく記法案へ降格する |
| **親稿** | `drafts/series/論文0_忘却の忘却_草稿.md` v0.15 |
| **作成日** | 2026-04-26 |
| **対象** | Paper 0 §6.4 L6.4-A |
| **役割** | C5「不完全性の幾何学的起源」のうち、文空間と証明可能部分を成長速度で比較できる有限近似へ落とす |

---

## 0. 一文核

L6.4-A は、形式体系の全文空間 `L(\mathcal T)` と証明可能部分 `P(\mathcal T)` に同じ物差しを押し付ける補題ではない。式の複雑度で「意味空間の大きさ」を切り、証明長で「到達可能部分」を切る二重 filtration により、L6.4-B/D が比較する有限 poset 列を作る補題である。

本 seed は L6.4-C、すなわち「証明可能部分から閉じられない独立 cycle が十分に供給される」ことは証明しない。ここで固定するのは、その問いを測れる舞台である。

---

## 1. 記法衛生

本文 §6.4 では形式体系を `T` と書いているが、Paper 0 全体では Chebyshev 1-形式も `T` と書く。混線を避けるため、本 seed では形式体系を `\mathcal T`、形式体系上に後で導入される Chebyshev 型 1-形式を `T_L` と書く。

| 記号 | 意味 |
|:---|:---|
| `\mathcal T` | 有限アルファベット上の再帰的な証明体系 |
| `Sent(\mathcal T)` | `\mathcal T` の閉論理式の集合 |
| `[\varphi]_{\mathcal T}` | `\mathcal T` での証明可能同値による文クラス |
| `L(\mathcal T)` | Lindenbaum-Tarski 代数 |
| `P(\mathcal T)` | 証明可能文のフィルタ |
| `c(\varphi)` | 文 `\varphi` の式複雑度 |
| `\ell(\pi)` | 証明 `\pi` の証明長 |
| `N(-)` | 半順序集合の nerve |
| `T_L` | L6.4-E/F で導入予定の形式体系側 Chebyshev 型 1-形式 |

---

## 2. 二つの物差し

### 2.1 式複雑度 `c`

`c(\varphi)` は、文の構文木のサイズを測る関数として固定する。第一候補は次である。

```text
c(\varphi)
  = 記号数
    + 量化子数
    + 結合子数
    + 項構成の深さ
```

重みの選択は後で調整できる。ただし、L6.4-A に必要なのは次の 3 条件だけである。

| 条件 | 内容 |
|:---|:---|
| C-A1 | 各 `a` について `c(\varphi) <= a` を満たす文は有限個 |
| C-A2 | すべての文 `\varphi` は有限の `c(\varphi)` を持つ |
| C-A3 | 変数名変更や構文符号化の違いは、cofinal な再添字で吸収できる |

### 2.2 証明長 `\ell`

`\ell(\pi)` は、証明列の行数または証明コード長として固定する。L6.4-B に必要なのは、長さ `<= b` の証明コードが有限個であることだけである。

```text
Proof_{\le b}(\mathcal T)
  = { \pi | \pi は \mathcal T の正しい証明かつ \ell(\pi) <= b }
```

この集合は有限であり、その結論集合も有限である。

---

## 3. filtration の定義

### 3.1 意味側

式複雑度で切った有限近似を次で定義する。

```text
L_{\le a}(\mathcal T)
  = { [\varphi]_{\mathcal T} in L(\mathcal T)
      | \varphi in Sent(\mathcal T), c(\varphi) <= a }
```

順序は Lindenbaum-Tarski 代数の順序から継承する。

```text
[\varphi]_{\mathcal T} <= [\psi]_{\mathcal T}
  iff
\mathcal T |- \varphi -> \psi
```

`L_{\le a}` は、有限個の文クラスからなる有限 poset である。`a <= a'` なら包含 `L_{\le a} -> L_{\le a'}` がある。

### 3.2 証明側

証明長だけで切ると、結論の式複雑度が `a` を超えることがある。そこで証明側は二重添字で固定する。

```text
P_{\le a,b}(\mathcal T)
  = { [\varphi]_{\mathcal T} in L_{\le a}(\mathcal T)
      | exists \pi in Proof_{\le b}(\mathcal T), conclusion(\pi)=\varphi }
```

これにより常に

```text
P_{\le a,b}(\mathcal T) subset L_{\le a}(\mathcal T)
```

が成り立つ。順序は `L_{\le a}` から継承する。

### 3.3 対角 filtration

本文で単一添字が必要なときは、cofinal な計算可能スケジュール `s(n)=(a(n),b(n))` を選び、

```text
L_n(\mathcal T) = L_{\le a(n)}(\mathcal T)
P_n(\mathcal T) = P_{\le a(n), b(n)}(\mathcal T)
```

と書く。第一候補は対角 `a(n)=n, b(n)=n` である。ただし、証明長の伸びが式複雑度より速い場合は `b(n)=n^2` などの cofinal schedule へ変える余地を残す。

---

## 4. L6.4-A 補題候補

**補題候補 L6.4-A.** `\mathcal T` が有限アルファベット上の再帰的な証明体系であるとする。このとき、`L(\mathcal T)` と `P(\mathcal T)` には、有限 poset の二重 filtration

```text
P_{\le a,b}(\mathcal T) subset L_{\le a}(\mathcal T)
```

が入り、任意の cofinal schedule `s(n)=(a(n),b(n))` に対して、包含

```text
N(P_n(\mathcal T)) -> N(L_n(\mathcal T))
```

は有限単体複体の filtration を与える。

**証明骨格.**

1. `c(\varphi) <= a` の文は有限個なので、商を取った `L_{\le a}` も有限である。
2. `\ell(\pi) <= b` の証明コードは有限個なので、結論集合も有限である。
3. `P_{\le a,b}` は `L_{\le a}` との交わりとして定義されるため、包含が自動的に立つ。
4. `a <= a'` かつ `b <= b'` なら、`P_{\le a,b} -> P_{\le a',b'}` と `L_{\le a} -> L_{\le a'}` は順序を保つ。
5. nerve は順序保存写像を単体写像へ送るため、`N(P_n) -> N(L_n)` の filtration が得られる。

---

## 5. なぜ二重 filtration か

式複雑度だけで切ると、「短い式だが長い証明を要する文」を証明側へ誤って含める。証明長だけで切ると、「短い証明で得られるが式としては巨大な文」が意味側の同じ段階に入ってしまう。

二重 filtration はこの混線を避ける。

| 物差し | 測るもの | C5 での役割 |
|:---|:---|:---|
| `c(\varphi)` | 意味空間側の候補文の広がり | `L_{\le a}` の cycle 供給を測る |
| `\ell(\pi)` | 証明体系が実際に到達した範囲 | `P_{\le a,b}` の像の大きさを測る |
| `s(n)` | 比較の同時刻化 | B/D/C を同じ有限段階で比較する |

---

## 6. L6.4-B/D への接続

L6.4-B は、この seed の `P_{\le a,b}` に対して述べる。

```text
rank H_1(N(P_{\le a,b}); k)
  <= #1-simplices of N(P_{\le a,b})
  <= |P_{\le a,b}|^2
```

L6.4-D は、包含

```text
N(P_{\le a,b}) -> N(L_{\le a})
```

が誘導する写像の非全射性を、相対ホモロジーへ昇格する。

この seed が与えるのは比較可能な舞台だけである。非全射性そのもの、すなわち `L_{\le a}` 側に `P_{\le a,b}` から閉じられない cycle が残ることは L6.4-C の仕事である。

---

## 7. 失敗条件

| 失敗 | 影響 |
|:---|:---|
| 言語が有限構文でない | `L_{\le a}` の有限性が壊れる。対象を有限シグネチャへ制限する必要がある |
| `[\varphi]` の最小複雑度を使う | 計算可能性が不透明になる。本文では代表文ベースの filtration を採る |
| diagonal schedule が粗すぎる | `P_n` と `L_n` の比較が人工的になる。cofinal schedule 依存を明記する |
| 商で cycle が潰れすぎる | pre-quotient の構文 poset から quotient への射を併用して再検討する |
| 証明体系変更で成長が変わる | 主張を「符号化に対して不変」ではなく「cofinal rescaling まで不変」として述べる |

---

## 8. 次の作業

1. L6.4-C をこの二重 filtration 上で書く。標的は `N(L_{\le a})` 側に `N(P_{\le a,b})` の像で閉じられない cycle が残ること。
2. L6.4-B/D seed の `L_{\le n}, P_{\le n}` を、本 seed の `s(n)=(a(n),b(n))` 記法へ同期する。
3. 本文 §6.4 へ戻すときは、A を「証明済みの強主張」ではなく「比較対象の固定」として書く。
