import sys

s = set()

for i in range(10):
    n = int(sys.stdin.readline())
    s.add(n % 42)

print(len(s))
