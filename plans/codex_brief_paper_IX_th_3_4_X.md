# Codex Brief: Paper IX 本文 §3.6 — Th. 3.4.X 独立定理化

**起草日**: 2026-04-27
**起草者**: Claude (Advisor)
**実行者**: Codex (Executor)
**呼出経路**: project hook `hooks/delegate-codex.sh --contract-mode off`
**対応する meta**: `drafts/series/論文IX_エントロピーは忘却である_草稿.meta.md` v0.3 §M6 C6 「次の実化操作 Step 2」
**親セッション**: monograph 第Ⅵ幕統合章 (Paper XIII Phase 5 + 動的第二法則) の旗艦定理化

---

## 1. タスク要約

Paper IX 本文 (`drafts/series/論文IX_エントロピーは忘却である_草稿.md` v0.8) に新節 **§3.6 「時間の矢 = 忘却の矢」(Th. 3.4.X)** を挿入する。これは備考 3.4.4 の三段チェーン $\mu\downarrow \to \alpha\uparrow \to S_{\mathrm{CPS}}\uparrow$ を、既存定理 (Th. 3.4.1 + Paper V Th. 2.3.1) の合成として **独立定理 Th. 3.4.X** に昇格させる作業。

OP-IX-7 を C6 として核主張化済み (meta v0.3 §M2)、Kalon ◎ Kalon△ 候補 (§M3)、±3σ 維持 + Future-Proof +1σ 強化 (§M4)、Refutation Gauntlet Round 1-2 で射程維持 ✓ (§M5)、虚→実変換面の 6 条件明示済み (§M6)。

**変更範囲**: Paper IX §3 末尾に §3.6 を新節挿入。§3.5 命題 3.5.1 の後、§4 「射計数エントロピーとの関係」の前。

---

## 2. 入力 SOURCE (原典確認義務)

実装前に以下を Read で確認すること:

1. `drafts/series/論文IX_エントロピーは忘却である_草稿.md` v0.8
   - **§3.4 定理 3.4.1** (CPS エントロピー単調性): L120-152 (証明 + 系 3.4.2 ダイバージェンス非依存性 + 備考 3.4.4 三段チェーン)
   - **備考 3.4.4** (時間の矢 = 忘却の矢): L148-152 — Th. 3.4.X はこの備考の独立定理化
   - **§3.5 命題 3.5.1** (CPS エントロピーの α-境界条件): L154-172 — Th. 3.4.X はこの後に挿入
   - **§7 Open Problems OP-IX-7**: L427 — 実装後に「閉鎖済 → Th. 3.4.X として §3.6 で形式化」に更新

2. `drafts/series/論文V_繰り込みは忘却である_草稿.md` (v3.5)
   - **Th. 2.3.1** ($\beta_{\alpha_{\mathrm{III}}} \leq 0$ の漸近自由性): 条件 ($n<5 \wedge \alpha < \alpha_*$) を確認
   - **系 2.3.1a** (RG 時間 = 物理時間 UV→IR): 仮説 (P*) の SOURCE
   - 注意: Paper V を Codex が独立に Read して、Th. 2.3.1 の正確な statement と条件を引用すること (Claude 起草時の paraphrase に依存しない)

3. `drafts/infra/リファレンス/統一記号表.md` v0.13
   - **§1.1 α パラメータ群**: $\alpha_{\mathrm{III}} \in \mathbb{R}$, $\alpha_{\mathrm{VIII}} \in [0,1]$, $\eta$ sigmoid 接続
   - **§2 Paper V 索引**: V-T1 (β_Φ 単調性 = c 定理) と Th. 2.3.1 の関係
   - **§2 Paper IX 索引**: IX-T1 (CPS エントロピー単調性) — Th. 3.4.X は IX-T2 として登録予定

4. `drafts/series/論文XII_速度は忘却である_草稿.md` (v0.8)
   - **§8.3** (β_α ≤ 0 による χ 単調性強化): 前方参照 (Th. 3.4.X が完成すれば forward link を追加可能) の現状を確認

5. `drafts/series/論文XIII_時空は忘却である_草稿.md` (v0.1)
   - **§4 (CPS と重力)** および **§8 (Face Lemma ↔ Einstein dictionary)**: Th. 3.4.X が monograph 第Ⅵ幕統合章で Verlinde / Jacobson 接続の核として機能する仕組みを把握

