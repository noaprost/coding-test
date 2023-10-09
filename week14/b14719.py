import sys

ssr = sys.stdin.readline()

# width, height
h, w = map(int, ssr.split())

# 벽 세우기
wall = list(map(int, sys.stdin.readline().split()))

ans = 0

# width를 하나씩 점검하면서 물이 찰 수 있으면 채울 수 있는 공간을 세줌
for i in range(1, w - 1):
    left_max = max(wall[:i])
    right_max = max(wall[i + 1 :])

    # 큰 벽 중에 더 작은 벽
    secondWall = min(left_max, right_max)

    if wall[i] < secondWall:
        ans += secondWall - wall[i]

print(ans)
