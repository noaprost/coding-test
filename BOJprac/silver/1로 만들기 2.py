import sys
from collections import deque

n = int(sys.stdin.readline())

# 그래프 탐색 시작 (BFS 이용)
que = deque()
visited = [False] * (n + 1)
distCheck = [0] * (n + 1)

que.append((n, 0))

dist = 0

while que:
    v = que.popleft()

    if v[0] == 1:
        dist = v[1]
        break

    if v[0] % 3 == 0 and not visited[v[0] // 3]:
        que.append((v[0] // 3, v[1] + 1))
        visited[v[0] // 3] = True
        distCheck[v[0] // 3] = v[0]

    if v[0] % 2 == 0 and not visited[v[0] // 2]:
        que.append((v[0] // 2, v[1] + 1))
        visited[v[0] // 2] = True
        distCheck[v[0] // 2] = v[0]

    if not visited[v[0] - 1]:
        que.append((v[0] - 1, v[1] + 1))
        visited[v[0] - 1] = True
        distCheck[v[0] - 1] = v[0]

print(dist)
ans = [1]
tmp = 1
for _ in range(dist):
    ans.append(distCheck[tmp])
    tmp = distCheck[tmp]

for i in range(len(ans) - 1, -1, -1):
    print(ans[i], end=" ")
