import sys

d = {}

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for aa in a:
    d[int(aa)] = a.count(aa)


m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for bb in b:
    if bb in d:
        print(d[bb], end=" ")
    else:
        print(0, end=" ")
