# 1987
import sys
from queue import Queue

h, w = map(int, sys.stdin.readline().split())

maps = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]

alph = []

stack = []

stack.append([0, 0])

distance = 0

while len(stack) != 0:
    v = stack.pop()
    x = v[0]
    y = v[1]
    if maps[y][x] not in alph:
        visited[y][x] = True
        alph.append(maps[y][x])
    else:
        continue

    if y > 0 and not visited[y - 1][x] and (maps[y - 1][x] not in alph):
        stack.append([x, y - 1])

    if y < h - 1 and not visited[y + 1][x] and (maps[y + 1][x] not in alph):
        stack.append([x, y + 1])

    if x < w - 1 and not visited[y][x + 1] and (maps[y][x + 1] not in alph):
        stack.append([x + 1, y])

    if x > 0 and not visited[y][x - 1] and (maps[y][x - 1] not in alph):
        stack.append([x - 1, y])

    distance += 1

for v in visited:
    print(v)
print(distance)
