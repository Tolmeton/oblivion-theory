# E-XIII-C3-04d Anisotropic TOV Stress Protocol

**日付**: 2026-04-26
**mode**: `/pei` L2
**目的**: E-XIII-C3-04b の perfect-fluid 制限 `p_r=p_t` を外し、O4 coupling が anisotropic stress でも残るかを検査する。

---

## 0. Question

E-XIII-C3-04b は static spherical perfect fluid で、

```text
T^mu_nu = diag(-rho(r), p(r), p(r), p(r))
div T=0 -> p'(r) + (rho(r)+p(r)) Phi'(r) = 0
```

を得た。

本 probe では、内容側の pressure slot を radial / tangential に分ける。

```text
T^mu_nu = diag(-rho(r), p_r(r), p_t(r), p_t(r))
```

ここで O4 が残れば、TOV support は isotropic perfect-fluid のみに依存しない。逆に保存式が perfect-fluid 形へ潰れたり、`p_t` が container-side geometry と結合しないなら、04b の support は弱くなる。

---

## 1. Setup

単位系は `G=c=1`、宇宙定数は使わない。metric は 04b と同じ:

```text
ds^2 = -exp(2 Phi(r)) dt^2
       + (1 - 2m(r)/r)^(-1) dr^2
       + r^2 dOmega^2
```

内容側は mixed form の anisotropic stress として:

```text
T^mu_nu = diag(-rho(r), p_r(r), p_t(r), p_t(r))
```

を置く。

---

## 2. Source Policy

| source | role |
|:---|:---|
| E-XIII-C3-04b TOV artifacts | metric / symbolic method / perfect-fluid baseline |
| Tolman (1939) / Oppenheimer-Volkoff (1939) records in 04b ledger | static spherical GR stress probe の標準的接地 |
| local SymPy symbolic run | 本稿で使う anisotropic `T^mu_nu` から `div T` と slot 対応を再計算する局所 SOURCE |

外部 source は TOV 型 probe の場を支える。anisotropic stress の忘却論的 container/content 読みは本稿の `INFERENCE` として分ける。

---

## 3. Pass Conditions

| id | condition | pass meaning |
|:---|:---|:---|
| T1 | `G^t_t` が `rho(r)` slot に入る | density slot は 04b から維持される |
| T2 | `G^r_r` が `p_r(r)` slot に入る | radial pressure が radial geometry と結合する |
| T3 | `G^theta_theta = G^phi_phi` が `p_t(r)` slot に入る | tangential pressure が angular geometry と結合する |
| T4 | `div T=0` が `p_r' + (rho+p_r)Phi' + 2(p_r-p_t)/r = 0` を与える | anisotropy が保存式の中に非自明に出る |
| T5 | `p_t=p_r` で 04b の perfect-fluid TOV へ戻る | 04d が 04b の整合的拡張になる |

---

## 4. Failure Conditions

| id | failure | implication |
|:---|:---|:---|
| F1 | `p_t` が保存式に現れない | anisotropic stress が O4 bridge で見えていない |
| F2 | angular pressure slot が container geometry と対応しない | TOV support は isotropic pressure に依存していた |
| F3 | anisotropic case が通っただけで C3 theorem へ昇格する | 過剰主張。一般 GR case / action / coefficient は未閉鎖 |
| F4 | anisotropic fluid の equation of state を導出したと読む | 別問題。ここでは `rho, p_r, p_t` の関係式は外部入力 |

---

## 5. Expected Output

1. `XIII_C3_anisotropic_tov_symbolic_ledger.md`
2. `XIII_C3_anisotropic_tov_matrix.md`
3. `XIII_C3_anisotropic_tov_result.md`
4. `論文XIII_時空は忘却である.meta.md` の C3 gauntlet / §M6 更新
5. `論文XIII_時空は忘却である_草稿.md` §8.2.2 の境界更新
