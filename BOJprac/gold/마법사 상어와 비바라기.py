# 21610
import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
moves = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

dy8 = ("empty", 0, -1, -1, -1, 0, 1, 1, 1)
dx8 = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)

dy4 = (-1, -1, 1, 1)
dx4 = (-1, 1, -1, 1)

clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for d, s in moves:
    moved_clouds = []
    for y, x in clouds:
        ny = (y + dy8[d] * s) % n
        nx = (x + dx8[d] * s) % n
        board[ny][nx] += 1
        moved_clouds.append((ny, nx))

    for y, x in moved_clouds:
        count = 0
        for d in range(4):
            ny = y + dy4[d]
            nx = x + dx4[d]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            elif board[ny][nx] > 0:
                count += 1
        board[y][x] += count

    new_clouds = []

    for y in range(n):
        for x in range(n):
            if (y, x) in moved_clouds or board[y][x] < 2:
                continue
            board[y][x] -= 2
            new_clouds.append((y, x))
    clouds = new_clouds

result = 0

for y in range(n):
    for x in range(n):
        result += board[y][x]

print(result)
