# 第3回
## 迷路ゲーム：迷えるこうかとん（ex03/maze.py）
### ゲーム概要
- ex03/maze.pyを実行すると，1500x900にcanvasに迷路が描画され，迷路に沿ってこうかとんを移動させるゲーム
- 実行するたびに迷路の構造は変化する
- スタート位置は黄色で示されており、目指すゴールは赤色である
- ゴールをすると迷路はリセットされ、初期位置に戻る
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
- rキーを押すことでリセットできる
- 特定の矢印キーの入力による隠しコマンドがある
### 追加機能
- スタート位置とゴールの色の変更
- リセット機能:こうかとんの位置と迷路を再生成する関数を作成した。rキーの押下時、ゴール時に呼び出すことによって、リセットを行う
- 隠しコマンド機能:入力したキーを保存することでコマンドを判定する機能を作成した。今回は、「上、左、下、右」を入力すると壁の中に入れるようになる。「上」を６回入力すると加速する。
### ToDo（実装しようと思ったけど時間がなかった）
- その他のコマンドの実装：減速するコマンド、こうかとんが増殖するコマンドなど
- ゴールの位置が生成された迷路によって変化する
- ゴール演出　
- if文の簡略化
### メモ
- コマンドで変化した状態は、同じコマンドを再度入力することで解除できる