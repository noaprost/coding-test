# 집합
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys

commandNum = int(sys.stdin.readline())

s = set()

for _ in range(commandNum):
    command = sys.stdin.readline().strip()

    if command[:3] == "add":
        c, v = command.split()
        if int(v) not in s:
            s.add(int(v))

    if command[:3] == "rem":
        c, v = command.split()
        if int(v) in s:
            s.remove(int(v))

    if command[:3] == "che":
        c, v = command.split()
        if int(v) in s:
            print(1)
        else:
            print(0)
    if command[:3] == "tog":
        if int(v) in s:
            s.remove(int(v))
        else:
            s.add(int(v))

    if command[:3] == "all":
        s = set([i for i in range(1, 21)])

    if command[:3] == "emp":
        s = set([])
