# 병 찍기 - 9
import sys

n = int(sys.stdin.readline())

nn = 2 * n - 1


for i in range(nn, 0, -2):
    print(" " * int((nn-i)/2), end="")
    print("*" * (i), end="")
    print()
for i in range(3, nn + 2, 2):
    print(" " * int((nn-i)/2), end="")
    print("*" * (i), end="")
    if(i < nn+2):
        print()
