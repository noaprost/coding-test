# 뱀
import sys
from collections import deque

n = int(sys.stdin.readline())
map = [[0] * n] * n

directions = ["T", "R", "B", "L"]
snakeDirec = directions[1]

appleLoc = int(sys.stdin.readline())

x, y = map(int, sys.stdin.readline().split())
print(x, y)
# 사과의 위치 표시
# for _ in range(appleLoc):
#     x, y = map(int, sys.stdin.readline().split())
    #map[x - 1][y - 1] = 4

# l = int(sys.stdin.readline())

# d = deque()
# d.append([0, 0])
# map[0][0] = 1
# i = 0
# for _ in range(l):
#     val, rotate = sys.stdin.readline().split()
#     while i < val:
#         if snakeDirec == "T":
            # [d[0][0] + 1, d[0][1]]이 경계를 넘어갔는지 -> 넘으면 종료
            # 안넘었으면 d.appendleft([d[0][0] + 1, d[0][1]])
            # [d[0][0] + 1, d[0][1]]에 사과가 있는지 검사 필요
            # -> 꼬리를 없앨지 말지 검사 필요