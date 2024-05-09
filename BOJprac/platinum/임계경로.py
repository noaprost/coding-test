# 1948
# import sys
# from collections import deque

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# graph = [[] for _ in range(n + 1)]
# degree = [1e8] + [0 for _ in range(n)]
# d = [0]
# dq = deque()
# dp = [0 for _ in range(n + 1)]
# dist = 0

# for _ in range(m):
#     s, e, w = map(int, sys.stdin.readline().split())
#     graph[s].append(e)
#     d.append(w)

# s, e = map(int, sys.stdin.readline().split())
# tmp = deque()
# tmp.append(s)

# while tmp:
#     v = tmp.popleft()

#     for g in graph[v]:
#         degree[g] += 1
#         tmp.append(g)

# dq.append(s)
# dp[s] = d[s]

# while dq:
#     v = dq.popleft()

#     for g in graph[v]:
#         degree[g] -= 1
#         dp[g] = max(dp[v] + d[g], dp[g])
#         if degree[g] == 0:
#             dq.append(g)
#             dist += 1

# print(dp)
# print(dist)
