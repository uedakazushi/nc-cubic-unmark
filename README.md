# AOU relation moduli と非可換三次曲面の無標識 Abel 圏

2026-11-18 / unmark-v4。**再開時は `00_research_plan.md` を読む。** 主論文は `papers/nc-cubic-unmark.tex` （日本語 LuaLaTeX）。GitHub main が正本。

中心課題は AOU 九関係式 stack / GIT 粗商と、非可換三次曲面の**無標識 Abel 圏**の関係。関係式のすべての点には rank45 の普遍有限代数 `B_r` が存在し、`gldim B_r=2`、`Perf(B_r)` は smooth proper。しかし `mod B_r` は可換点でも `coh X` とは Abel 同値ではなく、三次曲面型 heart の認識が未解決。

現在の主結果：Artin 局所上の有限代数変形を九関係式で完全記述。境界で `dim HH¹=10−ρ`, `dim HH²=18−ρ`, `HH³=0`（支持行列の階数ρ）。dense torus では HH¹=0,HH²=8。滑らかな cubic 点では AOU torus の KS 写像 `T M_Q° ≅ HH²(X)`。加えて、可換 locus の W(E6) 商、Picard 一次 shear と非常に一般の核 ZK、一次 shear の不変式の計算を保持。

AOU 関係式の全点が非可換三次曲面の Abel heart を持つ、GIT S-同値が exact Abel 同値を与える、あるいは無標識大域 stack が有限型であるとは主張しない。

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

Git に PDF、ZIP、コンパイル中間物を追跡しない。ambient は別の [nc-cubic-ambient](https://github.com/uedakazushi/nc-cubic-ambient) を参照。
