# 1520
import sys

m, n = map(int, sys.stdin.readline().split())

maps = []

for _ in range(m):
    maps.append(list(map(int, sys.stdin.readline().split())))

visited = [[False for _ in range(n)] for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0


def dfs(node, visited):
    global ans
    x, y = node[0], node[1]

    if x == m - 1 and y == n - 1:
        ans += 1
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if (
            0 <= nx < m
            and 0 <= ny < n
            and not visited[nx][ny]
            and maps[x][y] > maps[nx][ny]
        ):
            visited[nx][ny] = True
            dfs([nx, ny], visited)
            visited[nx][ny] = False


dfs([0, 0], visited)
print(ans)
