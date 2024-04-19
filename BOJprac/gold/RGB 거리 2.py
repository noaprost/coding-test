# 17404
import sys

INF = 1e8
n = int(sys.stdin.readline())
ans = INF

rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for c in range(3):
    dp = [[INF for _ in range(3)] for _ in range(n)]
    dp[0][c] = rgb[0][c]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]  # 빨
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]  # 초
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]  # 파

    for j in range(3):
        if c != j:
            ans = min(ans, dp[-1][j])

print(ans)
