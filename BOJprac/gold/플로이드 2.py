# 11780
import sys

INF = 1e9

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
path = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
pl = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    pl[s][e] = min(cost, pl[s][e])
    path[s][e] = s


for k in range(1, n + 1):
    pl[k][k] = 0
    path[k][k] = -1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if pl[i][k] + pl[k][j] < pl[i][j]:
                pl[i][j] = pl[i][k] + pl[k][j]
                path[i][j] = path[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if pl[i][j] == INF:
            print(0, end=" ")
        else:
            print(pl[i][j], end=" ")
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if path[i][j] == -1:
            print("0")
            continue

        v = j
        ans = [j]
        while v != i:
            v = path[i][v]
            ans.append(v)

        ans.reverse()
        print(len(ans), *ans)
