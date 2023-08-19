# 2 x n 타일링
# n을 1, 2를 사용해서 표현
# 순서 중요
# n이 1부터 증가함에 따라 피보나치 수열의 형태로 증가함

import sys

n = int(sys.stdin.readline())

p = [0 for _ in range(n + 1)]

p[0] = 1
p[1] = 1

for i in range(2, n + 1):
    p[i] = p[i - 1] + p[i - 2]

print(p[n] % 10007)
