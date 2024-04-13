import sys

stackLeft = []
stackRight = []

cm = sys.stdin.readline().rstrip()

for c in cm:
    stackLeft.append(c)

cmNum = int(sys.stdin.readline())

for _ in range(cmNum):
    c = sys.stdin.readline().rstrip()

    if c[0] == "P":
        p, s = c.split()
        stackLeft.append(s)

    elif c[0] == "L":
        if len(stackLeft) == 0:
            continue
        else:
            tmp = stackLeft.pop()
            stackRight.append(tmp)

    elif c[0] == "D":
        if len(stackRight) == 0:
            continue
        else:
            tmp = stackRight.pop()
            stackLeft.append(tmp)

    elif c[0] == "B":
        if len(stackLeft) == 0:
            continue
        else:
            stackLeft.pop()

for sl in stackLeft:
    print(sl, end="")

stackRight.reverse()

for sr in stackRight:
    print(sr, end="")
