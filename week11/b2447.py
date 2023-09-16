import sys

n = int(sys.stdin.readline())
star = [["." for _ in range(n)] for _ in range(n)]


def divAndCon(s, r):
    if (int(s / 3)) > 0:
        divAndCon(int(s / 3), r - 3)
    for i in range(r - 3, r):
        for j in range(r - 3, r):
            star[i][j] = "*"
            if i % 3 == 1 and j % 3 == 1:
                star[i][j] = " "


divAndCon(n, n)
print(star)
