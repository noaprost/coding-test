# 가장 긴 감소하는 부분 수열
import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.reverse()

dp = [1]
x = [num[0]]

for i in range(1, n):
    if num[i] > x[-1]:
        x.append(num[i])
        dp.append(dp[-1] + 1)
    else:
        idx = bisect_left(x, num[i])
        x[idx] = num[i]

print(dp[-1])
