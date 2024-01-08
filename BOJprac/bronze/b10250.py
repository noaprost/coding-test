# ACM 호텔
import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    h, w, n = map(int, sys.stdin.readline().split())

    y = n % h * 100
    x = n // h + 1

    if y == 0:
        y = h * 100
        x -= 1

    print(y + x)
