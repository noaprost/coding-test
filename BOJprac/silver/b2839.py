# 설탕 배달
# 3kg 5kg씩만 가능

import sys

n = int(sys.stdin.readline())
ans = []
five = n // 5
three = n // 3

for i in range(five + 1):
    for j in range(three + 1):
        if n - i * 5 - j * 3 == 0:
            ans.append(i + j)

if len(ans) == 0:
    print(-1)
else:
    print(min(ans))
