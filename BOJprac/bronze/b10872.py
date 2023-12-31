import sys

n = int(sys.stdin.readline())

if n == 0:
    exit(print(1))

if n == 1:
    exit(print(1))

fac = 1

for i in range(2, n + 1):
    fac *= i

print(fac)
