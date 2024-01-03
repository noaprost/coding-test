import sys

n = int(sys.stdin.readline())

print("*" * (n))

for i in range(1, n):
    print(" " * (i - 1), "*" * (n - i))
