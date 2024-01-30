# 15486
import sys

n = int(sys.stdin.readline())
con = []
for _ in range(n):
    con.append(list(map(int, sys.stdin.readline().split())))
ans = []
for k in range(n):
    conN = n - k
    tmp = 0
    while conN >= 0:
        print(n - conN)
        if conN - con[n - conN][0] >= 0:
            tmp += con[n - conN][1]
            conN -= con[n - conN][0]
        else:
            break
    ans.append(tmp)
print(max(ans))
