# 가장 작은 x 가장 큰 x 의 차이가 w
# 가장 작은 y 가장 큰 y 의 차이가 h

import sys

n = int(sys.stdin.readline())
x = []
y = []

for _ in range(n):
    xx, yy = map(int, sys.stdin.readline().split())

    x.append(xx)
    y.append(yy)

print((max(x) - min(x)) * (max(y) - min(y)))
