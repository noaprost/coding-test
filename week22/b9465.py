# 스티커
import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    n = int(sys.stdin.readline())

    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    ans = 0

    