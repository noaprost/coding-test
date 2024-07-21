# 11689
# 오일러 피 함수
import sys
import math

n = int(sys.stdin.readline())
ans = n

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        while n % i == 0:
            n //= i

        ans -= ans / i

if n > 1:
    ans -= ans / n

print(int(ans))
