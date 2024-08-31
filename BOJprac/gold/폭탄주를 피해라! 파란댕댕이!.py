# 30982
import sys

n, m, t = map(int, sys.stdin.readline().split())  # 구역 수, 최종 마릿 수, 제한 시간
q = list(map(int, sys.stdin.readline().split()))  # 각 구역의 댕댕이 수
p = int(sys.stdin.readline()) - 1  # 파댕이 팀의 위치
p_num = q[p]  # 파댕이 구역의 마릿 수

if p_num == m:
    exit(print("YES"))

m -= p_num

left_knap = [0] + [1e9 for _ in range(100000)]
right_knap = [0] + [1e9 for _ in range(100000)]

for i in range(1, t + 1):
    if p - i >= 0:

        l_w, l_v = q[p - i], i

        if l_w <= m:
            for j in range(m, 0, -1):
                if l_w + j <= m and left_knap[j] != 0:
                    left_knap[l_w + j] = min(left_knap[l_w + j], left_knap[j] + l_v)

            left_knap[l_w] = min(left_knap[l_w], l_v)

    if p + i < len(q):
        r_w, r_v = q[p + i], i

        if r_w <= m:
            for j in range(m, 0, -1):
                if r_w + j <= m and right_knap[j] != 1e9:
                    right_knap[r_w + j] = min(right_knap[r_w + j], right_knap[j] + r_v)

            right_knap[r_w] = min(right_knap[r_w], r_v)

for i in range(0, m):
    if (
        min(left_knap[i], right_knap[m - i]) * 2 + max(left_knap[i], right_knap[m - i])
        <= t
    ):
        exit(print("YES"))

print("NO")
