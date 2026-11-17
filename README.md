# AOU 関係式モジュライと非可換三次曲面の無標識 Abel 圏

2026-11-18 / unmark-v8。研究再開は **`00_research_plan.md`**、次に主論文 `papers/nc-cubic-unmark.tex` と `research/unmark_notes.md`。

数値的線束類の存在・一意性、weak許容性、exact自己同値軌道を研究する。Rainsの既知の線束存在・分類と、本稿の内在的χself=1判定を区別する。

滑らかな反標準曲線C、Q=−Kがnef内部、Q²=3のRains模型でGK filtrationと数値rank/torsionの一致を証明し、全弱標識の同型類がNS≅Z⁷となる。さらにη=det(Li*[pt])が無限位数なら、制限が線束である例外対象は線束。ample helixのcohproj再構成を用い、明記したRains模型との比較とright noetherian条件下でAOU tilting同値のt-exact性を得る。一般のAOU点、torsionパラメータ、相対降下まで証明したものではない。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub mainがソース正本。PDF・ZIP・中間生成物は追跡しない。全境界のheartと無標識GIT降下は未解決。ambient認識は `uedakazushi/nc-cubic-ambient` に分離する。
