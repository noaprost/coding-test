# 14888
import sys
from itertools import permutations

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
opernum = list(map(int, sys.stdin.readline().split()))

oper = []
oper += ["+" for _ in range(opernum[0])]
oper += ["-" for _ in range(opernum[1])]
oper += ["*" for _ in range(opernum[2])]
oper += ["/" for _ in range(opernum[3])]

minans = 10000000000
maxans = -10000000000

for op in permutations(oper, len(oper)):
    tmp = nums[0]
    for i in range(0, len(nums) - 1):
        if op[i] == "+":
            tmp += nums[i + 1]
        elif op[i] == "-":
            tmp -= nums[i + 1]
        elif op[i] == "*":
            tmp *= nums[i + 1]
        elif op[i] == "/":
            if tmp < 0 and nums[i + 1] > 0:
                tmp = abs(tmp) // nums[i + 1]
                tmp *= -1
            else:
                tmp = tmp // nums[i + 1]

    minans = min(minans, tmp)
    maxans = max(maxans, tmp)

print(maxans)
print(minans)
