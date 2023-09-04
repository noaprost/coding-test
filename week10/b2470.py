# 두 용액

import sys

n = int(sys.stdin.readline())

numList = list(map(int, sys.stdin.readline().split()))
numList.sort()

start = 0
end = n - 1

cur = numList[start] + numList[end]  # 최근 차이

idx1 = start
idx2 = end

while start < end:
    s = numList[start] + numList[end]
    if abs(cur) > abs(s):
        cur = s
        idx1 = start
        idx2 = end

    if s > 0:
        end = end - 1
    elif s < 0:
        start = start + 1
    else:
        idx1 = start
        idx2 = end
        break

print(numList[idx1], numList[idx2])
