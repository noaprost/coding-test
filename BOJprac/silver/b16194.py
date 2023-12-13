# 카드 구매하기2

import sys

n = int(sys.stdin.readline())
dp = [0] + list(map(int, sys.stdin.readline().split()))


for s in range(2, n + 1):
    k = 10001
    for i in range(1, s + 1):
        for j in range(i, s + 1):
            if i + j == s:
                t = dp[i] + dp[j]
                k = min(t, k)
    dp[s] = min(k, dp[s])

print(dp[n])
