# 7562
import sys
from collections import deque

testNum = int(sys.stdin.readline())

dx = [-2, 2, -1, 1, 2, -2, 1, -1]
dy = [1, 1, 2, 2, -1, -1, -2, -2]

for _ in range(testNum):
    n = int(sys.stdin.readline())
    locX, locY = map(int, sys.stdin.readline().split())
    aliveX, aliveY = map(int, sys.stdin.readline().split())
    visited = [[False for _ in range(n)] for _ in range(n)]

    que = deque()
    que.append([[locX, locY], 0])
    visited[locX][locY] = True

    while que:
        v = que.popleft()
        x, y = v[0][0], v[0][1]
        cost = v[1]

        if x == aliveX and y == aliveY:
            print(cost)
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                que.append([[nx, ny], cost + 1])
                visited[nx][ny] = True
