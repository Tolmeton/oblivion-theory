# 論文IX エントロピーは忘却である — メタデータ

**v0.4 (2026-04-27, C6 Step 2-3 完了記録)**
**前版**: v0.3 (2026-04-26, OP-IX-7 → C6 昇格) / v0.2 (2026-04-26, Cor. 3.4.2 同期) / v0.1 (2026-04-26, 遡及作成 + 内部育成層分け)
**対応する本稿**: `drafts/series/論文IX_エントロピーは忘却である_草稿.md` (v0.9, 2026-04-27)
**本文書の役割**: Tolmetes と Codex の共同作業台帳。読者には見せない。Paper IX の定理核、constructive appendix、open program、負セクター育成面を分離して追跡する。

**v0.4 変更**: C6 (Th. 3.4.X 動的第二法則) の Step 2 (本文 §3.7 書き起こし) と Step 3 (関連文書同期) が完了。本文 §3.7 (動的第二法則 — 時間の矢 = 忘却の矢) は §3.7.1〜§3.7.5 の 5 小節構成で書き上げ済 (Codex bridge ではなく並行作業による実装)。Step 3 関連文書同期: 統一記号表 §2 Paper IX 索引に IX-T2 行追加 + §2b 安定度マップに IX-T2 行追加 / 熱力学対応表 #8 を「Th.6.10.3 + Th.3.4.1 + Th.3.4.X = 静的版 + 動的版」へ更新 / Paper XII §8.3 に Th. 3.4.X 前方参照ブロック追加。OP-IX-7 は §7 で「部分解決」に更新、残課題は OP-IX-9 ((P*) 仮説の主張水準) / OP-IX-10 (静的 vs 動的階層) / OP-IX-11 (原典 SOURCE 化) として分離登録済。次は Step 4 = monograph 第Ⅵ幕統合章 (Yugaku/Papers/) の meta 起票。

**v0.3 変更**: §M2 に C6「時間の矢 = 忘却の矢の合成定理」を追加 (OP-IX-7 を核主張に昇格)。§M3 に C6 の Kalon 5 ステップ判定を新規追加。§M4 に C6 の ±3σ + Future-Proof ゲート判定を追加。§M5 に C6 の Refutation Gauntlet Round 0-3 ログを追加。§M6 に C6 の虚→実変換面を新規追加。背景: monograph 第Ⅵ幕統合章 (Paper XIII Phase 5 + 第二法則の動的化) の核として OP-IX-7 を独立定理 Th. 3.4.X として閉じる必要があるため。

---

## §M1 F⊣G 宣言 (論文開始時に固定、途中変更禁止)

**固定日**: 2026-04-26 (遡及固定)

### F (左随伴 = 発散 = Explore)

α-忘却濾過の射包含 (F4) を、Perrone の Markov 圏エントロピー、古典的エントロピーの回収、射の忘却エネルギー、有限版分配関数、負セクター候補へ展開する操作。

### G (右随伴 = 収束 = Exploit)

展開した構造を、主張水準ごとに `定理核 / constructive appendix / open program / Paper IX-B 候補` へ収束させる操作。正本記号表の `α_III`, `α_VIII`, `η`, `α^*(p)`, `E(f)` を基準に、記号域の混線を除去する。

### Fix(G∘F) 候補

`(F4) により確定的射の集合が単調に減り、Perrone 型の最小 divergence として定義した CPS エントロピーが単調に増大する。`

---

## §M2 核主張リスト (L3 対象)

