# 考察_CPSspan_Bridge対応表_lys

**作成日**: 2026-04-14  
**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文II_相補性は忘却である_草稿.md` の `CPS span` 語彙と、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` の `\mathrm{Bridge}(C,A;D_C)` 語彙を、typed に照合する辞書面。  
**派生**: `comparative`

## P-0 Prolegomena

**対象**: `CPS span ↔ Bridge(C,A;D_C)` の対応を 1 節ぶんの分析面として切り出し、どこが対応し、どこで型がずれるかを固定する。  

### 含む

1. Paper II の `C_D, U_A, U_B, Face Lemma, SST, α-層化`
2. 統一表ドラフトの `\mathrm{Bridge}(C,A;D_C), \Pi_{\mathrm{dynamic}}, \Pi_{\mathrm{static}}, \operatorname{ev}_{\pi}, \mathrm{FFCert}_{\pi}`
3. sectoral A の faithful / local full を支える補題 2 面

### 除外

1. `global A` の主張
2. `Paper VIII` の全基礎づけ
3. blanket 論の下流展開そのもの
4. `\varphi` や automath 側の代数的枝

**目的**: `同じものを別名で呼んでいる部分` と `本当に追加構造が乗っている部分` を切り分け、後続の本文接続で型ずれを起こさないようにする。

[CHECKPOINT P-0/5]

## P-1 Scale Setting

**粒度**: `MEDIUM`  
**深度**: `STANDARD`

**選択理由**: ここで必要なのは全理論の再設計ではなく、対応辞書として使える最小単位である。粗すぎると「だいたい同じ」で濁り、細かすぎると `Paper II` と `Bridge` の全文トレースになる。したがって、`共通機械 / 忘却射 / 検査面 / 復元` の 4 軸で切るのが最小十分である。

[CHECKPOINT P-1/5]

## P-2 Decomposition

対応面を次の 4 要素に直交分割する。

| 要素 | 独立変数名 | 役割 |
| :--- | :--- | :--- |
| E1 | `carrier_identity` | 何が「機械本体」なのか |
| E2 | `forgetful_readout` | どの忘却射でどの表示面へ出るのか |
| E3 | `detectability_constraint` | 差分がどこで露出し、どこで潰してよいか |
| E4 | `recoverability_scope` | 失われたものをどこまで戻せるか |

### MECE チェック

- `carrier_identity` は担体の問題であり、忘却や検査の問題ではない
- `forgetful_readout` は読取窓の問題であり、検査や復元の問題ではない
- `detectability_constraint` は faithful 側の識別条件であり、担体や復元の問題ではない
- `recoverability_scope` は full / adjoint / lift の問題であり、他 3 軸と独立

したがって、少なくともこの辞書面に必要な分割としては実質 MECE である。

[CHECKPOINT P-2/5]

## P-3 Deep Dive

### E1 `carrier_identity`

| Paper II / CPS span | Bridge 語彙 | 判定 | 理由 |
| :--- | :--- | :--- | :--- |
| 共通容器 `C_D` | 共通機械 `\mathrm{Bridge}(C,A;D_C)` | **対応 strong** | どちらも「片側の読解が生まれる前の未分化な本体」を担う |
| `Set_A, Set_B` | `\mathrm{AdmPath}(C,A), \mathrm{StaticRead}(C,A)` | **対応 weak** | 役割は同じく readout codomain だが、Bridge 側は集合ではなく typed な像と証明義務を含む |

**要点**: `C_D ↔ \mathrm{Bridge}(C,A;D_C)` が中核対応であり、`Set_A/Set_B` は `AdmPath/StaticRead` の「役割対応」に留まる。ここを `Set` と同一視すると型崩れが起きる。

### E2 `forgetful_readout`

| Paper II / CPS span | Bridge 語彙 | 判定 | 理由 |
| :--- | :--- | :--- | :--- |
| 忘却関手 `U_A, U_B` | `\Pi_{\mathrm{dynamic}}, \Pi_{\mathrm{static}}` | **対応 medium** | どちらも共通機械から二つの読解窓を作る forgetting map だが、Bridge 側は「動的/静的」という読取軸に再束縛されている |
| CPS2 の架橋 | `\operatorname{ev}_{\pi}` | **対応 strong** | 二つの窓のあいだに comparison arrow を立てる役割が一致する |

**重要な非一致**: Paper II の `A/B` はドメイン差を帯びやすいが、Bridge 側の `dynamic/static` は**読取様式の差**である。したがって `U_A = \Pi_{\mathrm{dynamic}}` を普遍主張として読むのは過剰で、`Euler \pi-sector における再束縛` として読むべきである。

### E3 `detectability_constraint`

| Paper II / CPS span | Bridge 語彙 | 判定 | 理由 |
| :--- | :--- | :--- | :--- |
| Face Lemma | `\mathrm{AdmPath}_{\triangle}` の Face 条件 | **対応 strong** | 「差分は 2-simplex 検査面に露出しなければならない」という核が同じ |
| `B_1^{\mathrm{ver}} \neq 0` | faithful 補題の witness face | **対応 strong** | どちらも comparison surface の実在判定 |
| SST の `(+\lambda)+(-\lambda)=0` | faithful 補題の residue rule | **対応 strong** | 「消してよい差分の型」を決める cancellation law が一致する |

