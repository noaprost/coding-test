# 1520
import sys

m, n = map(int, sys.stdin.readline().split())

maps = []

for _ in range(m):
    maps.append(list(map(int, sys.stdin.readline().split())))

# 주변에 있는 애들을 어떻게 넣지


def dfs(graph, node, visited):

    for i in graph:
        visited[i] = True
        dfs(graph, i, visited)
        visited[i] = False


# dfs
# 방문하고나서 방문처리를 풀어줘야 모든 경로를 찾을 수 있음
