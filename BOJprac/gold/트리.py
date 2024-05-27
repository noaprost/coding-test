# 4803
import sys


def tree(num, prev, visited):
    if visited[num]:
        return 0
    visited[num] = True
    for g in graph[num]:
        if prev != g:
            if tree(g, num, visited) == 0:
                return 0
    return 1


c = 0
while True:
    c += 1
    count = 0
    n, m = map(int, sys.stdin.readline().split())

    if n == 0:
        break

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)

    nodeVisited = [True] + [False for _ in range(n)]

    for i in range(1, n + 1):
        if not nodeVisited[i]:
            count += tree(i, 0, nodeVisited)

    if count == 0:
        print("Case {0}: No trees.".format(str(c)))
    elif count == 1:
        print("Case {0}: There is one tree.".format(str(c)))
    elif count > 1:
        print("Case {0}: A forest of {1} trees.".format(str(c), str(count)))
