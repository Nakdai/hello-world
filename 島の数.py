import sys
import os
f = open('input.txt', 'r')
sys.stdin = f
# 表の列数と行数の入力を受け取り、int型に変換
col, row = [int(x) for x in input().split()]

# 1行目を"0"で埋める
map_list = [["0"] * (col+2)]

# 各行に対して繰り返す
for i in range(row):
    # "0"で挟む
    map_list.append(["0"] + input().split() + ["0"])

# 1行目と同じリストを最後の行に追加
map_list.append(map_list[0])

# 関数を定義
def check(x, y):
    # リストを定義し最初の場所を追加
    lands = [[x, y]]

    # landsの要素が無くなるまで繰り返す
    while lands:
        # 座標を更新
        x, y = lands.pop()

        # "0"に置換
        map_list[y][x] = "0"

        # 下の場所
        if map_list[y+1][x] == "1":
            lands.append([x, y+1])
        # 右の場所
        if map_list[y][x+1] == "1":
            lands.append([x+1, y])
        # 上の場所
        if map_list[y-1][x] == "1":
            lands.append([x, y-1])
        # 左の場所
        if map_list[y][x-1] == "1":
            lands.append([x-1, y])

# 島の数を数える変数
count = 0

''' colが列数、rowが行数 '''
# 2行目からrow+1行目まで繰り返す
for i in range(1, row+1):
    # 2列目からcol+1列目まで繰り返す
    for j in range(1, col+1):
        # "1"の場合
        if map_list[i][j] == "1":
          # 島の大きさを確認し"0"に置換
            check(j, i)

            # 島をカウント
            count += 1

# 島の数を出力
print(count)
