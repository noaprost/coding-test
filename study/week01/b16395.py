# 파스칼의 삼각형
import sys

dp = [[0 for _ in range(31)] for _ in range(31)]

sN, sK = map(int, sys.stdin.readline().split())

for n in range(31):
    for k in range(31):
        if k == 1:
            dp[n][k] = 1
        elif k == n:
            dp[n][k] = 1
        else:
            dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k]

print(dp[sN][sK])
