import sys
import heapq

n = int(sys.stdin.readline())

h = []

for _ in range(n):
    com = int(sys.stdin.readline())
    if com == 0:
        if len(h) == 0:
            print(0)
        else:
            v = heapq.heappop(h)
            print(v[1])
    else:
        heapq.heappush(h, (abs(com), com))
