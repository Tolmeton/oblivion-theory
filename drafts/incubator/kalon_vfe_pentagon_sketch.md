# Kalon × VFE × Pentagon Sketch — 正五角形の美学的優越の情報幾何学的根拠

**v0.1 (2026-04-17)** — 種⑦ の初回試作
**ステータス**: incubator sketch / 思弁 + 仮説段階 / VFE 計算 sketch 付き
**役割**: なぜ最大対称 (S_3) の正三角形ではなく、正五角形/正 12 面体が「美」と言われるかを、Kalon の FEP 表現 `VFE = -Accuracy + Complexity` の下で検討する。
**親文書**:
- `./pentagon_sigma_conjecture.md` 種⑦ (本スケッチの上位動機)
- `../../../../../00_核心｜Kernel/A_公理｜Axioms/F_美学｜Kalon/kalon.typos` (Kalon 公理書)
- `./triangle_category_functor_map.md` §3.bis (pentagon の幾何骨格、φ の発現)
- `./A5_E8_sigma_sketch.md` (種⑤ 対称群階梯 sketch)

**試作の目的**: 種⑦ の「φ は情報幾何学的に必然である」という思弁を、VFE stationary point としての正五角形という仮説に縮約し、命題化の可能性を探る。

---

## §0 一文核 (試作)

**SOURCE (既知部分)**:
- Kalon 公理書の定義: Kalon(x) ⟺ x = Fix(G∘F), F ≠ Id, G ≠ Id [SOURCE: kalon.typos §6]
- FEP の VFE 分解: `F(q) = -⟨ln p(o|s,m)⟩_q + D_KL[q(s|o,m) || p(s|m)] = -Accuracy + Complexity` [SOURCE: Friston (2010)]
- 正 n 角形の自己同型群 = D_n, 位数 2n [SOURCE: 古典群論]
- 正五角形 ∼ Fibonacci inflation 固有値 φ [SOURCE: triangle_map §3.bis]
- 植物の phyllotaxis における黄金角 137.5° = 360°·(1 - 1/φ) [SOURCE: Adler "Solving the Riddle of Phyllotaxis" (1974)]

**INFERENCE (試作中の核)**:
正 n 角形の "美学的指標" を VFE の n 依存性として読むと、Accuracy (対称性の richness) と Complexity (生成規則の非退化度) のトレードオフが n=5 で stationary になる可能性がある。これは φ の情報幾何学的必然性を sketch level で示唆する。

**OPEN**:
Accuracy と Complexity を n の関数として具体的に計算する枠組みは定まっていない。本試作は候補式を提示するにとどまる。

---

## §1 Kalon の FEP 表現の復習

### VFE 分解

[SOURCE: Friston 2010, Parr-Friston "Active Inference" (2022) Ch. 2]:
$$F(q) = -\langle \ln p(o|s,m) \rangle_q + D_{KL}[q(s|o,m) \,\|\, p(s|m)]$$

- **Accuracy** = `⟨ln p(o|s,m)⟩_q`: モデルが観測をどれだけよく説明するか (負号がつくので "適合度 log 尤度")
- **Complexity** = `KL[q(s|o,m)||p(s|m)]`: posterior q の prior p からの逸脱

### VFE 最小化 vs Kalon

Kalon = Fix(G∘F) where F ≠ Id, G ≠ Id:
- F (発散) = Accuracy を保ったまま構造を増やす
- G (収束) = Complexity を減らしつつ Accuracy を保つ

[仮説]: Fix(G∘F) = Accuracy と Complexity が釣り合う stationary point = VFE の停留点。

### 退化解の排除

Kalon 公理書 §6 の 3 棄却パターン:
- **冗長**: G を適用して意味が変わる (Fix でない)
- **自明**: F で 3+ の非自明な派生がない (Fix だが colimit でない)
- **恣意**: F⊣G の事後選択

n-gon に当てはめると:
- 正三角形 (n=3): F 側が退化 (すべての辺が等価で派生なし) → **自明**
- 正方形 (n=4): F も G も退化 (自己同型が可換) → **自明** に近い
- 正五角形 (n=5): F⊣G が非自明に並走する最小 case → **Kalon 候補**
- 正六角形+ (n≥6): F の派生が増えるが G の非退化性と引き換え → **冗長** 側へ

