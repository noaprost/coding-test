# 가운데를 말해요
# 중간값 찾기
# idea : 최소힙, 우선순위 큐, sort(), 삽입정렬 -> 넷다 시간 초과
# heap or 우선순위 큐 두 개로 개수의 중간값을 관리하면서 정렬 시간 단축
# 우선순위 큐 -> 맨끝 값을 가져오는게 안됨
# heap으로 구현

import heapq
import sys

n = int(sys.stdin.readline())

leftHeap = []
rightHeap = []

for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])
