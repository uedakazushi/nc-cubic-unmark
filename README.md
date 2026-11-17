# AOU関係式モジュライと非可換三次曲面の無標識Abel圏

2026-11-17 / unmark-v3。最初に `00_research_plan.md` を読む。

最重要課題は、AOU関係式stackおよびトーリックGIT商から無標識Abel圏への射の定義域・本質像・ファイバー・慣性を解明し、公表用日本語LuaLaTeX論文にすること。

主論文 `papers/nc-cubic-unmark.tex`。入力 `papers/sections/marking_forgetful.tex`（Picardと形式標識忘却）、`papers/sections/aou_to_unmarked.tex`（AOU比較・可換Weyl商・非可換一次fiber・GIT降下）、`papers/sections/picard_invariants.tex`（一次Picard不変式と分離粗商の障害）。

AOUの関係式GIT商の全点がAbel圏を定めるとは主張しない。可換smooth locusではW(E6)商、非常に一般の許容相対一次非可換変形ではPicard整数kernel=ZK、構造対象軌道商=Z^6。後者をGIT粗商のfiberとは混同しない。新たに、一次Hochschild変形空間のPicard不変式環はPoisson成分の関数環に等しく、分離的な一次線形粗商は可換変形方向を区別できないと証明した。大域AOU GITでの不変式計算ではない。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub mainが正本。PDF/ZIP/中間ファイルはGit追跡しない。ambientは [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) に分離。