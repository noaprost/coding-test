# 7569
import sys
from collections import deque

c, b, a = map(int, sys.stdin.readline().split())
tomato = []
for _ in range(a):
    tmp = []
    for _ in range(b):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    tomato.append(tmp)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
que = deque()
day = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            if tomato[i][j][k] == 1:
                que.append(((i, j, k), 0))

while que:
    v = que.popleft()
    x, y, z = v[0][0], v[0][1], v[0][2]
    d = v[1]
    isRipe = False
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

        if 0 <= nx < a and 0 <= ny < b and 0 <= nz < c and tomato[nx][ny][nz] == 0:
            que.append(((nx, ny, nz), d + 1))
            tomato[nx][ny][nz] = 1
            isRipe = True

    if isRipe and day < d + 1:
        day = d + 1

for i in range(a):
    for j in range(b):
        if 0 in tomato[i][j]:
            exit(print(-1))

print(day)