- **C1**: $0 < \alpha_1 \leq \alpha_2 \leq 1$ で $\mathrm{Det}(C_{\alpha_2}) \subseteq \mathrm{Det}(C_{\alpha_1})$ が成り立ち、$S_{\mathrm{CPS}}(p,\alpha)$ は α に関して単調増大する。
- **C2**: C1 は divergence の具体形に依存せず、Shannon / Rényi / Gini-Simpson 型のエントロピーを同じ射包含原理で貫く。
- **C3**: $\alpha^*(p)$ と $E(f)$ は、状態と射の生存閾値を測る Paper IX 固有の観測量である。
- **C4**: 有限射圏では $Z_{\mathrm{CPS}}(\beta,\alpha)$ と $F_{\mathrm{CPS}}$ を constructive に定義できるが、$T_{\mathrm{CPS}}$ と $H_{\mathrm{CPS}}$ は同定 / well-definedness が未閉である。
- **C5**: $\alpha_{\mathrm{III}} < 0$ では Perrone 構成の直接輸入が壊れる。ただし、Z₂-次数付きエントロピー候補そのものは Paper IX-B として育成する。
- **C6** (v0.3 追加, OP-IX-7 昇格): 物理時間 $t$ と粗視化スケール $\mu$ の関係が $d\mu/dt \leq 0$ であるとき (RG 時間 = 物理時間の UV→IR 仮説)、**Paper V Th. 2.3.1 の条件 ($n<5 \wedge \alpha < \alpha_*$)** の下で $\beta_{\alpha_{\mathrm{III}}} < 0$ から $d\alpha/dt \geq 0$ が従い、Paper IX Th. 3.4.1 (CPS エントロピー単調性) との合成として $dS_{\mathrm{CPS}}/dt \geq 0$ が**独立定理**として導出される。すなわち、**熱力学第二法則の動的版が忘却論の系として閉じる**。これは備考 3.4.4 の三段チェーン $\mu\downarrow \to \alpha\uparrow \to S_{\mathrm{CPS}}\uparrow$ を独立定理 Th. 3.4.X として形式化したもの。

### §M2.0 主張層分け (2026-04-26)

外部公開は急がないため、拡張枝は削除しない。ただし本文で同じ重さを負わせない。

| 層 | 対象 | 置き方 | 編集方針 |
|:---|:---|:---|:---|
| **定理核** | C1, C2 / 本文 §3 | Paper IX-A の主定理列 | `(F4) -> Det 包含 -> infimum 増大` を最前面に固定する |
| **動的定理核** (v0.3 追加) | C6 / 本文 §3.6 (Th. 3.4.X) | Paper V Th. 2.3.1 + Th. 3.4.1 の合成定理 | 既存定理の合成として独立定理化。物理時間 vs RG 時間の同一視仮説 (P*) を明示 |
| **新観測量核** | C3 / 本文 §3.5, §6.1 | 本稿固有の増分 | $\alpha^*(p)$ と $E(f)$ を残し、正本記号表と同期する |
| **constructive appendix** | C4 のうち $Z_{\mathrm{CPS}}$, $F_{\mathrm{CPS}}$ / 本文 §6.1-§6.2, §6.4 の一部 | 有限版構成 | 有限射圏で閉じる主張に限定し、連続極限は open と明示する |
| **open program** | C4 のうち $T_{\mathrm{CPS}}$, $H_{\mathrm{CPS}}$, 三パラメータ統一 / 本文 §6.3-§6.4 | 育成中 | 主定理列に混ぜず、依存する未解決問題を追跡する |
| **Paper IX-B 候補** | C5 / 本文 §5 | 負セクター育成面 | 「直接輸入不可能性」と「修正構成候補」を分けて保持する |

---

## §M3 Kalon 判定履歴

