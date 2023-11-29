# 오르막 수

import sys

n = int(sys.stdin.readline())

count = [[] for _ in range(1001)]

for i in range(10):
    count[1].append(1)

d = 1

while d != n:
    d += 1
    for i in range(10):
        if i == 0:
            count[d].append(1)
        else:
            count[d].append(count[d][i - 1] + count[d - 1][i])


print(sum(count[d]) % 10007)
