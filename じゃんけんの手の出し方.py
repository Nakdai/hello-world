import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# じゃんけんの回数と指の合計の本数の入力を受け取り、int型に変換
num, finger = [int(x) for x in input().split()]

# 相手の出す手の入力を受け取る
hands = input()

# 相手がグーを出す回数
g = hands.count("G")

# 相手がチョキを出す回数
c = hands.count("C")

# 相手がパーを出す回数
p = num - g - c

# パーを出せる最大の回数
max_p = finger // 5

# 最大の勝利数を代入する変数を定義
max_win = 0

# パーの回数（範囲：0 ~ num）
for i in range(max_p + 1):
    # チョキの回数（範囲：0 ~ num - i)
    for j in range(num + 1 - i):
        # 合計の数がfingerと等しい時
        if 5*i + 2*j == finger:
            # 勝利数を計算
            win = min(g, i) + min(p, j) + min(c, num - i - j)
            # 以前より大きい場合のみ更新
            max_win = max(max_win, win)

# 最大の勝利数を出力
print(max_win)
