# 論文XIV_曲率は忘却の繰り上がりである — メタデータ

## §M1 F⊣G 宣言 (固定日: 2026-04-14)

- F (発散関手) = automath / Omega / 忘却論の三者対応を、離散 defect・連続曲率・圏論的忘却の三面へ展開する操作。文体ガイド §3 のメタファー三連と、分野越境 (symbolic dynamics ↔ information geometry ↔ category theory) を含む
- G (収束関手) = 上記の展開を、原典参照・反例・機械検証・Lean 型シグネチャへ蒸留する操作。文体ガイド §4 の数式裏付け + dictionary 正本 + NotebookLM/ローカル SOURCE 照合
- 固定日: 2026-04-14

## §M2 核主張リスト (L3 対象)

- C1: automath の carry defect は、忘却論の合成ドリフト / 忘却曲率の離散・有限体インスタンスである
- C2: OP-I-2 は単一の未証明問題ではなく、`ZeroForgetCollapse` を要する公理の穴、弱*連続測度族 `μ_λ` を要する極限の穴、`Discretizable` / `DescendsToCube` を要する関手の穴に分かれる
- C3: 黄金比 φ は外部からの輸入ではなく、排他制約と n-cell tower の成長率として忘却論の内部に現れる
  - **C3-core (Route D)**: 排他性 + grade 分離により `A(n)=A(n-1)\sqcup A(n-2)` の recurrence が立ち、Cor. F2.2 として seed 非依存に `growth rate = φ` が従う
  - **Route A**: C3-core の離散証人。反 Markov セクターと no-consecutive-1s 制約が同じ排他則を示す
  - **Route C**: C3-core の entropic corollary。排他制約の下で容量上限が `log φ` に落ちる
  - **Route B**: C3-core で得られた φ を `Fix(G∘F)` と読む Kalon 解釈。一次証明ではなく解釈層
  - **残る proof debt**: `ℤ₂→ℕ` の次数拡張 / seed `|A(1)|, |A(1.5)|` の確定 / 連続極限リフト。ここで seed は具体列の debt であり、漸近主張の debt ではない。Lean は verification layer であって本体ではない

## §M3 Kalon 判定履歴

| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| 2026-04-17 | C1 | ◯ Kalon△ | carry defect ↔ 合成ドリフトを「全域関手」ではなく `Man_No11` 制限付き strictness + 全域では schema として再固定。射程を縮めずに overclaim を除去 |
| 2026-04-14 | C2 | ◯ Kalon△ | `δ=0 ⇒ Hom∈{0,1}` を無条件主張から切り離し、橋梁公理・弱*リフト・全域関手化の三穴へ分解。射程を縮めずに論理を精密化 |
| 2026-04-17 | C3 | ◯ Kalon△ | Route D を proof spine、A/C/B を支線へ再配置。さらに recurrence と seed 非依存の漸近主張を切り分け、seed debt を具体列側へ押し込んだ。残るのは `ℤ₂→ℕ`、具体列、連続極限リフト |

## §M4 ±3σ ゲート履歴

| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| 2026-04-17 | C1 | ±3σ | ±3σ | 維持 — 「離散版 = 連続版の全域関手的証明」という誤読を封じつつ、局所模型 / 制限付き strictness の主張を保持 |
| 2026-04-14 | C2 | ±3σ | ±3σ | 維持 — 「連続版は未証明」を超えて「どこが穴か」を三分割し、μ への後退を回避 |
| 2026-04-17 | C3 | +4σ | +4σ | 維持 — 四並列のエッセイ束を一本の proof spine へ整理しつつ、`growth rate = φ` を concrete sequence から分離して μ への後退を回避 |

## §M5 Refutation Gauntlet ログ

### C1 — 2026-04-17 Round 1
- 反論 r: 「carry defect と忘却曲率の対応は analogy にすぎず、series 本体の核主張としては強すぎる」
- SFBT: できないのではなく、`theorem / schema / open` のラベルを分けていないだけではないか?
- 前提強化: C1 を「全域関手の完成」から切り離し、離散側 Lean 証明済み / `Man_No11` 上の strictness / `Man` 全体では schema という三層へ分解
- 結果: 射程維持 ✓ — 「離散・有限体インスタンス」という核を残したまま、過剰な一般化だけを剥がせた

