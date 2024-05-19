# 동전 1

import sys

baseN, baseK = map(int, sys.stdin.readline().split())

num = [int(sys.stdin.readline()) for _ in range(baseN)]

total = [0] * baseK
i = 0

for n in range(baseN):
    for k in range(baseK):
        if n == 0:  # 초기화
            # 사용할 수 있는 동전의 개수가 1개 이므로
            if (k + 1) % num[n] == 0:  # 나누어떨어지면 경우의 수 1 추가
                total[k] = 1
            else:
                total[k] = 0
        else:  # 총합 값 업데이트
            # 동전 가치보다 작은 수는 만들 수 없으므로
            if (k + 1) < num[n]:
                total[k] = total[k] + 0  # 경우의 수 0을 더해줌

            # 동전 가치와 같은 수는 동전 1개로 표현할 수 있으므로
            elif (k + 1) == num[n]:
                total[k] = total[k] + 1  # 경우의 수 1을 더해줌

            # 동전 가치보다 큰 수의 경우, 이전 동전들로 만들 수 있는 경우의 수가 반복되므로
            elif (k + 1) > num[n]:
                total[k] = total[k] + total[i]  # 이전 경우의 수를 더해줌
                i = i + 1
    i = 0

print(total)
