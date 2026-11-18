# 研究ノート：反標準 heart・有限 Weyl 標識・線束選択

2026-11-18 / unmark-v12。最初に `00_research_plan.md` を読む。論文に証明のある事項はラベルを参照し、ここでは再開に有用な要点・障害・補助的観察を保持する。

## 集合論的な辞書

基準はA=A_ac=qgr R_e、H=S^{-1}[2]。比較する別のheartはAS heartのみ。weak標識は許容線束Lのchoice。固定圏内の対象の同型だけを取ればLine_adm(A)、固定L上では標準Euler型のMark_Q^vs(A,L)を数える。root-free条件(R0)の下ではMark_Q^vs=Mark_Q^lineを認識済みである。矢の基底は標識に含めない。

全line・標識の存在が確認された範囲では、raw choicesはΛとW(E6)-torsor。圏のexact同値類を点にすると、第一fiberはMark(A,L)/Aut_ex(A,L)、第二はLine_adm(A)/Aut_ex(A)。full九対象があると自己同値の数値作用はD↦t+gD、g∈W(E6)で、Hの冪によるZKが中心に入る。従って実際のfiberはΓ_L\Wと(Λ/ZK)/barΓ_A（`prop:affine-auto-action`, `cor:actual-set-fibers`）。ΛとΛ/ZKの違いは可算集合の抽象的濃度ではなく、自然な数値ラベルと同一視の内容の違いである。

G_Q=(Gm)^18による矢の基底変更は九射影のK0を固定し、幾何学的Weyl標識変更とは異なる。全weak cubicがAOU/OUの像に入るとも、OUの一般very strong helixが標準三ブロック型とも仮定しない。

`thm:actual-aou-very-general` の忘却写像は、weak公理・指定AS/反標準比較に適合する標準AOU full very strong標識の最大の範囲M_Q^acを定義域とする（`def:maximal-weak-compatible-aou`）。heart公理を確保するために選んだ稠密開Uにmarked側を制限すると、同じweak markingの別のWeyl標識がUから外れる可能性がある。従ってU上の存在定理とM_Q^acでのfiber定理を区別する。全GIT境界への写像やWeyl作用の全域正則性は未確定である。

## 線束分類と反標準再構成

`thm:intrinsic-line-criterion`：rank1tfの非零射は単射、End=C、負H自己Hom=0、Ext²自己=0、exceptional iff χself=1。E自身の豊富性を入力にしない。数値RRの下でn=D²/2−ch₂≥0、Ext¹self=2n。I_pはn=1なので例外的でない。

`thm:ac-serre-positivity` は全対象のRR/H作用とr(O0)=1から、mixed shiftsの生成を使ってSerre消滅・A1={r=0}・有効次数正値性を導く。抽象weak heartの公理だけからのA0⇒d=0はなお不明である。中心楕円因子を持つ実際のAOUのUでは `prop:elliptic-divisor-length-recognition` によってA0={r=d=0}まで認識する。同c1のlineの一意性は `thm:numerical-line-uniqueness`。存在集合Ω_AはHでK方向に安定だが、一般のweak cubicでΩ_A=Λとは結論しない。

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

simple Tの正次数をd、c1をCとする。r(T)=0で、H^nTのch₂はs+ndとなるため数値類が相異なる。simple性とSerreによりHom(T,H²T)=Ext²(T,H²T)=0。RRからC²=dim Ext¹(T,H²T)≥0、Hodge指標からC²≤d²/3。整数RRからC²+dは偶数。d=1ならC²=0しかないので矛盾する。有限長対象も次数1にはならない。この数値論法だけではd≥2のsimpleを排除できない。中心曲線因子を仮定しない抽象weak heart全体ではA0⇒d=0が残る一方、実際の中心楕円因子locusでは後述の中心元による議論で全ての単純対象の次数零が従う。

## 固定weak標識上の有限Weyl作用

九相対類からh=x1+x2+x3−b、e_i=x_i、e_{3+j}=h−y_jを復元する。格子frameへの単射で標識数≤51840。六単純反射のうち五つは直交ブロック置換、残るe3↔e4は

B′=ker(X1⊕X2→Y1)、Y1′=coker(B→X1⊕X2)、X3′=複体[B→X1⊕X2⊕X3→Y1]の中間cohomology。

