# 研究方針：構造対象・quiver 標識と忘却射のモジュライ

**2026-11-19 / unmark-v13。最初に本ファイルを読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md`。GitHub `uedakazushi/nc-cubic-unmark` の main をソース正本とする。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。方針は現時点の目標・到達点・理由・未解決点として書き直し、時系列の履歴を積まない。既知の結果、証明記載、今回の証明点検、追加仮定付きの結果、未完成・予想・計算的観察を区別する。主要な主張の仮定、依存文献、証明所在、未確認点を明記する。誤りは依存する本文・要約・方針も訂正する。

論文は日本語LuaLaTeXで現在の成果を論理順に配置し、有効な証明を保持する。先行研究は一次資料で照合し、Introductionで既知入力と寄与を区別する。未確認の新規性・書誌を推測しない。ノートは作業日誌ではなく、現在有用な例・反例・障害・着手方法をまとめ、論文の証明を重複させない。

**ユーザーは研究の区切りごとに、承諾なく現行の研究継続bundleをLibraryに保存する一般許可を与えている。** bundleは現行の方針・ノート・論文・必要な全ソース・PDF・書誌・計算コード・再現手順だけで自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・変更履歴・重複を含めず、軽量化で数学的内容や検証可能性を損なわない。Library既存ファイルの削除は別操作であり明示指示なく行わない。生成・検証・GitHub反映・Library保存を別々に確認し、未実行や失敗はそのまま報告する。日付・版・参照先を揃える。

## II. 本研究の対象と達成基準

**主目標は、構造対象を指定する O-marking と、rolled-up quiver Q を持つ full very strong exceptional collection を指定する Q-marking のモジュライ、および忘却射 p:M^Q→M^O とその fiber を定義・記述することである。** 固定圏内の標識集合、基礎点との同定を保持する2-fiber、同型類集合のfiberを区別する。複素点の群oidと一般fiberの記述には到達し、次は実際の代数族との比較と相対幾何を中心に進める。

採用する最小のO-markingは、noetherian Abel圏A、Hom有限なDb(A)のSerre作用H=S^{-1}[2]、H(A)=A、GK filtrationでrank1 torsion-freeなO、AZ豊富対(O,H)、三次曲面型の反標準Hilbert級数からなる。Oの例外性は仮定に含めず、smooth proper enhancement・数値Picard格子・ambient表示も独立に扱う（`def:o-marked-cubic`）。AZ再構成によりAはqgr R_Oとなるため、基準はanticanonical heartである。比較する別の表面heartはAS heartのみ。構造対象をテンソル単位とみなさない。

Qは頂点の順序・先頭頂点・cut次数を含むrolled-up quiver。有限foundation R=End(⊕E_i)とB=⊕Hom(⊕E_i,H^n⊕E_i)を区別し、Bのaugmentationに関する最小表示kQ/Iを要求する。矢・関係・potentialの基底は標識に含めない（`def:q-marking`）。先頭E1は構造対象であり、残りの対象のheart所属はvery strongnessから導く。

標準AOU型では、Q-markingの存在から比較用weak公理と全対象RR/H構造を導く。さらに零次数root非存在条件(R0)と非空性の下で、固定(A,O)の標識集合はW(E6)-torsor。rawな2-fiberは51840個のB(Gm^8)の非交和、成分スカラーを除いた2-fiberは51840点、同型類集合のfiberはΓ_O\W(E6)である。exact自己同値の数値作用はこの範囲で忠実なので、Γ_Oは実際のO-pointed自己同値群と同型である。

実際の標準AOU relation torusのvery general点では、全許容線束の数値類がΛ、Aut_ex(A)=〈H〉≅Z、Aut_ex(A,O)=1であり、同型類集合の第一fiberも51840点となる。保持する第二の忘却結果Λ/ZK≅P(E6)は、**例外的構造対象の部分**のfiberである。最小O-markingの全体で例外性が従うことは未証明であり、第二fiberを無条件に全体へ広げない。

これらの点ごとの結果を代数スタックの存在や有限étale射の証明と同一視しない。relativeモデルの選択、heart・Serre・基底変換、降下、rigidificationの仮定を次の課題として明示する。証明用の小さい開Uと、全Weyl標識を含む飽和した定義域は異なる。一般OUの全quiver型や全GIT境界の分類は現結論に含めない。

## III. 現在の到達点と証明の状態

以下の到達点には本文に証明を記載する。今回の論理点検は最小O公理、Qの最小表示からEuler形式への導出、RRを使わないhelixのheart認識、群oidのfiber・慣性、Oの欠損比較、exact自己同値の数値作用の忠実性を中心とする。既存のvery-general線束存在の主要な依存関係も点検したが、保持した全証明の新たな独立再査読を意味しない。既知再構成・Morita理論・変形・格子論と本稿の推論を区別する。外部査読、証明支援系による形式化、網羅的な新規性確認は未実施。

- **最小構造対象と例外性の差**：定義からhdim A=2、負自己twistのHom消滅、非負自己twistのExt²消滅、中心Cを導く（`lem:o-minimal-consequences`, `lem:dimension-centre`）。既存のweak/RR heart内の構造対象はδ=D²/2−ch₂≥0を持ち、Ext¹(O,H^mO)=2δ (m≥0)。δ=0、例外性、正自己twist消滅、旧許容線束が同値（`prop:o-marking-defect-comparison`）。I_pは自己HomのHilbert条件を満たすがAZ生成を満たさず、最小O公理全体の反例ではない。
- **RRなしのheart認識**：構造対象からの全非負自己twist高次Ext消滅は、AZ生成とhdim2により全対象のeventual Serre消滅を与える。これが反標準Homによるheart検出を与え、very strong helixの全対象がAに入る（`lem:o-ample-serre-vanishing`, `prop:o-helix-heart-recognition`）。一般の豊富対だけに高次Ext消滅を読み込まない。
- **quiverから数値構造へ**：標準27矢rolled-up quiverのcut0部分は18矢三層代数。まずgldim≤2を示し、Kellerの未変形3-CY completionの最小逆関係矢を比較して九つの独立関係、dim R=45、標準Euler行列を得る（`prop:aou-quiver-euler-recognition`）。一つのQ-markingからsmooth proper性、O例外性、K0=Knum、全対象RR/Hと内在的rankを導く（`cor:q-marking-numerical-inputs`）。全係数非零には(R0)を別に使う。
- **モジュライとfiber**：M^O、M^Q、M^{Q,rig}を複素点の群oidとして定義。2-fiberは標識集合で添字付けられたB(Gm^{ell−1})、rigidified fiberは離散標識集合、π0のfiberはO-pointed自己同値軌道（`thm:q-o-fiber-groupoids`）。絶対慣性には中央拡大があるが、一般の分裂やglobalな積gerbeを主張しない（`prop:q-marking-scalar-inertia`）。étale site上の相対定義はモデルを指定してstackificationを取る。代数性・相対finite étale性は未証明。
- **数値作用の忠実性**：標準Q-marking存在+(R0)の下で、数値的に恒等のexact自己同値は各E_iを固定する。全係数非零関係のarrow rescalingはvertex innerに限られ、exact関手のdg liftとMorita bimoduleからF≅idを導く（`prop:q-numerical-auto-faithful`）。Aut_ex(A)↪Λ⋊W、O安定化群↪W、その標識集合への作用は自由。very generalにはAut_ex(A)=〈H〉、pointed群=1。抽象的な任意のtriangulated自己同値や、rootを持つ全圏への主張ではない。
- **内在的線束判定と数値一意性**：weak公理、全対象上の三次曲面型RR/H作用、r(O0)=1から、Serre消滅、A1={r=0}、有効次数正値性を導く。rank1tfのEnd=C、Ext²self=0、欠陥n≥0、Ext¹self=2n。例外性はn=0と同値で、c1でlineが一意（`thm:intrinsic-line-criterion`, `thm:ac-serre-positivity`, `thm:numerical-line-uniqueness`）。rank1tfだけでは例外性は出ず、可換I_pが反例。抽象weak heart全体でのA0⇒d=0は未証明だが、中心楕円因子を持つ実際のAOU locusでは以下の認識結果が成立する。
- **許容性の判定**：有限個の負H-twist of LからO0への全射と、全m≥0の正自己twist高次Ext消滅が、Lのweak許容性と同値（`prop:line-admissibility-test`）。
- **root型simpleの条件付き構成**：零次数root simple T=(0,C,s)が存在する場合、a=s−D·CについてHom(L,T)=max(a,0)、Ext¹(L,T)=max(−a,0)。評価核・普遍拡大によりline集合に反射D↦D−aCを構成し、反標準切断環を保つ。許容線束はa>0を満たす（`thm:root-line-reflection`, `cor:admissible-root-halfspace`）。Tの実在も一般的な排除も主張しない。全Λの許容lineがあればTは排除される。
- **有限Weyl作用の実現**：零次数simpleのc1が全て零という条件(R0)の下で、B′=ker(X1⊕X2→Y1)、Y1′=coker(B→X1⊕X2)、X3′=三項複体の中間cohomologyを構成。line性・fullness・very strongnessを証明し、非空な標準標識集合はW(E6)-torsor（`thm:rootfree-cross-reflection`）。一般OUの全helixの分類ではない。
- **AS比較と有限表示**：full very strong helixが一つのAZ豊富な周期部分列を含めば、helix全体が豊富で、そのZ代数は右noetherian。Polishchuk再構成によりAS heartは元の反標準heartにexact同値（`lem:ample-helix-reconstruction`, `cor:line-helix-as-reconstruction`）。(R0)では有限End代数は十八矢・九関係のAOU表示を持ち、全関係係数が非零（`lem:rootfree-aou-presentation`）。
- **標準helixの線束認識**：条件(R0)の下で、数値階数一、End=C、右反標準tailへのExt¹消滅からtorsion-free性を導く（`prop:right-tail-torsionfree-recognition`）。許容先頭Lを持つ標準Euler型のfull very strong helixでは、heart所属、数値階数一、右tail消滅が自動的に成立するため、九対象が全て線束となる（`thm:aou-helix-line-recognition`）。固定root-free weak heart上では `Mark_Q^vs=Mark_Q^line` であり、第一fiberを線束型の部分集合に限定する必要はない。
- **実際のAOU locusのheart認識**：楕円decupleに由来する稠密locus上でcompletion次数のrolled-up代数Bに正則中心元zを構成し、曲線商からnoetherian性を得る。`dim B/BeB<∞` を可換点で成立する有限次数の開条件として確保し、`qgr B≃qgr(eBe)` を得る。Minamoto–Moriの通常の有界導来圏比較、直接のAZ豊富性、曲線因子による内在的階数認識により、実際の非空開集合U上でweak公理を確認する（`sec:aou-heart-recognition`, `cor:actual-aou-weak-heart`）。全対象のRR/H作用は有限AOU代数の一定Euler格子から輸送される（`prop:aou-full-rr-transport`）。
- **実際のAOU locusの零次元層**：中心楕円因子を持つUでは `A0={r=d=0}`、`A1={r=0}`、`A2=A`（`prop:elliptic-divisor-length-recognition`）。単純対象への中心元の作用を同型の場合と零の場合に分け、前者はHilbert多項式の周期性、後者は曲線上の点層から次数零を導く。曲線商の点層の非零自己拡大は保たれるため、root simpleは中心元が可逆に作用する部分へ限定できる（`cor:root-simple-off-divisor`）。抽象weak公理だけに一般化してはいない。
- **very-general存在定理と実際の適用**：有限局所自由代数族と相対perfect比較を滑らかな既約底全体に持ち、weak反標準heartを稠密開Uと可換基準点b0で持てば、very generalに `Line_adm=Line≅Λ`、かつ全L上の標準標識が非空なW(E6)-torsor（`thm:very-general-line-existence`）。`b0∈U` は不要。projective複体の代数化、単射・全射のwitnessと可算個のheart/消滅条件を用いる。標準AOU relation torusでは上記のheart認識と普遍有限代数によって全入力が確認できる。
- **集合論的な実際のfiber**：full標識があればexact自己同値の数値像Γ_AはΛ⋊W(E6)の部分群で、中心のZKを含む。全line・標識の存在範囲で第一fiberはΓ_L\W、第二はΛ/Γ_A=(Λ/ZK)/barΓ_A（`prop:affine-auto-action`, `cor:actual-set-fibers`）。「set theoretic」でも自己同値による同一視は残る。
- **実際のvery-general自己同値像とfiber**：八次元の標準AOU relation torusにはAut(X)=1の可換点と整数核ZKのPoisson接方向を選べる。全係数非零のrelation商を八つの明示的torus不変式で記述し、可算個の数値ラベルごとにEnd代数の等化子が真閉となることから、very generalに `Γ_A=ZK`（`thm:very-general-numerical-aut`, `thm:actual-aou-very-general`）。generic自己同値自体の特殊化は不要。最大のweak適合標準AOU定義域で同型類集合の第一fiberは51840点のW(E6)-torsor、例外的構造対象に限った第二fiberは `Λ/ZK≅P(E6)`。上の忠実性命題を合わせると、このlocusでは自己同値群自体が〈H〉≅Zとなり、O-pointed群は自明である。
- **許容Artin底の全次数**：Aut(X)=1と、整数核がZKの一次Poisson方向を持つ許容相対変形では、特殊化自己同値像はちょうどZK。第一fiberはW-torsor、第二はPic/ZK。compatible形式塔にも成立（`thm:artin-actual-fibers`, `cor:first-order-pointings`）。分数体の任意の自己同値を特殊化できるとは主張しない。

有効な可換・形式比較、Picard一次障害・整数核・不変式、普遍有限代数、HH/Serre数値計算を現行本文・付録に保持する。線束持上げとtensor自己同値持上げを混同しない。

## IV. 未解決の核心と次の着手

1. **実際の族と内在的モジュライの比較。** AOUの関係式表示[R_good/G_18]から相対qgr、構造対象、指定helixを構成する。有限余次元corner、noetherian性、perfect HomとSerre、基底変換・heartの両立、exact同値の降下を確認し、`def:relative-marked-moduli` のモデルを具体化する。次の作業は相対corner比較と豊富対を保つ局所同型の降下から始める。証明用開Uをそのまま全fiberの定義域にせず、Weyl標識変更で飽和させる。
2. **rigidificationと相対忘却射。** vertexスカラーGm^8が平坦・有限表示の相対慣性部分群となることを確認し、Stacks Tag04V2の仮定を満たしてrigidificationを構成する。Q側の関係式商と内在的群oidを比較した後、O側の代数性とrigidified射の表現可能性を証明する。三対象交換のkernel/cokernel/中間cohomologyを相対化し、rootのない範囲での有限étale性と次数51840を調べる。点ごとの51840や形式的な一意持上げだけではpropernessや全familyの有限性を結論しない。
3. **忘却像と最小O公理。** 最小公理からExt¹(O,O)=0が従うかを先に調べる。既知RR heartでは欠損δに帰着するので、AZ生成とδ>0の両立を検討する。I_pは生成に失敗するため反例として使わない。その後、例外的Oから標準Q collectionが存在する条件を求める。特殊locusのroot simple、部分的許容類集合、許容半空間はこの像を理解する補助問題として保持する。
4. **境界・他型・公表上の位置。** 中心楕円因子locusではroot simpleは中心元が可逆に作用する部分に限られる。そこでの実在条件と、corner/豊富性/AS比較が失敗する境界を分けて調べる。中心因子なしのA0⇒d=0、他のOU quiver型、全GIT境界は未解決。AOU/OU、Keller/Toën、既存nc del Pezzo分類との一次資料比較を進め、各追加導出の優先権と公表価値を確認する。

今の研究方針は、定義と複素点のfiberを基礎として相対モジュライの幾何に進むことである。以前の集合論的結果はこの基礎として保持し、例外性の範囲を越えて主張を拡張しない。

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
