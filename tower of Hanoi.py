import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

n,t = [int(x) for x in input().split()]
#n,m = list(map(int, input().split()))
by = []
for i in range(n):
    by.append(t % 2)
    t = t//2

start = 0
middle = 1
goal = 2
disks = [[],[],[]]
for k in range(n):
    if by[n-k-1] == 0:
        middle,goal = goal,middle
        disks[start].append((n-k))
    elif by[n-k-1] == 1:
        middle,start = start,middle
        disks[goal].append((n-k))

print(type(disks[0])

"""
for i in range(3):
    if len(disks[i]) == 0:
        print("-")
    else:
        l = disks[i]
        print(l)
        [print(l[j]) for j in range(l)]
"""
