# 1011
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    dis = y - x
    count = 0
    move = 1
    total = 0
    while total < dis:
        count += 1
        total += move
        if count % 2 == 0:
            move += 1
    print(count)
