# 7662
import sys
import heapq

caseNum = int(sys.stdin.readline())

for _ in range(caseNum):
    commandNum = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    visited = [False for _ in range(commandNum)]

    for i in range(commandNum):
        op, num = sys.stdin.readline().rstrip().split()
        num = int(num)

        if op == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        else:
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    if min_heap and max_heap:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
    else:
        print("EMPTY")
