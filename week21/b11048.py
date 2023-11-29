# 이동하기
import sys

n, m = map(int, sys.stdin.readline().split())

candy = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    candy[i][0] += candy[i - 1][0]

for j in range(1, m):
    candy[0][j] += candy[0][j - 1]

for i in range(1, n):
    for j in range(1, m):
        candy[i][j] += max(candy[i - 1][j], candy[i][j - 1])

print(candy[n - 1][m - 1])
