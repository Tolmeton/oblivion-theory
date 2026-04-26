# 論文V_繰り込みは忘却である — メタデータ

## §M1 F⊣G 宣言 (論文開始時に固定、途中変更禁止)
- F (発散関手) = 「繰り込みは忘却である」という Type α の同一性主張を核に、QFT の RG・情報幾何・LLM 実測を Type δ 的に接続する。文体ガイドでは `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/遊学エッセイ_文体ガイド.md` の §3 メタファー三連と §10 Type α+δ 合成を採用。
- G (収束関手) = β 関数、異常次元、Padé 極、FRG 截断階層を数式と比較表で閉じる。反論は「T-射影保護破壊」「R の見積り誤差」「観測量の取り違え」を先回りして分解し、文体ガイド §4 と §6 で収束させる。
- 固定日 = 2026-04-14 (既存草稿への後付け整備)

## §M2 核主張リスト (L3 対象)
- C1: 繰り込みは補助計算ではなく、忘却のスケール組織化そのものである。
- C2: $\gamma_\Phi^{\text{obs}} \approx 0.86$ と 1-loop 上界 $\gamma_\Phi \leq 0.129$ の乖離は、パラメータ調整ではなく構造的診断である。
- C3: この乖離は T-射影保護の破壊ではなく、Padé 極を超えた強結合・非摂動領域への突入を意味する。
- C4: 強結合問題の benchmark 第一手は MC であり、理論側の改善は LPA' → DE2 → BMW の階層上昇でしか進まない。

## §M3 Kalon 判定履歴
| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| 2026-04-14 | C3/C4 | △ | 強結合診断と FRG 階層は立っているが、BMW 到達前なので Fix(G∘F) 完了ではない。 |
| 2026-04-14 | C4 (benchmark 順序) | △ | benchmark の first cut を MC に固定。BMW は MC が DE2 を超えた場合の second phase としてのみ正当化される。 |

## §M4 ±3σ ゲート履歴
| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| 2026-04-14 | C3 | +3σ | +3σ | 「理論が間違った」の平均値に退避せず、「強結合なので摂動論が壊れる」へ射程維持。 |
| 2026-04-14 | C4 | +3σ | +3σ | 「FRG を使う」一般論に退かず、LPA' / DE2 / BMW の階層差で問題を刻んだ。 |
| 2026-04-14 | C4 (benchmark 順序) | +3σ | +3σ | 「より高次の solver を作る」一般論に退かず、外部 benchmark = MC / 理論内昇格 = BMW の順序を固定。 |

## §M5 Refutation Gauntlet ログ
### C3 — 2026-04-14 Round 1
- 反論 r = 「0.86 はスケール比 $R$ の雑な見積りか、観測量の取り違えの artifact にすぎないのではないか」
- SFBT = 「できないのではなく、Padé 極超過・Null Result・FRG 截断差を同じ面に並べていないだけではないか」
- 前提強化 = 仮説 C の棄却、Paper IV の Gini Null Result、LPA' / DE2 / BMW の階層差を同じ strong-coupling 問題の下に再配置
- 結果 = 射程維持 ✓

### C4 — 2026-04-14 Round 1
- 反論 r = 「BMW を最初に実装しない限り、0.86 問題は前進しないのではないか」
- SFBT = 「進んでいないのは BMW が無いからではなく、benchmark と solver extension を同じ面で語っていたからではないか」
- 前提強化 = benchmark の役割を MC に固定し、BMW を『MC が DE2 を超えたときの残差同定器』へ格下げせず再定義
- 結果 = 射程維持 ✓

## §M6 虚→実変換面

### C1
- 野望: 繰り込みを補助計算ではなく、忘却がスケールをまたいで有効記述を作る操作そのものとして定式化する。
- 現在まだ虚な点: Markov 的・次元保存的粗視化と指数族近傍では核が立っているが、全ての RG 形式・全ての物理理論に対する普遍同一視ではない。
- 実へ引くための SOURCE: 本文 §2.1--§3.4、Paper III §4.7、Wilson 型 RG の原典、Čencov / Čencov-Morozova / Pitman-Koopman-Darmois 系の定理。
- 実化の判定条件: $\beta_\Phi$ 単調性、RG 不変性、次元的堅牢性を同じ前提条件の下で読めること。非 Markov / 次元縮約 / 非指数族では制限が明示されていること。
- 次の実化操作: §1 と §7.2 で Proved / Diagnosed / Open を明示し、「忘却が物理学の文法である」は定理核から導かれる射程として扱う。
- 最新状態: Proved core / incubation

