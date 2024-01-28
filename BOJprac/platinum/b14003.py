# 가장 긴 증가하는 부분 수열5
from bisect import bisect_left
import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
dp = [1]
x = [num[0]]
lis_total = [(num[0], 0)]

for i in range(1, n):
    if num[i] > x[-1]:
        lis_total.append((num[i], len(x)))
        x.append(num[i])
        dp.append(dp[-1] + 1)
    else:
        idx = bisect_left(x, num[i])
        if idx < len(x):
            x[idx] = num[i]
            lis_total.append((num[i], idx))

print(dp[-1])

lis_length = len(x) - 1
lis = []
lis_total.sort(key=lambda x: (x[1], x[0]))

curNum = 999999999999
while lis_total and lis_length >= 0:
    num, idx = lis_total.pop()
    if idx == lis_length and curNum > num:
        lis.append(num)
        lis_length -= 1
        curNum = num

print(*lis[::-1])
