import sys

n, m = map(int, sys.stdin.readline().split())

a = []

ans = 0

for _ in range(n):
    aa = list(map(int, sys.stdin.readline().split()))

    a.append(aa)

k = int(sys.stdin.readline())

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())

    i -= 1
    j -= 1
    x -= 1
    y -= 1
    tmpJ = j
    while i <= x and j <= y:
        ans += a[i][j]

        if j == y:
            j = tmpJ
            i += 1
        else:
            j += 1

    print(ans)
    ans = 0