### C2
- 野望: $\gamma_\Phi^{\mathrm{obs}}\approx0.86$ と 1-loop 上界 $\gamma_\Phi\leq0.129$ の差を、任意の係数調整ではなく構造的診断として固定する。
- 現在まだ虚な点: $\gamma_\Phi^{\mathrm{obs}}$ は Paper IV の観測量・スケール比 $R$・可観測化写像に依存するため、独立 benchmark による再測定は未完である。
- 実へ引くための SOURCE: 本文 §5.2、§5.4、§6.5、§6.8、Paper IV の多層 $\rho_{\mathrm{spec}}$ 実測、Gini Null Result、スケール比 $R$ の操作的定義。
- 実化の判定条件: $R$ の大型化だけでは 1-loop 上界へ逃げられないこと、$n_{\mathrm{eff}}$ 調整だけでは 0.86 を再現できないこと、観測量の対応が少なくとも同一プロトコル内で固定されること。
- 次の実化操作: MC first cut で $\eta(n)$ と $\gamma_\Phi(n)$ を測り、1-loop / 2-loop Padé / LPA' / DE2 と同じ観測量定義で比較する。
- 最新状態: Diagnosed / benchmark open

### C3
- 野望: 0.86 乖離を T-射影保護の破壊ではなく、Padé 極を超えた強結合・非摂動領域への突入として固定する。
- 現在まだ虚な点: 摂動論の no-go と LPA' / DE2 の部分到達は立っているが、非摂動 benchmark が 0.86 側へ到達する機構はまだ閉じていない。
- 実へ引くための SOURCE: 本文 §5.4.6、§5.5.8、§5.5.9、§6.8.3、FRG 文献、DE2 / BMW truncation の benchmark 文献。
- 実化の判定条件: T-射影保護破壊仮説が本文内から消え、Padé 極超過・LPA' 壁・DE2 部分突破が一つの strong-coupling 問題として読めること。
- 次の実化操作: MC benchmark で DE2 を超える残差が出るかを確認し、出た場合にのみ BMW を「残差同定器」として昇格する。
- 最新状態: Diagnosed / nonperturbative reproduction open

### C4
- 野望: 強結合問題の第一手を MC benchmark に固定し、理論側の昇格を LPA' → DE2 → BMW の順序で管理する。
- 現在まだ虚な点: MC 本走査は未実行であり、BMW はまだ実装されていない。したがって 0.86 の完全再現は Paper V の完了条件ではなく、次段 program の判定条件である。
- 実へ引くための SOURCE: 本文 §6.8.4、§6.8.6、§7.1 P-V.6 / P-V.7、meta §M5 C4、LPA' / DE2 の既存数値表。
- 実化の判定条件: 同じ観測量定義で MC / 1-loop / 2-loop Padé / LPA' / DE2 を比較し、MC が DE2 を上回る場合だけ BMW の必要性を正当化できること。
- 次の実化操作: `drafts/infra/experiments/P-V.6_強結合MCベンチマークプロトコル.md` を実行契約として使い、`drafts/infra/experiments/P-V.6_強結合MC_failure_ledger.md` で負・曖昧・未成熟な観測結果の帰属判定を事前固定してから、入力 $n$、格子化、観測量、比較表を実走査する。
- 最新状態: Open program with fixed order

## §M7 棄却された代替案
- 棄却 1 = 「T-射影保護の破壊が起きれば 0.86 は説明できる」。§5.4 以後は否定済みであり、旧仮説のまま残すと論文内部で時制が衝突する。
- 棄却 2 = 「$R$ を大きくすれば 1-loop と整合する」。必要な $R \sim 6.5 \times 10^9$ は BBH の操作的スケールから外れる。
- 棄却 3 = 「LPA' 0.43 で十分なので Paper IV 側を弱めればよい」。これは 0.86 を 0.43 に縮める後退であり、Yugaku の射程規律に反する。
- 棄却 4 = 「BMW を benchmark の第一手にする」。これは FRG 系列の内側を延長するだけで、observable / $R$ / truncation の帰属判定を外部から固定できない。

