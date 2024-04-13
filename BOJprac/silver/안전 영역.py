import sys
from queue import Queue


def isVisit(visited):
    i = 0
    for v in visited:
        if False in v:
            y = v.index(False)
            x = i
            return x, y
        i += 1
    return -1, -1


n = int(sys.stdin.readline())

maps = []
visited = [[False for _ in range(n)] for _ in range(n)]
safeArea = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

sa = -1
water = 0
while sa != 0:
    sa = 0
    que = Queue()
    # 물에 잠김 표시
    for i in range(n):
        for j in range(n):
            if maps[i][j] <= water:
                visited[i][j] = True

    x, y = isVisit(visited)

    while x != -1:
        que.put([x, y])

        while que.qsize() != 0:
            v = que.get()
            x = v[0]
            y = v[1]

            visited[x][y] = True

            if x > 0 and not visited[x - 1][y]:
                que.put([x - 1, y])
                visited[x - 1][y] = True

            if x < n - 1 and not visited[x + 1][y]:
                que.put([x + 1, y])
                visited[x + 1][y] = True

            if y > 0 and not visited[x][y - 1]:
                que.put([x, y - 1])
                visited[x][y - 1] = True

            if y < n - 1 and not visited[x][y + 1]:
                que.put([x, y + 1])
                visited[x][y + 1] = True

        sa += 1
        x, y = isVisit(visited)

    safeArea.append(sa)
    water += 1
    visited = [[False for _ in range(n)] for _ in range(n)]

print(max(safeArea))
