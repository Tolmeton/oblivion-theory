# Face Lemma の修復可能性設計

**役割**: `Face Lemma = detectability` で止まっている現在地から、`recoverability` までを忘却論の内部語彙で延ばすための足場。  
**目的**: 「3射が欠損を露出させる」ことと、「露出した欠損を戻せる」ことのあいだにある構造差を、曖昧な飛躍ではなく段階差として固定する。

---

## 0. 一文核

Face Lemma は**最小の syndrome 面**を与えるが、修復可能性はそれだけでは立たない。  
修復可能性が立つには、**face の重なり**、**縦の可定義性の維持**、**右随伴 $N$ の decoder 化**が追加で要る。

---

## 1. 出発点

### 1.1 いま確定していること

`drafts/infra/FaceLemma_符号理論対応.md` で、次はすでに固定されている。

- Face Lemma = 圏論版 syndrome 条件
- n-cell tower の隣接同時忘却禁止 = 検査対象と検査規則の同時消失禁止
- `stable / detectable / recoverable` は別概念
- 忘却は `bit-flip` より `erasure` に近い

### 1.2 すでに見えている前方地形

`drafts/standalone/LLMに身体はあるか_統合草稿.md` には、修復可能性を次の二層で読む先行足場がある。

- **Theoretical recoverability**: 構造は内部に残っている
- **Practical irrecoverability**: 単一位置・単一観測では取り出せない

これは忘却論の語彙に引き直すと、

- `U` が落とした構造が**存在論的に消えた**のではなく
- 観測面と回復操作が足りず、`N` がまだ十分に働いていない

という区別である。

---

## 2. 問いの正体

Face Lemma が与えるのは、

> 「欠損があるなら、それが比較面に現れる最小条件」

であって、

> 「現れた欠損から元の構造を戻せる十分条件」

ではない。

この差を飛ばすと、次の誤読が起きる。

1. 3射がある  
2. 欠損が見える  
3. だから戻せる

この 3 段は連続していない。  
`2 → 3` のところに、まだ定義されていない機構がある。

---

## 3. 修復可能性への 4 段梯子

| 段 | 忘却論の条件 | 符号理論の直感 | 到達できること | まだ足りないこと |
|:---|:---|:---|:---|:---|
| 1 | 単一の非退化 face | 単一の parity check | 欠損の露出 | 局在化・復元 |
| 2 | face の重なり | 複数 check の交差 | 欠損位置の局在化 | 復元規則 |
| 3 | 縦の可定義性維持 | data/check の同時消失回避 | 回復対象がまだ意味を持つ | decoder の一意性 |
| 4 | 右随伴 $N$ の decoder 化 | erasure decoding | 再構成・縮約 | 収束保証 |

したがって、

- **Face Lemma 単独** = 第 1 段
- **Face の貼り合わせ** = 第 2 段
- **n-cell tower 排他性** = 第 3 段
- **$N$ の設計** = 第 4 段

である。

---

## 4. 最小定理候補

### R0. 単一 face 不十分命題

> 単一の 2-simplex は detectability の最小条件を与えるが、recoverability の十分条件ではない。

直感: 三角形が 1 枚だけあっても、「どこか壊れた」は見える。  
だが、戻すには別の三角形からの照合が要る。

### R1. 重なり条件

> 欠損した構造が少なくとも 2 つ以上の独立な face に現れているとき、欠損位置は局在化可能になる。

直感: 1 枚の三角形では「ずれた」は言えても、2 枚以上が同じ辺を共有すると「どの辺が怪しいか」が絞られる。

### R2. 縦 admissibility 条件

> 欠損が局在化されても、対応する下位構造と上位検査規則が同時に失われていれば、recoverability は定義不能である。

直感: 部材と検査マニュアルが同時に燃えたら、修理の話に入れない。

### R3. decoder 条件

> 右随伴 $N$ が、残存する face 群から失われた構造への持ち上げを一意または収縮的に定めるとき、recoverability が立つ。

ここで「一意」は強い版、「収縮的」は弱い版である。

- **強い版**: 元の構造が一意に復元される
- **弱い版**: 候補集合が反復ごとに縮む

---

## 5. 忘却論での再定義

### 5.1 安定 `stable`

