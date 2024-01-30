# 17298
import sys
import heapq

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
ans = [-1] * n
h = []

for i in range(n):
    while len(h) > 0:
        if nums[i] > h[0][0]:
            ans[h[0][1]] = nums[i]
            heapq.heappop(h)
        else:
            break
    heapq.heappush(h, (nums[i], i))

print(*ans)
