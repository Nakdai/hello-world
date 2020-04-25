
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

