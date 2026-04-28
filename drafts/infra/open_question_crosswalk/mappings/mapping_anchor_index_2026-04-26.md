# Open Question Crosswalk — Oblivion Anchor Index 2026-04-26

- 作成日: 2026-04-26
- 対象: `intake_2026-04-26_batch01.md` / `intake_2026-04-26_batch02.md` の 32 open questions
- status: `mapped_index`
- 目的: 外部 open question / limitation / future work を、忘却論側の theorem / proposition / concept へ初期対応づけする。

## P-0 Inputs

| input | status | 採用範囲 |
|---|---|---|
| `../typing/typing_2026-04-26_batches01-02_summary.md` | SOURCE-local ledger | 32 OQ の型分類と 6 mapping lanes |
| `../mappings/mapping_QT-COMP-GEN_2026-04-26.md` | SOURCE-local ledger | compression / generalization / SAM / GeoIB mapping |
| `drafts/series/論文I_力としての忘却_草稿.md` | local SOURCE | 方向性定理、FEP 精度対応、α-SAM、CKA-KL、OA-SAM 実験 |
| `drafts/series/論文II_相補性は忘却である_草稿.md` | local SOURCE | Face Lemma、cohomology defect、Stability Simplex、compatibility lemma |
| `drafts/series/論文III_Markov圏の向こう側_草稿.md` | local SOURCE | α>0 Markov / α<0 anti-Markov、Z2-graded CPS、boson-fermion correspondence |
| `drafts/series/論文VI_行為可能性は忘却である_草稿.md` | local SOURCE | G∘F 結晶化随伴、Coherence τ-Invariance |
| `drafts/series/論文VII_知覚は忘却である_草稿.md` | local SOURCE | 知覚関手、構造保存定理、普遍フィルトレーション、量子重力の residual framing |
| `drafts/series/論文VIII_存在は忘却に先行する_草稿.md` | local SOURCE | α-忘却濾過、α-Yoneda、bridge functor、topos/sheaf coarsening、MB 三層 |
| `drafts/series/論文IX_エントロピーは忘却である_草稿.md` | local SOURCE | CPS entropy、単調性、critical forgetting threshold、forgetting energy |
| `drafts/series/論文X_ContextRotは忘却である_草稿.md` | local SOURCE | 条件付き不可逆性、状態依存最適忘却、boot⊣bye drift-performance |
| `drafts/series/論文XII_速度は忘却である_草稿.md` | local SOURCE | 欠如比 χ、Level 0/1 分離、hBN 位相特異点を外部較正点にする測定 protocol |

棄却:

| branch | 理由 |
|---|---|
| open question を「全部、忘却です」で束ねる | 候補回答ではなく語彙置換になる。OQ ごとに、欠落している説明の形と対応 anchor を分ける。 |
| theorem と concept を同じ強さで扱う | 外部 contact に使えるのは theorem / proposition / empirical anchor が揃うものだけ。concept は case seed に留める。 |
| physics / cognition / AI を同じ claim level で横断する | 物理系は observational calibration、認知系は explanation principle、最適化系は experiment seed として claim level を分ける。 |

## P-1 Anchor Inventory

