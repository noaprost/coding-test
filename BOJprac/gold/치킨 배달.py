# 15686
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
peopleLoc = []
chickenLoc = []
ans = 1e8

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            peopleLoc.append([i, j])
        elif maps[i][j] == 2:
            chickenLoc.append([i, j])

for chi in combinations(chickenLoc, m):
    totalLen = 0
    for p in peopleLoc:
        chickenLen = 1e8
        for j in range(m):
            chickenLen = min(chickenLen, abs(chi[j][0] - p[0]) + abs(chi[j][1] - p[1]))
        totalLen += chickenLen
    ans = min(ans, totalLen)

print(ans)
