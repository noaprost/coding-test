# 4485
import sys
import heapq

INF = int(1e8)
# LRBT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    hq = []
    heapq.heappush(hq, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while len(hq) != 0:
        cost, x, y = heapq.heappop(hq)

        # 상하좌우 탐색을 위함
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                ncost = cost + graph[nx][ny]

                if ncost < distance[nx][ny]:
                    distance[nx][ny] = ncost
                    heapq.heappush(hq, (ncost, nx, ny))


n = int(sys.stdin.readline())
count = 1

while n != 0:
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # 전체가 INF인 거리 배열 생성
    distance = [[INF] * n for _ in range(n)]

    dijkstra()

    print("Problem", count, end="")
    print(":", distance[n - 1][n - 1])
    count += 1

    n = int(sys.stdin.readline())
