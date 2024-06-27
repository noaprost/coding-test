# 10819
import sys
from itertools import permutations

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ans = 0

for per in permutations(nums, n):
    sum = 0
    for i in range(n - 1):
        sum += abs(per[i] - per[i + 1])
    ans = max(ans, sum)

print(ans)
