"""
神経衰弱と呼ばれるトランプゲームのシミュレーションをしましょう。
今回は数字が書かれたトランプのみを考え、ジョーカーは考えません。

まず、トランプを縦 H 枚、横 W 枚の長方形の形に並べた状態でスタートします。
H × W 枚のトランプには 1 〜 13 の数字のうちどれか1つが書かれています。
また、同じ数字が書かれたトランプが複数あります。

プレイヤーが N 人おり、それぞれ 1 〜 N で番号付けられています。
ゲームが始まると、1番の人から、このような手順でプレイしていきます。

・並べられたトランプから2枚のトランプを選び、めくります。
・めくった2枚のトランプに異なる数字が書かれていれば、次のプレイヤーの手番となります。同じ数字であれば、次の操作をおこないます。
・まず、2枚のトランプはめくったプレーヤーのものとなり、取り除かれます。
・トランプがすべて取り除かれた場合、ゲームは終了となります。
・トランプが残っている場合、同じプレーヤーがまた最初の手順に戻り、トランプをめくります。

ここで、N 番のプレイヤーの次のプレイヤーは 1 番のプレイヤーであるとします。

ゲームの初期状態におけるトランプの配置と、ゲームが終わるまでに捲られたトランプに関する時系列順の記録が与えられます。
その記録を用いて、各プレイヤーが取り除いたトランプの枚数を求めてください。

たとえば、入力例1は以下のようになります。
"""
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

inp = input().split(" ")
H = int(inp[0])
W = int(inp[1])
N = int(inp[2])

cards = []
for i in range(H):
    cards.append(input().split(" "))
#print(cards)

points = {}
for i in range(N):
    points[i]=0
#print(points)

num = int(input())
count = 0
for i in range(num):
    plyr = count % N
    #print(plyr)
    pair = input().split(" ")
    pair = list(map((lambda x: int(x)), pair)) #Python 3.Xのmap関数の返り値はmap型のオブジェクト
    #print(pair)
    a = cards[pair[0]-1][pair[1]-1]
    A = cards[pair[2]-1][pair[3]-1]
    #print(a,A)
    if a == A:
        #print(points)
        points[plyr] = points[plyr]+2
    else:
        count += 1
        #print(points)
for i in points:
    print(points[i])
