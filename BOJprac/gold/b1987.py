# 알파벳
import sys
from queue import Queue

h, w = map(int, sys.stdin.readline().split())

maps = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]

alph = [maps[0][0]]

que = Queue()

que.put([0, 0])

distance = 1

while que.qsize() != 0:
    v = que.get()
    x = v[0]
    y = v[1]
    print(alph)
    if y > 0 and not visited[y - 1][x] and (maps[y - 1][x] not in alph):
        que.put([x, y - 1])
        visited[y - 1][x] = True
        alph.append(maps[y - 1][x])
        distance += 1

    if y < h - 1 and not visited[y + 1][x] and (maps[y + 1][x] not in alph):
        que.put([x, y + 1])
        visited[y + 1][x] = True
        alph.append(maps[y + 1][x])
        distance += 1

    if x < w - 1 and not visited[y][x + 1] and (maps[y][x + 1] not in alph):
        que.put([x + 1, y])
        visited[y][x + 1] = True
        alph.append(maps[y][x + 1])
        distance += 1

    if x > 0 and not visited[y][x - 1] and (maps[y][x - 1] not in alph):
        que.put([x - 1, y])
        visited[y][x - 1] = True
        alph.append(maps[y][x - 1])
        distance += 1


print(distance)
