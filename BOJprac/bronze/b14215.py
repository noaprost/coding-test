import sys

num = list(map(int, sys.stdin.readline().split()))

maxValue = max(num)
num.remove(maxValue)

if num[0] + num[1] - 1 > maxValue:
    print(num[0] + num[1] + maxValue)
else:
    print(num[0] * 2 + num[1] * 2 - 1)
