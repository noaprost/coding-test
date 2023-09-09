import sys

n, m = map(int, sys.stdin.readline().split())
b = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    b1 = b[i - 1 : j]
    b1.reverse()

    idx = 0

    for k in range(i - 1, j):
        b[k] = b1[idx]
        idx += 1

for bb in b:
    print(bb)
