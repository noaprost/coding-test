# 1504
import sys
import heapq


def dijkstra(start):
    dist = [1e8 for _ in range(n + 1)]
    que = []
    heapq.heappush(que, (0, start))
    dist[start] = 0

    while que:
        v = heapq.heappop(que)
        curDist = v[0]
        curNode = v[1]

        if dist[curNode] < curDist:
            continue

        for nextDist, nextNode in graph[curNode]:
            cost = curDist + nextDist

            if cost < dist[nextNode]:
                dist[nextNode] = cost
                heapq.heappush(que, (cost, nextNode))

    return dist


n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))

v1, v2 = map(int, sys.stdin.readline().split())

fullDist = dijkstra(1)
v1Dist = dijkstra(v1)
v2Dist = dijkstra(v2)

first = fullDist[v1] + v1Dist[v2] + v2Dist[n]  # 1 -> v1 -> v2 -> n
second = fullDist[v2] + v2Dist[v1] + v1Dist[n]  # 1 -> v2 -> v1 -> n

ans = min(first, second)

if ans >= 1e8:
    print(-1)
else:
    print(ans)
