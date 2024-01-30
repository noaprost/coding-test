import sys

n = int(sys.stdin.readline())
star = [[" " for _ in range(n)] for _ in range(n)]


def divAndCon(x, y, l):
    if l // 3 == 1:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                star[x + i][y + j] = "*"

    else:
        l2 = int(l / 3)
        divAndCon(x, y, l2)
        divAndCon(x + l2, y, l2)
        divAndCon(x + l2 * 2, y, l2)
        divAndCon(x, y + l2, l2)
        divAndCon(x + l2 * 2, y + l2, l2)
        divAndCon(x, y + l2 * 2, l2)
        divAndCon(x + l2, y + l2 * 2, l2)
        divAndCon(x + l2 * 2, y + l2 * 2, l2)


divAndCon(0, 0, n)

for s in star:
    for ss in s:
        print(ss, end="")
    print()
