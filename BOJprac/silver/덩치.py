import sys

ssr = sys.stdin.readline()

n = int(ssr)

kgm = []

l = 1
level = [0] * n


for _ in range(n):
    kg, m = map(int, sys.stdin.readline().split())

    kgm.append([kg, m])

for i in range(n):
    for j in range(n):
        if i != j and kgm[i][0] < kgm[j][0] and kgm[i][1] < kgm[j][1]:
            l += 1
    level[i] = l
    l = 1

for i in level:
    print(i, end=" ")
