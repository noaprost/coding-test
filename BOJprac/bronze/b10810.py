import sys

n, m = map(int, sys.stdin.readline().split())
b = [0 for _ in range(n)]

for _ in range(m):
    s, e, v = map(int, sys.stdin.readline().split())
    for i in range(s - 1, e):
        b[i] = v

for j in range(n):
    print(b[j], end=" ")
