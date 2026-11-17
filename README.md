# 非可換三次曲面の標識忘却とPicard作用

このリポジトリは、標準九対象の標識付き非可換三次曲面から弱標識付き曲面（許容構造対象）へ、さらに無標識のAbel圏へ至る二段階の忘却を研究する。

公表用主論文：`papers/nc-cubic-unmark.tex`。再開時は`00_research_plan.md`を最初に読む。

内在的定義ではGabriel–Krull rank-one torsion-free性とexceptionalityを要求し、quadratic AS-regular ambientは仮定しない。可換三次曲面での標識忘却とPicard作用、形式W(E6)商、一次変形における障害と非常に一般の整数Picard核を中心とする。大域的なWeyl商は未証明。

ambient射、四頂点potential、R(1,3)成分の独立論文は [nc-cubic-ambient-moduli](https://github.com/uedakazushi/nc-cubic-ambient-moduli) の `papers/nc-cubic-ambient.tex` を参照。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub mainを研究ソースの正本とする。PDF・ZIP・LaTeX中間生成物は追跡しない。 
