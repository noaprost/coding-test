# 13975
import heapq
import sys

caseNum = int(sys.stdin.readline())
for _ in range(caseNum):
    n = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(files)
    ans = 0

    while len(files) > 1:
        tmp = 0
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        tmp += a + b
        ans += tmp
        heapq.heappush(files, tmp)

    print(ans)