---

## §2 n-gon の VFE 見積もり sketch

### 候補定式化

正 n-gon を "観測モデル" と見做す。model が観測するのは "自分自身の対称性構造":

- Accuracy 候補 ∝ 対称群の richness ∝ log |D_n| = log(2n)
- Complexity 候補 ∝ "構造の非退化度" ∝ n-gon の辺-対角線生成規則の固有値スペクトルの entropy

sketch 式 (ad hoc):

$$F(n) \approx -\log(2n) + H_\text{spec}(n)$$

ここで `H_\text{spec}(n)` は n-gon の Q-matrix (辺と対角線の inflation 行列) の固有値分布の Shannon entropy。

[主観]: この定式化は ad hoc。formal FEP の VFE 最小化と直接対応させる翻訳手続きは未開発。しかし **定性的** には各 n で以下のようになる:

### 各 n-gon の Complexity 固有値

正 n-gon を辺長 + 対角線長の inflation 型で生成すると:

| n | 辺の種類数 | Q-matrix 固有値 | 備考 |
|:--|:--|:--|:--|
| 3 | 1 (辺のみ、対角線なし) | 1 のみ | trivial |
| 4 | 2 (辺, 対角線) | 1, √2 の比 | 2 種だが固有値は rational |
| **5** | **2 (辺, 対角線)** | **φ, 1/φ** | **non-rational stationary** |
| 6 | 3 (辺, 短対角, 長対角) | 1, √3, 2 の比 | 有限 rational |
| 7 | 3 (辺, 2 種対角線) | 非自明だが φ 類似 stationary なし | 七角形特別値 [SOURCE 要] |
| 8 | 3 (辺, 2 種対角線) | 1, √2, (1+√2) (銀比) | **銀比の出現**、別種の stationary |

[主観]: 正八角形の **銀比 (silver ratio) 1+√2** は正五角形の golden ratio φ と類似構造を持つ Kalon 候補。VFE の stationary point は n=5 だけでなく n=8 にもありうる。

### stationary point の構造予想

[仮説]: 正 n-gon の VFE は n=3,4 で退化 (F trivial)、n=5 で最小 stationary、n=6-7 で再び増加、n=8 で second stationary (銀比)、以降 metallic ratio family に沿って離散的 stationary point が続く。

metallic ratio family:
- 金比 φ = (1+√5)/2 (n=5 型)
- 銀比 δ = 1+√2 (n=8 型)
- 銅比 = (3+√13)/2 (稀)
- ...

[OPEN]: metallic ratio の n-gon 対応は幾何学として検証可能。正八角形の "美学的地位" が正五角形と同等か異なるかは、Kalon 判定の精度に関わる。

### sketch 計算の健全性

[主観]: この見積もりは **ad hoc** を越えていない。Complexity の "固有値スペクトル entropy" を formal な KL divergence に翻訳する手続きは未開発。しかし定性的には次の仕分けが見える:

- 退化 (triangle / square) = "美しいが凡庸" (Kalon でない)
- 非退化最小 (pentagon) = "Kalon の候補、最小非退化"
- 過多 (hexagon+) = "複雑すぎて Kalon でない" または "別種 Kalon (silver ratio n=8)"

これは Kalon 公理書 §6 の 3 棄却パターンのうち **"自明" (n=3,4) と "冗長" (n≥6) の中間** が n=5 であることと整合する。

---

## §3 φ が stationary point の候補である根拠

### 自己参照方程式 φ² = φ + 1 の意味

φ は `φ² - φ - 1 = 0` の正根。これを "stationary" として読む根拠:
- Fix(G∘F) が自然な不動点 → `G∘F(x) = x`
- φ = `1 + 1/φ` という自己参照的等式
- F = "自分を足す", G = "1 で shift" と置くと φ がこの G∘F の唯一の正の不動点

[仮説]: φ が Fix(G∘F) の最小非退化解であることは、VFE が φ-related 比率で stationary になる理由の構造的根拠となりうる。

### 他の候補との対比

