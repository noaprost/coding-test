# 행동 1 +1 하기
# 행동 2 -1 하기
# 행동 3 *2 하기
# bfs로 하면 무조건 최단 경로가 나온다고 함

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
sec = [0] * 100002

que = deque([n])

while que:
    dis = que.popleft()
    if dis == k:
        print(sec[dis])
        break
    # 행동 3가지를 다음과 같이 인접노드를 탐색하듯이 표현 가능
    for i in (dis - 1, dis + 1, dis * 2):
        if (0 <= i and i < 100001) and sec[i] == 0:
            sec[i] = sec[dis] + 1  # 초 업데이트
            que.append(i)
