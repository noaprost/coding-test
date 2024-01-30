# 가운데를 말해요
# 중간값 찾기
# idea : 최소힙, 우선순위 큐, sort(), 삽입정렬 -> 넷다 시간 초과
# heap or 우선순위 큐 두 개로 개수의 중간값을 관리하면서 정렬 시간 단축
# 우선순위 큐 -> 맨끝 값을 가져오는게 안됨
# heap으로 구현

import sys
import heapq

global midNum

heap1 = []  # 중간값보다 작은 값이 담길 큐
heap2 = []  # 중간값보다 큰 값이 담길 큐

midNum = 100000

num = int(sys.stdin.readline())

while num > 1:
    x = int(sys.stdin.readline())
    s1 = len(heap1)
    s2 = len(heap2)

    # 맨 처음 원소를 넣을 때
    if s1 == 0 and s2 == 0:
        midNum = x
        print(midNum)
        heapq.heappush(heap1, (-1 * x, x))
        continue

    # 힙의 길이가 같을 때
    if s1 == s2:
        print("midNum, x : ", midNum, x)
        if midNum > x:
            heapq.heappush(heap1, (-1 * x, x))
            midNum = heap1[0][1]
            print(midNum)
        else:
            heapq.heappush(heap2, x)
            midNum = heap2[0]
            print(midNum)
    elif s1 > s2:
        if midNum > x:
            heapq.heappush(heap1, (-1 * x, x))
        else:
            heapq.heappush(heap2, x)

        if s1 > s2:
            heapq.heappush(heap2, heap1[0][1])
            heapq.heappop(heap1)

        midNum = heap1[0][1]
        print(midNum)

    elif s1 < s2:
        if midNum > x:
            heapq.heappush(heap1, (-1 * x, x))
        else:
            heapq.heappush(heap2, x)

        if s1 < s2:
            heapq.heappush(heap1, heapq.heappop(heap2))

        midNum = heap1[0][1]
        print(midNum)

    num = num - 1

    print("heap1 : ", heap1)
    print("heap2 : ", heap2)
