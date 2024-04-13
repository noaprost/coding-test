# 줄번호
import sys

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    s = sys.stdin.readline().rstrip()

    print(i, end="")
    print(".", s)