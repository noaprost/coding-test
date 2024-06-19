# 2448
import sys


def star(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    stars = star(n // 2)
    x = [" " * (n // 2) + i + " " * (n // 2) for i in stars]
    y = [i + " " + i for i in stars]
    return x + y


n = int(sys.stdin.readline())
result = star(n)
print("\n".join(result))
