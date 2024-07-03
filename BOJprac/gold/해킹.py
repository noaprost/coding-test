# 10282
import sys
import heapq


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, v = heapq.heappop(heap)
        visited[v] = True

        for g in graph[v]:
            if cost + g[1] < time[g[0]]:
                time[g[0]] = cost + g[1]
                heapq.heappush(heap, (time[g[0]], g[0]))


caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    n, d, c = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    time = [1e8 for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))

    dijkstra(c)

    t = []
    for i in range(n, 0, -1):
        if time[i] != 1e8:
            t.append(time[i])

    if len(t) == 0:
        print(visited.count(True), 0)
    else:
        print(visited.count(True), max(t))
