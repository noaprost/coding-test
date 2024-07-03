# 14921
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

i = 0
j = len(nums) - 1
cur = 200000002

while i < j:
    if nums[i] + nums[j] == 0:
        exit(print(0))

    if nums[i] + nums[j] > 0:
        if nums[i] + nums[j] < abs(cur):
            cur = nums[i] + nums[j]
        j -= 1

    elif nums[i] + nums[j] < 0:
        if abs(nums[i] + nums[j]) < abs(cur):
            cur = nums[i] + nums[j]
        i += 1

print(cur)
