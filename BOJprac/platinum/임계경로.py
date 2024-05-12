# 1948
import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
degree = [1e8] + [0 for _ in range(n)]
dq = deque()
dp = [0 for _ in range(n + 1)]
dist = [[] for _ in range(n + 1)]

for i in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w, i))
    degree[e] += 1

s, e = map(int, sys.stdin.readline().split())

dq.append(s)

while dq:
    v = dq.popleft()

    if v == e:
        break

    for g in graph[v]:
        degree[g[0]] -= 1

        if dp[v] + g[1] > dp[g[0]]:
            dist[g[0]] = [(g[2], v)]
            dp[g[0]] = dp[v] + g[1]

        elif dp[v] + g[1] == dp[g[0]]:
            dist[g[0]].append((g[2], v))

        if degree[g[0]] == 0:
            dq.append(g[0])

ans = set()
que = deque()
visited = [False for _ in range(m)]
for s in dist[e]:
    que.append(s)
    visited[s[0]] = True

while que:
    bri, pre = que.popleft()
    ans.add(bri)

    for d in dist[pre]:
        if not visited[d[0]]:
            que.append(d)
            visited[d[0]] = True

print(dp[e])
print(len(ans))