"""
あなたは、とあるウェブサイトを管理していました。
ある連続したk日間、このウェブサイトでキャンペーンを行ったのですが、いつからいつまでの期間に行ったかを忘れてしまいました。

幸い、ウェブサイトを運営していた全n日分のアクセスログが残っており、1日ごとの訪問者数が分かっています。
とりあえず、連続するk日の中で、1日あたりの平均訪問者数が最も多い期間を、キャンペーンを行った期間の候補だと考えることにしました。

n日分の訪問者数のリストとキャンペーンの日数kが入力されるので、キャンペーンを行った期間の候補数と、候補の中で最も早い開始日を出力してください。
"""

import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

days = input().split(" ")
#print(days)

all = int(days[0])
camp = int(days[1])
data = input().split(" ")
#print(data)
#print(data[0:0+camp])
data_sum = []
s = []

for i in range(all-camp+1):
    s = data[i:i+camp]
    #リストの要素を全て数値型にする。
    s = map((lambda x: int(x)), s)
    data_i = sum(s)
    #print(data_i)
    data_sum.append(data_i)

cand_day = max(data_sum)
print(data_sum.count(cand_day),end = " ")

x = 0
while True:
    if data_sum[x] == cand_day:
        print(x+1)
        break
    x += 1
