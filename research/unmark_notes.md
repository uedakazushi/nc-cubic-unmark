# 研究ノート：反標準 heart・有限 Weyl 標識・線束選択

2026-11-18 / unmark-v11。最初に `00_research_plan.md` を読む。論文に証明のある事項はラベルを参照し、ここでは再開に有用な要点・障害・補助的観察を保持する。

## 集合論的な辞書

基準はA=A_ac=qgr R_e、H=S^{-1}[2]。比較する別のheartはAS heartのみ。weak標識は許容線束Lのchoice。固定圏内の対象の同型だけを取ればLine_adm(A)、固定L上ではMark_Q^line(A,L)を数える。矢の基底は標識に含めない。

全line・標識の存在が確認された範囲では、raw choicesはΛとW(E6)-torsor。圏のexact同値類を点にすると、第一fiberはMark(A,L)/Aut_ex(A,L)、第二はLine_adm(A)/Aut_ex(A)。full九対象があると自己同値の数値作用はD↦t+gD、g∈W(E6)で、Hの冪によるZKが中心に入る。従って実際のfiberはΓ_L\Wと(Λ/ZK)/barΓ_A（`prop:affine-auto-action`, `cor:actual-set-fibers`）。ΛとΛ/ZKの違いは可算集合の抽象的濃度ではなく、自然な数値ラベルと同一視の内容の違いである。

G_Q=(Gm)^18による矢の基底変更は九射影のK0を固定し、幾何学的Weyl標識変更とは異なる。全weak cubicがAOU/OUの像に入るとも、OUの一般very strong helixが標準三ブロック線束型とも仮定しない。

## 線束分類と反標準再構成

`thm:intrinsic-line-criterion`：rank1tfの非零射は単射、End=C、負H自己Hom=0、Ext²自己=0、exceptional iff χself=1。E自身の豊富性を入力にしない。数値RRの下でn=D²/2−ch₂≥0、Ext¹self=2n。I_pはn=1なので例外的でない。

`thm:ac-serre-positivity` は全対象のRR/H作用とr(O0)=1から、mixed shiftsの生成を使ってSerre消滅・A1={r=0}・有効次数正値性を導く。A0⇒d=0はなお不明。同c1のlineの一意性は `thm:numerical-line-uniqueness`。存在集合Ω_AはHでK方向に安定だが、一般のweak cubicでΩ_A=Λとは結論しない。

`prop:line-admissibility-test` は、O0への有限生成全射 ⊕H^{-a_j}L→O0 と、全m≥0のExt^{>0}(L,H^mL)=0による判定。全射をO0の任意負tail生成と合成してLの生成を得る。eventual Ext消滅はO0の場合と同じmixed-shift証明で導く。単にself Euler=1や反標準切断環の一致では豊富性は分からない。

Lが許容ならAZ再構成でqgr R_L≃A。この同値はLを構造対象に送るが、異なるL同士を交換するAの自己同値やLine(A)の群法則を与えない。

## 零次数 root と線束の affine 反射

`lem:zero-degree-simple-classification` と `thm:root-line-reflection`：零次数simple Tがc1=C≠0ならC²=−2、HT≅T、Ext¹(T,T)=0。a=s−D·CについてHom(L,T)=max(a,0)、Ext¹(L,T)=max(−a,0)。普遍拡大Fの欠陥が−dim Hom(L,T)·dim Ext¹(T,L)となることが二者択一の要点。

a>0は評価核、a<0は普遍拡大、a=0は恒等によってD↦D−aCを実現する。line一意性からinvolutionとなり、制限射で反標準切断環を保つ。許容lineはa>0のstrict affine halfspaceにある。正の側にある全lineの豊富性は示していない。この反射はL自体を変え、固定L上の有限Weyl標識変更とは別。

root simpleの実例は未構成で、現在のweak公理のみからの排除も未証明。O0がTを生成していても、その評価核がTを生成しないことは矛盾ではない。spherical twistを固定heartのexact自己同値とみなしてはならない。

全Λの許容lineが実現されれば、D=−mCでa=s−2m≤0となるのでroot simpleは排除される（`cor:admissible-root-halfspace`）。この方向がvery-general定理と有限Weyl実現を結ぶ。

### 論文外の補助観察：零階数・零次数部分圏

B0={Q:r(Q)=d(Q)=0}はSerre部分圏で全対象が有限長。root型因子はH固定なのでeventual Serre消滅が全H冪に拡張する。点型因子には `lem:numerical-point-ext` をH^{-n}O0と適用する。組成列から、全整数nについて