6. `drafts/standalone/類推的自由エネルギー_草稿.md` v0.3
   - Friston FEP 接続: Th. 3.4.X が「VFE Complexity 削減の動的版」として読める可能性

---

## 3. 実装する §3.6 の構造

以下の構造で §3.6 を新節として書く。**節構造を変えるな。各小節の役割を保て。**

### §3.6 時間の矢 = 忘却の矢 (Th. 3.4.X)

#### §3.6.1 動機と位置づけ

備考 3.4.4 で示した三段チェーン $\mu\downarrow \to \alpha\uparrow \to S_{\mathrm{CPS}}\uparrow$ を、既存 2 定理 (Th. 3.4.1 + Paper V Th. 2.3.1) の合成として独立定理 Th. 3.4.X に昇格させる目的を明示する。
- 動機 1: monograph 第Ⅵ幕統合章 (Paper XIII Phase 5 + Paper IX 動的版) で旗艦定理として引用するため
- 動機 2: OP-IX-7 を閉鎖し、熱力学第二法則の動的版を忘却論内部で閉じる
- 動機 3: Paper XII §8.3 の χ 単調性予測に動的根拠を提供

#### §3.6.2 仮説 (P*) の precision note

**重要**: ここを丁寧に書くこと。Round 1 (循環論証告発) への応答として精密化が要る。

> **仮説 (P*)** [実験的知見の最強水準 / 仮説水準]. 物理時間 $t$ と粗視化スケール $\mu$ の間に関係 $d\mu/dt \leq 0$ が成立する (RG 時間 = 物理時間の UV→IR 同一視仮説)。

Paper V §2.3 系 2.3.1a を SOURCE として明示参照。
- (P*) は **経験的仮説** であり、本稿の定理の **前提として明示する** (循環ではなく条件付き導出)
- (P*) を **定義** に格上げする選択肢 (時間 t を $-\log \mu$ で定義) は §M5 Round 3 適用仮説として保留 (Paper XII XII-T0 との整合性確認 OP)

#### §3.6.3 定理 Th. 3.4.X 「動的第二法則」

> **定理 3.4.X (動的版 CPS 第二法則).** 仮説 (P*) が成立し、Paper V Th. 2.3.1 の条件 $n<5 \wedge \alpha < \alpha_*$ を満たす忘却論的系において、状態 $p$ の CPS エントロピーは時間に関して非減少である:
>
> $$\frac{dS_{\mathrm{CPS}}(p, \alpha(t))}{dt} \geq 0$$

**証明** (3-5 行で完結):
1. (P*) より $d\mu/dt \leq 0$
2. Paper V Th. 2.3.1 ($\beta_{\alpha_{\mathrm{III}}} \leq 0$, 条件 $n<5 \wedge \alpha < \alpha_*$ 下) より、$\mu$ の減少は $\alpha$ の増加を導く: $d\alpha/dt = (\partial \alpha / \partial \mu)(d\mu/dt) = (\beta_{\alpha} / \mu)(d\mu/dt) \geq 0$
3. Th. 3.4.1 (CPS エントロピー単調性) より、$\alpha$ の増加は $S_{\mathrm{CPS}}$ の増加を導く: $S_{\mathrm{CPS}}(p, \alpha_1) \leq S_{\mathrm{CPS}}(p, \alpha_2)$ for $\alpha_1 \leq \alpha_2$
4. (1) (2) (3) の合成: $dS_{\mathrm{CPS}}/dt \geq 0$. □

#### §3.6.4 系 (Cor. 3.4.X.1) と Cor. 3.4.X.2

**系 3.4.X.1 (ダイバージェンス非依存性の動的版).** 系 3.4.2 の動的版として、Th. 3.4.X は divergence $D$ の具体形に依存しない。Shannon / Rényi / Gini-Simpson のいずれの動的第二法則にも同じ証明が適用される。

**系 3.4.X.2 (Paper XII χ 単調性への前方接続).** Paper XII §8.3 の χ 単調性予測は、Th. 3.4.X の特殊例として読める。χ 関数の単調性は CPS エントロピーの単調性の **可区別性境界版** である。

