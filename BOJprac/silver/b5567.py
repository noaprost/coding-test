# 결혼삭
import sys
from queue import Queue

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

visited = [False for _ in range(n + 1)]

graph = [[] for _ in range(n + 1)]

que = Queue()

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

count = 0

if len(graph[1]) == 0:
    exit(print(0))
else:
    visited[1] = True
    for g in graph[1]:
        que.put(g)
        visited[g] = True
        count += 1

while que.qsize() != 0:
    v = que.get()
    visited[v] = True
    for g in graph[v]:
        if not visited[g]:
            visited[g] = True
            count += 1

print(count)
