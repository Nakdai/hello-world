#input.txtを標準入力として利用する。
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f
