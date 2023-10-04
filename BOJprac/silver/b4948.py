import sys

n = int(sys.stdin.readline())
while n != 0:
    eratos = [False, False] + [True for _ in range(1, 2 * n)]
    primes = []
    count = 0

    for i in range(2, 2 * n + 1):
        if eratos[i]:
            primes.append(i)
            for j in range(2 * i, 2 * n + 1, i):
                eratos[j] = False

    for j in range(len(primes)):
        if primes[j] > n:
            count += 1
    print(count)
    n = int(sys.stdin.readline())
