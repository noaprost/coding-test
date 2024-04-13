import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)

sum = 0

for aa, bb in zip(a, b):
    sum += aa * bb

print(sum)
