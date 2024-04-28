# 11404
import sys

INF = 1e9

cityN = int(sys.stdin.readline())
busN = int(sys.stdin.readline())

pl = [[INF for _ in range(cityN + 1)] for _ in range(cityN + 1)]

for i in range(1, cityN + 1):
    for j in range(1, cityN + 1):
        if i == j:
            pl[i][j] = 0

for _ in range(busN):
    s, e, cost = map(int, sys.stdin.readline().split())
    pl[s][e] = min(cost, pl[s][e])

for k in range(1, cityN + 1):
    for i in range(1, cityN + 1):
        for j in range(1, cityN + 1):
            if pl[i][k] + pl[k][j] < pl[i][j]:
                pl[i][j] = pl[i][k] + pl[k][j]

for i in range(1, cityN + 1):
    for j in range(1, cityN + 1):
        if pl[i][j] == INF:
            print(0, end=" ")
        else:
            print(pl[i][j], end=" ")
    print()
