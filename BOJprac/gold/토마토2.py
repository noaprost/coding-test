# 7569
import sys
from queue import Queue

m, n, h = map(int, sys.stdin.readline().split())

tomato = []
visited = [[False for _ in range(m)] for _ in range(n * h)]

for i in range(n * h):
    tomato.append(list(map(int, sys.stdin.readline().split())))

x, y = 0, 0
que = Queue()
count = 0

for r in range(n * h):
    if 1 in tomato[r]:
        c = tomato[r].index(1)
        x, y = r, c
        que.put([x, y])
        visited[x][y] = True

while que.qsize() != 0:
    v = que.get()
    x = v[0]
    y = v[1]
    count += 1

    # 상하좌우앞뒤를 인접노드로 넣어줌

    # 상
    if x > 0 and not visited[x - 1][y] and tomato[x - 1][y] == 0:
        tomato[x - 1][y] = 1
        que.put([x - 1, y])
        visited[x - 1][y] = True

    # 하
    if x < n * h - 1 and not visited[x + 1][y] and tomato[x + 1][y] == 0:
        tomato[x + 1][y] = 1
        que.put([x + 1, y])
        visited[x + 1][y] = True

    # 좌
    if y > 0 and not visited[x][y - 1] and tomato[x][y - 1] == 0:
        tomato[x][y - 1] = 1
        que.put([x, y - 1])
        visited[x][y - 1] = True

    # 우
    if y < m - 1 and not visited[x][y + 1] and tomato[x][y + 1] == 0:
        tomato[x][y + 1] = 1
        que.put([x, y + 1])
        visited[x][y + 1] = True

    # 앞
    if x + h < n * h and not visited[x + h][y] and tomato[x + h][y] == 0:
        tomato[x + h][y] = 1
        que.put([x + h, y])
        visited[x + h][y] = True

    # 뒤
    if x - h >= 0 and not visited[x - h][y] and tomato[x - h][y] == 0:
        tomato[x - h][y] = 1
        que.put([x - h, y])
        visited[x - h][y] = True

    for t in tomato:
        print(t)

    for v in visited:
        print(v)


# print(x, y)
print(count)
