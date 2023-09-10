import sys

n, m = map(int, sys.stdin.readline().split())
a = [[0 for _ in range(m)] for _ in range(n)]
b = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        a[i][j] = tmp[j]

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        a[i][j] += tmp[j]

for aa in a:
    for aaa in aa:
        print(aaa, end=" ")
    print("")
