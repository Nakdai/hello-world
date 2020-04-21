'''整数 N が入力として与えられます。

1からNまでの整数を1から順に表示してください。

ただし、表示しようとしている数値が、

・3の倍数かつ5の倍数のときには、"Fizz Buzz"
・3の倍数のときには、"Fizz"
・5の倍数のときには、"Buzz"

を数値の代わりに表示してください。'''

import sys
import os
f = open('input.txt', 'r')
sys.stdin = f


line = []
for s in range(1,int(input())+1):
    if s % 3 + s % 5 == 0 :
        line.append('Fizz Buzz')
    else:
        if s % 3 == 0 :
            line.append('Fizz')
        elif s % 5 == 0 :
            line.append('Buzz')
        else:
            line.append(s)

for i in line:
    print(i)
