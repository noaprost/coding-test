import sys
from queue import Queue


def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=" ")

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, node, visited):
    que = Queue()
    visited[node] = True
    que.put(node)

    while que.qsize() != 0:
        v = que.get()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                que.put(i)
                visited[i] = True


vertexNum, edgeNum, v = map(int, sys.stdin.readline().split())
graph = [[] + [] for _ in range(vertexNum + 1)]
visited = [False for _ in range(vertexNum + 1)]

for i in range(1, edgeNum + 1):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for g in graph:
    g.sort()

dfs(graph, v, visited)
print()

visited = [False for _ in range(vertexNum + 1)]
bfs(graph, v, visited)
