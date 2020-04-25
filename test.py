

import sys
import os
f = open('input.txt', 'r')
sys.stdin = f
#In[]
# じゃんけんの回数と指の合計の本数の入力を受け取り、int型に変換
N, M = [int(x) for x in input().split()]

# 相手の出す手の入力を受け取る
hands = input()

# 相手がグーを出す回数
G = hands.count("G")

# 相手がチョキを出す回数
C = hands.count("C")

# 相手がパーを出す回数
P = N - G - C
p0 = M//5 if M % 5 == 0 or M % 5 == 2 or M % 5 == 4 else M//5-1
#print(p0)
# In[]
if M % 5 == 0:
    c0 = 0
elif M % 5 == 1:
    c0 = 3
elif M % 5 == 2:
    c0 = 1
elif M % 5 == 3:
    c0 = 4
elif M % 5 == 4:
    c0 = 2
#print(c0)
# In[]
g0 = N - p0 - c0
#print(g0)
#In[]
k = 0
km = min(p0//2,g0//3)
#print(km)
#In[]
def w(k):
    pk = p0 - 2*k
    ck = c0 + 5*k
    gk = g0 - 3*k
    return min(pk,G) + min(ck,P) + min(gk,C)
#print(w(k))
#In[]
import matplotlib.pyplot as plt
import numpy as np

K = np.arange(km)
WK = [w(k) for k in range(km+1)]
#print(WK)
#In[]
#fig, ax = plt.subplots() # Create a figure containing a single axes.
#ax.plot(K,WK) # Plot some data on the axes.

#In[]
wmax = max(WK)

print(wmax)
# In[]

