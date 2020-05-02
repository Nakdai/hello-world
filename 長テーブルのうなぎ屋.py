import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

n,m = [int(x) for x in input().split()]
#n,m = list(map(int, input().split()))
sitting = []
for i in range(m):
    a,b = [int(x) for x in input().split()]
    b -= 1 #席番号を0,1,...,n-1にする。
    check = 0
    for j in range(b,a+b):
        if j % n in sitting:
            check = 1
    if check == 0:
        for j in range(b,a+b):
            sitting.append(j%n)

print(len(sitting))
