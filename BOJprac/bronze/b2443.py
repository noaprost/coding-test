# 별찍기-6
import sys

n = int(sys.stdin.readline())

for i in range(n * 2 - 1, 0, -2):
    print(" " * int((n * 2 - 1 - i) / 2), end="")
    print("*" * (i), end="")
    print()
