# 1309
import sys

n = int(sys.stdin.readline())
dp = [1, 3]

for i in range(2, n + 1):
    dp.append((dp[i - 1] * 2 + dp[i - 2]) % 9901)

print(dp[n])
