# 9019
import sys
from collections import deque

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    a, b = map(int, sys.stdin.readline().split())
    que = deque()
    visited = [False for _ in range(10001)]
    que.append((a, ""))
    visited[a] = True

    while que:
        n, c = que.popleft()

        if n == b:
            print(c)
            break

        d = (2 * n) % 10000
        if not visited[d]:
            visited[d] = True
            que.append((d, c + "D"))

        d = (n - 1) % 10000
        if not visited[d]:
            visited[d] = True
            que.append((d, c + "S"))

        d = (n % 1000) * 10 + n // 1000
        if not visited[d]:
            visited[d] = True
            que.append((d, c + "L"))

        d = (n % 10) * 1000 + n // 10
        if not visited[d]:
            visited[d] = True
            que.append((d, c + "R"))
