# 1647
import sys
import heapq

vnum, enum = map(int, sys.stdin.readline().split())
visited = [False] * (vnum + 1)
edgeList = [[] for _ in range(vnum + 1)]
heap = [(0, 1)]
for _ in range(enum):
    s, e, w = map(int, sys.stdin.readline().split())
    edgeList[s].append((w, e))
    edgeList[e].append((w, s))

totalWeight = []
count = 0
while heap:
    if count == vnum:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        totalWeight.append(w)
        count += 1
        for edge in edgeList[s]:
            heapq.heappush(heap, edge)

print(sum(totalWeight) - max(totalWeight))
