# 3055
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()


def bfs(ax, by):
    while queue:
        x, y = queue.popleft()
        if graph[ax][by] == "S":
            return dist[ax][by]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == "." or graph[nx][ny] == "D") and graph[x][
                    y
                ] == "S":
                    graph[nx][ny] = "S"
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                elif (graph[nx][ny] == "." or graph[nx][ny] == "S") and graph[x][
                    y
                ] == "*":
                    graph[nx][ny] = "*"
                    queue.append((nx, ny))
    return "KAKTUS"


for i in range(n):
    for j in range(m):
        if graph[i][j] == "S":
            queue.append((i, j))
        elif graph[i][j] == "D":
            x, y = i, j

for i in range(n):
    for j in range(m):
        if graph[i][j] == "*":
            queue.append((i, j))

print(bfs(x, y))
