# 1446
import sys
import heapq

n, d = map(int, sys.stdin.readline().split())
dist = [1e8 for _ in range(d + 1)]
graph = [[] for _ in range(d + 1)]
heap = []
heapq.heappush(heap, (0, 0))
dist[0] = 0

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    s, e, distance = map(int, sys.stdin.readline().split())
    if e > d:
        continue
    graph[s].append((e, distance))

while heap:
    cost, x = heapq.heappop(heap)

    if cost > dist[x]:
        continue

    for g in graph[x]:
        if cost + g[1] < dist[g[0]]:
            dist[g[0]] = cost + g[1]
            heapq.heappush(heap, (dist[g[0]], g[0]))

print(dist[d])
