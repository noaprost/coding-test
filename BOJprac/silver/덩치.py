import sys

n = int(sys.stdin.readline())
level = [0 for _ in range(n)]
kgm = list((list(map(int, sys.stdin.readline().split()))) for _ in range(n))

for i in range(n):
    l = 1
    for j in range(n):
        if i != j and kgm[i][0] < kgm[j][0] and kgm[i][1] < kgm[j][1]:
            l += 1
    level[i] = l

print(*level)