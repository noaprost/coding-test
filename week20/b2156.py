# 포도주 시식
import sys

n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(n)]

alcohol = [[[0, 0], [nums[0], 1]]] + [[] for _ in range(n - 1)]

for i in range(1, n):
    m = max(alcohol[i - 1])
    alcohol[i].append([m[0], 0])
    alcohol[i].append([alcohol[i - 1][0][0] + nums[i], 1])
    alcohol[i].append([alcohol[i - 1][1][0] + nums[i], 2])

tmp = max(alcohol[n - 1])
print(tmp[0])
