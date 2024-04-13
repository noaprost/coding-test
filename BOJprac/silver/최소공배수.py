import sys

a, b = map(int, sys.stdin.readline().split())

a1 = a
b1 = b

while True:
    r = a1 % b1
    if r == 0:
        break
    else:
        a1 = b1
        b1 = r

print(int(a * b / b1))
