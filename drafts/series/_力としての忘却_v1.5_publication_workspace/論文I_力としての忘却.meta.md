# 論文 I — 力としての忘却 `.meta.md`

> 本ファイルは calculations 棚卸しにより新規作成された meta ファイルである。
> §M1–§M7 は body (v1.5) から後付けで整備した骨格版である。
> ※ 2026-04-17 整合修正: body current は v1.5 (2026-04-11) を正本とし、本文末尾 colophon もこれに同期した。モノグラフ構成設計・統一記号表などのインフラ参照も v1.5 を current として扱う。
> body が安定した時点で著者が精査・拡充すること。

---

## §M1 F⊣G 宣言 (固定日: 2026-04-16)

- **F (発散関手)** = 「力は忘却から生まれる」という Type α の同一性主張を核に、統計多様体の局所幾何 (Φ, A_i, F_{ij}) から方向性定理 (Thm 5.1) → 指数型 class の $dT=0$ 簡約 → 非指数型境界と OP-I-7 → α-遷移層力 / FEP / SAM / CKA / 圏論ゼロ曲率極限の出口へと展開する操作。文体ガイドの §3 メタファー三連 (「力はどこから来るのか」) と §10 Type α 同一性主張を採用。
- **G (収束関手)** = 定理 5.1 (必要十分条件の双方向証明)、指数型分布族での $dT=0$、非指数型境界の明示、命題 6.6.1 (F_{ij} の $\alpha_I$-線形性が近似ではなく正確であることの証明) へ収束させる。FEP / SAM / CKA / 圏論ゼロ曲率極限は主結果ではなく、主定理から出る proposal / outlook / donor として分離する。
- **主要随伴**: index_op ⊣ Search (Hyphē §5.7 文脈) が Paper I の主要な F⊣G インスタンス。dF = 0 条件と G∘F の蒸留方向選択性を通じて方向性定理と接続。
- **固定日**: 2026-04-16 (body v1.5 後付け整備)

---

## §M2 核主張リスト (L3 対象)

- **C1**: 方向性定理 (Thm 5.1): 統計多様体上の忘却場 Φ に対し、忘却曲率 F_{ij} = (α/2)[d(ΦT)]_{ij} ≠ 0 であることと、忘却で重み付けされた Chebyshev 1-形式 ΦT が閉でないことは同値である。一般形では $d(\Phi T)=d\Phi\wedge T+\Phi\,dT$ であり、指数型分布族では $dT=0$ により条件は $d\Phi\wedge T\neq 0$ に簡約される (系 5.1.1)。[確信]
- **C2**: 指数型 class / 非指数型境界: ガウス族とカテゴリカルシンプレックスでは $dT=0$ が成立し、Student t 位置スケール族では $dT\neq 0$ が立つ。Cauchy 位置スケール族の鈍さにより「非指数型なら常に $dT\neq 0$」は採れないため、$dT=0$ の保持 / 破れの分類を OP-I-7 として開く。[推定]
- **C3**: 忘却曲率の $\alpha_I$-線形性 (命題 6.6.1): F_{ij} は Paper I の結合パラメータ $\alpha_I$ に対して正確に線形であり、この線形性は近似ではなく構造的に正確である。[確信]
- **C4**: 出口群の隔離: 精度-FEP 構造的同型 (§6.5)、α-遷移層力 (§6.3)、α-SAM / Oblivion-Aware SAM (§6.7-§6.8)、CKA-KL bridge、圏論のゼロ曲率極限 (§9.5) は、主結果ではなく proposal / outlook / donor / future theorem seed として温存する。α 関連の出口では、Paper I の結合パラメータを $\alpha_I$、Amari 接続パラメータを $\alpha_{III}$ と分離し、両者の橋は proposal として扱う。[運用方針]

---

## §M3 Kalon 判定履歴

| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| v1.5 時点 | C1 (方向性定理) | ◯ Kalon | $F_{ij}=0$ の必要十分条件が $d(\Phi T)=0$ (ΦT の閉性) という幾何学的条件に収束する。指数型 class では $dT=0$ により方向的不整合へ簡約され、ガウス族 Toy Model での等方/異方の鋭い二分法 (F_{12}=0 vs F_{12}=6μ/σ) が定理を具体化。 |
| v1.5 時点 | C2 (class 境界 / OP-I-7) | ◯ Kalon△ | 指数型では $dT=0$、Student t では $dT\neq 0$、Cauchy では非指数型でも鈍いという三点により、単純な二分ではなく class 分類問題として立つ。 |
| 2026-04-28 | C2 (class 境界 / OP-I-7) | ◯ Kalon△ (根拠強化) | [SOURCE: Nielsen 2020 PMC7517249 / Mitchell 1988] により Cauchy $T_{ijk}=0$ exact が確定 (機構: moment-cancellation)。Student-t の $q=(\nu+3)/(\nu+1)$ q-Gaussian 同定と $\alpha=\pm(\nu+5)/(\nu-1)$-dual flat 性質が追加。E0/N1/N0 の三 class が $dT$ 可積分性を軸に統一的に配置できる。N1→N0 極限の連続性確認と open search band 追加が次の昇格条件。 |
| v1.5 時点 | 旧C4 (忘却-抽象化定理; outlet) | ◯ Kalon△ | image(G) ∋ 高接続構造 / ker(G) ∌ 普遍構造 という対称性。ただし定量的層 (α ↑ → dim(image(G)) ↓ の単調性) は定理 5.9.3 単独からは従わず閾値の単調性が必要 — この追加要件が未整備 (未証明)。現行 Paper I の主砲からは外し、出口群に保持。 |
| v1.5 時点 | SWE-bench null result | ◯ Kalon | 忘却を操作しない系で r(Ξ_CV, P) = -0.007 (p=0.87) という null result が得られた。これは方向性定理の対偶の実証ではなく**境界条件の成功確認** — 忘却なしでは Ξ_theory ≈ 0 が予測され、それが実際に観測された。理論が「外れなかった」ことを示す。 |

---

## §M4 ±3σ ゲート履歴

| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| v1.5 時点 | C1 (方向性定理) | +3σ | +3σ | 一般形では $F=0 \iff d(\Phi T)=0$ を必要十分条件として双方向証明。指数型 class では $dT=0$ により $d\Phi\wedge T=0$ へ簡約する。一方向だけの証明には後退しなかった。 |
| v1.5 時点 | C3 ($\alpha_I$-線形性) | +3σ | +3σ | F_{ij} が $\alpha_I$ に「ほぼ線形」ではなく「正確に線形」であることを命題 6.6.1 で確立。「近似として有効」という弱い主張への後退を回避。 |
| v1.5 時点 | C4 出口群 (FEP 同型) | ±3σ | ±3σ | 「線形化レベルでの構造的同型」に射程を限定。FEP との完全対応 (全変数) には主張せず。この制限が射程の正直さを担保している。現行 Paper I の主結果ではなく proposal / outlook 側に保持。 |

---

## §M5 Refutation Gauntlet ログ

### C1 — v1.5 以前 Round 1 (Chebyshev 結合の一意性)
- **反論 r**: 「A_i = ∂_iΦ + (α/2)Φ T_i という結合形式は恣意的ではないか。Γ^(α)_i を使う方が自然では」
- **SFBT**: 「T_i ではなく Γ^(α)_i を使えるとしたら?」
- **前提強化**: §2.2 で Γ^(α)_i が真の 1-形式でないことを確認 (座標変換で非同次項 ∂log|J|)。命題 2.2 で T_i = Γ^(α)_i - Γ^(0)_i のテンソル的内容であることを示した。結合の選択は一意。
- **結果**: 射程維持 ✓ — T_i 結合は最小結合の「自然な候補」から必然的に帰結する

