# 研究方針：反標準 heart における二段階の標識忘却

**2026-11-18 / unmark-v9。最初に本ファイルを読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md`。GitHub `uedakazushi/nc-cubic-unmark` の main をソース正本とする。

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

- **定式化・既知再構成の帰結**：`anticanonical_set_unmark.tex`。二段階の選択集合を定義。許容線束Lで `R_L` を作り直してもAZ再構成で同じA_acを得る（`prop:ac-line-reconstruction`）。これは環同型やLを交換する固定圏の自己同値を主張しない。
- **可換・許容形式範囲**：通常の標識は有限W(E6)で記述できる（`aou_to_unmarked.tex`, `commutative_formal_markings.tex`）。一般の非可換AOU/OU領域で全標識を尽くすことは未証明。AOU/OU部分が全weak cubicを尽くすとも主張しない。
- **内在的証明を保持**：rank1tfのEnd=C、負H自己Hom=0、Ext²自己=0、exceptional iff χself=1。三次曲面型RR表示と有効次数正値性(EP)の下で各数値的線束類の対象は高々一つ（`line_bundle_classification.tex`）。この推論に他のheartを使わない。新規性は未確認。
- **未解決の存在・許容性**：`Ω_A={D:v_Dを持つrank1tf対象が存在}`、`Line_adm=Line`。一意性からΩ_A=Λを結論しない。任意の線束の交差Ext消滅やAZ生成も未証明の範囲では条件として残す。
- **自己同値との区別のための補助結果**：Picard一次障害 `δπ(L)=H¹(π^sharp)c1(L)`、一般rank4、非常に一般の整数核ZK、許容一次変形での軌道Pic/ZK、一次不変式。線束選択と自己同値の持上げを区別するために保持（`picard_obstructions.tex`, `picard_invariants.tex`）。
- **付録に保持**：普遍45次元有限代数、Artin関係式変形、HH支持公式、一定の数値Serre–E6、AS locus、DDL形式比較。これらだけでA_acとAS heartの一致や標識の網羅性を結論しない。形式Abel変形が反標準heartの許容条件を満たす範囲は別に確認する。

今回の改稿は研究対象と順序の再整理が中心。有限Weyl商と全線束存在の新しい全域定理を証明したとはしない。既存の全証明を再査読したわけでもない。

## IV. 次の課題と具体的な着手

1. 固定 `(A_ac,L)` のAOU/OU標識を正規化し、標準単純反射ごとに対象の変換を記述する。Lを保持すること、Weyl関係、標識集合の網羅性を順に検証する。G_Qの矢基底変更をW(E6)作用と同一視しない。
2. A_ac内の数値的線束類の存在構成を進める。既存一意性にはRRと(EP)の適用を確認する。存在した線束の交差Ext消滅・AZ生成を調べ、Line_adm=Lineを示す。まず既知の可換点と許容形式近傍を基準にする。
3. 必要な箇所だけAS heartとA_acを比較する。構造対象・反Serre作用・生成列の同定を明記し、導来同値のみからexact同値を主張しない。
4. 以上の選択集合が決まってからAut_exによる軌道を分類する。groupoid/stackと相対族は後段とする。

## V. 再現

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

PDFは `build/nc-cubic-unmark.pdf`。bundleには `pdf/nc-cubic-unmark.pdf` と必要な全ソースを入れ、GitにはPDF/ZIPを追跡しない。実行検証とその限界は `research/unmark_validation.json` に記す。
