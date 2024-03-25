# 1987
import sys

sys.setrecursionlimit(10**5)

n, m = map(int, sys.stdin.readline().split())

maps = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [False for _ in range(26)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

distance = []


def dfs(x, y, dist):
    distance.append(dist)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[ord(maps[nx][ny]) - 65]:
            visited[ord(maps[nx][ny]) - 65] = True
            dfs(nx, ny, dist + 1)
            visited[ord(maps[nx][ny]) - 65] = False


visited[ord(maps[0][0]) - 65] = True
dfs(0, 0, 1)
print(max(distance))
