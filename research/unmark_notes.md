# 研究ノート：AOU 関係式から無標識 Abel 圏へ

2026-11-18 / unmark-v8。まず `00_research_plan.md` を参照する。公表可能な証明はすべて `papers/nc-cubic-unmark.tex`（`papers/sections/` を入力）にあり、ノートには再研究に必要な障害、区別、具体例だけを保持する。

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

## 線束分類の現在有効な入力と障害

- 内在的証明は `line_bundle_classification.tex`。非零射の単射性、End=C、負のH自己Hom消滅、Ext²自己消滅、χ=1判定を別々に示す。負の自己Homは、O0の負twistからの単射と二次成長を使う。E自身のAZ豊富性を仮定していない。
- 数値的欠損 n=D²/2−ch₂(E) はRR表示の下で非負整数、Ext¹(E,E)=2n。可換の `L⊗I_Z` では n=length Z。I_pはrank1,c1=0でもExt¹次元2なので、rankとc1だけでは線束を判定できない。
- 同一数値的線束類の一意性には交差Ext²を消す必要がある。(EP)を仮定すると、非零 `F→H^{-1}E` の余核の次数は同次数なら−3となり矛盾。χ(E,F)=χ(F,E)=1から両向きの単射、End=Cから同型を得る。**(EP)は数値Euler行列だけでは証明していない。**
- Rains2019 Cor.7.10は全因子類の線束存在。Prop.10.13はrank1tf+χself1と線束の同値。rationalの場合同じc1の線束は一意。非有理quasi-ruledではPic0 torsorが残るので、分類をそのまま一般化しない。
- Rains模型でQ=−Kがnef cone内部なら、Prop.9.7とThm.9.10から各線束の切断数とAZ豊富性が従う。Cがsmooth connectedかつQ²=3の範囲では `thm:rains-gk-filtration` がGK条件との一致を証明する。一般の数値的AOU heartへは無条件に拡張しない。線束twistは異なる標識付き模型へのexact Morita同値であり、同じ模型のtensor自己同値ではない。
- AOU/OU p.8の明示的比較は導来同値。反標準制限が線束であることを使ったexact比較は `cor:aou-rains-exact-region` にある。C smooth、Q ample、η非torsion、Rains模型との反標準データの比較、right noetherianを明示する。この範囲外では導来同値をt-exactと読み替えない。
- 形式Artin変形では古典的線束の各持上げは一意だが、全整数Dについての開条件の可算交叉が非空Zariski開とは限らない。各クラスの局所存在から全クラス同時の代数化を推測しない。
- 調べる集合は Ω_A={D : 数値類v_Dを持つrank1tf対象が存在}。一意性の仮定下でLine(A)≅Ω_A、HでD→D−K。Line_adm=Lineの証明とAut_ex軌道の計算は別問題。

## 反標準曲線による橋渡しとその境界

証明は `anticanonical_heart_bridge.tex` に集約する。

**GK filtration:** Q=−K がnef内部、Q²=3、C smooth connected のRains模型で、rank0,c1=0層はχが正整数の長さ関数になる。逆にsimple MのθM→Mは零または同型なので数値的0次元。rank0層はdegreeでmod A0有限長。正rank層のtorsion-free商Nは N⊃θN⊃θ²N⊃…、各商degree=3rank N>0ゆえmod A0有限長でない。これでA0=T0、A1=T1、rank1定義一致。この議論はηtorsionでも成立する。

**制限による検出:** η=det(Li*[pt])∈Pic0(C)をQと混同しない。Rains §7 p.92のdeterminant-of-restrictionで定義される。η非torsion時、i*M=0ならθM→Mがepi。そのkernelのdegree=−3r(M)とχkernel=−degree(M)からMは数値n[pt]でLi*M=0。しかしdet=η^nなのでn=0、M=0。Cartier三角のcohomologyからLi*Eがdegree0ならEもdegree0。i*は零対象を検出するが、射に忠実やexactという主張ではない。

**例外対象→線束:** Li*Eが線束でE例外なら、Eは層でrank1。最大torsion Tのi*Tが線束i*Eに埋め込まれるが、rank0なので零。上の検出でT=0。Rains判定から線束、GK一致からintrinsic許容対象。mutation像を古典的記号O(D)だけで層と見なす誤りを避けられる。

**helix再構成:** AOU §9のτ7の制限σ7は式(9.53)で九線束。これらを上記Rains模型で実現できれば、全helixは線束。有限個のresidue classごとに負θ列のacyclic生成を使い、Polishchukのample sequence再構成でcoh X≃cohproj A。right noetherianならqgr A。指定したfoundationだけでなく全End代数の同定を使って標準tilting同値に一致することを確認する。単なるderived equivalenceの存在だけでは足りない。

