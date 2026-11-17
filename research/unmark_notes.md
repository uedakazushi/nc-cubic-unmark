# 研究ノート：AOUと無標識Abel圏の形式比較

2026-11-18 / unmark-v5。研究再開は `00_research_plan.md` から。証明は `papers/nc-cubic-unmark.tex` に全て収録（入力ファイル `papers/sections/`）。本ノートは論文に重複する証明を含めず、未解決の境界と計算に必要な情報を残す。

## 形式Artin近傍と大域化の境界

smooth cubic X の標準AOU helix H に対し、De Deken–Lowen Thm5.15 は `Def_ab(Qcoh X) ≃ Def_lin(a_[0,8])` を与える。v4の有向三層quiverの形式完備性と組み合わせ、全Artin関係式変形にGrothendieck Abel heartがある（主論文 `thm:aou-formal-abelian-reconstruction`）。`HH¹(B)=0`、全係数非零の矢スカラー作用のSmith form `diag(1^10,0^8)` から、関係式トーラスの形式8次元チャートが同型類関手を表す。**これは非可換な閉点でAS正則Z代数や反Serreのt-exact性が成立することを保証しない。** 

無標識化は特殊ファイバーの同定変更によりPic(X)⋊Aut(X)の形式作用groupoidとなる。これは形式作用の**存在**であり、Pic作用がAOUトーラスに代数的正則作用として延長することを証明しない。一次の微分はToda/Čechの `δ_π(L)=H¹(π^sharp)c₁(L)`。二次以上の具体式は未計算。全threadへの共通line-bundle twistは関係式End代数を変えないのに、固定した変形のexact自己同値としては一般に持ち上がらない。この差が「relation表示」「pointing」「unmarked」を区別する根本理由。

DDLの入力は `Qcoh X` の Z-generating geometric helix、`Ext^{1,2}(E_i,E_j)=0 (i≤j)`。AOU標準collectionの純粋性・Karpov–Noginの三ブロックhelixを一次資料で再確認する。DDLの結論は**Abel変形**であり、relative Serre Hのt-exact性、weak rank1/exceptionality/AZ性の形式変形全方向への検証を省略しない。局所noetherian性はR-flat生成対象の有限m-adic filtrationで確認。

## 境界と一般方向

全関係式 `R_Q=(P²)^9` で、階数45の有限代数Bとsmooth proper Perf(B)は存在。gldim B=2。各relation pointの係数の支持から作る D_r のrankをρとすると、`HH¹=10−ρ`, `HH²=18−ρ`, `HH^>=3=0`。一般(0,8)、全単項式境界(10,18)。境界のHH次元跳びはAS heartの有無を検出しない。必要なら関係式が2項・1項になる境界でrelative Serre/helixを個別に検査。

Pic(X)のrankは7、Q=K^⊥はE6 rank6、Pic/ZK≅Q^∨、Pic/(Q+ZK)=Z/3。smooth anticanonical Poisson section Cのもとでδの複素rankは3または4、具体的rank4例は `x³+y³+z³+txy+t³=0`, `C={t=0}`。非常に一般で整数核はZK（本稿に証明）。一次線形HH²空間のPic不変多項式/有理関数はPoisson四方向のみ。これを形式非線形・大域GITに無条件拡張しない。

## 次の検証手順

1. AOU標準三ブロックhelixのgeometric/Z-generatingの一次資料の正確な命題を定理の仮定に紐付け、DDL 4.5,5.13,5.15の底の条件を明示。
2. DDLの逆構成からSerre反作用がheartを保つかを、Z-algebraの周期性および生成列のt-structure認識を通じて検討。部分的な結果なら適用可能なArtin底を特定。
3. AOU relation座標でPic formal actionの二次項を計算。固定変形とbase shearの混同を避ける。
4. 境界S-同値を実例で計算し、同じGIT点に非同値のabelian heartsが生じるか判定。

## 主要な一次資料

- AOU, *Compact moduli of marked noncommutative cubic surfaces*, arXiv:2404.00175v1, §4, §5, Thm1.1/1.2; https://arxiv.org/abs/2404.00175
- O. De Deken, W. Lowen, *Abelian and derived deformations in the presence of Z-generating geometric helices*, JNCG 5 (2011), 477–505, Thm4.5/5.13/5.15, DOI 10.4171/JNCG/83; https://ems.press/journals/jncg/articles/4491
- B. Karpov, D. Nogin, *Three-block exceptional collections over Del Pezzo surfaces*, Izv Math 62 (1998), 429–463, DOI 10.1070/IM1998v062n03ABEH000205
- Y. Toda, *Deformations and Fourier–Mukai transforms*, JDG 81 (2009), 197–224, arXiv:math/0502571
- S. Okawa, K. Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, arXiv:2508.04986v1
- Bondal–Orlov, *Reconstruction ...*, Compositio 125 (2001), 327–344, arXiv:alg-geom/9712029
