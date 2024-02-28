# 윷놀이
import sys

for _ in range(3):
    num = list(map(int, sys.stdin.readline().split()))
    c = num.count(1)
    if c == 0:
        print("D")
    elif c == 1:
        print("C")
    elif c == 2:
        print("B")
    elif c == 3:
        print("A")
    elif c == 4:
        print("E")
