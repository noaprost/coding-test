# 1261
import sys
import heapq

m, n = map(int, sys.stdin.readline().split())
maps = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dist = [[1e8 for _ in range(m)] for _ in range(n)]
heap = []

heapq.heappush(heap, (0, 0, 0))
dist[0][0] = 0

while heap:
    x, y, c = heapq.heappop(heap)

    if c > dist[x][y]:
        continue

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if c + maps[nx][ny] < dist[nx][ny]:
                dist[nx][ny] = c + maps[nx][ny]
                heapq.heappush(heap, (nx, ny, dist[nx][ny]))

print(dist[n - 1][m - 1])
