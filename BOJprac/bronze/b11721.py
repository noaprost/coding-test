# 열 개씩 끊어서 출력하기
import sys

s = sys.stdin.readline().rstrip()

count = 0

for k in range(len(s) // 10):
    for i in range(k * 10, k * 10 + 10, 1):
        print(s[i], end="")
        count += 1
    print()
print(s[count:])
