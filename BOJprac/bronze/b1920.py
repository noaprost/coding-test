import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

m = int(sys.stdin.readline())

findNum = list(map(int, sys.stdin.readline().split()))

for f in findNum:
    s = 0
    e = n - 1
    isFind = False
    while s <= e:
        mid = (s + e) // 2

        if num[mid] < f:
            s = mid + 1
        elif num[mid] > f:
            e = mid - 1
        elif num[mid] == f:
            print(1)
            isFind = True
            break

    if not isFind:
        print(0)