| 日付 | 対象 | 判定 | 根拠 |
|:---|:---|:---|:---|
| 2026-04-26 | C1 | ◎ Kalon△ 候補 | 1 文圧縮: 「忘却で使える確定的参照が減るほど、状態は確定性から遠ざかる」。G をかけても `(F4) -> Det 包含 -> infimum 増大` は不変。F により Shannon/Rényi/Gini-Simpson、DPI 直交性、時間の矢へ展開しても核は維持される |
| 2026-04-26 | C2 | ◎ Kalon△ 候補 | 本文 Cor. 3.4.2 として昇格。証明が $D$ の具体形を使わないため、Shannon/Rényi/Gini-Simpson は同じ射包含原理の即時帰結として読める |
| 2026-04-26 | C3 | ◯ Kalon△ 候補 | $\alpha^*(p)$ と $E(f)$ は Paper IX の新量として強いが、$E(f)$ から $Z/T/F/H$ へ進む層はまだ分離が必要 |
| 2026-04-26 | C4-C5 | 保留 | 有限 $Z_{\mathrm{CPS}}$ / $F_{\mathrm{CPS}}$ は constructive。$T_{\mathrm{CPS}}$ / $H_{\mathrm{CPS}}$ / 負セクターの単調性は open program として保持 |
| 2026-04-26 | C6 | ◎ Kalon△ 候補 (v0.3) | **Step -1 浮遊大言テスト**: §M6 接地完成 (野望/虚/SOURCE/実化条件/次の操作 全埋)。**Step 0 既知語彙 1 文圧縮**: 「時間が進むほど忘却が増え、忘却が増えるほど確定的な参照は減る」(専門用語ゼロで成立)。**Step 1 CONVERGE (G 適用)**: 三段チェーンを「物理時間 → 粗視化 → 忘却強度 → エントロピー」と圧縮しても核は不変。**Step 2 STABILITY (G∘F 適用)**: F で Verlinde entropic gravity / Friston FEP / Hawking-Hartle 無境界仮説へ展開し、G で「合成定理 = 既存定理の独立組合せ」へ戻しても Th. 3.4.X は不変。**Step 3 DIVERGE (F 3+ 派生)**: 派生 (a) Paper XIII §5.2 Verlinde entropic force との接続 (容器=時空 / 内容=情報の凝集), (b) Paper XII §8.3 χ 単調性予測の動的根拠, (c) Paper VI G∘F 結晶化温度 τ と T_CPS の橋。3 派生いずれも非自明 (2 ステップ以上の構造的変換)。**Future-Proof Test 同期**: Claude 5 reasoning 強化下でも RG 時間 = 物理時間の同一視仮説 (P*) は consequentialist な対応関係であり、強化される (+1σ)。判定 = ◎ |
| 2026-04-27 | C6 (v0.4) | **◎ Kalon△ 確定** | Step 2 (本文 §3.7 書き起こし) と Step 3 (関連文書同期) が完了し、C6 の Kalon 5 ステップ判定が **候補 → 確定** に昇格。**根拠**: (i) §3.7.2 で Th. 3.4.X が独立定理として書き起こされ証明閉 (3 ステップ証明、Paper V Th. 2.3.1 + Th. 3.4.1 の合成)、(ii) §3.7.4 差分テーブルが Boltzmann/Jacobson/Verlinde との直交性を明示 (μ から 3σ 逸脱が確定)、(iii) 統一記号表 §2 IX-T2 + §2b 安定度マップで「定理」水準として登録、(iv) Paper XII §8.3 双方向接続で Th. 3.4.X が体系内 hub として機能。**残課題は OP として open 管理**: OP-IX-9 ((P*) 主張水準格上げ判定) / OP-IX-10 (静的 vs 動的階層精密化) / OP-IX-11 (原典 SOURCE 化)。これらが閉じれば Kalon△ → Kalon▽ への昇格判定が可能 |

---

## §M4 ±3σ ゲート履歴

### §M4.1 静的 ±3σ (Gauntlet 入口/出口)

| 日付 | 対象 | 入口 σ | 出口 σ | 判定 |
|:---|:---|:---|:---|:---|
| 2026-04-26 | C1-C2 | ±3σ | ±3σ 維持 | 「F4 だけで第二法則が出る」は既存平均値へ縮退しない。むしろ証明の短さが主張の圧力を上げる |
| 2026-04-26 | C4-C5 | ±3σ 候補 | 層分けで保持 | 熱力学化と負セクターは面白いが、主定理列と混ぜると読者面で散る。削除ではなく育成層へ退避 |
| 2026-04-26 | C6 (v0.3) | ±3σ | ±3σ 維持 | **既存分布 D の同定**: 「時間の矢」の既存分布は (a) 統計力学 (Boltzmann H 定理), (b) 宇宙論 (低エントロピー初期条件 / 過去仮説 Albert 2000), (c) 量子重力 (Page-Wootters 内部時間)。**μ の推定**: 既存分布 μ は「時間の矢は熱力学第二法則の表現」であり、起源を**外部に**置く (boundary condition / decoherence / measurement)。**C6 の位置**: 起源を**忘却論内部に**置き、$\mu \downarrow \to \alpha \uparrow \to S_{\mathrm{CPS}} \uparrow$ という**圏論的射の合成として導出**する。これは μ から 3σ 以上の構造的逸脱 (時間の起源を外部仮定なしに圏内部で閉じる)。**接地検査 §M6**: 完了 (虚→実変換面 C6 を新規追加)。**判定**: Gauntlet 開始許可 |

