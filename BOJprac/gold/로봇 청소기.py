# 14503
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
sx, sy, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maps[sx][sy] = 2
c = 1

que = deque()
que.append((sx, sy))
while que:
    x, y = que.popleft()
    # 4방향에 청소되지 않은 빈칸이 있는지 확인
    for _ in range(4):
        # 반시계 방향 회전
        d = (d + 3) % 4

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
            maps[nx][ny] = 2
            que.append((nx, ny))
            c += 1
            break

    if not que:
        if maps[x - dx[d]][y - dy[d]] == 1:
            exit(print(c))
        else:
            que.append((x - dx[d], y - dy[d]))
