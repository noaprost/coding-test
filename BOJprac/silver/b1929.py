import sys
import math


def isPrime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


a, b = map(int, sys.stdin.readline().split())

n = a

while True:
    if n >= a and n <= b:
        if isPrime(n):
            print(n)
    else:
        break
    n += 1
