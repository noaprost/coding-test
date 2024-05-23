import sys

n, m = map(int, sys.stdin.readline().split())
cost = [[1e8 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            cost[i][j] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    cost[a][b] = 1
    cost[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

ans = []
for c in cost[1:]:
    ans.append(sum(c[1:]))

print(ans.index(min(ans)) + 1)
