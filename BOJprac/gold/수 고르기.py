# 2230
import sys

n, m = map(int, sys.stdin.readline().split())

nums = [int(sys.stdin.readline()) for _ in range(n)]

diff = []

a, b = 0, 1

nums.sort()

while a < b and a < n and b < n:
    print(nums[b], nums[a])
    if nums[b] - nums[a] == m:
        exit(print(nums[a] - nums[b]))

    elif nums[b] - nums[a] > m:
        diff.append(nums[b] - nums[a])
        a += 1

# 이미 m보다 큰차이를 발견한 상황에서 b를 어떻게 증가시킬 것인가
# 해결해야하는 반례
# 7 4
# 1
# 8
# 15
# 16
# 17
# 18
# 22

print(min(diff))
