# 現行研究ノート：AOUから無標識Abel圏へ

2026-11-17 / unmark-v2。再開時は`00_research_plan.md`を最初に読み、証明は`papers/sections/marking_forgetful.tex`と`papers/sections/aou_to_unmarked.tex`で参照する。

## AOUで現在解決した部分と解決していない部分

関係式のパラメータは `(P²)^9`、矢スカラー変換は `(G_m)^18`。AOU §5.1のrelation stackは`[(P²)^9/(G_m)^18]`。これはAOU §5.4のtoric GIT schemeとは違う。AOU Theorem1.2の滑らかな可換marked cubicの埋込みはdense torus内の局所閉埋込みであり、全体の同一視ではない。Theorem1.1は楕円decupleとの双有理対応で、全点でのAS-regular性を意味しない。特にGIT境界のS-同値類が同じAbel圏を与えるかは未確認。

幾何的標識helixを持つカテゴリー的開部分について、標識選択のgroupoidから弱標識 `(A,O)`、さらに `A` へ忘れる。`R_Q^cat`と書くものは現在**証拠付きfibered groupoid**であり、AOU GIT内の開substackであると証明したわけではない。`M_Q^chi`から無標識moduliに写す主張は、十分なカテゴリ化・fpqc降下・S-同値不変性を確認してからでなければならない。

可換 locus はGabriel再構成からexact圏の同値類で`W(E6)`標識変更の商と同一視できる。標識選択はXを固定すると`W(E6)` torsor、自己同型はその上で自由に作用する。一般Xの標識同型類は51840であり、特別Xは51840/|Aut X|。これはAOU toric variety全体でW(E6)が正則作用することを意味しない。

形式方向ではピカール障害と慣性を分ける。`Pic(X)=Z^7` は可換圏のexact自己同値に実在するが、非可換固定一次fiberのexact自己同値として持ち上がるのは非常に一般には `Z[-K]` のみ。固定Abel圏の許容構造対象は各線束から持ち上がるので、軌道集合は`Z^6`。九対象標識を各線束捩れへ持ち上げる**相対仮定**を満たすなら、標識忘却の幾何的fiberもこの集合へ全射をもつ。従って「W(E6)だけでunmarkedへ行く」という単純な商ではfiberを取り違える。これをGIT商の無限fiberと読み替えてはいけない。

無標識stackは可換点でPicard無限離散慣性を持つ。HH¹=0とauto-equivalenceの変形制御が忠実なら、locally finite typeな代数的1-stackの対角がqcであることはできない。この議論は*粗* moduliの非存在でも、全ての代数stackの非存在でもない。scalar 2-morphismのrigidificationを常に明記する。

## 計算・変形の有用な具体例

滑らかな三次曲面 `X=V(x³+y³+z³+txy+t³)`, `C={t=0}`。平面変形`t=eps z`は平面楕円曲線の式に`eps xyz`を加え、Jacobian環`C[x,y,z]/(x²,y²,z²)`の次数3に非零元を与える。したがって接続写像rank1、`H¹(Ω¹)->H¹(T)`のrank4 witnessとなる。証明は主論文に置く。

Picard格子`Λ=Zh + sum Ze_i`はsignature(1,6)、`K=-3h+sum e_i`、`Q=K^⊥`はE6根格子。`Λ/(Q+ZK)=Z/3`、`Λ/ZK≅Q^∨`。root translationとweight-lattice型の全Picard shiftを混同してはいけない。`delta_pi(K)=0`（局所`π^sharp(dlog s)`のČech表示で分かる）。rank一般4から整数kernel rank3とは結論できない。

非常に一般の整数核の証明は、marked cubicとsmooth anticanonical sectionの既約パラメータ上で全kernel共通部分Nを考える。W(E6)に安定、CKを含み、Q複素反射表現既約かつrank4 witnessがあるのでN=CK。各非K整数Dの零点は真の閉集合であり、その可算個の外では整数kernel=ZK。詳しい証明は `thm:very-general-picard-kernel`。

## 失敗しやすい推論と調査課題

- AOU relationのderivedカテゴリが等価であるだけでは、**元のAbel heartが等価**とは言えない。t-exact同値が必要。
- 同じAbel変形へ線束Lが対象として持ち上がる（Ext¹=Ext²=0）ことと、tensor Lが固定変形の自己同値に持ち上がることは違う。後者の一次必要条件は`delta_pi(L)=0`。高次での十分性未証明。
- relative Serre, perfect base-change, AZ ampleness, rank-one torsion-free, exceptionalityの開性は**証明対象**。一般のdg変形すべてに自動的だとしない。
- AOU標準helixがすべてのAS-open点で幾何的に一意・完全であること、numerical markingからgeometric helixが復元できること、W作用がGIT境界へ延長することは未証明。
- abstract Picard商・Weyl商・GIT軌道商は異なる同値関係。安定化群・慣性の段階も区別する。

## 一次文献と正確な参照

- AOU, *Compact moduli of marked noncommutative cubic surfaces*, arXiv:2404.00175 v1, Introduction, §§4.6,5.1–5.4, Thms 1.1,1.2, §9 Theorem 9.4. https://arxiv.org/pdf/2404.00175
- Okawa–Ueda, *Marked Artin--Schelter surfaces of del Pezzo types*, arXiv:2508.04986 v1, Definition1.1, Theorem6.4. https://arxiv.org/pdf/2508.04986
- Gabriel, *Des catégories abéliennes*, Bull. Soc. Math. France 90 (1962),323–448, DOI:10.24033/bsmf.1583. Exact coherent category reconstruction.
- Toda, *Deformations and Fourier–Mukai transforms*, JDG81 (2009),197–224, arXiv:math/0502571. HKR/Fourier–Mukai作用。
- De Deken–Lowen, *Abelian and derived deformations in the presence of Z-generating geometric helices*, JNCG5 (2011),477–505, DOI:10.4171/JNCG/83, Thms4.5,5.13,5.15.
- Bondal–Orlov, *Reconstruction ... autoequivalences*, Compositio125 (2001),327–344, arXiv:alg-geom/9712029, derived and exact autoequivalences.
- Dolgachev–van Geemen–Kondō, *A complex ball uniformization ...*, J. reine angew. Math. 588 (2005),99–148, §§2.5–2.6, DOI:10.1515/crll.2005.2005.588.99, marking moduli and W.

## 未解決核と着手

優先(1) AOU quiver relation上で認識可能なAS-openとその相対カテゴリー構成を具体化。(2) 特に`HH²=H¹(T)⊕H⁰(-K)`の全8方向のrelation変形が許容になっているか比較。(3) AOU relation tupleの座標をPicard shearで明示変換する。(4) GIT S-同値・降下・相対慣性の検証。(5) full LaTeXコンパイルと数学的一次資料チェックを完了。ambientの認識は別リポジトリ`nc-cubic-ambient`。