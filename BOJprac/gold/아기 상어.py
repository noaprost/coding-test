# 16236
import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(time, x, y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    fish = []
    que = deque()
    que.append((time, x, y))
    visited[x][y] = True

    while que:
        time, x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 상어가 갈 수 있는 길
                if maps[nx][ny] == 0 or maps[nx][ny] == size:
                    que.append((time + 1, nx, ny))
                    visited[nx][ny] = True

                # 상어가 먹을 수 있는 길
                elif 0 < maps[nx][ny] < size:
                    fish.append((time + 1, nx, ny))
                    visited[nx][ny] = True

    if len(fish) == 0:
        return False
    else:
        return sorted(fish)  # 자동으로 최단 거리, 가장 왼쪽, 가장 위가 맨 앞에 오게 됨


size = 2
count = 0
time = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            x, y = i, j

while True:
    maps[x][y] = 0
    ans = bfs(0, x, y)

    if ans == False:
        print(time)
        break

    count += 1
    if size == count:
        size += 1
        count = 0

    x = ans[0][1]
    y = ans[0][2]
    time += ans[0][0]
