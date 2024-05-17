# 11000
import sys
import heapq

n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    meeting.append((a, b))

meeting.sort(key=lambda x: (x[0], x[1]))

h = [meeting[0][1]]
for i in range(1, n):
    if h[0] <= meeting[i][0]:
        heapq.heappop(h)
    heapq.heappush(h, meeting[i][1])

print(len(h))
