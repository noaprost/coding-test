# 오큰수
import sys

n = int(sys.stdin.readline())

nums = list(sys.stdin.readline().split())

stack = []
for i in range(n - 1, 0, -1):
    stack.append(nums[i])

tmp = []
ans = []
i = 0

while i < n and len(ans) != n:
    while len(stack) > 0 and stack[-1] <= nums[i]:
        tmp.append(stack.pop())

    if len(stack) == 0:
        ans.append(-1)
    else:
        ans.append(stack.pop())

    i += 1

    while len(tmp) != 0:
        stack.append(tmp.pop())

print(*ans)
