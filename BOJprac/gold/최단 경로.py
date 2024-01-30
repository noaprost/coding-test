# 1753
import sys
import heapq

vertexNum, edgeNUm = map(int, sys.stdin.readline().split())

k = int(sys.stdin.readline())

graph = [[] for _ in range(vertexNum + 1)]
for i in range(edgeNUm):
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u].append((v, w))

INF = 1e8

distance = [INF] * (vertexNum + 1)


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(que, (distance[i[0]], i[0]))


dijkstra(k)

for i in range(1, len(distance)):
    if distance[i] == 100000000.0:
        print("INF")
    else:
        print(distance[i])