### C1 — v1.5 Round 2 (Yang-Mills との混同)
- **反論 r**: 「F_{ij} を曲率テンソルと呼ぶなら Yang-Mills ゲージ理論と同一構造ではないか」
- **SFBT**: 「どこが異なるかを明示できるか」
- **前提強化**: §6.3 で明示: α-遷移層力は Yang-Mills ゲージ理論には類似物を持たない。Paper I は非最小結合スカラー場理論であり、ゲージ不変性もゲージ自由度も存在しない。
- **結果**: 射程維持 ✓ — Yang-Mills との混同を先回りして排除

### C2 — 2026-04-28 Round 1 (OP-I-7 外部 Sourcing: Mitchell 1988 / Nielsen 2020)
- **反論 r**: 「Cauchy の T≈0 は数値的偶然であり、鈍さの由来が対称性・パラメータ化・数値条件のどれにあるか未分離」(§M10 昇格条件より)
- **SFBT 問い**: 「Mitchell 1988 の原典が楕円分布族全体での T_{ijk}=0 を直接証明しているとしたら?」
- **前提強化**: [SOURCE: Nielsen (2020) PMC7517249] が Mitchell (1988) を引用して "the cubic skewness tensor T vanishes everywhere, T_{ijk}=0" を確認。機構: Cauchy スコア関数の奇数次積の対称性消去 + 偶数次交差項 $(T_{\mu\mu\sigma}$ 等) の Cauchy カーネル $(1+u^2)^{-1}$ に固有の代数的消去 (Mitchell 1988 直接計算)。T≈0 の「≈」を T_{ijk}=0 (exact) に昇格。
- **実化操作**: OP-I-7 Cauchy 注記 (L270) に Mitchell 1988 + Nielsen 2020 引用を追加; N0 行の "T≈0, dT≈0" → "T_{ijk}=0 (exact), dT=0" に修正; Cauchy の昇格条件を「鈍さの由来分離」→「同種相殺を持つ他族への汎化条件の同定」へ精密化。
- **虚→実判定**: 実化前進 ✓ (C_{abc}≡0 の機構 = moment-cancellation が SOURCE 確定)
- **結果**: 射程維持 ✓ — N0 の鈍さが「数値的偶然ではなく構造的」に昇格。残る問題は汎化条件の同定 (§M10 継続)

### C2 — 2026-04-28 Round 2 (Student-t の deformed exponential family 文脈)
- **反論 r**: 「Student t を "non-exponential" と呼ぶのは正確か? Tsallis q-Gaussian 族に属するという幾何学的文脈が欠落している」(GPT prior research report の genuine gap 指摘より)
- **SFBT 問い**: 「Matsuzoe-Henmi 2014 の deformed exponential family conformal Hessian 構造と、Student-t の α-dual flat 性質 (Mitchell 1988) を接続できるとしたら?」
- **前提強化**: [SOURCE: Nielsen (2020) PMC7517249] Student-t S_k は Fisher 計量で α=±(k+5)/(k-1) で dual flat (Mitchell 1988)。これは deformed exp family の conformal Hessian 構造に対応。q=(ν+3)/(ν+1) で Tsallis q-Gaussian として Student-t を同定 (ν=1 → q=2 = Cauchy, ν→∞ → q→1 = Gaussian)。Cauchy (ν=1, q=2) では α→∞ → dual flat 構造崩壊 → T_{ijk}=0。これが N1→N0 遷移の幾何学的正体。
- **実化操作**: OP-I-7 table の N1 class 名を "deformed exponential / twist-positive" に改名; q-Gaussian 同定と α-dual flat 構造を幾何学的構造列に追記; N0 class 名を "twist-dull / elliptic-degenerate" に更新。
- **虚→実判定**: 実化前進 ✓ (E0/N1/N0 を q パラメータ軸で統一的に配置する幾何学的文脈が確立)
- **結果**: 射程維持 ✓ — ただし Matsuzoe 2014 の具体定理内容は paywalled で [TAINT] 止まり。Mitchell 1988 / Nielsen 2020 が直接 SOURCE として機能。

