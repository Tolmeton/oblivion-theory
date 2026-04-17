# 証明_sectoralA_canonical_liftとlocal_full

**作成日**: 2026-04-14  
**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` における  
`canonical lift = local full` 補題の外部足場。  
**対象**: `L3 Canonical lift lemma`

## 0. 命題

示したいのは次である。

```text
\operatorname{ev}_{\pi}\circ\operatorname{Lift}_{\pi}
=
\mathrm{id}_{\mathrm{EndEq}_{\pi}(A)}
```

したがって `\operatorname{ev}_{\pi}` は `\pi`-sector で full である。

ただしここで言う full は、`A` 全体への full ではない。  
あくまで `e^{i\pi}+1=0` を含む `\mathrm{EndEq}_{\pi}(A)` に限った local full である。

## 1. SOURCE 束

### S1 統合面

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md`

ここで既に次が置かれている。

1. `D_C(E(0))=1_A`, `D_C(E(\pi))=0_A`  
2. `U(0)=1_A`, `\frac{dU}{d\theta}=iU`, `U(\pi)=-1_A`  
3. `\alpha_E(\theta)=\frac{1-\cos\theta}{2}`  
4. `\Omega(\theta)=e^{i\theta}D_C(E(0))`

### S2 補題束の足場

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_sectoralA_補題束の足場.md`

ここで `L3` は

```text
q_{\pi} が標準 path へ持ち上がる
```

という役割で固定済みである。

## 2. sector の定義

`\mathrm{EndEq}_{\pi}(A)` は、次の境界条件と位相輸送法則に両立する endpoint equalities の類である。

```text
D_C(E(0))=1_A,\qquad D_C(E(\pi))=0_A
```

```text
U(0)=1_A,\qquad \frac{dU}{d\theta}=iU,\qquad U(\pi)=-1_A
```

現在の草稿では、この sector は事実上

```text
e^{i\pi}+1=0
```

の typed representative を持つ局所 class である。

## 3. canonical lift

`q_{\pi} \in \mathrm{EndEq}_{\pi}(A)` に対し、標準持ち上げを

```text
\operatorname{Lift}_{\pi}(q_{\pi})(\theta)
:=
\bigl(
\alpha_E(\theta),
C_{\alpha_E(\theta)},
e^{i\theta}D_C(E(0)),
\operatorname{Im}(e^{i\theta}D_C(E(0)))
\bigr)
```

で定める。

この式の意味は、終点等式を「そのまま path に戻す」ことではない。  
Euler 累積公理が与える標準 path を使って、`\pi`-sector の endpoint read を**canonical な運動**へ戻している。

## 4. local full の骨格

### 命題

上の `\operatorname{Lift}_{\pi}` は

```text
\operatorname{ev}_{\pi}\circ\operatorname{Lift}_{\pi}
=
\mathrm{id}_{\mathrm{EndEq}_{\pi}(A)}
```

を満たす。

### 証明スケッチ

1. `\operatorname{Lift}_{\pi}(q_{\pi})` は `\alpha_E` と `C_{\alpha_E(\theta)}` により、忘却濾過の標準 path を与える。
2. `e^{i\theta}D_C(E(0))` は位相輸送 `U(\theta)` と `D_C(E(0))=1_A` の積に一致する。
3. よって終点 `\theta=\pi` では

```text
\Omega(\pi)+D_C(E(0))=D_C(E(\pi))
```

すなわち

```text
e^{i\pi}+1=0
```

がそのまま回収される。
4. したがって `\operatorname{ev}_{\pi}` で終点評価を取ると、始めに与えた `q_{\pi}` に戻る。

よって `\operatorname{Lift}_{\pi}` は `\pi`-sector 上の section であり、`\operatorname{ev}_{\pi}` は local full である。

## 5. この補題がしている仕事

この補題が支えているのは、`static 側の式は dynamic 側から本当に持ち上げ直せる` という一点である。

もし canonical lift が立たなければ、`e^{i\pi}+1=0` は path data から induced された静的読解ではなく、  
あとから貼られた別置きの式に戻る。  
その瞬間、A は壊れて B に落ちる。

## 6. 境界

この面がまだ言っていないことは明確である。

1. `\mathrm{EndEq}(A)` 全体への full は主張していない  
2. arbitrary endpoint class への lift theorem は与えていない  
3. global A の十分条件にはまだ届いていない

したがって本面の射程は、

```text
\pi-sector の endpoint identity は
canonical な Euler path を持つ
```

までで止まる。
