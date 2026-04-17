# 論文XI — 第3モデル条件 実験計画書

**対象論文**: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XI_プロンプトは忘却である_草稿.md`  
**対象節**: §7.10.4-§7.10.5  
**目的**: MB 透過性 $\kappa$ を 2 点補間から引き上げるのではなく、三者比較で撤回条件を正面から試験する。

## P-0 実験空間

### 0.1 固定面

- モデル anchor 1 = Claude Sonnet 4.6 (`低 compliance` 側の既存 anchor)
- モデル anchor 2 = Gemini 3.1 Pro Preview (`高 compliance` 側の既存 anchor)
- 第3モデル M3 = **Anthropic / Google 以外の provider** から 1 モデル
- トピック = T1-T5 (既存 Claude / Gemini 実験と同一)
- 条件 = A (plain) / B (CCL)
- 測定族 $\mathcal{M}$ = `total_structural`, `rho_notation`, `U_labels`, `categorical_vocab`, `axiom_ratio`, `assumption_count`, `bond_count`
- 生成形 = single-shot, tool off, same system/user scaffold, same max token ceiling

### 0.2 盲点 5 カテゴリ

1. **provider 交絡**: 同じ provider 内の別モデルを足しても、family-specific fine-tuning 差しか見えない。
2. **task drift**: M3 だけ別トピック・別温度・別出力長を使うと、第3モデル条件ではなく task 条件差を測ることになる。
3. **compliance の循環定義**: `d_struct` だけを見て compliance 順位を定めると $\kappa$ は再び事後命名になる。
4. **hidden policy 交絡**: safety refusal や verbosity policy が structural metrics を押し上げる可能性。
5. **credential drift**: 実験 runner が provider ごとに分断されると、同一プロトコルの比較が崩れる。

## P-1 仮説と反証条件

### 1.1 主仮説

- **H-T3-1 内容帰無保持**: M3 でも内容指標 (`axiom_ratio`, `assumption_count`, `bond_count`) は A/B 間で実質帰無に留まる。
- **H-T3-2 順序整合**: 独立 compliance 指標 $c_{\mathrm{fmt}}$ の順序と structural effect size 主指標 $d_{\text{struct}}^{\ast}$ の順序が一致する。
- **H-T3-3 局所性維持**: たとえ順序整合が得られても、$\kappa$ は固定された記法対 $\delta$ と測定族 $\mathcal{M}$ に対する局所推定量としてのみ解釈する。

### 1.2 pass / fail 判定

| 判定面 | Pass | Fail |
|:---|:---|:---|
| 内容帰無 | 3 指標すべてで `|d| < 0.30` を維持 | いずれか 1 指標で `|d| ≥ 0.50` かつ方向一貫 |
| 構造伝搬 | `total_structural` で明確な A/B 差、かつ副指標 3 本中 2 本以上が同方向 | 主指標だけが立ち、副指標が逆向きまたは消失 |
| 順序整合 | `ord(c_fmt) = ord(d_struct^*)` | compliance 順序と structural 順序が不一致 |
| κ 解釈 | 「局所推定量」として保持 | 「一般パラメータ」へ拡張したくなるだけの曖昧結果 |

### 1.3 反証条件

次のいずれかが起きたら、C4 は局所記述へ降格する。

1. M3 が内容帰無を破る。
2. M3 を入れると `c_fmt` 順序と `d_struct^*` 順序が食い違う。
3. M3 の structural 差が `total_structural` のみに局在し、副指標群では再現しない。
4. M3 の応答が refusal / verbosity policy に大きく支配され、A/B 差より policy 差の方が大きい。

## P-2 MVP 設計

### 2.1 モデル選定

- **初期 M3 候補**: `gpt-4-0125-preview`
- **理由**: 既存 anchor が Anthropic / Google に張られており、かつ `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/run_api.py` と互換な OpenAI 系候補として最小実装コストで着手できるため。これは local runner compatibility を優先した初期候補であり、「最新・最良」の主張ではない。
- **現在の runnable probe が直接サポートする provider**: `openai`, `anthropic`
- **OpenAI/Anthropic 以外の候補**: 将来の adapter 追加対象。現行 `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_third_model_probe.py` の runnable scope には含めない
- **同一 provider 内モデル**: 実行は可能だが、その場合は「第3モデル条件」ではなく「family 内補助観測」に格下げする

### 2.2 2 層ベンチ

#### A. 主実験ベンチ

- トピック = T1-T5
- 条件 = A/B
- **現行 repo 状態**: exact T1-T5 A/B prompt 本文は未 versioned。したがって主実験面はまだ `READY` ではなく、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_third_model_main_bench.template.json` を **source import contract** として保持する
- MVP サンプル = `N=20/条件`  
  配分: 各 topic 4 反復 × 5 topics = 20
