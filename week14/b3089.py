# 네잎 클로버를 찾아서
import sys

cloverNum, commandNum = map(int, sys.stdin.readline().split())
clover1 = []
clover2 = []
clover3 = []
clover4 = []

# 숭이 초기 위치
sx, sy = 0, 0

# tblr
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction = ["R", "D", "L", "U"]

for i in range(cloverNum):
    x, y = map(int, sys.stdin.readline().split())
    if x >= 0 and y >= 0:
        clover1.append([x, y])
    elif x >= 0 and y <= 0:
        clover2.append([x, y])
    elif x < 0 and y <= 0:
        clover3.append([x, y])
    elif x <= 0 and y >= 0:
        clover4.append([x, y])

command = list(sys.stdin.readline().strip())

for c in command:
    idx = direction.index(c)
    nx = sx
    ny = sy
    while True:
        nx = nx + dx[idx]
        ny = ny + dy[idx]

        if nx >= 0 and ny >= 0:
            if [nx, ny] in clover1:
                break
        elif nx >= 0 and ny <= 0:
            if [nx, ny] in clover2:
                break
        elif nx <= 0 and ny <= 0:
            if [nx, ny] in clover3:
                break
        elif nx <= 0 and ny >= 0:
            if [nx, ny] in clover4:
                break

    sx, sy = nx, ny

print(sx, sy)