(R0)「零次数simpleはc1=0」を仮定すると、零rank・零degreeの対象は数値的点の拡大であり、lineへの両向きExt¹が零。これを使って二つの評価の端exactnessとline性を示す。任意二本の合成が独立なので三本の関係係数は全て非零。反射後の九対象はfull三ブロック例外列で、Hのexact性からpure helixとなり、Bridgeland–Stern Theorem5.3(ii)からvery strong。完全な証明は `thm:rootfree-cross-reflection`。数値一意性からCoxeter関係と網羅性も従う。

`lem:rootfree-aou-presentation` は任意の第一ブロックUと第三ブロックY_sについて同じ二経路独立性を使い、十八矢・九二次関係の有限AOU代数を得る。三係数全て非零で、relation torusに入る。

`lem:ample-helix-reconstruction` は豊富な一剰余列を持つfull very strong helix全体の豊富性と、Z代数の右noetherian性を直接示す。任意のprojective部分加群の射の像をnoetherian対象中で安定化し、eventual Hom全射で負tailを有限生成するのが要点。Polishchukのcoherent quotientとOUのnoetherian quotientの違いをこの証明で解消する。OU2020のAS-Gorenstein/有限gldim入力と数値成長を併せて、AS heartと指定反標準heartを同定する。別のheartへの移動は使わない。

### AOU 型への包含と標準 helix の線束認識

`prop:aou-simple-resolution`：有限三層代数Rはgldim2。Kellerの変形パラメータ零の3-CY completionを用いると、関係に逆矢を加えたquiverとW=Σρ_r rのGinzburg代数となる。very strongnessによる次数零集中とGinzburgの対角分解から、右加群規約では0→P_{α,m−3}→⊕P_{β,m−2}→⊕P_{β,m−1}→P_{α,m}→S_{α,m}→0。これで構成した標識が実際のAOU型であることまで確認する。AOUの表示の正方向と比較する際はblock添字を反転する。

逆向きの標準型認識は `prop:right-tail-torsionfree-recognition` と `thm:aou-helix-line-recognition` による。条件(R0)の下で、r(E)=1、End(E)=C、Ext¹(E,H^nL)=0 (n≫0)ならEはtorsion-freeである。最大torsion部分Tを除いたFはrank1tf。右tail消滅からχ(T,H^nL)≥0となり、RRの一次係数によってd(T)=0を得る。(R0)ならT≠0は正の数値的点類であり、F→Tの非零射がEの平方零自己準同型を与えることとχ(F,T)>0が矛盾する。数値階数一・self Euler1だけを根拠にしてはいない。

許容先頭E0=Lを持つ標準Euler型C_Qのfull very strong threadには、反標準tailによるheart判定を適用できる。Euler格子同型はSerre作用と可換で、(H−1)²v=3r(v)[pt]とr(L)=1により点類を保つため、全九対象の数値階数が一となる。very strongnessが右tail Ext¹消滅を与え、上記の判定と例外性から全九対象がlineとなる。従って固定root-free weak heart上ではMark_Q^vs=Mark_Q^lineであり、標準型の全fiberを認識できる。異なるEuler型の一般OU helixや、指定heart比較のないGIT境界は対象外である。

## 実際のAOU locusにおけるheart認識

証明は `sec:aou-heart-recognition` に置く。有限九頂点relation代数Rのrolled-up代数Bにはcompletion次数を用い、B0=R、元の矢は次数零、関係に双対な追加矢は次数一とする。全矢を次数一にするpath-length gradingと混同しない。AOUの楕円decupleとのbirational対応により、稠密開U_ellでは楕円曲線Y上のline helix S_iとOUの自然変換η:H^{-1}→Idが得られる。曲線のcohYは中心因子の商としてだけ使い、別の表面heartへ移動する議論ではない。

`lem:elliptic-helix-central-element` はηから正則中心元z∈B1を構成し、B/zB=CをS_i間の正次数Hom代数として同定する。中心性にはηのH周期との両立が必要であり、自然性の式をforward Homの単射で消去して確認する。短完全列のsource a<jについて、a≤j−9はacyclicity、j−9<a<jは同じstrong foundation内の後退Ext消滅を使う。楕円line列の豊富性からCをnoetherianとし、gr_z B≅C[t]からBのnoetherian性を持ち上げる。g-adic補正の停止は固定した全次数でvaluationが有界であることによる。完備化を仮定していない。

