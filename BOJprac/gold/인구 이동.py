# 16234
import sys
from collections import deque


def bfs(a, b):
    que.append((a, b))
    move = []
    move.append((a, b))
    peo = maps[a][b]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and (L <= abs(maps[nx][ny] - maps[x][y]) <= R)
            ):
                move.append((nx, ny))
                que.append((nx, ny))
                peo += maps[nx][ny]
                visited[nx][ny] = True

    if len(move) <= 1:
        return 0
    
    p = peo // len(move)
    for i, j in move:
        maps[i][j] = p
    return 1


n, L, R = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

loc = []
for i in range(n):
    for j in range(n):
        loc.append((i, j))

day = 0
while True:
    flag = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    que = deque()
    for i, j in loc:
        if not visited[i][j]:
            visited[i][j] = True
            flag += bfs(i, j)

    if flag == 0:
        break
    day += 1

print(day)
