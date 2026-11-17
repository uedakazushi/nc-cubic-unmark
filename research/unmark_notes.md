# 標識忘却の現行研究ノート

2026-11-17 / unmark-v1。研究再開時は `00_research_plan.md`、次に `papers/nc-cubic-unmark.tex` を読む。本ノートは公表用論文に重複する証明を省き、境界・未解決の問題・関連する計算だけを保持する。

## 標識忘却・構造対象の現在の結論

日本語の術語は標識（marking）・標識付き・弱標識付き・無標識・標識変更。標識忘却とambient射は別論文とする方向がよいが、現在の主原稿は両方の成果と証明を保持している。分割に際して標識忘却論文の定理にambientのAS正則性を無意識に加えないこと。


- 現行の弱標識付き公理は(A,O)をとり、H=S^{-1}[2]のt-exact性、AZ豊富性、三次曲面Hilbert値に加えてGabriel–Krullのrank-one torsion-free性（qO非零単純・A1からOへのHom消滅）とexceptionality（End(O)=k、Ext^{>0}(O,O)=0）を**独立に要求**する。ambientや一次生成性を仮定しない。圏論的な主定理と十分な証明は `papers/sections/marking_forgetful.tex` にある。

- 忘却は `M_AOU^adm -> C^w -> C^u`。固定圏上では許容九対象threadの選択群oid、許容構造対象の選択群oidとなる。圏の同定を忘れるとexact自己同値2-groupでのhomotopy quotientとなる。従ってPicard商と呼ぶときはraw 2-groupとスカラーrigidification、同型類集合の商を区別する。

- 可換滑らかな三次曲面Xでは許容構造対象EはL⊗I_Zとなるが、RRからχ(E,E)=1−2length(Z)、exceptionalityからZ=∅。従って線束Lだけが許容。自然同型で割ったexact自己同値はPic(X)⋊Aut(X)、pointedの選択商はBAut(X)。AOUのrelation algebra End(⊕E_i)は全対象の共通tensorで変わらず、relation GIT点をさらにPicで重複して割らない。

- 特殊ファイバーと同定したArtin flat Abel変形（相対Serre・perfect base change・heart保存を要求）では各線束と標準helixの持上げはExt¹=Ext²=0により一意。各標準標識の形式chartは同じweak deformationへ対応し、有限W(E6) torsorになる。全境界・非可換一般点における大域商は未証明。

- **新しい障害の公式**：u=(ξ,π)∈H¹(T_X)⊕H⁰(∧²T_X)、線束LのMorita同値による標識変更の一次変化は規約を除き (ξ,π)↦(ξ+δ_π(L),π)、δ_π(L)=H¹(π^sharp)c₁(L)。構造対象Lが圏の変形へ持ち上がることと、(-)⊗Lが**同じ変形**の自己同値へ持ち上がることは異なる。後者にはδ=0が必要。

- πの零因子Cが滑らかな反標準楕円曲線なら0→Ω¹_X→T_X→T_X|_C→0で、長完全列の階数は7−h⁰(T_X|_C)=3+r（r=0または1）。非空開でr=1：X={x³+y³+z³+txy+t³=0}, C={t=0}ではCの平面移動t=εzがJacobian環のxyzに対応しKS非零。従って一般にrank4。**反標準線束の方向はδの核**：局所Cの方程式s_iに対してπ^sharp(dlog s_i)は正則で、そのČech差がδ_π(O(C))。従ってroot格子Q=K^⊥へのδの制限は全Picに対して同じ階数、一般には4。非常に一般の(X,π)の整数kernelは下記の新定理で計算済み。高次障害は未計算。

- Pic(X) rank7、Q(E6) rank6、Pic/(Q+ZK)=Z/3、Pic/ZK≅Q^∨。AOU/OUのaffine Weyl translation QとPic全体を同一視しない。新しい計算スクリプト `computations/verify_marking_lattice.py` は72根、27線、E6判別式3とsmoothな例のJacobian確認をQQ上で行う。一次障害と相対降下の数学的証明はコードではなく本文にある。

