# 研究ノート：構造対象・quiver 標識・モジュライ fiber

2026-11-19 / unmark-v14。最初に `00_research_plan.md` を読む。論文に証明のある事項はラベルを参照し、ここでは再開に有用な要点・障害・補助的観察を保持する。

## 構造対象と quiver 標識の辞書

基準はA=A_ac=qgr R_O、H=S^{-1}[2]。比較する別の表面heartはAS heartのみ。O-markingは内在的定義の構造対象を指定する。rank1 torsion-free、AZ豊富性、反標準Hilbert級数を要求し、例外性・smooth proper性・数値格子は最小定義に足さない（`def:o-marked-cubic`）。既存のweak標識/許容線束は例外性等を備えた比較用部分である。中心的正則切断を持つ既知weak/RR heartでは最小構造対象の例外性を証明したが、中央切断のない一般の最小公理の問題は残る。

Qには順序付きラベル、先頭頂点1、非負cut次数を固定する。有限foundation R=End(T)とrolled-up B=⊕_{n≥0}Hom(T,H^nT)を区別する。B0=Rで、元の矢はcut0、周期を越える逆矢はcut1。augmentation m=rad R⊕B_{>0}について、矢はm/m²を最小生成する。無限BのJacobson radicalを使わない。I⊂arrowideal²である最小斉次表示kQ/Iの存在を要求し、表示同型・矢の基底・関係の代表・potentialの座標は標識データにしない（`def:q-marking`）。

collection全体を[1]だけシフトしてもrolled-up代数は同じだが、非零E1∈AならE1[1]∉Aである。従ってQと導来collectionだけから指定heartの構造対象は自動的には決まらず、先頭の構造対象適合性を定義に含める。

E1が構造対象、Eがfull very strongなら、全対象はAに属する（`prop:o-helix-heart-recognition`）。証明は正自己twistのExt消滅→AZ生成とhdim2による全対象のSerre消滅→反標準Homのheart検出であり、数値RRに依存しない。一般の豊富対だけに高次Ext消滅を読み込まない。

標準AOU型Qは三ブロック各3頂点、隣接する二層に9+9矢、終端から先頭へ9逆矢。degree0の任意の三層関係代数はgldim≤2、Kellerの未変形3-CY completionには最小関係ごと逆矢が一つある。最小rolled-up quiverの指定から関係次元が各対1となり、dim R=45、標準Euler行列C_Qを得る（`prop:aou-quiver-euler-recognition`）。この時点では関係の全係数非零を使わない。一つのQ-markingからsmooth proper性とO例外性、全対象RR/H、K0=Knum、内在的rankを導ける（`cor:q-marking-numerical-inputs`）。その後の線束認識・Weyl実現には(R0)を別に使う。

### 三種類の fiber と慣性

x=(A,O)を固定する。Mark_Q(A,O)は同じAの中でE1≅Oを満たすcollectionの対象同型類集合であり、圏の自己同値で割らない。M^Oの射は(F,α:FO≅O)をcompatible自然同型で割る。自然中心Cの計算により、先頭O上で恒等な自然自己同型は自明。M^Qの射には全成分の指定同型を含め、M^{Q,rig}はi>1の同型の存在だけを要求する（`def:o-moduli-groupoid`, `def:q-moduli-groupoids`）。

`thm:q-o-fiber-groupoids`：基礎点との同定を保持する2-fiberは非交和 ⨿_{Mark_Q} B((C×)^{ell−1})。rigidifiedな2-fiberは離散Mark_Q。π0のfiberはG_x\Mark_Qで、G_x=Aut_ex(A,O)。基礎点との同定を保持したfiberをさらにG_xで割らない。raw Qの絶対慣性は相対torusとG_x内のmarking安定化群の中央拡大（`prop:q-marking-scalar-inertia`）。一般の分裂やglobal積gerbeは未証明。

標準Q存在+(R0)ならMark_QはW(E6)-torsor。raw fiberは51840個のB(Gm^8)、rigidified fiberは51840点、π0のfiberはΓ_O\Wで51840/|Γ_O|点（`cor:standard-q-o-weyl-fibers`）。この点数からfamilyの有限étale性を推論しない。étale siteで相対Abel圏とperfect部分圏、平坦対象・Serre/basechangeを指定しstackificationを取る定義は `def:relative-marked-moduli`。全内在的対象を含むモデルと、構成した有限商との相対比較は未確認。