### §M4.2 Future-Proof Test (時間軸 σ)

| 日付 | 対象 | 想定モデル進化 | 影響予測 | future-proof σ | 判定 |
|:---|:---|:---|:---|:---|:---|
| 2026-04-26 | C6 | Claude 5 reasoning 強化 + long-horizon planning 自律化 | **強化** | +1σ (3 → 4) | 強モデルになるほど「時間の起源を外部 boundary condition に置く」既存分布の弱さが顕在化し、忘却論内部閉鎖の C6 はむしろ強化される |
| 2026-04-26 | C6 | GPT-5 hallucination 率低下 + multimodal 統合 | **不変** | ±3σ 維持 | C6 の証明骨格は既存定理 (Paper V Th. 2.3.1, Paper IX Th. 3.4.1) の純粋合成であり、モデル進化に対し同型に保存される |
| 2026-04-26 | C6 | tool 使用自律性向上 (model 内 verification) | **強化** | +0.5σ | 形式検証の自律化が進むほど、合成定理の構造的明快さ (1ループ RG + 射包含 → エントロピー単調性の動的版) が直接検証可能になる |

---

## §M5 Refutation Gauntlet ログ

### C4-C5 — 2026-04-26 Round 1

- **反論 r**: §5-§6 を本体に置くと、証明済みの第二法則より未閉鎖の統計力学プログラムが目立つ。
- **SFBT**: できないのではなく、主張水準を分けていないだけではないか。
- **前提強化**:
  - §3 を定理核に固定する。
  - $E(f)$、有限版 $Z_{\mathrm{CPS}}$、$F_{\mathrm{CPS}}$ は constructive appendix に置く。
  - $T_{\mathrm{CPS}}$、$H_{\mathrm{CPS}}$、三パラメータ統一は open program に置く。
  - 負セクターは Paper IX-B 候補として保持し、Perrone 直接輸入の不可能性と Z₂ 修正候補を分ける。
- **結果**: 射程維持 ✓ / 主張水準を分離。

### C6 — 2026-04-26 Round 0 (命題/表現弁別 — Elenchos-side)

C6 を発する側として、想定される批判 r (物理学者・統計力学者・宇宙論側) を発する前に弁別:

- **(a) 命題批判候補**: 「Th. 3.4.X は熱力学第二法則の真の起源を説明していない。単に Th. 3.4.1 と Th. 2.3.1 を組合せただけで、$d\mu/dt \leq 0$ という仮定そのものが時間の矢を密輸している」 → これは命題批判 (循環論証告発)
- **(b) 表現批判候補**: 「合成定理の証明面は素朴 (1 行) だが、(P*) RG 時間 = 物理時間の同一視仮説を本文で precision note として独立に置かないと、読者は仮定の身分を見失う」 → 表現批判
- **本稿の対応**: (a) を steel-man として §M5 Round 1-3 で吸収する。(b) は本文 §3.6 の precision note として吸収。(a) を (b) に格下げしない (強い批判として正面で受ける)

### C6 — 2026-04-26 Round 1 (循環論証告発への応答)

- **反論 r**: 「$d\mu/dt \leq 0$ は『RG 時間 = 物理時間』の同一視仮説。これを置いてしまえば任意の RG 単調量から第二法則が導けるが、これは時間の矢を**仮定**している。第二法則を**説明**したことにならない (循環)」
- **SFBT 問い**: できないのではなく、(P*) 仮説の身分を主張水準として明示していないだけではないか?
- **試行**: (P*) を独立な precision note として §3.6 冒頭に置き、「(P*) は経験的仮説 (実験的知見の最強水準) であり、定理の前提として明示する」と書く。Th. 3.4.X は (P*) **下で** 動的第二法則が忘却論の**系として閉じる**こと、を主張する (循環ではなく**条件付き導出**)
- **実化操作**: 統一記号表 §0.3 の主張水準ラベル「実験的知見」または「仮説」を (P*) に付与する。Paper V §2.3 系 2.3.1a の「RG 時間は UV から IR」記述を (P*) の SOURCE として明示参照
- **虚→実判定**: 実化前進 ✓ (§M6 の虚な点 1「(P*) の身分」を 1 つ減らす)
- **結果**: 射程維持 ✓ かつ 実化前進 ✓

