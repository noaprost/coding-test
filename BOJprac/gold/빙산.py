# 2573
import sys
from collections import deque


def countSurroundingWater(x, y):
    count = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
            count += 1

    return count


def bfs(x, y):
    fade = []
    que.append((x, y))
    visited[x][y] = True
    fade.append((x, y, countSurroundingWater(x, y)))
    while que:
        v = que.popleft()
        x, y = v[0], v[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] > 0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    fade.append((nx, ny, countSurroundingWater(nx, ny)))

    if len(fade) != 0:
        for f in fade:
            x, y, c = f[0], f[1], f[2]
            maps[x][y] = max(0, maps[x][y] - c)

    return 1


n, m = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

ices = []
for i in range(n):
    for j in range(m):
        if maps[i][j] > 0:
            ices.append((i, j))

year = 0  # 걸린 시간(년)
que = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while ices:
    visited = [[False for _ in range(m)] for _ in range(n)]
    deleteIce = []  # 0이 되서 삭제해야하는 빙산 배열
    piece = 0  # 빙산 개수

    for ice in ices:
        x, y = ice[0], ice[1]
        if maps[x][y] > 0 and not visited[x][y]:
            piece += bfs(x, y)
        if maps[x][y] == 0:
            deleteIce.append((x, y))
    if piece > 1:
        exit(print(year))

    ices = sorted(list(set(ices) - set(deleteIce)))
    year += 1

print(0)
