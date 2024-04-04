# 모음의 개수
import sys


s = sys.stdin.readline().rstrip()

while s != "#":
    total = 0
    s = s.lower()
    total += s.count("a")
    total += s.count("e")
    total += s.count("i")
    total += s.count("o")
    total += s.count("u")

    print(total)

    s = sys.stdin.readline().rstrip()
