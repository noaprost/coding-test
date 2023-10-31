# AC
# 필요한 함수 R, D
import sys

t = int(sys.stdin.readline()) # 테스트 케이스 개수

for _ in range(t):
    reverse = False
    isError = False
    p = sys.stdin.readline().rstrip() # 수행할 함수 ex)RDD
    n = int(sys.stdin.readline()) # 배열 원소 개수
    arr = sys.stdin.readline().rstrip() # 배열

    if not n: # 원소 개수가 0이면
        num = []
    else:
        num = list(map(int, list(arr[1:-1].split(","))))
    
    # reverse랑 delete를 도와줄 인덱스
    start = 0
    end = n - 1

    for pp in p: # 함수에서 하나씩 꺼냄
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
