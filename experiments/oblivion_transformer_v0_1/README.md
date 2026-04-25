# Oblivion Transformer v0.1

Oblivion Transformer v0.1 は、次の暫定的な実装仮説から導いた最小の PyTorch 骨格である。

> **推論** = 道を増やし、道を殺し、最後に一つを通すことだ。
> 直感的に言えば、自由は道を増やす。忘却は道を減らす。推論はその往復である。

本 README では、この往復を Γ/Q 分解の言葉に写して実装する。厳密には、情報場上の認知ベクトル場において、自由としての回転成分 Q と忘却としての勾配成分 Γ の相互作用として近似的に扱う。

これはベンチマークで実証されたモデルではない。  
理論をすぐに信じるための完成品でもない。  
これは、理論を「点検できる形」「書き換えられる形」「反証できる形」にまで落とした設計骨格である。  
特に `source tether`、`self-completion`、`KalonJudge` は Helmholtz 草稿そのものではなく、
v0.1 で理論を機械化するために仮置きした実装上の補助概念である。

## 核心

このループを、ふつうの意味での「深く考える」とは見なさない。
また、ここでの 4 相ループは Helmholtz 草稿の定義そのものではなく、
Γ/Q 分解を v0.1 の実装へ写すための近似的な操作列である。

実装上は、次の 4 相で記述している。

```text
expand -> forget -> repair -> judge
```

- `expand`: 候補方向をひらく
- `forget`: 価値の低い候補を `ker` 側へ送る
- `repair`: 射影で崩れた整合を補完する
- `judge`: さらに忘れることが精密化なのか、劣化なのかを判定する

## アーキテクチャ

```text
Input ids
  -> SourceReservoir
  -> token_state, source_state
  -> Loop[
       FreedomExpander
       -> OblivionProjector
       -> SelfCompletionCore
       -> KalonJudge
     ] x T
  -> CommitHead
  -> logits
```

## モジュール対応

| モジュール | モデル上の役割 | 理論上の役割 |
|---|---|---|
| `SourceReservoir` | トークンを埋め込み、参照アンカーを持つ | 実装上の tether 仮説 |
| `FreedomExpander` | 各位置で複数の潜在候補を提案する | 自由側の近似 |
| `OblivionProjector` | 候補を採点し、上位だけを残す | 忘却側の近似 / ker-image 分離の作業仮説 |
| `SelfCompletionCore` | 射影後の状態を補完する | 実装上の補完仮説 |
| `KalonJudge` | もう 1 ループ回す価値があるかを見る | 停止判定の仮置き |
| `CommitHead` | 潜在状態を logits に変換する | 具体的選択への遅延コミット |

## 不変条件

この骨格は、次の 4 条件を守る前提で作ってある。

1. `source_state` は全ループで参照可能でなければならない。
2. 価値コミットは忘却ループの中ではなく、後段で起こるべきである。
3. 忘却は副作用として隠さず、質量として観測可能でなければならない。
4. 停止は単なる時間ではなく、fidelity と saturation の両方に依存すべきである。

## 意図的に未実装なもの

これは v0.1 の骨格なので、あえて単純なまま残してある部分がある。

- 学習レシピはまだ入れていない。
- `FreedomExpander` は完全な探索機構ではなく、密な候補提案層に留まる。
- `KalonJudge` は局所的でヒューリスティックな判定器である。
- 失敗様式を隠さないため、内部ループ統計を返す。

## 想定している loss 面

以下はコード未実装であり、現時点では設計仮説である。

| Loss | 役割 |
|---|---|
| `source_fidelity` | 入力に tether されるべき成分を保持する |
| `minimal_oblivion` | 不要な忘却を罰する |
| `coherence_invariance` | 補完後の構造安定性を保つ |
| `late_commitment` | 早すぎる価値固定を抑制する |
| `halt_calibration` | 停止の仕方を実際の精密化と整合させる |

## ファイル

| ファイル | 用途 |
|---|---|
| `忘却_変換器.py` | モデル骨格本体 |
| `demo.py` | 最小の smoke demo |

## 実行例

```bash
python '/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/oblivion_transformer_v0_1/demo.py'
```

PyTorch が無い場合、demo は「動いたふり」をせず、依存不足として停止する。
