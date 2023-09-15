# 작은 수부터 약수를 구하기 때문에 정렬이 필요 없음

import sys

n, k = map(int, sys.stdin.readline().split())

m = []

for i in range(1, n + 1):
    if n % i == 0:
        m.append(i)
if len(m) >= k:
    print(m[k - 1])
else:
    print(0)
