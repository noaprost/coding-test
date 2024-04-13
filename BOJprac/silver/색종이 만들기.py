import sys

n = int(sys.stdin.readline())
paper = []
oneCount = 0
zeroCount = 0
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))


def isOne(x, y, length):
    for i in range(x, x + length):
        for j in range(y, y + length):
            if paper[i][j] == 0:
                return False
    return True


def isZero(x, y, length):
    for i in range(x, x + length):
        for j in range(y, y + length):
            if paper[i][j] == 1:
                return False
    return True


def divAndCon(x, y, length):
    global oneCount
    global zeroCount

    if length == 0:
        return 0

    else:
        if isOne(x, y, length):
            oneCount += 1
        elif isZero(x, y, length):
            zeroCount += 1
        else:
            d = int(length / 2)
            divAndCon(x, y, d)
            divAndCon(x + d, y, d)
            divAndCon(x, y + d, d)
            divAndCon(x + d, y + d, d)


divAndCon(0, 0, n)

print(zeroCount)
print(oneCount)
