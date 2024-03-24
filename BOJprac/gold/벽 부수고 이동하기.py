# 2206
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    s = list(str(sys.stdin.readline().rstrip()))
    board.append(list(map(int, s)))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

que = deque()
que.append([0, 0, 0])
visited[0][0][0] = 1

while que:
    x, y, flag = que.popleft()
    if x == n - 1 and y == m - 1:
        exit(print(visited[x][y][flag]))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                visited[nx][ny][flag] = visited[x][y][flag] + 1
                que.append([nx, ny, flag])

            elif board[nx][ny] == 1 and flag == 0:
                visited[nx][ny][flag + 1] = visited[x][y][flag] + 1
                que.append([nx, ny, flag + 1])

print(-1)
