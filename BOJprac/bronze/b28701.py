# 세제곱의 합
import sys

n = int(sys.stdin.readline())

nums = [i for i in range(1, n + 1)]

print(sum(nums))
print(pow(sum(nums), 2))
for i in range(n):
    nums[i] = pow(nums[i], 3)
print(sum(nums))
