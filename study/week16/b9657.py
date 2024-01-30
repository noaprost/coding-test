# 돌게임 3

import sys

n = int(sys.stdin.readline())

dp = ["", "SK", "CY", "SK", "SK"]

for i in range(5, n + 1):
    if dp[i - 1] == "CY" or dp[i - 3] == "CY" or dp[i - 4] == "CY":
        dp.append("SK")
    else:
        dp.append("CY")
print(dp)
