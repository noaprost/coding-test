# 좋다

import sys

n = int(sys.stdin.readline())

numList = list(map(int, sys.stdin.readline().split()))
numList.sort()

goodCount = 0

for i in range(n):
    idx1 = 0
    idx2 = n - 1

    while True:
        if idx1 == i:
            idx1 = idx1 + 1

        if idx2 == i:
            idx2 = idx2 - 1

        sum = numList[idx1] + numList[idx2]

        if idx1 >= idx2:
            break

        if sum > numList[i]:
            idx2 = idx2 - 1
        elif sum < numList[i]:
            idx1 = idx1 + 1
        else:
            goodCount = goodCount + 1
            break

print(goodCount)
