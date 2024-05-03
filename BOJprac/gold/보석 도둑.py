# 1202
import sys
from queue import PriorityQueue

n, k = map(int, sys.stdin.readline().split())
ju = []
bag = []
visited = [False for _ in range(k)]

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())

    ju.append([-v, m])

ju.sort()

for _ in range(k):
    b = int(sys.stdin.readline())
    bag.append(b)

bag.sort()

ans = 0

i = 0
while i < n:
    w = ju[i]
    v, m = w[0], w[1]
    for j in range(k):
        if not visited[j] and bag[j] >= m:
            ans -= v
            visited[j] = True
            break
    i += 1

print(ans)
