# 1520
import sys

m, n = map(int, sys.stdin.readline().split())  # 세로, 가로

maps = []

for _ in range(m):
    maps.append(list(map(int, sys.stdin.readline().split())))