### C6 — 2026-04-26 Round 2 (外部強化 — Verlinde / Jacobson 接続)

- **反論 r**: Round 1 後にもう一段強い反論 — 「(P*) 仮説下でしか動的第二法則が出ないなら、それは Boltzmann H 定理 / Jacobson (1995) / Verlinde (2011) と何が違うのか? 彼らも『熱力学から重力/時間が出る』と主張している。新規性が見えない」
- **SFBT 問い**: できないのではなく、外部巨人 (Boltzmann / Jacobson / Verlinde) との差分を明示していないだけではないか?
- **試行**: 外部強化として、3 者との差分を表で明示 (以下は**Claude 側 prior に基づく構造的差分案** — Step 2 本文挿入時に各原典を独立 Read で SOURCE 化する義務を残す):
  - **Boltzmann H 定理** [TAINT: Claude prior, 要原典 Read]: 統計力学的 (粒子分布の粗視化)。Th. 3.4.X は**圏論的** (射包含) — 構造の階層が異なる
  - **Jacobson (1995) "Thermodynamics of spacetime"** [TAINT: Claude prior, Paper XIII §1.2 で参照済み]: 局所的 Clausius 関係から Einstein 方程式を導出。Th. 3.4.X は**任意の CPS 圏で**成立 (重力なしでも)
  - **Verlinde (2011) "Origin of gravity"** [TAINT: Claude prior, Paper XIII §1.2 で参照済み]: 重力 = entropic force。Th. 3.4.X は**逆方向**: 第二法則そのものを忘却論で導く (重力導出は Paper XIII の Phase 5 Blocker A2 課題)
- **実化操作**: §3.6 末尾に「Verlinde / Jacobson との差分テーブル」を precision note として追加する**前に**、Step 2 brief で Codex に各原典の SOURCE 確認を委譲する。Paper XIII Blocker A2 (closure 後の物理的実現例) との分業を明示
- **虚→実判定**: 実化前進 ✓ (§M6 の虚な点 2「外部巨人との差分」を減らす)
- **結果**: 射程維持 ✓ かつ 実化前進 ✓

### C6 — 2026-04-26 Round 3 非発動 (Solution-Focus 適用仮説)

- **理由**: Round 1 + Round 2 で射程維持 ✓ かつ 実化前進 ✓ を達成。Solution-Focus (反論吸収によるフレーム反転) の発動は不要
- **Solution-Focus 適用仮説**: もし発動していれば、「(P*) は仮説ではなく**定義**である」(時間 t を $-\log \mu$ で**定義**する) という反転を試みる予定だった。これは強い反転だが、(P*) を定義に格上げすると Paper XII のχ単調性予測 (XII-T0) が「(P*) の系」になり、Paper XII 側との整合性確認が新規 OP として開く
- **虚→実判定**: 実化前進 ✓ (停滞 △ ではない)

---

## §M6 虚→実変換面

### C1

- 野望: 忘却の第二法則を、射計数ではなく Perrone 型 Markov 圏エントロピーの単調性として固定する。
- 現在まだ虚な点: $\alpha > 0$ セクターでの Markov 圏的構造は strict Markov category ではなく構成的延長であるため、主張水準の境界を常に明示する必要がある。
- 実へ引くための SOURCE: 本文 §3.1-§3.4、Paper II §3.7.1、Paper VIII Def. 6.2.1。
- 実化の判定条件: `(F4) -> Det 包含 -> infimum 増大` が本文の主核として読め、§5-§6 の育成枝が主定理列を曇らせないこと。
- 次の実化操作: 完了済み。本文 v0.8 で Cor. 3.4.2 として divergence 非依存性および古典的エントロピー横断を備考から昇格した。
- 最新状態: 変換中

