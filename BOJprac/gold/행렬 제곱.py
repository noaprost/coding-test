# 10830
import sys

n, p = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def matrix_multi(u, v):
    global n
    z = [[0 for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            s = 0

            for i in range(n):
                s += u[row][i] * v[i][col]
            z[row][col] = s % 1000
    return z


def matrix_square(matrix, power):
    global n
    if power == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000

        return matrix

    tmp = matrix_square(matrix, power // 2)

    if power % 2 == 0:
        return matrix_multi(tmp, tmp)
    else:
        return matrix_multi(matrix_multi(tmp, tmp), matrix)


answer = matrix_square(a, p)
for ans in answer:
    print(*ans)
