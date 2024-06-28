# 11559
import sys
from collections import deque

maps = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
que = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0


def bfs(x, y):
    que = deque()
    que.append((x, y))
    color = maps[x][y]
    tmp = []

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (
                0 <= nx < 12
                and 0 <= ny < 6
                and maps[nx][ny] == color
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                tmp.append((ny, nx))
                que.append((nx, ny))

    if len(tmp) >= 4:
        tmp.sort()
        for j, i in tmp:
            maps[i][j] = "."
            deletePos.append((i, j))


while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    deletePos = []

    for i in range(12):
        for j in range(6):
            if maps[i][j] != "." and not visited[i][j]:
                bfs(i, j)

    if len(deletePos) == 0:
        exit(print(ans))

    for x, y in deletePos:
        for i in range(x, 0, -1):
            maps[i][y] = maps[i - 1][y]
        maps[0][y] = "."

    ans += 1
