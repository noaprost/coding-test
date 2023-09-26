# 두 배 더하기
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
count = 0

while True:
    for i in range(n):
        if nums[i] == 0:
            continue

        if nums[i] % 2 != 0:
            nums[i] -= 1
            count += 1

    if sum(nums) == 0:
        exit(print(count))

    for j in range(n):
        if nums[j] != 0:
            nums[j] = int(nums[j] / 2)
    count += 1
