# 15649
# 배열에 저장 -> 제일 기초(재귀할때 배열을 같이 넘기는 것, 크기가 작을 경우 부담이 덜되서 좋은거고 10만번 넘기는데 배열을 넘기는 건 부담이 감)
import sys

n, m = map(int, sys.stdin.readline().split())


def backTracking(num, depth, arr):
    if depth == 0:
        print(*arr)
        return

    if num == n:
        return

    for i in range(1, n + 1):
        if i < num:
            continue
        elif i == num:
            arr = []
            arr.append(i)
        else:
            if i not in arr:
                backTracking(num, depth - 1, arr + [i])
if m == 1:
    for i in range(1, n + 1):
        print(i)
else:
    backTracking(0, m, [])
