import sys

x, y, w, h = map(int, sys.stdin.readline().split())

m = [x, y, abs(x - w), abs(y - h)]

print(min(m))
