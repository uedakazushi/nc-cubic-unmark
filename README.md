# 非可換三次曲面の二段階の標識忘却

2026-11-18 / unmark-v10。再開は **`00_research_plan.md`**、次に主論文 `papers/nc-cubic-unmark.tex` と `research/unmark_notes.md`。

anticanonical heartを基準として集合論的に扱う。比較対象はAS heartのみ。

- AOU/OU marking → weak marking：固定weak marking上の有限W(E6)自由度。
- weakly marked → unmarked：固定anticanonical heart内のline bundleのchoice。

RRとr(O0)=1からSerre消滅・A1={r=0}・次数正値性と線束一意性を導く。AOU三ブロック線束標識は≤51840、全Weyl作用は一種類の三対象交換へ還元。root型simpleが存在する場合のnon-ample line構成を条件付き障害として記載（実例未構成）。

線束の存在・一意性・weak許容性を先に分類し、exact自己同値による軌道は後に分ける。groupoid/stackはさらに後段の課題。有限Weyl商の全域的実現と、全数値的線束類の存在は未解決の範囲を明示する。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 computations/verify_weyl_frames.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub mainがソース正本。PDF/ZIP/中間物は追跡しない。数学的仮定と現在の検証状況は研究方針と `research/unmark_validation.json` を参照。
