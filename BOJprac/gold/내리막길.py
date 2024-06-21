# 1520
import sys

sys.setrecursionlimit(10**9)


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if count[x][y] != -1:
        return count[x][y]

    count[x][y] = 1

    tmp = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if not (0 <= nx < n and 0 <= ny < m):
            continue

        if maps[x][y] > maps[nx][ny]:
            tmp += dfs(nx, ny)

    count[x][y] = tmp
    return count[x][y]


n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = [[-1 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(0, 0))
