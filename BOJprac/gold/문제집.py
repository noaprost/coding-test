# 1766
import sys
from queue import PriorityQueue

n, c = map(int, sys.stdin.readline().split())

quest = [[] for _ in range(n + 1)]
degree = [1e8] + [0 for _ in range(n)]

for _ in range(c):
    a, b = map(int, sys.stdin.readline().split())

    quest[a].append(b)
    degree[b] += 1

que = PriorityQueue()

for i in range(1, n+1):
    if(degree[i] == 0):
        que.put(i)

ans = []

while que.qsize() != 0:
    v = que.get()
    ans.append(v)

    for g in quest[v]:
        degree[g] -= 1
        if(degree[g] == 0):
            que.put(g)

print(*ans)