# 2580
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
        for d in doku:
            print(*d)
        exit()

    for i in range(1, 10):
        x, y = blank[n]

        if existRow(x, i) and existCol(y, i) and existSquare(x, y, i):
            doku[x][y] = i
            sudoku(n + 1)
            doku[x][y] = 0


doku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if doku[i][j] == 0:
            blank.append([i, j])
sudoku(0)
