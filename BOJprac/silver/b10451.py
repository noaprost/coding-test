# 순열 사이클
import sys
from queue import Queue

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    n = int(sys.stdin.readline())
    tmp = list(map(int, sys.stdin.readline().split()))
    graph = [[]]
    for i in range(n):
        graph.append([tmp[i]])
    visited = [True] + [False for _ in range(n)]
    que = Queue()
    que.put(1)
    count = 0
    while True:
        while que.qsize() != 0:
            v = que.get()
            visited[v] = True
            if not visited[graph[v][0]]:
                que.put(graph[v][0])
        count += 1
        if visited.count(False) == 0:
            break
        else:
            que.put(visited.index(False))

    print(count)