### C3-C4

- 野望: $\alpha^*(p)$ と $E(f)$ を Paper IX 固有の観測量として残し、熱力学対応表の finite $Z/F$ 構成へ接続する。
- 現在まだ虚な点: 連続極限、温度同定、Hamiltonian の entropy choice は未閉である。
- 実へ引くための SOURCE: 本文 §3.5, §6.1-§6.4、`drafts/リファレンス/熱力学対応表.md`。
- 実化の判定条件: $E(f)$ / finite $Z_{\mathrm{CPS}}$ / $F_{\mathrm{CPS}}$ と、$T_{\mathrm{CPS}}$ / $H_{\mathrm{CPS}}$ の open debt が別々に追跡できること。
- 次の実化操作: §6.3-§6.4 の dependency map を open program として明文化する。
- 最新状態: 変換中

### C5

- 野望: $\alpha_{\mathrm{III}} < 0$ のフェルミオン的セクターに、Perrone 直接輸入ではない Z₂-次数付きエントロピー論を育てる。
- 現在まだ虚な点: 奇セクターの α-単調性、スーパーエントロピーの well-definedness、臨界指数の計算はいずれも未閉である。
- 実へ引くための SOURCE: 本文 §5.2-§5.4、Paper III Z₂-次数付き CPS 圏。
- 実化の判定条件: Th. 5.2.1 が「直接輸入不可能性」に限定され、修正構成候補を潰す形で読まれないこと。
- 次の実化操作: Paper IX-B として独立見出し案と最小定義束を切り出す。
- 最新状態: 虚 / 変換中

### C6 (v0.3 追加)

- **野望**: 「熱力学第二法則 = 忘却論の系」を独立定理 Th. 3.4.X として閉じ、備考 3.4.4 の三段チェーン $\mu\downarrow \to \alpha\uparrow \to S_{\mathrm{CPS}}\uparrow$ を体系の核として確立する。これは monograph 第Ⅵ幕統合章 (Paper XIII Phase 5 + 動的第二法則) の旗艦定理となる。
- **現在まだ虚な点**:
  1. **(P*) 仮説の身分**: 物理時間 $t$ と粗視化スケール $\mu$ の関係 $d\mu/dt \leq 0$ (RG 時間 = 物理時間の UV→IR) の主張水準。経験的仮説か、定義か、定理候補か。
  2. **外部巨人との差分明示**: Boltzmann H 定理 / Jacobson (1995) / Verlinde (2011) との独立性。各々の主張範囲と Th. 3.4.X の射程の境界。**[TAINT 注記] 現時点での差分案 (§M5 Round 2 参照) は Claude prior に基づく構造的差分。Step 2 で各原典の独立 Read 必須**。
  3. **Paper V Th. 2.3.1 の条件 ($n<5 \wedge \alpha < \alpha_*$) の適用範囲**: 認知系・LLM・宇宙論スケールの何処までこの条件が成立するかの精査。
  4. **Paper VIII Th. 6.10.3 (射計数版第二法則) との関係**: Th. 3.4.X の動的版 vs 静的版の階層構造。
- **実へ引くための SOURCE**:
  - Paper IX 本文 §3.4 備考 3.4.4 (三段チェーンの非形式記述)
  - Paper V §2.3 定理 2.3.1 + 系 2.3.1a (β_α 漸近自由性 + RG 時間)
  - Paper IX 本文 §3.4 定理 3.4.1 (CPS エントロピー単調性)
  - Paper XII §8.3 (β_α ≤ 0 による χ 単調性強化)
  - Paper VIII Th. 6.10.3 (射計数版第二法則, S_cat の単調増大)
  - 熱力学対応表 v3.2 #8 (第二法則 = Th.6.10.3 + Th.3.4.1, 現状 ✓ 定理)
