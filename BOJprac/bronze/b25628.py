import sys

b, p = map(int, sys.stdin.readline().split())

print(min(b // 2, p))
