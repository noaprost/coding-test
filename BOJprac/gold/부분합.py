# 1806
import sys

n, s = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

total = nums[0]
ans = 1e8

a, b = 0, 0

while True:
    if total < s:
        b += 1
        if b == n:
            break
        total += nums[b]
    else:
        total -= nums[a]
        ans = min(ans, b - a + 1)
        a += 1

if ans == 1e8:
    print(0)
else:
    print(ans)
