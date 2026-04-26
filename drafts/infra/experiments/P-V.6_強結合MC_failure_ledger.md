# P-V.6 強結合 MC failure ledger

**日付**: 2026-04-26
**状態**: pre-run failure ledger fixed / MC benchmark 未本走査
**対象**: P-V.6 強結合 MC benchmark protocol の負・曖昧・未成熟な観測結果
**目的**: MC 実行後の後知恵的救済を防ぎ、各失敗型を claim impact / next operation / forbidden interpretation に事前対応させる。

## 0. SOURCE 境界

| SOURCE | 役割 |
|:---|:---|
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/experiments/P-V.6_強結合MCベンチマークプロトコル.md` | Phase gate、Decision Table、Exit Criteria の正本 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/plans/P-V.6_強結合benchmark計画_v1.md` | BMW first / DE2 close / 0.86 弱化を棄却した設計根拠 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文V_繰り込みは忘却である.meta.md` §M6 C4, §M7 | MC first / BMW second と棄却代替案の meta contract |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/results_strong_coupling/phase1_analysis.md` | Phase 0 / Phase 1 の現行通過状態 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/experiments/results_strong_coupling/phase5_fractional_topology_analysis.md` | H3/H4 surface の anchor 未到達状態 |

## 1. Ledger Contract

この ledger は、MC benchmark の結果が出る前に固定する失敗時解釈表である。

- 0.86 の完全再現は、この ledger の成功条件ではない。
- 失敗結果を Paper V の証明済み核に波及させない。
- 失敗結果を 0.86 の後知恵的救済にも使わない。
- 各 failure mode は、必ず `claim impact` と `forbidden interpretation` を伴って読む。

## 2. Claim Impact Labels

| Label | 意味 |
|:---|:---|
| `NO-IMPACT-CORE` | $\beta_\Phi$ 単調性、RG 不変性、次元的堅牢性、1-loop 上界には影響しない |
| `DIAGNOSIS-ONLY` | strong-coupling diagnosis は保つが、0.86 への到達機構は未閉鎖のまま |
| `PAPER-IV-RETURN` | Paper IV 側の observable / $R$ / calibration に差し戻す |
| `SOLVER-PROMOTE` | BMW など momentum-dependent solver への昇格理由になる |
| `PROXY-REBUILD` | 現行 proxy family / selector / topology を作り直す |
| `BENCHMARK-INVALID` | MC benchmark として未成熟。理論的帰属判定に使わない |

## 3. Failure Ledger

| ID | 観測 | Failure Type | Claim Impact | Next Operation | Forbidden Interpretation |
|:---|:---|:---|:---|:---|:---|
| F0 | Phase 0 reference が 3D Ising の既知値を再現しない | MC pipeline invalid | `BENCHMARK-INVALID`, `NO-IMPACT-CORE` | MC 実装、thermalization、observable extraction を修正 | Paper V の 0.86 診断が崩れた、と読むこと |
| F1 | Phase 1 の schema completeness / dimension alignment が FAIL | schema invalid | `BENCHMARK-INVALID` | `strong_coupling_common.py` と出力 schema を修正 | 数値の大小から solver 優劣を読むこと |
| F2 | finite-size drift / autocorrelation / scaling window 依存が大きい | benchmark immature | `BENCHMARK-INVALID` | lattice size、update kernel、FSS protocol を作り直す | 0.86 に近い window だけを採用すること |
| F3 | fractional / T-projected proxy が FRG anchors へ calibrate できない | proxy calibration failure | `PROXY-REBUILD`, `DIAGNOSIS-ONLY` | fractional proxy と T-projection mapping を再設計 | proxy 失敗を 0.86 no-go の失敗と混同すること |
| F4 | MC が DE2 と同程度で、両者とも 0.86 から遠い | truncation not dominant | `PAPER-IV-RETURN`, `DIAGNOSIS-ONLY` | Paper IV 側の observable / $R$ / calibration を再監査 | BMW を自動起動すること |
| F5 | MC が DE2 を系統的に上回るが、0.86 には届かない | partial truncation residual | `SOLVER-PROMOTE`, `DIAGNOSIS-ONLY` | BMW を残差同定器として起動 | 「0.86 を解いた」と書くこと |
| F6 | MC が 0.86 側へ寄るが selector / topology 変更にだけ依存する | selector overfit | `PROXY-REBUILD` | cross-$n$ portability を満たす proxy family へ移る | 局所 selector の成功を benchmark 成功と扱うこと |
| F7 | MC が 0.86 に近いが cross-$n$ portability を満たさない | non-portable anchor hit | `PROXY-REBUILD`, `DIAGNOSIS-ONLY` | n-grid と scaling window を拡張して再判定 | 単一点 anchor hit を再現と呼ぶこと |
| F8 | MC が 0.86 へ robust に近づき、DE2 を上回り、cross-$n$ portability も満たす | strong truncation evidence | `SOLVER-PROMOTE` | BMW / momentum-dependent solver を本命化し、Paper IV observable mapping を再確認 | MC だけで Paper V を Proved に昇格すること |
| F9 | 必要な $R$ または scale ratio が Paper IV の操作的範囲から外れる | scale-ratio mismatch | `PAPER-IV-RETURN` | Paper IV の $R$ 推定と可観測化を再較正 | large-$R$ rescue として採用すること |
| F10 | $\eta(n)$ と $\gamma_\Phi(n)$ の定義が script / Paper V / Paper IV の間で一致しない | observable mismatch | `BENCHMARK-INVALID` | observable dictionary と conversion rule を先に固定 | 不一致な観測量を同じ表で比較すること |
| F11 | topology / selector を変えても全 surface が out-of-anchor のまま | proxy family exhausted | `PROXY-REBUILD` | long-range / hierarchical / nonlocal proxy family を検討 | selector tweak の反復で情報利得があると見なすこと |
| F12 | calibration が FRG anchors に過適合し、independent rows で崩れる | calibration leakage | `BENCHMARK-INVALID`, `PROXY-REBUILD` | calibration / validation を分離 | calibrated rows の一致を外部再現と呼ぶこと |
| F13 | 0.86 に近い値が Paper IV 想定と別の $n_{\mathrm{eff}}$ でのみ出る | $n_{\mathrm{eff}}$ mapping mismatch | `PAPER-IV-RETURN`, `DIAGNOSIS-ONLY` | Paper IV の $n_{\mathrm{eff}}$ 逆推定を再監査 | 0.86 の再現として即採用すること |
| F14 | Paper IV target $\gamma_\Phi^{\mathrm{obs}}\approx0.86$ 自体が再測定で不安定になる | target instability | `PAPER-IV-RETURN` | Paper IV target を再確定し、Paper V では target を TAINT に戻す | target 不安定性を solver の問題として処理すること |

## 4. Decision Precedence

結果が複数の failure mode に該当する場合、次の順に読む。

1. `BENCHMARK-INVALID` がある場合、理論的帰属判定に進まない。
2. observable mismatch がある場合、数値の近さを評価しない。
3. finite-size / portability が未通過なら、単一点 anchor hit を採用しない。
4. `PAPER-IV-RETURN` と `SOLVER-PROMOTE` が競合する場合、observable / $R$ / calibration を先に潰す。
5. BMW は `SOLVER-PROMOTE` かつ `BENCHMARK-INVALID` なしのときだけ起動する。

## 5. Update Contract

この ledger を変更した場合、次の面も同期する。

| 面 | 同期内容 |
|:---|:---|
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/infra/experiments/P-V.6_強結合MCベンチマークプロトコル.md` §8, §9 | Rejection Ledger / Exit Criteria との接続 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文V_繰り込みは忘却である.meta.md` §M6 C4 | 次の実化操作 |
| `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/plans/P-V.6_強結合benchmark計画_v1.md` §7 | 棄却 ledger から failure ledger への参照 |

## 6. Exit Rule

P-V.6 の MC benchmark は、成功だけで進むのではない。失敗した場合も、この ledger のどの ID に該当するかを記録すれば一段閉じる。

ただし、どの ID でも次は禁止する。

- `Open` を `Proved` に昇格すること。
- 0.86 を「解いた」と書くこと。
- Paper IV target の不安定性を Paper V の solver 成功として処理すること。
- MC benchmark の未成熟を理論的帰属判定に読み替えること。
