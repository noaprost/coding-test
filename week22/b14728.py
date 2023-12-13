# 벼락치기
# 여러 과목을 동시에 / 한과목을 딱 채워서

import sys

n, time = map(int, sys.stdin.readline().split())

study = [0] * (time + 1)

for _ in range(n):
    k, s = map(int, sys.stdin.readline().split())
    if k > time:
        continue
    for j in range(time,0,-1):
        if k + j <= time and study[j] != 0:
            study[k + j] = max(study[k+j], study[j]+s)
    study[k] = max(study[k], s)

print(max(study))