**要点**: Bridge 側の faithful は新発明ではない。Paper II が `照合面` と `符号付き相殺` で用意した detectability/cancellation を、`\operatorname{ev}_{\pi}` の injectivity 条件へ再配線したものだ。

### E4 `recoverability_scope`

| Paper II / CPS span | Bridge 語彙 | 判定 | 理由 |
| :--- | :--- | :--- | :--- |
| Layer 1 の左随伴 / 部分復元 | `\operatorname{Lift}_{\pi}` | **対応 medium** | どちらも忘却された像からの復元を担うが、Bridge 側は `\pi`-sector に限った local section |
| `CPS3` の同時完全適用不能性 | `\mathrm{EndEq}_{\pi}(A)` への制限 | **対応 medium** | 全域復元を諦め、局所 sector に閉じることで過剰主張を避けている |
| blanket 生成 | 直接像なし | **対応 none** | blanket は Paper II の下流分岐であり、Bridge の Euler 節では使用していない |

**重要な非一致**: `\operatorname{Lift}_{\pi}` は global adjoint ではない。ここで回収しているのは `A 全体` ではなく、`e^{i\pi}+1=0` を含む `\pi`-sector の endpoint identity だけである。

### 対応表の圧縮版

| CPS span 語彙 | Bridge 語彙 | 対応の強さ | 留保 |
| :--- | :--- | :--- | :--- |
| `C_D` | `\mathrm{Bridge}(C,A;D_C)` | strong | 共通機械として読む限り安定 |
| `U_A, U_B` | `\Pi_{\mathrm{dynamic}}, \Pi_{\mathrm{static}}` | medium | A/B はドメイン差ではなく readout 差へ再束縛される |
| CPS2 架橋 | `\operatorname{ev}_{\pi}` | strong | sectoral comparison arrow |
| Face Lemma | Face 条件 / `\mathrm{AdmPath}_{\triangle}` | strong | detectability の供給元 |
| SST | residue rule | strong | cancellation law の供給元 |
| 左随伴 / 部分復元 | `\operatorname{Lift}_{\pi}` | medium | local full に限定 |
| blanket 生成 | なし | none | この節では枝を切っている |
| `\Delta d` / α 層化 | `\alpha_b(\theta)` | weak | 直接橋ではなく、別途 `θ↔α` の橋が必要 |

[CHECKPOINT P-3/5]

## P-4 Integration

### 要素間関係

1. `E1 → E2`: 共通機械が立たないと二つの readout は同じ本体の窓にならない  
2. `E2 → E3`: 二つの readout があっても、Face/SST がなければ `\operatorname{ev}_{\pi}` は faithful にならない  
3. `E3 → E4`: detectability が立ったうえで `\operatorname{Lift}_{\pi}` があって初めて local full まで閉じる  
4. `E4 → sectoral A`: faithful と local full が揃って初めて `L4` が「同じ機械の二投影」と言える

### クリティカルパス

```text
Paper II の C_D / U_A,U_B
  ↓ 再束縛
Bridge(C,A;D_C) / Π_dynamic, Π_static
  ↓ 検査面の移植
Face Lemma + SST
  ↓ 比較射の健全化
ev_π faithful
  ↓ 局所復元
Lift_π / local full
  ↓
sectoral A (L4)
```

### 再構成テスト

`CPS span ↔ Bridge(C,A;D_C)` の対応は、「Paper II が語る共通容器と二つの忘却窓」を、そのまま Euler の `\pi`-sector に持ち込んだものではない。実際には、共通容器 `C_D` は `\mathrm{Bridge}(C,A;D_C)` に、二つの忘却窓 `U_A, U_B` は `\Pi_{\mathrm{dynamic}}, \Pi_{\mathrm{static}}` に**再束縛**され、さらに Face Lemma と SST が `\operatorname{ev}_{\pi}` の faithful 条件へ、左随伴的復元が `\operatorname{Lift}_{\pi}` の local full へ読み替えられている。この再束縛があるからこそ `L4` は「同じ機械の二投影」と言えるのであって、blanket 生成や global adjoint までそのまま移植しているわけではない。

### T1-T3

- `T-1 合成`: `C_D → U_A/U_B → ev_π → Lift_π → L4` の連鎖は、各段が前段の欠けを埋める方向で合成されており矛盾しない  
- `T-2 結合律`: `Face/SST → faithful` と `Bridge → local full` の左右どちらから束ねても、`L4` が local claim に留まる限り結論は一致する  
- `T-3 恒等`: `Bridge(C,A;D_C)` を抜いてしまうと static/dynamic は同じ本体の窓でなくなるので、恒等的に保たれる核は共通機械そのものにある

### 下流制約

1. 今後本文で `CPS` と `Bridge` を混ぜるときは、`A/B = dynamic/static の再束縛` を明記すること  
2. `blanket` を Euler 節に持ち込まないこと。これは別枝であり、ここでは対応なしと固定する  
3. `\operatorname{Lift}_{\pi}` を global adjoint のように言わないこと。local full に限定すること

[CHECKPOINT P-4/5]