Ext^{>0}(O0,H^nQ)=0、dim Hom(O0,H^nQ)=χ(O0,Q)>0 (Q≠0)。

従ってHom(O0,−):B0→Vect_Cはexact faithful。非零射の像もB0にあり、この正値性がfaithfulnessを与える。この観察自体はroot simpleを排除しない。

### 論文外の補助観察：次数1のsimpleは存在しない

simple Tの正次数をd、c1をCとする。r(T)=0で、H^nTのch₂はs+ndとなるため数値類が相異なる。simple性とSerreによりHom(T,H²T)=Ext²(T,H²T)=0。RRからC²=dim Ext¹(T,H²T)≥0、Hodge指標からC²≤d²/3。整数RRからC²+dは偶数。d=1ならC²=0しかないので矛盾する。有限長対象も次数1にはならないが、d≥2のsimpleは排除できず、A0⇒d=0は未証明のままである。

## 固定weak標識上の有限Weyl作用

九相対類からh=x1+x2+x3−b、e_i=x_i、e_{3+j}=h−y_jを復元する。格子frameへの単射で標識数≤51840。六単純反射のうち五つは直交ブロック置換、残るe3↔e4は

B′=ker(X1⊕X2→Y1)、Y1′=coker(B→X1⊕X2)、X3′=複体[B→X1⊕X2⊕X3→Y1]の中間cohomology。

(R0)「零次数simpleはc1=0」を仮定すると、零rank・零degreeの対象は数値的点の拡大であり、lineへの両向きExt¹が零。これを使って二つの評価の端exactnessとline性を示す。任意二本の合成が独立なので三本の関係係数は全て非零。反射後の九対象はfull三ブロック例外列で、Hのexact性からpure helixとなり、Bridgeland–Stern Theorem5.3(ii)からvery strong。完全な証明は `thm:rootfree-cross-reflection`。数値一意性からCoxeter関係と網羅性も従う。

`lem:rootfree-aou-presentation` は任意の第一ブロックUと第三ブロックY_sについて同じ二経路独立性を使い、十八矢・九二次関係の有限AOU代数を得る。三係数全て非零で、relation torusに入る。

`lem:ample-helix-reconstruction` は豊富な一剰余列を持つfull very strong helix全体の豊富性と、Z代数の右noetherian性を直接示す。任意のprojective部分加群の射の像をnoetherian対象中で安定化し、eventual Hom全射で負tailを有限生成するのが要点。Polishchukのcoherent quotientとOUのnoetherian quotientの違いをこの証明で解消する。OU2020のAS-Gorenstein/有限gldim入力と数値成長を併せて、AS heartと指定反標準heartを同定する。別のheartへの移動は使わない。

### AOU 型への包含と未解決の逆向き

`prop:aou-simple-resolution`：有限三層代数Rはgldim2。Kellerの変形パラメータ零の3-CY completionを用いると、関係に逆矢を加えたquiverとW=Σρ_r rのGinzburg代数となる。very strongnessによる次数零集中とGinzburgの対角分解から、右加群規約では0→P_{α,m−3}→⊕P_{β,m−2}→⊕P_{β,m−1}→P_{α,m}→S_{α,m}→0。これで構成した標識が実際のAOU型であることまで確認する。AOUの表示の正方向と比較する際はblock添字を反転する。

逆向きに、任意のAOU標識の九対象が固定反標準heartで全てrank1tfになることは未証明。数値階数一・self Euler1だけからtorsion-free性を読み込まない。現在の第一fiberはMark_Q^lineに限定する（`rem:aou-line-converse`）。この認識と、族の反標準heart仮定の確認が、全AOUのvery-general第一fiberに到達するための二つの課題である。

## very general な代数族への移行

`thm:very-general-line-existence` の族仮定は明示的：有限局所自由代数、固定vertex projectives、指定された各fiberのweak反標準heartと数値格子、相対perfect RHom・反Serre作用、可換fiber。これらをAOU族で確認することが次の核心。

Ext²(L_D,L_D)=0を用い、固定有界projective項の微分のschemeが指定点でsmoothと示す。Stacks Tag057Gの指定点を通るétale sliceで代数化する。L_D→H^mO0の単射と(H^{-a}L_D)^N→O0の全射を一緒に延長し、対象と二coneのheart所属を可算個の反標準RHom消滅で確保する。単射witnessはrank1tfを保証するため不可欠。

