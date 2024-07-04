# 23250
n, k = map(int, input().split())


def hanoi(n, start, end, via):
    global k

    if n == 0:
        return

    if k + 1 <= 2 ** (n - 1):
        hanoi(n - 1, start, via, end)
    else:
        k = k - 2 ** (n - 1) + 1

    k -= 1

    if k == 0:
        exit(print(start, end))

    if k + 1 <= 2 ** (n - 1):
        hanoi(n - 1, via, end, start)
    else:
        k = k - 2 ** (n - 1) + 1


hanoi(n, 1, 3, 2)
