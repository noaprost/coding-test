# 돌게임

import sys

n = int(sys.stdin.readline())

tmp = n % 4

if tmp % 2 != 0:
    print("SK")
else:
    print("CY")
