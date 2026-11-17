# 研究ノート：AOU 関係式から無標識 Abel 圏へ

2026-11-18 / unmark-v6。まず `00_research_plan.md` を参照する。公表可能な証明はすべて `papers/nc-cubic-unmark.tex`（`papers/sections/` を入力）にあり、ノートには再研究に必要な障害、区別、具体例だけを保持する。

## 相対 AS locus と形式 chart の区別

- AOU Proposition 7.3 の許容楕円 decuple 8 次元 fine moduli は既約。Theorem 1.1 の birational な相互逆写像の定義域を交わらせると、稠密トーラス中の非空開 `U_ell` で各幾何学的点が AS-regular Z 代数を持つ。§7 Lemma 7.4 と OU の構成が入力。これは **既知結果の直接の帰結** であり、本研究の新規な構成ではない。必要なら開集合を縮める。全GIT境界の heart、弱標識付き定義の rank-one 条件、相対 algebraic stack と降下はなお未証明。
- 滑らかな可換点の形式 completion は De Deken--Lowen 5.15 と AOU有限代数の形式完備性により `Def_ab(Qcoh X)` に一致する（本稿証明、DDLに依存）。Grothendieck Abel heart の Artin 変形があることから、relative Serre `H=S^{-1}[2]` がすべてのArtin底で t-exact であると飛躍しない。標準 `Z` generating helix の相対条件をもう一度確認する。
- 有向三層 quiver の全 `R_Q=(P²)^9` 上で rank45・gldim2 の有限代数と smooth proper `Perf(B_r)` がある。有限代数の標準 `mod B_r` heart は三次曲面 `coh X` と Abel 同値ではない。普遍導来圏だけから目的の t-structure を選ぶことはできない。

## 数値的 E6 と境界判定

- 9射影の Euler 行列は規約に応じて `C` または `C^T`、`C=[[I,0,0],[J,I,0],[2J,J,I]]`（I=3次単位行列、J=3次全1）。数値 Serre `S=C^{-1} C^T` の Jordan 型は `(3,1^6)`、`rank(S-I)=2`、`rank(S-I)^2=1`、`(S-I)^3=0`。`ker(S-I)` rank7 の χ の根基は1次元、商は判別式3の E6 正定値根格子。証明は `thm:aou-numerical-E6`、計算は `verify_aou_relation_tangent.py`。
- AOU の矢基底変換 `G_Q=(G_m)^18` は原始冪等元を固定するので K0 の基底と E6 に自明に作用。古典的な W(E6) の非自明な標識変更は、この群作用では表せない。**数値的標識を固定すること**と**幾何学的 helix を標識すること**は違う。
- Hochschild公式：支持行列階数 ρ に対し `HH1=10−ρ`, `HH2=18−ρ`。全係数非零は `(0,8)`、九つの単項式関係式は `(10,18)`、よって後者は前者と導来 Morita 非同値。Euler/Serre/E6 だけではこの差が見えない。ただし、単項式境界に三次曲面型 heart が絶対に存在しないという結論ではない。
- 境界点 `(u0,z0)` の一関係式だけ `[1:0:0]`、他の八つは全係数非零としても ρ=10。証明は二部グラフ K3,3 の1辺を除いても連結という事実。したがって `HH1=0` という条件だけでも AS の定義域は特徴付けられない。二項式 `[1:1:0]` でも同様にρ=10。

## 無標識ファイバーと Picard 作用

- 可換 smooth locus の標識は W(E6)-torsor（|W|=51840）であり、Gabriel 再構成で exact coh 同値は X の同型を意味する。これは可換点についての完全な比較。
- 固定圏で線束 L が平坦に持ち上がることと、それを表す tensor 自己同値が同じ非可換 fiber に持ち上がることは異なる。一次障害は `δ_π(L)=H¹(π^sharp)c₁(L)`。X の Poisson 零因子が smooth のとき複素 rank 3または4、一般4。非常に一般の整数核は ZK_X（本稿に証明・条件を参照）、pointing 同型類集合は Pic/ZK≅Q(E6)^∨≅Z^6。
- Picard shear は標識付き形式チャート上の作用の微分だが、高次座標式は未計算。一次線形空間 `H¹T_X⊕H⁰(-K_X)` の Picard 不変式は Poisson4方向だけ。GIT粗商全域への作用は確立していない。形式作用の粗商と relation torus の G_Q 商を同一視しない。

## 次に行う証明の具体的な入口

1. AOU §7 の普遍 decuple から AS-regular Z 代数の相対構成がどの程度底変更に両立するか、OU 定理を正確に照合。相対 `qgr` と Serre/heart/t-exact を同時に確認する条件を抽出。
2. 開 `U_ell` で異なる decuple が exact 同値な unmarked Abel 圏を与える具体的同値の構成または障害。標準 helix の変更群と Picard/Aut の区別を追跡。
3. `HH1=0` の境界で AS heart が残る例と残らない例を探す。有限Bの数値 K0 と HHだけでは判定不能なので、Z-generating helix、AZ豊富性、point modules の開条件を扱う。
4. 相対Picardの二次以上の形式変形をTodaのMorita作用と比較。規約と自己同値の慣性を明示。

## 一次資料

- Abdelgadir–Okawa–Ueda, *Compact moduli of marked noncommutative cubic surfaces*, arXiv:2404.00175v1, Theorems 1.1/1.2, §§4, 7, 9. https://arxiv.org/pdf/2404.00175
- Okawa–Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, arXiv:2508.04986v1, Definition 1.1 and §3. https://arxiv.org/pdf/2508.04986
- De Deken–Lowen, J. Noncommut. Geom. 5 (2011), 477–505, Thms 4.5, 5.13, 5.15, DOI 10.4171/JNCG/83. https://ems.press/content/serial-article-files/30497
- Karpov–Nogin, *Three-block exceptional collections over Del Pezzo surfaces*, Izv. Math. 62 (1998), 429–463, DOI 10.1070/IM1998v062n03ABEH000205
- Toda, *Deformations and Fourier–Mukai transforms*, JDG 81 (2009), 197–224, arXiv:math/0502571.
- Bondal–Orlov, *Reconstruction of a variety from the derived category and groups of autoequivalences*, Compositio Math. 125 (2001), 327–344, arXiv:alg-geom/9712029.

新しい数値 E6 の主張の外部文献における優先権は未確認。今回の手計算とスクリプトは数値結果を検算するものであり、幾何的 heart の認識の証明ではない。
