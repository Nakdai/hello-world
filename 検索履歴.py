"""
あなたが利用しているブラウザでは検索ワードの履歴を見ることができません。あなたは検索ワードの履歴を見られないのは不便だと思ったので、検索ワードの履歴を見る機能を自分でつくることにしました。

検索ワードの履歴とは次のようにつくられます。

検索ワード W が以前に入力されたことがある場合：
履歴中の W を削除する。
履歴の先頭に W を追加する。
検索ワード W が以前に入力されたことがない場合：
履歴の先頭に W を追加する。

検索ワード W が N 個与えられるので、N 個の検索ワードが与えられた後の履歴を表示するプログラムを書いてください。
"""
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

num = int(input())

hist = []

for i in range(num):
    hist_i = input()
    if hist_i in hist:
        hist.remove(hist_i)
    hist.insert(0,hist_i)

for i in hist:
    print(i)
