'''スペースで区切られた英単語列が与えられます。
英単語列に含まれる英単語の出現回数を出現した順番に出力してください。'''

#input.txtを標準入力として利用する。
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

data = input().split(" ")

counts = {}

for x in data:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1
#print(counts)

for x, i in counts.items():
    print(x, i)