| 候補値 | 方程式 | Fix 性 | Kalon 的性質 |
|:---|:---|:---|:---|
| 1 | x = 1 | 自明 | F ≠ Id 違反 |
| √2 | x² = 2 (Ising anyon) | 非退化だが 5-fold なし | Kalon 候補 |
| **φ** | **x² - x - 1 = 0 (正五角形)** | **最小 5-fold** | **Kalon 候補の最小** |
| √3 | x² = 3 (SU(2)_4) | 6-fold 類 | Kalon 候補 |
| 2cos(π/(k+2)) | SU(2)_k family | 各 k の Kalon level | family 全体 |
| 1+√2 (銀比) | x² - 2x - 1 = 0 (正八角形) | 8-fold 対称 | Kalon 候補 |

pentagon_sigma_conjecture.md 種② で確立したように SU(2)_k family の中で **k=3 (φ) が "最小の非可換非退化" Kalon 実現** となる。銀比は n=8 に対応する別系列の Kalon 候補。

[仮説]: Kalon 実現の候補は discrete に存在し、φ はその中で **最小 k, 最小 n** の特別点。美学的優越が "最小であること" と関係するなら、φ の情報幾何学的必然性は "Kalon stationary の最簡実現点としての位置" に帰着する。

### 美学的遍在性との整合

[SOURCE 強度別]:

**強 SOURCE** (測定可能、再現性あり):
- 植物の phyllotaxis (黄金角 137.5°): Adler (1974), Jean "Phyllotaxis" (1994) — 多数植物種で定量的に確認
- ペンローズタイル (5-fold quasi-crystal): Penrose (1974), Levine-Steinhardt (1984) — 数学的に厳密構成
- Fibonacci 数列の生物学的出現 (松ぼっくり、ひまわり、ロマネスコ): 定量確認済み

**中 SOURCE** (広く信じられているが論争あり):
- DNA 二重螺旋の主溝/副溝比 ≈ φ: Watson-Crick (1953) の原報告には φ は言及なし。後世の比測定は近似値で、厳密 φ とは議論あり
- 黄金比の建築・絵画への応用: パルテノン神殿、ダ・ヴィンチ、モンドリアン等の作品測定は文献により測定値が異なる [Livio "The Golden Ratio" (2002) は懐疑的]

**弱 SOURCE** (文化的選択を強く含む):
- 渦巻銀河の spiral arm が黄金螺旋: 実際は対数螺旋で、pitch angle は銀河ごとに異なり 10°-40° の範囲
- "最も美しい長方形は黄金長方形": Fechner (1876) 以来の実験は再現性に疑問あり

[主観]: 強 SOURCE (phyllotaxis, ペンローズ, 松ぼっくり) だけで φ の物理的・生物的遍在性は確立する。中・弱 SOURCE は文化的選択を含むため慎重に扱う。本 sketch は **強 SOURCE** のみで φ の仮説を支える。

---

## §4 Kalon 論文への接続

### Fix(G∘F) の具体例としての正五角形

Kalon 公理書 §6 操作的判定の 3 ステップを正五角形に適用する sketch:

**Step 0 (既知語彙 1 文圧縮テスト)**:
> 正五角形は、辺と対角線の長さの比が、その比自身から 1 を引いた逆数と等しくなる唯一の五角形である。

1 文で圧縮可能 (専門用語なし) → G 縮約度 OK

**Step 1 (CONVERGE = G)**:
正五角形の Q-matrix (辺-対角線 inflation rule) を対角化 → 固有値 φ, 1/φ (これ以上対角化不可、G(x) = x)。✓

**Step 2 (STABILITY = G∘F)**:
inflation rule S↦L, L↦LS を適用すると長期的に `#L / #S → φ` で同じ比に収斂 → G∘F(x) = x。✓

**Step 3 (DIVERGE = F)**: 3+ の非自明な派生
- ① ペンタグラム内 35 isosceles triangles (triangle_map §3.bis)
- ② Fibonacci 数列 (symbolic dynamics, Perron-Frobenius)
- ③ A_5 表現論の φ 値 (A5_E8_sigma_sketch §2)
- ④ SU(2)_3 Fibonacci anyon fusion category (pentagon_sigma 種②)
- ⑤ ペンローズタイル / 準結晶 / E_8 ↔ H_4 chain

