# 14502
import sys
from queue import Queue
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

lab = [[] for _ in range(n)]  # 실험실
visited = [[False for _ in range(m)] for _ in range(n)]
virusLoc = []  # 바이러스의 위치
zeroLoc = []  # 0의 위치
zeroCount = []
que = Queue()
items = []
count = 0

# 전체적인 배열 입력
for i in range(n):
    k = 0
    for j in list(sys.stdin.readline().strip().split()):
        lab[i].append(j)
        if j == "0":
            zeroLoc.append([i, k])
        elif j == "1":
            visited[i][k] = True
        elif j == "2":
            virusLoc.append([i, k])
        k += 1

for item in list(combinations(zeroLoc, 3)):
    # item 한개에 3개의 좌표가 들어옴
    lab[item[0][0]][item[0][1]] = "1"
    lab[item[1][0]][item[1][1]] = "1"
    lab[item[2][0]][item[2][1]] = "1"

    visited[item[0][0]][item[0][1]] = True
    visited[item[1][0]][item[1][1]] = True
    visited[item[2][0]][item[2][1]] = True

    for vl in virusLoc:
        que.put(vl)

    while que.qsize() != 0:
        v = que.get()
        x = v[0]
        y = v[1]
        visited[x][y] = True

        if x > 0 and not visited[x - 1][y] and lab[x - 1][y] == "0":
            que.put([x - 1, y])
            visited[x - 1][y] = True

        if x < n - 1 and not visited[x + 1][y] and lab[x + 1][y] == "0":
            que.put([x + 1, y])
            visited[x + 1][y] = True

        if y > 0 and not visited[x][y - 1] and lab[x][y - 1] == "0":
            que.put([x, y - 1])
            visited[x][y - 1] = True

        if y < m - 1 and not visited[x][y + 1] and lab[x][y + 1] == "0":
            que.put([x, y + 1])
            visited[x][y + 1] = True

    for v in visited:
        count += v.count(False)
    zeroCount.append(count)

    # 초기화
    lab[item[0][0]][item[0][1]] = "0"
    lab[item[1][0]][item[1][1]] = "0"
    lab[item[2][0]][item[2][1]] = "0"

    for i in range(n):
        for j in range(m):
            if lab[i][j] == "1":
                visited[i][j] = True
            else:
                visited[i][j] = False
    count = 0

print(max(zeroCount))
