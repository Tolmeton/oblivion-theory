# E-XIII-C3-04b Non-FLRW TOV Stress Protocol

**日付**: 2026-04-26
**mode**: `/ene` L2
**目的**: E-XIII-C3-03 の O4 coupling が flat FLRW の高対称性だけに依存していないかを、静的球対称 perfect fluid で検査する。

---

## 0. Question

E-XIII-C3-03 は flat FLRW で、

```text
G_00 <-> rho
G_ii/a^2 <-> p
div G = 0 <-> div T = 0
```

という slot 対応を得た。

本 probe では、時間発展する一様宇宙ではなく、半径方向に内容が変化する静的球対称 fluid を使う。ここで O4 が残れば、対応は FLRW のみに閉じた偶然ではなくなる。

---

## 1. Setup

単位系は `G=c=1`、宇宙定数は使わない。metric は

```text
ds^2 = -exp(2 Phi(r)) dt^2
       + (1 - 2m(r)/r)^(-1) dr^2
       + r^2 dOmega^2
```

内容側は mixed form の perfect fluid として

```text
T^mu_nu = diag(-rho(r), p(r), p(r), p(r))
```

を置く。

この metric は FLRW ではない。容器側には `m(r)` と `Phi(r)` という半径方向の構造があり、内容側には `rho(r)` と `p(r)` がある。

---

## 2. Source Policy

| source | role |
|:---|:---|
| Tolman (1939), CaltechAUTHORS record | static spheres of fluid in Einstein equations の歴史的・標準的接地 |
| Oppenheimer-Volkoff (1939), APS record | neutron cores / relativistic equilibrium の標準的接地 |
| local SymPy symbolic run | 本稿で使う metric から `G^mu_nu` と `div T` を再計算する局所 SOURCE |

外部 source は TOV 型 probe の正当性を支える。忘却論的な container/content 読みは外部 source には無いので、`INFERENCE` として分ける。

---

## 3. Pass Conditions

| id | condition | pass meaning |
|:---|:---|:---|
| T1 | `G^t_t` が `rho(r)` slot に入る | 内容密度が容器側の mass function と結合する |
| T2 | `G^r_r` / `G^theta_theta` が pressure slot に入る | 圧力が幾何の radial/tangential 成分と結合する |
| T3 | `div T=0` が `p'(r)` を含む非自明な radial balance を与える | FLRW の continuity equation より強い stress test になる |
| T4 | `Phi'(r)` が `m(r), p(r)` から定まる | 容器側と内容側が同じ coupling equation に入る |
| T5 | 未導出項目を切り分ける | 係数・作用原理・一般 GR case を過剰主張しない |

---

## 4. Failure Conditions

| id | failure | implication |
|:---|:---|:---|
| F1 | `G` と `T` の slot 対応が FLRW でしか成立しない | O4 は高対称 case の偶然へ降格 |
| F2 | `div T=0` が容器側の構造を含まない | O3->O4 の closure bridge が弱い |
| F3 | TOV が通っただけで定理昇格する | 過剰主張。係数・作用原理・一般 case が未閉鎖 |
| F4 | physical EOS を閉じたと読む | 別問題。ここでは equation of state は導出しない |

---

## 5. Expected Output

1. `XIII_C3_non_flrw_tov_symbolic_ledger.md`
2. `XIII_C3_non_flrw_tov_matrix.md`
3. `XIII_C3_non_flrw_tov_result.md`
4. `論文XIII_時空は忘却である.meta.md` の C3 gauntlet / §M6 更新
