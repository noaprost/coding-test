# 1915
import sys

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = maps[i][j]

        elif maps[i][j] == 0:
            dp[i][j] = 0

        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        ans = max(dp[i][j], ans)

print(ans**2)