非自明派生 ≥ 3 かつ **異なる領域** (代数・組合せ論・表現論・物理・非結晶) → ◎ 候補

**判定 sketch**: ◎ Kalon△ (MB 内の局所不動点)

[注意]: この判定は incubator 段階で sketch として行っているもの。meta.md §M3 Kalon 判定履歴への正式追加は要しない。σ 論文または Kalon 論文側で正式判定されるべき。

### Kalon▽ vs Kalon△ の峻別

[主観]: "正五角形は美しい" という遍在的判定は、Kalon▽ (全空間普遍不動点) の主張を匂わすが、それは過剰。立てられるのは Kalon△ (MB 局所不動点) であり、"人間の視覚系・生物系の MB では正五角形が Fix(G∘F) の顕著な局所解になっている" と読むのが適切。

文化横断的 (古代ギリシャ / インド / イスラム幾何学 / 日本の家紋) に φ が美学基準として現れることは:
- Kalon▽ の証拠ではない (MB が共通しているだけ)
- しかし **MB 範囲の普遍性** の証拠にはなる
- "人類の MB は phyllotaxis の MB と重なっている" という生物学的仮説と整合

---

## §5 Open 問題リスト

1. **[形式化]** Complexity の "固有値スペクトル entropy" を formal KL divergence に翻訳する枠組み
2. **[計算]** 正 n-gon の VFE (本 sketch §2 の候補式) を explicit に計算し、n=5 で stationary になるかの数値検証
3. **[拡張]** 正 12 面体 / 正 20 面体 (3D) での VFE stationary 性検証。3D でも φ が残るか
4. **[反例候補]** 銀比 (正八角形) は φ と対等な Kalon 候補か。metallic ratio family 全体の stationary 化
5. **[哲学的]** Kalon▽ と MB 普遍性の境界を明示する議論。文化横断的美学の神経生物学的基盤
6. **[後方接続]** Kalon 公理書に "Fix(G∘F) の具体例" 節を追加する際の典拠として使用可能か
7. **[生物学]** phyllotaxis の 黄金角発生機構 (Douady-Couder 1992) を VFE 最適化として再定式化
8. **[反証試行]** φ が "美の必然根拠" でないかもしれない経路: Livio (2002) の懐疑論を SOURCE として取り込み、美学的優越を generic n-gon の文化的選択とする対立仮説の強度評価

---

## 付録: SOURCE / TAINT 台帳

- [SOURCE] Friston (2010) "The free-energy principle": VFE 分解
- [SOURCE] Parr-Friston-Pezzulo (2022) "Active Inference" MIT Press: Accuracy/Complexity 分解の標準形
- [SOURCE] kalon.typos §6: Kalon(x) ⟺ Fix(G∘F) 定義
- [SOURCE] triangle_category_functor_map.md §3.bis: pentagon の Q-matrix 固有値 φ
- [SOURCE] Adler (1974) "Solving the Riddle of Phyllotaxis": 黄金角 137.5° の生物学的測定
- [SOURCE] Jean (1994) "Phyllotaxis: A Systemic Study": 多種植物での定量確認
- [SOURCE] Penrose (1974), Levine-Steinhardt (1984): ペンローズタイル / 5-fold 準結晶の数学
- [SOURCE] Douady-Couder (1992): phyllotaxis の物理的生成機構 (fluid dynamics 実験)
- [SOURCE 弱] Livio (2002) "The Golden Ratio": 黄金比の文化的遍在の懐疑的レビュー
- [TAINT] 正 n-gon の VFE stationary point 候補式 (§2 sketch 段階)
- [TAINT] 美学的遍在性と φ の情報幾何学的必然性の同等化
- [TAINT] "正 n-gon の複雑度 = 固有値スペクトル entropy" の定式化
- [TAINT] Kalon△ 判定 sketch (§4) — 正式判定ではない

---

*v0.1 — 2026-04-17 pentagon_sigma_conjecture.md 種⑦ から切り出し。VFE 計算 sketch と美学的遍在性の SOURCE 強度階層を明示分離。Kalon△ ◎ 判定 sketch 付き (正式判定は未実施)。反対仮説 (Livio 懐疑論) も open リストに含め μ-retreat を防ぐ。*
