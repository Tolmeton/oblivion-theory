# FEP 全体再導出のための統合関手 — 探索ノート

## 0. 判定

[推定] 外部成果に、CPS / 忘却論 / U⊣N / 回復操作へそのまま接続できる「完成済みの統合関手」は見つかっていない。

ただし、かなり近い外部骨格は存在する。Smithe 系の active inference doctrine は、統計ゲーム・Bayesian lens・polynomial interface・力学系を関手的に接続している。さらに `Polynomial Life` は、active inference doctrine を indexed functor として捉え、FEP をその随伴として形式化する方向を示している。

したがって本件は「無いならやる」に値する。新規性の核は、外部の `Poly` インデックスと、CPS の時間インデックス `(R, <=)` を積にし、U⊣N の回復フィルトレーションへ通す統合関手を構成する点にある。

## 1. SOURCE

### 1.1 外部 SOURCE

- [arXiv:2211.01831](https://arxiv.org/abs/2211.01831) `Polynomial Life: the Structure of Adaptive Systems`
  - polynomial functor によって身体境界・感覚・行為を形式化する。
  - internal universes を polynomial 上の statistical games の indexed category とし、dynamics を behaviours の indexed category とする。
  - active inference doctrines を indexed functor として特徴づけ、FEP をそれらの随伴として形式化する方向を示す。
- [arXiv:2208.12173](https://arxiv.org/abs/2208.12173) `Compositional Active Inference II`
  - statistical games から dynamical systems へ関手的に移す approximate inference doctrine を構成する。
  - polynomially indexed categories と hierarchical inference systems を使う。
  - Laplace / Hebb-Laplace doctrine を外部実例として持つ。
- [arXiv:2109.04461](https://arxiv.org/abs/2109.04461) `Compositional Active Inference I`
  - Bayesian lens と statistical game により、Bayesian inversion と free-energy objective を compositional に扱う。
- [arXiv:2308.00861](https://arxiv.org/abs/2308.00861) `Active Inference in String Diagrams`
  - generative model, Bayesian updating, perception, planning, active inference, free energy を string diagram として与える。
  - active inference の式を free energy minimisation から図式的に導く。
- [arXiv:2406.07577](https://arxiv.org/abs/2406.07577) `Structured Active Inference`
  - generative model を interface 上の system とし、その interface を Markov blanket の compositional abstraction とする。
  - agent を generative model の controller とし、dual な関係で捉える。
  - meta-agent や構造変更する agent へ拡張する。
- [arXiv:2305.06112](https://arxiv.org/abs/2305.06112) `The Compositional Structure of Bayesian Inference`
  - Markov kernel の圏で Bayesian inversion を fibred category 上の state-dependent morphism として扱う。
  - inversion の compositional rule を functor として扱う。
- [arXiv:2209.14728](https://arxiv.org/abs/2209.14728) `Dependent Bayesian Lenses`
  - support object によって canonical Bayesian inversion へ入る section を構成する。

### 1.2 内部 SOURCE

- `本リポジトリ外の内部作業ノート`
  - CPS は時刻 `t` ごとに `C_CPS(t)` を割り当てる擬関手 `F: T^op -> Cat` を定義し、Grothendieck 全圏 `∫F` を構成している。
- `本リポジトリ外の内部作業ノート`
  - Smithe は `Poly` で型を index し、CPS は `(R, <=)` で時間を index する。統合枠組みには `Poly × (R, <=)` が必要だと明示している。
- `本リポジトリ外の内部基礎ノート`
  - U⊣N は、忘却 U = 溶解、回復 N = 結晶化として定義される。
- `本リポジトリ外の内部基礎ノート`
  - N-Series は回復構成子として、射・合成・自然変換・精度・因果・文脈・随伴・自己関手を段階化する。
- `本リポジトリ外の内部基礎ノート`
  - `Γ⊣Q`, `F⊣G`, `U⊣N` は同一 Helmholtz モナドの異なるファクタリゼーションとして扱われる。

## 2. 統合関手の候補

仮称: **二重添字 Helmholtz 統合関手**。

外部側:

```text
StatGame_Poly  --D_AI-->  Dyn_Poly
```

ここで `D_AI` は Smithe 系の active inference doctrine であり、統計ゲームを、そのゲームを実行する力学系へ移す。

CPS 側:

```text
T := (R, <=)
F_CPS: T^op -> Cat
t |-> C_CPS(t)
∫_T F_CPS
```

統合側:

```text
B := Poly × T
F_CPS^*: B^op -> Cat
(p, t) |-> C_CPS(p, t)

J: ∫_Poly StatGame -> ∫_{Poly × T} CPS
```

直観的には、`p` が「どんな身体・界面・blanket 型を持つか」を指定し、`t` が「その構造が時間の中でどの α 状態にあるか」を指定する。外部 FEP は `p` の側から agent/interface/policy を与え、CPS は `t` の側から α-twisted Markov blanket の生成・退化・相転移を与える。

## 3. U⊣N への対応

統合関手 `J` は、単なる翻訳関手ではなく、U⊣N の回復操作を実行する関手として読むべきである。

| U/N 層 | 外部成果での対応 | CPS / 忘却論での対応 | 統合関手での役割 |
|:---|:---|:---|:---|
| `N_sensory` | Bayesian lens の Put / sensing | 感覚入力の回復 | interface から観測チャネルを回復 |
| `N_arrow` | Markov kernel / stochastic map | 射の回復 | agent, blanket, environment の関係を明示 |
| `N_compose` | compositional Bayesian inference | 合成律の回復 | 部分推論を全体推論へ接続 |
| `N_depth` | string diagram / hierarchical model | 自然変換の回復 | 階層間の対応を図式化 |
| `N_precision` | free-energy objective / precision update | 精度チャネルの回復 | VFE / EFE を α, π の更新として読む |
| `N_causal` | policy / action / intervention | 因果構造の回復 | action を外界変化として接続 |
| `N_context` | structured interface / polynomial system | 文脈関手の回復 | `Poly × T` で型と時間を同時に持つ |
| `N_adjoint` | FEP as adjoint to doctrine | 随伴片側の回復 | `D_AI` の反対向きを FEP として構成 |
| `N_self` | meta-agent / structure-changing agent | 自己関手の回復 | agent が自分の構造を変える場合へ拡張 |

この表の要点は、FEP 全体を「既存 FEP の語彙で再説明する」のではなく、FEP が前提する回復操作を U⊣N の各層へ分解して再構成する点にある。

## 4. 研究命題

**命題 C-FEP-UN-01**
Smithe 系の active inference doctrine `D_AI` と CPS の時間ファイバー束 `∫_T F_CPS` は、積基底 `Poly × (R, <=)` 上の二重添字圏へ持ち上げられる。この持ち上げ `J` が U⊣N の回復フィルトレーションを保存するなら、FEP の各構成要素は CPS / 忘却論の回復操作として再導出される。

現時点で言えること:

- [SOURCE] 外部には、active inference を indexed functor / string diagram / structured interface として扱う成果がある。
- [SOURCE] 内部には、CPS の時間ファイバー束と `Poly × (R, <=)` 要求が既にある。
- [SOURCE] 内部には、U⊣N の回復フィルトレーションと Helmholtz モナド統一がある。
- [推定] 以上を接続する統合関手 `J` は構成可能である。
- [未主張] `J` はまだ定理ではない。FEP 全体が CPS に包含された、または FEP と CPS が圏的同値である、とはまだ書けない。

## 5. 次の実化操作

1. `J` の定義域と余定義域を固定する。
2. `Poly × T` 上の対象 `(p, t, X)` と射を定義する。
3. Smithe の `D_AI` が `J` を通じて CPS 側の `C_CPS(p,t)` に入ることを示す。
4. U⊣N 表の各 `N_*` について、外部 FEP 操作が対応する回復操作を満たすかを検査する。
5. `N_adjoint` 層で、FEP が active inference doctrine の随伴として本当に立つかを証明候補にする。

この構成が通れば、C 層は「外部成果接続・未統合層」から「統合関手構成層」へ昇格できる。

## 6. `J` の候補定義 v0.1

### 6.1 型上の修正

前節の

```text
J: ∫_Poly StatGame -> ∫_{Poly × T} CPS
```

は、方向としては正しいが、裸のままでは型が足りない。理由は、左辺の statistical game は polynomial interface `p` を持つが、CPS 側の時間 `t` をまだ持たないからである。

したがって、正確には次の 3 つの補助データを添えた関手として定義する。

```text
J_{D,χ,R}: ∫_Poly PSGame_P -> ∫_{Poly × T} CPS^*
```

ここで:

- `D` は active inference doctrine。外部 SOURCE では、`D: PSGame_P -> MProc^T_P` 型の monoidal indexed functor として与えられる。
- `χ` は時間割当。各 game `g` に、CPS 時間圏 `T := (R, <=)` の点 `χ(g)` を割り当てる。
- `R` は CPS 実現。`D(g)` が与える polynomial interface 上の behaviour / Markov process を、時刻 `χ(g)` の α-twisted CPS Markov category へ移す。

直観的には:

```text
statistical game
  --D-->  active-inference behaviour
  --χ-->  time / α-phase を得る
  --R-->  CPS 上の α-twisted Markov blanket dynamics
```

### 6.2 定義域

定義域は、Smithe 系の polynomially indexed category of statistical games の Grothendieck 全圏である。

```text
Dom(J) := ∫_Poly PSGame_P
```

対象:

```text
(p, g)
```

- `p` は polynomial interface。直観的には、身体境界・感覚面・行為可能な構成の型である。
- `g ∈ PSGame_P(p)` は、その interface 上の statistical game。
- `g` は少なくとも、Bayesian lens と fitness / loss function の組として読む。

射:

```text
(φ, u): (p, g) -> (q, h)
```

- `φ: p -> q` は polynomial morphism。interface の組み替え、合成、粗視化、または部分系から全体系への構成を表す。
- `u: PSGame_P(φ)(g) -> h` は、`φ` に沿って移された game と target game の間の game morphism。

この射の直観は、「部分 interface 上の game を、polynomial map `φ` によって別 interface 上の game へ移す」ことである。

### 6.3 余定義域

余定義域は、CPS の時間ファイバー束を polynomial interface で型付けした二重添字全圏である。

```text
Cod(J) := ∫_{Poly × T} CPS^*
```

基底:

```text
B := Poly × T
T := (R, <=)
```

ファイバー:

```text
CPS^*(p,t) := C_CPS^p(t)
```

ここで `C_CPS^p(t)` は、Paper II の `C_CPS(t)` を polynomial interface `p` で型付けしたファイバーである。まだ既存定義ではないので、候補定義として次のように置く。

対象:

```text
(X, b_p, B(X,t))
```

- `X` は時刻 `t` の α-twisted Markov category `C_CPS(t)` の対象。
- `B(X,t)` は動的 Markov blanket。
- `b_p` は `p` の sensorium / action boundary を `B(X,t)` へ対応させる interface 実現。

射:

```text
(φ, s<=t, k): (p,s,X') -> (q,t,X)
```

- `φ: p -> q` は interface 変換。
- `s <= t` は時間遷移。
- `k` は CPS 側の Markov kernel / α-transport で、次を満たす:

```text
k: X' -> (φ, s<=t)^*(X)
```

ここで `(φ, s<=t)^*` は、target の `q`-typed `t`-structure を、source の `p`-typed `s`-structure へ引き戻す操作である。中身は二つに分かれる。

```text
(φ, s<=t)^* = φ^* ; τ_{α(t)->α(s)}
```

- `φ^*`: polynomial interface の pullback / reindexing。
- `τ_{α(t)->α(s)}`: Paper II §4.3.5 の α-transport。

この contravariant な読みは、Paper II の Grothendieck 構成と合う。未来時刻 `t` の構造を過去時刻 `s` のファイバーへ輸送し、そこで source から target への Markov kernel を比較する。

### 6.4 `J` の対象写像

対象 `(p,g)` に対して:

```text
J_{D,χ,R}(p,g) :=
  (p, χ(p,g), R_{p,χ(p,g)}(D_p(g)))
```

読み下すと:

1. `g` を active inference doctrine `D_p` に入れる。
2. 得られた behaviour / dynamical process に時間 `χ(p,g)` を割り当てる。
3. CPS 実現 `R` により、時刻 `χ(p,g)` の `p`-typed α-twisted CPS object へ送る。

### 6.5 `J` の射写像

射 `(φ,u): (p,g) -> (q,h)` に対して、まず基底射を:

```text
(φ, χ(g) <= χ(h)): (p,χ(g)) -> (q,χ(h))
```

へ送る。このために必要な第一条件は:

```text
χ(g) <= χ(h)
```

つまり `χ` は射に沿って時間を逆行させてはならない。これが満たされない場合、`J` は全域関手ではなく、chronological subcategory 上の部分関手になる。

ファイバー射は:

```text
J(φ,u):
  R_{p,χ(g)}(D_p(g))
    ->
  (φ, χ(g)<=χ(h))^* R_{q,χ(h)}(D_q(h))
```

として定義する。

この射は次の合成として得る。

```text
R(D_p(g))
  --R(D(u))-->
R(D_q(h) pulled along φ)
  --τ-->
(φ, χ(g)<=χ(h))^* R(D_q(h))
```

ここで `D` が indexed functor であることにより `φ` 方向の自然性が与えられ、Paper II の `τ` が時間方向の輸送を与える。

## 7. 射の保存条件

`J_{D,χ,R}` が通常の関手、または弱い意味での pseudo / lax functor として立つには、少なくとも以下を満たす必要がある。

### J0. 時間単調性

任意の射 `(φ,u): (p,g)->(q,h)` について:

```text
χ(g) <= χ(h)
```

これがないと、domain の射を `Poly × T` 上の射へ送れない。

### J1. 恒等射保存

任意の対象 `(p,g)` について:

```text
J(id_p, id_g) = id_{J(p,g)}
```

ただし CPS 側の `τ_{α(t)->α(t)} = id` は Paper II §4.3.5 の擬関手条件に依存する。

### J2. 合成保存

二つの射

```text
(p,g) --(φ,u)--> (q,h) --(ψ,v)--> (r,k)
```

について:

```text
J((ψ,v) ∘ (φ,u)) ≅ J(ψ,v) ∘ J(φ,u)
```

等号ではなく `≅` とする。理由は、Paper II 側の時間輸送が

```text
τ_{β->γ} ∘ τ_{α->β} ≅ τ_{α->γ}
```

という自然同型で与えられるからである。したがって現段階の `J` は strict functor ではなく、pseudo functor 候補として置くのが安全である。

### J3. Monoidal / compositional 保存

statistical game 側の合成・テンソルは、lens composition と fitness の加法で与えられる。CPS 側では、Markov kernel の合成、blanket の合成、α-twisted copy/del の合成へ送られる必要がある。

保存条件:

```text
J(g ⊗ h) ≅ J(g) ⊗_CPS J(h)
J(g ; h) ≅ J(g) ;_CPS J(h)
```

ここで `⊗_CPS` と `;_CPS` は未定義なので、次に構成すべき対象である。

### J4. Fitness / free-energy 保存

statistical game の fitness / loss function は、CPS 側では VFE / EFE / precision update として読まれる必要がある。

弱い保存条件:

```text
loss(g) decreases
  =>
α/π precision channel in J(g) is recovered or stabilized
```

強い保存条件:

```text
F_CPS(J(g)) = F_FEP(g) + boundary_residue(p,t)
```

ここで `boundary_residue(p,t)` は、CPS が FEP より余分に持つ blanket 生成条件・α<0 セクター・相転移面を表す剰余である。剰余が 0 になる局所扇区が、従来の FEP と一致する候補になる。

### J5. Blanket 生成保存

FEP 側は Markov blanket を前提する。CPS 側は blanket の生成条件を持つ。

したがって `J` は次を満たす必要がある。

```text
if g has interface p and D(g) is active-inference-realizable,
then J(g) has B(X,t) generated by CPS Face / α-twisted Markov structure.
```

これは最重要条件である。ここが通れば、「FEP は blanket を前提するが、CPS はその前提を生成する」と言える。

### J6. 特異ファイバー制限

Paper II では `α = 0` で Markov blanket 構造が退化する。

したがって通常の関手としては:

```text
J は α(t) > 0 の開区間上で定義する
```

または、より野心的には:

```text
J は α=0 を特異ファイバーとして持つ stratified / partial functor
```

として定義する。

安全な初稿では前者を採る。α=0 横断を含めると、CPS の強みは出るが、関手性の証明が一段難しくなる。

### J7. U⊣N 回復保存

`J` が忘却論の統合関手であるためには、単に FEP を CPS へ翻訳するだけでは足りない。U⊣N の回復フィルトレーションを保存する必要がある。

要求する比較射:

```text
ρ_i: J ∘ N_i^FEP  =>  N_i^CPS ∘ J
υ_i: U_i^CPS ∘ J  =>  J ∘ U_i^FEP
```

少なくとも次の対応を持つ。

| 層 | 保存されるべき構造 |
|:---|:---|
| `N_sensory` | Bayesian lens の Put / sensing が CPS の感覚入力回復へ送られる |
| `N_arrow` | stochastic map / Markov kernel が CPS の射として保存される |
| `N_compose` | game composition が Markov kernel / blanket composition へ送られる |
| `N_depth` | hierarchy / string diagram が CPS の自然変換層へ送られる |
| `N_precision` | free-energy objective が α/π precision channel へ送られる |
| `N_causal` | action / policy が intervention / causal recovery へ送られる |
| `N_context` | polynomial reindexing が `Poly × T` 文脈回復へ送られる |
| `N_adjoint` | FEP-as-adjoint 候補が U⊣N の随伴回復へ送られる |
| `N_self` | meta-agent / structure-changing agent が CPS 自己関手へ送られる |

この条件は「FEP 全体の再導出」の本体である。

## 8. 現時点の未解決点

1. `R` の構成が未定義である。Smithe の behaviour / Markov process を CPS の `α`-twisted Markov kernel へ送る実現関手が必要。
2. `χ` の自然性が未証明である。game morphism が本当に時間単調性 `χ(g)<=χ(h)` を持つかは、学習過程の向きに依存する。
3. `C_CPS^p(t)` は新規定義である。Paper II には `C_CPS(t)` はあるが、polynomial interface で型付けしたファイバーはまだ構成されていない。
4. `⊗_CPS` と `;_CPS` の定義が必要である。ここは Smithe の monoidal structure と Paper II の α-twisted Markov composition の照合になる。
5. `N_adjoint` は未証明である。外部 SOURCE でも FEP が doctrine の随伴になる方向は ongoing research とされているため、ここは主張ではなく研究命題に留める。

## 9. 次の局所定理候補

**定理候補 J-1 (well-typedness).**
`D`, `χ`, `R` が与えられ、`χ` が domain の射に沿って単調であり、`R` が α-transport と polynomial pullback に自然であるなら、`J_{D,χ,R}` は `∫_Poly PSGame_P` から `∫_{Poly × T} CPS^*` への pseudo functor を定める。

**定理候補 J-2 (FEP 局所扇区).**
`α(t)>0` かつ `boundary_residue(p,t)=0` の局所扇区では、`J` は FEP の active inference dynamics を CPS の α-twisted Markov dynamics として回収する。

**定理候補 J-3 (忘却論再導出).**
`J` が J7 の比較射 `ρ_i`, `υ_i` を全 N-Series 層で持つなら、FEP の perception / planning / action / free-energy minimisation / meta-agent は、U⊣N の回復操作として再導出される。
