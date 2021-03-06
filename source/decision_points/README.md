# このフォルダの説明
- このフォルダは，交点サークルとブロックサークルの各座標を取得するためのプログラムが入っています．
- `get_circle_point.py`は，台形補正した画像にドラッグ・アンド・ドロップで四角形を描くことで，座標を求めます．
- `move_get_circle_point.py`は，四角形で囲んで求めた座標を，**tkinter**で描画しマウスで手動で修正できます．

## `get_circle_point.py`の使い方
- `get_circle_point.py`を実行
- 端の交点サークルの中心に四角形の頂点が来るようにドラッグ・アンド・ドロップ
- すべての交点サークルの座標と場所を描画します
- ブロックサークルの中心に四角形の頂点が来るようにドラッグ・アンド・ドロップ
- すべてのブロックサークルの座標と場所を描画します
- 交点サークル，ブロックサークルすべての座標を求めると，辞書型のメンバ変数である，`named_points`に座標を代入（`BlockBingoPoint.py`にあったやつと同じ）
- どれかのキーボードを押すと処理を終了します
---
#### 注意
- 途中でキーボードを押すとその時点で処理を終了します
- 四角形で囲む時に起点をどこから囲んでもきちんと計算できます．
---
## `move_get_circle_point.py`の使い方
- `move_get_circle_point.py`を実行
- 上に記載してあるまずは，`get_circle_point.py`の使い方の通りに囲んでください
- `tkinter`が起動し各サークル上に円を描画します
- 修正したい箇所をマウスでドラッグ・アンド・ドロップで修正してください
- 終了したい時は，バツボタンを押してください
---
#### 注意
- マウスで円を掴んで動かす時にマウスが早すぎると変な動きをします
- 円を掴んでいる状態で他の円にぶつかると変な挙動をします
---