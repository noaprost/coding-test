import sys

n = int(sys.stdin.readline())

a = 0
b = 1

for i in range(2, n + 2):
    tmp = b
    b = (a + b) % 15746
    a = tmp

print(b)
