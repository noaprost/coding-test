# 수리공 항승
import sys
import math

n, length = map(int, sys.stdin.readline().split())

leak = list(map(int, sys.stdin.readline().split()))
leak.sort()

ans = []

for i in range(n):
    if i == 0:
        tmp = 1
    else:
        if abs(leak[i - 1] - leak[i]) <= (length - 1):
            tmp += 1
        else:
            ans.append(tmp)
            tmp = 0

ans.append(tmp)
sum = 0
for a in ans:
    sum += math.ceil(a / length)
print(sum)
