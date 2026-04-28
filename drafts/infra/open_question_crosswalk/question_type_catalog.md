# Open Question Crosswalk — Question Type Catalog

- 作成日: 2026-04-26
- 目的: 外部論文の open question / limitation / future work を、忘却論 anchor 探索に渡せる中間型へ分類する。
- 注意: この型は外部論文側の問いの形であり、忘却論側の答えではない。

## Typing Rule

| rule | 内容 |
|---|---|
| primary type | その OQ が最も強く問うている欠落。1つだけ付ける。 |
| secondary type | 隣接する欠落。0〜2個まで。 |
| split required | 1つの OQ に複数の独立問題が詰まっている場合、mapping 前に child OQ へ分割する。 |
| source discipline | type 判定は intake の SOURCE 行に基づく。domain scope seed は WEAK INPUT として別扱い。 |

## Type Catalog

| type id | type name | 外部論文側の問い | 忘却論側で探す anchor の方向 |
|---|---|---|---|
| QT-REP-ONTO | Representation Ontology | feature / representation / divergence / object とは何か。何を単位として切ればよいか。 | 粗視化、可区別性、構造保存、関手像、α-米田、CPS object |
| QT-DECOMP-REC | Decomposition / Recoverability | 観測されたモデル・表現・出力から、内部構造をどこまで分解・回復できるか。 | N∘U 剰余、η_unit / Ker(η_unit)、回復フィルトレーション、inverse recovery |
| QT-FORMAL-VERIF | Formalization / Verification | toy model 的理解を frontier system の保証・形式検証へ拡張できるか。 | forgetful abstraction の証明可能範囲、symbolic reduction の限界、可検証性の残余 |
| QT-TRANSFER-INV | Transfer / Invariance | ある architecture / modality / scale で見えた構造は、別の系へ移るか。 | 基質非依存性、構造保存定理、自然性、invariant under U |
| QT-CLOSURE | Closure / Boundary Maintenance | action-perception loop, Markov blanket, identity, self-update などの閉路・境界がどう保たれるか。 | MB維持、境界面、閉包条件、忘却バンドル、可逆/不可逆忘却 |
| QT-CONTEXT | Context Allocation / Degradation | 長文脈・入力集合の中で、何を使い、何を落とし、なぜ劣化するか。 | Context Rot、attention as non-uniform forgetting、回復不能性、選択的忘却 |
| QT-COMP-GEN | Compression / Generalization | 記憶・圧縮・単純性・一般化の関係をどう説明するか。 | 学習=忘却、IB/GeoIB、effective simplicity、忘却の第二法則 |
| QT-EMERGENCE | Emergence / Threshold | scale / depth / training / structure で、なぜ閾値的に能力や効率が現れるか。 | 臨界忘却閾値、phase transition、genuine n-cell、構造保存の発火条件 |
| QT-MEAS-DEFORM | Measurement Deformation | metric / benchmark / probe / similarity measure が現象を作っていないか。 | 観測関手、U_obs、Goodhart 化、測定誘導の忘却、diagnostic vs ontic |
| QT-GROUNDING | Grounding / Multimodal Binding | 記号・言語・文化・身体・modalities をどう接地・結合するか。 | 制約-符号化分離、MB透過性、差異による同定、精度加重 |
| QT-FACT-AMB | Factorization / Subsystem Ambiguity | subsystem, interior, marginal, entanglement, boundary の切り方が一意でない。 | CPS分解、射影選択、superselection、境界制約、部分系としての忘却 |
| QT-OBS-ACCESS | Observational Access / Resolution | phase-space, real-time interior, sub-cycle/sub-wavelength など、対象への観測アクセスが不足する。 | 観測関手、解像度限界、隠れ座標、projection loss、外部較正点 |
| QT-PRECISION-MECH | Precision Mechanism / Specificity | precision weighting の実装機構、neuromodulation、障害別 specificity が未解明。 | 異方的精度、精度加重、MB維持、認知的ゲージ接続、相転移 |
| QT-MEM-CONSOL | Memory Consolidation / Selection | 睡眠・固定化・downscaling で、何が保持され何が刈られるかが未解明。 | 学習=忘却、選択的忘却、schema 化、Ostwald 熟成、再結晶化 |
| QT-GEOM-OBSTR | Geometric Obstruction / Structure Existence | 情報不等式、divergence、connection、cohomological obstruction など、構造の存在条件は何か。 | 曲率、torsion、障害類、CPS span、忘却曲率、enriched distance |
| QT-SYN-SEM | Syntax-Semantics Bridge | 実装 syntax と制約 semantics、top-down と bottom-up をどう橋渡しするか。 | 忘却関手としての抽象化、CPS container-projection-span、adjunction, semantics-preserving U |
| QT-META-AGENDA | Meta Agenda / Bundle | survey/roadmap 型で、複数の独立 open question を束ねている。 | mapping 前に child OQ 分割。単独 anchor を急がない。 |

## Rejection / Split Criteria

| condition | action |
|---|---|
| 1つの row に3型以上が自然に入る | `QT-META-AGENDA` として child OQ 分割 |
| field name だけで型を決めている | rejected: vocabulary-only |
| measurement problem と mechanism problem が混在 | primary を著者の明示問いに合わせ、secondary にもう一方を残す |
| 忘却論 anchor が先に浮かんで型を引っ張る | 型判定をやり直す。外部論文側の欠落を優先する |
| 物理側の reconstruction / factorization と AI側の recoverability が似て見える | primary は著者の対象に寄せる。横断統合は anchor mapping 段階で行う。 |
