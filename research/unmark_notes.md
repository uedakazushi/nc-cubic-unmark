# 研究ノート：AOU relation moduli と無標識 Abel 圏

2026-11-17 / unmark-v3。研究再開は `00_research_plan.md` から。証明は主論文の `papers/sections/marking_forgetful.tex`、`papers/sections/aou_to_unmarked.tex`、`papers/sections/picard_invariants.tex` に置く。本ノートはそれらと重複しない判断・具体例・障害・将来の着手方法を保持する。

## AOU moduli で区別すべき層

AOU v1 の relation stack は `[(P²)^9/(Gm)^18]`（§5.1, (5.3)）、その線形化による粗商は8次元toric variety（§5.4）、potential stackへの関係式stackの開埋込みは Proposition 5.1（§5.3）。これらは **AS-regular Z-algebra が現実に再構成できる相対圏的表示** とは異なる。AOU Theorem 1.1 は admissible elliptic decupleとrelationの双有理比較、Theorem 1.2 は可換marked cubic moduliのdense torusへの局所閉埋込み。GIT境界を一律に圏へ送る操作は未証明。

可換smooth cubic Xの通常のmarkingはW(E6)-torsor（|W|=51840）。Gabriel再構成でcoh X≃coh Yのexact同値ならX≅Y。幾何学的同型類レベルで可換locusの忘却はW商、Aut(X)を考慮すると標識の同型類数51840/|Aut(X)|。一般の非可換開部分に有限W商を無条件に拡張しない。

「圏的AOU標識選択」の増補dataの群oidと、矢基底で割った relation stack、さらに GIT粗商の同型類は異なる。`thm:aou-infinite-relative-fibre` の無限性は標準helixと相対heart持上げの条件を入れた**増補圏的ファイバー**の主張であって、relation GIT scheme の幾何学的ファイバーの主張ではない。共通line bundle twistは固定可換fiberの有限End代数に影響しない（`prop:common-tensor`）が、同じ非可換一次fiber上での自己同値として持ち上がるとは限らない。

## Picard shear の具体例と非分離障害

基準X: smooth cubic `F=x³+y³+z³+txy+t³=0`, smooth anticanonical elliptic curve `C={t=0}`。平面の一次変形`t=ε z`はHesse cubicに`εxyz`を追加し、Jacobian algebra `C[x,y,z]/(x²,y²,z²)` の3次に非零。これが`δ_π:H¹Ω¹→H¹T`のrank4 witness。 `π∈H⁰(-K)` を変えるとrank4は非空Zariski開。

`Λ=Pic(X)=Z⁷`、`Q=K^⊥=E6 root lattice`、`Λ/(Q+ZK)=Z/3`、`Λ/ZK≅Q^∨=Z⁶`。`δ_π(K)=0` は局所 `π^sharp(dlog s)` のČech coboundary。非常に一般の `(X,π)` の整数核はZKであり、固定一次非可換Abel変形のpointing orbit集合はZ6（証明と相対条件は主論文）。complex kernelは一般に3次元なのに整数核がrank1となる点が重要。

**今回得た理論的障害**: `E=V⊕P`, `V=H¹T_X≅C⁴`, `P=H⁰(-K_X)≅C⁴`、`r_L(ξ,π)=(ξ+δ_π(L),π)`。一般rank4のπでは `δ_π(Λ)` の複素線形包はV、整数平行移動群のZariski閉包はV全体。したがって

`C[E]^Λ=C[P]`、`C(E)^Λ=C(P)`。

固定π≠0の一般位置では無限のPicard shear orbitがV-fiber内でZariski稠密。にもかかわらずπ=0では全shearは恒等。よってaffine不変式商は可換方向Vを丸ごと潰す。さらに任意の分離有限型 algebraic space YへのPicard不変正則写像E→YはPを通る。証明は `thm:picard-linear-invariants` と `cor:separated-linear-quotient`。これは8次元の**一次線形表現についての厳密な代数定理**、大域AOU GITを計算したものでも無標識粗moduli全域の非存在を証明したものでもない。この区別を必ず残す。

この現象は、無標識化を単純な有限W(E6)商や有限型分離粗商とみなす方針に構造的な障害があることを示唆する。正しい対象は2-stackあるいは非分離な商stackの可能性があり、相対AS-openを確定してから考える必要がある。

## 次に解くべき具体問題

1. AOUの relation stack の（4.12）(4.13)と§9のAS条件を用いて、smooth marked cubic点の形式8次元近傍でAS正則なZ代数/heartを証明する。または十分条件を明示した反例/証明を示す。
2. DDL Theorems 4.5,5.13,5.15 を使い、固定可換標識のもとでrelation変形の全8方向と `HH²(X)` の局所的同一視を検証する。変形を比較する際、weak Oを固定したものとunmarked Aを分ける。
3. `r_L` をAOU torusの正確な形式近傍の座標で計算し、非線形高次での曲率/障害を調べる。一般Picard群を固定非可換fiber上の自己同値群と混同しない。
4. AOU GITの半安定点でS-同値のrelationが非同値heartを持つ具体例があるか探索。常に同値ならその降下を検証。
5. 自己同値の慣性 `Pic(X)⋊Aut(X)` とscalar rigidificationを区別。`HH¹(X)=0`を用いる非準コンパクト対角の議論は変形制御に関する仮定付き。大域stackの代数性未証明。

## 先行研究（一次資料と適用範囲）

- AOU, *Compact moduli of marked noncommutative cubic surfaces*, arXiv:2404.00175v1, Theorems 1.1/1.2, §4.6, §5.1 Eq.(5.3), Proposition 5.1, §5.4, §9. https://arxiv.org/pdf/2404.00175
- O. De Deken, W. Lowen, *Abelian and derived deformations in the presence of Z-generating geometric helices*, J. Noncommut. Geom. 5 (2011), 477–505, Theorems 4.5,5.13,5.15. DOI:10.4171/JNCG/83.
- Y. Toda, *Deformations and Fourier--Mukai transforms*, J. Differential Geom. 81 (2009), 197–224. arXiv:math/0502571. Morita/Fourier–Mukai action on HKR components.
- P. Gabriel, *Des catégories abéliennes*, Bull. Soc. Math. France 90 (1962), 323–448, DOI:10.24033/bsmf.1583. Coh reconstruction.
- A. Bondal, D. Orlov, *Reconstruction ... and groups of autoequivalences*, Compositio Math. 125 (2001), 327–344. arXiv:alg-geom/9712029.
- S. Okawa, K. Ueda, *Marked Artin--Schelter surfaces of del Pezzo types*, arXiv:2508.04986v1, Definition 1.1 and Theorem 6.4. 部分の詳細な適用は今後さらに照合。
- I. Dolgachev, B. van Geemen, S. Kondō, *A complex ball uniformization of the moduli space of cubic surfaces via periods of K3 surfaces*, J. reine angew. Math. 588 (2005), 99–148, §§2.5–2.6, DOI:10.1515/crll.2005.2005.588.99.

新しい不変式定理の直接の先行優先権は網羅的に確認していない。証明は初等的な加法群平行移動とrank4を使用する。投稿時に既知のPoisson Picard Morita作用の不変式との比較を強化する。