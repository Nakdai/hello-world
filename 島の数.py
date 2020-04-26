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
irlands = []
for i in range(N):
    irlands.append(input().split())
#print(irlands)
"""
#In[]
M,N = 4,5
irlands = [["0","1","1","0"],["1","0","1","0"],["1","0","0","0"],["0","0","1","1"],["0","1","1","1"]]
"""
#1行目、1列目に0ベクトルを追加する。
zero_row = [["0"]*M]
irlands = zero_row + irlands
for i in range(N+1):
    irlands[i].insert(0,"0")
#print(irlands)

#In[]
same_irland = []
loop0 = 0
loop1 = 0
loop2 = 0
loop3 = 0
loop4 = 0
loop5 = 0
stock = 0
#2行目2列目を起点に1セルずつ見ていく。
for i in range(1,N+1):
    for j in range(1,M+1):
        #セルの値が1の場合は左隣と上隣の値で場合分けする。
        if irlands[i][j] == "1":
            #左隣が0、上隣が0の場合。same_irlandにセルの座標を加え、カウントアップする。
            if irlands[i][j-1] == "0":
                if irlands[i-1][j] == "0":
                    same_irland.append([[i,j]])
                    loop0 += 1
                #左隣が0、上隣が1の場合。上のセルを含む第2次元リストにセルを加える。
                elif irlands[i-1][j] == "1":
                    for k in range(len(same_irland)):
                        if [i-1,j] in same_irland[k]:
                            stock = k
                    same_irland[k].append([i,j])
                    loop1 += 1
            #左隣が1の場合。same_irlandの最後にセルを追加。
            elif irlands[i][j-1] == "1":
                same_irland[-1].append([i,j])
                loop2 += 1
                #左隣が1、上隣が1の場合。上のセルを含む第2次元リストにセルを加える。
                if irlands[i-1][j] == "1":
                    for k in range(len(same_irland)):
                        if [i-1,j] in same_irland[k]:
                            stock = k
                    #上のセルと左のセルが異なる第2次元リストに含まれる場合は、両者を含む第2次元リストを統合する。
                    if stock != len(same_irland):
                        for l in range(len(same_irland[-1])):
                            same_irland[stock].append(same_irland[-1][l])
                        del same_irland[-1]
                    #上のセルと左のセルが同じ第2次元リストに含まれる場合は、既にセルが追加済み。
            loop3 += 1
        loop4 += 1
    loop5 += 1
print(loop0,loop1,loop2,loop3,loop4,loop5)


print(same_irland)
