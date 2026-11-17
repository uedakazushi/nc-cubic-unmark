# AOU関係式モジュライと非可換三次曲面の無標識Abel圏

現行版 2026-11-18 / unmark-v5。再開時は `00_research_plan.md` を最初に読む。

**主論文**: `papers/nc-cubic-unmark.tex`（日本語 LuaLaTeX）。

AOU全関係式空間には階数45の普遍有限代数・smooth proper導来圏があるが、三次曲面型Abel heartは別問題。smooth可換AOU点の局所Artin形式近傍では、De Deken–Lowen変形同値と関係式の形式完備性により平坦Grothendieck Abel heartを復元できる。標準helixを選ぶと形式8次元チャート、無標識化はPic(X)⋊Aut(X)の形式作用群oidとなり、一次作用はPicard shear。GIT全境界へのAbel heart/AS性の延長と大域Pic作用は未証明。

研究用入力節: `papers/sections/aou_universal_algebras.tex`、`formal_abelian_recognition.tex`、`aou_to_unmarked.tex`、`marking_forgetful.tex`、`picard_invariants.tex`。数値検算は `computations/`、状態は `research/unmark_validation.json`。

```
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub mainに原稿ソース、PDFはGit追跡せず研究継続bundleに収録。ambient問題は `uedakazushi/nc-cubic-ambient` に分離。
