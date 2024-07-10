# 14889
import sys
from itertools import combinations
from collections import deque

n = int(sys.stdin.readline())
members = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nums = [i for i in range(n)]
que = deque()
ans = []

for combi in combinations(nums, n // 2):
    que.append(combi)

while que:
    v = que.popleft()

    curmem = set()
    diff1 = 0
    diff2 = 0

    for i in range(len(v)):
        curmem.add(v[i])

    diffmem = set(nums).difference(curmem)

    for c in combinations(curmem, 2):
        diff1 += members[c[0]][c[1]] + members[c[1]][c[0]]

    for c in combinations(diffmem, 2):
        diff2 += members[c[0]][c[1]] + members[c[1]][c[0]]

    ans.append(abs(diff1 - diff2))

print(min(ans))
