import sys

n = list(map(int, sys.stdin.readline().strip()))

n.sort(reverse=True)

print("".join(map(str, n)))
