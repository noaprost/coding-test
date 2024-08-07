# 1976
import sys
from collections import deque


def bfs(s, e):
    que = deque()
    que.append(s)
    visited = [False for _ in range(n)]
    visited[s] = True

    while que:
        v = que.popleft()

        if v == e:
            return True

        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                que.append(i)
                visited[i] = True

    return False


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

cityPlan = list(map(int, sys.stdin.readline().split()))

for i in range(m - 1):
    if cityPlan[i] != cityPlan[i + 1]:
        if not bfs(cityPlan[i] - 1, cityPlan[i + 1] - 1):
            exit(print("NO"))

print("YES")
