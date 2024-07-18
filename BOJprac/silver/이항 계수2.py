import sys

sN, sK = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(sN + 2)] for _ in range(sN + 2)]

for n in range(1, sN + 2):
    for k in range(1, sN + 2):
        if k == 1:
            dp[n][k] = 1
        elif k == n:
            dp[n][k] = 1
        else:
            dp[n][k] = (dp[n - 1][k - 1] + dp[n - 1][k]) % 10007
print(dp[sN + 1][sK + 1])
