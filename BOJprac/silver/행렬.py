# 1080
import sys

n, m = map(int, sys.stdin.readline().split())
base_matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
ans_matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
count = 0


def changeMatrix(i, j, matrix):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            matrix[x][y] = 1 - matrix[x][y]


for i in range(n - 2):
    for j in range(m - 2):
        if base_matrix[i][j] != ans_matrix[i][j]:
            changeMatrix(i, j, base_matrix)
            count += 1

for i in range(n):
    for j in range(m):
        if base_matrix[i][j] != ans_matrix[i][j]:
            exit(print(-1))

print(count)
