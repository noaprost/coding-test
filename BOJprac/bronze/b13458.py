# 시험 감독
import sys

n = int(sys.stdin.readline())
test_rooms = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
ans = 0

for room in test_rooms:
    if room <= b:
        ans += 1
    else:
        ans += 1
        room -= b

        if room % c == 0:
            ans += room // c
        else:
            ans += room // c + 1

print(ans)
