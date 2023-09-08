import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

b1 = b // 100
b2 = (b % 100) // 10
b3 = b % 10

ans = a * b1 * 100 + a * b2 * 10 + a * b3
print(a * b3)
print(a * b2)
print(a * b1)
print(ans)
