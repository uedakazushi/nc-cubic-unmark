# 研究指示 — nc-cubic-unmark

まず `00_research_plan.md` を読む。最優先は AOU 関係式から無標識 Abel 圏への忘却の実際の定義域・同型条件・慣性・GIT降下。主論文は `papers/nc-cubic-unmark.tex`。稠密 AS locus (AOU/OU 既知結果の帰結)、形式 DDL Abel chart、全境界にある数値的Serre-E6、数値では区別不能な導来非同値を厳密に区別する。数値 E6 だけで三次曲面型 heart やAS-regularityを推論しない。

研究価値を最大化するよう目標を柔軟に改め、現行研究方針を時系列履歴なしで書き直す。証明済み・仮定付き・未証明・計算検算・先行研究を区別する。既知の結果の新規性を主張しない。一次資料を確認し、独自の新規性が未確認なら明示。主論文は日本語LuaLaTeX、全証明を現行原稿に維持する。GitHub mainへ直接 fast-forward push（PR/Actions/force pushなし）。PDF・ZIP・キャッシュはGit非追跡。

ユーザーの一般許可により、研究の区切りで自己完結した現行軽量bundleを承諾なくLibraryへ保存する。旧版・ログ・キャッシュを同梱しない。Library上の旧ファイルを指示なく削除しない。生成、計算、組版、GitHub更新、Library保存は別状態として検証する。

検証: `python3 computations/verify_marking_lattice.py`、`python3 computations/verify_aou_relation_tangent.py`、`python3 scripts/verify_unmark_bundle.py`、`latexmk -lualatex papers/nc-cubic-unmark.tex`。
