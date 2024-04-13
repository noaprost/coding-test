import sys

n, m = map(int, sys.stdin.readline().split())

d = set([sys.stdin.readline().strip() for _ in range(n)])
b = set([sys.stdin.readline().strip() for _ in range(m)])


print(len(d.intersection(b)))

for s in sorted(d.intersection(b)):
    print(s)
