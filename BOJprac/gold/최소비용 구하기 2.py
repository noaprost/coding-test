# 11779
import sys
import heapq

INF = int(1e8)


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while len(heap) != 0:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            newdist = dist + i[1]
            if newdist < distance[i[0]]:
                distance[i[0]] = newdist
                prev_node[i[0]] = now
                heapq.heappush(heap, (distance[i[0]], i[0]))


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

distance = [INF] * (n + 1)
prev_node = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

s, e = map(int, sys.stdin.readline().split())

dijkstra(s)
print(distance[e])

path = [e]
now = e
while now != s:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(*path)
