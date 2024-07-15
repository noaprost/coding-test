# 쉬운 계단 수
import sys

n = int(sys.stdin.readline())
count = [[0 for _ in range(n)] for _ in range(10)]

for d in range(n):
    for i in range(10):
        if d == 0:  # 문제의 가장 작은 상태, 초기화
            if i != 0:  # 0으로 시작하는 수는 해당 x
                count[i][d] = 1
        else:
            if i == 0:  # 다음 수는 무조건 1 한개, 0로 끝나는 수의 개수만큼 존재
                count[i][d] = count[i + 1][d - 1]
            elif i == 9:  # 다음 수는 무조건 8 한개, 9로 끝나는 수의 개수만큼 존재
                count[i][d] = count[i - 1][d - 1]
            else:  # 1 ~ 8은 +-한 수에 각각 1개씩 생김
                count[i][d] = count[i - 1][d - 1] + count[i + 1][d - 1]

sum = 0
for i in range(10):
    sum = sum + count[i][n - 1]

print(sum % 1000000000)
