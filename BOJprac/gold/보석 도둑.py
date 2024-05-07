# 1202
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
ju = []
bag = []

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    ju.append((m, v))

for _ in range(k):
    b = int(sys.stdin.readline())
    bag.append(b)

bag.sort()
ju.sort()

ans = 0
heap = []

for b in bag:
    while ju and ju[0][0] <= b:
        heapq.heappush(heap, -ju[0][1])
        heapq.heappop(ju)
    if heap:
        ans -= heapq.heappop(heap)

print(ans)
