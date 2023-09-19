import sys

sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())


def divAndCon(l, k, i):
    if l == 3:
        if i == 1:
            exit(print("m"))
        else:
            exit(print("o"))

    if i < int((l - k) / 2):
        divAndCon(int((l - k) / 2), k - 1, i)
    elif i < (int((l - k) / 2) + k):
        if i - int((l - k) / 2) == 1:
            exit(print("m"))
        else:
            exit(print("o"))
    else:
        divAndCon(int((l - k) / 2), k - 1, i - int((l - k) / 2) - k)


l = 3
k = 4

while True:
    if l > n:
        break
    l = l * 2 + k
    k += 1

k -= 1

divAndCon(l, k, n)

# l = 25

# print(int((l - 5) / 2))  # 10
# 012 3456 789 10 -> 10은 가운데 부분의 첫인덱스

# print(int((l - 5) / 2) + 5)  # 15
# 012 3456 789 1011121314 15 -> 15는 뒷부분의 첫인덱스

# int((l - 5) / 2)를 m으로 둔다면
# 범위는 다음과 같이 나타낼 수 있음
# n < m
# n >= m and n < m+5
# n >= m+5

# 함수에서 저걸 구한다고 하면
# 현재 전체 길이 -> 앞, 뒷 부분일 경우 m , 가운데일 경우 k
# 함수(l(현재 전체 길이), k(현재 가운데 길이), n(구하려는 인덱스))
# l이 3이 되면 그때 인덱스가 0이면 m 아니라면 o 출력