### C1 — 2026-04-17 Round 2
- 反論 r: `D: \mathbf{Man} \to \mathbf{Hyp}` を関手と呼ぶ限り、本文自身が open と衝突している
- SFBT: 別角度から吸収できないか?
- 前提強化: 本文 §4.4 を `離散化 schema D と制限付き関手性` に改め、strictness が回復する範囲を `Man_No11` に限定。全域拡張には `Discretizable` / `DescendsToCube` の proof debt が残ると明示
- 結果: 射程維持 ✓ — C1 は「関手完成」ではなく「局所模型の固定」として防衛可能になった

### C1 — 2026-04-17 Round 3
- 反論 r: 連続側の carryElement 対応物が未定なら、C1 本体も弱いのではないか
- SFBT: できるとしたら、前に進めるとしたら?
- 取り込み戦略: carryElement ↔ 連続幾何量の同定を C1 の必要条件から外し、C1 本体は defect / drift / curvature condition の対応へ限定する。carryElement の幾何学的実体は open list に隔離
- 結果: 射程維持 ✓ — 本体命題と donor / open を分離できた

### C2 — 2026-04-14 Round 1
- 反論 r: `δ = 0` が示せれば、Hom の Boolean 崩壊も既存公理から従うのではないか
- SFBT: できないのではなく、やっていないだけではないか?
- 前提強化: 一対象圏 `Hom(*,*)=[0,1]`, 合成 `= min`, `G = id` の反例を採用し、`OP-I-3 + δ=0` では `Hom(*,*)=1/2` を排除できないことを SOURCE 化
- 結果: 射程維持 ✓ — 問題は「証明不足」ではなく「追加公理が必要」と確定

### C2 — 2026-04-14 Round 2
- 反論 r: なら OP-I-2 全体を後退させるしかないのではないか
- SFBT: 別角度から吸収できないか?
- 前提強化: OP-I-2 を三分割する。公理の穴 = `ZeroForgetCollapse`、極限の穴 = `μ_λ` 弱*連続測度族、関手の穴 = `Discretizable` / `DescendsToCube` + Strategy B
- 結果: 射程維持 ✓ — 主張は「偽の全証明」から「設計図が露出した未解決問題」へ精密化

### C2 — 2026-04-14 Round 3
- 反論 r: `ZeroForgetCollapse` の採用は恣意的ではないか
- SFBT: できるとしたら、前に進めるとしたら?
- 取り込み戦略: 本稿では `ZeroForgetCollapse` を**橋梁公理**として採用しつつ、導出済みとは主張しない。本文では局所的に `(d)→(e)` を閉じる役割に限定し、将来課題として「より深い原理からの導出」を明記
- 結果: 射程維持 ✓ — 公理採用と導出保留を両立

### C3 — 2026-04-17 Round 1
- 反論 r: Route A-D を並べるだけでは「四本のエッセイ」が併置されているだけで、何が証明本体か分からない
- SFBT: できないのではなく、並べ方を変えていないだけではないか?
- 前提強化: Route D を **C3-core / proof spine** に固定し、Route A を離散証人、Route C を entropic corollary、Route B を Kalon 読みへ後退させる
- 結果: 射程維持 ✓ — 新しい第五経路を足さずに、既存四経路の地位を整理するだけで論証剛性が上がった

### C3 — 2026-04-17 Round 2
- 反論 r: それでも C3-core は Paper 0 の言い換えにすぎず、未解決が散らばったままではないか
- SFBT: 別角度からではなく、残差を減らす形で前に進めるとしたら?
- 前提強化: proof debt を三件へ限定する。`ℤ₂→ℕ` の次数拡張、seed `|A(1)|, |A(1.5)|` の確定、連続極限リフト。Lean は proof debt の代用品でなく verification layer と明記
- 結果: 射程維持 ✓ — C3 は「路線が多い」状態から「主線が見え、残差も数えられる」状態へ移行

### C3 — 2026-04-17 Round 3
- 反論 r: seed が未確定なら `φ` を本文の核主張に据えるのは早すぎるのではないか
- SFBT: できないのではなく、漸近主張と具体列を分けていないだけではないか?
- 前提強化: 命題 F2.1 を recurrence、系 F2.2 を seed 非依存の漸近主張として露出させる。seed debt は tower 全体の具体列に限定し、`growth rate = φ` から切り離す
- 結果: 射程維持 ✓ — `φ` は「種が決まったら出る数」ではなく、「再帰が立った時点で出る支配根」として防衛可能になった

