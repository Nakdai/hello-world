#input.txtを標準入力として利用する。
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

array = []

for k in range(len(array)):
    if k == 0:
        print(1)
    continue
print(2)
