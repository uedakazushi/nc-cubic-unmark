# 研究方針：AOU 関係式モジュライと無標識 Abel 圏

**2026-11-18 / unmark-v6。** 再開時はまず本ファイル、次に `papers/nc-cubic-unmark.tex`、`research/unmark_notes.md` を読む。GitHub `uedakazushi/nc-cubic-unmark` の `main` を原稿ソースの正本とする。最新 bundle のみで再組版・再計算できる構成を維持する。

## I. 恒常的な研究原則と保存許可

研究全体の価値を、数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性によって最大化する。状況に応じて目標と優先順位を変更し、研究方針は現時点で有効な内容に書き直す。過去の更新履歴は蓄積しない。既知の結果、本研究で証明を記載した結果、独立に検証した計算、追加仮定付きの主張、未証明の問題を区別する。主要主張の仮定・依存文献・証明所在・未検証点を明記し、新規性が未確認ならその旨を記す。論文は原則日本語 LuaLaTeX で書き、有効な証明・成果を維持する。先行研究は可能な限り一次資料に当たり、書誌を推測しない。

**ユーザーは研究の区切りごとに承諾なく軽量で自己完結した現行の研究継続 bundle を Library に保存する一般許可を与えている。** 収録物は研究方針・研究ノート・現行論文・必要な全ソース・PDF・計算コード・再現手順だけとし、旧 ZIP、旧原稿、ログ、キャッシュ、履歴、不要な重複を含めない。Library の既存ファイルは明示的な指示なしに削除しない。生成・組版・計算・GitHub push・Library 保存は別々に検証して報告する。

## II. 研究目標と現在の判断

最重要課題は AOU の九関係式モジュライから **無標識 Abel 圏への忘却の定義域・本質像・ファイバー・慣性・GIT 降下** を解明し、投稿可能な論文に仕上げること。関係式空間 `(P²)^9` と stack、GIT 粗商、普遍 45 次元有限代数 `B_r` と `Perf(B_r)`、AS-regular `Z` 代数の `qgr` heart、弱標識付き `(A,O)`、無標識 `A` はそれぞれ異なる対象として扱う。

**現時点の重要な整理：** AOU Theorem 1.1 と §7 の既知の楕円 decuple 構成から、8 次元関係式トーラスの稠密な Zariski 開部分に実際の AS-regular heart が存在する（論文 `prop:generic-as-locus`）。滑らかな可換 AOU 点の Artin 形式近傍には DDL Thm 5.15 から Grothendieck Abel 変形を復元できる（`thm:aou-formal-abelian-reconstruction`）。**一方、全境界には smooth proper `Perf(B_r)` と一定の数値的 Serre–E6 があるが、数値標識だけでは Abel heart を認識できない（`thm:aou-numerical-E6`）。** 形式的な存在、稠密開の実際の存在、全境界での認識を混同しない。

上位目標は、AS 型 heart が存在する開集合における **実際の相対族と exact 同値判定** を確立し、標識忘却の群oid・慣性を計算すること。ambient の quadratic AS-regular 認識は別の `uedakazushi/nc-cubic-ambient` を扱う。

## III. 到達点：仮定・証明状態・所在

