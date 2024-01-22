# 팩토리얼2
import sys

n = int(sys.stdin.readline())
f = 1
if n == 0 or n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        f *= i
    print(f)
