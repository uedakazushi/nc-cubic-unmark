# 研究方針：AOU 関係式と無標識 Abel 圏

2026-11-18 / unmark-v5。**再開時は本ファイルを最初に読む。** 正本は `uedakazushi/nc-cubic-unmark` の main。続いて `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md` を読む。

## I. 恒常的な研究原則・保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を考慮して研究価値を最大化する。現時点の有効な方針として書き直し、時系列の履歴は持たない。既知の結果・本稿の証明・独立に確認した計算・相対仮定付きの結果・未証明を区別し、各定理の証明と依存する文献を明記する。新規性が未確認ならその旨を明記する。主論文は日本語LuaLaTeX、現行の有効な成果と証明を保持する。

**ユーザーは研究の区切りごとに承諾なしで、最新の軽量・自己完結な研究継続 bundle を Library に保存することを一般的に許可している。** 現行の研究方針・研究ノート・論文・必要なソース・PDF・計算コードだけを入れ、旧ZIP、ログ、キャッシュ、重複は入れない。Library上の既存ファイルを明示指示なしに削除しない。生成・実行・GitHub push・Library保存を別々に検証する。

## II. 最重要課題・達成基準

AOU の九関係式モジュライから無標識 Abel 圏への忘却の**定義域・本質像・ファイバー・慣性・GIT降下**を数学的に理解し、投稿可能な論文にする。区別すべき対象は `(P²)^9` と関係式stack、GIT粗商、有限代数BとPerf(B)、形式Artin上で復元するQcoh/ coh型heart、AS正則・反Serre t-exact性・AZ豊富性を満たす弱標識付き圏、無標識圏である。

本研究では、**滑らかな可換AOU点の形式近傍**に対しては、有限代数の関係式完備性とDe Deken–Lowen Theorem 5.15を結合し、すべてのArtin関係式変形から平坦Grothendieck Abel変形を回復する。標準helixを選ぶと8次元形式チャートを得る。標識を忘れるとPic(X)⋊Aut(X)の形式作用が現れ、一次作用はPicard shearとなる。**これはGIT全境界でのAbel圏の存在や、全8方向でのweakly marked公理の検証とは異なる。**

大域AOU moduli上に適切なAS-regular heartを認識し、その同型条件と慣性を決めることが上位目標。ambientのquadratic AS正則認識は別リポジトリ `uedakazushi/nc-cubic-ambient` に属する。

## III. 到達点と主張の状態

- 【本稿証明、既知のDDL定理を使用】smooth cubicの標準AOU helixのZ-generating/geometric条件の下、`Def_ab(Qcoh X) ≃ Def_lin(B)`。v4の関係式形式完備性から全局所Artin関係式変形がAbel heartへ持ち上がり、局所noetherian性も確保（`thm:aou-formal-abelian-reconstruction`）。必要な文献：DDL Thms 4.5,5.13,5.15、AOU §4、Karpov–Nogin。
- 【本稿証明】全係数非零トーラスのsmooth可換点で、標識付き形式Abel変形関手は8次元トーラス商の形式完成に同型（`thm:aou-formal-chart`）。同型類関手であり、普遍的な大域正則座標ではない。
- 【本稿証明、相対同定について】Pic(X)⋊Aut(X)が形式変形関手に作用し、一次作用は`(ξ,π)↦(ξ+H¹(π^sharp)c₁(L),π)`。自然同型によりrigidifyした無標識形式変形はこの群の形式作用groupoid（`prop:formal-picard-action`, `cor:aou-formal-unmarked-quotient`）。明示的な高次座標式は未計算。
- 【本稿証明】普遍45次元有限代数B_r、全点gldim2/smooth proper dg圏、Artin代数変形の九関係式による形式完備性（`aou_universal_algebras.tex`）。これは全点での三次曲面型Abel heartを意味しない。
- 【本稿証明】支持行列D_rの階数ρにより`dim HH¹(B_r)=10−ρ`, `dim HH²(B_r)=18−ρ`, `HH^n=0(n≥3)`。全係数非零で(0,8)、単項式関係式境界で(10,18)。計算コード `verify_aou_relation_tangent.py` はrankとSmith標準形のみを検算。
- 【可換部分・本稿証明】smooth可換AOU locusの無標識同型類は古典W(E6)商、一般に51840標識（`aou_to_unmarked.tex`）。GIT粗商全体のWeyl作用ではない。
- 【相対仮定付き】weak構造対象と形式W(E6)商、非常に一般のPoisson一次変形の整数核ZK、許容構造対象の自己同値軌道集合Pic/ZK≅Z⁶（`marking_forgetful.tex`）。AS性と相対Serre t-exact性は別途要確認。
- 【一次線形模型についての本稿証明】Picard shearの不変式環は`C[H⁰(-K_X)]`、分離的粗商では可換変形方向が失われる（`picard_invariants.tex`）。非線形AOU GITの不変式とは主張しない。
- 【未解決】全AOU境界でのAS/heart、幾何学的ファイバーでの代数化、形式Picard作用の高次表示、GIT S-同値とAbel同値との適合、unmarked代数的stackの構成。

## IV. 優先課題・具体的着手

1. **形式から代数的なheartへの拡張**：標準helixのArtin変形を、AOU関係式トーラスの実際の非可換開集合へ代数化する。反Serre `S^{-1}[2]` のt-exact性、rank-one構造対象、AZ豊富性が相対的に保たれるための開条件または明示的な反例を求める。
2. **高次Picard作用の算出**：DDLの逆構成とTodaのMorita変換を比較し、形式作用の二次項・不変式・非分離性を計算する。標準helixを共通Lで捩っても関係式は変わらないが、形式チャートの同定が変わることに留意。
3. **GITとAbel圏の同値類**：半安定境界のS-同値点で三次曲面型heartを持つか、同値なheartになるかを判定。普遍Perf(B)の存在とt-exact Abel圏の存在を混同しない。
4. **投稿品質**：AOU/DDL/KN/OU/Todaの一次資料と適用範囲、新規性を照合。局所的な既知定理と本稿の新しい組合せの寄与をIntroductionで具体的に分ける。全TeX組版・有限計算・論理検証を反復する。

## V. 再現

```
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

PDFや中間生成物はGit追跡せず、bundleには現行PDFと全TeX、検証コードを収録する。形式変形の証明と外部査読の状態は分ける。