### 数値的に自明な exact 自己同値

`prop:q-numerical-auto-faithful` は標準Q存在と、(R0)またはcanonical九対象のline性+全関係係数非零からAut_ex(A)→Aut(Knum,χ)が単射であると示す。数値的に恒等のFは九線束を固定し、Rの各頂点を保つ自己同型を誘導する。全係数非零関係により十八矢のscalingはvertex scaling、従ってinnerに限られる。Fはexactなので標準dg quotientへliftし、tilting後のMorita bimodule XはF(T)≅Tから次数0に集中する。H0Xがinner-twisted regularなのでX≃Rとなる。一般のabstract triangulated自己同値への主張ではない。

この結果でG_x≅Γ_O⊂Wとなり、標識集合への作用が自由になる。rigidified Q対象の絶対慣性は自明、raw Q対象の絶対慣性はGm^8（`cor:standard-q-absolute-inertia`）。very generalにΓ_A=ZKという既存の結果と合わせるとAut_ex(A)=〈H〉≅Z、G_x=1（`cor:very-general-q-o-groupoids`）。中央楕円因子locusでは下記の全構造対象例外性が成立するため、第二の写像のΛ/ZKは全最小構造対象の結果となる。

### 表示の商と標識の忘却を区別する

G_18=(Gm)^18による矢の基底変更は九射影のK0を固定し、幾何学的Weyl標識変更とは異なる。AOU relation/potential quotientのvertex scalar kernelはGm^8だが、この階数一致だけで内在的M^Qと同定しない。相対heart、基底変換、exact比較、同型降下が要る。

`thm:actual-aou-very-general` の集合論的忘却写像は、weak公理と指定AS/反標準比較に適合する標準AOU full very strong標識の全範囲を定義域とする（`def:maximal-weak-compatible-aou`）。heart公理を確保するproof open Uにmarked側を制限すると別のWeyl標識を落とし得る。次の相対比較でも飽和定義域が必要。全GIT境界・全OU型・Weyl作用の全域正則性は未確定。

### 最小構造対象と欠損

既存のweak/RR heart内の最小構造対象Oについてδ=D²/2−ch₂≥0、Ext¹(O,H^mO)=2δ (m≥0)（`prop:o-marking-defect-comparison`）。δ=0、例外性、正自己twist消滅、旧許容線束が同値。I_pは自己Homの反標準Hilbert級数がO_Xと同じでもExt¹self=2であり、負twistからの射が全てpのidealを通るためO_Xを生成できず、AZ豊富性に失敗する（`rem:o-ideal-sheaf-test`）。従ってI_pは最小O公理全体の反例ではない。

`lem:central-section-self-vanishing` はz:id→H^a、z_HM=Hz_M、z_O単射という追加データからtail self Ext¹=0を導く。固定全射H^aO→coker zへのAZ Hom全射はzのeventual単射性、各固定拡大へのAZ Hom全射はzの各元上の局所冪零性を与える。pullbackとpushoutの同一視にはzの自然性をDb上に延長し、H周期との両立を使う。この二条件を省いて、任意の切断の冪で同じ議論ができるとは扱わない。数値RRはtail消滅からδ=0へ戻す段階だけに必要である。

正則中心元gを持つqgr Rでは、gで消される対象は高次数tailでR/gRの有限和の商となりrank0。そのため任意rank1tf対象のg-kernelはA1に属して零となる（`prop:central-ring-all-structures-exceptional`）。候補Oを先にlineと仮定しない。実際の中心楕円因子locusではStr₃=Line_adm（`cor:aou-all-structures-exceptional`）。中央切断の存在自体は最小公理から未導出であり、そのない場合のδ>0は未決着である。

## 相対標識と completion の moduli

非正則Artin RではA_RとD_R⊂Db(A_R)を別に指定する（`def:admissible-artin-dg-model`）。A_Rはflat Grothendieck Abel変形のnoetherian部分、D_Rはrelative smooth proper perfect圏。考慮するflat noetherian持上げがD_Rに入ることもモデル仮定。Perf(P^n_R)の標準例外束はPerfを生成するが、非R-perfect coherent対象まで含むDbは生成しない。flat coherent対象だけの部分圏も一般にAbelでない。この区別は既存Artin/Weyl/AZ証明にも適用する。

