# 선물
import sys

n, l, w, h = map(int, sys.stdin.readline().split())

# <필요한 것>
# 길이의 크기 비교 -> 몫을 올려봤을 때 가장 길이가 크게 나오는걸 적용 max함수 적용
# 몫 계산
# 원하는 개수를 담을 수 있을 때 까지 -> 몫을 다 곱한게 담을 수 있는 개수

m = min(l, w, h)  # 길이의 최소값, 초기화

q = [l // m, w // m, h // m]  # 몫들을 저장할 배열
num = q[0] * q[1] * q[2]  # 담을 수 있는 개수
m1 = min(l, w, h)
while num < n:
    l1 = l / (q[0] + 1)
    l2 = w / (q[1] + 1)
    l3 = h / (q[2] + 1)

    if max(l1, l2, l3) == l1:
        q[0] += 1
        m1 = l1
    elif max(l1, l2, l3) == l2:
        q[1] += 1
        m1 = l2
    elif max(l1, l2, l3) == l3:
        q[2] += 1
        m1 = l3

    # 개수 업데이트
    num = q[0] * q[1] * q[2]

print(m1)
