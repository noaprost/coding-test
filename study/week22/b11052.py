# 카드 구매하기

import sys

n = int(sys.stdin.readline())
dp = [0] + list(map(int, sys.stdin.readline().split()))

for s in range(2, n + 1):
    k = 0
    for i in range(1, s + 1):
        for j in range(i, s + 1):
            if i + j == s:
                k = max(k, dp[i] + dp[j])
    dp[s] = max(k, dp[s])

print(dp[n])