### C2 — 2026-04-28 Round 3 非発動
- **理由**: Round 2 で射程維持 ✓ かつ実化前進 ✓ 達成 — E0/N1/N0 三 class の q-Gaussian 文脈整備と Cauchy moment-cancellation 確定が同時に達成されたため
- **Solution-Focus 適用仮説**: もし発動していれば「open search band を q>2 Gaussian と混合族の交差として位置づけ、dT=0 保持条件を q パラメータの連続関数として追跡する」戦略を検討した
- **虚→実判定**: 実化前進 ✓

### 旧C4 — v1.5 Round 1 (定量的層の未確立)
- **反論 r**: 「定理 5.9.3 は定性的 (普遍構造は ker(G) に属せない) だけで、定量的な α ↑ → dim(image(G)) ↓ は証明されていないのでは」
- **SFBT**: 「定量的層を証明したとしたら、何が必要か」
- **前提強化**: §5.9.3 本文で「定量的層は定理 5.9.3 単独からは従わず、閾値の単調性を必要とする」と明記。定性的層と定量的層を分離して主張した。
- **結果**: 射程維持 ✓ — 定性的確信と定量的未確立を区別して記録

---

## §M6 虚→実変換面

### C1 (方向性定理 Thm 5.1)
- **野望**: 力の発生条件は、忘却で重み付けされた Chebyshev 1-形式 $\Phi T$ の閉性破れ $d(\Phi T) \neq 0$ として完全に特徴づけられる。
- **現在まだ虚な点**:
  - (i) 一般非指数型統計多様体上での $dT = 0$ 保持/破れの完全分類は未完 (OP-I-7)。Student t / Cauchy 以外の class はまだ計算されていない。
  - (ii) 定理は数学的に閉じているが、Toy Model (Gaussian, カテゴリカルシンプレックス) を超える経験的実装での $F_{ij} \neq 0$ の直接観測は未取得。E12 (30 sessions, 6053 steps) は ker(G) / image(G) 因果は観測したが、$F_{ij}$ それ自体の量的観測は未実施。
  - (iii) FEP との対応は本稿では「線形化レベルでの構造的類似」に射程限定。線形化を超えた完全埋め込みは未確立 (§6.5)。
- **実へ引くための SOURCE**:
  - Amari & Nagaoka "Methods of Information Geometry" Ch.2-3 (Amari-Chentsov tensor の非指数型計算)
  - Eguchi 1983 (statistical manifold dual structures)
  - 本稿 §11 数値再現コードと Appendix B/F の toy model 計算
  - Friston (2010) の generative model formalization (FEP 接続再評価用)
- **実化の判定条件**:
  - (a) OP-I-7 で開いた Student t / Cauchy 以外の少なくとも 3 つの非指数型 class について $dT$ の振る舞いが分類される
  - (b) Toy model 以外の少なくとも 1 領域 (Transformer 層 / RAG / SAM 訓練軌跡) で $F_{ij}$ の予測が経験的に確認される
  - (c) FEP との対応について線形化を超える接続条件 (Conjecture vs Theorem) が明確化される
- **次の実化操作**:
  - (1) §11 reproducibility 検証スクリプトの公開と独立実装による再現
  - (2) E12 拡張版で $F_{ij}$ の経験的観測を実施 (Hyphē 別稿)
  - (3) OP-I-7 の class 拡張 (Mixture / GP / VAE families) を計算短稿として Hyphē に登録
  - (4) 後続論文 (Paper II 候補) 準備過程で FEP との完全対応 Conjecture を明示化
- **最新状態**: 変換中 (主結果は確立、射程一般化と経験的接続は途上)

