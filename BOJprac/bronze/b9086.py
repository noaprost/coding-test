import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()
    print("{0}{1}".format(s[0], s[-1]))
