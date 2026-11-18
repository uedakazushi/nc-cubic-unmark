# 研究方針：反標準 heart における二段階の標識忘却

**2026-11-18 / unmark-v12。最初に本ファイルを読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md`。GitHub `uedakazushi/nc-cubic-unmark` の main をソース正本とする。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。方針は現時点の目標・到達点・理由・未解決点として書き直し、時系列の履歴を積まない。既知の結果、証明記載、今回の証明点検、追加仮定付きの結果、未完成・予想・計算的観察を区別する。主要な主張の仮定、依存文献、証明所在、未確認点を明記する。誤りは依存する本文・要約・方針も訂正する。

論文は日本語LuaLaTeXで現在の成果を論理順に配置し、有効な証明を保持する。先行研究は一次資料で照合し、Introductionで既知入力と寄与を区別する。未確認の新規性・書誌を推測しない。ノートは作業日誌ではなく、現在有用な例・反例・障害・着手方法をまとめ、論文の証明を重複させない。

**ユーザーは研究の区切りごとに、承諾なく現行の研究継続bundleをLibraryに保存する一般許可を与えている。** bundleは現行の方針・ノート・論文・必要な全ソース・PDF・書誌・計算コード・再現手順だけで自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・変更履歴・重複を含めず、軽量化で数学的内容や検証可能性を損なわない。Library既存ファイルの削除は別操作であり明示指示なく行わない。生成・検証・GitHub反映・Library保存を別々に確認し、未実行や失敗はそのまま報告する。日付・版・参照先を揃える。

## II. 本研究の対象と達成基準

基準は **anticanonical heart** `A_ac=qgr R_e`、`H=S^{-1}[2]`。比較する別のheartは **AS heartのみ**。Rains/VdB heartは議論に用いない。Hのt-exact性だけで任意のheartを反標準heartと呼ばず、豊富対による再構成または指定されたexact比較を保持する。

中心は二段階の集合論的分類である。

1. 固定した弱標識 `(A_ac,L)` 上の標準Euler型を持つfull very strongなAOU三ブロック標識を有限Weyl群 `W(E6)` で記述する。九対象の線束性も認識する。
2. 固定した `A_ac` 内の許容線束を数値Picard格子 `Λ=I_{1,6}` で分類し、その後、圏のexact同値類を点とする忘却写像のfiberを求める。

固定圏内の対象の同型類と、圏の自己同値による同一視は集合論の段階から区別する。標準AOU relation torusのvery generalな点では、前者は `W(E6)` のtorsorと `Λ`、後者は `W(E6)` のtorsorと `Λ/ZK≅P(E6)` である。後者の第二fiberが生のPicard格子ではないのは、Hの冪が必ずK方向を同一視するためである。群oid/stack・慣性・降下はこの集合論的問題の後に扱う。

標準AOU relation torusの稠密開部分 `U` について、指定反標準heartのweak公理・全対象のRR/H作用・相対perfect比較を確認し、very-general定理を実際に適用するという達成基準は満たした（`sec:aou-heart-recognition`, `thm:actual-aou-very-general`）。忘却写像の定義域は、weak公理と指定AS/反標準heart比較に適合する標準AOU・full very strong標識の最大の範囲 `M_Q^ac` とする（`def:maximal-weak-compatible-aou`）。証明用に選んだ開部分 `U` へmarked側を恣意的に縮めると別のWeyl標識を落とし得るため、`U` とfiberの定義域を区別する。一般OUの全型や全GIT境界はこの定理の対象としない。

## III. 現在の到達点と証明の状態

以下の到達点には本文に証明を記載する。今回追加した右tail認識、実際のAOU heart構成、階数・有限長認識、代数族への適用は独立に論理点検した。保持した既存証明すべてを今回再査読したという意味ではない。既知再構成・変形・格子論と本稿の推論を区別する。外部査読、証明支援系による形式化、網羅的な新規性確認は未実施。

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
- **実際のvery-general自己同値像とfiber**：八次元の標準AOU relation torusにはAut(X)=1の可換点と整数核ZKのPoisson接方向を選べる。全係数非零のrelation商を八つの明示的torus不変式で記述し、可算個の数値ラベルごとにEnd代数の等化子が真閉となることから、very generalに `Γ_A=ZK`（`thm:very-general-numerical-aut`, `thm:actual-aou-very-general`）。generic自己同値自体の特殊化は不要。最大のweak適合標準AOU定義域では第一fiberは51840点のW(E6)-torsor、第二は `Λ/ZK≅P(E6)`。数値的に自明な自己同値群そのものの分類は含まない。
- **許容Artin底の全次数**：Aut(X)=1と、整数核がZKの一次Poisson方向を持つ許容相対変形では、特殊化自己同値像はちょうどZK。第一fiberはW-torsor、第二はPic/ZK。compatible形式塔にも成立（`thm:artin-actual-fibers`, `cor:first-order-pointings`）。分数体の任意の自己同値を特殊化できるとは主張しない。

有効な可換・形式比較、Picard一次障害・整数核・不変式、普遍有限代数、HH/Serre数値計算を現行本文・付録に保持する。線束持上げとtensor自己同値持上げを混同しない。

## IV. 未解決の核心と次の着手

1. **特殊locusの線束とroot simple。** 中心楕円因子を持つUではGabriel--Krull filtrationを数値的に認識できた。次は零次数root simpleの実在・排除を調べ、部分的な線束実現集合Ω_Aと許容半空間条件の関係を決定する。曲線の点層は非零self Ext¹を持ち、exact fully faithfulな商環からの制限がその拡大を保つため、rigidなroot simpleは中心元が可逆に作用する部分に限られる（`cor:root-simple-off-divisor`）。この部分のsimpleと線束に対する評価射から実在条件を追う。root affine反射は先頭Lを動かすので、固定L上の有限W作用とは別である。中心因子を仮定しない抽象weak heartではA0⇒d=0も残る。
2. **最大weak適合locusの幾何学的境界と作用。** 証明に用いたUは全適合範囲の一部である。有限余次元corner条件、noetherian性、AS/反標準比較、weak公理のどこが境界で失われるかを分けて調べる。三対象交換のkernel・cokernel・cohomology構成を相対化し、有限Weyl作用がどこまで代数的・正則に定義されるかを追う。一般OUの全Euler型や全GIT境界の分類を現在の結果へ読み込まない。
3. **先行研究との精密な比較と公表上の位置。** AOU/OUの標識moduli、Minamoto–MoriとAmiotの導来・corner比較、既存の非可換del Pezzo線束分類を一次資料で照合し、仮定と対象範囲の差、新たな導出の優先権を確定する。有限Weyl格子論・AZ再構成・相対持上げ理論そのものは既知入力として扱う。
4. **集合論の後の精密化。** 特殊locusと最大定義域を見極めた後、数値自明な自己同値、相対降下、groupoid/stackを扱う。very-general fiberの集合論的結論はその前提として保持する。

標準AOU relation torusの非常に一般の点については、全線束の存在・許容性、標準helixの線束認識、自己同値の数値像、二段階の実際のfiberがまとまった。現在の中心課題はこの結論を一律に全境界へ広げることではなく、特殊locusの具体的な障害と最大適合範囲の構造を理解することである。

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

出力は `build/nc-cubic-unmark.pdf`。bundleには `pdf/nc-cubic-unmark.pdf` と必要な全ソースを入れ、GitにPDF/ZIPを追跡しない。実行検証とその限界は `research/unmark_validation.json` に記す。本文に証明があることと、当該版の計算・組版・GitHub反映・Library保存が完了したことは別の状態であり、成功は各確認後にのみ記録する。