### C2 (class 境界 / OP-I-7)
- **野望**: 「非指数型統計多様体は常に $dT \neq 0$ という一般命題は成立しない — Chebyshev 1-形式の閉性は分布族の代数的構造 (moment-cancellation) により保持されうる」という主張を、E0/N1/N0 の三 class 構造として $dT$ の可積分性という単一不変量で完全に形式化する。
- **現在まだ虚な点**:
  - (i) N1→N0 の極限: $\nu\to1$ ($q\to2$) での $dT\to0$ 収束が連続的であるかの数値追試未完 ($\nu\in\{1.5, 2, 3, 5\}$ での $|dT|$ 追跡が未実施)。
  - (ii) Matsuzoe-Henmi 2014 の具体定理内容: deformed exponential family の "two kinds of dualistic Hessian structures and conformal structures" が $dT=0$ の保持を含意するかは [TAINT] 止まり (paywalled)。
  - (iii) open search band の具体的候補 ($q$-Gaussian $q>2$、混合族、楕円形重尾) の $dT$ 計算が未着手。
  - (iv) "twist-dull" が Class N0 に固有か、より広い族 (一般楕円分布) で成立するかは Mitchell 1988 の圏では言及済みだが、Paper I の文脈で formal theorem として昇格していない。
- **実へ引くための SOURCE**:
  - Mitchell 1988 "Statistical manifolds of univariate elliptic distributions" Int. Stat. Rev. 56:1-16 (直接読み未了; Nielsen 2020 経由で T_{ijk}=0 exact を間接確認)
  - [SOURCE: Nielsen 2020 PMC7517249] (直接取得済み; Mitchell 1988 引用箇所を確認)
  - Matsuzoe-Henmi 2014 Springer ch. (paywalled、[TAINT])
  - Amari-Ohara-Matsuzoe 2012, Physica A 391:4308-4319 (preprint 未確認)
- **実化の判定条件**:
  - (a) $\nu\in\{1.5, 2, 3, 5\}$ での数値で $|dT|$ の $\nu\to1$ 単調収束が確認される
  - (b) E0/N1/N0 の三 class が $dT$ の可積分性 (閉性) という単一不変量で形式的に定義され、各 class の代表族について証明が揃う
  - (c) open search band に 1 つ以上の新 class または反例が追加される
- **次の実化操作**:
  - (1) $\nu\in\{1.5, 2, 3, 5\}$ での $|dT|$ 数値追試 (Lethe 側)
  - (2) Amari-Ohara-Matsuzoe 2012 preprint の web 探索 (Layer 1α)
  - (3) Mitchell 1988 原典の直接取得試み (JSTOR doi:10.2307/1403358)
  - (4) §5.4 working classification の「昇格に必要な操作」列への (a)(b)(c) 追記
- **最新状態**: 変換中 (Cauchy N0 の moment-cancellation が [SOURCE: Nielsen 2020 / Mitchell 1988] で確定。N1→N0 極限の連続性と open search band が残る虚)

### C3
- 野望: [§M2 C3 の核主張を 1 文で言い直す]
- 現在まだ虚な点: [未証明・未観測・未形式化・未反駁処理の核]
- 実へ引くための SOURCE: [読むべき原典 / 必要データ / 必要定理]
- 実化の判定条件: [何が揃えば『実へ近づいた』と言えるか]
- 次の実化操作: [Sourcing / 定義追加 / 証明 / 実験 / 反論吸収]
- 最新状態: 変換中

### C4
- 野望: [§M2 C4 の核主張を 1 文で言い直す]
- 現在まだ虚な点: [未証明・未観測・未形式化・未反駁処理の核]
- 実へ引くための SOURCE: [読むべき原典 / 必要データ / 必要定理]
- 実化の判定条件: [何が揃えば『実へ近づいた』と言えるか]
- 次の実化操作: [Sourcing / 定義追加 / 証明 / 実験 / 反論吸収]
- 最新状態: 変換中

## §M7 棄却された代替案

