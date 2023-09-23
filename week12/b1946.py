# 신입사원
# 서류, 면접 각각 1등을 고르고, 나머지 서류 면접 두부분이 모두 높은 사람을 추가로 뽑음
#
import sys

t = int(sys.stdin.readline())

while t != 0:
    count = 0
    result = []
    s = True
    n = int(sys.stdin.readline())
    for i in range(n):
        doc, itv = map(int, sys.stdin.readline().split())
        if doc == 1 and itv == 1:
            count += 1
            continue

        if doc == 1:
            count += 1
            continue

        if itv == 1:
            count += 1
            continue

        result.append([doc, itv])

    for i in range(n - count):
        for j in range(n - count):
            if i != j:
                if result[i][0] > result[j][0] and result[i][1] > result[j][1]:
                    s = False
                    break
        if s:
            print(result[i])
            count += 1
        s = True

    print(count)
    t -= 1
