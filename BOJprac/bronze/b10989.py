# 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
nums = [0] * (10001)

for _ in range(n):
    nums[int(sys.stdin.readline())] += 1

for num in range(len(nums)):
    if nums[num] != 0:
        for _ in range(nums[num]):
            print(num)