`prop:aou-corner-open` の有限余次元条件dim B/BeB<∞は、可換三次曲面でOの負反標準twistによる生成とSerre消滅から従う。Bは次数零・一で生成されるため、一つの十分高い次数Nの(B/BeB)_N=0だけで全tailが零となる。この有限coherent加群の消滅は可換点b0を含む開条件であり、U_cornerを与える。U=U_ell∩U_cornerは非空開集合である。

`lem:cofinite-corner-tails` によりqgr B≃qgr(eBe)。inverseのN⊗_{eBe}eBは加群圏では右exactにとどまるが、高次Torはeで消え、B/BeBが有限次元なので有限次元となる。従ってqgrでexactに降下する。unit・counitの核と余核にも同じ有限次元性を使う。corner同値の一般原理は既知であり、本稿の有限開条件への適用と区別する。

通常の有界導来圏の比較にはMinamoto–Mori Corollary4.13/Theorem4.14を使う。acyclicityからRがquasi-Fano、ΠR=Bが対称AS-regular・Gorenstein parameter一となり、noetherian性からgraded coherent性を得る。∇B=RなのでD^b(qgr B)≃D^b(mod R)。頂点projectiveはπe_iBへ、Hは次数シフトへ対応する。dg quotientだけから通常のD^b(qgr)を自動的に同一視しない。Amiot Theorem2.3にもq(−⊗^L_RΠR)とS_d^{-1}↔(1)が明記される。

AZ豊富性はcornerの有限生成から負O-twistによる全射を得て、very strongnessとSerre双対性から直接証明する。全射P→Mに対する負自己Hom消滅でExt²(O,H^nM)=0、同じ議論を核へ適用してExt¹消滅を得る。noetherian性だけからχ条件やAZのeventual Hom全射を読み込まない。

`prop:aou-full-rr-transport` は九頂点の一定な非退化Euler行列から全対象のRR/H作用を輸送する。内在的階数の認識は別段階である。R_e=eBeには正則中心元g=ezeがあり、R_e/gR_e=eCe、qgr(eCe)≃cohY、π(eCe)は線束に対応する。eCeが整な曲線上のline間のHom cornerなのでdomainであり、有限g-adic valuationによりR_eもdomainとなる。これがOの非零rank-zero部分対象を排除する。さらにH^{-1}O→Oの曲線余核は無限長で、A/A0の長さを用いてO∉A1を示す。この二つにより数値階数とGabriel--Krull filtrationを整合させ、`cor:actual-aou-weak-heart` を得る。階数公理を階数認識の前提へ戻す循環を避ける。

`prop:elliptic-divisor-length-recognition` では単純対象Mへのgの作用H^{-1}M→Mを調べる。同型ならHilbert多項式が周期的なのでr=d=0。零なら十分高いtailがgで消され、曲線商cohYの単純対象、従って点層から来るので同じ結論を得る。有限組成列の加法性によってA0⊂{r=d=0}となり、既知の逆包含と合わせてA0={r=d=0}。この証明でHilbert定数が必ず一となるのはgで消されるsimpleであり、g可逆のsimpleの定数には同じ結論を課していない。中心因子のない抽象weak heartへの一般化は残る。`cor:root-simple-off-divisor` は、曲線の点層の非零self Ext¹をexact fully faithfulなj_*が保つことを用い、gで消されるsimpleはrigidなroot型にならないと示す。拡大が像で分裂すればfullnessで分裂射が戻るため、Ext¹の単射性は導来full faithfulnessを仮定せずに得られる。従ってroot simpleにはgが可逆に作用する。

## very general な代数族への移行

`thm:very-general-line-existence` の族仮定は明示的：滑らかな既約底全体の有限局所自由代数、固定vertex projectives、相対perfect RHom・反Serre作用と底変更、稠密開Uと可換基準点b0でのweak反標準heartと数値格子。b0∈Uは不要であり、全底点にheartを用意する必要もない（`rem:generic-heart-dense-domain`）。標準AOU relation torusでは普遍45次元・gldim2の有限代数と `cor:actual-aou-weak-heart` によって入力を確認できる。

