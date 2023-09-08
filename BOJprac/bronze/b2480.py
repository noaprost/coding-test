import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == b and b == c and a == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    if a == b:
        print(1000 + a * 100)
    else:
        print(1000 + c * 100)

elif a != b and b != c and a != c:
    print(max(a, b, c) * 100)
