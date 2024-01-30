# 2 x n 타일링
# n을 1, 2를 사용해서 표현 + 순서 중요
# 1, 2, ... n의 경우의 수가 피보나치 수열의 형태로 증가함
# n의 맨 앞을 채우는 경우는 1x2 1개, 2x1 2개 두가지 경우만 존재
# 1x2 1개 채우고 남은게 n-1의 경우의 수, 2x1 2개 채운고 남은게 n-2의 경우의 수

import sys

n = int(sys.stdin.readline())

p = [0 for _ in range(n + 1)]

p[0] = 1
p[1] = 1                                                                                                                                                                    

for i in range(2, n + 1):
    p[i] = p[i - 1] + p[i - 2]

print(p[n] % 10007)
