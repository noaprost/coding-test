# 숨바꼭질3
# 0-1 bfs
import sys
from collections import deque

INF = 1e8
start, end = map(int, sys.stdin.readline().split())
dq = deque()
dist = [INF for _ in range(100001)]

dq.append(start)
dist[start] = 0

while dq:
    v = dq.popleft()

    if v == end:
        exit(print(dist[end]))

    if v * 2 <= 100000 and dist[v] + 0 < dist[v * 2]:
        dist[v * 2] = dist[v] + 0
        dq.appendleft(v * 2)

    if 0 <= v - 1 and dist[v] + 1 < dist[v - 1]:
        dist[v - 1] = dist[v] + 1
        dq.append(v - 1)

    if v + 1 <= 100000 and dist[v] + 1 < dist[v + 1]:
        dist[v + 1] = dist[v] + 1
        dq.append(v + 1)
