# 研究方針：AOU関係式モジュライと無標識 Abel 圏

2026-11-17 / unmark-v3。**研究再開時は本ファイルを最初に読む。** 次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md`、`papers/sections/aou_to_unmarked.tex` と `papers/sections/picard_invariants.tex` を読む。GitHub `uedakazushi/nc-cubic-unmark` の main が原稿正本。

## I. 恒常的な研究原則と保存許可

数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して研究全体の価値を最大化する。研究方針は現時点で有効な内容に書き直し、履歴を蓄積しない。既存文献、完全な証明、追加仮定付きの定理、未証明の予想、計算観察を区別し、証明所在・依存する既知結果・検証状況を明記する。公表用原稿は日本語LuaLaTeXとし、既に得られた有効な数学的内容は消さず、読者に理解しやすく統合する。文献は一次資料で照合し、未確認の新規性・書誌は推測で補わない。

**ユーザーは研究の区切りごとに承諾なく現行研究継続bundleをLibraryへ保存することを一般的に許可している。** 保存するのは研究方針・研究ノート・公表用論文と再現に不可欠な現行のソース・計算資産・証明であり、旧ZIP、ログ、キャッシュ、試行履歴、重複は含めない。旧Libraryファイルを明示的な削除指示なしに削除しない。生成、計算、LuaLaTeX組版、GitHub push、Library保存は別々に確認して報告する。

## II. 中心問題と論文の達成基準

最優先課題は、AOUの関係式モジュライから **無標識 Abel 圏への圏的忘却の定義域・本質像・ファイバー・慣性・粗商の限界** を解明し、公表価値のある定理と完全な証明を備えた論文にすること。

次の五段階を区別する：

1. AOUの関係式stack `[R_Q/G_Q]`, `R_Q=(P^2)^9`, `G_Q=(G_m)^18`；
2. 線形化に依存するトーリックGIT粗商 `M_Q^χ`；
3. 相対heart、Serre、生成helix等の証拠を持つ許容圏的AOU表示；
4. 弱標識付き `(A,O)`；
5. 無標識の基礎Abel圏 `A`。

`M_Q^χ` の全境界がAbel圏を定めることも、GIT S-同値がexact Abel同値を意味することも未証明。ambientのquadric AS-regular認識は別論文 `uedakazushi/nc-cubic-ambient` に分ける。

第一到達基準は：(a) smooth可換locusのW(E6)標識忘却の厳密な記述、(b) DDL/Todaと一致する相対一次非可換変形でのPicard shear、(c) Picard shearの粗商の障害を証明する、(d) AOU関係式とAS-regular heartの比較範囲を明示、(e) 全TeX組版と優先権調査。最上位目標は、AOU側の非可換幾何的開集合で実際の相対忘却を構成し、必要十分な同値条件と慣性を記述すること。

## III. 現在の到達点（主張の状態と所在）

- 【既知・一次資料照合】AOU, arXiv:2404.00175 v1, Theorems 1.1, 1.2, §§4.6,5.1–5.4。GITの稠密トーラスは8次元、可換marked cubicのmoduliがその中に局所閉埋込み、楕円decupleとの対応は双有理。全境界のカテゴリー化は証明されていない。
- 【主論文に証明】可換smooth locusの無標識同型類はW(E6)軌道、一般のX上に51840標識（`thm:aou-commutative-quotient`）。GabrielのAbel圏再構成を使用。
- 【定義的/条件付き】相対圏的許容AOU表示から弱標識・無標識への擬関手（`prop:aou-categorical-map`）。AOU関係式stack内の開性・全域の降下・境界は未証明。GIT粗商降下の必要条件だけ（`prop:aou-git-descent-test`）。
- 【証明記載】固定圏上の選択2-fiberとexact自己同値作用、可換構造対象の線束分類、共通tensorの有限End代数への非依存（`thm:forgetful-fibres`, `thm:commutative-structure`, `prop:common-tensor`）。
- 【相対仮定付き】Artin変形上の構造対象持上げと形式W(E6)比較（`thm:formal-structure`, `thm:formal-weyl`）。全dg変形にheart条件を無条件には与えない。
- 【証明記載】一次Picard shear `δ_π(L)=H¹(π^sharp)c₁(L)`、一般階数4、反標準方向の核、非常に一般の整数核 `Z K_X`、許容一次変形上の構造対象同型類の軌道 `Pic/ZK=Z^6`（`prop:picard-first-order`, `thm:picard-obstruction-rank`, `thm:very-general-picard-kernel`, `cor:first-order-pointings`）。
- 【追加仮定付き】標準AOU helixの相対持上げをすべてのline bundle twistに対して要求すれば、**拡張された圏的helix選択**の無標識ファイバーが`Z^6`へ全射（`thm:aou-infinite-relative-fibre`）。これをAOUのGIT粗商のファイバーと混同しない。
- 【新定理・証明記載】固定smooth cubic Xで`δ_π`があるπについてrank4なら、一次Hochschild変形線形空間`E=H¹T_X⊕H⁰(-K_X)`上のPicard shearについて `C[E]^Pic=C[P]`, `C(E)^Pic=C(P)`（`thm:picard-linear-invariants`）。一般rank4のπでは各H¹T_X-fiberのPicard軌道はZariski稠密。有限型分離代数空間へのPicard不変な射は`P=H⁰(-K_X)`を経由し、可換方向を区別しない（`cor:separated-linear-quotient`）。**線形一次模型の定理であって、AOU GITに無条件のPicard作用を構成したものでも、一般のunmarked粗moduli非存在定理でもない。**
- 【条件付き】exact自己同値を記録する無標識stackの非準コンパクト対角の障害（`prop:nonqc-inertia`）。変形制御の仮定を削除しない。
- 【有限計算】`computations/verify_marking_lattice.py`: 72根、27直線、判別式3、W軌道のrank6、rank4具体例。圏の降下やPicard shear不変式の数学的証明は本文にある。

## IV. 優先順位の高い次の課題と具体的着手

1. **AOU関係式の相対AS-openの認識**：AOU §4.6 の解消列(4.12)–(4.13)、§5.3の関係式/potential stackの開埋込み、OUの楕円decupleの存在開集合を照合。相対AS-regularity・heart・Serre・AZ豊富性を全8方向で示せる最小の開部分を特定。
2. **一次Picard shearをrelation座標で実現**：AOUのquiver $Q$ の九関係式の一次変形と、line bundle twistによる有限threadの持上げの比較。`Pic(X)/ZK`の作用がAOU関係式の形式近傍でどこまで定義できるかを精密化。形式的な座標と相対heartの証拠を明記。
3. **GITと無標識の相違を実例で判定**：S-同値な半安定点で非同値Abel圏が起こるかを調べる。粗商降下が不可能なら、適切な2-stack・非分離商・良いモジュライ空間の対象を探す。線形一次不変式環 `C[P]` を診断に使うが、非線形全域へ推論しない。
4. **投稿品質**：IntroductionでAOU, DDL, Toda, Gabriel, Bondal–Orlov, OU2025を正確に比較。条件付き主張の読み替えを排除。全体のLuaLaTeX組版と原稿/脚注/用語を再点検。

## V. 再現・保存

正本: https://github.com/uedakazushi/nc-cubic-unmark

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

Bundleは現行版の原稿・コード・必要な書誌情報を同梱し、PDFは必要な範囲でLuaLaTeXで再生成。GitHubへはPDFを追跡しない。各検査で未実行項目があれば検証JSONに記す。