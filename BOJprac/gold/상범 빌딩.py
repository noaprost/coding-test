# 6593
import sys
from collections import deque

h, x, y = map(int, sys.stdin.readline().split())

while h != 0:
    maps = []
    for _ in range(h):
        tmp = []
        for _ in range(x):
            tmp.append(list(sys.stdin.readline().rstrip()))
        input()
        maps.append(tmp)

    que = deque()
    visited = [[[False for _ in range(y)] for _ in range(x)] for _ in range(h)]
    dh = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]
    dy = [1, -1, 0, 0, 0, 0]

    for i in range(h):
        for j in range(x):
            for k in range(y):
                if maps[i][j][k] == "S":
                    que.append((i, j, k, 0))
                    visited[i][j][k] = True

    while que:
        v = que.popleft()
        v1, v2, v3, time = v[0], v[1], v[2], v[3]

        if maps[v1][v2][v3] == "E":
            print("Escaped in", time, "minute(s).")
            break

        for i in range(6):
            nv1 = v1 + dh[i]
            nv2 = v2 + dx[i]
            nv3 = v3 + dy[i]

            if (
                0 <= nv1 < h
                and 0 <= nv2 < x
                and 0 <= nv3 < y
                and not visited[nv1][nv2][nv3]
                and (maps[nv1][nv2][nv3] == "." or maps[nv1][nv2][nv3] == "E")
            ):
                que.append((nv1, nv2, nv3, time + 1))
                visited[nv1][nv2][nv3] = True

    else:
        print("Trapped!")

    h, x, y = map(int, sys.stdin.readline().split())
