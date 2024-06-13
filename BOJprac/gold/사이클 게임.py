# 20040
import sys
sys.setrecursionlimit(10**8)

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[x] = y

for i in range(1, m + 1):
    s, e = map(int, sys.stdin.readline().split())

    if find(s) == find(e):
        exit(print(i))

    union(s, e)

print(0)
