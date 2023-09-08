import sys

a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

if a + ((b + c) // 60) > 23:
    print(a + ((b + c) // 60) - 24, (b + c) % 60)
else:
    print(a + ((b + c) // 60), (b + c) % 60)
