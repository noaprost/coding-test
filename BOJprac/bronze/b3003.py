import sys

n = list(map(int, sys.stdin.readline().split()))

c = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(c[i] - n[i], end=" ")