- **棄却 1**: 「A_i に Γ^(α)_i を直接使う (最小結合の素朴版)」。Γ^(α)_i が真の 1-形式でないことにより不可 (§2.2)。T_i 結合が一意の正規化。
- **棄却 2**: 「Φ を忘却の量 (絶対値) として解釈する」。§3.1 リマークで明示的に棄却。Φ は忘却ポテンシャル (まだ忘却されずに残っている構造量) であり、絶対値の解釈では方向性定理 (∇Φ 依存) が無意味になる。
- **棄却 3**: 「ゲージ理論として定式化する (A_i → A_i + ∂_iχ)」。本理論は A_i が Φ と背景幾何から完全に決まる非最小結合スカラー場理論。ゲージ自由度は存在しない。Yang-Mills との類似は記号レベルのみ (§6.3 注記)。
- **棄却 4**: 「作用の形式は S[Φ] = ∫ ΦF_{ij}F^{ij} (一次結合) が自然」。命題 3.4.1 (作用の一意性) により、微分同相不変 + F_{ij} の2次 + 最低階微分の3条件から (1/4)F_{ij}F^{ij} + (λ/2)Φ² が一意に確定。
- **棄却 5**: 「Cauchy 位置スケール族を反例として dT ≠ 0 の非指数型を例示する」。数値 pilot で $T \approx 0$, $dT \approx 0$ を返し、閉形式計算でも $C_{abc}\equiv0$ と確定。[SOURCE: Nielsen 2020 PMC7517249 / Mitchell 1988] により $T_{ijk}=0$ (exact) が独立確認済み — 数値的 $\approx0$ が代数的 $=0$ に昇格。機構は Cauchy スコア関数のモーメント相殺 (奇数次積の対称性消去 + Cauchy カーネル $(1+u^2)^{-1}$ に固有の偶数次交差項消去; Mitchell 1988 直接計算)。反例としては機能しなかったが、「非指数型 $\Rightarrow$ $dT \neq 0$」という一般命題が成立しないことの exact witness として OP-I-7 N0 class に記録。
- **棄却 6**: 「$\alpha_I$ と $\alpha_{III}$ を添字なしの α として横断同一視する」。統一記号表 §1.1/§1.12 により、Paper I の忘却場結合パラメータ $\alpha_I$ と Amari 接続パラメータ $\alpha_{III}$ は現時点では独立添字で読む。§6 の α-field / FEP / SAM は両者を橋渡しする proposal であり、方向性定理の前提ではない。

---

## §M8 Donor 統合メモ (calculations 棚卸し)

以下は `calculations/` 配下の作業文書から Paper I に関連する donor の棚卸し結果である。本文 (body) への直接吸収は行わず、meta 参照として記録する。

### D1: CKA–KL ブリッジ (B-class)
- **donor**: `calculations/CKA_KLブリッジ.md` (540 lines)
- **donor status**: 理論ノート (theory note)。確信度: Gaussian 仮定 [推定 75%→確信 95%]、同時対角化 [推定 80%→確信 95%]、非線形 kernel CKA [仮説 60%→推定 85%]
- **内容**: CKA (形状) と KL (形状＋スケール) の分離定理 (Th.3.1)、CKA 方向性定理 (Th.5.1: 条件 A–C 下で body Th.5.1 の CKA 拡張)、情報幾何学的ピタゴラス定理 (Th.8.1)、非ガウス方向保存 (Th.8.2: 条件 D = negentropy slow change)、RKHS リフト原理 (Prop.11.1)。次元補正 C★≈6.3 (CV=1.3%, d∈[10,500])。修正 SAM 目的関数を提案。
- **本文との関係**: Paper I body (v1.5) の主構造は Φ(θ)=D_KL(p_θ‖q)、α-接続 A_i (§2.2)、忘却曲率 F_{ij}=(α/2)[d(ΦT)]_{ij} (§4)、方向性定理 Th.5.1 (§5)。donor の Th.5.1 (CKA 方向性定理) は body の Th.5.1 を CKA 測度へ直接拡張する対応定理。CKA/KL の測度論的詳細は本文の抽象度を超えるが、橋渡しの構造は明確。
- **判定**: 計算は valid。本文 v1.5 の段階では CKA 側の詳細を前景に出す段階ではないが、donor Th.5.1 ↔ body Th.5.1 の対応は将来版で remark として言及する候補。Paper IV/V との cross-paper reference としても記録。
- **著者判断待ち**: (1) donor Th.5.1 を body Th.5.1 の remark として言及するか、(2) 修正 SAM 目的関数を Paper IV/V へ回すか。

