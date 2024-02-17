# 크냐?
import sys

a, b = map(int, sys.stdin.readline().split())
while a != 0:
    if a > b:
        print("Yes")
    else:
        print("No")

    a, b = map(int, sys.stdin.readline().split())
