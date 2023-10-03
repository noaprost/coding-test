# N-Queen
import sys

n = int(sys.stdin.readline())
count = 0
row = [-1 for _ in range(n)]  # 퀸의 위치가 저장될 배열 (최대 15)


# 현재 진행된 열까지만 조건을 체크
def check(col):
    for i in range(col):
        # 대각선도 결국은 직선이므로 x변화량과 y변화량이 같으면 같은 직선내에 있는 것
        if row[col] == row[i] or abs(row[col] - row[i]) == col - i:
            return False
    return True


# depth : 현재 진행된 열의 위치
def Queen(depth):
    global count
    if depth == n:
        count += 1  # 열을 다 돌때까지 퀸을 놓을 수 있다면 경우의 수 +1
    else:
        for i in range(n):
            row[depth] = i  # 행의 값을 하나씩 넣음
            if check(depth):  # i행, depth열에 넣을 수 있다면
                Queen(depth + 1)  # 다음 열로 이동


Queen(0)  # 0열부터 시작
print(count)
