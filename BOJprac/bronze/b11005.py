import sys

n, b = map(int, sys.stdin.readline().split())

r = []

while n > 0:
    r.append(n % b)
    n = int(n / b)

r.reverse()

for rr in r:
    if int(rr) >= 10:
        print(chr(int(rr) + 55), end="")
    else:
        print(rr, end="")
