# 研究方針：非可換三次曲面の標識忘却

2026-11-17 / unmark-v1。**最初に本ファイルを読み、次に `papers/nc-cubic-unmark.tex` と `research/unmark_notes.md` を読む。** GitHub mainが現行正本。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して研究の価値を最大化する。必要に応じ研究方針を現時点の結論と課題に書き直し、変更履歴を積み上げない。証明済み・条件付き・未証明・予想・有限計算による観察を区別し、各主張の仮定、既存の入力、証明の所在を明記する。先行研究の一次資料を照合し、書誌や新規性を推測で補わない。公表用論文は日本語LuaLaTeXで現在有効な証明と結果を保持する。現行bundleは方針・論文・ノートと必要な最小限のTeX/計算コード/検証手順で自己完結させ、旧版・ZIP・ログ・キャッシュ・重複・PDFをGitに入れない。PDFは必要時に組版する。

**ユーザーから研究区切りごとに承諾なくLibraryへ軽量継続bundleを保存する一般許可を受けている。** GitHubへのpush、Library保存、組版・計算の実行は別々の状態として確認する。Libraryの既存ファイルは明示的な削除指示がない限り削除しない。

## II. 本研究の目標と対象

最優先は、AOU型標準九対象helix → 弱標識付き `(A,O)` → 無標識のAbel圏 `A` の二段階の忘却のファイバー・慣性・相対降下の理解。weakな構造対象はGabriel–Krull rank-one torsion-freeかつexceptionalであり、反Serre作用 `H=S^{-1}[2]` はheartを保ち、Artin–Zhang豊富性と三次曲面の切断数を要求する。**ambientのquadratic AS-regularityは定義にも定理の前提にも入れず、その自動認識問題は保留する。** 別論文 `nc-cubic-ambient-moduli/papers/nc-cubic-ambient.tex` にambient比較を収録する。

## III. 到達点と主張の状態

- 【証明を記載】固定圏上の標識・構造対象の選択群oidと、exact自己同値2-groupの作用による忘却の2-fiber（主論文 `thm:forgetful-fibres`）。全体の代数的stackとしての有限型性は未証明。
- 【証明を記載】可換滑らかな三次曲面では許容構造対象がちょうど線束になる（`thm:commutative-structure`）。AOU標識の有限End代数は全項への共通線束捩れを見ない（`prop:common-tensor`）。
- 【相対仮定付き】可換点での各標識と構造対象の持上げ、形式 `W(E6)` 商（`thm:formal-structure`, `thm:formal-weyl`）。relative heart/Serre/base-changeの条件を無視して全dg変形へ拡張しない。
- 【証明を記載】一次標識変更の障害 `delta_pi(L)=H¹(pi^sharp)c1(L)`、零曲線が滑らかな場合の階数3または4（一般に4）、反標準方向は核に入る（`prop:picard-first-order`, `thm:picard-obstruction-rank`, `prop:canonical-kernel`）。
- 【証明を記載・非常に一般／一次Artin底に限定】整数Picard核は `ZK_X`、許容変形の自己同型群が自明な可換特殊ファイバーでは構造対象軌道集合が `Pic/ZK = Q(E6)^vee = Z^6`（`thm:very-general-picard-kernel`, `cor:first-order-pointings`）。
- 【計算】`computations/verify_marking_lattice.py` はE6根72個、27直線、判別式3、Weyl反射軌道rank6と具体例を正確に検査する。プログラムは圏論的な定理や相対降下の証明ではない。

## IV. 未解決の核心と着手

1. AOUの九対象relation GIT・数値標識・実際の幾何的標識の全同型を、許容な非可換開部分で族と慣性を含めて証明する。
2. 非可換特殊fiber、特に明示的な量子化で許容構造対象のexact自己同値軌道、Picard整数核、高次形式自動同値を計算する。
3. 許容構造対象の相対Moduliの開性・代数性、t-exactなinvertible bimodule、fpqc/étale降下を明らかにする。
4. 全大域的 `W(E6)` 商およびaffine Weyl作用の適用範囲を一次資料と照合する。既知の命題と本研究の新しい部分の優先権確認を進める。

## V. 再現

```sh
python3 -m pip install -r requirements.txt
python3 computations/verify_marking_lattice.py
python3 scripts/verify_unmark_bundle.py
latexmk -lualatex papers/nc-cubic-unmark.tex
```
