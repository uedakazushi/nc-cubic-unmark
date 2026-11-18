# 非可換三次曲面の二段階の標識忘却

2026-11-18 / unmark-v12。再開は **`00_research_plan.md`**、次に `papers/nc-cubic-unmark.tex` と `research/unmark_notes.md`。

anticanonical heartを基準に集合論的に研究する。比較する別のheartはAS heartのみ。

標準AOU relation torusの非常に一般の点について、本文 `thm:actual-aou-very-general` は次を示す。

- 指定反標準heartのweak公理とAS heartとのexact比較を実際の稠密開部分で確認する。
- 固定heart内では全数値Picard類が一意の許容線束として実現され、`Line_adm=Line≅Λ`。
- 固定weak標識上の標準Euler型・full very strongなAOU標識は全て九線束の標識となり、`W(E6)`-torsorをなす。
- exact自己同値の数値像は `Γ_A=ZK`。圏のexact同値類を点とする忘却写像の第一fiberは51840点の `W(E6)`-torsor、第二は `Λ/ZK≅P(E6)`。固定圏内の線束選択そのものはΛであり、第二fiberとは区別する。

fiberはweak公理と指定AS/反標準比較に適合する標準AOU標識の最大の定義域で取る（`def:maximal-weak-compatible-aou`）。証明用の小さい開部分へmarked側を制限すると別のWeyl標識を落とす可能性がある。一般OUの全型、全GIT境界、Weyl作用の全域正則性はこの結論に含めない。

線束の内在的判定と一意性、root simpleによるaffine反射と許容半空間条件、三対象交換、右反標準tailによるtorsion-free認識、中心楕円因子からのheart・Gabriel--Krull filtrationの認識を本文に証明する。許容Artin変形の全次数のfiber定理も保持する。次の課題は特殊locus、root simpleの実在・排除、最大weak適合locusの境界と作用、先行研究との優先権比較である。新規性の網羅的確認は未完了。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 computations/verify_line_bundle_numerics.py
python3 computations/verify_weyl_frames.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

GitHub mainがソース正本。PDF/ZIP/中間物は追跡しない。当該版の計算・組版などの検証状況と限界は `research/unmark_validation.json` を参照。生成・検証・GitHub反映・Library保存は別々に確認する。
