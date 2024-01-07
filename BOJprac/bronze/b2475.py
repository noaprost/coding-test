# 검증수
import sys

num = list(map(int, sys.stdin.readline().split()))

sum = 0

for i in range(5):
    sum += pow(num[i], 2) % 10

if sum >= 10:
    print(sum % 10)
else:
    print(sum)
