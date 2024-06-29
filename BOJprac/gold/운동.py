# 1956
import sys

v, e = map(int, sys.stdin.readline().split())
dist = [[1e9 for _ in range(v + 1)] for _ in range(v + 1)]

for _ in range(e):
    x, y, c = map(int, sys.stdin.readline().split())
    dist[x][y] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = 1e8
for i in range(1, v + 1):
    ans = min(ans, dist[i][i])

if ans == 1e8:
    print(-1)
else:
    print(ans)
