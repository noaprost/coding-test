# 종이의 개수
# idea : 9칸을 어떤식으로 나누고 검사할 것인지 함수를 짜고, 나눈 칸의 크기가 1이면 return
import sys

n = int(sys.stdin.readline())

paper = []
count = [0, 0, 0]
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))


def isSame(x, y, length):
    tmp = paper[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if paper[i][j] != tmp:
                return 2
    return tmp


def divAndCon(x, y, length):
    if length == 0:
        return 0

    c = isSame(x, y, length)

    if c == -1:
        count[-1] += 1
    elif c == 0:
        count[0] += 1
    elif c == 1:
        count[1] += 1
    elif c == 2:
        d = int(length / 3)
        divAndCon(x, y, d)
        divAndCon(x, y + d, d)
        divAndCon(x, y + d * 2, d)
        divAndCon(x + d, y, d)
        divAndCon(x + d, y + d, d)
        divAndCon(x + d, y + d * 2, d)
        divAndCon(x + d * 2, y, d)
        divAndCon(x + d * 2, y + d, d)
        divAndCon(x + d * 2, y + d * 2, d)


divAndCon(0, 0, n)

print(count[-1])
print(count[0])
print(count[1])
