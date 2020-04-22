"""
あなたは友達たちと N 人でしりとりを行うことにしました。
1 人目、 2 人目、...、 N 人目、 1 人目、2 人目、... という順序で発言をします。

ここで、それぞれの人は、次に挙げる 4 つのしりとりのルールを守って発言をする必要があります。

1. 発言は、単語リストにある K 個の単語のうちのいずれかの単語でなければならない。
2. 最初の人以外の発言の頭文字は、直前の人の発言の最後の文字と一緒でなければならない。
3. 今までに発言された単語を発言してはならない。
4. z で終わる単語を発言してはならない。

ここで、発言の途中で上のルールを破った場合、ルールを破った人はしりとりから外れます。
そして、その人を抜いて引き続きしりとりを続けていきます。このとき、後続の人は、ルール 2 を守る必要はありません。

N 人がしりとりを行ったログが M 行分与えられます。
このとき、M 回の発言が終わった後、しりとりから脱落せずに残っている人のリストを表示するプログラムを書いてください。
"""
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

inp = input().split(" ")
N = int(inp[0])
K = int(inp[1])
M = int(inp[2])

norms = []
for i in range(K):
    norms.append(input())
#print(norms)
norm = "" #現在の発語
count = 0 #1サイクル中の順番
plyrs = [i for i in range(1,N+1)] #アクティブなプレーヤ
fail = 0 #脱落者の人数
next = 0 #次番が試行の先頭か途中か
for i in range(M):
    before = norm #前番の発語
    norm = input()
    #print(norm)
    #print(N-fail)
    #print(plyrs)
    count = (count + next) % (N - fail)
    plyr = plyrs[count] #今発語するプレーヤ
    #ルールに従っているか判定
    R2 = True if next == 0 or before[-1] == norm[0] else False #試行の先頭はR2が不要 しりとりの判定
    R1_3 = True if norm in norms else False #発語がリストにあるかの判定
    R4 = True if not norm[-1] == "z" else False #zで終わってないか判定
    #既出発語をリストから削除
    if norm in norms:
        norms.remove(norm)
    #print(R1_3,R2,R4)
    if R1_3 and R2 and R4 == True:
        next = 1
    else:
        plyrs.remove(plyr) #脱落者を記録
        fail += 1 #脱落者を追加
        next = 0

print(len(plyrs))
for i in plyrs:
    print(i)
