# 오큰수
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

stack = []
nums.reverse()
ans = []
i = 0

while i < n - 1:
    v = nums.pop()
    if len(nums) != 0 and nums[-1] <= v:
        while len(nums) != 0 and nums[-1] <= v:
            stack.append(nums.pop())
        if len(nums) == 0:
            ans.append(-1)
        else:
            ans.append(nums[-1])
            a = nums[-1]
    elif len(nums) == 0:
        ans.append(v)
        break
    else:
        ans.append(nums[-1])

    if len(stack) != 0:
        while len(stack) != 0:
            nums.append(stack.pop())
    i += 1


ans.append(-1)

print(*ans)
