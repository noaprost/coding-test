# 11657
import sys

INF = int(1e9)

v_num, e_num = map(int, sys.stdin.readline().split())
dist = [INF] * (v_num + 1)

edges = []
for _ in range(e_num):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))


def bellman_ford(start):
    dist[start] = 0

    for i in range(v_num):
        for j in range(e_num):
            s, e, c = edges[j][0], edges[j][1], edges[j][2]

            if dist[s] != INF and dist[e] > dist[s] + c:
                dist[e] = dist[s] + c
                if i == v_num - 1:
                    return True
    return False


isCycle = bellman_ford(1)

if isCycle:
    print(-1)
else:
    for i in range(2, v_num + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
