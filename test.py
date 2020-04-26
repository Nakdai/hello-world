#input.txtを標準入力として利用する。
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

array = [[[0,3]]]

array[0].append([0,1])
array.append([[0,2]])
array[1].append([0,4])
print(array)
print(len(array))

zero_row = [[0]*4]
print(zero_row)


for k in range(len(array)):
    if [0,3] in array[k]:
            array[k].append([1,3])
print(array)

for i in range(len(array[1])):
    array[0].append(array[1][i])
print(array)
print(array[0])
