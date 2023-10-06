import sys
from queue import Queue

n, m = map(int, sys.stdin.readline().split())

maze = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
count = [[0 for _ in range(m)] for _ in range(n)]

x, y = 0, 0

que = Queue()
que.put([x, y])

count[0][0] = 1


while que.qsize() != 0:
    v = que.get()
    x = v[0]
    y = v[1]

    visited[x][y] = True

    if x == n - 1 and y == m - 1:
        exit(print(count[n - 1][m - 1]))

    if (x < n - 1) and (not visited[x + 1][y]) and (maze[x + 1][y] == "1"):
        que.put([x + 1, y])
        visited[x + 1][y] = True
        count[x + 1][y] += count[x][y] + 1

    if y < m - 1 and not visited[x][y + 1] and maze[x][y + 1] == "1":
        que.put([x, y + 1])
        visited[x][y + 1] = True
        count[x][y + 1] += count[x][y] + 1

    if x > 0 and not visited[x - 1][y] and maze[x - 1][y] == "1":
        que.put([x - 1, y])
        visited[x - 1][y] = True
        count[x - 1][y] += count[x][y] + 1

    if y > 0 and not visited[x][y - 1] and maze[x][y - 1] == "1":
        que.put([x, y - 1])
        visited[x][y - 1] = True
        count[x][y - 1] += count[x][y] + 1
