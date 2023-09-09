import sys

n, m = map(int, sys.stdin.readline().split())

b = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    b[i - 1], b[j - 1] = b[j - 1], b[i - 1]

for bb in b:
    print(bb, end=" ")
