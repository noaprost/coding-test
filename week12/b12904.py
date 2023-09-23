# A와 B
# s를 t로 바꿀 수 있으면 1, 없으면 0을 출력
import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

t.reverse()
s.reverse()

while True:
    if len(t) == 0:
        exit(print(0))

    if t[-1] == "A":
        t.remove("A")
    else:
        t.reverse()
        if t[-1] == "B":
            t.remove("B")
        else:
            exit(print(0))

    if t == s:
        exit(print(1))
