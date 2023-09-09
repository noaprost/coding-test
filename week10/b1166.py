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

while num < n:
    l1 = l / (q[0] + 1)
    l2 = w / (q[1] + 1)
    l3 = h / (q[2] + 1)

    if max(l1, l2, l3) == l1:
        q[0] += 1
    elif max(l1, l2, l3) == l2:
        q[1] += 1
    elif max(l1, l2, l3) == l3:
        q[2] += 1

    # 개수 업데이트
    num = q[0] * q[1] * q[2]

a1 = l / q[0]
a2 = w / q[1]
a3 = h / q[2]

# 가장 작은 길이보다는 작아야함
# 작은 것들 중에서는 제일 커야함 -> 몫이

t = [a1, a2, a3]
aa = []
qq = []
for i in range(3):
    if t[i] <= m:
        aa.append(t[i])
        qq.append(q[i])
print(round(aa[qq.index(max(qq))], 15))
