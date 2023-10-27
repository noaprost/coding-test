# 뱀
import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [[0 for _ in range(n)] for _ in range(n)]

directions = ["T", "R", "B", "L"]
snakeDirec = directions[1]

appleLoc = int(sys.stdin.readline())

# 사과의 위치 표시
for _ in range(appleLoc):
    x, y = map(int, sys.stdin.readline().split())
    maps[x - 1][y - 1] = 4

l = int(sys.stdin.readline())

d = deque()
d.append([0, 0])
maps[0][0] = 1
i = 1

command = []

for _ in range(l):
    val, rotate = sys.stdin.readline().split()
    command.append([val, rotate])

command.append([10001, command[l - 1][1]])

for c in command:
    val, rotate = c[0], c[1]
    while i < int(val):
        for m in maps:
            print(m)
        print()
        x = d[0][0]
        y = d[0][1]
        if snakeDirec == "R":
            i += 1
            if y > n - 1:  # 경계를 벗어날 경우
                exit(print(i))
            elif maps[x][y + 1] == 1:  # 자기 몸에 닿은 경우
                exit(print(i))
            else:  # 경계에 닿지 않은 경우
                if maps[x][y + 1] == 4:
                    d.appendleft([x, y + 1])
                    maps[x][y + 1] = 1
                else:
                    d.appendleft([x, y + 1])
                    maps[x][y + 1] = 1
                    v = d.pop()
                    maps[v[0]][v[1]] = 0

        elif snakeDirec == "B":
            i += 1
            if x + 1 > n - 1:  # 경계를 벗어날 경우
                exit(print(i))
            elif maps[x + 1][y] == 1:  # 자기 몸에 닿은 경우
                exit(print(i))
            else:  # 경계에 닿지 않은 경우
                if maps[x + 1][y] == 4:
                    d.appendleft([x + 1, y])
                    maps[x + 1][y] = 1
                else:
                    d.appendleft([x + 1, y])
                    maps[x + 1][y] = 1
                    v = d.pop()
                    maps[v[0]][v[1]] = 0

        elif snakeDirec == "L":
            i += 1
            if y < 0:  # 경계를 벗어날 경우
                exit(print(i))
            elif maps[x][y - 1] == 1:  # 자기 몸에 닿은 경우
                exit(print(i))
            else:  # 경계에 닿지 않은 경우
                if maps[x][y - 1] == 4:
                    d.appendleft([x, y - 1])
                    maps[x][y - 1] = 1
                else:
                    d.appendleft([x, y - 1])
                    maps[x][y - 1] = 1
                    v = d.pop()
                    maps[v[0]][v[1]] = 0

        elif snakeDirec == "T":
            i += 1
            if x < 0:  # 경계를 벗어날 경우
                exit(print(i))
            elif maps[x - 1][y] == 1:  # 자기 몸에 닿은 경우
                exit(print(i))
            else:  # 경계에 닿지 않은 경우
                if maps[x - 1][y] == 4:
                    d.appendleft([x - 1, y])
                    maps[x - 1][y] = 1
                else:
                    d.appendleft([x - 1, y])
                    maps[x - 1][y] = 1
                    v = d.pop()
                    maps[v[0]][v[1]] = 0

    if rotate == "D":
        snakeDirec = directions[(directions.index(snakeDirec) + 1) % 4]
    elif rotate == "L":
        didx = directions.index(snakeDirec)
        if didx == 0:
            snakeDirec = directions[3]
        else:
            snakeDirec = directions[didx - 1]
print(i)
