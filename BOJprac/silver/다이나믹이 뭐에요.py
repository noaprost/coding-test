import sys

n, m = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    matrix[i][0] = 1

for i in range(m):
    matrix[0][i] = 1

for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] + matrix[i - 1][j - 1]

print(matrix[n - 1][m - 1] % 1000000007)
