# 2230
import sys

n, m = map(int, sys.stdin.readline().split())

nums = [int(sys.stdin.readline()) for _ in range(n)]

diff = []

a, b = 0, 1

nums.sort()

while b < n:
    if nums[b] - nums[a] == m:
        exit(print(nums[b] - nums[a]))

    elif nums[b] - nums[a] < m:
        b += 1

    elif nums[b] - nums[a] > m:
        diff.append(nums[b] - nums[a])
        a += 1

print(min(diff))
