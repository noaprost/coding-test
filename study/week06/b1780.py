# 종이의 개수
import sys


def samePaperCheck(n, arr):
    tmp = arr[0][0]
    for i in range(n):
        for j in range(n):
            if tmp != arr[i][j]:
                return False
    return True


n = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def paperCut(n, arr):
    if(n == 1):
        print()
    else:
        paperCut()
