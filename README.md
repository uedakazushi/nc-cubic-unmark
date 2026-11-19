# 非可換三次曲面の構造対象・quiver 標識と忘却射

2026-11-19 / unmark-v14。再開は **`00_research_plan.md`**、次に `papers/nc-cubic-unmark.tex` と `research/unmark_notes.md`。

構造対象を一つ固定する **O-marking** と、指定したrolled-up quiverを持つfull very strong exceptional collectionを固定する **Q-marking** を定義し、忘却射 `M^Q→M^O` とfiberを研究する。基準はanticanonical heart、比較する別の表面heartはAS heartのみ。

## 現在の結果

- 最小のO公理と、例外性を加えた比較用weak公理を区別する。構造対象を先頭に持つvery strong helixの全対象は、数値RRを使わずに指定heartに入る。
- 標準27矢rolled-up quiverの最小表示から、有限foundationの18矢・9関係、次元45、標準Euler形式を導く。一つのQ-markingが比較用weak公理と三次曲面型数値構造を与える。
- 複素点のモジュライ群oidを定義。固定(A,O)上の2-fiberは標識集合で添字付けられた `B(Gm^(ell−1))` の非交和。成分スカラーを除いた2-fiberは離散標識集合。同型類集合のfiberはさらにOを保つexact自己同値で割る。
- 標準Q-markingが存在し零次数rootがない場合、標識集合は `W(E6)`-torsor。rigidified fiberは51840点、元のfiberは51840個の `B(Gm^8)`。exact自己同値の数値作用もこの範囲で忠実となる。
- 正則中心切断とAZ豊富性から自己Extの漸近消滅を示す。既知weak/RRの中心楕円因子locusでは最小構造対象がすべて例外的となり、`Str₃=Line_adm`。実際のvery general点の第二fiber `Λ/ZK≅P(E6)` は、この範囲の全最小構造対象について成立する。
- 普遍有限relation代数の三項複体からT8上の忠実なW(E6)有理作用を構成する。非空安定affine開U上で `U→[U/W]` は次数51840の有限étale torsor。九cornerの同時認識により、`[U/W](C)` はUに現れるO-marked cubicのfull essential imageと群oidとして同値。各点のpointed自己同値群はWの安定化群となる。
- Abel圏とrelative perfect部分圏を分けた許容Artinモデルで、rigidified標識忘却は形式étale。固定smooth proper dg族上のfull strong completionはGm^(ell−1)-gerbeを介してétale代数空間となる。very strong/Q型の開性には一様tail消滅等を別に課す。
- noetherian基礎環上の有限余次元corner比較と、その基底変換適合性を証明する。族への適用では必要な全基底変換後のnoetherian性と普遍flat性を明記する。
- 実際の標準AOU relation torusのvery general点では `Aut_ex(A)=〈H〉≅Z`、`Aut_ex(A,O)=1`。全内在的標準Q-markingについて同型類集合の第一fiberも51840点である。

定義・点fiberは `def:o-marked-cubic`, `def:q-marking`, `thm:q-o-fiber-groupoids`。現在の主要結果は `cor:aou-all-structures-exceptional`, `prop:aou-all-corner-lines`, `thm:weyl-finite-etale-chart`, `prop:weyl-chart-point-comparison`, `cor:q-o-artin-formal-etale`, `thm:full-strong-completion-etale`。

## 未解決と範囲

構成済みの有限étale商モデル、複素点の群oid同定、全内在的relative moduliの同定は区別する。最後の比較には、実際の族の相対noetherian性、Abel/Perf/Serreの基底変換、Weyl比較のcoherence、exact同値の降下、全incoming Q-markingの網羅性が残る。中心切断なしの一般最小Oの例外性、Q-markingの存在範囲、全OU型・全GIT境界は未解決。新規性の網羅的確認は未完了。

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
