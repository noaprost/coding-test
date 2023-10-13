import sys

n = int(sys.stdin.readline())

i = 1
sum = 0

while True:
    n -= 2 * i + 1
    if n <= 0:
        break
    i += 1

print(i)


