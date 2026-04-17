# 6.7.14 の証明圧固定 — 分析面

**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md` §6.7.14 が、どこまで既存 SOURCE に還元され、どこからが最小追加公理なのかを固定する補助面。統一表ドラフトをこれ以上膨らませる前に、Paper VIII 側の「証明圧」をここへ露出させる。

## P-0 Prolegomena

**対象**: §6.7.14 の 5 断面  
`固定計量 / 測地ゲージ / 端点閉包 / 累積 law / pathwise bridge`  
が、どこまで既存 SOURCE でどこからが追加主張かを切り分ける。

**含む**:

- Paper I §6.7.1 の Fisher 計量一意性
- Paper I Appendix C.5 の Liouville 変換と測地長 `π`
- Paper VIII §6.7.14c-d の `η / E_p` 区別
- Paper VIII 命題 6.7.4c の boundary closure

**除外**:

- `typed decategorification`
- `sectoral A`
- `global A`
- `d\alpha_E/d\theta=(1/2)\sin\theta` の完全定理化

### SOURCE

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文I_力としての忘却_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文VIII_存在は忘却に先行する_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_theta_alpha累積公理_lys.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_eta_Ep区別_lys.md`

[CHECKPOINT P-0/5]

## P-1 Scale Setting

粒度: `MEDIUM`  
深度: `STANDARD`

理由: ここで要るのは新しい補題の追加ではなく、§6.7.14 のどこが「もう既存系から引けているか」を固定し、何だけがまだ theorem 候補でなく最小追加公理なのかを圧縮することだからである。

[CHECKPOINT P-1/5]

## P-2 Decomposition

§6.7.14 の証明圧を 5 要素へ直交分割する。

| 要素 | 独立変数 | 役割 |
| :--- | :--- | :--- |
| `metric_fixation` | `g^{(0)}` | path の背景計量を固定し、α を接続側だけへ押し込む |
| `geodesic_gauge` | Liouville / geodesic length `π` | prefactor を測地ゲージへ吸収する prototype を与える |
| `endpoint_closure` | `\bar{\eta}(\pm\infty)` | 開区間の外で端点 `0,1` を閉じる |
| `accumulation_law` | `d\alpha_E/d\theta` | 局所非整列密度を累積忘却度へ変換する |
| `pathwise_bridge` | `η / E_p` | scalar 整合と categorical lift を分離した経路実現 |

MECE 判定:

- `metric_fixation` は背景
- `geodesic_gauge` は座標選択
- `endpoint_closure` は境界処理
- `accumulation_law` は真の新規核
- `pathwise_bridge` は統一系への接続

重複はない。

[CHECKPOINT P-2/5]

## P-3 Deep Dive

### 要素 1: `metric_fixation`

**SOURCE**: Paper I §6.7.1 は、統計多様体の計量を Fisher 計量 `g^{(0)}` に固定し、α は計量ではなく接続側にのみ入ると明示する。  
**INFERENCE**: したがって §6.7.14 が path を扱うとき、背景計量そのものを新しく発明する必要はない。ここで既に「角度 `θ` をどの幾何の上で測るか」は既存 SOURCE で固定されている。

### 要素 2: `geodesic_gauge`

**SOURCE**: Paper I Appendix C.5 は Liouville 変換で変数係数を除去し、測地長が `π` に正規化される prototype を与える。  
**INFERENCE**: したがって §6.7.14a が言う「prefactor の吸収」は無根拠な convenience ではなく、既存の測地ゲージ選択の延長として読める。ここで追加されるのは gauge の採用であって、新しい力学ではない。

### 要素 3: `endpoint_closure`

**SOURCE**: Paper VIII 命題 6.7.4c は `\bar{\eta}(-\infty)=0`, `\bar{\eta}(+\infty)=1` を与える。  
**SOURCE**: Paper VIII §6.7.14c は `\alpha_{\mathrm{III}}^E(\theta)` が `\theta \to 0^+` と `\theta \to \pi^-` で発散することを書いている。  
**INFERENCE**: 端点 `0,\pi` を閉じる仕事は `η` 単独ではなく、既存の boundary closure が担っている。ゆえに端点処理は「新規追加」ではなく「既存 SOURCE の接続」である。

### 要素 4: `accumulation_law`

**SOURCE**: Paper VIII §6.7.14a-b は `\rho_E(\theta)\propto\sin\theta` と

```text
dα_E/dθ = K sinθ
```

から `K=1/2` を境界条件で固定する流れを置いている。  
**INFERENCE**: ここが §6.7.14 の真の圧点である。固定計量・測地ゲージ・境界閉包を全部既存 SOURCE へ還元しても、`局所非整列密度を累積忘却度へ積み上げる law` 自体はなお最小追加公理として残る。

### 要素 5: `pathwise_bridge`

**SOURCE**: Paper VIII §6.7.14c は `η` が開区間での scalar 整合を与えると述べる。  
**SOURCE**: Paper VIII §6.7.14d は `E_p(\theta)=C_{\alpha_E(\theta)}` を定め、Euler path の categorical content はこの濾過列にあると述べる。  
**INFERENCE**: §6.7.14 の pathwise bridge はすでに「`η` が橋で `E_p` が持ち上げ」という型分離に成功している。したがってここでの残課題は `η / E_p` の区別ではなく、その手前にある `accumulation_law` の地位である。

### 浮上次元

1. §6.7.14 のうち、`固定計量 / 測地ゲージ / 端点閉包 / η と E_p の型分離` は、もう既存 SOURCE へかなり戻せている。  
2. いま本当に theorem 候補として圧を受けるのは `accumulation_law` だけである。  
3. したがって「6.7.14 が弱い」のではなく、「6.7.14 の弱点は一点にまで縮減された」と読むべきである。

[CHECKPOINT P-3/5]

## P-4 Integration

再構成すると、§6.7.14 の現在地は次の 1 文に圧縮できる。

```text
6.7.14 は、背景計量・測地ゲージ・端点閉包・η/E_p の型分離を既存 SOURCE へ還元したうえで、局所非整列密度を累積忘却度へ積み上げる law だけを最小追加公理として残した補題候補である。
```

この圧縮の内訳は次である。

- `metric_fixation` = Paper I §6.7.1 の SOURCE
- `geodesic_gauge` = Paper I Appendix C.5 の SOURCE
- `endpoint_closure` = Paper VIII 命題 6.7.4c の SOURCE
- `η / E_p` の区別 = Paper VIII §6.7.14c-d の SOURCE
- `accumulation_law` = 依然として最小追加公理

したがって、Paper VIII 側で次にやるべきことは二択に尽きる。

```text
route A:
局所非整列密度 → 累積忘却度 の law を、既存の変分原理または作用汎関数から導出する

route B:
この law を明示的に最小追加公理として受理し、6.7.14b を theorem ではなく lemma candidate のまま固定する
```

**再説明**: いまの §6.7.14 は「全部が仮説」ではない。むしろ、多くの部品はすでに既存の骨組みに接地している。まだ宙に浮いているのは、「その場のズレをどう積み上げると忘却進行度になるのか」という一点だけだ。証明圧は広く拡散していない。一本の細い首に集まっている。

ρ_hard: `ρ₂=0 ρ₃=0 ρ₄=0 total=0`  
ρ_soft: `ρ₀=0 ρ₁=0`

[CHECKPOINT P-4/5]
