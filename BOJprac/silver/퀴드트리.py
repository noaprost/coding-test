import sys

sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
bw = [list(sys.stdin.readline().rstrip()) for _ in range(n)]


def check(x, y, d):
    cur = bw[x][y]
    for i in range(x, x + d):
        for j in range(y, y + d):
            if bw[i][j] != cur:
                return -1
    return cur


def rec(x, y, n):
    if check(x, y, n) != -1:
        return check(x, y, n)

    tmp = ""
    if rec(x, y, n // 2) != -1:
        tmp += rec(x, y, n // 2)

    if rec(x, y + n // 2, n // 2) != -1:
        tmp += rec(x, y + n // 2, n // 2)

    if rec(x + n // 2, y, n // 2) != -1:
        tmp += rec(x + n // 2, y, n // 2)

    if rec(x + n // 2, y + n // 2, n // 2) != -1:
        tmp += rec(x + n // 2, y + n // 2, n // 2)

    return "(" + tmp + ")"


print(rec(0, 0, n))
