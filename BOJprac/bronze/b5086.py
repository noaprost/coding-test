import sys

a, b = map(int, sys.stdin.readline().split())
case3 = False

while a != 0:
    if a < b:
        if b % a == 0:
            print("factor")
        else:
            case3 = True
    else:
        if a % b == 0:
            print("multiple")
        else:
            case3 = True
    if case3:
        print("neither")
        case3 = False
    a, b = map(int, sys.stdin.readline().split())