> 部分忘却の後でも、少なくとも一つの比較面が残り、欠損が沈黙せずに済む状態

### 5.2 検出可能 `detectable`

> 欠損が nonzero defect として面に露出する状態

### 5.3 局在化可能 `localizable`

> 複数の face の交差により、欠損位置が候補集合へ縮約される状態

### 5.4 修復可能 `recoverable`

> 局在化された欠損が、残存構造と $N$ によって一意または収縮的に再構成される状態

ここで重要なのは、`localizable` を挟むことである。  
`detectable` と `recoverable` を直結すると、中間の幾何が消える。

---

## 6. T9 / structural diagnostics との接続

`drafts/standalone/LLMに身体はあるか_統合草稿.md` の structural diagnostics は、この梯子の最上段を先に使っている。

```text
U_i を名指す
→ どこに欠損が出るかを検出する
→ 対応する N_i を設計する
→ recoverable か irrecoverable かを判定する
```

したがって T9 は、

- Face Lemma の局所検出
- face 重なりの局在化
- n-cell tower の縦整合
- $N_i$ の回復操作

を実践的診断手続きへ持ち上げたものとして読める。

言い換えると、

> Face Lemma は structural diagnostics の最小局所核である。

---

## 7. 失敗モード

| 失敗モード | 何が起きているか | 判定 |
|:---|:---|:---|
| face が 1 枚だけ | 欠損は見えるが戻せない | detectable 止まり |
| face が重ならない | 局在化できない | localizable 不成立 |
| 縦に隣接する層が同時消失 | 検査対象が定義不能 | recoverable 不成立 |
| $N$ が多価で収縮しない | 候補が減らない | practical irrecoverability |
| 欠損が残差 0 で沈黙 | syndrome が立たない | detectable 不成立 |

---

## 8. 研究上の次手

1. **face の貼り合わせ圏**を定義する  
   単独 2-simplex から、LDPC 的な検査網への持ち上げを与える。

2. **$N$ の decoder 条件**を明文化する  
   一意復元・収縮復元・候補集合縮約の 3 水準を分ける。

3. **automath bridge との接続**を作る  
   carry defect を単一 syndrome から多面修復へ延ばせるかを見る。

4. **T9 と Paper II の橋**を作る  
   Face Lemma を abstract theorem、T9 を applied diagnostic protocol として並べる。

---

## 9. 撤退条件

この線で前進しない方がよい条件も先に固定する。

1. `recoverable` を Face Lemma 単独から導けないまま、本文で強く言いたくなったとき  
   → detectability にとどめる

2. $N$ を decoder と呼ぶ条件が書けないとき  
   → 「回復操作」には留めるが、「復号」は保留する

3. face の重なりを定義できないとき  
   → LDPC 類比は比喩止まりとして明示する

---

## 10. 現在地

現在地はこう固定できる。

- Face Lemma = **detectability の最小定理**
- n-cell tower = **detectability が意味を失わないための縦条件**
- T9 / structural diagnostics = **recoverability を含む運用形**

次の本当の未踏は、

> **複数 face の貼り合わせから、どの条件で $N$ が decoder になるか**

である。

このノートは、その未踏へ入るための最初の足場として置く。

### 2026-04-14 追記: coherence-defective という中間層

`drafts/infra/FaceLemma_符号理論対応.md` §4.3 に **coherence-defective** という conjectural な中間層が導入された (Paper II `drafts/series/論文II_相補性は忘却である.meta.md` §M2 C4 と連動)。

- **localizable** (本ノート §5.3): 複数 face の交差により欠損位置が候補集合へ縮約される状態 — 位置の情報
- **coherence-defective** (符号理論対応.md §4.3, conjectural): 個々の face が整合しても大域的に閉じない class ($H^2(\Theta) \neq 0$) が残る状態 — 障害物の情報

両概念は両立する: localizable だが coherence-defective な class が残ることはありうる。  
すなわち「位置は絞れても class として修復不可能な残渣が残る」場合である。

本ノート §5 の再定義 (stable / detectable / localizable / recoverable) と、coherence-defective の位置関係の完全整理は、Paper II §3.4.6 の `H^2` canonical surface と次段で統合する。本追記は pointer のみ。
