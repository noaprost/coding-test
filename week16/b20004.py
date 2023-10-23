# 베스킨 라빈스 31
# 가장 작은 필승 숫자가 n보다 크면 시온이 승
# 이길 수 있는 확률이 1/n+1 밖에 안됨
import sys

a = int(sys.stdin.readline())

for n in range(1, a + 1):
    to = 30
    while to > n + 1:
        to -= n + 1
    if to > n:
        print(n)
