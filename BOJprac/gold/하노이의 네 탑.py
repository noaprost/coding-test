# 9942
import sys


def power(num):
    res = 1
    for _ in range(num):
        res *= 2
    return res


i = 1

while True:
    try:
        n = int(sys.stdin.readline())
        t, count, s = 1, 0, 0

        while t * (t + 1) / 2 < n:
            t += 1
        t -= 1

        count = n - t * (t + 1) / 2

        for j in range(t):
            s = s + power(j) * (j + 1)

        s += power(t) * count
        print("Case", i, end="")
        print(":", int(s))

        i += 1

    except:
        break
