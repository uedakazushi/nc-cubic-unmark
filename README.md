# 非可換三次曲面の構造対象・quiver 標識と忘却射

2026-11-19 / unmark-v13。再開は **`00_research_plan.md`**、次に `papers/nc-cubic-unmark.tex` と `research/unmark_notes.md`。

構造対象を一つ固定する **O-marking** と、指定したrolled-up quiverを持つfull very strong exceptional collectionを固定する **Q-marking** を定義し、忘却射 `M^Q→M^O` とfiberを研究する。基準はanticanonical heart、比較する別の表面heartはAS heartのみ。

## 現在の結果

- 最小のO公理と、例外性を加えた比較用weak公理を区別する。構造対象を先頭に持つvery strong helixの全対象は、数値RRを使わずに指定heartに入る。
- 標準27矢rolled-up quiverの最小表示から、有限foundationの18矢・9関係、次元45、標準Euler形式を導く。一つのQ-markingが比較用weak公理と三次曲面型数値構造を与える。
- 複素点のモジュライ群oidを定義。固定(A,O)上の2-fiberは標識集合で添字付けられた `B(Gm^(ell−1))` の非交和。成分スカラーを除いた2-fiberは離散標識集合。同型類集合のfiberはさらにOを保つexact自己同値で割る。
- 標準Q-markingが存在し零次数rootがない場合、標識集合は `W(E6)`-torsor。rigidified fiberは51840点、元のfiberは51840個の `B(Gm^8)`。exact自己同値の数値作用もこの範囲で忠実となる。
- 実際の標準AOU relation torusのvery general点では `Aut_ex(A)=〈H〉≅Z`、`Aut_ex(A,O)=1`。同型類集合の第一fiberも51840点である。構造対象自体も忘れる第二fiberの結果 `Λ/ZK≅P(E6)` は、例外的構造対象の部分について保持する。

主要参照は `def:o-marked-cubic`, `def:q-marking`, `prop:aou-quiver-euler-recognition`, `prop:o-helix-heart-recognition`, `thm:q-o-fiber-groupoids`, `cor:standard-q-o-weyl-fibers`, `prop:q-numerical-auto-faithful`。

## 未解決と範囲

最小O公理から例外性が従うか、Q-markingの存在範囲、相対moduliの代数性、rigidified忘却射の有限étale性と境界は未解決。相対モデルを指定したstackificationの定義と、代数スタック性の証明は別である。固定点の51840という計算から相対有限性を推論しない。全OU型・全GIT境界・Weyl作用の全域正則性は主張しない。新規性の網羅的確認は未完了。

既存の線束の存在・一意性、root affine反射、三対象交換、AS/反標準heart比較、very-general自己同値像、許容Artin変形、Picard一次障害と数値計算の完全な証明を現行原稿に保持する。

## 再現

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 computations/verify_weyl_frames.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

組版にはLuaLaTeX、日本語クラス `ltjsarticle` とHaranoajiフォントが必要。TeX Liveの `scheme-basic` に `luatexja haranoaji mathtools booktabs jknapltx rsfs xkeyval fontspec lualatex-math` とそれらの依存パッケージを加えた構成を使用する。PDFの出力先は `build/nc-cubic-unmark.pdf`。

GitHub mainがソース正本。PDF/ZIP/中間物は追跡しない。当該版の検証と限界は `research/unmark_validation.json`。生成・検証・GitHub反映・配布物保存を別々に確認する。
