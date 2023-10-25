# A->B

import sys

a, b = sys.stdin.readline().rstrip().split()

calc = 1

while a != b:
    if int(a) > int(b):
        exit(print(-1))

    if b[-1] == "1":
        b = b[: len(b) - 1]
        calc += 1
    else:
        if int(b) % 2 == 0:
            b = str(int(b) // 2)
            calc += 1
        else:
            exit(print(-1))
print(calc)
