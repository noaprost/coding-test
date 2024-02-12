# 첫 글자를 대문자로
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    s = list(s)
    s[0] = s[0].upper()

    print("".join(s))
