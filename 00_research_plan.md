# 研究方針：反標準 heart における二段階の標識忘却

**2026-11-18 / unmark-v11。最初に本ファイルを読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md`。GitHub `uedakazushi/nc-cubic-unmark` の main をソース正本とする。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。方針は現時点の目標・到達点・理由・未解決点として書き直し、時系列の履歴を積まない。既知の結果、証明記載、今回の証明点検、追加仮定付きの結果、未完成・予想・計算的観察を区別する。主要な主張の仮定、依存文献、証明所在、未確認点を明記する。誤りは依存する本文・要約・方針も訂正する。

論文は日本語LuaLaTeXで現在の成果を論理順に配置し、有効な証明を保持する。先行研究は一次資料で照合し、Introductionで既知入力と寄与を区別する。未確認の新規性・書誌を推測しない。ノートは作業日誌ではなく、現在有用な例・反例・障害・着手方法をまとめ、論文の証明を重複させない。

**ユーザーは研究の区切りごとに、承諾なく現行の研究継続bundleをLibraryに保存する一般許可を与えている。** bundleは現行の方針・ノート・論文・必要な全ソース・PDF・書誌・計算コード・再現手順だけで自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・変更履歴・重複を含めず、軽量化で数学的内容や検証可能性を損なわない。Library既存ファイルの削除は別操作であり明示指示なく行わない。生成・検証・GitHub反映・Library保存を別々に確認し、未実行や失敗はそのまま報告する。日付・版・参照先を揃える。

## II. 本研究の対象と達成基準

基準は **anticanonical heart** `A_ac=qgr R_e`、`H=S^{-1}[2]`。比較する別のheartは **AS heartのみ**。Rains/VdB heartは議論に用いない。Hのt-exact性だけで任意のheartを反標準heartと呼ばず、豊富対による再構成または指定されたexact比較を保持する。

中心は二段階の集合論的分類である。

1. 固定した弱標識 `(A_ac,L)` 上のAOU標準三ブロック線束標識を有限Weyl群 `W(E6)` で記述する。
2. 固定した `A_ac` 内の許容線束を数値Picard格子 `Λ=I_{1,6}` で分類し、その後、圏のexact同値類を点とする忘却写像のfiberを求める。

固定圏内の対象の同型類と、圏の自己同値による同一視は集合論の段階から区別する。期待するvery-general像は、前者では `W(E6)` と `Λ`、後者では `W(E6)` と `Λ/ZK≅P(E6)`。後者の第二fiberが生のPicard格子ではないのは、Hの冪が必ずK方向を同一視するためである。群oid/stack・慣性・降下はこの集合論的問題の後に扱う。

達成基準は、AOU relation族の具体的な既約locusについて、指定反標準heartのweak公理・全対象のRR/H作用・相対perfect比較を確認し、本文の条件付きvery-general定理を適用できると示すこと。一般OUの全very strong helicesや全GIT境界は同じ定理の対象としない。

## III. 現在の到達点と証明の状態

以下の追加導出は本文に証明を記載し、今回独立の論理点検を行った。既知再構成・変形・格子論と本稿の推論を区別する。外部査読、証明支援系による形式化、網羅的な新規性確認は未実施。

- **内在的線束判定と数値一意性**：weak公理、全対象上の三次曲面型RR/H作用、r(O0)=1から、Serre消滅、A1={r=0}、有効次数正値性を導く。rank1tfのEnd=C、Ext²self=0、欠陥n≥0、Ext¹self=2n。例外性はn=0と同値で、c1でlineが一意（`thm:intrinsic-line-criterion`, `thm:ac-serre-positivity`, `thm:numerical-line-uniqueness`）。rank1tfだけでは例外性は出ず、可換I_pが反例。A0⇒d=0はなお未証明。
- **許容性の判定**：有限個の負H-twist of LからO0への全射と、全m≥0の正自己twist高次Ext消滅が、Lのweak許容性と同値（`prop:line-admissibility-test`）。
- **root型simpleの条件付き構成**：零次数root simple T=(0,C,s)が存在する場合、a=s−D·CについてHom(L,T)=max(a,0)、Ext¹(L,T)=max(−a,0)。評価核・普遍拡大によりline集合に反射D↦D−aCを構成し、反標準切断環を保つ。許容線束はa>0を満たす（`thm:root-line-reflection`, `cor:admissible-root-halfspace`）。Tの実在も一般的な排除も主張しない。全Λの許容lineがあればTは排除される。
- **有限Weyl作用の実現**：零次数simpleのc1が全て零という条件(R0)の下で、B′=ker(X1⊕X2→Y1)、Y1′=coker(B→X1⊕X2)、X3′=三項複体の中間cohomologyを構成。line性・fullness・very strongnessを証明し、非空な標準標識集合はW(E6)-torsor（`thm:rootfree-cross-reflection`）。一般OUの全helixの分類ではない。
- **AS比較と有限表示**：full very strong helixが一つのAZ豊富な周期部分列を含めば、helix全体が豊富で、そのZ代数は右noetherian。Polishchuk再構成によりAS heartは元の反標準heartにexact同値（`lem:ample-helix-reconstruction`, `cor:line-helix-as-reconstruction`）。(R0)では有限End代数は十八矢・九関係のAOU表示を持ち、全関係係数が非零（`lem:rootfree-aou-presentation`）。
- **条件付きvery-general存在**：滑らかな既約有限型底上の有限局所自由代数族、指定されたweak反標準heartと数値格子、相対perfect底変更・反Serre作用、可換三次曲面fiberを仮定すれば、very generalに `Line_adm=Line≅Λ`、かつ全L上の標準標識が非空なW(E6)-torsor（`thm:very-general-line-existence`）。個々のprojective複体を代数化し、単射・全射のwitnessと可算個のheart/消滅条件を用いる。実際のAOU族のheart比較が未確認な範囲をこの定理で解決済みにしない。
- **集合論的な実際のfiber**：full標識があればexact自己同値の数値像Γ_AはΛ⋊W(E6)の部分群で、中心のZKを含む。全line・標識の存在範囲で第一fiberはΓ_L\W、第二はΛ/Γ_A=(Λ/ZK)/barΓ_A（`prop:affine-auto-action`, `cor:actual-set-fibers`）。「set theoretic」でも自己同値による同一視は残る。
- **条件付きvery-general自己同値像**：有限AOU族と、Aut(X)=1・整数核ZKのPoisson接方向を仮定すると、Γ_A=ZK（`thm:very-general-numerical-aut`）。全係数非零のrelation商を八つの明示的torus不変式で記述し、可算個の数値ラベルごとにEnd代数の等化子が真閉となることを証明する。generic自己同値自体の特殊化は不要。第一fiberは標準三ブロック線束型でW-torsor、第二はΛ/ZK。
- **許容Artin底の全次数**：Aut(X)=1と、整数核がZKの一次Poisson方向を持つ許容相対変形では、特殊化自己同値像はちょうどZK。第一fiberはW-torsor、第二はPic/ZK。compatible形式塔にも成立（`thm:artin-actual-fibers`, `cor:first-order-pointings`）。分数体の任意の自己同値を特殊化できるとは主張しない。

有効な可換・形式比較、Picard一次障害・整数核・不変式、普遍有限代数、HH/Serre数値計算を現行本文・付録に保持する。線束持上げとtensor自己同値持上げを混同しない。

## IV. 未解決の核心と次の着手

1. **AOU族の反標準heart仮定を具体化する。** relation torusの普遍45次元代数を出発点に、相対反Serre双加群、標準九対象、O0部分列を追う。指定した反標準qgrとAS qgrを同定し、全対象のRR・階数・内在的torsion条件を確認する。一般有限代数のHH次元だけでweak公理を推論しない。
2. **全AOU標識の線束認識を示す。** 構成した標準線束標識がAOU型AS標識になることはsimple resolutionまで確認した（`prop:aou-simple-resolution`）。逆に任意のAOU型標識の九対象が固定反標準heartでrank1tfになることは未証明（`rem:aou-line-converse`）。Euler/Serreからの数値階数と、torsion-free性を分けて調べる。この逆向きなしには全AOU fiberをW軌道と断定しない。
3. **特殊locusの障害を理解する。** root simpleがweak公理の下で存在するか、またA0⇒d=0かを調べる。全クラス存在とは別に、部分的な実現集合Ω_Aと許容半空間条件の関係を追う。root affine反射は先頭Lを動かすので、固定L上の有限W作用とは別である。
4. 対象範囲と仮定の比較を一次文献で続け、新規性を確認する。集合論的結果が定まった後に相対降下・groupoid/stackへ進む。

三対象交換と、明示的代数族仮定の下の全線束存在・許容性は証明済みの到達点となったため、現在の優先課題はAOU族へのheart仮定確認と、全AOU標識の線束認識である。明示した族仮定の下のvery-general自己同値像は、有限関係式の等化子で決定できた。条件なしの全非可換locusの線束分類は残っている。

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

出力は `build/nc-cubic-unmark.pdf`。bundleには `pdf/nc-cubic-unmark.pdf` と必要な全ソースを入れ、GitにPDF/ZIPを追跡しない。実行検証とその限界は `research/unmark_validation.json` に記す。
