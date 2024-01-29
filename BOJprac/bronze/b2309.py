# 일곱 난쟁이
import sys
from itertools import combinations

tall = []
for _ in range(9):
    tall.append(int(sys.stdin.readline()))
tall.sort()
for combi in list(combinations(tall, 7)):
    if sum(combi) == 100:
        for c in combi:
            print(c)
        exit()
