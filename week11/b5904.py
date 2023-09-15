import sys

n = int(sys.stdin.readline())

Sk_1 = "moo"
Sk = Sk_1
count = len(Sk)

k = 1
while True:
    n -= count
    if n < len(Sk):
        break
    Sk = "m" + "o" * (k + 2) + Sk_1
    count = len(Sk)
    Sk_1 = Sk
    k += 1

print(Sk[n - 1])