Ext²(L_D,L_D)=0を用い、固定有界projective項の微分のschemeが指定点でsmoothと示す。Stacks Tag057Gの指定点を通るétale sliceで代数化する。L_D→H^mO0の単射と(H^{-a}L_D)^N→O0の全射を一緒に延長し、対象と二coneのheart所属を可算個の反標準RHom消滅で確保する。単射witnessはrank1tfを保証するため不可欠。

九対象のfullnessはprojective生成対象GからE9,…,E1の順にevaluation coneを取り、残余が古典点で零であるという開条件で確保する。順序を逆にすると既に消した直交性を保存できない。各九対象にもmono witnessを付ける。

étale V→Bはquasi-finiteなので、Vの真閉集合の像の閉包はBの真閉集合。可算個のbad lociをBへ移してから全Picard類について合併する。像と可算交叉を交換しない。very generalには可算交叉で十分であり、単一Zariski開である必要はない。

### generic自己同値を形式結果から推論する際の障害

許容Artin底の自己同値像ZKだけから、generic fiberの全自己同値像もZKとは推論しない。例えばB=A1、U=B\{0}で群scheme G=B⊔Uを取り、第二成分をU上の位数2元とすると、G→Bはseparated étaleだが特殊fiberは自明、generic fiberはZ/2。この例はnc cubicの反例ではなく、代数性・無限小剛性だけではgeneric成分の特殊化が保証されないことを示す。

`thm:very-general-numerical-aut` は、数値ラベルごとの有限End代数の等化子を使って、明示した族仮定の下でΓ_A=ZKを証明する。各(t,g)∈Λ⋊Wについて古典的九対象を代数化し、その有限関係式moduliが元のものと一致する閉条件を取る。自己同値があればline一意性からこの一致が必要。g≠1はAut(X)=1とBondal–Orlov、g=1,t∉ZKはPicard一次障害で真閉性を検出する。relation商の同型類検出とKodaira–Spencer比較は確認できる。指定weak反標準heartと全対象の数値表示は実際の稠密Uと可換点b0で確保されるため、標準AOU relation torusへ適用できる。

全係数非零のc_ijmについてr_ijm=c_ijm/c_ij0、θ_ijm=r_ijm r_00m/(r_i0m r_0jm) (i,j=1,2; m=1,2)。各mの3×3行列の零行・零列を1に正規化すれば、八つのθが頂点を保つ代数同型類の大域標準形となる（`lem:aou-fullsupport-torus`）。作用核は連結な頂点スカラートーラス、有限の残余安定化群はない。局所環上でも単元だけで同じ正規化ができる。

等化子の真閉性は、w≠1なら可換点の非一致、w=1,t∉ZKなら接写像の非一致で示す。後者では接写像が一致すると双対数上の有限代数同型、相対tiltingによる導来Morita自己同値が得られ、特殊化がtensor L_tとなる。可逆双加群の左右の一次変形障害の差φ_*(u)−uが零でなければならず、Picard shearによりδπ(t)=0となって矛盾する（`lem:derived-picard-tangent-necessity`）。この段階に相対Abel heartの存在を隠れた仮定として使わない。

数値ラベルごとに一つの既約étale branchだけを選ぶ。一般点でのline一意性がそのbranchの九対象と任意の自己同値像を同定するので、全branchの列挙は不要。八次元relation torusの正規化切断上で適用し、18→8の正次元商に真閉集合を直接押し下げない。

`thm:actual-aou-very-general` は以上を統合し、可算個の真閉集合を除く実際のAOU点でLine_adm=Line≅Λ、Γ_A=ZK、M_Q^acからの第一fiber=W(E6)-torsor、第二fiber=Λ/ZK≅P(E6)を得る。全Λの許容line存在が(R0)を与え、線束認識定理がincomingな全標準very strong標識を捕捉する。構成した各line標識がAOU表示とAS比較を持つことにより逆包含も成立する。数値的に自明な自己同値群自体の分類は不要で、その核はline・標識の同型類に自明に作用する。

## 許容Artin変形の実際のfiber

