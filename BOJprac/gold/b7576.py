import sys
from queue import Queue

m, n = map(int, sys.stdin.readline().split())
tomato = [[] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
ripeTomatoLoc = []  # 익은 토마토의 위치
count = [[0 for _ in range(m)] for _ in range(n)]
que = Queue()

for i in range(n):
    k = 0
    for j in list(sys.stdin.readline().strip().split()):
        tomato[i].append(j)
        if j == "1":
            ripeTomatoLoc.append([i, k])
            visited[i][k] = True
        k += 1

for r in ripeTomatoLoc:
    que.put(r)

    while que.qsize() != 0:
        v = que.get()
        x = v[0]
        y = v[1]
        visited[x][y] = True

        if x > 0 and not visited[x - 1][y] and tomato[x - 1][y] == "0":
            que.put([x - 1, y])
            visited[x - 1][y] = True
            count[x - 1][y] += count[x][y] + 1

        if x < n - 1 and not visited[x + 1][y] and tomato[x + 1][y] == "0":
            que.put([x + 1, y])
            visited[x + 1][y] = True
            count[x + 1][y] += count[x][y] + 1

        if y > 0 and not visited[x][y - 1] and tomato[x][y - 1] == "0":
            que.put([x, y - 1])
            visited[x][y - 1] = True
            count[x][y - 1] += count[x][y] + 1

        if y < m - 1 and not visited[x][y + 1] and tomato[x][y + 1] == "0":
            que.put([x, y + 1])
            visited[x][y + 1] = True
            count[x][y + 1] += count[x][y] + 1

        if que.qsize() != 0:
            print(count[x][y])

for t in tomato:
    print(t)

for c in count:
    print(c)
