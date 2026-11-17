# 研究方針：AOU relation moduli と無標識 Abel 圏

2026-11-18 / unmark-v4。研究再開時は **本ファイルを最初に読む**。次に `papers/nc-cubic-unmark.tex`（全証明）、`research/unmark_notes.md`（残る障害）、`computations/verify_aou_relation_tangent.py`（有限計算）を参照する。現行正本は GitHub `uedakazushi/nc-cubic-unmark` の `main`。

## I. 恒常的な研究原則・保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究の価値を最大化する。方針は現時点の結果と課題を理解できるよう書き直し、変更履歴を堆積しない。既知の定理、原稿に証明を記載した結果、独立検証済みの結果、条件付き結果、未証明の推測、有限計算を区別し、依存関係と未解決箇所を明記する。先行研究の一次資料を調べ、未確認の新規性・書誌を推測しない。論文は日本語 LuaLaTeX で書き、既存の有効な結果と証明を保持する。

**ユーザーは研究の区切りごとに承諾なしで軽量・自己完結の現行研究継続 bundle を Library に保存することを一般的に許可している。** 旧 ZIP・旧原稿・ログ・キャッシュ・重複を同梱しない。Library 上の既存ファイルを明示指示なく削除しない。ファイル生成・検証・GitHub push・Library 保存は別々に記録し、成功を確認した操作だけ報告する。

## II. 目標と達成基準

AOU 九関係式モジュライから**無標識 Abel 圏**への忘却を、定義域・本質像・ファイバー・相対慣性・GIT 粗商への降下の観点から理解し、独立して投稿可能な論文にする。次の階層を区別する：

1. 九関係式の全空間 `R_Q=(P²)^9` と quotient stack `[R_Q/G_Q]`；
2. GIT 線形化に依存する粗商 `M_Q^χ`；
3. すべての relation 点で定義される45次元有限代数 `B_r` と smooth proper `Perf(B_r)`；
4. 相対 AS-regular helix と適切な t-structure の証拠を備えた圏的許容表示；
5. 弱標識付き `(A,O)`、および無標識 Abel 圏 `A`。

重要な変更の理由：AOU relation は全境界で有限代数と導来圏を与えるが、標準 heart `mod B_r` は可換点でも `coh X` と同値でない。従って必要なのは導来圏の存在自体ではなく、三次曲面型 Abel heart と Serre/helix 条件を認識すること。以前の目標である AOU→無標識 Abel 圏の全域降下は依然未解決。ambient quadratic AS 正則性の認識問題は別リポジトリ `nc-cubic-ambient` に分離する。

## III. 主要結果・証明の所在

- 【本稿証明】全関係式空間上に階数45の普遍有限代数があり、各 fiber の大域次元は2、smooth proper dg category を与える（`thm:universal-directed-family`, `papers/sections/aou_universal_algebras.tex`）。これは三次曲面型 Abel heart を与えるとは主張しない。
- 【本稿証明】Artin 局所上のすべての平坦な有限代数変形は九つの関係式の変形と矢の基底変換で記述される（`thm:aou-relation-formal-completeness`）。既存の AOU の三層 quiver の特殊な性質を利用。
- 【本稿証明】任意の relation 点で支持行列 `D_r` の階数をρとすると `HH^0=C`, `dim HH¹=10−ρ`, `dim HH²=18−ρ`, `HH^{≥3}=0`。dense torus では `(0,8)`、単項式関係式では `(10,18)`（`thm:aou-hh-support`）。`computations/verify_aou_relation_tangent.py` は整数行列の rank10・Smith 標準形と境界例を検算。数学的証明は論文。
- 【本稿証明、既知 Morita 理論使用】smooth 可換 cubic の AOU relation トーラスにおける Kodaira–Spencer `T M_Q° ≅ HH²(B) ≅ HH²(X)`（`prop:aou-kodaira-spencer-iso`）。**有限代数の一次変形**の比較として確立。相対 Abel heart の全変形とはまだ同一視していない。
- 【既知 AOU と本稿証明】AOU, arXiv:2404.00175v1 は全 relation stack と toric GIT（§5）、可換 marked locus の局所閉埋込み（Thm 1.2）。本稿は可換無標識同型類が `W(E6)` 軌道に等しいことを示す（`thm:aou-commutative-quotient`）。OU, arXiv:2508.04986v1 の Def. 1.1(4) は AS-regular potentials の開 substack を定義。
- 【本稿証明、相対仮定付き】弱標識付き構造対象の分類と持上げ、形式 `W(E6)` 比較、一次 Picard shear、一般 rank4、非常に一般の整数核 `ZK_X`、構造対象軌道 `Pic/ZK=Z⁶`（`marking_forgetful.tex`）。境界/全非可換点への一般化は未証明。
- 【本稿証明、線形一次模型限定】`C[HH²(X)]^Pic=C[H⁰(-K)]` と有理不変式、分離粗商の情報消失（`picard_invariants.tex`）。**AOU の非線形 GIT 全域の不変式ではない**。
- 【定義的・条件付き】圏的許容 AOU 表示から unmarked Abel 圏への擬関手、追加持上げ条件下の無限 helix fiber、GIT S-同値の必要条件（`aou_to_unmarked.tex`）。全 GIT への降下や無標識 stack の有限型性は未証明。

## IV. 次の重要課題（具体的着手）

1. **最優先：相対 Abel heart 認識**。`Perf(B)` の smooth 可換点近傍で既知の `coh X` の heart を復元し、DDL の変形同値・Serre の t-exact性・AZ 豊富性を統合して、関係式 torus のどこで相対 `qgr` が定義できるかを証明する。
2. **Picard action の relation 座標**。今回の tangent の完全性を使い、`r_L(ξ,π)` が八次元 relation トーラスの形式座標でどう現れるかを構成し、二次以降の障害を調べる。固定 Abel 圏の自己同値と Morita 標識変更を区別する。
3. **境界と GIT 降下**。支持行列による `HH¹/HH²` 跳びと AS-regular locus の交わりを調べる。GIT の S-同値点間で Abel heart の同値性を確認する。有限代数の smoothness と cubic heart の存在を混同しない。
4. **投稿準備**。AOU/OU/DDL/Toda の一次資料との比較、形式定理の仮定と stack 慣性、可換 Picard の既知性を Introduction で明確化。数学的な原稿査読と全体の LuaLaTeX 組版を行う。

## V. 再現

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

PDFは Git に追跡しない。現行 bundle には PDF と全 TeX・計算コード・簡潔な検証手順を収録する。
