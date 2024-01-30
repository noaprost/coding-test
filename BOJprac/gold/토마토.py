# 7576
import sys
from queue import Queue

m, n = map(int, sys.stdin.readline().split())
tomato = [[] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
ripeTomatoLoc = []  # 익은 토마토의 위치
count = 0
que = Queue()

minusCount = 0
oneCount = 0

for i in range(n):
    k = 0
    for j in list(sys.stdin.readline().strip().split()):
        tomato[i].append(j)
        if j == "1":
            ripeTomatoLoc.append([i, k])
            visited[i][k] = True
            oneCount += 1
        elif j == "-1":
            visited[i][k] = True
            minusCount += 1

        k += 1

if minusCount + oneCount == m * n:
    exit(print(0))

tmp = []
for r in ripeTomatoLoc:
    que.put(r)

while True:
    tmp = []

    while que.qsize() != 0:
        v = que.get()
        x = v[0]
        y = v[1]
        visited[x][y] = True

        if x > 0 and not visited[x - 1][y] and tomato[x - 1][y] == "0":
            tmp.append([x - 1, y])
            visited[x - 1][y] = True

        if x < n - 1 and not visited[x + 1][y] and tomato[x + 1][y] == "0":
            tmp.append([x + 1, y])
            visited[x + 1][y] = True

        if y > 0 and not visited[x][y - 1] and tomato[x][y - 1] == "0":
            tmp.append([x, y - 1])
            visited[x][y - 1] = True

        if y < m - 1 and not visited[x][y + 1] and tomato[x][y + 1] == "0":
            tmp.append([x, y + 1])
            visited[x][y + 1] = True

    count += 1

    if len(tmp) == 0:
        break

    if len(tmp) != 0:
        for t in tmp:
            que.put(t)

for v in visited:
    if False in v:
        exit(print(-1))

print(count - 1)
