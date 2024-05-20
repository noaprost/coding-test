import sys

n = int(sys.stdin.readline())

maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if maps[i][j] == 0:
            maps[i][j] = 1e8

for k in range(n):
    for i in range(n):
        for j in range(n):
            if maps[i][k] + maps[k][j] < maps[i][j]:
                maps[i][j] = maps[i][k] + maps[k][j]
                
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1e8:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
