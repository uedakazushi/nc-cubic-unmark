# 研究ノート：反標準 heart・有限 Weyl 標識・線束選択

2026-11-18 / unmark-v10。再開は `00_research_plan.md` から。証明は現行主論文を参照する。

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

`thm:ac-serre-positivity` は全対象のRR/H作用とr(O0)=1からSerre消滅とA1={r=0}を導く。(EP)とrank1tfのr=1は帰結である。証明はmixed shiftsの生成だけを使う。単一指数での各n生成、A0⇒d=0は主張しない。

`thm:numerical-line-uniqueness` はこの数値仮定の下で成立する。F→H^{-1}Eの単射の余核は同次数ならdegree=−3、(EP)と矛盾。χ(E,F)=χ(F,E)=1から両向きの単射を得て同型。存在集合Ω_Aの決定は別。Ω_A−K=Ω_AはHから従うがΩ_A=Λは未証明。

Line_adm=Lineにはcross Ext消滅とAZ生成が必要。例外性は自己Ext消滅であって、全mのExt¹(L,H^mL)消滅ではない。全クラスの個々の開条件の可算交叉を非空Zariski開としない。

## 許容性に関する具体的な障害と点対象

`prop:root-simple-obstruction`：零次数simple Tのc1=Cが非零ならC²=−2、HT≅T、Ext¹(T,T)=0。c=Hom(O0,T)>0として評価全射O0→T^cの核Eはline。全H^-nEからTへのHomが消えるため生成不能。一方制限はR_O0≅R_Eを与える。**条件付き命題であり、このTの実例や非存在は未確認**。反標準切断環を作って元のheartを再構成する際、豊富性の確認を環同型で代用してはならない。

`lem:numerical-point-ext`：ch(P)=(0,0,s)のsimpleはs>0。line LについてExt¹(P,L)=Ext¹(L,P)=0, Hom(L,P)次元s。非分裂拡大0→L→F→P→0があればFはrank1tf、しかしn(F)=−s<0となるのが証明の要点。root型simpleを排除すると、零階数・零次数対象全体に組成列でExt消滅が拡張する。これだけで正次数torsionや全生成を解決したとはしない。

## 有限Weyl作用の具体的な残課題

`weyl_line_markings.tex`：九相対類(0,a,b;x1,x2,x3;y1,y2,y3)からh=x1+x2+x3−b、e_i=x_i (i≤3)、e_{3+j}=h−y_jを復元。GramはI1,6、K=−3h+Σe。line一意性から実標識→frameが単射で≤51840。OU一般定義の全very strong helicesではなく、指定したAOU三ブロック線束型を数える。

単純根α_i=e_i−e_{i+1} (i=1..5), α6=−h+e4+e5+e6=a−b。s1,s2,s4,s5,s6はX/Yブロックと(A,B)の置換。唯一残るs3で

- b'=x1+x2−y1
- x3'=h−y1
- y1'=h−x3

となり他六対象を保つ。各点でこの交換が同じ型の実標識を与えれば、有限W作用・Coxeter関係・網羅性は一意性と生成元論から従う。

**未完成の構成候補**：B'=ker(X1⊕X2→Y1)、Y1'=coker(B→X1⊕X2)。X3'は複体[B→X1⊕X2⊕X3→Y1]の中間cohomology。三本の合成の唯一関係を使って二射の合成を零にする。関係係数が零になる境界では成分の消失も検討する。K0/chの式は検算済みだが、評価epi、余評価mono、複体の端exactness、得られる対象のrank1tf・例外性・fullness・very strongnessは未証明。kernel/cokernelを取る操作自体はheart内でも、所定rankと数値類を得るには端exactnessが不可欠。

`verify_weyl_frames.py` は27(-1)類の網羅性をCauchyの有限範囲と整数探索で確認し、72の直交six、51840のordered frames、E6 Coxeter関係、九対象Euler、三候補ch式を検算する。これは圏内の構成証明ではない。

## 可換・形式標識とPicard障害

固定可換X上の通常標識はW(E6)-torsor、|W|=51840。Xの自己同型でも割った標識同型類数は51840/|Aut(X)|。この違いは集合論だけで扱える。

