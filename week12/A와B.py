# 12904
# s를 t로 바꿀 수 있으면 1, 없으면 0을 출력
import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

while len(s) != len(t):
    if t[-1] == "A":
        t.pop()

    elif t[-1] == "B":
        t.pop()
        t.reverse()

if t == s:
    print(1)
else:
    print(0)
