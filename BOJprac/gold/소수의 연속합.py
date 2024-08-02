# 1644
import sys

n = int(sys.stdin.readline())
eratos = [False, False] + [True for _ in range(2, n + 1)]
prime = [0]

for i in range(2, n + 1):
    if eratos[i]:
        prime.append(i)
        for j in range(2 * i, n + 1, i):
            eratos[j] = False

for i in range(1, len(prime)):
    prime[i] += prime[i - 1]

ans = 0
s = 0
e = 0

while e < len(prime):
    tmp = prime[e] - prime[s]
    if tmp == n:
        ans += 1
        e += 1
    elif tmp < n:
        e += 1
    elif tmp > n:
        s += 1

print(ans)
