import sys

n = int(sys.stdin.readline())

maps = []

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

maps.reverse()

for i in range(n - 1):
    for j in range(len(maps[i]) - 1):
        maps[i + 1][j] += max(maps[i][j], maps[i][j + 1])

print(maps[-1][0])
