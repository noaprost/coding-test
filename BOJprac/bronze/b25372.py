# 성택이의 은밀한 비밀번호
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    if 6 <= len(s) <= 9:
        print("yes")
    else:
        print("no")