## 非可換一次変形の整数Picard核と構造対象軌道

主論文の定理 `thm:very-general-picard-kernel` と系 `cor:first-order-pointings` に完全証明。

(1) 標識付き滑らかな三次曲面の既約moduli M^m は六本の順序付き斜交直線のblow-down（一般位置のP²六点）で記述される。W(E6)が標識を変える。一次資料：Dolgachev–van Geemen–Kondō, *A complex ball uniformization of the moduli space of cubic surfaces via periods of K3 surfaces*, J. reine angew. Math. 588 (2005), 99–148, §§2.5–2.6, DOI 10.1515/crll.2005.2005.588.99（著者公開PDF https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/cubic05.pdf、p.105を確認）。一次標識変更にはToda, *Deformations and Fourier–Mukai transforms*, JDG 81 (2009) 197–224, arXiv:math/0502571を参照。

(2) smooth anticanonical Poisson sectionを持つ標識付き pair空間P^mも既約。標準Picard格子Λ=I_{1,6}を自明化してΛ_C=C K⊕Q_C、Q=K^⊥=E6。全パラメータのδ核の共通部分NはW(E6)安定でCKを含む。WのQ_C上の反射表現は既約：任意の非零W安定部分が根と非直交なvを含むなら反射差から根を含み、その軌道72根はQ_Cを張る。非空開でδのrank4なのでNはΛ_C全体でなく、N=CK。ゆえに各D∈Λ\ZKの零点条件δ(D)=0はP^m上の真の閉部分集合。可算個のDを除外すると、非常に一般の(X,π)についてker(δ:Pic(X)→H¹(T_X))=ZK。これは単一のZariski開上での一様な主張ではない。

(3) Aut(X)=1の非常に一般な滑らかな可換三次曲面Xと、Poisson成分πが上の条件に入る許容一次Abel変形A_εを考える。特別fiberのexact自己同値はBondal–Orlovによりtensor L（非零shiftなし）。これが固定A_εへ持ち上がればδ_π(L)=0、従ってL∈ZK。逆に相対反Serre H=S_ε^{-1}[2]はt-exactで、特殊fiber上でtensor(-K)なので全ZKを実現する。各LはExt¹=Ext²=0により唯一の許容構造対象L_εへ持ち上がるため、同じA_ε上のpointingをexact自己同値で割った同型類集合はPic/ZK≅Q(E6)^∨≅Z^6。**同型類の集合の結果であり、2-groupの慣性や大域stackの無限成分を主張しない**。当然、全非可換変形や高次形式変形へ無条件には拡張しない。

(4) 計算資産：`computations/verify_marking_lattice.py` はE6の72根・27直線・判別式3・rank4 witnessに加え、単純反射による一根のWeyl軌道72個とQ上のrank6張りをQQで検算する。既約性は本文の反射による通常証明から従い、コードだけが証明ではない。

### 主要な未解決箇所
1. NC fiberで許容構造対象のexact自己同値軌道・安定化群・相対慣性を具体化すること。
2. AOUの標準helix（relation stack）と数値標識の大域的降下を証明すること。
3. 非常に一般の一次変形の整数核は決定済み。特殊fiberの整数核、形式高次の障害、invertible bimoduleによる実際の作用を求めること。
4. AOU GIT compactificationのどこでheart/構造対象の許容性が保たれるか判定すること。


## 公表論文との境界

ambient射、四頂点potential、Poisson延長、中心三次ペンシルとAS4の計算は `nc-cubic-ambient-moduli` に移し、この研究の自足した標識忘却論文の再開には必要としない。非可換fiberの許容構造対象について、高次形式変形、自己同値2-groupの慣性、数値標識の純粋helix認識が未解決である。新規性は網羅的に確認できていない。