| anchor | claim level | SOURCE | usable for | caution |
|---|---|---|---|---|
| `I-T5.1` 方向性定理 | theorem | `drafts/series/論文I_力としての忘却_草稿.md:203-235` | 圧縮・一般化・測定 proxy を「量」ではなく忘却の方向として扱う核。 | operational estimator は未完。 |
| `I-FEP-6.5` FEP 精度場対応 | constructive proposition | `drafts/series/論文I_力としての忘却_草稿.md:708-754` | precision weighting / psychopathology を α 場の幾何として読む入口。 | 圏的同値ではなく線形化レベルの構成的対応。 |
| `I-P6.6.1` 曲率の α_I-線形性 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:760-766` | precision / α 介入が曲率へ正確に線形反映される点。 | FEP の π と同一化する部分は別構成が必要。 |
| `I-P6.7.1/2` α-SAM / 表現制御 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:801-821` | SAM / Fisher SAM / representation control の候補機構。 | 大規模実装は未検証。 |
| `I-P6.8.1` α-Oblivion SAM 包含 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:864-893` | SAM → Fisher SAM → α-SAM → OA-SAM の特殊化関係。 | λ 安定性と Φ 定義に依存。 |
| `I-T6.8.1` CKA-KL 分離 | theorem | `drafts/series/論文I_力としての忘却_草稿.md:897-905` | representation alignment / information-plane / proxy failure の測定分解。 | 近似仮定を外部 case で明示する。 |
| `I-P6.8.2/3` CKA-KL 方向保存・比例 | proposition | `drafts/series/論文I_力としての忘却_草稿.md:907-923` | CKA 操作量と KL 理論量の橋渡し。 | CKA のスケール盲点を併記する。 |
| `I-E12` OA-SAM 実験 | empirical | `drafts/series/論文I_力としての忘却_草稿.md:961-1028` | same accuracy / different forgetting attractors、λ 符号制御。 | small-scale empirical clue。 |
| `II-T3.4.1` Face Lemma | theorem | `drafts/series/論文II_相補性は忘却である_草稿.md:407-440` | emergence / verification / minimal nontrivial face の条件。 | 物理・DL へ使う時は比喩化を避ける。 |
| `II-H2` cohomology defect | concept / theorem seed | `drafts/series/論文II_相補性は忘却である_草稿.md:522-536` | HoTT / cohomology / obstruction 型 OQ。 | QM instance 中心で一般化は未閉。 |
| `II-Stability-Simplex` Stability Simplex | theorem | `drafts/series/論文II_相補性は忘却である_草稿.md:575-629` | syntax-semantics / categorical DL / emergence threshold。 | 外部形式体系へは再記述が必要。 |
| `II-Compat` Fritz compatibility lemma | lemma | `drafts/series/論文II_相補性は忘却である_草稿.md:732-776` | Markov blanket / conditional independence / FEP closure。 | leak quantification は別課題。 |
| `III-Z2-CPS` Z2-graded CPS | definition / theorem family | `drafts/series/論文III_Markov圏の向こう側_草稿.md:152-208` | fermionic QI / no-copy / factorization ambiguity。 | 物理 claim は external grounding が要る。 |
| `III-BF` boson-fermion correspondence | theorem | `drafts/series/論文III_Markov圏の向こう側_草稿.md:202-208` | spin-statistics / α>0 Markov and α<0 anti-Markov の橋。 | direct theorem としては CPS 圏内。 |
| `VI-D2.1.1` G∘F 結晶化随伴 | definition | `drafts/series/論文VI_行為可能性は忘却である_草稿.md:68-79` | memory consolidation / down-selection / schema formation。 | sleep physiology への直答ではない。 |
| `VI-T3.3.1` Coherence τ-Invariance | theorem | `drafts/series/論文VI_行為可能性は忘却である_草稿.md:268-299` | 粒度が変わっても結晶化後の質が保たれる条件。 | 3 条件を外部系で検査する必要。 |
| `VII-D1.3.1` 知覚関手 | definition | `drafts/series/論文VII_知覚は忘却である_草稿.md:47-49` | feature ontology / measurement choice / proxy formation。 | 広すぎるため case では補助 anchor。 |
| `VII-T6.1.1` 構造保存定理 | theorem | `drafts/series/論文VII_知覚は忘却である_草稿.md:575-586` | representation / transfer / alignment の核。 | 外部表現空間の構造対応が必要。 |
| `VII-T6.3.1` 普遍フィルトレーション | theorem | `drafts/series/論文VII_知覚は忘却である_草稿.md:659-667` | substrate independent transfer / architecture invariance。 | 「普遍」の読み過ぎに注意。 |
| `VII-QG-residual` 量子重力 residual framing | concept | `drafts/series/論文VII_知覚は忘却である_草稿.md:160-189` | holography / QG を self-referential forgetting と読む種。 | concept 段階。contact anchor には弱い。 |
| `VIII-D6.2.1/T6.2.3` α-忘却濾過 / α-Yoneda | definition / theorem | `drafts/series/論文VIII_存在は忘却に先行する_草稿.md:456-492` | HoTT truncation / reconstruction / representation recovery。 | OP-VIII-5 は open として残る。 |
| `VIII-Bridge` bridge functor | definition / proposition | `drafts/series/論文VIII_存在は忘却に先行する_草稿.md:647-656`, `drafts/series/論文VIII_存在は忘却に先行する_草稿.md:732-748` | higher structures / invariance / transfer の形式 bridge。 | faithful 条件を外部圏で確認する。 |
| `VIII-Topos` α-oblivion topos / sheaf coarsening | corollary / theorem | `drafts/series/論文VIII_存在は忘却に先行する_草稿.md:935-955` | HoTT / topos / sheaf OQ の形式的入口。 | HoTT (-1)-truncation 直結は open program。 |
| `VIII-MB3` MB0/MBp/MBf 三層 | concept / response | `drafts/series/論文VIII_存在は忘却に先行する_草稿.md:1148-1164` | FEP / active inference / Markov blanket persistence。 | response framing。case では II-Compat と併用。 |
| `IX-D3.3.1/T3.4.1` CPS entropy / monotonicity | definition / theorem | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:112-132` | IB / compression / entropy / memory down-selection。 | Kolmogorov complexity への直答ではない。 |
| `IX-P3.5.1` critical forgetting threshold | proposition | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:156-172` | どこまで忘れても finite entropy / recoverability が残るか。 | 実データ推定が必要。 |
| `IX-P4.1.1` double coarse-graining | proposition | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:197-217` | coarse/fine entropy measure の階層。 | algorithmic profile には追加 bridge。 |
| `IX-E(f)` forgetting energy | definition / proposition | `drafts/series/論文IX_エントロピーは忘却である_草稿.md:332-356`, `drafts/series/論文IX_エントロピーは忘却である_草稿.md:364-385` | survivability / thermodynamic metaphor / partition function。 | 物理量としての同定は段階化が必要。 |
| `X-P1/P2` 条件付き不可逆性 / 状態依存最適忘却 | proposition | `drafts/series/論文X_ContextRotは忘却である_草稿.md:94-129` | context degradation / LITM / retrieval strategy。 | LLM context-specific。 |
| `X-P3` boot⊣bye drift-performance | proposition | `drafts/series/論文X_ContextRotは忘却である_草稿.md:271-291` | memory consolidation / long-context reset / drift control。 | runtime experiment が必要。 |
| `XII-χ` 欠如比 / Level 0-1 分離 | definition / protocol | `drafts/series/論文XII_速度は忘却である_草稿.md:443-470` | hyperbolic media / observational calibration。 | theorem ではなく external calibration protocol。 |

