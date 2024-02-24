# 분산 처리
import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    a, b = map(int, sys.stdin.readline().split())
    if a % 10 == 0:
        print(10)
    else:
        tmp = []
        s = 1
        for _ in range(b):
            s = (s * a) % 10
            if s not in tmp:
                tmp.append(s)
            else:
                break
        print(tmp[b % len(tmp) - 1])