九対象のfullnessはprojective生成対象GからE9,…,E1の順にevaluation coneを取り、残余が古典点で零であるという開条件で確保する。順序を逆にすると既に消した直交性を保存できない。各九対象にもmono witnessを付ける。

étale V→Bはquasi-finiteなので、Vの真閉集合の像の閉包はBの真閉集合。可算個のbad lociをBへ移してから全Picard類について合併する。像と可算交叉を交換しない。very generalには可算交叉で十分であり、単一Zariski開である必要はない。

### generic自己同値を形式結果から推論する際の障害

許容Artin底の自己同値像ZKだけから、generic fiberの全自己同値像もZKとは推論しない。例えばB=A1、U=B\{0}で群scheme G=B⊔Uを取り、第二成分をU上の位数2元とすると、G→Bはseparated étaleだが特殊fiberは自明、generic fiberはZ/2。この例はnc cubicの反例ではなく、代数性・無限小剛性だけではgeneric成分の特殊化が保証されないことを示す。

`thm:very-general-numerical-aut` は、数値ラベルごとの有限End代数の等化子を使って、明示した族仮定の下でΓ_A=ZKを証明する。各(t,g)∈Λ⋊Wについて古典的九対象を代数化し、その有限関係式moduliが元のものと一致する閉条件を取る。自己同値があればline一意性からこの一致が必要。g≠1はAut(X)=1とBondal–Orlov、g=1,t∉ZKはPicard一次障害で真閉性を検出する。relation商の同型類検出とKodaira–Spencer比較は確認できる。残る適用入力は指定weak反標準heartの族と全対象の数値表示の整合性である。

全係数非零のc_ijmについてr_ijm=c_ijm/c_ij0、θ_ijm=r_ijm r_00m/(r_i0m r_0jm) (i,j=1,2; m=1,2)。各mの3×3行列の零行・零列を1に正規化すれば、八つのθが頂点を保つ代数同型類の大域標準形となる（`lem:aou-fullsupport-torus`）。作用核は連結な頂点スカラートーラス、有限の残余安定化群はない。局所環上でも単元だけで同じ正規化ができる。

等化子の真閉性は、w≠1なら可換点の非一致、w=1,t∉ZKなら接写像の非一致で示す。後者では接写像が一致すると双対数上の有限代数同型、相対tiltingによる導来Morita自己同値が得られ、特殊化がtensor L_tとなる。可逆双加群の左右の一次変形障害の差φ_*(u)−uが零でなければならず、Picard shearによりδπ(t)=0となって矛盾する（`lem:derived-picard-tangent-necessity`）。この段階に相対Abel heartの存在を隠れた仮定として使わない。

数値ラベルごとに一つの既約étale branchだけを選ぶ。一般点でのline一意性がそのbranchの九対象と任意の自己同値像を同定するので、全branchの列挙は不要。八次元relation torusの正規化切断上で適用し、18→8の正次元商に真閉集合を直接押し下げない。

## 許容Artin変形の実際のfiber

`thm:artin-actual-fibers`：Aut(X)=1なら相対自己同値の特殊化はtensor M。R→双対数商への制限とδπ(M)=0を使い、kerδπ=ZKなら像⊂ZK。H_Rの冪で逆包含。lineの一意持上げにより作用は平行移動だけで、kernel functorの分類は不要。固定L_Rの安定化群は特殊化が恒等なので、全九対象の一意持上げを固定する。第一fiberはW-torsor、第二はPic/ZK。

一次のgeneric整数核ZKは、複素線型写像のgeneric rank4から直接出るのではない。W(E6)のroot表現の既約性と可算個の整数類の非消滅を用いる。rank4 witnessはx³+y³+z³+txy+t³=0、C={t=0}で、t=εzがJacobian環の非零類xyzを与える。

compatible形式塔の対象同型はR_{n+1}^×→R_n^×の全射で調整する。effectivityや分数体自己同値の分類をこれに含めない。二段階を合成したfiberは(Pic/ZK)×Mark(X)。標準frameを選ぶと拡大affine Weyl群P(E6)⋊W(E6)のunderlying setで添字付けられるが、その事実だけから大域作用を主張しない。

## 現行付録の用途

普遍relation代数は45次元、gldim2。支持行列rankρによりHH¹=10−ρ、HH²=18−ρ。全単項式境界は(10,18)、一般torusは(0,8)、一関係だけ単項式でも(0,8)。Serre Jordan型(3,1^6)、E6数値格子、一次Picard不変式を保持する。数値型やHH次元のみから反標準heartを認識しない。

