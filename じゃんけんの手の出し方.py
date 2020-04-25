"""あなたはこれから友人と N 回じゃんけんをします。しかし、あなたは全てを見通す千里眼の持ち主なので、友人がこれから出す N 回のじゃんけんの手が全て分かってしまいました。

ただただ全勝してしまうのは面白くないので、あなたは、N 回のじゃんけんで出した指の本数の合計がちょうど M 本になるようにじゃんけんをすることにしました。
このとき、あなたは最高で何回じゃんけんに勝つことができるでしょうか。


ここで、上の文中に出てくる「出した指の本数」というのは、じゃんけんで出した手の何本の指が立っていたか、ということであり、グー、チョキ、パーそれぞれ

・グー　のとき ... 0 本
・チョキのとき ... 2 本
・パー　のとき ... 5 本

の指を出していたということになります。



例えば、あなたが 4 回のじゃんけんで グー、パー、チョキ、グー と出したとすると、出した指の本数の合計は、

0 + 5 + 2 + 0 = 7

で 7 本となります。"""
# In[]
# N,Mの生成
import random

N = random.randint(1,1000)

g = random.randint(0,N)
c = random.randint(0,N-g)
p = N-c-g
M = 5*p + 2*c
print(N,M)
# In[]
# 相手の手札の生成
G = random.randint(0,N)
C = random.randint(0,N-G)
P = N-C-G
print(G,C,P)
# In[]
N = 245
M = 1214
G = 68
C = 92
P = 85
#In[]
p0 = M//5 if M % 5 == 0 or M % 5 == 2 or M % 5 == 4 else M//5-1
print(p0)
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
print(c0)
# In[]
g0 = N - p0 - c0
print(g0)
#In[]
k = 0
km = min(p0//2,g0//3)
print(km)
#In[]
def w(k):
    pk = p0 - 2*k
    ck = c0 + 5*k
    gk = g0 - 3*k
    return min(pk,G) + min(ck,P) + min(gk,C)
print(w(k))
#In[]
import matplotlib.pyplot as plt
import numpy as np

K = np.arange(km)
WK = [w(k) for k in range(km+1)]
print(WK)
#In[]
fig, ax = plt.subplots() # Create a figure containing a single axes.
ax.plot(K,WK) # Plot some data on the axes.

#In[]
FK = [w(i) for i in range(km+1)]
wmax = max(FK)

print(wmax)
# In[]
