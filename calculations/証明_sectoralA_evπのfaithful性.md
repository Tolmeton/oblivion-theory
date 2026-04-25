# 証明_sectoralA_evπのfaithful性

**作成日**: 2026-04-14  
**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` における  
`\operatorname{ev}_{\pi}` faithful 補題の外部足場。  
**対象**: `L1 Face witness lemma` + `L2 SST residue lemma`

## 0. 命題

示したいのは次である。

```text
\operatorname{ev}_{\pi} :
\mathrm{AdmPath}_{\triangle}(C,A)/\!\sim\;\to \mathrm{EndEq}_{\pi}(A)
```

が sectoral に faithful であること、すなわち

```text
\operatorname{ev}_{\pi}(\gamma_1)=\operatorname{ev}_{\pi}(\gamma_2)
⇒
\gamma_1\sim\gamma_2
```

である。

ここで重要なのは、これは「任意の path の global faithful 性」ではないという点だ。  
本面が防衛するのは、`Face 条件` と `SST 条件` を満たす `\pi`-sector の admissible path に限った faithful 性である。

## 1. SOURCE 束

### S1 Face 面

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/Face補題_ホモロジー厳密化.md`

この面が与える核は次だ。

1. 2-simplex は「穴」ではなく**照合面**である  
2. `B_1^{ver} = im(\partial_2)` が立つとき、差分は 2-face 上で syndrome として露出する  
3. 高次 simplex は 2-face の束としてしか効かず、faithful の最小検査面は 2-simplex で足りる

### S2 Face の飽和面

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/Face補題_証明修正.md`

この面が与える核は次だ。

1. nerve は `2-coskeletal` に読める  
2. `dim Ξ = 2` が検査面の最小位相である  
3. faithful のために高次 horn を新たに持ち込む必要はない

### S3 SST 面

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/incubator/legacy/力とは忘却である_v2.md`

この面が与える核は次だ。

1. 三角恒等式は `(+\lambda)+(-\lambda)=0` の相殺型を持つ  
2. 非自明な差分が消えるのは「符号付き残差が正しく対応したとき」に限る  
3. `\mathbb{R}_{\ge 0}` ではなく符号付き `\mathbb{R}` が必要

### S4 統合面

`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md`

ここで `\mathrm{Bridge}(C,A;D_C)`、`\Pi_{\mathrm{dynamic}}`、`\operatorname{ev}_{\pi}`、`\mathrm{AdmPath}_{\triangle}(C,A)` が既に置かれている。

## 2. 補題分解

### L1 Face witness lemma

`Face 条件` を満たす `\gamma_1, \gamma_2 \in \mathrm{AdmPath}_{\triangle}(C,A)` が genuinely 異なるなら、  
少なくとも一つの `\theta_*` と非退化 2-simplex `\sigma_* \subset St(E_{\gamma_i}(\theta_*))` が存在して、その差分が照合面 `B_1^{ver}` 上に露出する。

直感は単純だ。  
path の差分が本物なら、それは「道中のどこかで別の回り道をした」ということだから、その detour は 2-face の比較面に現れなければならない。

### L2 SST residue lemma

上の witness face `\sigma_*` で露出した差分が endpoint を保ったまま消えるためには、  
その局所残差が

```text
(+\lambda)+(-\lambda)=0
```

の型で記述されなければならない。

逆に言えば、この型に入らない残差は endpoint equality の保存だけでは消えない。  
したがって genuinely 異なる差分がありながら `\operatorname{ev}_{\pi}` の像だけが一致するなら、その差分はどこかの face に非自明残差を残す。

## 3. faithful 補題の骨格

### 命題

`Face Lemma` と `SST` の下で、

```text
\operatorname{ev}_{\pi} :
\mathrm{AdmPath}_{\triangle}(C,A)/\!\sim\;\to \mathrm{EndEq}_{\pi}(A)
```

は faithful である。

### 証明スケッチ

1. `\operatorname{ev}_{\pi}(\gamma_1)=\operatorname{ev}_{\pi}(\gamma_2)` を仮定する。
2. もし `\gamma_1 \not\sim \gamma_2` なら、L1 により差分はどこかの 2-simplex 検査面に露出する。
3. 露出した差分が endpoint を保ったまま消えるには、L2 により局所残差が `(+\lambda)+(-\lambda)=0` 型でなければならない。
4. しかし `\mathrm{AdmPath}_{\triangle}` では、その型に入る差分だけが reparameterization に吸収されるように admissibility が組まれている。
5. よって endpoint equality が同じで、しかも face 上に非自明残差が残らないなら、差分は genuine な構造差ではなく reparameterization 差にすぎない。

したがって

```text
\operatorname{ev}_{\pi}(\gamma_1)=\operatorname{ev}_{\pi}(\gamma_2)
⇒
\gamma_1\sim\gamma_2
```

が従う。

## 4. この補題がしている仕事

この faithful 補題が支えているのは、`static 側は dynamic 側を潰しすぎていない` という一点である。

もしここが立たなければ、`e^{i\pi}+1=0` は動的 path data から induced された静的読解ではなく、  
複数の genuinely 異なる path を同じ式へ押しつぶした粗い quotient に落ちる。  
そのとき Verdict は A ではなく B に落ちる。

## 5. 境界

この面がまだ言っていないことは明確である。

1. global faithful を証明してはいない  
2. `Face Lemma` と `SST` 自体の本証明をここで再演していない  
3. recoverability までは主張していない

したがって本面の射程は、

```text
\pi-sector の endpoint evaluation が
path 差分を十分に識別できる
```

までで止まる。
