import sys

eratos = [False, False] + [True for _ in range(2, 1000001)]

for i in range(2, 1000001):
    if eratos[i]:
        for j in range(2 * i, 1000001, i):
            eratos[j] = False

n = int(sys.stdin.readline())
while n != 0:
    isExit = False
    for i in range((n // 2) + 1):
        if eratos[i] and eratos[n - i]:
            print(str(n) + " = " + str(i) + " + " + str(n - i))
            isExit = True
            break
    if not isExit:
        print("Goldbach's conjecture is wrong.")
    n = int(sys.stdin.readline())
