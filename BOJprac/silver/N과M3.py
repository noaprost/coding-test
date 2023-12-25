import sys

n, m = map(int, sys.stdin.readline().split())


def backTracking(num, depth, arr):
    if depth == 0:
        print(*arr)
        return

    if num == n:
        return

    for i in range(1, n + 1):
        if i == num:
            arr = []
            arr.append(i)
        else:
            backTracking(num, depth - 1, arr + [i])


if m == 1:
    for i in range(1, n + 1):
        print(i)
else:
    backTracking(0, m, [])
