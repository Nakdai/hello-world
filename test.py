import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

data = input().split(" ")

line = []
for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        print(data[i],data[j])
        if data[i] != data[j]:
            line.append(data[i])
            #line.pop(j)

print(line)
"""
for x, i in line.items():
    print(x, i)
"""
