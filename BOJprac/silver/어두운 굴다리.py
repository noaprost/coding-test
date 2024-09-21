# 17266
import sys
import math

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
h = max(x[0], n - x[-1])


for i in range(0, m - 1):
    h = max(h, math.ceil((x[i + 1] - x[i]) / 2))

print(h)
