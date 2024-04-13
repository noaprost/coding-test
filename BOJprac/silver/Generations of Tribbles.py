import sys

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    fibo = [1, 1, 2, 4]
    n = int(sys.stdin.readline())
    if n < 2:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        for i in range(4, n + 1):
            fibo.append(fibo[i - 4] + fibo[i - 3] + fibo[i - 2] + fibo[i - 1])
        print(fibo[n])