`thm:artin-exceptional-lift` の対象持上げはLowenのflat dual（障害Ext²、差Ext¹）を使用する。相対RHomのperfect Nakayamaはstrongnessとvery strongnessを保存し、有限threadのfullnessは後ろからのevaluation coneで証明する。Artin底では無限個の組に一つずつNakayamaを適用してよいが、一般底で無限個の開条件の共通部分が開とは限らない。rawな持上げ群oidはB((1+I)^(ell−1))、rigidified忘却はArtin形式étale（`cor:q-o-artin-formal-etale`）。

固定smooth proper dg族上ではTVのsimple object stackとscalar gerbeを用い、exceptional locus→full strong locusを開条件で切り出す（`thm:full-strong-completion-etale`）。同型類のétale sheafificationがétale algebraicspaceを与える。底の線束捩れは局所的に同型でも大域的には同型とは限らず、普遍対象やgerbeの中立性を主張しない。有限性・準コンパクト性・分離性も未結論。very strong/Q locusにはheart平坦性の開性、一様tail閾値、相対Q型条件を追加する（`cor:q-completion-etale-locus`）。

相対最小quiverはHom階数だけで決まらない。R=C[ε]/ε²上、三矢a:1→2,b:2→3,c:1→3に関係ba=εcを課すと代数は自由rank6だがaugmentation a/a²のc成分はR/(ε)。標準AOU foundationの18矢9関係はR³→R²の全射と自由kernelで保存できる。rolled-up27矢にはrelative Serre--CY completion比較写像を構成する必要がある。次は相対対角解消をdualし、各cut次数のperfect比較と特殊fiberの同型からArtin Nakayamaを適用する。単に『Kellerをrelativeに適用する』だけでは比較写像の確認を代用しない。

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

`prop:aou-all-corner-lines` は全九頂点にcorner-openを同時に課す。可換点b0で各E_vは線束なので九つとも成立し、その有限交差をU_ellと交差しても非空。e_vCe_vは楕円線束のHomからなる整域、e_vBe_vは正則中心元による整域持上げ。各E_vでHilbert/例外性/豊富性を確保した後にrank認識を適用する。この順序により(R0)を仮定せず、非空開U_allの全canonical対象が許容lineとなる。別のincomingな任意Q列のline性は同時には証明していない。

### 相対 corner の到達点

`prop:relative-cofinite-corner` はC-noetherian上の局所有限次数代数に同じ証明を適用し、torsionを高次数零の有限生成加群として扱う。Be右eBe有限生成とeB左eBe有限生成を両方確認し、Torのe消滅からqgrでexactになる。`prop:relative-corner-basechange` の通常tensorは、各次数で十分高くなれば同型である射を保つためSerre局所化へ降りる。非平坦底変更の関手自体がexactだとはしない。

固定底のC-linear exact同値は有限表示C-moduleとのtensorに可換なので、内在的C-flat性を保つ。ただしこの事実だけから、任意の底変更後にもflatとなることを推論しない。族の系では『考慮する全底変更で内在的flat』を普遍flatとして用いる。Bの右noetherian性は各fiberでなく全必要basechange後を仮定する。AOU族への適用に残るのはrelative楕円Hom代数と正則中心元からこのnoetherian性を示すことであり、cornerの高次数零条件自体は既に任意底変更で保たれる。

## 有理 Weyl 作用と代数的商 chart

`thm:weyl-birational-action`：普遍有限代数R/T8上で三対象を有界射影複体として直接構成し、K=C(T8)上の定義を確保する。全係数非零関係Σλ_j f_j u_j=0にλを入れて三項複体のd²=0を厳密にする。finite RHomの指定階数、fullness、各R³→R²の全射とkernelの全係数非零を有限開条件として課す。Euler行列だけでquiverを認識しない。

八つの正規化不変量がf_sを与え、very-generalなroot-free点の同一heartで交換を繰り返してCoxeter等式を得る。途中パラメータが初めのheartのproof-openへ入るとは仮定せず、tiltingで輸送した既存heartを使う。s²=idからdominance、Coxeterから右W作用 t·w=f_w(t), f_v∘f_w=f_wv。Aut(X)=1の可換点で作用の忠実性を確認する。ここはverystrong無限条件を一つの開へ置き換える議論ではない。

