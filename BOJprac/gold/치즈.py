# 2638
import sys
from queue import Queue

n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
que = Queue()
fade = []
hours = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def countOutsideAir(x, y):
    count = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and cheese[nx][ny] == 2:
            count += 1

    return count


def markToOutsideAir():
    tmp_que = Queue()

    tmp_que.put([0, 0])
    tmp_visted = [[False for _ in range(m)] for _ in range(n)]

    while tmp_que.qsize() != 0:
        x, y = tmp_que.get()
        tmp_visted[x][y] = True

        if cheese[x][y] != 1:
            cheese[x][y] = 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not tmp_visted[nx][ny]:
                if cheese[nx][ny] == 0 or cheese[nx][ny] == 2:
                    tmp_visted[nx][ny] = True
                    cheese[nx][ny] = 2
                    tmp_que.put([nx, ny])
                elif cheese[nx][ny] == 1:
                    tmp_visted[nx][ny] = True


que.put([0, 0])

while True:
    fade = []
    while que.qsize() != 0:
        x, y = que.get()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= y < m - 1 and not visited[nx][ny]:
                if cheese[nx][ny] == 1 and countOutsideAir(nx, ny) > 1:
                    fade.append([nx, ny])
                    visited[nx][ny] = True
                elif cheese[nx][ny] != 1:
                    que.put([nx, ny])
                    visited[nx][ny] = True

    if len(fade) != 0:
        for f in fade:
            que.put(f)
            cheese[f[0]][f[1]] = 2
        hours += 1
        markToOutsideAir()
    else:
        exit(print(hours))

    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                visited[i][j] = False
