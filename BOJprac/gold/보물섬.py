# 2589
import sys
from collections import deque


def bfs(i, j):
    que.append((i, j, 0))
    visited = [[False for _ in range(m)] for _ in range(n)]
    while que:
        x, y, time = que.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and maps[nx][ny] == "L"
            ):
                que.append((nx, ny, time + 1))
                visited[nx][ny] = True
    return time


n, m = map(int, sys.stdin.readline().split())
maps = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    maps.append(list(sys.stdin.readline().rstrip()))

que = deque()
locs = []
ans = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == "L":
            locs.append((i, j))

for loc in locs:
    ans.append(bfs(loc[0], loc[1]))

print(max(ans))
