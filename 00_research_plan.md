# 研究方針：反標準 heart における二段階の標識忘却

**2026-11-18 / unmark-v10。最初に本ファイルを読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md`。GitHub `uedakazushi/nc-cubic-unmark` の main をソース正本とする。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究全体の価値を最大化する。方針は現時点の目標・到達点・理由・未解決点として書き直し、時系列の履歴を積まない。既知の結果、証明記載、今回の証明点検、追加仮定付きの結果、未完成・予想・計算的観察を区別する。主要な主張の仮定、依存文献、証明所在、未確認点を明記する。誤りは依存する本文・要約・方針も訂正する。

論文は日本語LuaLaTeXで現在の成果を論理順に配置し、有効な証明を保持する。先行研究は一次資料で照合し、Introductionで既知入力と寄与を区別する。未確認の新規性・書誌を推測しない。ノートは作業日誌ではなく、現在有用な例・反例・障害・着手方法をまとめ、論文の証明を重複させない。

**ユーザーは研究の区切りごとに、承諾なく現行の研究継続bundleをLibraryに保存する一般許可を与えている。** bundleは現行の方針・ノート・論文・必要な全ソース・PDF・書誌・計算コード・再現手順だけで自己完結させる。旧ZIP・旧原稿・バックアップ・ログ・キャッシュ・変更履歴・重複を含めず、軽量化で数学的内容や検証可能性を損なわない。Library既存ファイルの削除は別操作であり明示指示なく行わない。生成・検証・GitHub反映・Library保存を別々に確認し、未実行や失敗はそのまま報告する。日付・版・参照先を揃える。

## II. 本研究の対象と最優先課題

**基準の心は anticanonical heart。別の心として扱うのは AS heart のみ。Rains/VdB heart は本研究の議論・比較対象から外す。**

反標準環 `R_e=⊕ Hom(e,H^n e)`、`H=S^{-1}[2]` から `A_ac=qgr R_e` を取る。既存Abel圏で `(e,H)` がAZ ampleなら再構成によってこのheartと同定する。単にHがt-exactな任意のheartを名前だけでanticanonical heartにしない。AS表示との比較は、指定されたexact/t-exact比較または反標準再構成が確認された範囲に限定する。

中心の二段階は以下である。

1. **AOU/OU marking → weak marking**：固定した `(A_ac,L)` 上の標準標識の選択集合を、有限Weyl群 `W(E6)` の作用で記述する。数値標識の作用、実際のhelixとしての実現、網羅性、安定化群を分けて確認する。
2. **weakly marked → unmarked**：固定した `A_ac` 内のline bundleのchoiceを分類する。各数値的線束類 `v_D=(1,D,D²/2)` の存在・一意性と、全線束がweak標識として許容されることを優先する。

**まず集合論的に考える。** 固定圏内の線束の同型類集合 `Line_adm(A_ac)` を最初から `Aut_ex(A_ac)` で割らない。組のexact同値類を求める段階では、その集合への自己同値作用を別に計算する。群oid/stack、相対慣性、降下はその次の課題であり、現在の主問題の代替にしない。

この方針により、他のheartを経由する比較を中心課題から除き、二つの忘却の自由度に研究を集中させる。従来の内在的線束判定、一意性、可換・形式比較、Picard障害、有限代数と数値計算の有効な証明は現行原稿に保持する。対象範囲の異なる分類を、反標準heartの全線束存在定理として移し替えない。

## III. 現在の到達点と確実性

- **既知再構成の帰結**：許容線束Lなら反標準環R_Lのqgrは同じA_ac（`prop:ac-line-reconstruction`）。構造対象を交換する自己同値を与えるとはしない。
- **内在的線束判定・証明記載**：rank1tfのEnd=C、負H自己Hom=0、Ext²自己=0、exceptional iff χself=1（`thm:intrinsic-line-criterion`）。rank1tfだけから例外性は出ず、可換I_pが反例。
- **本稿で導出・今回独立点検**：weak公理、全対象上の三次曲面型RR/H作用、r(O0)=1から、任意MのExt^{>0}(O0,H^nM)=0 (n≫0)、Hilbert多項式、r≥0、A1={r=0}、rank1tfのr=1、有効次数正値性(EP)を導く（`thm:ac-serre-positivity`）。旧来のrank互換性と(EP)は独立仮定不要。A0⇒d=0は未証明。
- **一意性・証明記載と依存更新**：上の数値仮定だけでc1:Line(A)→Λが単射（`thm:numerical-line-uniqueness`）。Ω_A−K=Ω_AだがΩ_A=Λは未証明。内在的定義だけにRRを自動付与するとはしない。
- **第一段階の有限上界・今回証明**：AOU三ブロック線束型の九対象からK-frameを一意に復元し、Mark_Q^line(A,L)→F(Λ,K)は単射、標識数≤51840（`lem:weyl-frame-reconstruction`, `thm:weyl-frame-injection`）。一般OUの全very strong helicesへの上界ではない。
- **実現問題の還元・今回証明**：六単純反射の五つは直交ブロック内の置換。残るe3↔e4に対応する三対象交換を各標識で実現すれば、W(E6)-torsorとCoxeter関係・網羅性が従う（`cor:weyl-one-move`）。一般非可換点での交換の実現は未証明。
- **許容形式範囲**：特殊ファイバーでrank1tf性を保つAOU型相対線束標識は、通常の51840標識の一意な持上げで尽くされる（`cor:formal-all-line-markings`）。固定相対heartと特殊ファイバー同定を保持し、自己同値で割らないのでAut(X)=1不要。相対perfect底変更・helix生成等の入力は明記する。
- **条件付き障害・今回証明、実例未構成**：d=0でc1≠0のsimple Tが存在すれば、TはH不変のroot型であり、評価O0→T^cの核Eはline、R_E≅R_O0だが(E,H)はnon-ample（`prop:root-simple-obstruction`）。現公理の下でTが実在するとも不可能とも未証明。数値的点simpleへのLineのExt¹は両向きに消える（`lem:numerical-point-ext`）。
- **有効な補助結果を保持**：Picard一次障害δπ、一般rank4/非常に一般の整数核ZK、一次軌道Pic/ZKと不変式。付録の普遍45次元有限代数、HH支持公式、数値Serre–E6、AS locus、DDL形式比較。これらの仮定と証明は現行本文に保持し、全域線束存在の代替にしない。

新しい導出の証明を本文に記載し、独立の論理点検と数値検算を行った。外部査読・証明支援系による形式化・網羅的な優先権確認は未実施。既知の格子論・再構成定理と本稿の推論を区別する。一般の有限Weyl作用、全数値類の存在、全線束の許容性は完成した定理として扱わない。

## IV. 次の課題と具体的な着手

1. **三対象交換を構成する。** 九対象を(L,A,B;X1,X2,X3;Y1,Y2,Y3)とする。反射後の候補はB'=ker(X1⊕X2→Y1)、Y1'=coker(B→X1⊕X2)、X3'は[B→X1⊕X2⊕X3→Y1]の中間cohomology。まずAOUの一つの関係式で複体を作り、両端のexactness、rank1tf・χself=1、fullness・very strongnessを示す。数値式は検算済み、実際の対象は未構成。詳細は研究ノート。
2. **Line_adm=Lineの障害を調べる。** 零次数root型simpleが反標準heartの公理で排除されるかを先に調べる。数値的点へのExt消滅を正次数torsionへ拡張し、生成条件へ結ぶ。Hilbert関数や反標準切断環の一致だけを豊富性の証明にしない。
3. **数値的線束類の存在を構成する。** Ω_Aを決定する。既存一意性は用いてよいが、未知のv_Dの対象を形式的に操作して存在したと扱わない。可換点と許容Artin近傍の全線束を基準にし、個々の開条件の可算交叉をZariski開としない。
4. 必要な箇所だけAS heartとA_acを比較し、構造対象・反Serre作用・生成列を追う。以上を解いた後にAut_ex軌道、さらにgroupoid/stack・相対族へ進む。

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

PDFは `build/nc-cubic-unmark.pdf`。bundleには `pdf/nc-cubic-unmark.pdf` と必要な全ソースを入れ、GitにはPDF/ZIPを追跡しない。実行検証とその限界は `research/unmark_validation.json` に記す。
