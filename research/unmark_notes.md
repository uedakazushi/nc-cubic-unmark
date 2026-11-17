# 研究ノート：反標準 heart・有限 Weyl 標識・線束選択

2026-11-18 / unmark-v9。再開は `00_research_plan.md` から。証明は現行主論文を参照する。

## 二つの忘却の集合論的辞書

基準A=A_ac=qgr R_e。H=S^{-1}[2]、weak標識は許容線束Lのchoice。AS heartだけを別の構成として比較する。固定圏内ではLine_adm(A)を対象の同型で割る。固定weak標識上ではMark_AOU/OU(A,L)を数える。

`Mark_AOU/OU(A)=coprod_[L] Mark_AOU/OU(A,L)` は選択の分解であって、各項の非空性を主張しない。第一段階の有限W(E6)と第二段階の線束格子を混同しない。基礎圏の同定を忘れた組のexact同値類はLine_adm(A)/Aut_ex(A)となるが、線束そのものの分類をこの商で代用しない。

G_Q=(Gm)^18は矢の基底変更で九射影のK0を固定する。W(E6)の幾何学的標識変更とは異なる。全weak cubicがAOU/OUのmarked像に入るとは仮定しない。

## 反標準 heart の同定

`R_L=⊕ Hom_A(L,H^nL)`。Lが許容ならAZ再構成でqgr R_L≃A。この同値はLをπR_Lへ送るが、異なるLでの環の同型、固定A内でLを交換する自己同値、またはLine(A)の群法則を与えるものではない。

弱標識公理でHのt-exact性を仮定するだけでは、もとの指定された導来圏の中の反標準heartとの同定は済まない。環からのqgrと指定比較を明記する。AS heartから標準対象を移す場合は構造対象と反標準作用を追う。`lem:ample-heart-transfer` は両側のacyclic生成列が対応する場合の十分条件。

## 線束分類の入力と障害

`thm:intrinsic-line-criterion`：rank1tfの非零射は単射、End=C、負H自己Hom=0、Ext²自己=0、exceptional iff χself=1。既存O0の豊富性と二次成長で証明。E自身の豊富性を仮定しない。

数値RRがある場合、n=D²/2−ch₂(E)≥0、Ext¹(E,E)=2n。I_pはrank1,c1=0でもn=1、Ext¹次元2でexceptionalでない。rankとc1だけでは不十分。

`thm:numerical-line-uniqueness` はRRと(EP)を仮定する。F→H^{-1}Eの単射の余核は同次数ならdegree=−3、(EP)と矛盾。χ(E,F)=χ(F,E)=1から両向きの単射を得て同型。存在集合Ω_Aの決定は別。Ω_A−K=Ω_AはHから従うがΩ_A=Λは未証明。

Line_adm=Lineにはcross Ext消滅とAZ生成が必要。例外性は自己Ext消滅であって、全mのExt¹(L,H^mL)消滅ではない。全クラスの個々の開条件の可算交叉を非空Zariski開としない。

## 可換・形式標識とPicard障害

固定可換X上の通常標識はW(E6)-torsor、|W|=51840。Xの自己同型でも割った標識同型類数は51840/|Aut(X)|。この違いは集合論だけで扱える。

各線束の許容Artin持上げは一意。対象の持上げとtensor自己同値の持上げは異なる。δπ(L)=H¹(π^sharp)c1(L)、一般rank4、非常に一般の整数核ZK。許容一次変形の自己同値軌道Pic/ZK≅Z6は、選択集合がPic分あることと矛盾しない。全型への無条件拡張はしない。

rank4 witnessは `x³+y³+z³+txy+t³=0, C={t=0}`。t=εzで平面三次にεxyzが現れ、Jacobian環で非零。一次線形Picard不変式はPoisson4方向だけ。これはAOUの大域商や線束存在分類を代用しない。

## 現行付録の用途

全relationの45次元gldim2代数、HH¹=10−ρとHH²=18−ρ、SerreのJordan型(3,1^6)、E6の数値格子は構成と数値の検算として保持。全単項式境界は(10,18)、一般トーラスは(0,8)、一つの関係式だけ単項式でも(0,8)。数値やHH次元の一般性から反標準heartを認識しない。

DDL形式比較は固定可換heartのAbel変形を記述する補助結果。反標準heartのweak許容条件を全形式方向で証明したと読み替えない。群oid/stack的精密化は現在の集合論的分類後に行う。

## 先行研究と参照

AOU arXiv:2404.00175v1 §§4–5,7, Thms1.1/1.2。OU arXiv:2508.04986v1 Def1.1とhelix構成。Artin–Zhang, Noncommutative projective schemes, Adv.Math.109(1994),228–287, DOI10.1006/aima.1994.1087, Thm4.5。Polishchuk arXiv:math/0212182v4のIntroductionとThm2.4に再構成の枠組み。DDL DOI10.4171/JNCG/83 Thms4.5,5.13,5.15。Toda arXiv:math/0502571。Bondal–Orlov arXiv:alg-geom/9712029。詳細書誌は主論文。

anticanonical heartをqgr反標準環と呼ぶ用語は、接続した `nc-dp-surface-hearts/research/common_del_pezzo_framework.md` の該当定義を確認した。他リポジトリの全定理を暗黙の入力にはしない。

内在的線束判定などには既存文献との重複の可能性があり、一般的新規性を主張しない。今回の改稿は対象範囲と論理順の修正であり、以前のモデル依存の分類をA_acの定理として移したものではない。
