# automath bridge PR 素材の復元手順

`/tmp/automath` が消えたため、ここに PR 素材を永続退避してある。

## 復元対象

- `OblivionBridge.lean`
- `README.md`
- `ISSUE_REPLY_DRAFT.md`
- `Omega.lean.import.patch`

## automath clone が戻ったらやること

1. `OblivionBridge.lean` を `lean4/Omega/Frontier/OblivionBridge.lean` に置く
2. `README.md` を `theory/bridges/oblivion-theory/README.md` に置く
3. `ISSUE_REPLY_DRAFT.md` を `theory/bridges/oblivion-theory/ISSUE_REPLY_DRAFT.md` に置く
4. `Omega.lean.import.patch` の 1 行 import を `lean4/Omega.lean` に適用する

## 検証

clone 復帰後の検証コマンド:

```bash
cd /path/to/automath/lean4
lake exe cache get
lake build Omega.Frontier.OblivionBridge
lake build Omega
```

## 主張境界

- strict projection functoriality は主張してよい
- defect cocycle / coherence datum は主張してよい
- full `Man -> Hyp` canonical functor は主張しない
- continuous chain-map の完全 formalization は主張しない
- curvature/drift と carry cocycle の完全同一性は主張しない
