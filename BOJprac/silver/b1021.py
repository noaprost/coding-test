# 회전하는 큐
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
position = list(map(int, sys.stdin.readline().split()))
dq = deque()
count = 0

for i in range(1, n + 1):
    dq.append(i)

for p in position:
    while True:
        if dq[0] == p:
            dq.popleft()
            break
        else:
            # 뽑아내려는 위치 인덱스가 dq의 길이를 반으로 나눈 것보다 작으면 왼쪽으로 움직여야 최소
            if dq.index(p) < len(dq) / 2:
                while dq[0] != p:
                    dq.append(dq.popleft())
                    count += 1
            # 뽑아내려는 위치 인덱스가 dq의 길이를 반으로 나눈 것보다 크면 오른쪽으로 움직여야 최소
            else:
                while dq[0] != p:
                    dq.appendleft(dq.pop())
                    count += 1

print(count)