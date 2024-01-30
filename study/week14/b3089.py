# 네잎 클로버를 찾아서
import sys

cloverNum, commandNum = map(int, sys.stdin.readline().split())

clover = [[] for _ in range(200000)]

# 숭이 초기 위치
sx, sy = 0, 0

# tblr
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction = ["R", "D", "L", "U"]

for i in range(cloverNum):
    x, y = map(int, sys.stdin.readline().split())
    clover[x].append(y)


command = list(sys.stdin.readline().strip())

for c in command:
    idx = direction.index(c)
    nx = sx
    ny = sy
    while True:
        nx = nx + dx[idx]
        ny = ny + dy[idx]

        if ny in clover[nx]:
            break

    sx, sy = nx, ny

print(sx, sy)
