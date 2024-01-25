# 하노이 탑
import sys


def hanoi(n, start, end, via):
    if n == 1:
        move.append([start, end])
    else:
        hanoi(n - 1, start, via, end)
        move.append([start, end])
        hanoi(n - 1, via, end, start)


n = int(sys.stdin.readline())

if n > 20:
    exit(print(pow(2, n) - 1))

move = []
hanoi(n, 1, 3, 2)
print(len(move))
for m in move:
    print(*m)