`thm:artin-actual-fibers`：Aut(X)=1なら相対自己同値の特殊化はtensor M。R→双対数商への制限とδπ(M)=0を使い、kerδπ=ZKなら像⊂ZK。H_Rの冪で逆包含。lineの一意持上げにより作用は平行移動だけで、kernel functorの分類は不要。固定L_Rの安定化群は特殊化が恒等なので、全九対象の一意持上げを固定する。第一fiberはW-torsor、第二はPic/ZK。

一次のgeneric整数核ZKは、複素線型写像のgeneric rank4から直接出るのではない。W(E6)のroot表現の既約性と可算個の整数類の非消滅を用いる。rank4 witnessはx³+y³+z³+txy+t³=0、C={t=0}で、t=εzがJacobian環の非零類xyzを与える。

compatible形式塔の対象同型はR_{n+1}^×→R_n^×の全射で調整する。effectivityや分数体自己同値の分類をこれに含めない。二段階を合成したfiberは(Pic/ZK)×Mark(X)。標準frameを選ぶと拡大affine Weyl群P(E6)⋊W(E6)のunderlying setで添字付けられるが、その事実だけから大域作用を主張しない。

## 特殊locusへ進むための着手点

中心楕円因子を持つlocusではsimpleの次数零と、root simpleへのgの可逆性が分かった。後者は点層の非零self Ext¹とrootのrigidityによるので、Hilbert定数が一という情報だけからc1=0を推論しているのではない。次はg可逆のsimpleにroot型が実在するかを調べる。部分的な実現集合Ω_Aを求め、そのlineに対するa=s−D·Cの符号と許容性を比較する。a>0は必要条件であり、十分性を仮定しない。

最大weak適合locusの境界では、曲線商の退化、rolled-up代数のnoetherian性、cofinite corner条件、usual derived比較、内在的rank認識を個別に追う。Uを最大locusと同一視せず、有限Weyl交換の相対kernel・cokernel・cohomologyがflatか、どこでline性を失うかを調べる。全OU型・全GIT境界・Weyl作用の全域正則性は未解決である。

## 現行付録の用途

普遍relation代数は45次元、gldim2。支持行列rankρによりHH¹=10−ρ、HH²=18−ρ。全単項式境界は(10,18)、一般torusは(0,8)、一関係だけ単項式でも(0,8)。Serre Jordan型(3,1^6)、E6数値格子、一次Picard不変式を保持する。数値型やHH次元のみから反標準heartを認識しない。

`verify_weyl_frames.py` は27個の(-1)類の網羅性、72 sixers、51840 ordered frames、Coxeter関係、九対象Euler/frame復元、三反射対象と点類のchを検算する。`verify_line_bundle_numerics.py` は欠陥、Hilbert多項式、root普遍拡大、affine反射、(H−1)²v=3r[pt]、右tail Eulerの係数−d(T)、周期Hilbert多項式の係数を検算する。圏内のexactness・存在・豊富性は数値コードではなく本文の証明に依存する。

## 先行研究と参照

AOU arXiv:2404.00175v1 §§4–5,7, Thms1.1/1.2。OU arXiv:2508.04986v1 Def1.1とhelix構成。Artin–Zhang, Noncommutative projective schemes, Adv.Math.109(1994),228–287, DOI10.1006/aima.1994.1087, Thm4.5。Polishchuk arXiv:math/0212182v4のIntroductionとThm2.4に再構成の枠組み、Lemma2.1(ii)に任意tailのmixed-index生成。AOU(4.1),(9.44)の九線束、OU Def1.1(3)/Def3.1の一般marking/very strongness、DGK DOI10.1515/crll.2005.2005.588.99 §2.6のO(I1,6)_K=W(E6)を一次資料で確認。DDL DOI10.4171/JNCG/83 Thms4.5,5.13,5.15。Toda arXiv:math/0502571。Bondal–Orlov arXiv:alg-geom/9712029。詳細書誌は主論文。

Hoffmann–Reede, Torsion-free rank one sheaves over del Pezzo orders, J.Algebra493(2018)251–266, DOI10.1016/j.jalgebra.2017.08.029, arXiv1603.03324v1 Lemma3.9は、P²上terminal del Pezzo orderで同c1 rank1tf間のExt²消滅を証明する。Serre→mono→torsion余核の有効次数と標準類の負性、という論法を一次本文で確認。本稿ではその対象圏との同定をせず、反標準heartの公理から次数正値性を導く部分を区別する。

