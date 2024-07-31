# 16928
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
visited = [False for _ in range(101)]

ladders = {}
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ladders[x] = y

snakes = {}
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    snakes[x] = y

heap = []
heapq.heappush(heap, (0, 1))

while heap:
    v = heapq.heappop(heap)

    if v[1] == 100:
        exit(print(v[0]))

    for i in range(1, 7):
        moveLoc = v[1] + i
        if moveLoc <= 100 and not visited[moveLoc]:
            if moveLoc in ladders:
                moveLoc = ladders[moveLoc]

            if moveLoc in snakes:
                moveLoc = snakes[moveLoc]

            if not visited[moveLoc]:
                visited[moveLoc] = True
                heapq.heappush(heap, (v[0] + 1, moveLoc))