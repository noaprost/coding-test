# 30685
import sys

n = int(sys.stdin.readline())
l = [None for _ in range(n)]

for i in range(n):
    x, h = map(int, sys.stdin.readline().split())
    l[i] = (x, h)

l.sort()
small = 1000000000

for i in range(n - 1):
    t = l[i][1] // 2 + l[i + 1][1] // 2
    dif = l[i + 1][0] - l[i][0]
    if t < dif:
        continue
    time = 0
    if (dif - 1) / 2 <= l[i][1] // 2 and (dif - 1) / 2 <= l[i + 1][1] // 2:
        time = (dif - 1) // 2
    elif (dif - 1) / 2 > l[i][1] // 2:
        time = dif - 1 - l[i][1] // 2
    else:
        time = dif - 1 - l[i + 1][1] // 2
    small = small if small < time else time


if small == 1000000000:
    print("forever")
else:
    print(small)
