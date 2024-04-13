import sys

n = int(sys.stdin.readline())

xy = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xy.append([x, y])

xy.sort()

for a in xy:
    print(a[0], a[1])
