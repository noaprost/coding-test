import sys

mbti = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

mbtis = [sys.stdin.readline().rstrip() for _ in range(n)]

print(mbtis.count(mbti))