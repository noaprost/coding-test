import sys
from bisect import bisect_left  # 이진 탐색 도와주는 라이브러리

n = int(sys.stdin.readline())

xy = list(map(int, sys.stdin.readline().split()))

xyPrime = sorted(set(xy))

for x in xy:
    print(bisect_left(xyPrime, x), end=" ")