#### §3.6.5 外部巨人との差分テーブル

Round 2 (Verlinde / Jacobson 接続) で要求された差分テーブルをここに置く。

| 既存理論 | 領域 | 主張形式 | Th. 3.4.X との関係 |
|:--|:--|:--|:--|
| Boltzmann H 定理 (1872) | 統計力学 | 粒子分布の粗視化から $dH/dt \leq 0$ | 統計力学の特殊例。Th. 3.4.X は **圏論的射包含** で同じ構造を抽象化 |
| Jacobson (1995) 熱力学 Einstein 方程式 | 一般相対論 | 局所 Clausius 関係 $\delta Q = T dS$ から Einstein 方程式 | Jacobson は時空に限定。Th. 3.4.X は **任意の CPS 圏で成立** (重力なしでも) |
| Verlinde (2011) entropic gravity | 重力 | 重力 = entropic force ($F = T \nabla S$) | Verlinde は重力の起源を熱力学に求める。Th. 3.4.X は **逆方向**: 第二法則そのものを忘却論で導出 |
| Page-Wootters (1983) 内部時間 | 量子重力 | 時間 = 観測者の内部相関 | Page-Wootters は時間の起源を量子相関に求める。Th. 3.4.X は **粗視化の単調性** で同型構造を提供 |

差分の核心: **Th. 3.4.X は時間の矢の起源を忘却論内部 (圏論的射包含) で閉じる**。外部 (boundary condition / decoherence / measurement / 量子相関) に置かない。

#### §3.6.6 Th. 3.4.X が閉じる open problems と残る OP

**閉じる**:
- OP-IX-7「時間の矢 = 忘却の矢」: 独立定理 Th. 3.4.X として形式化 → §7 OP-IX-7 を「閉鎖済 (§3.6 Th. 3.4.X)」に更新

**残る (新規 OP)**:
- OP-IX-7' (高次元 / $\alpha_*$ 超え): Paper V Th. 2.3.1 の条件 ($n<5 \wedge \alpha < \alpha_*$) 外での Th. 3.4.X の振る舞い
- OP-IX-7'' ((P*) を定義に格上げ): 時間 $t$ を $-\log \mu$ で定義する反転 (Round 3 Solution-Focus 適用仮説) と Paper XII XII-T0 との整合性

#### §3.6.7 monograph 第Ⅵ幕統合章への前方参照

> **前方参照**: Th. 3.4.X は monograph 第Ⅵ幕統合章 (Paper IX + Paper XIII + Paper XIV + 類推自由エネルギー) で旗艦定理として引用される。Paper XIII Phase 5 Blocker A1 (Face Lemma → Einstein closure) において、時間方向の整合性は Th. 3.4.X によって与えられる。Paper XIV Route D (Pauli 排他律 → φ) との接続は、忘却の動的構造の離散・有限体インスタンスとして読める。

---

## 4. 同期する関連文書 (Step 3 — Claude 直接実装、本 brief の対象外だが Codex 認識用)

**Codex は以下を変更しない。Step 3 として Claude が別途実施する**:
- 統一記号表 §2 Paper IX 索引に **IX-T2 (Th. 3.4.X 動的第二法則)** を追加
- 熱力学対応表 #8 の備考を「Th.6.10.3 + Th.3.4.1 + Th.3.4.X = 静的版 + 動的版」に更新
- Paper XII §8.3 の β_α ≤ 0 接続箇所に Th. 3.4.X への前方参照を追加

---

## 5. 受入基準

実装後、Advisor (Claude) が以下で ACCEPT/GUIDE/REJECT/STOP を判定する:

**ACCEPT 条件**:
1. §3.6 が §3.5 の後、§4 の前に新節として挿入されている
2. 仮説 (P*) が precision note として独立に明示されている (循環論証告発への応答)
3. Th. 3.4.X の証明が 3-5 行で完結し、Paper V Th. 2.3.1 + Th. 3.4.1 の合成として読める
4. 系 Cor. 3.4.X.1 (ダイバージェンス非依存性の動的版) と Cor. 3.4.X.2 (Paper XII χ 単調性接続) が明示されている
5. 外部巨人差分テーブル (Boltzmann / Jacobson / Verlinde / Page-Wootters) が §3.6.5 に置かれている
6. §7 Open Problems の OP-IX-7 が「閉鎖済 (§3.6 Th. 3.4.X)」に更新されている
7. OP-IX-7' と OP-IX-7'' が新規 OP として §7 に追加されている
8. 主張水準ラベル (定理 / 仮説 / 実験的知見) が §1b.1〜§1b.3 (批判反証レジストリ) に従って明示されている
9. 変更履歴に v0.9 (2026-04-27, §3.6 Th. 3.4.X 独立定理化) として記録されている

