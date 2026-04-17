# 論文XIV_曲率は忘却の繰り上がりである — メタデータ

## §M1 F⊣G 宣言 (固定日: 2026-04-14)

- F (発散関手) = automath / Omega / 忘却論の三者対応を、離散 defect・連続曲率・圏論的忘却の三面へ展開する操作。文体ガイド §3 のメタファー三連と、分野越境 (symbolic dynamics ↔ information geometry ↔ category theory) を含む
- G (収束関手) = 上記の展開を、原典参照・反例・機械検証・Lean 型シグネチャへ蒸留する操作。文体ガイド §4 の数式裏付け + dictionary 正本 + NotebookLM/ローカル SOURCE 照合
- 固定日: 2026-04-14

## §M2 核主張リスト (L3 対象)

- C1: automath の carry defect は、忘却論の合成ドリフト / 忘却曲率の離散・有限体インスタンスである
- C2: OP-I-2 は単一の未証明問題ではなく、`ZeroForgetCollapse` を要する公理の穴、弱*連続測度族 `μ_λ` を要する極限の穴、`Discretizable` / `DescendsToCube` を要する関手の穴に分かれる
- C3: 黄金比 φ は外部からの輸入ではなく、排他制約と n-cell tower の成長率として忘却論の内部に現れる
  - **C3-core (Route D)**: 排他性 + grade 分離により `A(n)=A(n-1)\sqcup A(n-2)` が閉じ、growth rate が φ になる
  - **Route A**: C3-core の離散証人。反 Markov セクターと no-consecutive-1s 制約が同じ排他則を示す
  - **Route C**: C3-core の entropic corollary。排他制約の下で容量上限が `log φ` に落ちる
  - **Route B**: C3-core で得られた φ を `Fix(G∘F)` と読む Kalon 解釈。一次証明ではなく解釈層
  - **残る proof debt**: `ℤ₂→ℕ` の次数拡張 / seed `|A(1)|, |A(1.5)|` の確定 / 連続極限リフト。Lean は verification layer であって本体ではない

## §M3 Kalon 判定履歴

| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| 2026-04-14 | C2 | ◯ Kalon△ | `δ=0 ⇒ Hom∈{0,1}` を無条件主張から切り離し、橋梁公理・弱*リフト・全域関手化の三穴へ分解。射程を縮めずに論理を精密化 |
| 2026-04-17 | C3 | ◯ Kalon△ | Route D を theorem spine、A/C/B を支線へ再配置。射程は維持されたが、`ℤ₂→ℕ`、seed、連続極限リフトが残る |

## §M4 ±3σ ゲート履歴

| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| 2026-04-14 | C2 | ±3σ | ±3σ | 維持 — 「連続版は未証明」を超えて「どこが穴か」を三分割し、μ への後退を回避 |
| 2026-04-17 | C3 | +4σ | +4σ | 維持 — 四並列のエッセイ束を一本の theorem spine へ整理しつつ、μ へ後退しなかった |

## §M5 Refutation Gauntlet ログ

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
- 前提強化: Route D を **C3-core / theorem spine** に固定し、Route A を離散証人、Route C を entropic corollary、Route B を Kalon 読みへ後退させる
- 結果: 射程維持 ✓ — 新しい第五経路を足さずに、既存四経路の地位を整理するだけで論証剛性が上がった

### C3 — 2026-04-17 Round 2
- 反論 r: それでも C3-core は Paper 0 の言い換えにすぎず、未解決が散らばったままではないか
- SFBT: 別角度からではなく、残差を減らす形で前に進めるとしたら?
- 前提強化: proof debt を三件へ限定する。`ℤ₂→ℕ` の次数拡張、seed `|A(1)|, |A(1.5)|` の確定、連続極限リフト。Lean は proof debt の代用品でなく verification layer と明記
- 結果: 射程維持 ✓ — C3 は「路線が多い」状態から「主線が見え、残差も数えられる」状態へ移行

## §M6 棄却された代替案

