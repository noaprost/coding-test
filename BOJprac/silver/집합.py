# 11723
import sys

commandNum = int(sys.stdin.readline())
s = set()

for _ in range(commandNum):
    command = sys.stdin.readline().strip().split()

    if command[0] == "add":
        c, v = command
        s.add(int(v))

    if command[0] == "remove":
        c, v = command
        s.discard(int(v))

    if command[0] == "check":
        c, v = command
        if int(v) in s:
            print(1)
        else:
            print(0)

    if command[0] == "toggle":
        c, v = command
        if int(v) in s:
            s.remove(int(v))
        else:
            s.add(int(v))

    if command[0] == "all":
        s = set([i for i in range(1, 21)])

    if command[0] == "empty":
        s = set([])
