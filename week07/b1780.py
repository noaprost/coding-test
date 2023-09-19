# 종이의 개수
# idea : 9칸을 어떤식으로 나누고 검사할 것인지 함수를 짜고, 나눈 칸의 크기가 1이면 return
global count


def addCount(item):
    if item == -1:
        count[0] = count[0] + 1
    elif item == 0:
        count[1] = count[1] + 1
    elif item == 1:
        count[2] = count[2] + 1


def isSame(n, arr):
    item = arr[0][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != item:
                return False
    return True


def paperCut(n, arr):
    if isSame(n, arr):
        addCount(arr[0][0])
    else:
        nn = int(n / 3)
        # for문으로 종이를 각각 자르기
        paperCut(nn, arr)


n = int(input())
count = [0, 0, 0]

arr = [list(map(int, input().split())) for _ in range(n)]

paperCut(n, arr)

# TODO
# 행렬 표현할 방법 생각하기
# 잘라서 코드가 동작하는 과정 그려보거나 생각해보기
