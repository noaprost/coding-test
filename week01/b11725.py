import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

graph = [[] + [] for _ in range(n + 1)]

visited = [False + False for _ in range(n + 1)]

parent = [0 + 0 for _ in range(n + 1)]

for i in range(1, n):
    s, e = map(int, sys.stdin.readline().split())

    graph[s].append(e)
    graph[e].append(s)


def dfs(graph, node, visited):
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            visited[i] = True
            dfs(graph, i, visited)


dfs(graph, 1, visited)

for i in range(2, n + 1):
    print(parent[i])
