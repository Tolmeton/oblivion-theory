# E-XIII-C3-01 Result

**日付**: 2026-04-26
**状態**: Round 1 paper-probe level 完了
**判定**: C3 は D2 修正後にのみ生きる。定理昇格なし。

## 1. Kernel Result

D2 の直読は強すぎる。

> Einstein tensor = Face Lemma 2-simplex area / defect.

Round 1 では、この読みを raw defect として棄却する。Schwarzschild exterior separator が理由である。vacuum は Riemann curvature を非零にできる一方で、`T_{μν}=0`, Ricci = 0, `G_{μν}=0` になりうる。したがって raw geometric defect を Einstein tensor だけに担わせることはできない。

救済された読みは次である。

> Riemann/holonomy = raw defect; Ricci/scalar = contracted defect; Einstein tensor = conserved coupling projection.

この読みなら、vacuum curvature を保持しつつ、`G_{μν}` に container/content coupling の役割を残せる。

## 2. C3 状態

| dimension | before Round 1 | after Round 1 |
|:---|:---|:---|
| O1 type assignment | direction/comparison/transport で安定 | 維持 |
| O2 defect | 直読が強すぎる / 曖昧 | Riemann -> Ricci/scalar -> Einstein projection へ再配置 |
| O3 closure | open | 次の中心実験 |
| O4 coupling | open | O3 に依存 |
| Kalon status | near / skeleton | near / skeleton のまま。ただし混線は減った |

## 3. 何が変わったか

**保持**

- C3 は Paper XIII の decisive shock point のまま。
- O1 は有効。3 role は direction / comparison / transport。
- C2 は錨のまま。container/content asymmetry があるから `G_{μν}` と `T_{μν}` が効く。

**修正**

- D2 は Einstein tensor を raw face defect として提示してはいけない。
- defect ladder を明示する: raw local defect -> contraction -> conserved projection。
- Bianchi identity は side note ではなく O3 の中心に置く。

**棄却**

- 「GR 側にも3つあるから Face Lemma」という argument は採らない。
- C1/C4 で C3 を救わない。
- Round 1 output を closure と呼ばない。これは修理済み protocol である。

## 4. Paper XIII への編集契約

次の実験までは、本文の大規模 polish はしない。安全に許される note は一つだけ。

> D2 is currently a skeleton. The next version should distinguish raw curvature defect from the divergence-free projection that couples to content.

もし今編集するなら、対象は §8 のみ。

| section | allowed change |
|:---|:---|
| §8.2 D2 | direct "Einstein tensor = face area" を D2' ladder へ置換 |
| §8.2.1 O2 | Riemann/holonomy を raw defect として追加 |
| §8.2.1 O3 | Bianchi identity を次の formal closure gate として前景化 |
| conclusion | 強化しない |

## 5. 次実験

**E-XIII-C3-02: Bianchi as Face-side closure**

問い:

contracted Bianchi identity `∇^μG_{μν}=0` を、stress-energy conservation を後から輸入せずに、Face Lemma 側の closure / syndrome-conservation condition として翻訳できるか。

pass condition:

Face 側 closure rule が、なぜ conserved projection が raw Riemann curvature ではなく `G_{μν}` なのかを説明する。

fail condition:

`∇^μG_{μν}=0` を GR 事実として反復するだけで Face 側の役割を与えられないなら、C3 は O3 で resemblance に留まる。

## 6. Round 1 Verdict

**判定**: support after revision.

C3 は閉じていない。しかし死んでもいない。Round 1 が露出した正しい圧点は、Paper XIII が `G_{μν}` に defect 全体を背負わせてはいけないという点である。曲率を raw defect、contracted defect、conserved coupling projection に分けること。この分割が、resemblance から correspondence へ進む次の道である。
