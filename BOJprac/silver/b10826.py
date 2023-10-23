import sys

n = int(sys.stdin.readline())

if n == 1:
    exit(print(1))
elif n == 0:
    exit(print(0))

a = 1
b = 1
for _ in range(n - 2):
    tmp = b
    b = a + b
    a = tmp
print(b)