### C3-core — 2026-04-27 Round 4 (連続極限リフトの再精密化)
- 反論 r: 「連続極限リフトを Open C: lax monoidal coherence の defect 2-cell 同定に再精密化し、3 路線 (橋梁公理 / 弱*連続測度族 / Discretizable+DescendsToCube) に分けるのは、単一の未解決問題を 3 つに分割しただけの責務再配分であり、実質的前進ではない」
- SFBT: できないのではなく、何が閉じて何が残ったかを区別していないだけではないか?
- 試行: 問題位相の 1 段下げを 2 つの操作に分解 — (a) 既に閉じている部分の露出 (Theorem A: strict 1-functor on `CubeExp_proj` with `restrict_functorial` Lean witness, Theorem B: chain-map on multilinear obs as cubical cochain-level theorem)、(b) 残る未解決の正確な型付け (Open C: lax monoidal coherence — 求める型は ordinary functor ではなく lax monoidal functor / pseudofunctor、bridge essay §2.4 confessed)
- 実化操作: SOURCE 追加 (関手の合成保存問題_再定式化.md L8-23 / 曲率は忘却のcarryである_草稿.md L99-105 / 三者対応辞書.md §2.B-§2.C) + body §4.4 の 3 段分離 + body §5.3 の Open C と 3 路線統合 + meta §M6 C3-core の精密化 (commit 27f6009)。3 路線は「責務の再配分」ではなく Open C への並列攻略経路であり、最ローリスク路線 1 (橋梁公理) は局所固定 / 路線 2-3 は段階的閉鎖戦略
- 虚→実判定: 実化前進 ✓ — 「連続極限リフトは未閉」(粗い虚) → 「Open C: composition drift δ ↔ Čech 型 2-cocycle κ の連続側同定」(precise 虚) + Theorem A/B の閉鎖を露出
- 結果: 射程維持 ✓ — C3-core の射程は変わらず、虚な点が「単一の粗い未解決」から「閉じた部分 + 並列攻略経路を持つ残未解決」に分解された

