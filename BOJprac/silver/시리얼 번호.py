# 1431
import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(sys.stdin.readline().rstrip())

for i in range(n - 1):
    for j in range(i + 1, n):

        if len(nums[i]) > len(nums[j]):
            nums[i], nums[j] = nums[j], nums[i]

        elif len(nums[i]) == len(nums[j]):
            tmpA = 0
            tmpB = 0

            for a, b in zip(nums[i], nums[j]):
                if a.isdigit():
                    tmpA += int(a)

                if b.isdigit():
                    tmpB += int(b)

            if tmpA > tmpB:
                nums[i], nums[j] = nums[j], nums[i]

            elif tmpA == tmpB:
                for a, b in zip(nums[i], nums[j]):
                    if a > b:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    elif a < b:
                        break

for num in nums:
    print(num)