## §M9 Donor Absorption Ledger (2026-04-18)

### D-T-01: 2026-04-11_T抽象化実験メモ

- **donor path**: `drafts/incubator/2026-04-11_T抽象化実験メモ.md`
- **receiver surfaces**: `論文0_忘却の忘却_草稿.md` v0.8 改訂履歴、`論文I_力としての忘却.meta.md` 本節
- **kept**: §9.1-§9.8 の反転履歴、基礎石再定位、Chebyshev 1-形式 `T` の再解釈、Kalon ◎ 不動点到達の provenance
- **discarded**: 時間配分や探索順序の局所メモのみ。内容面の棄却はなし
- **final disposition**: donor file を削除し、provenance は本文改訂履歴 + meta ledger に再配置

### D-T-02: Fisher_SAMを超えて

- **donor path**: `drafts/incubator/Fisher_SAMを超えて.md`
- **receiver surfaces**: `論文I_力としての忘却_草稿.md` §6.7-§6.8、`論文II_相補性は忘却である_草稿.md` §2.5.6、Paper I/II meta の吸収台帳
- **kept**: 方向1 `α-SAM`、方向2 `Oblivion-Aware SAM`、合成案 `α-Oblivion SAM`、Paper I/II 統合計画
- **discarded**: 重複する導入文と phrasing のみ。主張面の棄却はなし
- **final disposition**: donor file を削除し、主張の所在は body 側、由来は Paper I/II meta に保存

## §M10 Incubation / Promotion Ledger (2026-04-26)

| レーン | 対象 | 現在の水準 | 昇格条件 |
|:---|:---|:---|:---|
| spine | C1 方向性定理、C2 class 境界、C3 α_I-線形性 | Paper I 本体 | §5.1-§5.4 と Appendix B/F の閉鎖性を保つ。結論で proposal 群を主結果化しない。 |
| theorem seed | OP-I-7: $dT=0$ の保持 / 破れの class 分類 | §5.4 / Appendix F.6 に working classification 挿入済み。E0 は exact $dT=0$。N1 (Student-t, $q=(\nu+3)/(\nu+1)$ q-Gaussian) は $\alpha=\pm(\nu+5)/(\nu-1)$-dual flat。N0 (Cauchy, $q=2$, $\nu=1$) は $T_{ijk}=0$ exact (moment-cancellation) が [SOURCE: Nielsen 2020 PMC7517249 / Mitchell 1988] により確定済み。$dT$ 可積分性が三 class 統一軸として §5.4 closing text に明示済み。 | E0 の exact $dT=0$ の解析的証明の整備、N1 の解析的 $dT\neq0$ 証明、N1→N0 極限の連続的収束 ($\nu\in\{1.5,2,3,5\}$ 数値追試)、open search band への新 class または反例の追加。 |
| sign governance | $\alpha_I$ / $\alpha_{III}$ / $\alpha_{VIII}$ の分離 | 止血済み、監視継続 | 本文で e/m 接続を語る箇所は $\alpha_{III}$ と明記する。$A_i$ と $F_{ij}$ の結合パラメータは $\alpha_I$ として読む。 |
| incubator | FEP、α-遷移層力、α-SAM、Oblivion-Aware SAM、CKA-KL、圏論ゼロ曲率極限 | proposal / outlook / donor | 直接観測、追加公理、または独立証明が揃うまで §10 の burden-bearing claim に戻さない。 |
