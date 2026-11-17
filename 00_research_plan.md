# 研究方針：線束の数値的分類からの標識忘却

**2026-11-18 / unmark-v8。最初に本ファイルを読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md` を読む。GitHub `uedakazushi/nc-cubic-unmark` の main が原稿正本。最新 bundle だけで研究内容と再現手順を理解できる構成を保つ。

## I. 恒常的な研究原則・保存許可

数学的重要性、新規性、理解の深化、応用、正確性、実現可能性を総合し研究全体の価値を最大化する。方針は現行の目標・理由・到達点・未解決点として書き直し、時系列の履歴を積まない。既知結果、本稿に証明を記載した結果、今回の証明点検、仮定付き主張、予想、有限計算を区別する。仮定・依存文献・証明所在・未確認箇所を明示し、誤りがあれば依存先の本文・要約・方針も直す。原稿は日本語 LuaLaTeX。有効な数学的成果と証明は現行論文に保持し、経緯ではなく理解しやすい順序で構成する。

先行研究は一次資料を確認し、Introduction で既知結果と本稿の関係を具体的に説明する。未確認の書誌や新規性を推測しない。研究ノートは現在有用な例、反例、障害、再取得困難な情報を整理し、本文の証明を重複させない。

**ユーザーは研究の区切りごとに、承諾なく現行の研究継続 bundle を Library に保存する一般許可を与えている。** bundle は現行の方針・ノート・論文・必要な全ソース・PDF・コード・書誌・再現手順のみを収録する。旧版ZIP、旧原稿、バックアップ、ログ、キャッシュ、編集履歴、重複、外部論文PDFの大量収録を避ける。軽量化で数学的内容や検証可能性を削らない。Library 既存ファイルの削除は別操作であり明示指示なく行わない。日付と版を揃え、生成・計算・組版・GitHub反映・Library保存を別々に検証する。未実行検証や保存失敗はそのまま報告する。

## II. 中心問題と現在の達成基準

最上位目標は、AOU 関係式モジュライから無標識 Abel 圏への忘却を、公表可能な定理にすること。固定圏で **数値的線束類ごとの存在・一意性 → weak 許容性 → exact 自己同値軌道** の順に調べる。数値的 E6 や抽象的な商の記述だけで対象の分類を代用しない。

Rains 模型の線束存在は既知である。本稿の重点はその分類を内在的定義と AOU heart へ接続することにある。現在、滑らかな反標準曲線 C の類 Q=−K が nef cone 内部、Q²=3 の Rains 非可換有理曲面では rank/torsion の二定義が一致し、全弱標識が NS(X)≅Z⁷ で分類されると証明した。さらに η=det(Li*[pt]) が無限位数なら、反標準制限が線束である例外対象は曲面上でも線束となり、ample helix の exact 再構成ができる。

**AOU に対する結論の範囲：** AOU §9 の blowup が上の Rains 模型として反標準制限と Serre を保って実現され、関連 AS Z-代数が right noetherian である場合、標準 tilting 同値は t-exact になる。模型の比較自体を全AOU点で済ませたわけではない。非torsion条件は点ごとの条件でありZariski開性を主張しない。相対族・全境界・自己同値軌道の課題は残る。

ambient 認識は別リポジトリ `uedakazushi/nc-cubic-ambient`。既存の普遍有限代数、数値Serre–E6、形式chart、Picard障害の有効な証明はすべて保持する。

## III. 現在の主張・仮定・証明所在

中心は `line_bundle_classification.tex` と `anticanonical_heart_bridge.tex`（ともに `papers/sections/`）。

- **本稿で証明・点検：** intrinsic weak cubic 公理下で rank1tf の End=C、負H自己Hom=0、Ext²自己=0、exceptional ⇔ χself=1。RR表示と (EP) を仮定すれば同一数値的線束類で高々一つ（`thm:intrinsic-line-criterion`, `thm:numerical-line-uniqueness`）。一般内在的模型で (EP) を勝手に仮定しない。
- **既知の分類：** Rains Cor.7.10, Prop.10.13 による非可換有理曲面の Line↔NS。これは本研究の新しい存在定理ではない。反標準 ample なら既知の消滅・生成から AZ とHilbert値を得る（`prop:rains-weak-admissibility`）。
- **本稿で証明・今回点検：** Rains rational、C smooth connected、Q interior nef、Q²=3 の下で A0={r=0,c1=0}, A1={r=0}（`thm:rains-gk-filtration`）。単純対象の反標準射、χとdegreeの長さ関数、θの無限下降列を使う。rank1tfの定義が一致し、Line_adm=Line≅Z⁷（`cor:rains-all-weak-markings`）。この二結果はη非torsionを要しない。
- **本稿で証明・今回点検：** 上記にη無限位数を追加すると i*M=0⇒M=0。Cartier三角から Li*E が層なら Eも層、制限が線束である例外対象は線束（`thm:restriction-detects-heart`, `cor:restricted-exceptional-line`）。Li*のt-exact性やi*の射上の忠実性は主張しない。可換模型のC外の点が無条件拡張の反例。
- **既知再構成を使う本稿証明：** foundationの制限がすべて線束となる周期9のgeometric helixから coh X≃cohproj A を得る（`thm:restricted-helix-exact`）。Polishchuk Lem2.1/Thm2.4を使用。qgr表記にはright noetherianを要求する。AOU式(9.53)と接続する系 `cor:aou-rains-exact-region` は明記した模型比較範囲の十分条件であり、全AOU点での断定でない。
- **既存成果を保持：** 普遍45次元/gldim2関係式代数とArtin形式完備性、HH支持階数公式、全点の数値Serre–E6、矢基底変更の数値的自明性。DDLによる形式Abel chart、相対条件下の線束持上げ、Picard障害δπ、非常に一般の整数核ZK、一次軌道Pic/ZK、一次線形不変式も維持。数学的仮定は対応節を参照。

新しい橋渡しの推論の証明は本文にあるが、外部査読・形式化・網羅的な優先権照合は未実施。先行文献の分類そのもの、入力となる再構成定理、新たに書いた推論を区別する。

## IV. 優先課題と具体的着手

1. **模型比較の適用範囲を確定する。** AOU §9 の VdB blowup と Rains blowup の構成を追い、同じ反標準制限・Serreを持つことを証明する。AOUのtranslationパラメータとηの対応、およびright noetherian性の入力箇所を特定する。現在の十分条件を単に適用済みと読み替えない。
2. **全弱標識分類から同値判定へ。** exact比較が得られる各点でLine_adm≅NSを使い、Aut_exがNSにどう作用するかを調べる。全線束の存在から全NSが固定圏のtensor自己同値になるとは結論しない。構造対象の相対族とスカラーGm慣性も別扱い。
3. **torsionパラメータと相対化。** η torsionではC外の有限長対象が制限で見えなくなり得る。既知の可換線束分類と整合する別のheart判定を探す。非torsionの点ごとの証明を有限型の開族やGIT降下へ延長しない。
4. **投稿準備。** 主要結果を線束分類・rank比較・反標準検出・AOU十分条件の論理順に整理し、既知入力をIntroductionに明示する。旧結果は必要な証明を削らず保持。全境界のheart、GIT S-同値のexact判定、無標識stack代数性は未解決とする。

## V. 再現・保存

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

組版出力は `build/nc-cubic-unmark.pdf`。bundleは `pdf/` にPDFを一つ収録し、GitはPDF/ZIPを追跡しない。書誌と参照箇所は本文と研究ノート、検証の実行範囲は `research/unmark_validation.json` にまとめる。
