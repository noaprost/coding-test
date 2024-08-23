# 3190
import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [[0 for _ in range(n)] for _ in range(n)]
apple_num = int(sys.stdin.readline())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 사과
for _ in range(apple_num):
    x, y = map(int, sys.stdin.readline().split())
    maps[x - 1][y - 1] = 2

l = int(sys.stdin.readline())
directions = dict()
x, y = 0, 0
que = deque()
que.append((x, y))
maps[x][y] = 1
count = 0
direction = 0

# 방향
for _ in range(l):
    val, rotate = sys.stdin.readline().rstrip().split()
    directions[int(val)] = rotate


def turn(d):
    global direction
    if d == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    count += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if maps[x][y] == 2:
        maps[x][y] = 1
        que.append((x, y))

        if count in directions:
            turn(directions[count])

    elif maps[x][y] == 0:
        maps[x][y] = 1
        que.append((x, y))
        tx, ty = que.popleft()
        maps[tx][ty] = 0

        if count in directions:
            turn(directions[count])
    else:
        break

print(count)
