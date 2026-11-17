# 研究方針：線束の数値的分類からの標識忘却

**2026-11-18 / unmark-v7。最初に本ファイルを読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md` を読む。GitHub `uedakazushi/nc-cubic-unmark` の main が原稿正本。最新 bundle だけで研究内容と再現手順を理解できる構成を保つ。

## I. 恒常的な研究原則・保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合し研究全体の価値を最大化する。方針は現行の目標・理由・到達点・未解決点として書き直し、時系列の履歴を積まない。既知結果、本稿に証明を記載した結果、今回の証明点検、仮定付き主張、予想、有限計算を区別する。仮定・依存文献・証明所在・未確認箇所を明示し、誤りがあれば依存先の本文・要約・方針も直す。原稿は日本語 LuaLaTeX。有効な数学的成果と証明は現行論文に保持し、経緯ではなく理解しやすい順序で構成する。

先行研究は一次資料を確認し、Introduction で既知結果と本稿の関係を具体的に説明する。未確認の書誌や新規性を推測しない。研究ノートは現在有用な例、反例、障害、再取得困難な情報を整理し、本文の証明を重複させない。

**ユーザーは研究の区切りごとに、承諾なく現行の研究継続 bundle を Library に保存する一般許可を与えている。** bundle は現行の方針・ノート・論文・必要な全ソース・PDF・コード・書誌・再現手順のみを収録する。旧版ZIP、旧原稿、バックアップ、ログ、キャッシュ、編集履歴、重複、外部論文PDFの大量収録を避ける。軽量化で数学的内容や検証可能性を削らない。Library 既存ファイルの削除は別操作であり明示指示なく行わない。日付と版を揃え、生成・計算・組版・GitHub反映・Library保存を別々に検証する。未実行検証や保存失敗はそのまま報告する。

## II. 現在の中心問題と達成基準

最上位目標は AOU 関係式モジュライと無標識 Abel 圏の関係を公表可能な定理にすること。**現在の最優先は、固定 nc cubic の各数値的線束類 `v_D=(1,D,D²/2)` に対する rank-one torsion-free 対象の存在・一意性である。** その後に weak marking の豊富性・切断数を検証し、exact 自己同値の軌道を求める。

この優先順位の理由は、忘却の形式的な商記述だけでは、そのファイバーを成す対象を分類したことにならないため。既存の普遍関係式代数・数値Serre–E6・形式chart・Picard障害の成果はすべて保持し、入力と障害として使う。ambient認識は別リポジトリ `uedakazushi/nc-cubic-ambient` の課題。

重要な文献上の到達点：Rains の非可換有理曲面では各因子類の線束の存在は既知である。従って「その全クラスでの存在」を新しい未解決問題とみなさず、**AOU の指定された heart が Rains の heart と exact に同定できる範囲**を明らかにする。

## III. 主張の状態・所在

中心節は `papers/sections/line_bundle_classification.tex`。

- **内在的証明を記載・今回点検**：現行の弱標識公理の下で、rank-one torsion-free E の非零射は単射、End(E)=C、Hom(E,H^{-b}E)=0 (b>0)、Ext²(E,E)=0。従って exceptional ⇔ χ(E,E)=1（`thm:intrinsic-line-criterion`）。E 自身の豊富性は仮定せず、既存O0の豊富性と切断数の二次増大を用いる。Rains の既知判定と同じ現象であり新規性は未確定。
- **追加仮定付き・証明記載**：三次曲面型RR表示と数値H作用を仮定すると欠損 n=D²/2−ch₂≥0、dim Ext¹(E,E)=2n（`cor:line-numerical-defect`）。さらに (EP): torsion T∈A1 に対し (−K)c1(T)≥0 を仮定すると、同次数の二対象間の Ext² が消え、各 v_D で高々一つ（`thm:numerical-line-uniqueness`）。数値E6だけから (EP) は出ない。
- **既知結果の帰結**：Rains arXiv:1907.11301v1 Cor.7.10, Prop.10.13 から、Rains の意味の非可換有理曲面では線束の同型類 ↔ NS(X)。同一類の一意性の既知比較は arXiv:2107.13540v2 Prop.5.14（`thm:rains-line-classification`）。非有理quasi-ruledのPic0付き分類と混同しない。
- **既知結果からの適用・条件付き**：Q=−K がnef cone内部、Q²=3 のRains模型では全線束がAZ豊富性と三次曲面切断数を満たす。rank/torsionの意味が本稿のGabriel–Krull条件と一致すれば全線束=全許容構造対象（`prop:rains-weak-admissibility`）。このrank比較とAOU心のexact比較は全域では未完。
- **証明記載・十分条件**：消滅と生成を持つ列を同定する導来同値はt-exact（`lem:ample-heart-transfer`）。AOU–Rains比較への具体的適用は未実施。AZの生成条件だけで交差Ext消滅を先取りしない。
- **相対仮定付き既存結果**：許容Artin変形では可換特殊fiberの各線束は一意に持ち上がる（`thm:formal-structure`）。全因子類で共通の代数的開部分への拡張は別問題。
- **既存の論文成果を保持**：普遍45次元・gldim2関係式代数とArtin形式完備性、支持階数ρからHH¹=10−ρ, HH²=18−ρ、全点の数値Serre–E6、G_Qの数値的自明作用（`aou_universal_algebras.tex`, `generic_hearts_numerical_boundary.tex`）。Rains比較の代替にはならない。
- **既存の条件付き結果を保持**：DDLによる可換点の形式Abel chart、Picard形式作用、δπの一般rank4と非常に一般の整数核ZK、許容一次変形での構造対象軌道Pic/ZK=Z6、一次線形不変式環C[P]。全GITへの作用・降下や全境界のheartは未証明。

## IV. 優先順位の高い次の課題

1. **AOU–Rains heart比較**：OU arXiv:2508.04986v1 p.8 の導来同値を取り、対応する構造対象または標準線束の像を特定。反標準列の像がRainsの線束列になることと両側のacyclic生成を確認し、`lem:ample-heart-transfer` を適用する。単に導来同値があるという記述で代用しない。
2. **rankと正値性**：Rainsの数値rank/torsion filtration と本稿のA0,A1の一致を証明する。Rains側で torsion のc1が有効、−Kがnefなら (EP) が従う。一般内在的モデルでは (EP) の独立性を調べる。
3. **実現集合Ω_Aと許容性**：exact比較を得た範囲では既知存在を移送し、Ω_A=Λ、Line_adm=Lineを結論する。比較外では個別数値類の構成から進める。一意性は存在の代替でない。自己同値軌道は最後に調べ、線束による異なる模型へのMorita同値と固定模型の自己同値を分ける。
4. **公表品質**：新規性の重心を、既知の線束分類そのものではなくAOU表示・heart・弱標識への比較に置く。一次資料参照、仮定、例、結論を整合させる。相対族・スカラー慣性・GIT降下は完成扱いしない。

## V. 再現

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

出力PDFは `build/nc-cubic-unmark.pdf`。bundleは `pdf/` に組版済みPDFを収録するがGitにはPDF/ZIPを追跡しない。書誌と具体的参照箇所は主論文と研究ノート、今回の検証範囲は `research/unmark_validation.json` にある。
