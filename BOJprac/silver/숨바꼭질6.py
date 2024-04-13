import sys

n, s = map(int, sys.stdin.readline().split())

bro = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    bro[i] = abs(bro[i] - s)

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        while r != 0:
            r = a % b
            a = b
            b = r
        return a


if len(bro) == 1:
    print(bro[0])
elif len(bro) == 2:
    print(gcd(bro[0], bro[1]))
else:
    r = gcd(bro[0], bro[1])
    for i in range(2, len(bro)):
        r = gcd(bro[i], r)
    print(r)
