# 1005
import sys
from collections import deque

input = sys.stdin.readline

cn = int(input())

# 위상 정렬을 해두고 그다음에 그 순서대로 따라가면서 시간 구해야되는 문제인듯 하다

for _ in range(cn):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    degree = [1e8] + [0 for _ in range(n)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        degree[y] += 1
    w = int(input())
    dq = deque()
    ans = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if degree[i] == 0:
            dq.append(i)
            ans[i] = d[i]

    while dq:
        v = dq.popleft()

        if v == w:
            break

        for g in graph[v]:
            degree[g] -= 1
            ans[g] = max(ans[v] + d[g], ans[g])
            if degree[g] == 0:
                dq.append(g)

    print(ans[w])
