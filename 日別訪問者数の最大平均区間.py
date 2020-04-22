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

#入力
days = input().split(" ")
#print(days)
all = int(days[0])
camp = int(days[1])
 #リストの要素を全て数値型にする。
data = list(map((lambda x: int(x)), input().split(" ")))

term_i = sum(data[0:camp]) #最初の区間の訪問者数
max_term = term_i #訪問者数最大区間
cand_day = 1 #候補日の数
earliest_cand = 0 #一番早い候補日

#2番目以降の訪問者数
for i in range(1,all-camp+1):
    term_i = term_i - data[i-1] + data[i+camp-1]
    if term_i == max_term:
        cand_day += 1
    elif term_i > max_term:
        earliest_cand = i
        max_term = term_i
        cand_day = 1

print(cand_day,earliest_cand+1)
