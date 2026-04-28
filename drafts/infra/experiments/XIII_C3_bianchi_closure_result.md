# E-XIII-C3-02 Result

**日付**: 2026-04-26
**状態**: O3 role-level probe 完了
**判定**: 支持。ただし定理昇格なし。C3 は skeleton から一段締まったが、まだ closure 完了ではない。

---

## 1. Kernel Result

E-XIII-C3-02 の結果は次である。

```text
Face Lemma = raw defect の detectability
Bianchi identity = projected defect の closure / conservation
Einstein tensor = conserved coupling projection
```

この読みでは、`∇^μG_{μν}=0` は Face Lemma そのものではない。Face Lemma が比較面を立て、Riemann/holonomy の raw defect を露出可能にする。その後、contracted Bianchi identity が、内容へ結合できる rank-2 projection を divergence-free に制約する。

したがって E-XIII-C3-01 の D2' は維持できる。

```text
Riemann/holonomy = raw defect
Ricci/scalar = contracted defect
Einstein tensor = conserved coupling projection
```

---

## 2. C3 状態

| dimension | before E-02 | after E-02 |
|:---|:---|:---|
| O1 type assignment | direction / comparison / transport で安定 | 維持 |
| O2 defect | raw defect ladder を得た | 維持 |
| O3 closure | open | role-level support。Bianchi = projected syndrome closure |
| O4 coupling | open | 次の中心実験 |
| Kalon status | near / skeleton | near / skeleton。O3 は締まったが定理化なし |

---

## 3. What Was Rejected

**棄却 1**

```text
Bianchi identity = Face Lemma の 2-simplex closure そのもの
```

理由: Face Lemma は comparison surface / detectability の最小条件であり、Bianchi は projected defect の保存条件である。両者を同一視すると、Face Lemma と Coherence Defect / closure 層が潰れる。

**棄却 2**

```text
∇^μT_{μν}=0 を前提にして ∇^μG_{μν}=0 の意味を作る
```

理由: それでは geometry-side closure ではなく、内容側保存則の輸入になる。O3 は O4 coupling の前提でなければならない。

**棄却 3**

```text
O3 が通ったので Einstein 方程式の導出も通った
```

理由: O3 は `G_{μν}` が coupling-ready な projection であることまでしか支えない。`G_{μν}=8πG_NT_{μν}` の等号、係数、内容との整合は O4 に残る。

---

## 4. Paper XIII への編集契約

本文をすぐ大きく編集するなら、§8 だけを対象にする。

| section | allowed change |
|:---|:---|
| §8.2 D2 | `Einstein tensor = 2-simplex area` を `raw curvature -> contraction -> conserved projection` に置換 |
| §8.2.1 O2 | raw defect は Riemann/holonomy 側へ明示 |
| §8.2.1 O3 | `∇^μG_{μν}=0` を projected syndrome closure として書く |
| §8.2.1 O4 | まだ open。`T_{μν}` との等号へ進めるが、ここでは閉じない |
| conclusion | 強化しない |

---

## 5. Surprise Harvest

**Surprise**: MED / 型誤差。

予測では、Bianchi identity を Face-side closure として比較的直接に置ける可能性があった。観測結果は一段ずれている。Bianchi は Face Lemma の直接実現ではなく、Face Lemma が露出した defect を conserved projection へ落とす次段条件である。

このずれは C3 を弱めるというより、層を正しく分ける方向に働く。

---

## 6. Verdict

**判定**: support with demotion.

O3 は role-level では通る。だが `[定理]` ではなく `[構造的対応] / [予想]` に留める。現時点で言える最大値は次である。

> contracted Bianchi identity は、Face Lemma が露出させる raw geometric defect を、内容へ結合可能な conserved projection へ制約する closure condition として読むことができる。

次は O4 である。`G_{μν}` が conserved projection として選ばれるだけでは足りない。その projection がなぜ `T_{μν}` と等置され、容器/内容の非対称整合条件になるのかを、FLRW または Jacobson-style local patch で試す必要がある。