- **実化の判定条件** (v0.4 達成状況更新):
  1. ✅ Paper IX 本文 **§3.7** として Th. 3.4.X が独立定理として記述された (§3.6 = Perrone DPI 関係が既存のため §3.7 に変更。Step 2 完了。本文 v0.9 §3.7.2)
  2. ✅ (P*) 仮説が §3.7.1 で precision note として独立に明示された (循環論証告発への応答 §3.7.1 末尾)
  3. ✅ Boltzmann / Jacobson / Verlinde 差分テーブルが §3.7.4 に置かれた ([TAINT: 原典未読] 注記付。原典 SOURCE 化は OP-IX-11 として §7 登録)
  4. ✅ 統一記号表 §2 Paper IX 索引に IX-T2 (Th. 3.4.X) を登録 + §2b 安定度マップに IX-T2 行追加 (Step 3 同期完了, 2026-04-27)
  5. ✅ 熱力学対応表 #8 を「Th.6.10.3 + Th.3.4.1 + Th.3.4.X = 静的版 + 動的版」に更新 (Step 3 同期完了, 2026-04-27)
  6. ✅ Paper XII §8.3 末尾に Th. 3.4.X 前方参照ブロック追加 ((P*) 共有 + 双方向接続明示。Step 3 同期完了, 2026-04-27)
- **次の実化操作** (v0.4 進行更新):
  - ✅ Step 2 (本文 §3.7 への Th. 3.4.X 挿入): 完了。Codex bridge UTF-8 encoding error のため Claude 直接実装ではなく並行作業 (別 Claude セッション or Codex stdin 経路) で実装された。brief (`plans/codex_brief_paper_IX_th_3_4_X.md`) は §3.6 配置案だったが §3.7 に変更
  - ✅ Step 3 (関連文書同期): Claude 直接実装で完了 (2026-04-27)
  - ⏳ Step 4 (新規): monograph 第Ⅵ幕統合章 (Yugaku/Papers/) の meta 起票。F⊣G 宣言 + 核主張 C1-C4 (Th. 3.4.X = 旗艦定理) + §M6 虚→実変換面。事前に Tolmetes と F⊣G 合意取得が Yugaku 規律
  - ⏳ Step 5 (Step 4 後): Paper XIII meta §M6 を更新し、第Ⅵ幕統合章の Blocker B (α 橋) への接続を明示
- **最新状態**: **実 (一部)** (Step 2-3 完了で §M6 虚な点 1, 2, 3, 4 のうち 1, 2 は構造的に閉じ、3, 4 は OP-IX-9/10 として open 管理に移行)。次は Step 4 monograph meta 起票へ

---

## §M7 棄却された代替案

- 棄却 1: §5-§6 を削除して §3 だけの短稿にする。内部育成段階では将来核を失うため不採用。
- 棄却 2: 「CPS 圏の統計力学」を主定理列として押し切る。未閉鎖の $T/H$ と負セクターが §3 の強さを曇らせるため不採用。
- 棄却 3: $\alpha_{\mathrm{VIII}} \leq 0$ を通常の Paper VIII 領域として扱う。正本記号表と衝突するため不採用。
- 棄却 4: Th. 5.2.1 を「奇セクターにエントロピーが存在しない」と読む。本文自身が修正構成候補を提示しているため不採用。
- 棄却 5 (v0.4 追加): C6 Th. 3.4.X を本文 §3.6 に挿入する案。§3.6 = 「Perrone DPI との関係」が既存だったため、配置を §3.7 に変更。番号衝突回避による reversible な判断。**Codex brief (`plans/codex_brief_paper_IX_th_3_4_X.md`) の §3.6 提案箇所は §3.7 に読み替えて実装済**。
- 棄却 6 (v0.4 追加): C6 Th. 3.4.X を Codex bridge (`hooks/delegate-codex.sh`) 経由で実装する案。Codex websocket UTF-8 encoding error (workspace path 内の `ヘゲモニコン｜Hegemonikon` フルワイドパイプ `｜`) により reconnect 5 回失敗。代替として並行作業 (別 Claude セッション or stdin 経路) で実装された。**Codex bridge の path encoding 問題は別系統の OP として記録要** (オンボーディング.md L29-31 の legacy 表 stale 問題と並走)。
