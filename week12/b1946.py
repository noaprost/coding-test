# 신입사원
# 정렬 후 서류 기준으로 1등을 뽑고 1등의 면접 점수보다 높은 사람을 다 뽑음
import sys

t = int(sys.stdin.readline())

while t != 0:
    count = 1
    result = []

    n = int(sys.stdin.readline())

    for _ in range(n):
        doc, itv = map(int, sys.stdin.readline().split())
        result.append([doc, itv])

    result.sort()

    itvRank = result[0][1]
    for i in range(1, n):
        if result[i][1] < itvRank:
            count += 1
            itvRank = result[i][1]

    print(count)
    t -= 1
