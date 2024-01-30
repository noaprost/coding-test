# 신입사원
import sys

t = int(sys.stdin.readline())

while t != 0:
    count = 1
    result = []

    n = int(sys.stdin.readline())

    for _ in range(n):
        doc, itv = map(int, sys.stdin.readline().split())
        result.append([doc, itv])

    result.sort()

    itvRank = result[0][1]
    for i in range(1, n):
        if result[i][1] < itvRank:
            count += 1
            itvRank = result[i][1]

    print(count)
    t -= 1