## P-2 OQ-to-Anchor Matrix

| OQ ID | type | candidate anchor | candidate answer pattern | grade |
|---|---|---|---|---|
| `OQ-B01-001` | `QT-REP-ONTO` | `VII-D1.3.1`, `VII-T6.1.1`, `VIII-D6.2.1/T6.2.3`, `I-T6.8.1` | feature は表象の atom ではなく、どの知覚関手・濾過段階で構造保存されるかの residue として定義する。 | B+ |
| `OQ-B01-002` | `QT-FORMAL-VERIF` | `II-T3.4.1`, `II-Stability-Simplex`, `VIII-Bridge` | toy model から frontier への移行は、単純化の量ではなく、2-simplex / face が保たれるかで判定する。 | B |
| `OQ-B01-003` | `QT-TRANSFER-INV` | `VII-T6.1.1`, `VII-T6.3.1`, `VIII-Bridge` | architecture transfer は、基質を越えて保存される忘却フィルトレーションの段階を探す問題になる。 | B+ |
| `OQ-B01-004` | `QT-META-AGENDA` | split required | NLP open agenda bundle は単一対応しない。child OQ に分割してから mapping する。 | split |
| `OQ-B01-005` | `QT-MEAS-DEFORM` | `VII-D1.3.1`, `I-T6.8.1`, `X-P1/P2` | benchmark / proxy は対象を外から測るだけでなく、どの忘却関手を通した対象を作っているかを固定する。 | B |
| `OQ-B01-006` | `QT-CLOSURE` | `VIII-MB3`, `II-Compat`, `X-P1/P2` | active-inference loop の閉鎖性は MB を一枚の境界として置くのではなく、MB0/MBp/MBf の層差と leak で診断する。 | B+ |
| `OQ-B01-007` | `QT-COMP-GEN` | `I-T5.1`, `I-E12`, `IX-D3.3.1/T3.4.1`, `IX-P3.5.1` | generalization は parameter count ではなく、recoverable な忘却後構造が残るかで読む。 | B |
| `OQ-B01-008` | `QT-COMP-GEN` | `I-T5.1`, `I-T6.8.1`, `I-P6.8.2/3`, `IX-D3.3.1/T3.4.1` | information-plane の収束点は単一情報量でなく、shape / scale / direction に分解された忘却場の射影として読む。 | A- |
| `OQ-B01-009` | `QT-EMERGENCE` | `II-T3.4.1`, `II-Stability-Simplex`, `VII-T6.3.1` | depth / scale の利得は、追加層そのものではなく非自明な face / simplex が保存される時だけ出る。 | B |
| `OQ-B01-010` | `QT-CLOSURE` | `II-Compat`, `VIII-MB3`, `X-P3` | wandering Markov blankets は、境界の移動ではなく、conditional independence の leak と boot/bye 後の復元非一意性として扱う。 | B+ |
| `OQ-B01-011` | `QT-CONTEXT` | `X-P1/P2`, `X-P3`, `VIII-D6.2.1/T6.2.3` | long-context degradation は状態依存の最適忘却が失敗し、薄い MB が維持限界を超える現象として読む。 | A- |
| `OQ-B01-012` | `QT-MEAS-DEFORM` | `I-T6.8.1`, `I-P6.8.2/3`, `VII-T6.1.1` | alignment proxy の不一致は、形状だけを見る測定と形状+スケールを見る測定の関手差として分解する。 | A- |
| `OQ-B01-013` | `QT-EMERGENCE` | `II-T3.4.1`, `I-T6.8.1`, `IX-P3.5.1` | emergence / mirage は、測定関手が閾値を作っている場合と、非自明 face が本当に生じる場合を分ける。 | B |
| `OQ-B01-014` | `QT-GEOM-OBSTR` | `IX-D3.3.1/T3.4.1`, `IX-P4.1.1` | Kolmogorov 問題への直答ではなく、Shannon/Renyi/Gini 側を deterministic reference loss として統一する bridge seed。 | C |
| `OQ-B01-015` | `QT-GEOM-OBSTR` | `I-P6.6.1`, `I-P6.7.1/2`, `I-P6.8.1`, `IX-D3.3.1/T3.4.1` | α≠±1 の実例を、抽象接続ではなく α-SAM / OA-SAM の update-direction control として与える。 | B+ |
| `OQ-B01-016` | `QT-SYN-SEM` | `VIII-D6.2.1/T6.2.3`, `VIII-Bridge`, `II-Stability-Simplex` | categorical DL の syntax / semantics gap は、証人・意味・存在を同じ強度で保持しない α-同定問題として読む。 | B |
| `OQ-B02-001` | `QT-FACT-AMB` | `VII-QG-residual`, `VIII-Topos`, `IX-E(f)` | black-hole / subregion ambiguity は、部分系分解の失敗を self-referential forgetting の residual として記述する。 | C+ |
| `OQ-B02-002` | `QT-DECOMP-REC` | `VIII-D6.2.1/T6.2.3`, `VII-T6.1.1`, `IX-P3.5.1` | holographic reconstruction は、どの α 段階なら構造が recoverable かを問う問題に変換する。 | B |
| `OQ-B02-003` | `QT-COMP-GEN` | `I-P6.7.1/2`, `I-P6.8.1`, `I-E12` | SAM の flatness 仮説を、Euclidean sharpness から forgetting-field direction の制御へ拡張する。 | B+ |
| `OQ-B02-004` | `QT-GEOM-OBSTR` | `I-P6.6.1`, `I-P6.7.1/2`, `I-P6.8.1` | Fisher SAM の自然勾配化は、α-接続近傍の特殊化として整理できる。 | A- |
| `OQ-B02-005` | `QT-MEAS-DEFORM` | `I-T6.8.1`, `I-P6.8.2/3`, `I-E12` | SAM approximation instability は、sharpness proxy が内部忘却 attractor を見落とす測定問題として扱う。 | B+ |
| `OQ-B02-006` | `QT-COMP-GEN` | `IX-D3.3.1/T3.4.1`, `IX-P3.5.1`, `IX-P4.1.1`, `I-T6.8.1` | GeoIB / IB は compression scalar ではなく、recoverability threshold と測定分解で拡張する。 | B+ |
| `OQ-B02-007` | `QT-GEOM-OBSTR` | `VIII-Topos`, `II-H2`, `VIII-D6.2.1/T6.2.3` | HoTT / cohomology の計算問題は、証人消去と obstruction を別層で扱う必要がある。 | B |
| `OQ-B02-008` | `QT-GEOM-OBSTR` | `VIII-D6.2.1/T6.2.3`, `VIII-Topos`, `II-Stability-Simplex` | strict equality / semi-simplicial の難所は、同一性をどの α 強度で保持するかの問題として読む。 | B |
| `OQ-B02-009` | `QT-GEOM-OBSTR` | `VII-T6.3.1`, `VIII-Bridge`, `VIII-Topos` | higher structures の invariance は、普遍フィルトレーションと bridge functor の faithful 条件へ落とす。 | B |
| `OQ-B02-010` | `QT-SYN-SEM` | `II-Stability-Simplex`, `VIII-Bridge`, `VIII-Topos` | enriched / Gray tensor の coherence は、どの compositional face が壊れず残るかの問題として扱う。 | B- |
| `OQ-B02-011` | `QT-OBS-ACCESS` | `XII-χ`, `VII-D1.3.1` | hyperbolic media は候補回答ではなく、欠如の境界と担体の速度を分ける外部較正点として使う。 | calibration |
| `OQ-B02-012` | `QT-FACT-AMB` | `III-Z2-CPS`, `III-BF`, `IX-D3.3.1/T3.4.1` | fermionic QI の no-copy / factorization ambiguity は、α<0 anti-Markov セクターとして整理する。 | A- |
| `OQ-B02-013` | `QT-PRECISION-MECH` | `I-FEP-6.5`, `I-P6.6.1`, `VIII-MB3` | precision weighting の機構は、π を直接実体化せず、α 場と MB 層差の coupling として説明する。 | B+ |
| `OQ-B02-014` | `QT-PRECISION-MECH` | `I-FEP-6.5`, `I-P6.6.1`, `VIII-MB3` | ASD など障害別 specificity は、精度の大小ではなく異方的な α / MB leak profile として立てる。 | B |
| `OQ-B02-015` | `QT-MEM-CONSOL` | `VI-D2.1.1`, `VI-T3.3.1`, `IX-D3.3.1/T3.4.1`, `X-P3` | SHY だけでは足りない記憶選別は、G∘F 結晶化と entropy monotonicity の組として読む。 | B |
| `OQ-B02-016` | `QT-MEM-CONSOL` | `VI-D2.1.1`, `VI-T3.3.1`, `IX-P3.5.1`, `X-P3` | sleep down-selection は、忘却で消す過程ではなく、recoverable な結晶単位を残す相転移として扱う。 | B+ |

