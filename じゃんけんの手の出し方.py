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
#input.txtを標準入力として利用する。
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

inp = input().split(" ")
N = int(inp[0])
M = int(inp[1])
#print(N,M)
hands = input()
G = hands.count("G")
C = hands.count("C")
P = hands.count("P")
#print(G,C,P)

p0 = M//5 if M % 5 == 0 or M % 5 == 2 or M % 5 == 4 else M//5-1
#print(p0)
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
g0 = N - p0 - c0
#print(g0)
def w(k):
    pk = p0 - 2*k
    ck = c0 + 5*k
    gk = g0 - 3*k
    return min(pk,G) + min(ck,P) + min(gk,C)
#print(w(k))
km = p0//2
FK = [w(i) for i in range(km+1)]
wmax = max(FK)
"""
k = 0
wmax = w(0)
while w(k+1)>=w(k) and k <= km:
    wmax = w(k+1)
    k += 1
"""
print(wmax)
