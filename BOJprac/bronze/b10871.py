import sys

n, x = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

for aa in a:
    if aa < x:
        print(aa, end=" ")