- Full サンプル = `N=50/条件`
- 主指標 = `total_structural`
- 副指標 = `rho_notation`, `U_labels`, `categorical_vocab`
- guardrail 指標 = `axiom_ratio`, `assumption_count`, `bond_count`

#### B. compliance 校正ベンチ

`d_struct` と別面を測る 12 問の mini-benchmark を事前登録する。

| ブロック | 問数 | 測るもの | 例 |
|:---|:---|:---|:---|
| JSON 厳守 | 4 | key 順序・余剰 prose の抑制 | 指定 4 keys のみを返す |
| Label 固定 | 4 | ラベル保持 | `A1/A2/B1/B2` を一字一句保持 |
| 禁止自由文 | 4 | 余計な説明の抑制 | 理由説明を禁じた yes/no 出力 |

この 12 問から

$$c_{\mathrm{fmt}} := \frac{\text{exact-format success}}{12}$$

を定義する。これは structural vocabulary の効果量ではなく、**外部指定への従属性**そのものを測る独立校正面である。

### 2.3 Skin-in-the-Game

- MVP で `c_fmt` と `d_struct^*` が同方向なら Full run へ進む
- 逆方向なら、その時点で C4 を局所記述へ降格する
- 結果に応じて本文の `65%` を上げるか下げるかを必ず更新する

## P-3 実行プロトコル

### 3.1 実行順

1. M3 で compliance 校正ベンチ 12 問を実行
2. 同じ M3 で主実験ベンチ A/B を `N=20/条件` 実行
3. Claude / Gemini の既存 anchor を同じ集計器に流し込み、`c_fmt` と `d_struct^*` の順序を比較
4. MVP pass 時のみ M3 を `N=50/条件` に拡張

### 3.2 実装面

- Anthropic / OpenAI 系 runner = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/run_api.py`
- Gemini anchor = 既存 §7.9 と同じ headless 実行面
- 第 3 モデル calibration runner = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_third_model_probe.py`
- calibration prompt asset = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_third_model_cfmt12.jsonl`
- execution manifest = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_third_model_probe_manifest.json`
- main bench scaffold = `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/paper_xi_third_model_main_bench.template.json`
- dry-run 出力は live calibration artifact を上書きしない。既定では `*_dry_run.jsonl` に分岐する
- 出力は provider を跨いでも同じ JSONL schema に揃える:

```json
{
  "model": "M3",
  "provider": "openai",
  "topic": "T1",
  "condition": "A",
  "prompt_variant": "plain",
  "response_text": "...",
  "metrics": {
    "total_structural": 0,
    "rho_notation": 0,
    "U_labels": 0,
    "categorical_vocab": 0,
    "axiom_ratio": 0.0,
    "assumption_count": 0,
    "bond_count": 0
  }
}
```

### 3.3 事前固定

- temperature = 0
- top_p = 1
- same max output cap
- no tools / no browsing / no retrieval
- A/B 順序は topic ごとに交互化
- 集計は `Cohen's d + Welch + Brown-Forsythe` で既存節と同型に保つ

## P-4 収穫パターン

| パターン | 観測 | 解釈 | 処置 |
|:---|:---|:---|:---|
| P1 | M3 が Claude と Gemini の中間 | $\kappa$ は局所順序パラメータとして前進 | C4 を 65→75% 候補 |
| P2 | M3 が Gemini より高 compliance / 高 d | 高 compliance 側の拡張 | 第4モデル条件へ進む |
| P3 | M3 が構造差を示すが内容帰無を破る | H₃ と C4 の切断 | $\kappa$ を局所記述へ降格 |
| P4 | `c_fmt` は高いのに `d_struct^*` が低い | compliance と structural 伝搬は同じでない | `κ = MB 透過性` の解釈を撤回 |
| P5 | M3 だけ refusal / policy に支配 | provider policy 交絡 | M3 を失格にし別 provider を選ぶ |

## 次の一手

1. M3 を 1 つ確定する。
2. `c_fmt` の 12 問を別ファイルへ固定する。
3. A/B 主実験の JSONL schema を Claude / Gemini 既存結果と揃える。
4. MVP (`N=20/条件 + 12 問`) を先に回し、通った場合のみ Full run (`N=50/条件`) へ進む。
