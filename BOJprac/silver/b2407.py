# 조합
import sys

n, m = map(int, sys.stdin.readline().split())


def facto(a):
    sum = 1
    for i in range(2, a + 1):
        sum *= i

    return sum


print(facto(n) // (facto(n - m) * facto(m)))
