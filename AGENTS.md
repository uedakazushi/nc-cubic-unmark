# 研究指示 — nc-cubic-unmark

最初に `00_research_plan.md` を読む。研究の最優先は標識忘却（AOU九対象→構造対象→無標識Abel圏）のモジュライと自己同値。weakly markedな構造対象にrank-one torsion-freeとexceptionalityを要求し、ambientのAS性を仮定しない。

一般原則：重要性・新規性・正確性・実現可能性を考慮して方針を変える。証明済み、条件付き、未証明、計算観察を厳密に区別。論文は日本語LuaLaTeXで有効な証明を削らず編集し、ノートは現行知識のみ保持する。一次資料を確認し、未確認の優先権・書誌を推測しない。研究区切りごとの軽量bundleのLibrary保存を承諾なしに行ってよい。GitHub mainはソースの正本で、PR・Actions・force pushは使わず区切りでfast-forward pushする。GitのPDF・ZIP・キャッシュ・バックアップ追跡を避ける。GitHub更新、組版・計算、Library保存は別々に検証する。旧Library資産を明示指示なく削除しない。

投稿向け成果の中心：`papers/nc-cubic-unmark.tex`。`latexmk -lualatex papers/nc-cubic-unmark.tex` および `python3 scripts/verify_unmark_bundle.py` を確認する。ambient射の研究は独立の `uedakazushi/nc-cubic-ambient` を正本とする。
