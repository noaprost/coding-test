# 가운데를 말해요
# 중간값 찾기
# idea : 최소힙, 우선순위 큐, sort(), 삽입정렬 -> 넷다 시간 초과
import sys


def getMiddleIdx(n):
    if n % 2 == 0:
        return int(n / 2) - 1
    else:
        return int((n + 1) / 2) - 1


def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]


li = []

num = int(sys.stdin.readline())
while num > 0:
    x = int(sys.stdin.readline())
    li.append(x)
    insertion_sort(li)

    mIdx = getMiddleIdx(len(li))
    print("ans : ", li[mIdx])

    num = num - 1
