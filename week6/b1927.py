# 최소 힙
# heapq, PriorityQueue 둘다 시간초과
# input -> sys.stdin.readline 으로 변경하니 성공
from queue import PriorityQueue
import sys

que = PriorityQueue()

n = int(input())

for i in range(n):
    item = int(sys.stdin.readline())
    if item == 0:  # 입력이 0이면
        if que.empty():  # 큐가 비어있으면
            print(0)
        else:
            print(que.get())  # 비어있지 않으면 큐에서 꺼내서 출력
    else:
        que.put(item)  # 입력이 0이 아니면 큐에 삽입
