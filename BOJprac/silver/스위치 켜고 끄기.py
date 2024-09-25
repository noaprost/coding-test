# 1244
import sys

n = int(sys.stdin.readline())
switches = [-1] + list(map(int, sys.stdin.readline().split()))
student_num = int(sys.stdin.readline())


def change(num):
    if switches[num] == 0:
        switches[num] = 1
    else:
        switches[num] = 0
    return


for _ in range(student_num):
    t, num = map(int, sys.stdin.readline().split())

    if t == 1:
        for i in range(num, n + 1, num):
            change(i)
    else:
        change(num)
        for k in range(n // 2):
            if num + k > n or num - k < 1:
                break
            if switches[num + k] == switches[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, n + 1):
    print(switches[i], end=" ")
    if i % 20 == 0:
        print()
