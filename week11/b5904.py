import sys

sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())

# 1. 구하려는 수를 찾으려면 적어도 몇번째 순열까지 구해야하는지 확인 -> 그때의 길이는 l
# 2. 찾으면 함수에 넣고 재귀 실행 앞 블록 길이, 현재 순열 번호, 뒷 블록 길이(앞 블록 길이 + 현재 순열 번호), 구해야되는 인덱스
# 3. 함수에서는 l이 3이 아니면2 범위 체크후 더 작은 함수단위로 이동, 이때 길이를 참고해서 구해야되는 인덱스 업데이트
# 4. 만약 l이 3이 된다면 0, 1, 2중 하나를 얻어서 m인지 o인지 출력


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
