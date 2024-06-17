# 11058
import sys

n = int(sys.stdin.readline())

dp = [0, 1, 2, 3, 4, 5, 6]

for i in range(7, n + 1):
    dp.append(max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4))

print(dp[n])
