# 21608
import sys

n = int(sys.stdin.readline())
nums = [[0 for _ in range(n)] for _ in range(n)]
preferList = [[] for _ in range((n**2) + 1)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n**2):
    stu, *prefer = list(map(int, sys.stdin.readline().split()))
    position = []

    for p in prefer:
        preferList[stu].append(p)

    for x in range(n):
        for y in range(n):
            if nums[x][y] == 0:

                pre = 0
                empty = 0

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n:
                        if nums[nx][ny] == 0:
                            empty += 1
                        elif nums[nx][ny] in prefer:
                            pre += 1

                        position.append((-pre, -empty, x, y))

    position.sort()
    nums[position[0][2]][position[0][3]] = stu


ans = 0
score = [0, 1, 10, 100, 1000]
for x in range(n):
    for y in range(n):
        pre_count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if nums[nx][ny] in preferList[nums[x][y]]:
                    pre_count += 1

        ans += score[pre_count]

print(ans)
