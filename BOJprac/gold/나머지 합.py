import sys

n, m = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split())) + [0]
r = [0 for _ in range(m)]
for i in range(n):
    x[i] += x[i - 1]
    r[x[i] % m] += 1

count = r[0]

for i in r:
    count += i * (i - 1) // 2

print(count)
