# 계단 오르기
# 이것이 바로 나의 첫 knapsack..?
import sys

n = int(sys.stdin.readline())
stairs = []
for _ in range(n):
    s = int(sys.stdin.readline())
    stairs.append(s)

score = 0
threeCnt = 0
idx = -1
while idx < n - 2:
    if threeCnt == 3:
        idx += 1
        threeCnt = 1
        continue

    if stairs[idx + 1] > stairs[idx + 2]:
        score += stairs[idx + 1]
        threeCnt += 1
        idx += 1
    else:
        score += stairs[idx + 2]
        threeCnt = 1
        idx += 2

print(score)
