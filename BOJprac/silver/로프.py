import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort(reverse=True)

num = [nums[0]]
s = nums[0]
for i in range(1, len(nums)):
    num.append(nums[i])
    s = max(s, num[-1] * (i + 1))

print(s)
