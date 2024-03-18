# 조별과제를 하려는데 조장이 사라졌다
import sys

n = int(sys.stdin.readline())

ans = 0

ans = n // 5
n = n % 5

if n == 0:
    print(ans)
else:
    print(ans + 1)