可換例外層のK0類での一意性はKN §1.3 p433の命題として既知。今回は出版社一次PDF由来の検索本文で命題を確認し、その前後の証明を全面再査読したとはしない。root型評価核の形式はSeidel–Thomas, arXiv math/0001043v2 Def2.7/Def2.9/Prop2.10のdual spherical twistと対応する。本文の短完全列による直接証明はtwist同値定理に依存しない。AZ原論文Cor7.5の原文は未取得なので、一般χ条件とSerre消滅の定理を未確認引用で追加しない。

本稿のanticanonical heartは、許容構造対象の反標準切断環のqgrとして定義・再構成する。他の文献やリポジトリのheartの同定を暗黙の入力にしない。定義と比較の必要条件は本稿だけで確認できる。

内在的線束判定、Serre消滅・階数認識、root反射、有限Weyl実現、very-general族の導出は既存文献との重複の可能性があり、一般的新規性を主張しない。本稿の追加導出は指定した反標準heartの公理からの証明である。既知の古典格子論・AZ再構成・相対持上げ理論そのものを本研究の新結果として扱わない。

追加の一次資料：Bridgeland–Stern, arXiv:0909.1732, Definition3.1/Theorems4.5,5.3(ii)のpure block helixからgeometricityへの定理。Polishchuk, arXiv:math/0212182v4, Lemma2.1(ii), Proposition2.3, Theorem2.4。Okawa–Ueda, arXiv:2007.07620v1, (18)–(25)とTheorem5後の最終段落によるAS-Gorenstein/有限global dimension。OU2025 §3 Definition3.1直後も確認。AS-regularityをOU2020 Theorem5だけの結論として引用しない。Stacks Project Tag057G, Lemma37.38.5は指定点を通るsmooth射のétale sliceに使用する。Tag055Uの局所sectionだけでは指定点の条件を省けない。

実際のheart認識の一次資料：AOU arXiv:2404.00175v1, Theorem1.1, §4.6, Definition7.1/Lemma7.4。OU arXiv:2007.07620v1, (30)–(32)の自然変換とtriangleを使用する。Minamoto–Mori, The structure of AS-Gorenstein algebras, Adv.Math.226(2011),4061–4095, DOI10.1016/j.aim.2010.11.004（著者版の表題はStructures of AS-regular Algebras）, Corollary4.13/Theorem4.14（著者preprint https://www.math.kyoto-u.ac.jp/preprint/2010/06Minamoto.pdf ）は準Fano代数のpreprojective algebraと通常のtailsの有界導来圏を比較する。Amiot, Preprojective Algebras, Singularity Categories and Orthogonal Decompositions, in Algebras, Quivers and Representations, Abel Symposia8, Springer(2013),1–11, DOI10.1007/978-3-642-39485-0_1（著者稿 https://www-fourier.univ-grenoble-alpes.fr/~amiot/amiot.pdf ）のTheorem2.3に導来同値の具体的関手と反Serre/shift対応、Corollary3.3の証明に有限余次元cornerによるqgr同値を確認した。arXiv:1211.2615の表題はSingularity categories, preprojective algebras and orthogonal decompositionsで、刊行版と語順が異なる。本文照合には著者稿を用いた。一般corner同値、AS-regularity、通常のD^b比較そのものの新規性は主張しない。

有限AOU resolutionの追加一次資料：Keller, Deformed Calabi–Yau completions, arXiv:0908.3499, Theorems4.8/6.10（本稿は変形パラメータ零）。Ginzburg, Calabi–Yau algebras, arXiv:math/0612139, Proposition5.1.9/Corollary5.4.3。Kellerのerratum arXiv:1809.01126は一般の変形パラメータの負巡回持上げ条件を扱うため、ここでは未変形completionのTheorem4.8を入力とする。Toda arXiv:math/0502571, Proposition5.6/Lemma5.8/§6では核の自己Extを介したHochschild作用と一次障害の比較を確認した。

当該版の計算・組版などの実行状況と限界は `research/unmark_validation.json` を参照。本文の証明、独立点検、数値検算、配布物の生成・保存は別の状態として扱う。
