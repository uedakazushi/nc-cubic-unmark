# 非可換三次曲面の二段階の標識忘却

2026-11-18 / unmark-v11。再開は **`00_research_plan.md`**、次に `papers/nc-cubic-unmark.tex` と `research/unmark_notes.md`。

anticanonical heartを基準に集合論的に研究する。比較する別のheartはAS heartのみ。

- 固定weak標識上のAOU三ブロック線束標識：零次数rootのない条件でW(E6)-torsor。
- 固定heart内の線束選択：明示した代数族仮定の下でvery generalに全Picard格子Λ。
- 圏のexact同値類を点とするfiber：一般形はΓ_L\WとΛ/Γ_A。HがK方向を同一視するので第二fiberは生のPicではない。指定した有限AOU族ではvery generalに自己同値の数値像がZKとなり、標準線束型でW(E6)とPic/ZK。許容Artin変形の全次数にも同じ結論。

線束の一意性、root simpleによるaffine反射と許容半空間条件、三対象交換の実構成、helixからのAS/反標準heart比較を本文に証明する。AOU族への適用に必要な反標準heart・数値・相対比較の仮定は明示する。任意のAOU標識の九対象がlineになる逆向きの認識は未証明であり、第一fiberの結論は標準三ブロック線束型に限定する。全GIT境界や全OU helixの分類ともしていない。新規性の網羅的確認は未完了。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 computations/verify_weyl_frames.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub mainがソース正本。PDF/ZIP/中間物は追跡しない。検証状況と限界は `research/unmark_validation.json` を参照。
