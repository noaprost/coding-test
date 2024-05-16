# 17219
import sys

n, m = map(int, sys.stdin.readline().split())
d = {}

for _ in range(n):
    address, password = sys.stdin.readline().split()
    d[address] = password

for _ in range(m):
    ad = sys.stdin.readline().rstrip()
    print(d[ad])