**GUIDE 条件** (Codex に追加指示):
- (P*) の主張水準ラベルが「実験的知見」「仮説」「予想」のいずれか曖昧な場合 → 統一記号表 §0.3 + 批判反証レジストリ §1b.2 を引用して水準を明示させる
- Th. 3.4.X の証明が Paper V Th. 2.3.1 を「条件付きで」引用していない場合 → 条件 ($n<5 \wedge \alpha < \alpha_*$) の明示を要求

**REJECT 条件** (再実行):
- §3.6 を §3.4 内の備考として書いた場合 (独立節として独立定理化が core 要求)
- 証明が 10 行を超えて複雑化した場合 (合成定理の単純さが核)
- 外部巨人差分テーブルを欠く場合 (Round 2 の SFBT 試行が未反映)
- (P*) を定理として書いた場合 (循環論証告発を防げない)

**STOP 条件**:
- Paper V Th. 2.3.1 の statement が Codex の Read で確認できない or 異なる場合 → Tolmetes に確認義務
- Paper XII §8.3 の β_α ≤ 0 記述が見つからない場合 → 前方参照を保留して Tolmetes に確認

---

## 6. 制約

### 6.1 主張水準ラベル統一

`drafts/infra/リファレンス/批判反証レジストリ.md` §1b.1-§1b.3 に従って、Th. 3.4.X 周辺の全主張に水準ラベルを付与:
- Th. 3.4.X = **定理** (構成的証明あり、(P*) を前提として明示)
- (P*) = **実験的知見** または **仮説** (Paper V §2.3 系 2.3.1a を SOURCE として引用)
- Cor. 3.4.X.2 (Paper XII 接続) = **構成的命題** (Paper XII XII-T0 が暫定水準のため)

### 6.2 記号衝突回避

統一記号表 §1.12 の衝突解消規則を厳守:
- $\alpha$ は $\alpha_{\mathrm{III}}$ または $\alpha_{\mathrm{VIII}}$ を明示 (Th. 2.3.1 は $\alpha_{\mathrm{III}}$、Th. 3.4.1 は $\alpha_{\mathrm{VIII}}$、両者は sigmoid $\eta$ で接続)
- $\beta$ は $\beta_{\alpha_{\mathrm{III}}}$ を明示 (情報幾何的 RG 流。$\beta_{\mathrm{IB}}$ や Boltzmann $\beta$ と区別)
- $T$ は $T_{\mathrm{CPS}}$ または避ける (Paper IX §6.3 の T_CPS、Chebyshev $T_i$、温度 $T$ の三重衝突)

### 6.3 禁止事項

- Th. 3.4.X を新規証明として書くこと (既存 2 定理の合成として書け。証明は 3-5 行)
- (P*) を「自明」「明らか」と書くこと (経験的仮説として明示すること)
- Verlinde / Jacobson を Th. 3.4.X の根拠として書くこと (差分対象として書け、根拠は Paper V + Paper IX)
- §3.6 を §3.4 内の備考として書くこと (独立節 §3.6 として書け)

---

## 7. 委譲メタデータ

- **Advisor Strategy 適合**: implementation task (15 行超) のため Codex 委譲が default
- **委譲経路**: project hook `hooks/delegate-codex.sh --contract-mode off` (memory:codex_invocation_path 整合)
- **timeout**: 30 分 (L3 級タスク想定)
- **本 brief 完了後の Claude 役割**: ACCEPT/GUIDE/REJECT/STOP 判定 → ACCEPT なら Step 3 (関連文書同期) へ移行 → meta v0.4 へ更新 (Step 2 完了記録)

---

*本 brief v1.0 — 2026-04-27 起草*
