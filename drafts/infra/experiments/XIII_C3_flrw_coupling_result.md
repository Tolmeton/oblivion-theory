# E-XIII-C3-03 Result

**日付**: 2026-04-26
**状態**: O4 FLRW local probe 完了
**判定**: single-instance local support。定理昇格なし。

---

## 1. Kernel Result

flat FLRW の最小 symbolic run は、O4 に必要な slot 対応を与えた。

```text
G_00 = 3H^2                 ↔  ρ
G_ii/a^2 = -2a''/a - H^2    ↔  p
∇_μG^μ_ν = 0                ↔  ∇_μT^μ_ν = 0
```

ここで右辺の perfect fluid conservation は、

```text
ρ' + 3H(ρ+p) = 0
```

として出る。

したがって、E-XIII-C3-02 の結果

```text
Einstein tensor = conserved coupling projection
```

は、flat FLRW では内容側の density / pressure slot と結合できる。

---

## 2. What This Supports

O4 は次の水準では支えられた。

> `G_{μν}=κT_{μν}` は、少なくとも flat FLRW において、容器側の projected curvature と内容側の density / pressure を同じ tensor slot に置く整合条件として読める。

これは C2 と C3 の接続である。C2 の容器/内容非対称性は「metric が先にあり、stress-energy は metric 上で tensor として定義される」という形で残る。C3 の O3 は「`G` が conserved projection である」という形で残る。O4 はその二つを、単一 case で接続する。

---

## 3. What Was Rejected

**棄却 1**

```text
FLRW が通ったので Einstein 方程式は忘却論から導出された
```

理由: 係数 `κ=8πG_N` は導いていない。作用原理も導いていない。今回の成果は slot 対応と conservation bridge までである。

**棄却 2**

```text
T_{μν} が G_{μν} を定義する
```

理由: Paper VIII / C2 の方向と逆になる。metric がなければ perfect fluid の covariant components `T_{ii}=p a^2` も定義できない。内容は容器上に置かれる。

**棄却 3**

```text
flat FLRW だけで一般 GR case が閉じる
```

理由: FLRW は高対称 case である。anisotropic stress、non-perfect-fluid、inhomogeneous case では追加 probe が要る。

---

## 4. C3 状態

| dimension | before E-03 | after E-03 |
|:---|:---|:---|
| O1 type assignment | direction / comparison / transport | 維持 |
| O2 defect | raw defect ladder | 維持 |
| O3 closure | role-level support | 維持 |
| O4 coupling | open | flat FLRW single-instance local support |
| Kalon status | near / skeleton | near / local-support。定理昇格なし |

---

## 5. Paper XIII への編集契約

今すぐ本文へ戻すなら、§8.2.1 O4 に 1 段落だけ追加できる。

```text
In the flat FLRW probe, the conserved projection G_{μν} occupies the same component slots as the perfect-fluid stress tensor: G_{00} ↔ ρ and G_{ii}/a^2 ↔ p. The contracted Bianchi identity then corresponds to the continuity equation ρ' + 3H(ρ+p)=0. This does not derive the coupling coefficient, but it shows that the container-side conserved projection and the content-side density-pressure pair can be read as one local consistency condition.
```

ただし、現時点では本文本体を編集しない。実験 artifact と meta に留める。

---

## 6. Verdict

**判定**: support with boundary.

E-XIII-C3-03 は、C3 が O4 まで一例で進むことを示した。だがこれは `flat FLRW` の高対称 case であり、一般定理ではない。次に必要なのは、標準 GR source の promotion と、non-FLRW stress test である。

**source promotion**: E-XIII-C3-04a により、FLRW / Bianchi / perfect fluid の標準 GR 側は `drafts/infra/experiments/XIII_C3_GR_source_promotion_ledger.md` へ昇格済み。ただし、係数・作用原理・一般 GR case は未閉鎖のまま。

次の候補:

| candidate | purpose |
|:---|:---|
| E-XIII-C3-04a source ledger | FLRW / Bianchi / perfect fluid を標準 GR source で補強 |
| E-XIII-C3-04b non-FLRW stress test | 高対称性への過適合を検査 |
| E-XIII-C3-04c Jacobson local patch | thermodynamic realization と C2/C3 の接続を検査 |
