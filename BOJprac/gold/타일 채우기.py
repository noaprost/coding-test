# 2133

import sys

n = int(sys.stdin.readline())

dp = [1, 0, 3] + [0 for _ in range(n - 2)]

if n % 2 != 0:
    exit(print(0))

for k in range(4, n + 1, 2):
    dp[k] += 3 * dp[k - 2]
    for i in range(4, k + 1, 2):
        dp[k] += 2 * dp[k - i]

print(dp[n])
