# AC
# 필요한 함수 R, D
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    reverse = False
    isError = False
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()
    if not n:
        num = []
    else:
        num = list(map(int, list(arr[1:-1].split(","))))
    start = 0
    end = n - 1

    for pp in p:
        if pp == "R":
            reverse = not reverse
        elif pp == "D":
            if start > end:
                print("error")
                isError = True
                break
            if reverse:
                end -= 1
            else:
                start += 1
    if isError:
        continue

    if reverse:
        print("[", end="")
        for i in range(end, start - 1, -1):
            if i != start:
                print(num[i], end="")
                print(",", end="")
            else:
                print(num[i], end="")
        print("]")
    else:
        print("[", end="")
        for i in range(start, end + 1):
            if i != end:
                print(num[i], end="")
                print(",", end="")
            else:
                print(num[i], end="")
        print("]")
