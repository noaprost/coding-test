import sys
from queue import Queue

p = int(sys.stdin.readline())

s, e = map(int, sys.stdin.readline().split())

edgeNum = int(sys.stdin.readline())

graph = [[] + [] for _ in range(p + 1)]

for _ in range(edgeNum):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

que = Queue()
que.put(s)
visited = [False + False for _ in range(p + 1)]
count = 0

while que.qsize() != 0:
    node = que.get()
    visited[node] = True

    if e in graph[node]:
        exit(print(count))

    for i in graph[node]:
        if not visited[i]:
            count += 1
            que.put(i)
print(-1)