有限群についてVを共通定義域とし、U=⋂_w(V∩f_w^{-1}(V))を取る。群法則と分離性により全f_wがUを保つ。さらにaffine開の有限個のtranslateを交差して安定affine開を得る（`lem:finite-birational-stable-open`）。これによりU→[U/W]は有限étale torsor、次数51840（`thm:weyl-finite-etale-chart`）。固定点があっても商stackへの射はétaleだが、coarse quotientへの射は別。有限個の非恒等元の固定点集合を除けば自由作用のscheme quotientになる。

U⊂U_allに取り、有限個wのtilting比較を同時に広げる。Oを保つ導来同値はSerreと可換で、反標準Homのheart検出からt-exact（`cor:o-pointed-derived-exact`）。全canonical対象がlineなので、任意のexact O同値が運ぶ九対象のframeはWで記述され、line一意性とtorus完全不変量からv=u·w。そのfunctorも数値的忠実性で一意。従って[U/W](C)≃UのO-familyのfull essential image、Aut_ex(A_u,O_u)=Stab_W(u)（`prop:weyl-chart-point-comparison`）。この比較は全点(R0)を必要としない一方、全intrinsicQ-sourceの網羅性を結論しない。

相対比較の具体的な次の案：perfect Morita bimodule P_wの合成とP_wvのrelative RHomを作り、先頭O上のHomへの評価を調べる。very-general fiberでpointed自然同型が存在し一意なので、汎用点上の評価が同型なら1を逆に引き、有限個(w,v)のcone supportと分母を除いて自然同型を広げられる可能性がある。先頭で正規化した中心が自明なら三元coherenceは一意性から従う。ただしrelative RHomのperfect性・basechange、評価の汎用点同型、相対heart/descentを確認する必要があり、この案は未証明として残す。複素fiberの同型存在だけから大域同型があるとは扱わない。

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

`thm:actual-aou-very-general` は以上を統合し、可算個の真閉集合を除く実際のAOU点でLine_adm=Line≅Λ、Γ_A=ZK、M_Q^acからの第一fiber=W(E6)-torsor、第二fiber=Λ/ZK≅P(E6)を得る。全Λの許容line存在が(R0)を与え、線束認識定理がincomingな全標準very strong標識を捕捉する。構成した各line標識がAOU表示とAS比較を持つことにより逆包含も成立する。この集合論的証明自体は数値作用の核の分類を使わない。さらに `prop:q-numerical-auto-faithful` によって、この標準root-free locusの核は自明で、自己同値群は〈H〉≅Zとなる。

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

本稿のanticanonical heartは、最小定義の構造対象の反標準切断環のqgrとして定義・再構成する。他の文献やリポジトリのheartの同定を暗黙の入力にしない。定義と比較の必要条件は本稿だけで確認できる。

内在的線束判定、Serre消滅・階数認識、root反射、有限Weyl実現、very-general族の導出は既存文献との重複の可能性があり、一般的新規性を主張しない。本稿の追加導出は指定した反標準heartの公理からの証明である。既知の古典格子論・AZ再構成・相対持上げ理論そのものを本研究の新結果として扱わない。

追加の一次資料：Bridgeland–Stern, arXiv:0909.1732, Definition3.1/Theorems4.5,5.3(ii)のpure block helixからgeometricityへの定理。Polishchuk, arXiv:math/0212182v4, Lemma2.1(ii), Proposition2.3, Theorem2.4。Okawa–Ueda, arXiv:2007.07620v1, (18)–(25)とTheorem5後の最終段落によるAS-Gorenstein/有限global dimension。OU2025 §3 Definition3.1直後も確認。AS-regularityをOU2020 Theorem5だけの結論として引用しない。Stacks Project Tag057G, Lemma37.38.5は指定点を通るsmooth射のétale sliceに使用する。Tag055Uの局所sectionだけでは指定点の条件を省けない。

実際のheart認識の一次資料：AOU arXiv:2404.00175v1, Theorem1.1, §4.6, Definition7.1/Lemma7.4。OU arXiv:2007.07620v1, (30)–(32)の自然変換とtriangleを使用する。Minamoto–Mori, The structure of AS-Gorenstein algebras, Adv.Math.226(2011),4061–4095, DOI10.1016/j.aim.2010.11.004（著者版の表題はStructures of AS-regular Algebras）, Corollary4.13/Theorem4.14（著者preprint https://www.math.kyoto-u.ac.jp/preprint/2010/06Minamoto.pdf ）は準Fano代数のpreprojective algebraと通常のtailsの有界導来圏を比較する。Amiot, Preprojective Algebras, Singularity Categories and Orthogonal Decompositions, in Algebras, Quivers and Representations, Abel Symposia8, Springer(2013),1–11, DOI10.1007/978-3-642-39485-0_1（著者稿 https://www-fourier.univ-grenoble-alpes.fr/~amiot/amiot.pdf ）のTheorem2.3に導来同値の具体的関手と反Serre/shift対応、Corollary3.3の証明に有限余次元cornerによるqgr同値を確認した。arXiv:1211.2615の表題はSingularity categories, preprojective algebras and orthogonal decompositionsで、刊行版と語順が異なる。本文照合には著者稿を用いた。一般corner同値、AS-regularity、通常のD^b比較そのものの新規性は主張しない。

