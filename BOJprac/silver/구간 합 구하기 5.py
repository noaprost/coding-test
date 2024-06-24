import sys

n, m = map(int, sys.stdin.readline().split())

maps = [[0 for _ in range(n + 1)]]

for _ in range(n):
    tmp = [0] + list(map(int, sys.stdin.readline().split()))
    maps.append(tmp)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        maps[i][j] += maps[i - 1][j]
        maps[i][j] += maps[i][j - 1]
        maps[i][j] -= maps[i - 1][j - 1]

for _ in range(m):
    ans = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = maps[x2][y2]
    ans -= maps[x1 - 1][y2]
    ans -= maps[x2][y1 - 1]
    ans += maps[x1 - 1][y1 - 1]

    print(ans)
