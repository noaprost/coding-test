# 2110
import sys

n, c = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

s = 1
e = nums[-1] - nums[0]
ans = 0

while s <= e:
    mid = (s + e) // 2
    cur = nums[0]
    cnt = 1

    for i in range(1, n):
        if nums[i] >= cur + mid:
            cnt += 1
            cur = nums[i]
    if cnt >= c:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)
