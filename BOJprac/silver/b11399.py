# ATM

import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

num.sort(reverse=True)
sum = 0

for i in range(1, n + 1):
    sum += i * num[i - 1]

print(sum)
