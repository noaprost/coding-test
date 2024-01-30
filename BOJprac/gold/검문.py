# 2981
# 여러수를 각각 나눴을 때 같은 나머지가 나오게 만드는 수 찾기
# 1. 가장 작은 수를 각 수에서 빼준다
# 2. 나머지 수의 gcd를 구해준다

import sys
from math import gcd

n = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for _ in range(n)]

num.sort()

minus = []

# 이 부분이 있으면 같은 나머지가 나오는 수 중에 가장 큰 수를 구할 수 있음
for i in range(n - 1):
    minus.append(num[i + 1] - num[i])


# 모든 수의 gcd 값
gcm = gcd(*minus)

result = set()

# gcd의 약수와 해당 몫 저장
for j in range(2, int(gcm**0.5 + 1)):
    if gcm % j == 0:
        result.add(j)
        result.add(gcm // j)

result.add(gcm)
result = list(result)
result.sort()
print(*result)
