# 研究方針：AOU関係式モジュライと無標識 Abel 圏

2026-11-17 / unmark-v2。再開時には本ファイル、`papers/nc-cubic-unmark.tex`、`research/unmark_notes.md`、`papers/sections/aou_to_unmarked.tex` の順に読む。GitHub mainを原稿正本とする。

## I. 恒常的な原則・保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し研究の価値を最大化する。重要な方針変更は現在有効な方針として理由と未解決点を整理し、更新履歴を堆積しない。既知の結果、本稿で証明を書いたもの、追加仮定付きのもの、未証明・予想・計算観察を区別し、典拠と未検証事項を明記する。必要に応じて先行研究を一次資料で確認し、未確認の新規性を断定しない。公表用論文は日本語LuaLaTeXで書き、正しい有効な証明を省略・削除しない。ノートは再取得の難しい障害・未解決点を整理し、作業履歴を残さない。

ユーザーから、研究の区切りごとに承諾なしで現在の軽量研究継続bundleをLibraryに保存する一般許可を受けている。bundleは現行の方針・ノート・論文・最低限のソース/検証物だけを含み、過去のZIP・履歴・ログ・中間物を含めない。既存のLibraryファイルは明示的な削除指示なく削除しない。GitHub更新、原稿生成、PDF組版・計算、Library保存は個別に実施状態を確認する。

## II. 中心課題・達成基準

**最重要課題は、AOU の関係式モジュライから無標識 Abel 圏への射の定義域・本質像・相対慣性・ファイバーを決定し、投稿できる論文にすること。** まずAS-regular/相対heartが意味を持つ幾何的領域を対象にする。GIT境界を無条件にカテゴリ化しない。

AOU の `R_Q=(P^2)^9` と `G_Q=(G_m)^18` に対し、(i) quotient stack `[R_Q/G_Q]`、(ii) GIT coarse scheme `M_Q^chi`、(iii) 幾何的標識 helix の moduli、(iv) 弱標識 `(A,O)`、(v) 無標識 Abel 圏 `A` を分離する。`M_Q^chi` 全域から無標識の代数的 stack への射は未証明。ambient認識は引き続き保留、`nc-cubic-ambient` の独立課題。

公表への第一到達基準は: (a) AOU 原著の既知定理との厳密な対応、(b) smooth commutative locus の完全記述、(c) 相対仮定付きでも非可換一次変形でのPicard障害による具体的差異、(d) 有効な定義域・降下補題、(e) LuaLaTeX組版、(f) 新規性と限界の明瞭な Introduction。第二到達基準は非可換AS-openの存在・相対比較の無条件化。

## III. 確認済みの骨格（証明の所在）

- 【AOU既知・一次資料確認】`M_Q^chi` はトーリックGIT商、dense torus `(G_m)^8`、滑らかな標識付き三次曲面の moduli は局所閉埋込み。AOU arXiv:2404.00175 v1, §5.1, §5.4, Theorem 1.2; Theorem 1.1 は楕円decupleとの**双有理性**。全GIT境界のカテゴリ化を主張していない。
- 【本稿に証明】可換 locus の無標識同型類は `W(E6)` 標識変更の軌道、一般X上の標識数51840、特異でない特殊Xでは `51840/|Aut X|`（`thm:aou-commutative-quotient`）。GabrielのAbel圏再構成を使用。
- 【定義的な構成/条件付き】圏的に許容されるAOU表示から `(A,O)` と無標識 `A` を得る擬関手（`prop:aou-categorical-map`）。相対表現可能性・AS-openの代数性未証明。GITへの降下にはS-同値点で圏が同値である必要がある（`prop:aou-git-descent-test`）。
- 【証明を記載】固定圏上の選択groupoid/2-fiber、可換構造対象は線束、relation End代数の共通tensor不変性（`thm:forgetful-fibres`, `thm:commutative-structure`, `prop:common-tensor`）。
- 【相対仮定付き】Artin変形での構造対象とAOU標準helixの持上げ、形式`W(E6)`比較（`thm:formal-structure`, `thm:formal-weyl`）。
- 【証明を記載】一次Picardのshear `delta_pi(L)=H^1(pi^sharp)c1(L)`、一般rank4、非常に一般の整数核`Z K_X`、許容一次fiberでの構造対象商`Pic/Z K = Q(E6)^vee = Z^6`。追加のhelix持上げ仮定下ではAOU標識忘却のファイバーからこのZ^6への全射（`thm:aou-infinite-relative-fibre`）。**AOU射影GIT商の無限ファイバーは主張しない。**
- 【条件付きの必要条件】exact自己同値を完全に記録するunmarked 1-stackがHH¹制御を満たせば、可換点の無限Picard慣性ゆえに準コンパクト対角は期待できない（`prop:nonqc-inertia`）。
- 【有限計算】`computations/verify_marking_lattice.py` はE6の72根・27直線・判別式3等のみを検査する。幾何・降下・Moritaの証明ではない。

## IV. 優先課題・着手方法

1. **相対AS-openの認識**: AOUの関係式をbase-change可能なZ代数として取り出す操作、AS-regularityとt-exact H・AZ豊富性が成立する領域を整理し、AOU §4.6とOU2025の定義を比較する。1次のPoisson変形で具体的AOU relationが許容になるかを判定。
2. **無標識忘却の相対群oid**: relation stackの慣性とexact自己同値2-groupの比較。中心Gm, rigidification、pointed/absoluteでの自然同型を区別。S-同値点のカテゴリ不変性を調べる。
3. **Poisson shearの実験と証明**: generic cubic, πの上でE6各基本線束のdeltaを計算し、AOU relationの座標変換と照合。整数rankとcomplex rankの混同を避ける。
4. **投稿仕上げ**: IntroductionでAOU Theorem1.1/1.2、OU2025、Toda、DDL、Gabrielの適用範囲を明示。形式W商と高次/境界の未知を断定しない。定理依存性を再点検しLuaLaTeXで完全組版。

## V. 再現・正本

GitHub: https://github.com/uedakazushi/nc-cubic-unmark （main）。ambient正本: https://github.com/uedakazushi/nc-cubic-ambient 。

```
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

TeX全体の組版と数値検証はその都度再実行して記録する。文献一次資料: AOU https://arxiv.org/pdf/2404.00175, OU2025 https://arxiv.org/pdf/2508.04986, Gabriel DOI:10.24033/bsmf.1583, Toda arXiv:math/0502571, DDL DOI:10.4171/JNCG/83。