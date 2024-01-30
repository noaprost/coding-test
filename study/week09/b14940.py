# 쉬운 최단거리

import sys
from queue import Queue

n, m = map(int, sys.stdin.readline().split())

# n x m map
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

que = Queue()

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            que.put([i, j])
            maps[i][j] = 0

while que.qsize() != 0:
    v = que.get()
    x = v[0]
    y = v[1]
    visited[x][y] = True
    if (x > 0) and not visited[x - 1][y] and maps[x - 1][y] != 0:
        que.put([x - 1, y])
        visited[x - 1][y] = True
        maps[x - 1][y] += maps[x][y]

    if (x < n - 1) and not visited[x + 1][y] and maps[x + 1][y] != 0:
        que.put([x + 1, y])
        visited[x + 1][y] = True
        maps[x + 1][y] += maps[x][y]

    if (y > 0) and not visited[x][y - 1] and maps[x][y - 1] != 0:
        que.put([x, y - 1])
        visited[x][y - 1] = True
        maps[x][y - 1] += maps[x][y]

    if (y < m - 1) and not visited[x][y + 1] and maps[x][y + 1] != 0:
        que.put([x, y + 1])
        visited[x][y + 1] = True
        maps[x][y + 1] += maps[x][y]

for i in range(n):
    for j in range(m):
        if not visited[i][j] and maps[i][j] != 0:
            maps[i][j] = -1

for i in range(n):
    for j in range(m):
        print(maps[i][j], end=" ")
    print()
