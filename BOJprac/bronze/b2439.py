import sys

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    print("{0: >{1}}".format("*" * i, n))
