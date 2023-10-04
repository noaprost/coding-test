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


caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    n = int(sys.stdin.readline())

    while True:
        if isPrime(n):
            print(n)
            break
        n += 1
