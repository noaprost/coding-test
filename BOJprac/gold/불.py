# 5427
import sys
from collections import deque


def bfs():
    hour = 0
    while sanggen:
        hour += 1
        while fire and fire[0][2] < hour:
            x, y, t = fire.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if maps[nx][ny] == "." or maps[nx][ny] == "@":
                        maps[nx][ny] = "*"
                        fire.append((nx, ny, t + 1))

        while sanggen and sanggen[0][2] < hour:
            x, y, t = sanggen.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if maps[nx][ny] == "." and not visited[nx][ny]:
                        visited[nx][ny] = True
                        sanggen.append((nx, ny, t + 1))
                else:
                    return hour

    return "IMPOSSIBLE"


caseNum = int(sys.stdin.readline())
for _ in range(caseNum):
    n, m = map(int, sys.stdin.readline().split())

    maps = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    fire = deque()
    sanggen = deque()

    for i in range(m):
        for j in range(n):
            if maps[i][j] == "@":
                visited[i][j] = True
                sanggen.append((i, j, 0))

    for i in range(m):
        for j in range(n):
            if maps[i][j] == "*":
                fire.append((i, j, 0))

    print(bfs())
