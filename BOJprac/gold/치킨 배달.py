# 15686
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
peopleLoc = deque()
chickenLoc = deque()

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            peopleLoc.append([i, j])
        elif maps[i][j] == 2:
            chickenLoc([i, j])
