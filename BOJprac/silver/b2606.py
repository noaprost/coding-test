import sys

n = int(sys.stdin.readline())

connect = int(sys.stdin.readline())

count = -1  # 1번 노드는 count에서 제외

# 노드번호와 인덱스를 맞추기 위해 n+1 크기로 선언해줌
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(connect):
    idx, adj = map(int, sys.stdin.readline().split())
    graph[idx].append(adj)
    graph[adj].append(idx)


def dfs(graph, node, visited):
    global count
    # 해당 노드 방문 처리
    visited[node] = True
    count += 1

    # 한 노드로부터 인접한 노드를 재귀적으로 방문 처리
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(count)
