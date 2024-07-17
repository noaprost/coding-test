# 11049
import sys

n = int(sys.stdin.readline())
dp = [[0 for _ in range(n)] for _ in range(n)]
matrix = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    matrix.append((a, b))

if n == 1:
    exit(print(0))

for i in range(1, n):
    for j in range(n - i):
        m = 10000000000
        for k in range(j, j + i):
            tmp = (
                dp[j][k]
                + dp[k + 1][j + i]
                + matrix[j][0] * matrix[k][1] * matrix[j + i][1]
            )
            m = min(m, tmp)
        dp[j][j + i] = m

print(dp[0][n - 1])
