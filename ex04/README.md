# 第4回
## 逃げろこうかとん（ex04/dodge_bomb.py）
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
- Rキーでリセットすることができる
### 追加機能
- 1秒ごとに爆弾が増殖する
- Rキー押下時のリセット機能
- 爆弾の色をランダムに決定する
- 20%の確率で速い爆弾が生まれる
- 20%の確率で遅い爆弾が生まれる
- 33%の確率で大きい爆弾が生まれる
### ToDo（実装しようと思ったけど時間がなかった）
- if文を１行にする
- ゲームオーバー演出
### メモ
- 爆弾を増殖させるために、爆弾のリストを作成した。また、爆弾の生成をwhile文内に取り入れた。
- if文を短縮した
- 爆弾生成時の範囲を1からにすることでバグが生まれないようにした