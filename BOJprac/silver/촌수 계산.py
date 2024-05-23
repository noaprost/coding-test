import sys


def dfs(node, visited, cost):
    visited[node] = True

    if node == e:
        exit(print(cost))

    for g in graph[node]:
        if not visited[g]:
            dfs(g, visited, cost + 1)


p = int(sys.stdin.readline())
s, e = map(int, sys.stdin.readline().split())
edgeNum = int(sys.stdin.readline())
graph = [[] for _ in range(p + 1)]

for _ in range(edgeNum):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(p + 1)]
count = 0

dfs(s, visited, count)
print(-1)
