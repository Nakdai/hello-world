import sys
import os
f = open('input.txt', 'r')
sys.stdin = f
# 表の列数と行数の入力を受け取り、int型に変換
N = int(input())
nums = [int(input()) for i in range(N)]
#print(nums)
count = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            pair = nums[i]+nums[j]+nums[k]
            #print(nums[i],nums[j],nums[k])
            if pair % 7 == 0:
                count += 1
print(count)
