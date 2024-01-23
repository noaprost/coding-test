# 다리 놓기
import sys
from itertools import combinations

caseNum = int(sys.stdin.readline())

sum = 1

for _ in range(caseNum):
    a, b = map(int, sys.stdin.readline().split())

    if b - a == 0:
        print(1)
    else:
        for i in range(b, b - a, -1):
            sum *= i

        print(sum)