各線束の許容Artin持上げは一意。`cor:formal-all-line-markings` は特殊ファイバーがrank1tfとなるAOU型相対標識全体を通常標識の持上げで尽くす。fixed relative heart/特殊ファイバー同定を保持するためAut(X)=1は不要。この範囲と自己同値商の区別を保つ。対象の持上げとtensor自己同値の持上げは異なる。δπ(L)=H¹(π^sharp)c1(L)、一般rank4、非常に一般の整数核ZK。許容一次変形の自己同値軌道Pic/ZK≅Z6は、選択集合がPic分あることと矛盾しない。全型への無条件拡張はしない。

rank4 witnessは `x³+y³+z³+txy+t³=0, C={t=0}`。t=εzで平面三次にεxyzが現れ、Jacobian環で非零。一次線形Picard不変式はPoisson4方向だけ。これはAOUの大域商や線束存在分類を代用しない。

## 現行付録の用途

全relationの45次元gldim2代数、HH¹=10−ρとHH²=18−ρ、SerreのJordan型(3,1^6)、E6の数値格子は構成と数値の検算として保持。全単項式境界は(10,18)、一般トーラスは(0,8)、一つの関係式だけ単項式でも(0,8)。数値やHH次元の一般性から反標準heartを認識しない。

DDL形式比較は固定可換heartのAbel変形を記述する補助結果。反標準heartのweak許容条件を全形式方向で証明したと読み替えない。群oid/stack的精密化は現在の集合論的分類後に行う。

## 先行研究と参照

AOU arXiv:2404.00175v1 §§4–5,7, Thms1.1/1.2。OU arXiv:2508.04986v1 Def1.1とhelix構成。Artin–Zhang, Noncommutative projective schemes, Adv.Math.109(1994),228–287, DOI10.1006/aima.1994.1087, Thm4.5。Polishchuk arXiv:math/0212182v4のIntroductionとThm2.4に再構成の枠組み、Lemma2.1(ii)に任意tailのmixed-index生成。AOU(4.1),(9.44)の九線束、OU Def1.1(3)/Def3.1の一般marking/very strongness、DGK DOI10.1515/crll.2005.2005.588.99 §2.6のO(I1,6)_K=W(E6)を一次資料で確認。DDL DOI10.4171/JNCG/83 Thms4.5,5.13,5.15。Toda arXiv:math/0502571。Bondal–Orlov arXiv:alg-geom/9712029。詳細書誌は主論文。

Hoffmann–Reede, Torsion-free rank one sheaves over del Pezzo orders, J.Algebra493(2018)251–266, DOI10.1016/j.jalgebra.2017.08.029, arXiv1603.03324v1 Lemma3.9は、P²上terminal del Pezzo orderで同c1 rank1tf間のExt²消滅を証明する。Serre→mono→torsion余核の有効次数と標準類の負性、という論法を一次本文で確認。本稿ではその対象圏との同定をせず、反標準heartの公理から次数正値性を導く部分を区別する。

可換例外層のK0類での一意性はKN §1.3 p433の命題として既知。今回は出版社一次PDF由来の検索本文で命題を確認し、その前後の証明を全面再査読したとはしない。root型評価核の形式はSeidel–Thomas, arXiv math/0001043v2 Def2.7/Def2.9/Prop2.10のdual spherical twistと対応する。本文の短完全列による直接証明はtwist同値定理に依存しない。AZ原論文Cor7.5の原文は未取得なので、一般χ条件とSerre消滅の定理を未確認引用で追加しない。

anticanonical heartをqgr反標準環と呼ぶ用語は、接続した `nc-dp-surface-hearts/research/common_del_pezzo_framework.md` の該当定義を確認した。他リポジトリの全定理を暗黙の入力にはしない。

内在的線束判定、今回のSerre消滅・階数認識、root型障害、frame復元は既存文献との重複の可能性があり、一般的新規性を主張しない。本稿の追加導出は指定した反標準heartの公理からの証明である。既知の古典格子論・AZ再構成・相対持上げ理論そのものを本研究の新結果として扱わない。