**残る模型比較:** AOU/VdB blowupとRains模型の同定、および反標準データとの整合、translation sigmaとηの対応を全点で検証したわけではない。従って本稿のAOU系は適用条件付き。非torsion集合がZariski開と主張しない。相対的な線束のGm gerbeと無標識降下は別問題。

**有用な反例:** 可換cubic上でp∉CならLi*O_p=0、O_X⊕O_p[1]は層でなくても制限O_C。この複体はexceptionalでないので「exceptionalなら失敗」という反例ではないが、非torsionなしの一般的層検出が成り立たないことを示す。Li*自体も一般の層をdegree0に保たない。

## 次の具体的な入口

AOU §9のτ7の各制限線束とRains側のrestriction dataを対応させる。両構成でcentral Cartier三角が一致し、AS代数がnoetherianである範囲を一次文献から確定する。そこで既に証明したexact再構成を適用し、全弱標識集合を固定した上でAut_ex軌道を計算する。torsionの場合はC外で見えない有限長対象を制御する別条件を探す。

## 一次資料

- Abdelgadir–Okawa–Ueda, *Compact moduli of marked noncommutative cubic surfaces*, arXiv:2404.00175v1, Theorems 1.1/1.2, §§4, 7, 9. https://arxiv.org/pdf/2404.00175
- Okawa–Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, arXiv:2508.04986v1, Definition 1.1 and §3. https://arxiv.org/pdf/2508.04986
- De Deken–Lowen, J. Noncommut. Geom. 5 (2011), 477–505, Thms 4.5, 5.13, 5.15, DOI 10.4171/JNCG/83. https://ems.press/content/serial-article-files/30497
- Karpov–Nogin, *Three-block exceptional collections over Del Pezzo surfaces*, Izv. Math. 62 (1998), 429–463, DOI 10.1070/IM1998v062n03ABEH000205
- Toda, *Deformations and Fourier–Mukai transforms*, JDG 81 (2009), 197–224, arXiv:math/0502571.
- Bondal–Orlov, *Reconstruction of a variety from the derived category and groups of autoequivalences*, Compositio Math. 125 (2001), 327–344, arXiv:alg-geom/9712029.

新しい数値 E6 の主張の外部文献における優先権は未確認。今回の手計算とスクリプトは数値結果を検算するものであり、幾何的 heart の認識の証明ではない。

### 線束分類の一次資料と参照箇所

- E. M. Rains, *The birational geometry of noncommutative surfaces*, arXiv:1907.11301v1 (2019), https://arxiv.org/abs/1907.11301v1 。Definition 5.1とpp.67–68（線束とtwist）、Corollaries 7.9–7.10（存在・数値類・Pic0）、Corollary 7.13（RR）、Proposition 9.7（線束間Ext消滅）、Theorem 9.10（acyclic生成）、Lemma 10.11 / Corollary 10.12 / Proposition 10.13（rank1と線束判定）。この文献のrankとGK条件の比較は本稿 `thm:rains-gk-filtration` の範囲で証明した。追加参照: Lemma7.2、Props7.5/7.6/7.19、Cor7.15、Prop7.24直前、Thm9.10、Cor9.11。
- E. M. Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2 (2022), https://arxiv.org/abs/2107.13540v2 。Proposition 5.14、p.42（例外的torsion-free層の同一K0類での一意性）。Proposition 5.16のDVR延長を一般AOU模型へ無条件には適用しない。
- Okawa–Ueda arXiv:2508.04986v1 p.8、Theorem 6.4直前の導来同値を本文とページ画像で確認。Introduction p.2の「blowupである」との記述と、heart間のexact比較を本稿で独立に確認したことを区別する。

Rainsの上記各命題は一次資料の本文で確認した。大型PDFのWeb画像取得は失敗したため、図表を使った確認はしていない。既知結果の全証明の再証明、外部査読、新規性の網羅的照合は未完。内在的補題と一意性の本稿証明は仮定ごとに点検し、数値恒等式は `verify_line_bundle_numerics.py` で独立に検算する。

- A. Polishchuk, *Noncommutative Proj and coherent algebras*, Math. Res. Lett. 12 (2005), 63–74, arXiv:math/0212182. Lemma2.1（生成とprojective sequence）、Theorem2.4（ample sequenceのcohproj再構成）、§1（noetherian時のqgr）。公開一次本文: https://intlpress.com/site/pub/files/_fulltext/journals/mrl/2005/0012/0001/MRL-2005-0012-0001-a007.pdf 。

今回の主要入力は上記一次資料の本文で照合し、AOUはHTML式(9.19),(9.44),(9.53),Thm9.4、OUはp.8画像も確認した。RainsとPolishchukのWebスクリーンショット取得は失敗し、本文を使用（図表に依存しない）。新しい推論の仮定・符号・cohomologyの向きを点検した。全先行証明の再証明、外部査読、網羅的新規性判定は未実施。
