# 研究指示 — nc-cubic-unmark

**再開時は `00_research_plan.md` を最初に読む。** 最重要はAOU関係式モジュライから無標識Abel圏への忘却（定義域・本質像・ファイバー・慣性）。GIT境界を無条件に圏と同一視しない。

主論文 `papers/nc-cubic-unmark.tex` と `papers/sections/aou_to_unmarked.tex`, `papers/sections/marking_forgetful.tex`, `papers/sections/picard_invariants.tex`。相対helix持上げ、Picard一次障害、GIT降下、大域Weyl商の仮定や未証明性を明記。weakのrank-one torsion-free, exceptionality, Hのt-exact性, AZ豊富性を維持。ambient認識は別の課題。

数学的価値を最大化し、研究方針は現行の結論として書き直し履歴を積まない。既知引用、証明、仮定付き、未証明、計算観察を分離。一次資料確認。日本語LuaLaTeX。GitHub main直push、PR・Actions・force pushを使用しない。PDF/ZIPや中間物はGit追跡しない。研究区切りごとに最新の軽量bundleをLibraryに承諾なく保存してよい。既存Libraryファイルを明示指示なく削除しない。

検証: `python3 scripts/verify_unmark_bundle.py`、`python3 computations/verify_marking_lattice.py`、`latexmk -lualatex papers/nc-cubic-unmark.tex`。生成・実行・GitHub更新・Library保存は別々に報告。
一次Picard shearの不変式はPoisson成分だけを検出する（論文の証明）。これを大域AOU GITや一般の無標識粗moduliの非存在に拡張してはならない。
