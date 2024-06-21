import sys
sys.setrecursionlimit(10**9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if count[x][y]:
        return count[x][y]

    count[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < n):
            continue

        if maps[x][y] < maps[nx][ny]:
            count[x][y] = max(count[x][y], dfs(nx, ny) + 1)
    return count[x][y]


n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not count[i][j]:
            dfs(i, j)
ans = 0
for i in range(n):
    ans = max(ans, max(count[i]))
print(ans)
