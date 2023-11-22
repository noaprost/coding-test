# 연속합

import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

dp = [nums[0]]

if max(nums) < 0:
    print(max(nums))
else:
    for i in range(1, n):
        dp.append(max(dp[i - 1] + nums[i], 0))
    print(max(dp))
