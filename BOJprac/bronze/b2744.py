# 대소문자 바꾸기
import sys

ss = sys.stdin.readline().rstrip()

ans = ""

for s in ss:
    if s.islower():
        ans += s.upper()
    else:
        ans += s.lower()

print(ans)
