import sys

ssr = sys.stdin.readline()

# width, height
w, h = map(int, ssr.split())

# 벽 세우기
wall = list(map(int, sys.stdin.readline().split()))

# 벽 중에 가장 높은 벽
m = max(wall)


mIdx = []
for i in range(len(wall)):
    if wall[i] == m:
        mIdx.append(i)

