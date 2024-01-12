# 더하기 사이클
import sys

n = int(sys.stdin.readline())

cycle = 0

tmp = n

while True:
    cycle += 1
    if tmp < 10:
        a = 0
        b = tmp
    else:
        a = tmp // 10
        b = tmp % 10

    newNum = b * 10 + (a + b) % 10

    if newNum == n:
        exit(print(cycle))

    tmp = newNum
