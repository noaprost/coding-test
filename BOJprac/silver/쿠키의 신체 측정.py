# 20125
import sys

n = int(sys.stdin.readline())
cookie_map = [sys.stdin.readline().rstrip() for _ in range(n)]

heart = [0, 0]

for i in range(n):
    if cookie_map[i].count("*") == 1:  # 머리
        heart[0], heart[1] = i + 1, cookie_map[i].index("*")
        print(heart[0] + 1, heart[1] + 1)  # 심장
        break

# 왼팔
left_arm = 0
for i in range(heart[1] - 1, -1, -1):
    if cookie_map[heart[0]][i] == "*":
        left_arm += 1
    else:
        break

# 오른팔
right_arm = 0
for i in range(heart[1] + 1, n, 1):
    if cookie_map[heart[0]][i] == "*":
        right_arm += 1
    else:
        break

waist = 0  # 허리
left_leg = 0  # 왼다리
right_leg = 0  # 오른다리
for i in range(heart[0] + 1, n, 1):
    if cookie_map[i][heart[1]] == "*":
        waist += 1
    if cookie_map[i][heart[1] - 1] == "*":
        left_leg += 1
    if cookie_map[i][heart[1] + 1] == "*":
        right_leg += 1

# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리
print(left_arm, right_arm, waist, left_leg, right_leg)
