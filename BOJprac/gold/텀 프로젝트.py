# 9466
import sys

sys.setrecursionlimit(10 ** 8)


def dfs(node):
    global ans
    visited[node] = True
    team.append(node)

    next = order[node]

    if not visited[next]:
        dfs(next)
    else:
        if next in team:
            ans += len(team) - team.index(next)


caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    n = int(sys.stdin.readline())
    visited = [True] + [False for _ in range(n)]
    ans = 0

    order = [0] + list(map(int, sys.stdin.readline().split()))

    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n - ans)
