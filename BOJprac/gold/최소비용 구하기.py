# 1916
import sys
import heapq

INF = int(1e8)


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while len(hq) != 0:
        dist, now = heapq.heappop(hq)

        # 저장되어있는 것보다 길이가 길다면 볼 것도 없음
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 간선을 하나씩 탐색
        for i in graph[now]:
            newdist = dist + i[1]
            if newdist < distance[i[0]]:
                distance[i[0]] = newdist
                heapq.heappush(hq, (distance[i[0]], i[0]))


n = int(sys.stdin.readline())  # 정점 개수
m = int(sys.stdin.readline())  # 간선 개수

# 시작 노드가 어딘지에 따라 그 노드부터 다른 모든 노드까지의 거리를 저장
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

s, e = map(int, sys.stdin.readline().split())

dijkstra(s)

print(distance[e])