### C3-core — 2026-04-27 Round 5 (ZFC Boolean 化の 3 軸発見と Dual citizenship 採用)
- 反論 r: 「OP-S05-3.2 (Paper IX α=1 経路) を /noe で『派生不能』と結論したが (信頼度 88%)、Tolmetes の信頼問いを契機に再走査すると、`Boolean 化』の意味を 2 軸 (値 vs 濃度) に二分したのは不完全。3 軸目 (Hom 集合の濃度を {0,1} indicator として読む経路) を見落としており、CD-3 確証バイアスの可能性。前ターン archived 提案は時期尚早」
- SFBT: できないのではなく、ZFC の発動条件における Boolean 化の意味を解釈未固定で進めていただけではないか?
- 試行: Definition Surface Protocol [SOURCE: ~/.claude/rules/dialogue-definition-surface.md] に従い、Boolean 化を 3 軸で再定義 — (i) Hom 集合の濃度 / (ii) Hom 集合内の射の値 / (iii) Hom 集合の存在 indicator。ZFC の解釈を 2 候補に分離 — 解釈 A (V-enriched [0,1] base): 反例 min合成圏が有効 / 解釈 B (Set existence indicator): Paper IX §3.5(ii) で派生可能。Tolmetes 判断で **A+B Dual citizenship** 採用
- 実化操作: meta §M6 C3-core 路線 1 を Dual citizenship 構造に再記述 + 三者対応辞書 §7.5 OT-S05-3 を A 文脈 / B 文脈の二重 ledger に分離 + Paper XIV body §5.3 路線 1 で射程明示。OP-S05-3.2 は archived ではなく **解釈 B での派生定理候補** として保持。ZFC は文脈依存の 2 重市民権を持つ
- 虚→実判定: 実化前進 ✓ — 信頼度 88% の暗黙 prior が「解釈 A 限定」だったことを露出。CD-3 自己告発で実質信頼度 60-70% に下方修正後、解釈固定で 2 解釈下の射程を明示化。OP-S05-3.2 を捨てずに保持
- 結果: 射程維持 ✓ — ZFC の射程は「古典圏論限定独立公理」から「文脈依存 (A 独立公理 / B 派生定理)」に拡張。前ターンの archived 提案を撤回し、Yugaku Refutation Gauntlet 規律 (Round 3 全敗後のみ後退許可) を遵守

### C3-core — 2026-04-27 Round 6 (Smithe Bayesian lens 経路の派生不能確定)
- 反論 r: 「OP-S05-3.4 Smithe Bayesian lens 合成経路は ICE 315 で 2 番目に高評価、しかも /noe が『自覚的盲点』と認めた経路。本気で叩けば派生可能の道筋が見えるのではないか? 4 段合成 (Φ=0 → posterior delta → Giry trivialize → Kleisli Set collapse → [0,1]→{0,1}) の各段は単独では数学的に valid なはず」
- SFBT: できないのではなく、(iii)→(iv) lift の構造的制約を見ていないだけではないか?
- 試行: /noe+ L3 で 7 phase 全実行 (P-0〜P-6)。R5 (Kleisli morphism collapse は base monoidal V を変えない、enriched category theory 標準事実) + R8 (Paper II §7.5 インデックス圏不一致 Poly vs (ℝ,≤)) の二重防御を P-2 結合分析で固定。Smithe ref 表記の TAINT エラー (前ターン「Smithe et al. 2023」) を S-0.5 で訂正 (正しくは Smithe 2021/2022 + Tull-Kleiner-Smithe 2024)
- 実化操作: SOURCE 追加 (Paper II §7.5 L1543-1545 + L790 + L1279 / kalon.md §6 L1044-1257 BRD-B8) + 三者対応辞書 §7.5 OT-S05-3.4 を Open → **Closed (派生不能)** に確定 + meta §M6 C3-core 路線 1 で派生候補 3 → 2 経路に縮約 + body §5.3 路線 1 で射程更新 (Smithe 経路 Closed 反映)。**Boolean 化 3 軸 ↔ 派生候補 ↔ 解釈の 3:3 対応構造**を Yoneda で確認: (i) 濃度↔3.1 Lawvere↔解釈 A / (ii) 値↔3.4 Smithe (Closed)↔解釈 A / (iii) indicator↔3.3 HoTT + 3.2 Paper IX↔解釈 A or B
- 虚→実判定: 実化前進 ✓ — 派生候補空間が 4 → 3 (Smithe Closed) に縮約。解釈 A の独立公理性が **強化** (派生候補が減ると独立公理として残る可能性が高まる)。Boolean 化 3 軸と派生候補の対応構造が露出
- 結果: 射程維持 ✓ — Yugaku「身の丈を理想に引き上げる」精神。Smithe 経路の派生候補を喪失したが、構造的事実として固定。前ターン /noe で「自覚的盲点」と認めた経路を本気で叩いた誠実な後退/前進

## §M6 虚→実変換面

### C1
- 野望: carry defect を忘却曲率 / 合成ドリフトの離散・有限体インスタンスとして固定し、Paper I と automath のあいだに橋ではなく series 内部の支持脚を立てる
- 現在まだ虚な点: `Man` 全体での厳密関手性と carryElement の連続幾何量への同定は未閉である。いま確定しているのは、離散側 Lean 証明、`Man_No11` 上の strictness、そして `Δ^n` を足場にした schema の三層までである
- 実へ引くための SOURCE: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XIV_曲率は忘却の繰り上がりである_草稿.md` §2.4, §4.4, §7.1、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/automath_bridge/automath_bridge.meta.md` §M2 C1, C1 Round 1-3
- 実化の判定条件: 本文が `theorem / schema / open` を混線させず、C1 を「離散インスタンス」として防衛できること。全域関手化と carryElement 幾何同定は open として見える位置に残ること
- 次の実化操作: §4.4 の語彙を `schema + Man_No11 制限` に揃え、carryElement の幾何学的実体は donor / open list 側へ隔離する
- 最新状態: 変換中

### C2
- 野望: OP-I-2 を「連続版は未証明」の一言で溶かさず、公理の穴・極限の穴・関手の穴へ分解し、何を埋めれば series の骨格が閉じるかを露出する
- 現在まだ虚な点: `ZeroForgetCollapse` の正当化、弱*連続測度族 `μ_λ`、`Discretizable` / `DescendsToCube` を通した全域拡張のいずれも未閉である。三穴の切り分けは済んだが、三穴自体は解けていない
- 実へ引くための SOURCE: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XIV_曲率は忘却の繰り上がりである_草稿.md` §5.1-§5.3、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/standalone/automath_bridge/automath_bridge.meta.md` §M2 C1/C4, C2 Round 1-3
- 実化の判定条件: 本文を読んだ第三者が、追加公理 debt / 極限 debt / 関手 debt を別々の仕事として追跡できること。「離散版が真だから連続版も真」という誤読が物理的にできないこと
- 次の実化操作: §5 と meta の三分割を同期し続け、`ZeroForgetCollapse` を橋梁公理、`μ_λ` を極限戦略、`Discretizable` / `DescendsToCube` を実装 debt として固定する
- 最新状態: 変換中

### C3
- 野望: 黄金比 φ が forgetting theory の外部装飾ではなく、理論内部の排他制約から必然的に出ることを示す
- 現在まだ虚な点: `φ` の出現が「離散 n-cell tower における seed 非依存の漸近主張」なのか、「tower 全体の具体列」なのかが混線すると、一撃で弱くなる
- 実へ引くための SOURCE: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文0_忘却の忘却_草稿.md` §2.2a、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文III_Markov圏の向こう側_草稿.md` §3.1(D)
- 実化の判定条件: recurrence と seed 非依存の漸近主張が本文内で分離され、seed が具体列にだけ必要であると明示される
- 次の実化操作: recurrence / asymptotic / concrete-sequence の三層分解を保持したまま、`ℤ₂→ℕ` の次数拡張へ進む
- 最新状態: 変換中

### C3-core
- 野望: Pauli 排他律から `A(n)=A(n-1)\sqcup A(n-2)` を導き、Cor. F2.2 として `growth rate = φ` を seed 非依存に押す
- 現在まだ虚な点: `ℤ₂→ℕ` の正準持ち上げは未閉。seed も concrete sequence の面では未確定。連続極限リフトは Open C: lax monoidal coherence の defect 2-cell 同定として再精密化済み。1-functor 部分と chain-map 部分は閉じた (Theorem A / B, body §4.4 同期済み)。残るのは合成ドリフト δ を Čech 型 2-cocycle κ として連続側で同定する 3 路線 (橋梁公理 / 弱*連続測度族 / Discretizable+DescendsToCube)。
- 実へ引くための SOURCE: `/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文0_忘却の忘却_草稿.md` §2.2a、`/home/makaron8426/Sync/oikos/01_ヘゲモニコン｜Hegemonikon/10_知性｜Nous/04_企画｜Boulēsis/12_遊学｜Yugaku/03_忘却論｜Oblivion/drafts/series/論文XIV_曲率は忘却の繰り上がりである_草稿.md` §7.3
- 実化の判定条件: recurrence が補題列で支えられ、`φ` の主張が concrete sequence から独立に防衛できる
- 次の実化操作:
  - 補題 F2.1c の内部構成と seed 決定を切り分け、先に `ℤ₂→ℕ` の bridge を閉じる
  - Open C の 3 路線のいずれかで部分的閉鎖を試みる。**路線 1 (`ZeroForgetCollapse`) は A+B Dual citizenship 構造で採用 (2026-04-27 第二次更新)**:
    - **解釈 A (V-enriched [0,1] base 文脈)**: ZFC は独立公理。反例 (min合成圏 [SOURCE: 三者対応辞書 L249-251]) は有効。派生候補は **2 経路** ((a) Lawvere Boolean topos / (c) HoTT) に縮約 (2026-04-27 第三次更新)。**(d) Smithe Bayesian lens 合成は Closed (派生不能) 確定** — /noe+ L3 で R5 (Kleisli morphism collapse は base monoidal V を変えない、enriched category theory 標準事実) + R8 (Paper II §7.5 インデックス圏不一致 Poly vs (ℝ,≤)) の二重防御で派生不能と確定。残 2 経路のいずれかが completion した時点で ZFC は派生定理に格下げ
    - **解釈 B (Set existence indicator 文脈)**: ZFC は **Paper IX §3.5(ii) からの派生定理候補**。Mor(C_α)(I,X) の存在/非存在を {0,1} indicator で読む経路。OP-S05-3.2 として ledger 化
    - 同一の ZFC が 2 解釈下で異なる地位を持つことを Yugaku Definition Surface Protocol で明示固定
  - 派生候補 4 経路は `三者対応辞書.md` §7.5 OP-S05-3.1〜3.4 として ledger 化
  - 路線 2 (`μ_λ` 弱*連続) と路線 3 (Strategy B) は automath repo との Lean 4 連携が必要
- 最新状態: 変換中 (2026-04-27 /noe + /ele Round 5 を経て Dual citizenship 採用)

## §M7 棄却された代替案

- 棄却 1: `OP-I-3` 単独で `δ=0 ⇒ Hom∈{0,1}` を押し切る。反例により不可能
- 棄却 2: `D* : Hyp → Man` を主経路に据える。現時点では補助的展望であり、主経路は弱*測度族 `μ_λ` と Strategy B
- 棄却 3: OP-I-2 を「連続版は未証明」の一言で曖昧化する。穴の位置が見えなくなり、実装者も読者も次の一手を決められない
- 棄却 4: Route B の Kalon 読みを C3 の一次証明に据える。Kalon は意味づけとしては強いが、φ の出現それ自体は導出しない
- 棄却 5: q=5 anomaly や Paper XII の速度接続を C3-core に先に混ぜる。面白いが、spine を閉じる仕事とは別である

---

## §M8 Donor 統合メモ (calculations 棚卸し)

以下は `calculations/` 配下の作業文書から Paper XIV に関連する donor の棚卸し結果である。いずれも本文 (body) への直接吸収は行わず、meta 参照として記録する。

### D1: automath 第一障害可視化閾値 (B-class)
- **donor**: `calculations/構想_automath_第一障害可視化閾値.md` (275 lines)
- **donor status**: 構想 (design/schema stage)。核心テーゼへの集合的確信は高いが個別要素は暫定的。反駁条件 4 件が明示。
- **内容**: q=5 が "第一障害可視化閾値" であるとする核心テーゼ。q=5 で (C_q, X_q) の座標交換 (11,−7)→(−7,11) が起きる (Prop.1)。e₂(A₅)=L₅=11 は family law ではなく q=5 限定の境界共鳴 (Prop.2: q≥6 で不成立)。3予想 H*1-H*3: H1/H2/H3 は単一障害の 3 射影。K_q=[κ_q] (障害クラス)、k_q=1_{K_q≠0} (可視化プロキシ)。BF 行列式: |det(I−A_q)|=F_{2q−2} (q≤4)、q=5 で超過 32−21=11=L₅。
- **本文との関係**: Paper XIV body (v0.1) は carry defect δ=Φ(x⊕y)−Φ(x)⊕Φ(y) を忘却曲率の離散版として展開。donor の q=5 閾値は body の carry defect 構造に transfer operator 側から数値的証拠を提供。body の Fibonacci 構造 (φ = n-cell tower 成長率) と donor の BF 行列式 Fibonacci 背景 F_{2q−2} が対応。
- **判定**: 構想段階。T1-T4 の theory tasks は未着手。Prop.2 が q≥6 で崩れること自体が q=5 の特殊性の証拠。body の carry defect δ との形式的接続は著者判断が必要。automath Lean 4 ソースへの具体参照あり (CollisionKernel.lean, CollisionZeta.lean)。

### D2: automath K_q 定義 (B-class)
- **donor**: `calculations/考察_automath_Kq定義_noe.md` (52 lines)
- **donor status**: 補助 (technical annex)。K_q の存在論的固定のみを責務とする。
- **内容**: K_q の 3 層分解: defect 2-cell (局所図式の不整合証拠) → defect 2-cocycle (計算可能な代表元) → obstruction class [κ_q] (coboundary 不変な第一障害クラス)。k_q:=1_{K_q≠0} は可視化プロキシ。K_q は「曲率量子化因子」ではなく「第一障害クラス」。
- **本文との関係**: Paper XIV の C1 (carry defect = 忘却曲率の離散インスタンス) と直結。donor の K_q 存在論は body の δ (carry defect) をどの抽象レベルで扱うかを精密化。cell/cocycle/class の混同防止。
- **判定**: 定義精密化の annex。hub (D1) 経由でのみ参照すべき。K_q の語義が揺れた時に開く。

### D3: automath Problem 10 reduction map (B-class) — Iteration 1+2 反映 (2026-04-24)
- **donor**: `calculations/考察_automath_Problem10_reduction_map.md` (75 lines) + `calculations/調査_Problem10a_integral_lift.md` (Codex Iteration 2)
- **donor status**: 補助 (technical annex) → **partial 解 + diagnostic 提示**。open checks 3 件のうち (a) integral lift Int_q 構成は 2 候補で attempted (Iteration 1: indicator scaling / Iteration 2: Walsh primitive)。(b) スペクトル自己双対性、(c) 圏論的意味は引き続き open。
- **内容**:
  - 元の構成: K_q:=[κ_q]:=ρ₂(Int_q([F_q])) の 3 段階。λ_q^evt (event quantum) vs λ_q^amp=F_m·λ_q^evt (amplitude refinement) の分離。
  - **Iteration 1 (Codex 2026-04-24, 398s)**: λ_q^evt:=|E_q| (BF excess の絶対値) を採用。Int_q∈{-1,0,+1} に collapse。q=4→0, q=5→1 (k_q 観測一致) だが indicator scaling と数学的に同型 (Tolmetes review R1)。Problem 10 が想定する rich ℤ-cohomology の中間 step を効果的に飛ばす (R2)。
  - **Iteration 2 (Codex 2026-04-24, 669s, R1/R2 feedback 後)**: 5 方針比較 (A min-period / D Fibonacci weight / E carry amp / F Walsh primitive / G rich vector)。D, E は整数性 fail で棄却。**方針 F (λ:=1, Walsh primitive lattice) を採用** — raw integer flux class E_q∈{0,11,55,278} を保持し、Iteration 1 の R1 を構造的解消。**方針 G (cell-dependent rich vector (E_q, C_q, X_q)) は別 annex `考察_automath_sector_parity_diagnostic.md` に分離** — H1/H2/H3 三投影の coefficient diagnostic として独立展開、`K_q` representative としては採用しない (class vs representative の規律維持)。
  - **q=4/5 観測整合**: 両 iteration とも Tolmetes hub の k_4=0, k_5=1 と一致。
  - **q≥6 新規情報**: Iteration 2 が初めて q≥6 の coefficient parity 候補を提示 (q=6 で `55 mod 2 = 1`、q=7 で `278 mod 2 = 0`、Walsh primitive convention)。Tolmetes hub には q≥6 の k_q 観測はなく、これらは AlyciaBHZ proxy 由来の novel observation として記録される。official `collisionKernel6/7` 待ち。
- **本文との関係**: Walsh-Stokes identity との構造対応に加え、**rich vector G は AlyciaBHZ の Sym²/Λ² 座標交換と直結する sector parity diagnostic** を提供する。詳細は別 annex (`考察_automath_sector_parity_diagnostic.md`) で展開。論文XIV body の carry defect δ との直接接続は引き続き donor D4 が担う。
- **判定**:
  - (a) integral lift: Walsh primitive `λ:=1` で raw integer flux class が保持できる。ただし「event quantum」概念は trivial (`λ=1`)。中間値 `0 < λ_q < |E_q|` で natural integer pattern を生む候補は未発見。
  - **(b) Phase 1 deep-dive 進展 (2026-04-24)**: `KilloFoldCollisionSpectralSelfDuality.lean` (lean4-codex-auto-dev branch) 発見により、AlyciaBHZ self-duality $\chi(t,\lambda)+\chi(t,-\lambda)=4(1-\lambda^4)$ は q=4 で Lean 形式化済 [SOURCE: lean4/Omega/Folding/KilloFoldCollisionSpectralSelfDuality.lean L9 ref=lean4-codex-auto-dev]。代数的偶奇分離 $\chi_{A_4(t)}(x)=(-2x^4+2)+(x^5-tx^3-2x)$ も `paper_killo_fold_collision_metric_tensor_separation` で証明済 [SOURCE: lean4/Omega/Folding/KilloFoldCollisionMetricTensorSeparation.lean L8 ref=lean4-codex-auto-dev]。representative の偶/奇分離は q=4 では **代数的に** Lean で保証 (Fisher/Amari-Chentsov 対応は Issue #25 コメント由来の情報幾何学的解釈)。新規 corollary `paper_killo_fold_collision_self_dual_zeros` (self-dual root ⟺ $\lambda_0^4=1$、整数量化のため整数上は $\{1,-1\}$ のみ) も発見。残存は q≥5 への拡張。
  - (c) は引き続き未着手。
  - Lean 形式化は skeleton (sorry 3) で `lake env lean` pass。実体は `/tmp/p10a_lean/IntegralLift.lean`。
  - **q=7 偶数 parity (`278 mod 2 = 0`)** は novel observation。hub の `q*=5` 境界読みと整合 (q=5 boundary resonance / q=7 sector parity reset の 2 段構造を示唆する可能性)。詳細: `考察_automath_sector_parity_diagnostic.md` §O3。

### D4: q5 符号反転 Z₂ 接続 (B-class)
- **donor**: `calculations/調査_automath_q5符号反転とPaperIII_Z2接続.md` (348 lines)
- **donor status**: 正本 / SOURCE + interpretation (source ledger)。automath Lean 4 facts と Paper III 接続の第一解釈を保持。
- **内容**: §1 SOURCE レジャー: carry defect κ(x,y) が H²(G_m; Z/2Z) の非自明 2-cocycle [SOURCE]、BF 行列式 Fibonacci パターン (q≤4) と q=5 での break [SOURCE]、trace 符号反転 tr(A_q)=+2→−2 [SOURCE]。§3 局所数値検査: 固有値構成変化 (q=5 で複素共役ペア支配)、trace power 振動、e₂(A₅)=tr(Λ²A₅)=11 は anti-copy セクター trace [SOURCE]、graded supertrace 反転 +18→−18。§4 最短接続仮説 H1: 2-body lifted phase reversal (copy→anti-copy 座標交換)、H2: L₅=11 は odd pair sector correction。§6 Negativa: "q odd ⟹ odd sector" 棄却、"trace flip alone sufficient" 棄却、"α<0 proven in Lean" 棄却。
- **本文との関係**: Paper XIV body の carry defect δ と donor の数値的 q=5 anomaly は同じ現象を離散代数側 (body) と transfer operator 側 (donor) から捉えている。Paper III Z₂-graded copy/anti-copy 構造との接続は Paper XIV の scope 外だが、q=5 数値事実は Paper XIV の carry defect 解析に直結。
- **判定**: 数値的事実の source ledger として最も信頼度が高い donor (Lean 4 facts は機械検証済み)。Paper III 接続は cross-paper reference。q=6,7 probe が未完、graded lift 定義が未着手。著者判断待ち: (1) body の carry defect と donor の e₂ 接続を明示するか、(2) Paper III bridge は別 paper で扱うか。
- **判定追記 (2026-04-24, SF 調査結果反映)**:
  - **donor status update**: 「source ledger」から「source ledger + SF-refined structural interpretation」へ拡張。SF 調査 (`calculations/調査_sf_sign_flip_由来.md`) により [SOURCE] q=5 全符号反転の事実と `momentSum_five_recurrence_verified` 不在が確定 (97%)。[TAINT: inference, confidence 75%] 由来を **Lucas-aligned dual companion の意図的選択** として読む H-LUCAS 仮説が提示された (author 意図の直接確認は未実施) [SOURCE: 調査_sf_sign_flip_由来.md §3, commit `ce497566` exists]。
  - **内容追記**: [TAINT: inference] D4 donor の §3.4 graded second lift supertrace 反転 (+18 → −18 at q=4→5) は、Lean `collisionKernel5` の Lucas-aligned dual character と構造的に一致する方向を向く。両者を同一 phenomenon (copy/anti-copy 座標交換) の双対記述として読む可能性がある。
  - **著者判断待ち (3) 新設**: D4 を **Lucas-aligned dual companion の構造的 donor** として読み、論文XIV body の carry defect δ 解析に「Lucas-invariant framework での representative choice」の議論を追加するか。ただし棄却 5 (§M7) との整合を保つ (spine C1/C3 と q=5 anomaly を混ぜない方針)。最短の運用は、D4 を **supporting evidence** として保持しつつ、本文には取り込まないまま置く案。
  - **blocker 更新**: Problem 10(a) `Int_q` の構成は別 iteration で Walsh primitive λ:=1 として解けた (D3 iteration 2)。残存 blocker は [TAINT: inference] 「**Lucas-aligned dual の 2 representative を K_q class で統合する theoretical framework**」。これは hub §T2 の更新内容と連動する。
  - **staging 参照**: `calculations/提案_sf_lucas_aligned_反映drafts.md` §3.4 / `calculations/調査_sf_sign_flip_由来.md`
