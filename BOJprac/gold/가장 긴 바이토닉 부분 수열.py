# 11054
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
re_nums = nums[::-1]

incDP = [1 for _ in range(n)]
decDP = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            incDP[i] = max(incDP[i], incDP[j] + 1)
        if re_nums[i] > re_nums[j]:
            decDP[i] = max(decDP[i], decDP[j] + 1)

ans = []

for i in range(n):
    ans.append(incDP[i] + decDP[n - i - 1] - 1)

print(max(ans))