有限AOU resolutionの追加一次資料：Keller, Deformed Calabi–Yau completions, arXiv:0908.3499, Theorems4.8/6.10（本稿は変形パラメータ零）。Ginzburg, Calabi–Yau algebras, arXiv:math/0612139, Proposition5.1.9/Corollary5.4.3。Kellerのerratum arXiv:1809.01126は一般の変形パラメータの負巡回持上げ条件を扱うため、ここでは未変形completionのTheorem4.8を入力とする。Toda arXiv:math/0502571, Proposition5.6/Lemma5.8/§6では核の自己Extを介したHochschild作用と一次障害の比較を確認した。

quiver認識・数値忠実性の一次資料：AOU §§4.2–4.5/§5の有限quiver・rolled-up quiverとrelation/potential商、OU2025 Definition1.1(3)/§5とRemark5.4のmarking・periodic展開、OU2020 (18)–(22)のcompletion。Keller arXiv:0908.3499 §6.9/Theorem6.10の未変形completionから最小関係への逆矢を使用。Keller, On differential graded categories, ICM2006 Vol.II pp151–190, arXiv:math/0601185v5 §4.4/Thm4.8のdg quotientと、Toën, The homotopy theory of dg-categories and derived Morita theory, Invent.Math.167(2007)615–667, DOI10.1007/s00222-006-0025-y, arXiv:math/0408337v7 Thm7.2(2)/Cor7.6のMorita表示を数値自己同値忠実性に使用。Stacks Tag0436はstackificationの普遍性、Tag04V2は既に代数的なstackの平坦慣性部分群のrigidificationの仮定確認に使用し、代数性を先取りしない。

相対completionの一次資料：Toën–Vaquié, Moduli of objects in dg-categories, Ann.Sci.Éc.Norm.Supér.(4)40(2007),387–444, DOI10.1016/j.ansens.2007.05.001, arXiv:math/0503269v5、Cor3.15/3.17/3.21/3.22。本文はarXiv PDFと著者公開出版版 https://www.math.univ-toulouse.fr/~vaquie/marque/vaquie_AnnEns40.pdf を照合。Lieblich, Moduli of complexes on a proper morphism, J.AlgebraicGeom.15(2006),175–206, arXiv:math/0502198v2、Thm3.1.1/Cor4.3.3は可換proper flat族の対照入力であり、任意nc圏にそのまま適用しない。Lowen math/0407019のIntroductionがTheoremAのflat dualを明記する。Stacks https://stacks.math.columbia.edu/tag/0616 はalgebraicspaceのlfp+formalétale⇔étale、Tag0BDKはperfect複体の指定次数・階数locus、Tag04UVはtorsorによるquotientstack、Tag07S7は自由有限局所自由群作用のscheme商。いずれも一次本文で適用仮定を確認した。

中央切断の証明はAZ Cor7.5に依存せず、最小定義のeventual Hom全射を二度使う。Polishchuk math/0212182v4 §2のample/projective sequence定義は高次Ext消滅を含めない。Yekutieli–Zhang, Serre duality for noncommutative projective schemes, Proc.AMS125(1997),697–707、著者稿 https://www.math.bgu.ac.il/~amyekut/publications/nc-serre/paper.pdf のThms2.2(b),2.3(1b),2.4もχを別条件として使う。Serre functor存在からχ全体が従うと読み替えない。新規の中心切断導出と有理W作用の一般的新規性は未確認。AOU §2.3の古典的Weyl商と§5のrelation torus商は一次本文で確認したが、T8全体の本稿の有理作用を同論文の定理として引用していない。

当該版の計算・組版などの実行状況と限界は `research/unmark_validation.json` を参照。本文の証明、独立点検、数値検算、配布物の生成・保存は別の状態として扱う。
