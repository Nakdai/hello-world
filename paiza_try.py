import sys
import os
f = open('input.txt', 'r')
sys.stdin = f
#入力パターン

N,M = list(map(int, input().split()))

for i in range(1,N+1):
    point,count = list(map(int, input().split()))
    if point < count*5:
        point = 0
    else:
        point = point-count*5
    if point >= M:
        print(i)
