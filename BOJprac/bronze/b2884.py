import sys

h, m = map(int, sys.stdin.readline().split())

if m - 45 < 0:
    if h - 1 < 0:
        print(24 + h - 1, 60 + m - 45)
    else:
        print(h - 1, 60 + m - 45)
else:
    print(h, m - 45)
