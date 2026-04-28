# E-XIII-C3-04a Source Promotion Ledger

**日付**: 2026-04-26
**mode**: `/ene` L2
**目的**: E-XIII-C3-03 の FLRW / Bianchi / perfect fluid 使用を、ローカル symbolic ledger だけでなく標準 GR source へ昇格する。

---

## 0. Promotion Level

今回の外部 SOURCE は、Sean M. Carroll, *Lecture Notes on General Relativity*, arXiv:gr-qc/9712019 である。

- arXiv record: `https://arxiv.org/abs/gr-qc/9712019`
- PDF used: `https://sites.astro.caltech.edu/~george/ay21/readings/carroll-gr-textbook.pdf`
- status: standard GR lecture source
- limitation: historical primary source ではない。内部育成稿の source promotion としては十分だが、投稿稿では教科書または原論文 citation へ整える。

---

## 1. External SOURCE Map

| id | source location | supports | promotion result |
|:---|:---|:---|:---|
| GR-S1 | Carroll arXiv record, lines 30-47 | author, title, arXiv ID, DOI | bibliographic SOURCE |
| GR-S2 | Carroll PDF lines 1651-1702 | perfect fluid stress-energy has `rho` and `p` slots | supports E-03 `T` slot reading |
| GR-S3 | Carroll PDF lines 1730-1742 | stress-energy conservation as divergence condition | supports conservation slot |
| GR-S4 | Carroll PDF lines 6597-6632 | Ricci-only equation fails conservation; Einstein tensor is conserved; `G_{μν}=κT_{μν}` is proposed | supports O3 -> O4 bridge |
| GR-S5 | Carroll PDF lines 6707-6719 | Einstein equation and Bianchi constraint on independent equations | supports `G` as constrained projection |
| GR-S6 | Carroll PDF lines 7034-7039 | for arbitrary metric, one may compute `G` and demand `T=G`; conservation follows from Bianchi | supports “do not overclaim physical matter source” caveat |
| GR-S7 | Carroll PDF lines 12650-12730 | Robertson-Walker metric and scale factor | supports FLRW metric choice |
| GR-S8 | Carroll PDF lines 12774-12837 | RW Christoffel / Ricci / scalar formulae | supports local symbolic tensor ledger |
| GR-S9 | Carroll PDF lines 12838-12888 | perfect fluid in comoving coordinates and conservation equation | supports E-03 `rho,p` and continuity bridge |
| GR-S10 | Carroll PDF lines 12983-13029 | Friedmann equations from Einstein equations | supports FLRW component equations |

---

## 2. Claim Promotion Table

| E-03 claim | prior status | promoted status | remaining limit |
|:---|:---|:---|:---|
| flat FLRW metric is a legitimate minimal cosmology probe | local symbolic setup | GR-S7 | only flat case used locally |
| perfect fluid has density and pressure slots | local symbolic setup | GR-S2, GR-S9 | sign/index convention must be stated in manuscript |
| conservation slot is `∇T=0` | local symbolic run | GR-S3, GR-S9 | physical matter equations still source-dependent |
| Einstein tensor is selected by conservation / Bianchi | E-02 role-level | GR-S4, GR-S5 | still not a derivation of coefficient |
| FLRW equations connect curvature components to `rho,p` | local symbolic run | GR-S8, GR-S10 | high-symmetry case |
| arbitrary `T=G` is mathematically possible but physically unconstrained | inferred caveat | GR-S6 | strengthens boundary, not the positive claim |

---

## 3. SOURCE / INFERENCE Split

**SOURCE**

Carroll gives the standard route:

1. perfect fluid stress-energy has energy density and pressure as its two independent rest-frame quantities;
2. energy-momentum conservation is expressed by divergence vanishing;
3. Ricci-only coupling fails the conservation requirement;
4. the Einstein tensor is the conserved geometric tensor used in Einstein's equation;
5. the Robertson-Walker metric plus perfect fluid leads to the Friedmann equations.

**INFERENCE**

E-XIII-C3-03 uses these facts to support a forgetful-theory reading:

```text
container-side conserved projection  ↔  content-side density/pressure slots
```

This inference is not in Carroll. It remains Paper XIII / C3 theory work.

---

## 4. Boundary Ledger

| boundary | status |
|:---|:---|
| coefficient `κ=8πG` | not derived by E-03; Carroll derives it via Newtonian limit |
| Einstein-Hilbert action | not used in E-03 |
| general GR solution space | not covered by flat FLRW |
| realistic matter source restrictions | not closed; GR-S6 explicitly warns against arbitrary source assignment |
| non-FLRW stress test | still required |

---

## 5. Effect On C3

E-XIII-C3-04a upgrades E-03 from:

```text
local symbolic source only
```

to:

```text
standard GR source + local symbolic source
```

This does not make C3 a theorem. It removes a weaker blocker: E-03 no longer rests only on our own symbolic calculation.
