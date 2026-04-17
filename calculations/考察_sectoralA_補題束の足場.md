# 考察_sectoralA_補題束の足場

**作成日**: 2026-04-14  
**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` の `\pi`-sector A を、後続の `/ene` が補題束として実装できるように足場化する。  
**派生**: `deepen`

## P-0 Direction Reception

**方向**: `deepen`  
**対象**: `e^{i\pi}+1=0` の sectoral A を支える補題束を、`Bridge(C,A;D_C)` の言語で切り出す。  
**踏破対象**: 「A が成り立つか」ではなく、「A を支える 5 本の補題をどの既存面から起こせるか」。  

**撤退条件**

1. `canonical lift` が `\mathrm{EndEq}_{\pi}(A)` を越えて `\mathrm{EndEq}(A)` 全域の full を要求し始めたら停止  
2. `Face Lemma` と `SST` をこの面で再証明しないと sectoral A が閉じないと判明したら停止  
3. `Bridge(C,A;D_C)` の存在が Euler 累積公理だけではなく、追加の未定義構造をさらに 2 本以上要求したら停止

**判定**: `PROCEED`

## P-1 First Contact

### 想定

sectoral A の弱点は「Face/SST が存在しないこと」ではなく、それらが `\operatorname{ev}_{\pi}` の faithful/full へどう接続されるかの接続面だと想定した。

### 実態

既存面を読むと、足場は既にかなりある。

1. `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/Face補題_ホモロジー厳密化.md`  
   `B_1^{ver}` を中心に、「2-simplex は穴ではなく照合面である」という再基礎づけがある。これは `\operatorname{ev}_{\pi}` の faithful 性に必要な「検査面」を与える。

2. `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/Face補題_証明修正.md`  
   nerve の `2-coskeletal` 性と CPS-安定性が整理されている。これは「高次 simplex を持ち込まずとも 2-face で足りる」という飽和論の源泉になる。

3. `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/incubator/力とは忘却である_v2.md`  
   Stability Simplex Theorem が「三角恒等式の 3 つの読み方」として整理されている。これは `(+\lambda)+(-\lambda)=0` の残差規則を sectoral A へ供給する。

4. `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md`  
   ここで初めて `Bridge(C,A;D_C)`、`\Pi_{\mathrm{dynamic}}`、`\operatorname{ev}_{\pi}`、`\Pi_{\mathrm{static}}`、`\mathrm{FFCert}_{\pi}(C,A)` が一つの機械として置かれた。

### 差分

未踏だったのは theorem 本体ではない。  
未踏だったのは、**既存の Face/SST 資産を `\operatorname{ev}_{\pi}` の faithful/full へ束ねる「補題束の配線図」**である。

## P-2 Anchor

### 最小補題束

sectoral A を後続が歩けるようにするため、補題束を 5 本に固定する。

| ID | 補題名 | 役割 | 主 SOURCE |
|:---|:---|:---|:---|
| L0 | Bridge existence lemma | `b \in \mathrm{Bridge}(C,A;D_C)` が立つ最小条件を固定する | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` |
| L1 | Face witness lemma | 非自明な path 差分は 2-simplex 検査面に露出することを保証する | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/Face補題_ホモロジー厳密化.md` |
| L2 | SST residue lemma | 露出した差分が `(+\lambda)+(-\lambda)=0` の型でしか相殺されないことを固定する | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/incubator/力とは忘却である_v2.md` |
| L3 | Canonical lift lemma | `q_{\pi}` が標準 path へ持ち上がることを示す | `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` |
| L4 | Sectoral A corollary | `\Pi_{\mathrm{static}}` と `\Pi_{\mathrm{dynamic}}` が同じ bridge machine の二投影だと結ぶ | 同上 + L1-L3 |

### 依存順

```text
L0
↓
L1 + L2
↓
L3
↓
L4
```

順序の意味は明確である。

- `L0` がないと共通機械が立たない  
- `L1` がないと faithful が空文化する  
- `L2` がないと差分の相殺条件が型付けされない  
- `L3` がないと full が「別置きの式」へ戻る  
- `L4` はそれら 4 本の上にしか立たない

### 後続への道

後続の `/ene` は、上の 5 本をそのまま節または別紙補題へ落とせばよい。  
特に最初の実装単位は次の 2 本で十分である。

1. `L1 + L2` をまとめて [/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/証明_sectoralA_evπのfaithful性.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/証明_sectoralA_evπのfaithful性.md) へ外部化  
2. `L3` を [/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/証明_sectoralA_canonical_liftとlocal_full.md](/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/証明_sectoralA_canonical_liftとlocal_full.md) へ外部化

この 2 本が立ったので、`L4` は本体の sectoral A 系として短く再接続できる。

### 発見

**epistemic**

1. 弱点は theorem 不在ではなく、既存資産の配線不在だった  
2. Face Lemma は detectability、SST は cancellation law、canonical lift は realizability を与える  
3. sectoral A は「一つの大証明」より「5 本の補題束」の方が歩きやすい

**pragmatic**

1. `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` からこの足場面へ入口リンクを張れる  
2. `/ene` は `L1+L2` と `L3` を別々に施工できた  
3. global A を言わずに sectoral A の防衛線だけを太くできる

## P-3 Momentum Check

**撤退条件**: `CLEAR`  
`canonical lift` はまだ `\pi`-sector の local full で止められている。Face/SST も本面で再証明を要求していない。

**勢い**: `意図的 ✅`  
今回の踏破は「既にある Face/SST 面をなぞった」だけではない。`Bridge → ev_{\pi} → StaticRead` という後続経路を新しく可視化し、補題束として歩ける地図にした。

**次の一歩**

1. `/ops` — `Paper II`、`統一表ドラフト`、`Face 補題計算面`、新設 2 補題面の依存関係を俯瞰する  
2. `/kop` — global A へ widen せず、まず `\pi`-sector の補題束だけを deepen し続ける  
3. `/ene` — `L4` 以後に必要なら、comparison arrow 周辺の記法統一だけを局所整備する

## 結果

**踏破**: `deepen × sectoral A × 補題束の足場化`  
**地形**: theorem 不足ではなく配線不足  
**足場**: 構築済み。`L0-L4` の順で後続が歩け、`L4` は本文へ再接続済み  
**発見**: epistemic 3 件 + pragmatic 3 件  
**撤退条件**: `CLEAR`

## WM

`$direction = deepen`  
`$terrain = sectoral A の補題束`  
`$anchor = L0-L4 の依存順`  
`$discovery = theorem 不足ではなく配線不足`