- 棄却 1: `OP-I-3` 単独で `δ=0 ⇒ Hom∈{0,1}` を押し切る。反例により不可能
- 棄却 2: `D* : Hyp → Man` を主経路に据える。現時点では補助的展望であり、主経路は弱*測度族 `μ_λ` と Strategy B
- 棄却 3: OP-I-2 を「連続版は未証明」の一言で曖昧化する。穴の位置が見えなくなり、実装者も読者も次の一手を決められない
- 棄却 4: Route B の Kalon 読みを C3 の一次証明に据える。Kalon は意味づけとしては強いが、φ の出現それ自体は導出しない
- 棄却 5: q=5 anomaly や Paper XII の速度接続を C3-core に先に混ぜる。面白いが、spine を閉じる仕事とは別である

---

## §M7 Donor 統合メモ (calculations 棚卸し)

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

### D3: automath Problem 10 reduction map (B-class)
- **donor**: `calculations/考察_automath_Problem10_reduction_map.md` (75 lines)
- **donor status**: 補助 (technical annex)。open checks 3 件 (量子化条件、代表元一致、q=5 first visibility)。
- **内容**: K_q:=[κ_q]:=ρ₂(Int_q([F_q])) の 3 段階構成: (1) cubical 積分 I_q(F_q)(□):=∫_□ F_q、(2) 整数リフト Int_q:=(1/λ_q)∫_□ F_q、(3) Z/2Z 係数還元 ρ₂。量子化スキーマ: λ_q^evt (単一 carry event quantum)、λ_q^amp:=F_m·λ_q^evt (amplitude refinement)。sign-holonomy は暫定代替。
- **本文との関係**: Paper XIV の Walsh-Stokes identity (離散 Leibniz 則) と cubical 積分は構造的に対応。body の OP-I-2 (support chain: discrete → continuous lift) と donor の integral lift が同じ数学的問題を別角度から攻めている。
- **判定**: open checks 3 件が未解決。integral lift が立たない場合の暫定 surrogate (sign-holonomy) は「本丸ではない」と donor 自身が宣言。body 安定後に再評価。著者判断待ち。

### D4: q5 符号反転 Z₂ 接続 (B-class)
- **donor**: `calculations/調査_automath_q5符号反転とPaperIII_Z2接続.md` (348 lines)
- **donor status**: 正本 / SOURCE + interpretation (source ledger)。automath Lean 4 facts と Paper III 接続の第一解釈を保持。
- **内容**: §1 SOURCE レジャー: carry defect κ(x,y) が H²(G_m; Z/2Z) の非自明 2-cocycle [SOURCE]、BF 行列式 Fibonacci パターン (q≤4) と q=5 での break [SOURCE]、trace 符号反転 tr(A_q)=+2→−2 [SOURCE]。§3 局所数値検査: 固有値構成変化 (q=5 で複素共役ペア支配)、trace power 振動、e₂(A₅)=tr(Λ²A₅)=11 は anti-copy セクター trace [SOURCE]、graded supertrace 反転 +18→−18。§4 最短接続仮説 H1: 2-body lifted phase reversal (copy→anti-copy 座標交換)、H2: L₅=11 は odd pair sector correction。§6 Negativa: "q odd ⟹ odd sector" 棄却、"trace flip alone sufficient" 棄却、"α<0 proven in Lean" 棄却。
- **本文との関係**: Paper XIV body の carry defect δ と donor の数値的 q=5 anomaly は同じ現象を離散代数側 (body) と transfer operator 側 (donor) から捉えている。Paper III Z₂-graded copy/anti-copy 構造との接続は Paper XIV の scope 外だが、q=5 数値事実は Paper XIV の carry defect 解析に直結。
- **判定**: 数値的事実の source ledger として最も信頼度が高い donor (Lean 4 facts は機械検証済み)。Paper III 接続は cross-paper reference。q=6,7 probe が未完、graded lift 定義が未着手。著者判断待ち: (1) body の carry defect と donor の e₂ 接続を明示するか、(2) Paper III bridge は別 paper で扱うか。
