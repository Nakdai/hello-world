"""
列の数がM、行の数がNの表があります。表の各マスは白か黒で塗られています。
黒で塗られたマスが上下左右で隣接している時、その黒マスの塊をまとめて「島」と呼びます。
例えば、以下のような4列×5行の表（M=4、N=5）があった場合、


この表には以下の(1)～(3)のように3つの島が存在します。


島の数を計算して出力するプログラムを作成して下さい。
"""

# 標準入力からの取得
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f
#In[]
#入力
M,N = [int(x) for x in input().split()]
islands = []
for i in range(N):
    islands.append(input().split())
#print(irlands)
"""
import random

M = random.randint(1,100)
N = random.randint(1,100)
islands = []
islands = [[str(random.randint(0,1)) for j in range(M)] for i in range(N)]
print(M,N)
"""
#1行目、1列目に0ベクトルを追加する。
zero_row = [["0"]*M]
islands = zero_row + islands
for i in range(N+1):
    islands[i].insert(0,"0")
#print(islands)

#In[]
same_island = []
loop = 0
#2行目2列目を起点に1セルずつ見ていく。
for i in range(1,N+1):
    for j in range(1,M+1):
        if islands[i][j] == "1":
            clear = 0
            for k in range(len(same_island)):
                if [i,j-1] in same_island[k]:
                    same_island[k].append([i,j])
                    left = k
                    clear += 1
            for k in range(len(same_island)):
                if [i-1,j] in same_island[k]:
                    same_island[k].append([i,j])
                    up = k
                    clear += 1
            if clear == 2 and left != up:
                for l in range(len(same_island[left])):
                    same_island[up].append(same_island[left][l])
                #same_island[up].remove([i,j])
                del same_island[left]
            if clear == 0:
                same_island.append([[i,j]])
            loop += 1

#print(loop)
#print(same_island)
print(len(same_island))
