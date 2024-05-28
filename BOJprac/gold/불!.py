# 4179
import sys
from collections import deque


def bfs():
    hour = 0
    while jihun:
        hour += 1
        while fire and fire[0][2] < hour:
            x, y, t = fire.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if maps[nx][ny] == "." or maps[nx][ny] == "J":
                        maps[nx][ny] = "F"
                        fire.append((nx, ny, t + 1))

        while jihun and jihun[0][2] < hour:
            x, y, t = jihun.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if maps[nx][ny] == "." and not visited[nx][ny]:
                        visited[nx][ny] = True
                        jihun.append((nx, ny, t + 1))
                else:
                    return hour

    return "IMPOSSIBLE"


m, n = map(int, sys.stdin.readline().split())

maps = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fire = deque()
jihun = deque()

for i in range(m):
    for j in range(n):
        if maps[i][j] == "J":
            visited[i][j] = True
            jihun.append((i, j, 0))

for i in range(m):
    for j in range(n):
        if maps[i][j] == "F":
            fire.append((i, j, 0))

print(bfs())
