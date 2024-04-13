import sys
import math

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    r, n = map(int, sys.stdin.readline().split())
    print(math.comb(n, r))
