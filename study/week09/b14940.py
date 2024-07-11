# 쉬운 최단거리
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

que = deque()

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            que.append((i, j))
            maps[i][j] = 0

while que:
    x, y = que.popleft()
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 0:
            que.append((nx, ny))
            visited[nx][ny] = True
            maps[nx][ny] += maps[x][y]

for i in range(n):
    for j in range(m):
        if not visited[i][j] and maps[i][j] != 0:
            maps[i][j] = -1

for i in range(n):
    print(*maps[i])
