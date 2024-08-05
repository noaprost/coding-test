# 13913
import sys
from collections import deque

su, bro = map(int, sys.stdin.readline().split())
dist = [0 for _ in range(100001)]
path = [0 for _ in range(100001)]
que = deque()

que.append(su)

while que:
    v = que.popleft()

    if v == bro:
        print(dist[v])
        break

    for i in (v + 1, v - 1, 2 * v):
        if 0 <= i <= 100000 and dist[i] == 0:
            dist[i] = dist[v] + 1
            que.append(i)
            path[i] = v

prev_node = [bro]
now = bro
while now != su:
    now = path[now]
    prev_node.append(now)

prev_node.reverse()

print(*prev_node)
