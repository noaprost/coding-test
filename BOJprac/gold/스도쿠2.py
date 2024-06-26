# 2239
import sys


def existRow(x, n):
    for i in range(9):
        if n == doku[x][i]:
            return False
    return True


def existCol(y, n):
    for i in range(9):
        if n == doku[i][y]:
            return False
    return True


def existSquare(x, y, n):
    for i in range(3):
        for j in range(3):
            if n == doku[x // 3 * 3 + i][y // 3 * 3 + j]:
                return False
    return True


def sudoku(n):
    if n == len(blank):
        for do in doku:
            for d in do:
                print(d, end="")
            print()
        exit()

    for i in range(1, 10):
        x, y = blank[n][0], blank[n][1]

        if existRow(x, i) and existCol(y, i) and existSquare(x, y, i):
            doku[x][y] = i
            sudoku(n + 1)
            doku[x][y] = 0


doku = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if doku[i][j] == 0:
            blank.append([i, j])
sudoku(0)
