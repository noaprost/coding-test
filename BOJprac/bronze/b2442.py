# 별찍기-5
import sys

n = int(sys.stdin.readline())

for i in range(1, n * 2, 2):
    print(" " * (int((n * 2 - 1 - i) / 2)), end="")
    print("*" * i, end="")
    print()
