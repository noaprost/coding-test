# 패션왕 신해빈
# 옷의 조합을 구해야하는 문제, 부분집합 구하기와 유사해보임
import sys

caseNum = int(sys.stdin.readline())
for _ in range(caseNum):
    closet = {}
    count = 1
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
        continue
    for _ in range(n):
        cloth, type = sys.stdin.readline().rstrip().split()
        if type not in closet:
            closet[type] = [cloth]
        else:
            closet[type].append(cloth)

    if len(closet) == n:
        print(pow(2, len(closet)) - 1)
        continue

    for c in closet.keys():
        count *= len(closet[c]) + 1

    print(count - 1)
