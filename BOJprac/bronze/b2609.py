# 최대공약수와 최소공배수
import sys

a, b = map(int, sys.stdin.readline().split())


def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    while r != 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd(a, b))
print((a * b) // gcd(a, b))