## §M8 Donor 統合メモ (calculations 棚卸し)

以下は `calculations/` 配下の作業文書から Paper V に関連する donor の棚卸し結果である。いずれも本文 (body) への直接吸収は行わず、meta 参照として記録する。

### D1: 構成_CPS-Gauge関手 (B-class)
- **donor**: `calculations/構成_CPS-Gauge関手.md`
- **内容**: CPS→Gauge の関手的対応を85%構造一致まで構成。ゲージ結合定数空間と Fisher 多様体の関手的接続。
- **本文との関係**: §2.4 の作用汎関数、§6 の再解釈に関連するが、v3.5 の幾何的定式化 (F_{ij}F^{ij} 構造) との直接接続は未整備。
- **判定**: 概念的に有効。本文吸収には v3.5 言語への翻訳が必要。著者判断待ち。

### D2: CPS-YM 関手構成 (A→B 降格)
- **donor**: `calculations/計算_CPS-YM関手構成.md`
- **内容**: 忘却関手 U_YM: Gauge → CPS の明示的構成。対象写像 (G, R, g(μ)) → (α, Θ) と射写像 (ゲージ変換 → id_CPS) を定義。V4 (Higgs 対応の非構成性) 封鎖を目的。
- **降格理由**: v2 §9.4 に対して書かれた計算。Paper V v3.5 では作用汎関数が S[α, Θ] → S[Φ, α; μ] に変更され、場のパラメタ化が異なる。関手の方向 (YM → CPS) と概念は有効だが、v3.5 の曲率テンソル F_{ij} = (α/2)(dΦ∧T)_{ij} を経由した再構成が必要。
- **判定**: 関手構成は valid。v3.5 定式化への適応は著者判断。

### D3: CW 導出 U(Θ) (A→B 降格)
- **donor**: `calculations/計算_CW導出_UΘ.md`
- **内容**: Coleman-Weinberg 1-loop 有効ポテンシャルから U(Θ) を導出。自由パラメータ μ², ν² をゲージ結合定数 g⁴ から決定し、V1 (パラメータ自由度) を封鎖。m_H² = 3g⁴/(8π²)。
- **降格理由**: Paper V v3.5 は U(Θ) ポテンシャル項を含まない。v2 の 2-scalar action S[α, Θ] に対する導出であり、v3.5 の S[Φ, α; μ] (F_{ij}F^{ij} + κ(∂α)² + λΦ²) との直接対応がない。パラメータ消滅という結果自体は概念的に重要。
- **判定**: 結果は有効だが formulation stale。v3.5 での再導出が必要。

### D4: 三未踏踏破 — κ 導出 (A→B 降格)
- **donor**: `calculations/計算_三未踏踏破.md`
- **内容**: Zamolodchikov 計量 G_{IJ} から κ = G_ΘΘ/G_αα を導出。SU(2) では κ = d_R/(C₂(G)·d_A) = 2/6 = 1/3。全パラメータ消滅と5つの数値予測 P1–P5。
- **降格理由**: v3.5 の作用 (line 182) で κ は使用されているが無導出。Zamolodchikov 導出は v2 の対角的2場系 S[α, Θ] を前提とする。v3.5 では Φ の運動項が F_{ij}F^{ij} (非対角的) であるため、κ = G_ΘΘ/G_αα の直接適用に field reparametrization の考慮が必要。
- **判定**: κ=1/3 (SU(2)) は本文の open parameter を埋める最有力候補。ただし v3.5 kinetic structure での再導出を経て初めて body 吸収可能。§7.2 ロードマップへの追記候補。著者判断待ち。

## §M9 Donor Absorption Ledger (2026-04-18)

### D-V-01: TriAttention×忘却論_考察

- **donor path**: `drafts/incubator/TriAttention×忘却論_考察.md`
- **receiver surfaces**: `論文IV_なぜ効果量は小さいか_草稿.md` §8.12-§8.13、`論文V_繰り込みは忘却である_草稿.md` §6.5-§6.8、Paper IV/V meta
- **kept**: 離散 RG 作用素としての TriAttention、`ρ_budget` と `ρ_eff` の分離、RG 不変性主張の引き締め
- **discarded**: donor 単独稿としての叙述順のみ
- **final disposition**: donor file を削除し、RG 側の provenance を Paper V meta に固定