- 【先行研究の直接の帰結】AOU Theorem 1.1、Proposition 7.3、Lemma 7.4 と OU の AS 構成から、稠密開 `U_ell⊂M_Q^°` の各点で `qgr A_r` と `Perf(B_r)` の tilting 同値が得られる（論文 `prop:generic-as-locus`）。点ごとの存在は成立するが、このことだけで全弱標識公理、相対 fpqc 降下、無標識同型類の一意性は得られない。
- 【本稿に証明】全関係式空間の普遍有限代数の階数 45、大域次元 2、相対 smooth proper `Perf(B)`（`thm:universal-directed-family`）、関係式による Artin 代数変形の形式完備性（`thm:aou-relation-formal-completeness`）。
- 【本稿に証明／厳密計算で検算】境界の Hochschild 次元 `dim HH¹=10−ρ`, `dim HH²=18−ρ`（`thm:aou-hh-support`）、稠密トーラスで `(0,8)`、全単項式境界で `(10,18)`、一つの関係式だけ単項式としても `(0,8)`（`prop:aou-boundary-hh-minimal`）。
- 【本稿に証明／厳密計算で検算】Euler 形式と数値的 Serre 作用は全関係式点で一定、`(S−1)^3=0`、rank `(S−1)=2`、rank `(S−1)^2=1`、`ker(S−1)/radχ ≅ E6`（`thm:aou-numerical-E6`）。矢の基底変更群はこの E6 に自明に作用し、古典 Weyl 標識変更とは異なる（`prop:aou-numerical-trivial-torus`）。全単項式境界と稠密トーラスは同じ数値不変量でも `HH¹` が異なり、導来 Morita 非同値（`cor:aou-numerical-not-enough`）。
- 【既知 DDL 定理を用いた本稿証明／適用条件あり】滑らかな可換 AOU 点の標準 `Z`-generating geometric helix と DDL Theorem 5.15 を入力として `Def_ab(Qcoh X)≃Def_lin(B)` を構成し、AOU の 8 次元形式 chart と Picard 形式作用を得る（`formal_abelian_recognition.tex`）。relative anti-Serre の全方向 t-exact 性は未証明。
- 【本稿に証明】可換 locus の W(E6) 標識忘却（一般 51840 標識）、選択 2-fiber と exact 自己同値による quotient、可換構造対象は線束（`aou_to_unmarked.tex` と `marking_forgetful.tex`）。
- 【相対仮定付き】Poisson 一次 Picard shear `δ_π(L)=H¹(π^sharp)c₁(L)`、rank4 の具体例、非常に一般の整数 Picard 核 `ZK_X` と許容 Artin 変形上の構造対象軌道 `Pic/ZK≅Z⁶`。相対 AS/Serre/heart の条件と「非常に一般」の範囲を外さない。
- 【一次線形模型のみ】Picard shear の多項式・有理不変式は Poisson 4 方向の関数環（`picard_invariants.tex`）。このことだけで大域 GIT や無標識粗 moduli の非存在を主張しない。
- 【未解決】AS heart の実際の相対 algebraic 族、全境界、GIT の S-同値での Abel 同値判定、非可換一般点の exact 自己同値慣性、形式 Picard 作用の高次明示式、普遍的無標識 stack の代数性。

## IV. 優先順位と着手手順

1. **稠密 AS locus の相対幾何学**：AOU 楕円 decuple の fine moduli と OU の相対 helix、`qgr` 再構成から、開集合 `U_ell` 上の fpqc/étale 族とその base-change、Serre t-exact 性、AZ 豊富性、構造対象の rank/exceptionality を個別に検証する。既知の存在定理の入力を厳密に区別する。
2. **無標識同値判定**：`U_ell` 上で二つの decuple/AS heart がいつ exact 同値となるかを調べ、Picard 形式作用や mutations と比較。特に `G_Q` の矢基底変更は E6 に自明、W(E6) は非自明という差異を利用する。
3. **境界の幾何的判定**：数値的 E6 は全点に存在する一方、HH 次元は複雑に変化する。有限 algebra と anticanonical helix/heart の独立な認識条件を構成する。境界に全く heart がないと早合点しない。
4. **論文品質**：AOU/DDL/OU/KN/Toda/Bondal–Orlov の一次資料と証明を照合し、独自結果と既知の帰結を Introduction で区別。未確認の新規性は未確認と記す。完成していない大域定理を完成扱いしない。

## V. 再現

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 computations/verify_aou_relation_tangent.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```

TeX 全体、計算コード、PDF、依存設定を現行 bundle に収録する。GitHub は TeX/コードのみ追跡、PDF・ログ・キャッシュ・ZIP を追跡しない。検証記録は `research/unmark_validation.json` に現在の状態のみ記す。
