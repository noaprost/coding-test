# 1707
import sys
from collections import deque


def bfs(start):
    que.append(start)
    color[start] = 1
    visited[start] = True

    while que:
        v = que.popleft()

        for ed in edges[v]:
            if not visited[ed]:
                color[ed] = -color[v]
                que.append(ed)
                visited[ed] = True

            elif color[v] == color[ed]:
                return "NO"

    return "YES"


caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    n, m = map(int, sys.stdin.readline().split())
    que = deque()
    edges = [[] for _ in range(n + 1)]
    color = [0 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    for _ in range(m):
        s, e = map(int, sys.stdin.readline().split())
        edges[s].append(e)
        edges[e].append(s)

    cur = bfs(1)
    for i in range(1, n + 1):
        if not visited[i]:
            tmp = bfs(i)
            if tmp == cur:
                cur = tmp
            elif tmp != cur:
                cur = "NO"
                break

    print(cur)
