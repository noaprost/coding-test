# 모음의 개수
import sys

s = sys.stdin.readline().rstrip()

ans = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

print(ans)