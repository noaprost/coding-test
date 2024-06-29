# 2668
import sys
from itertools import permutations

n = int(sys.stdin.readline())
base = [i for i in range(1, n + 1)]
nums = [0] + [int(sys.stdin.readline()) for _ in range(n)]
