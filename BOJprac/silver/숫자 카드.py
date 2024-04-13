import sys

n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for bb in b:
    if bb in a:
        print(1, end=" ")
    else:
        print(0, end=" ")
