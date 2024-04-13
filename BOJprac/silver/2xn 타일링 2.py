import sys

n = int(sys.stdin.readline())

p = [1, 3]

if n == 1 or n == 2:
    exit(print(p[n - 1]))
else:
    for i in range(2, n):
        p.append(p[i - 2] * 2 + p[i - 1])
    print(p[n - 1] % 10007)
