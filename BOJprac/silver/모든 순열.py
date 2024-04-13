import sys
from itertools import permutations

n = int(sys.stdin.readline())

num = [i for i in range(1, n + 1)]

for per in list(permutations(num, n)):
    print(*per)
