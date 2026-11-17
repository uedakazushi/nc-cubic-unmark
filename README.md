# AOU関係式モジュライと非可換三次曲面の無標識 Abel 圏

**2026-11-18 / unmark-v6**。研究の再開は必ず `00_research_plan.md` から。

最重要課題は、AOU九関係式モジュライから無標識 Abel 圏への忘却の定義域・本質像・ファイバー・慣性・GIT降下を解決すること。論文は日本語 LuaLaTeX の `papers/nc-cubic-unmark.tex`。入力節は `papers/sections/` の現行全TeX。

主要な到達点：全関係式点で45次元・gldim2の普遍有限代数、境界Hochschild次元の支持行列公式、稠密開上にAS-regular heartが存在する既知AOU/OUの帰結、全関係式点で一定の数値的Serre-E6格子、数値標識では区別できない導来非同値な境界、滑らかな可換点でのAbel形式変形と8次元AOUチャート、Picard一次障害、可換W(E6)標識忘却。

形式的 Grothendieck Abel 変形、稠密AS locusの点ごとの存在、全GIT境界でのAS heartの認識は別問題。全域の無標識 stack、相対 t-exact Serre、GIT S-同値降下は未証明。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub `main` がソース正本。PDF/ZIP/組版キャッシュはGit追跡しない。ambientのAS認識問題は [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) で扱う。