## P-3 Promotion Priority

| priority | target | reason | next operation |
|---|---|---|---|
| P1 | `OQ-B01-008` information-plane / CKA-KL | 外部 IB open question と Paper I の theorem anchor が最も強い。 | case 化して外部 quote と `I-T6.8.1` を対置する。 |
| P2 | `OQ-B02-004` Fisher SAM / natural-gradient SAM | 外部 SAM 系 open question と `α-SAM` 系 proposition が同じ最適化面に乗る。 | `mapping_QT-COMP-GEN_2026-04-26.md` に増補し、実験設計へ落とす。 |
| P3 | `OQ-B02-012` fermionic QI factorization | `III-Z2-CPS` / `III-BF` がかなり直接に当たる。 | factorization quote を取り、anti-Markov case にする。 |
| P4 | `OQ-B01-011` long context degradation | Paper X が専用 anchor を持つため、説明原理として強い。 | Context Rot case へ分岐。 |
| P5 | `OQ-B02-016` sleep down-selection | Paper VI + IX + X の三点で concept は強いが、生理学 directness は弱い。 | clinical / neuroscience ではなく memory-selection case として低 claim で起こす。 |

## P-4 Rejection Ledger

| rejected mapping | reason |
|---|---|
| `OQ-B02-001` を Paper XIII で直答扱い | 今回の SOURCE read は Paper VII / VIII / IX まで。Paper XIII の時空・質量 CPS span は未精読のため anchor_pending に留める。 |
| `OQ-B02-007` HoTT を OP-VIII-5 で解決済み扱い | Paper VIII 自身が HoTT (-1)-truncation 接続を open program として残している。 |
| `OQ-B02-011` hyperbolic media を忘却論の勝利例として使う | Paper XII でも測定 protocol / external calibration であり、候補回答ではない。 |
| `OQ-B02-015` sleep を SHY の代替理論として主張 | 現段階では memory down-selection の説明原理。睡眠生理の direct replacement ではない。 |

## Carry Forward

次の detailed mapping:

1. `mapping_lane_B_boundary_reconstruction.md` を作り、`OQ-B02-012` を優先 case にする。
2. `cases/OQ-B01-008_information_plane_CKA_KL.md` を作る。
3. `cases/OQ-B02-004_fisher_sam_alpha_sam.md` を作る。
4. `OQ-B02-003/004/005/006` は `mapping_QT-COMP-GEN_2026-04-26.md` に増補済みなので、次は case / experiment seed へ昇格する。
