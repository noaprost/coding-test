# 상근이의 친구들
import sys

a, b = map(int, sys.stdin.readline().split())

while a != 0:
    print(a + b)
    a, b = map(int, sys.stdin.readline().split())
