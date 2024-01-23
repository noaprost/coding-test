# 오큰수
import sys

n = int(sys.stdin.readline())

nums = list(sys.stdin.readline().split())

stack = []
nums.reverse()
ans = []

while len(nums) != 0:
    v = nums.pop()
    if nums[-1] <= v:
        while nums[-1] < v:
            stack.append(nums.pop())
        ans.append(nums[-1])
    else:
        ans.append(nums[-1])

    if len(stack) != 0:
        for s in stack:
            nums.append(s)

ans.append(-1)

print(*ans)
