import sys
from queue import Queue

n, m = map(int, sys.stdin.readline().split())

edges = [[] + [] for _ in range(n + 1)]

visited = []
visited.append(True)
for _ in range(n):
    visited.append(False)

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    edges[s].append(e)
    edges[e].append(s)

que = Queue()

total = 0

while False in visited:
    que.put(visited.index(False))

    while que.qsize() != 0:
        v = que.get()
        visited[v] = True

        for i in edges[v]:
            if not visited[i]:
                visited[i] = True
                que.put(i)
    total += 1

print(total)
