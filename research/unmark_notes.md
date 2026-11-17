# 研究ノート：AOU 関係式から無標識 Abel 圏へ

2026-11-18 / unmark-v4。最初に `00_research_plan.md` を読む。詳細な証明は論文の `papers/sections/aou_universal_algebras.tex`、`aou_to_unmarked.tex`、`marking_forgetful.tex`、`picard_invariants.tex` に保持する。本ノートには今後必要な論点と反例的障害のみ整理する。

## 三層 quiver による普遍有限代数と boundary

AOU Q は U,W,Z の各3頂点で、隣接層完全二部グラフ (18矢印) かつ長さ3の道がない。各 U→Z に三つの道と一本の関係式で九つの P²。全 `R_Q=(P²)^9` に普遍代数 B rank45 =9頂点+18矢+18残存二歩道。任意の関係式は非零なので、単純加群の極小射影解消は長さ≤2、全 fiber gldim=2。双加群解消の長さも2（無重複関係式）で、すべての `Perf(B)` が smooth proper。**AS regular helix と三次曲面型 heart はここから自動的に従わない。** 可換点でも `mod B` は有限長で `coh X` と Abel 同値でない。

全 Artin 局所の平坦な B 変形は冪等元を持ち上げて18箭基底を選び、九つの `R³→R²` の核線を読むことで relation から得る。逆向きは普遍 flat B。冪等元持上げは nilpotent inner conjugacy、基底の差は矢 rescaling。代数の変形と Abel heart の変形を取り違えない。

支持集合 `S_{ij}={m:c_{ijm}≠0}` の各組で `a_{im}+b_{mj}` の差をとった行列の rank ρ は HH の跳びを決める：`dim HH¹=10−ρ`, `dim HH²=18−ρ`, `HH^{≥3}=0`。全係数非零の dense torus では ρ=10（HH¹=0, HH²=8）、全単項式点では ρ=0（HH¹=10, HH²=18）。境界の dg deformation が跳ぶ現象を正確に追えるが、無標識 Abel 自己同値の跳びと同一視しない。Smith normal form `1^10,0^8` は整数計算 `verify_aou_relation_tangent.py` で検査。

可換 X の relation dense torus の KS は `T M_Q° → HH²(B) → HH²(X)` の8次元同型。HH² の内訳は H¹(T_X)4 + H⁰(-K_X)4。この比較は **有限次元代数** について完了。適切な heart を伴う変形との全形式比較は別の課題。

## Abel heart・AOU GIT・標識忘却の障害

AOU の M_rel と GIT M_Q^χ は異なる。OU (arXiv:2508.04986 Def 1.1(4)) は AS-regular potential の marked moduli を開部分として定義しているが、全 M_Q^χ に AS regularity や heart を与えていない。普遍 B の smooth properness は GIT の S-同値で derived/Morita 同値が成り立つことすら意味しない。必要なのは cubic-type t-structure と Serre/helix/AZ の相対的同定。

可換 smooth X の通常標識は W(E6)-torsor (|W|=51840)、Gabriel で exact coh 同値が X の同型と同値。AOU relation algebra は全 thread を同じ線束で tensor しても不変だが、非可換 Artin fiber 上の tensor autoequivalence は一般に持ち上がらない。この違いと raw 2-group の慣性を保持する。

Picard shear: `r_L(ξ,π)=(ξ+H¹(π^sharp)c₁(L),π)`。滑らかな零因子のとき複素階数3または4、一般4。非常に一般の整数核は ZK_X だが、これは一次 Picard action の必要条件であって高次の自己同値群の完全記述ではない。許容一次 Abel 変形で相対 Serre を持つと fixed category の構造対象軌道は Pic/ZK≅Z6。すべての twists を標準 helix として持ち上げる追加仮定を外して AOU GIT fiber の無限性を主張しない。

Picard shear の線形一次不変式は `C[HH²]^Pic=C[H⁰(-K)]`, 有理不変式も同様。有限型分離粗商は可換方向を潰す。しかし AOU relation torus の**非線形** Picard action を構成していないため、全 GIT 粗商の障害へ無条件に拡張しない。

## 研究再開の具体的課題

- `Perf(B)` の **heart 問題**：AOU 原論文 §4.6 の periodic Z-algebra と OU2025 very strong helix の構成に、今回得た Artin relation 完備性を接続する。Deken--Lowen の相対 Abel 変形定理の仮定（幾何学的生成、t-exact Serre、底変更）を一つずつ証明または追加仮定として正確に切り分ける。
- **非線形 Picard charts**：marking O と一般 L の relation 形式座標間の遷移を Toda 一次公式から高次へ計算する。固定 Abel 圏の自己同値と Morita 同値を区別。
- **boundary 支持パターン**：ρ が落ちる stratum と AS-open、GIT 半安定性の交差を計算する。単項式点の HH¹=10 は高い慣性の例として保持する。
- **一次資料**：AOU arXiv:2404.00175v1 §§4.2, 4.6, 5.1–5.4, Thm1.2; OU arXiv:2508.04986v1 Definition1.1(4), Definition3.1, Thm6.4; DDL DOI 10.4171/JNCG/83; Toda arXiv:math/0502571; Gabriel DOI 10.24033/bsmf.1583; Bondal–Orlov arXiv:alg-geom/9712029。これらと新規性の最終比較は未了。