`verify_weyl_frames.py` は27個の(-1)類の網羅性、72 sixers、51840 ordered frames、Coxeter関係、九対象Euler/frame復元、三反射対象と点類のchを検算する。`verify_line_bundle_numerics.py` は欠陥、Hilbert多項式、root普遍拡大、affine反射、(H−1)²v=3r[pt]を検算する。圏内のexactness・存在・豊富性は数値コードではなく本文の証明に依存する。

## 先行研究と参照

AOU arXiv:2404.00175v1 §§4–5,7, Thms1.1/1.2。OU arXiv:2508.04986v1 Def1.1とhelix構成。Artin–Zhang, Noncommutative projective schemes, Adv.Math.109(1994),228–287, DOI10.1006/aima.1994.1087, Thm4.5。Polishchuk arXiv:math/0212182v4のIntroductionとThm2.4に再構成の枠組み、Lemma2.1(ii)に任意tailのmixed-index生成。AOU(4.1),(9.44)の九線束、OU Def1.1(3)/Def3.1の一般marking/very strongness、DGK DOI10.1515/crll.2005.2005.588.99 §2.6のO(I1,6)_K=W(E6)を一次資料で確認。DDL DOI10.4171/JNCG/83 Thms4.5,5.13,5.15。Toda arXiv:math/0502571。Bondal–Orlov arXiv:alg-geom/9712029。詳細書誌は主論文。

Hoffmann–Reede, Torsion-free rank one sheaves over del Pezzo orders, J.Algebra493(2018)251–266, DOI10.1016/j.jalgebra.2017.08.029, arXiv1603.03324v1 Lemma3.9は、P²上terminal del Pezzo orderで同c1 rank1tf間のExt²消滅を証明する。Serre→mono→torsion余核の有効次数と標準類の負性、という論法を一次本文で確認。本稿ではその対象圏との同定をせず、反標準heartの公理から次数正値性を導く部分を区別する。

可換例外層のK0類での一意性はKN §1.3 p433の命題として既知。今回は出版社一次PDF由来の検索本文で命題を確認し、その前後の証明を全面再査読したとはしない。root型評価核の形式はSeidel–Thomas, arXiv math/0001043v2 Def2.7/Def2.9/Prop2.10のdual spherical twistと対応する。本文の短完全列による直接証明はtwist同値定理に依存しない。AZ原論文Cor7.5の原文は未取得なので、一般χ条件とSerre消滅の定理を未確認引用で追加しない。

anticanonical heartをqgr反標準環と呼ぶ用語は、接続した `nc-dp-surface-hearts/research/common_del_pezzo_framework.md` の該当定義を確認した。他リポジトリの全定理を暗黙の入力にはしない。

内在的線束判定、Serre消滅・階数認識、root反射、有限Weyl実現、very-general族の導出は既存文献との重複の可能性があり、一般的新規性を主張しない。本稿の追加導出は指定した反標準heartの公理からの証明である。既知の古典格子論・AZ再構成・相対持上げ理論そのものを本研究の新結果として扱わない。

追加の一次資料：Bridgeland–Stern, arXiv:0909.1732, Definition3.1/Theorems4.5,5.3(ii)のpure block helixからgeometricityへの定理。Polishchuk, arXiv:math/0212182v4, Lemma2.1(ii), Proposition2.3, Theorem2.4。Okawa–Ueda, arXiv:2007.07620v1, (18)–(25)とTheorem5後の最終段落によるAS-Gorenstein/有限global dimension。OU2025 §3 Definition3.1直後も確認。AS-regularityをOU2020 Theorem5だけの結論として引用しない。Stacks Project Tag057G, Lemma37.38.5は指定点を通るsmooth射のétale sliceに使用する。Tag055Uの局所sectionだけでは指定点の条件を省けない。

有限AOU resolutionの追加一次資料：Keller, Deformed Calabi–Yau completions, arXiv:0908.3499, Theorems4.8/6.10（本稿は変形パラメータ零）。Ginzburg, Calabi–Yau algebras, arXiv:math/0612139, Proposition5.1.9/Corollary5.4.3。Kellerのerratum arXiv:1809.01126は一般の変形パラメータの負巡回持上げ条件を扱うため、ここでは未変形completionのTheorem4.8を入力とする。Toda arXiv:math/0502571, Proposition5.6/Lemma5.8/§6では核の自己Extを介したHochschild作用と一次障害の比較を確認した。
