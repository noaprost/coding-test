# 최소 힙
# heapq, PriorityQueue 둘다 시간초과
# input -> sys.stdin.readline 으로 변경하니 성공
from queue import PriorityQueue
import sys

que = PriorityQueue()

n = int(input())

for i in range(n):
    item = int(sys.stdin.readline())
    if item == 0:
        if que.empty():
            print(0)
        else:
            print(que.get())
    else:
        que.put(item)
