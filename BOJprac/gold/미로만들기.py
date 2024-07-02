# 2665
import sys
import heapq

n = int(sys.stdin.readline())
maps = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 0:
            maps[i][j] = 1
        else:
            maps[i][j] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dist = [[1e8 for _ in range(n)] for _ in range(n)]
dist[0][0] = 0

heap = []
heapq.heappush(heap, (0, 0, 0))

while heap:
    x, y, cost = heapq.heappop(heap)

    if cost > dist[x][y]:
        continue

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if cost + maps[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = cost + maps[nx][ny]
                heapq.heappush(heap, (nx, ny, dist[nx][ny]))

print(dist[n - 1][n - 1])
