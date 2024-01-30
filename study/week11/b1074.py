# Z
# 별찍기처럼 재귀로 반복하니까 시간초과..
# 전수탐색이 아닌 범위를 좁혀가면서 찾아야 하는 문제 인듯

import sys

n, r, c = map(int, sys.stdin.readline().split())
check = False


def divAndCon(x, y, n):
    global count
    if n == 0:
        exit(print(count))

    length = int(pow(2, n) / 2)

    if r < x + length and c < y + length:
        divAndCon(x, y, n - 1)
    elif r < x + length and c >= y + length:
        count += pow(length, 2)
        divAndCon(x, y + length, n - 1)
    elif r >= x + length and c < y + length:
        count += pow(length, 2) * 2
        divAndCon(x + length, y, n - 1)
    elif r >= x + length and c >= y + length:
        count += pow(length, 2) * 3
        divAndCon(x + length, y + length, n - 1)


count = 0
divAndCon(0, 0, n)
