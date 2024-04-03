# 인공지능 시계
import sys

h, m, s = map(int, sys.stdin.readline().split())
addTime = int(sys.stdin.readline())

h += addTime // 3600
m += (addTime % 3600) // 60
s += (addTime % 3600) % 60

if s >= 60:
    m += s // 60
    s = s % 60

if m >= 60:
    h += m // 60
    m = m % 60

if h == 24:
    h = 0

if h > 24:
    h = h % 24

print(h, m, s)
