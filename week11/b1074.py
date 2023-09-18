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

    if r < x + int(pow(2, n) / 2) and c < y + int(pow(2, n) / 2):
        divAndCon(x, y, n - 1)
    elif r < x + int(pow(2, n) / 2) and c >= y + int(pow(2, n) / 2):
        count += int(pow(2, n) / 2) * int(pow(2, n) / 2)
        divAndCon(x, y + int(pow(2, n) / 2), n - 1)
    elif r >= x + int(pow(2, n) / 2) and c < y + int(pow(2, n) / 2):
        count += int(pow(2, n) / 2) * int(pow(2, n) / 2) * 2
        divAndCon(x + int(pow(2, n) / 2), y, n - 1)
    elif r >= x + int(pow(2, n) / 2) and c >= y + int(pow(2, n) / 2):
        count += int(pow(2, n) / 2) * int(pow(2, n) / 2) * 3
        divAndCon(x + int(pow(2, n) / 2), y + int(pow(2, n) / 2), n - 1)


count = 0
divAndCon(0, 0, n)
