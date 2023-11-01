# 가장 긴 증가하는 부분 수열

import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
dp = [[num[0]]]

for i in range(1, n):
    for j in range(len(dp)):
        if max(dp[j]) < num[i]:
            dp[j].append(num[i])
        else:
            dp.append([num[i]])
    print(dp)
dplen = []
for d in dp:
    dplen.append(len(d))
print(max(dplen))
