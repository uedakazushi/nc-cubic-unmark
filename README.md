# AOU 関係式モジュライと非可換三次曲面の無標識 Abel 圏

2026-11-18 / unmark-v7。研究再開時は **`00_research_plan.md`**、次に `papers/nc-cubic-unmark.tex` と `research/unmark_notes.md` を読む。

最優先は、固定圏内の数値的線束類ごとの存在・一意性、その弱標識としての許容性、exact自己同値軌道。内在的な線束判定は rank-one torsion-free + χ(E,E)=1 ⇔ exceptional。数値RRと有効次数正値性 (EP) の下で同一数値類の一意性を証明する。

Rainsの非可換有理曲面では各因子類の線束の存在・分類は既知。これをAOUの指定heartへ移すためのexact比較とrank条件の一致はなお課題である。Rains分類を本研究の新規成果としない。既存のAOU普遍有限代数、数値Serre–E6、形式Abel chart、Picard障害の証明を保持する。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub mainがソース正本。PDF・ZIP・組版中間物をGit追跡しない。ambient認識は `uedakazushi/nc-cubic-ambient` で扱う。全GIT境界のheartと無標識降下は未証明。
