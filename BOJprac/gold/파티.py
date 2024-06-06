# 1238
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


n, m, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((c, e))

ans = []

for i in range(1, n + 1):
    goDist = dijkstra(i)
    aliveDist = dijkstra(x)
    ans.append(goDist[x] + aliveDist[i])

print(max(ans))
