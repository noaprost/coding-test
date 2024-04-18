# 2467
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

s = 0
e = n - 1

cur = nums[s] + nums[e]

idx1 = s
idx2 = e

while s < e:
    y = nums[s] + nums[e]
    if abs(cur) > abs(y):
        cur = y
        idx1 = s
        idx2 = e

    if y > 0:
        e = e - 1
    elif y < 0:
        s = s + 1
    else:
        idx1 = s
        idx2 = e
        break

print(nums[idx1], nums[idx2])
