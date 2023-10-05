import sys


n = int(sys.stdin.readline())  # 입력 받을 개수
num = [int(sys.stdin.readline()) for i in range(int(n))]  # 입력 받은 수의 배열

eratos = [False, False] + [True for _ in range(2, 1000001)]
primes = []

for i in range(2, int(max(num) / 2)):
    if eratos[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            eratos[j] = False

for n in num:
    count = 0

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] + primes[j] > n:
                break
            elif primes[i] + primes[j] == n:
                count += 1

    print(count)
