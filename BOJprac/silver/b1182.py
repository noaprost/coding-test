# 부분 수열의 합
from itertools import combinations
import sys

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, n + 1):
    for combi in list(combinations(num, i)):
        if len(combi) != 0 and sum(combi) == s:
            count += 1

print(count)
