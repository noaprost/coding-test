# 1717
# union-find 알고리즘
import sys

sys.setrecursionlimit(10**5)


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
