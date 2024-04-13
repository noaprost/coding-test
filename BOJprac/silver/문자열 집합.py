import sys

n, m = map(int, sys.stdin.readline().split())

a = set([sys.stdin.readline().strip() for _ in range(n)])
b = [sys.stdin.readline().strip() for _ in range(m)]

count = 0

for bb in b:
    if bb in a:
        count += 1
print(count)
