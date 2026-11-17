# 研究指示 — nc-cubic-unmark

最初に `00_research_plan.md` を読む。最重要課題はAOU relation moduliから無標識Abel圏への圏的忘却、形式Artin近傍から代数的なAS heartへの拡張、Picard作用、慣性とGIT降下。主論文は `papers/nc-cubic-unmark.tex`、新しい形式heart比較は `papers/sections/formal_abelian_recognition.tex`。

恒常的研究原則：数学的価値最大化、現在有効な方針、証明・既知結果・追加仮定・計算観察の区別、一次資料確認、現在の数学的成果と証明を完全保持。日本語LuaLaTeX、主原稿と研究ノートを整理して保持。ユーザーは研究区切りごとの自己完結した軽量bundleのLibrary保存を承諾なく許可している。旧Library資産の明示指示のない削除は不可。

GitHub main直push、PR・Actions・force pushは使用しない。PDF・ZIP・コンパイルキャッシュをGit追跡しない。形式Abel変形の存在から、反Serreのt-exact性やGIT境界のAS正則性を勝手に結論しない。Picard形式作用の存在と具体的な高次作用式、大域代数的作用を区別する。生成・検証・push・Library保存は別々に実際の状態を記録。

検証：`python3 scripts/verify_unmark_bundle.py`、`python3 computations/verify_aou_relation_tangent.py`、`python3 computations/verify_marking_lattice.py`、`latexmk -lualatex papers/nc-cubic-unmark.tex`。
