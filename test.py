import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

data = input().split(" ")

counts = {}
for i in range(0,len(data)):
    for j in range(i,len(data)):
        if i<j and data[i] != data[j]:

    else:
        counts[x] = 1
print(counts)

for x, i in counts.items():
    print(x, i)
