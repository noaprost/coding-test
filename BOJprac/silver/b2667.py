import sys
from queue import Queue

n = int(sys.stdin.readline())
visited = [[True for _ in range(n)] for _ in range(n)]


def findFalse(m):
    for x in range(m):
        if False in visited[x]:
            y = visited[x].index(False)
            return x, y
    return -1, -1


total = 0

danji = []
que = Queue()

for i in range(n):
    k = 0
    for j in list(sys.stdin.readline().strip()):
        danji.append([])
        danji[i].append(j)
        if j == "1":
            visited[i][k] = False
        k += 1

x, y = findFalse(n)
counts = []

while x != -1:
    visited[x][y] = True
    que.put([x, y])
    count = 1
    while que.qsize() != 0:
        v = que.get()
        x = v[0]
        y = v[1]

        if x > 0:
            if not visited[x - 1][y] and danji[x - 1][y] == "1":
                que.put([x - 1, y])
                visited[x - 1][y] = True
                count += 1
        if x < n - 1:
            if not visited[x + 1][y] and danji[x + 1][y] == "1":
                que.put([x + 1, y])
                visited[x + 1][y] = True
                count += 1
        if y > 0:
            if not visited[x][y - 1] and danji[x][y - 1] == "1":
                que.put([x, y - 1])
                visited[x][y - 1] = True
                count += 1
        if y < n - 1:
            if not visited[x][y + 1] and danji[x][y + 1] == "1":
                que.put([x, y + 1])
                visited[x][y + 1] = True
                count += 1

    x, y = findFalse(n)
    total += 1
    counts.append(count)

print(total)
counts.sort()
for c in counts:
    print(c)
