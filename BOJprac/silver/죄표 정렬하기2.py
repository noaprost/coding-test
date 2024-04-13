import sys

n = int(sys.stdin.readline())

yx = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    yx.append([y, x])

yx.sort()

for a in yx:
    print(a[1], a[0])
