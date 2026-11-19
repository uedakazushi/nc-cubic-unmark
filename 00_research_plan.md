# 研究方針：構造対象・quiver 標識と忘却射のモジュライ

**2026-11-19 / unmark-v14。最初に本ファイルを読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md`。GitHub `uedakazushi/nc-cubic-unmark` の main をソース正本とする。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。方針は現時点の目標・到達点・理由・未解決点として書き直し、時系列の履歴を積まない。既知の結果、証明記載、今回の証明点検、追加仮定付きの結果、未完成・予想・計算的観察を区別する。主要な主張の仮定、依存文献、証明所在、未確認点を明記する。誤りは依存する本文・要約・方針も訂正する。

論文は日本語LuaLaTeXで現在の成果を論理順に配置し、有効な証明を保持する。先行研究は一次資料で照合し、Introductionで既知入力と寄与を区別する。未確認の新規性・書誌を推測しない。ノートは作業日誌ではなく、現在有用な例・反例・障害・着手方法をまとめ、論文の証明を重複させない。

**ユーザーは研究の区切りごとに、承諾なく現行の研究継続bundleをLibraryに保存する一般許可を与えている。** bundleは現行の方針・ノート・論文・必要な全ソース・PDF・書誌・計算コード・再現手順だけで自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・変更履歴・重複を含めず、軽量化で数学的内容や検証可能性を損なわない。Library既存ファイルの削除は別操作であり明示指示なく行わない。生成・検証・GitHub反映・Library保存を別々に確認し、未実行や失敗はそのまま報告する。日付・版・参照先を揃える。

## II. 本研究の対象と達成基準

**主目標は、構造対象を指定する O-marking と、rolled-up quiver Q を持つ full very strong exceptional collection を指定する Q-marking のモジュライ、および忘却射 p:M^Q→M^O とその fiber を定義・記述することである。** 固定圏内の標識集合、基礎点との同定を保持する2-fiber、同型類集合のfiberを区別する。現在は複素点の群oidに加え、有限Weyl商の代数的モデル、許容Artin変形での形式étale性、固定dg族上のfull strong completionのétale空間まで構成した。次の達成基準は、これらのモデルと実際の内在的relative moduliを族のレベルで比較することである。

採用する最小のO-markingは、noetherian Abel圏A、Hom有限なDb(A)のSerre作用H=S^{-1}[2]、H(A)=A、GK filtrationでrank1 torsion-freeなO、AZ豊富対(O,H)、三次曲面型の反標準Hilbert級数からなる。Oの例外性は仮定に含めず、smooth proper enhancement・数値Picard格子・ambient表示も独立に扱う（`def:o-marked-cubic`）。AZ再構成によりAはqgr R_Oとなるため、基準はanticanonical heartである。比較する別の表面heartはAS heartのみ。構造対象をテンソル単位とみなさない。

Qは頂点の順序・先頭頂点・cut次数を含むrolled-up quiver。有限foundation R=End(⊕E_i)とB=⊕Hom(⊕E_i,H^n⊕E_i)を区別し、Bのaugmentationに関する最小表示kQ/Iを要求する。矢・関係・potentialの基底は標識に含めない（`def:q-marking`）。先頭E1は構造対象であり、残りの対象のheart所属はvery strongnessから導く。

標準AOU型では、Q-markingの存在から比較用weak公理と全対象RR/H構造を導く。さらに零次数root非存在条件(R0)と非空性の下で、固定(A,O)の標識集合はW(E6)-torsor。rawな2-fiberは51840個のB(Gm^8)の非交和、成分スカラーを除いた2-fiberは51840点、同型類集合のfiberはΓ_O\W(E6)である。exact自己同値の数値作用はこの範囲で忠実なので、Γ_Oは実際のO-pointed自己同値群と同型である。

実際の標準AOU relation torusのvery general点では、全許容線束の数値類がΛ、Aut_ex(A)=〈H〉≅Z、Aut_ex(A,O)=1であり、同型類集合の第一fiberも51840点となる。**中心楕円因子を持つ既知のAOU heartでは全ての最小構造対象が例外的である。** 正則中心切断とAZ豊富性から自己Extの漸近消滅を得て、RRの一定欠損を零にする。従ってこのlocusでの第二fiber Λ/ZK≅P(E6)は全最小構造対象に適用できる。中心的切断を持たない一般の最小公理の例外性は未解決。

標準relation torus T8に忠実な有理W(E6)作用を構成し、九つのcorner条件を満たす非空な安定affine開U上で正則化する。U→[U/W]は次数51840の有限étale torsorであり、[U/W](C)はUに現れるO-marked cubicのfull essential imageと同値である。この点の比較には全点(R0)を要しない。ただし、全incoming Q-markingを非線束型も含めて族で網羅したとはしない。

**代数的商モデルの存在、複素点の群oid同定、全内在的relative moduliとの同値は別の主張である。** 最後の主張にはrelative noetherian性、Abel heartとperfect圏の比較、Serre/basechange、Weyl比較のcoherenceとexact同値の降下が残る。非正則底では有限threadのfullnessはrelative Perfの厚生成であり、通常Db全体の生成ではない。一般OUの全型と全GIT境界は現結論に含めない。

## III. 現在の到達点と証明の状態

以下の到達点には本文に証明を記載する。今回の論理点検は中心切断による例外性、九cornerの同時認識、O-pointed導来同値のexact性、相対corner、許容Artin持上げとfull strong completion空間、有限Weyl作用・安定開・複素点群oidの比較を中心とする。独立点検の範囲と実行状況は `research/unmark_validation.json` に記す。保持した全証明の新たな独立再査読を意味しない。既知再構成・Morita理論・変形・格子論と本稿の推論を区別する。外部査読、証明支援系による形式化、網羅的な新規性確認は未実施。

- **最小構造対象と例外性の差**：定義からhdim A=2、負自己twistのHom消滅、非負自己twistのExt²消滅、中心Cを導く（`lem:o-minimal-consequences`, `lem:dimension-centre`）。既存のweak/RR heart内の構造対象はδ=D²/2−ch₂≥0を持ち、Ext¹(O,H^mO)=2δ (m≥0)。δ=0、例外性、正自己twist消滅、旧許容線束が同値（`prop:o-marking-defect-comparison`）。I_pは自己HomのHilbert条件を満たすがAZ生成を満たさず、最小O公理全体の反例ではない。
- **中心切断による全構造対象の例外性**：z:id→H^aがHと可換でz_Oが単射なら、AZ Hom全射条件からz:Ext¹(O,H^nO)→Ext¹(O,H^{n+a}O)はeventual単射。一方、各拡大に同じ豊富性を適用するとzは局所冪零なのでtail Ext¹=0（`lem:central-section-self-vanishing`）。既知RR heartではδ=0。正則中心元gを持つqgr表示ではgで消される対象のrankが零であることから任意rank1tf上の単射性を得る。従って実際の中心楕円因子locusでStr₃=Line_adm、very-general第二fiberは全構造対象についてΛ/ZK（`prop:central-ring-all-structures-exceptional`, `cor:aou-all-structures-exceptional`）。
- **RRなしのheart認識**：構造対象からの全非負自己twist高次Ext消滅は、AZ生成とhdim2により全対象のeventual Serre消滅を与える。これが反標準Homによるheart検出を与え、very strong helixの全対象がAに入る（`lem:o-ample-serre-vanishing`, `prop:o-helix-heart-recognition`）。一般の豊富対だけに高次Ext消滅を読み込まない。
- **quiverから数値構造へ**：標準27矢rolled-up quiverのcut0部分は18矢三層代数。まずgldim≤2を示し、Kellerの未変形3-CY completionの最小逆関係矢を比較して九つの独立関係、dim R=45、標準Euler行列を得る（`prop:aou-quiver-euler-recognition`）。一つのQ-markingからsmooth proper性、O例外性、K0=Knum、全対象RR/Hと内在的rankを導く（`cor:q-marking-numerical-inputs`）。全係数非零には(R0)を別に使う。
- **モジュライとfiber**：M^O、M^Q、M^{Q,rig}を複素点の群oidとして定義。2-fiberは標識集合で添字付けられたB(Gm^{ell−1})、rigidified fiberは離散標識集合、π0のfiberはO-pointed自己同値軌道（`thm:q-o-fiber-groupoids`）。絶対慣性には中央拡大があるが、一般の分裂やglobalな積gerbeを主張しない（`prop:q-marking-scalar-inertia`）。étale site上の相対定義はAbel圏とrelative Perfを分離して指定し、stackificationを取る。
- **相対標識の持上げとétale completion**：許容Artin Abel/dgモデルで、例外列はLowenの障害・差Ext²/Ext¹の零性により一意に持ち上がる。perfect Nakayamaと有限評価coneでstrong/full、Artin底でのvery strongnessも保存。raw持上げ群oidはB((1+I)^{ell−1})、rigidified忘却はArtin形式étale（`thm:artin-exceptional-lift`, `cor:q-o-artin-formal-etale`）。固定smooth proper dg族上のfull strong completionはToën–Vaquiéの対象stackを用いたGm^{ell−1}-gerbe→étale algebraicspace（`thm:full-strong-completion-etale`）。Q-completionへの制限にはheart平坦性・一様tail消滅・相対Q型の開条件を明示する。一般の有限性は未証明。
- **相対corner**：noetherian基礎環上の有限余次元cornerのexact tails同値、通常tensorによる基底変換との適合性、固定底での内在的flat性の対応を証明（`prop:relative-cofinite-corner`, `prop:relative-corner-basechange`）。全考慮基底変換後のnoetherian性を仮定すれば普遍flat tailsの族の比較を得る。この条件をAOU族全体で確認したとはしない。
- **数値作用の忠実性**：標準Q存在と(R0)、または標準九対象のline性と全関係係数非零の下で、数値的に恒等のexact自己同値は各E_iを固定する。arrow rescalingはvertex innerに限られ、exact関手のdg liftとMorita bimoduleからF≅id（`prop:q-numerical-auto-faithful`）。Aut_ex(A)↪Λ⋊W、O安定化群↪W、その標識集合への作用は自由。very generalにはAut_ex(A)=〈H〉、pointed群=1。任意の抽象的triangulated自己同値への主張ではない。
- **内在的線束判定と数値一意性**：weak公理、全対象上の三次曲面型RR/H作用、r(O0)=1から、Serre消滅、A1={r=0}、有効次数正値性を導く。rank1tfのEnd=C、Ext²self=0、欠陥n≥0、Ext¹self=2n。例外性はn=0と同値で、c1でlineが一意（`thm:intrinsic-line-criterion`, `thm:ac-serre-positivity`, `thm:numerical-line-uniqueness`）。rank1tfだけでは例外性は出ず、可換I_pが反例。抽象weak heart全体でのA0⇒d=0は未証明だが、中心楕円因子を持つ実際のAOU locusでは以下の認識結果が成立する。
- **許容性の判定**：有限個の負H-twist of LからO0への全射と、全m≥0の正自己twist高次Ext消滅が、Lのweak許容性と同値（`prop:line-admissibility-test`）。
- **root型simpleの条件付き構成**：零次数root simple T=(0,C,s)が存在する場合、a=s−D·CについてHom(L,T)=max(a,0)、Ext¹(L,T)=max(−a,0)。評価核・普遍拡大によりline集合に反射D↦D−aCを構成し、反標準切断環を保つ。許容線束はa>0を満たす（`thm:root-line-reflection`, `cor:admissible-root-halfspace`）。Tの実在も一般的な排除も主張しない。全Λの許容lineがあればTは排除される。
- **有限Weyl作用の実現**：零次数simpleのc1が全て零という条件(R0)の下で、B′=ker(X1⊕X2→Y1)、Y1′=coker(B→X1⊕X2)、X3′=三項複体の中間cohomologyを構成。line性・fullness・very strongnessを証明し、非空な標準標識集合はW(E6)-torsor（`thm:rootfree-cross-reflection`）。一般OUの全helixの分類ではない。
- **AS比較と有限表示**：full very strong helixが一つのAZ豊富な周期部分列を含めば、helix全体が豊富で、そのZ代数は右noetherian。Polishchuk再構成によりAS heartは元の反標準heartにexact同値（`lem:ample-helix-reconstruction`, `cor:line-helix-as-reconstruction`）。(R0)では有限End代数は十八矢・九関係のAOU表示を持ち、全関係係数が非零（`lem:rootfree-aou-presentation`）。
- **標準helixの線束認識**：条件(R0)の下で、数値階数一、End=C、右反標準tailへのExt¹消滅からtorsion-free性を導く（`prop:right-tail-torsionfree-recognition`）。許容先頭Lを持つ標準Euler型のfull very strong helixでは、heart所属、数値階数一、右tail消滅が自動的に成立するため、九対象が全て線束となる（`thm:aou-helix-line-recognition`）。固定root-free weak heart上では `Mark_Q^vs=Mark_Q^line` であり、第一fiberを線束型の部分集合に限定する必要はない。
- **実際のAOU locusのheart認識**：楕円decupleに由来する稠密locus上でcompletion次数のrolled-up代数Bに正則中心元zを構成し、曲線商からnoetherian性を得る。`dim B/BeB<∞` を可換点で成立する有限次数の開条件として確保し、`qgr B≃qgr(eBe)` を得る。Minamoto–Moriの通常の有界導来圏比較、直接のAZ豊富性、曲線因子による内在的階数認識により、実際の非空開集合U上でweak公理を確認する（`sec:aou-heart-recognition`, `cor:actual-aou-weak-heart`）。全対象のRR/H作用は有限AOU代数の一定Euler格子から輸送される（`prop:aou-full-rr-transport`）。
- **九cornerと有限Weyl chart**：同じ可換点で全九corner条件を開にし、楕円locusと交差させると、標準九対象すべてが許容lineとなる（`prop:aou-all-corner-lines`）。Oを保つ導来同値はheart検出からexact（`cor:o-pointed-derived-exact`）。普遍三項複体をC(T8)上に直接定義し、有限End条件とvery-general数値一意性から忠実なW有理作用を得る。有限群の共通定義域を安定affine開Uへ縮めるとU→[U/W]はfinite étale、次数51840（`thm:weyl-birational-action`, `thm:weyl-finite-etale-chart`）。[U/W](C)はUのO-familyのfull essential image、Aut_ex(A_u,O_u)=Stab_W(u)（`prop:weyl-chart-point-comparison`）。全点(R0)と全incoming Qの網羅性はここでは要求・証明していない。族のcoherence・descentは残る。
- **実際のAOU locusの零次元層**：中心楕円因子を持つUでは `A0={r=d=0}`、`A1={r=0}`、`A2=A`（`prop:elliptic-divisor-length-recognition`）。単純対象への中心元の作用を同型の場合と零の場合に分け、前者はHilbert多項式の周期性、後者は曲線上の点層から次数零を導く。曲線商の点層の非零自己拡大は保たれるため、root simpleは中心元が可逆に作用する部分へ限定できる（`cor:root-simple-off-divisor`）。抽象weak公理だけに一般化してはいない。
- **very-general存在定理と実際の適用**：有限局所自由代数族と相対perfect比較を滑らかな既約底全体に持ち、weak反標準heartを稠密開Uと可換基準点b0で持てば、very generalに `Line_adm=Line≅Λ`、かつ全L上の標準標識が非空なW(E6)-torsor（`thm:very-general-line-existence`）。`b0∈U` は不要。projective複体の代数化、単射・全射のwitnessと可算個のheart/消滅条件を用いる。標準AOU relation torusでは上記のheart認識と普遍有限代数によって全入力が確認できる。
- **集合論的な実際のfiber**：full標識があればexact自己同値の数値像Γ_AはΛ⋊W(E6)の部分群で、中心のZKを含む。全line・標識の存在範囲で第一fiberはΓ_L\W、第二はΛ/Γ_A=(Λ/ZK)/barΓ_A（`prop:affine-auto-action`, `cor:actual-set-fibers`）。「set theoretic」でも自己同値による同一視は残る。
- **実際のvery-general自己同値像とfiber**：八次元の標準AOU relation torusにはAut(X)=1の可換点と整数核ZKのPoisson接方向を選べる。全係数非零のrelation商を八つの明示的torus不変式で記述し、可算個の数値ラベルごとにEnd代数の等化子が真閉となることから、very generalに `Γ_A=ZK`（`thm:very-general-numerical-aut`, `thm:actual-aou-very-general`）。generic自己同値自体の特殊化は不要。最大のweak適合標準AOU定義域で同型類集合の第一fiberは51840点のW(E6)-torsor。中心切断の結果により、第二fiber `Λ/ZK≅P(E6)`はこのlocusの全構造対象に適用できる。忠実性と合わせAut_ex(A)=〈H〉≅Z、O-pointed群=1。
- **許容Artin底の全次数**：Aut(X)=1と、整数核がZKの一次Poisson方向を持つ許容相対変形では、特殊化自己同値像はちょうどZK。第一fiberはW-torsor、第二はPic/ZK。compatible形式塔にも成立（`thm:artin-actual-fibers`, `cor:first-order-pointings`）。分数体の任意の自己同値を特殊化できるとは主張しない。

有効な可換・形式比較、Picard一次障害・整数核・不変式、普遍有限代数、HH/Serre数値計算を現行本文・付録に保持する。線束持上げとtensor自己同値持上げを混同しない。

## IV. 未解決の核心と次の着手

1. **Weyl商と相対O-moduliの比較。** 構成済みU→[U/W]と複素点full essential imageを出発点に、U上の相対qgr/構造対象/Serreを具体化する。相対corner定理に必要な任意noetherian基底変換後のnoetherian性を、相対楕円曲線のHom代数と正則中心元から調べる。Abel圏A_Sとrelative perfect部分圏D_S、普遍flat tailsと対象moduliを分けて扱う。Morita比較P_wの合成P_w∘f_w^*P_vとP_wvのrelative Homを調べ、先頭Oで正規化した比較同型を構成する。比較同型の存在が得られた後に中心の一意性でcoherenceを処理し、exact同値の降下と局所的Weyl認識を証明する。
2. **全Q-sourceへの比較。** 固定dg族上のfull strong completionはétale algebraicspaceとして構成済み。そこに指定heartのflat性、very strongness、rolled-up Q型を課す。優先着手は普遍有限AOU代数の相対対角解消の双対から、相対Serre--CY completionの比較写像を構成すること。固定cut次数のperfect性と特殊fiber比較を確認し、ArtinではNakayamaで比較条件を外す。その後、一様なtail Ext消滅の閾値を探す。全点(R0)のZariski開性や、形式étale性だけから大域的有限性を仮定しない。非線束型の追加標識が現れない範囲を確定して初めて、構成したfinite Weyl chartと全内在的忘却の源を同定する。
3. **構造対象の存在範囲。** 中心的正則切断を持つ既知weak/RR heartでは、最小Oの例外性は解決した。残る一般問題は中央切断の存在を最小公理から導けるか、または中央切断なしで欠損δを排除できるかである。AZのeventual Hom全射と高次Ext消滅を同一視しない。その後、例外的Oから標準Q collectionが存在する条件を探し、忘却像を広げる。
4. **特殊rootと境界・先行研究。** 中心楕円因子locusのroot simpleは中心元が可逆な部分に限られる。その実在、許容line半空間、corner条件や相対flat性が破れる境界を調べる。中央因子のないA0認識、他のOU型、全GIT境界は未解決。AOU/OUにある古典的Weyl商と、本稿のT8上の有理Weyl作用・中心切断の例外性の導出を一次資料で比較し、公表上の新規性を確認する。

現在の方針は、具体的な有限Weyl商を、内在的相対モジュライとの比較の候補として使うことである。元の目標のうち、定義・複素点fiber・形式持上げ・代数的な商モデルは得た。未解決の核心は、これらを同じ族のモジュライとして同定することにある。一般のO例外性が未解決だからといって、中央因子locusで解決した結果を制限し直さない。

## V. 再現

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 computations/verify_weyl_frames.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

組版環境はLuaLaTeX、`ltjsarticle`、Haranoaji。TeX Liveの `scheme-basic` に `luatexja haranoaji mathtools booktabs jknapltx rsfs xkeyval fontspec lualatex-math` と依存パッケージを追加すればよい。出力は `build/nc-cubic-unmark.pdf`。bundleには `pdf/nc-cubic-unmark.pdf` と必要な全ソースを入れ、GitにPDF/ZIPを追跡しない。実行検証とその限界は `research/unmark_validation.json` に記す。本文に証明があることと、当該版の計算・組版・GitHub反映・Library保存が完了したことは別の状態であり、成功は各確認後にのみ記録する。
