# 25682
import sys


n, m, k = map(int, sys.stdin.readline().split())
chess = [sys.stdin.readline().rstrip() for _ in range(n)]
b = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
w = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            if chess[i][j] == "B":
                b[i][j] = 1 + b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]
                w[i][j] = 0 + w[i - 1][j] + w[i][j - 1] - w[i - 1][j - 1]
            else:
                b[i][j] = 0 + b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]
                w[i][j] = 1 + w[i - 1][j] + w[i][j - 1] - w[i - 1][j - 1]
        else:
            if chess[i][j] == "B":
                b[i][j] = 0 + b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]
                w[i][j] = 1 + w[i - 1][j] + w[i][j - 1] - w[i - 1][j - 1]
            else:
                b[i][j] = 1 + b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1]
                w[i][j] = 0 + w[i - 1][j] + w[i][j - 1] - w[i - 1][j - 1]

ans = 2000000
for i in range(-1, n - k):
    for j in range(-1, m - k):
        B_sub_sum = b[i + k][j + k] - b[i][j + k] - b[i + k][j] + b[i][j]
        W_sub_sum = w[i + k][j + k] - w[i][j + k] - w[i + k][j] + w[i][j]
        ans = min(ans, B_sub_sum, W_sub_sum)

print(ans)
