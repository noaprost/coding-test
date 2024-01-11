# 피보나치 수

import sys

pibo = [1, 1]
n = int(sys.stdin.readline())

for i in range(2, n):
    pibo.append(pibo[i - 1] + pibo[i - 2])

print(pibo[n-1])
