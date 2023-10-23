# 이친수
import sys

n = int(sys.stdin.readline())

fibo = [1, 1]

if n == 1 or n == 2:
    print(1)
else:
    for i in range(2, n + 1):
        fibo.append(fibo[i - 2] + fibo[i - 1])
    print(fibo[n - 1])
