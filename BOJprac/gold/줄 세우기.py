# 2252
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

degree = [1e8] + [0 for _ in range(n)]
dq = deque()
graph = [[] for _ in range(n + 1)]
ans = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        dq.append(i)
        ans.append(i)

while dq:
    v = dq.popleft()

    for g in graph[v]:
        degree[g] -= 1

        if degree[g] == 0:
            dq.append(g)
            ans.append(g)

print(*ans)
