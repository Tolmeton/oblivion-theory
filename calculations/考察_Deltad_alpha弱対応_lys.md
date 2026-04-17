# Δd / α 弱対応 — 分析面

**役割**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文II_相補性は忘却である_草稿.md` の `Δd / α` 層化と、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md` の `\alpha_E(\theta)` / `\alpha_b(\theta)` を、直接同一視ではなく弱橋梁として固定する補助面。

## P-0 対象固定

**対象**: `Δd / α` 層化が、Euler bridge の `\pi`-sector における `\alpha_b(\theta)` とどこまで結びつくかを、強橋ではなく weak correspondence として切り出す。  
**含む**: `Δd` の位相的不変量性、Paper II の底空間/ファイバー層化、統一表ドラフトの `\alpha_E(\theta)` 試作最小モデル、`θ↔α` の追加仮説。  
**除外**: `Δd \leftrightarrow \alpha` の厳密導出、Paper VIII §6.7.14 の全文再証明、global A への拡張。

### SOURCE

- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文II_相補性は忘却である_草稿.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/統一表の関手化_構想ドラフト_v0.2.md`
- `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/calculations/考察_CPSspan_Bridge対応表_lys.md`

### MECE チェック

- `Δd` は離散底空間
- `α(θ)` は底空間上の連続ファイバー
- `\alpha_b(\theta)` は `\pi`-sector に正規化された pathwise 累積座標

## P-1 三層分解

| 項 | 型 | 役割 | SOURCE 上の地位 |
| :--- | :--- | :--- | :--- |
| `Δd` | 離散 (`\mathbb{N}`) | 忘却関手のカーネル差が与える位相的 Type 分類 | Paper II の定義 |
| `α(θ)` | 連続 (`\mathbb{R}`) | 固定 `Δd` の内部で動く局所精度 / 局所変動 | Paper II の層化定義 |
| `\alpha_E(\theta)` / `\alpha_b(\theta)` | 連続 (`[0,\pi]\to[0,1]`) | Euler path を `\pi`-sector に正規化した累積忘却座標 | 統一表ドラフトの試作最小モデル / bridge datum |

**INFERENCE**: ここで既に 3 つは同型ではない。`Δd` は「山があるか」を決める離散分類、`α(θ)` は「その山の中でどこにいるか」という局所座標、`\alpha_b(\theta)` は「その山を `\pi`-sector の 1 本の標準経路で歩いたときの累積進行度」である。

## P-2 対応の強さ

| Paper II 側 | Euler bridge 側 | 判定 | 理由 |
| :--- | :--- | :--- | :--- |
| `Δd \ge 1` が Type I を決める | `\pi`-sector で非自明な bridge datum が必要 | medium | 両方とも非対称性の起動条件を与えるが、片方は離散分類、片方は path data |
| 固定 `Δd` の内部で `α(θ)` が変動する | 固定 sector の内部で `\alpha_b(\theta)` が進行する | medium | どちらも「固定された殻の内側の連続変化」だが、`α(θ)` は局所場、`\alpha_b(\theta)` は累積 path 座標 |
| `α(θ_\infty)=Δd` の整数部分対応 | `\alpha_b(0)=0`, `\alpha_b(\pi)=1` | weak | Paper II 自身が motivated construction / 定義として採用しており、統一表側の正規化と直結する定理ではない |
| `Δd / α` 層化 | `\alpha_b(\theta)` | weak | 直接橋ではなく、`底空間 → ファイバー → pathwise normalization` の 2 段階を要する |

**要約**: `Δd / α` から `\alpha_b(\theta)` への関係は、直接の等式ではなく

```text
Δd が許す Type / sector を決める
  ↓
その固定 sector の内部で α が局所的に変動する
  ↓
Euler bridge がそのうち 1 本の正規化 path を α_b(θ) として選ぶ
```

という factorization でしか読めない。

## P-3 最初の破断点

```text
最初の破断点 = Δd と α_b(θ) の型不一致
理由 = Δd は位相的な離散不変量であり、α_b(θ) は [0,1] 上の正規化累積座標である。両者を同一視する前に、「固定 Δd が sector を定め、その内部に連続 path がある」という層化公理を挟まないといけない。
```

二番目の破断点は、Paper II 自身が `α(θ_\infty)=Δd` を**定義として採用**しており、導出としてはまだ持っていない点である。したがって、ここを Euler bridge 側の実証済み結果として引用してはいけない。

## P-4 使ってよい言い方 / 禁止すべき言い方

### 使ってよい

- `Δd` は Type を決める底空間、`α` はその内部のファイバー、`\alpha_b(\theta)` はそのファイバー上の標準経路である
- `\pi`-sector の bridge datum は、固定された非対称性クラスの内部運動を正規化して読む装置である
- `Δd / α` 層化は `\alpha_b(\theta)` を動機づけるが、まだ一意には強制しない

### 禁止すべき

- `Δd = \alpha_b(\theta)` と書く
- `\alpha_b(\pi)=Δd` のように endpoint を整数 Type に直接等置する
- `α(θ_\infty)=Δd` を定理として扱う

## P-5 強橋に上げるための追加仮説

1. **base-fiber 公理**  
   固定 `Δd` が sector / Type class を定め、その内部で `α` が連続的に動くことを typed に書く。

2. **`θ↔α` 累積公理**  
   局所非整列の累積が `\alpha_b(\theta)` を与える、という bridge law を立てる。

3. **endpoint 正規化公理**  
   `\alpha_b(0)=0`, `\alpha_b(\pi)=1` を Paper VIII の boundary closure と接続する。

## P-6 Integration

`Δd / α` 層化は、Euler bridge の `\alpha_b(\theta)` と無関係ではない。しかし関係の型は「同じ量」ではなく、「離散底空間が先にあり、その上で連続ファイバーが動き、そのファイバーの 1 本の正規化 path が `\alpha_b(\theta)` になる」である。したがって本稿で安全に言えるのは weak correspondence までであり、強橋へ上げるには `base-fiber`, `θ↔α`, `endpoint closure` の 3 本を別公理として受ける必要がある。
