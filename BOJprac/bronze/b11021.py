import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1}".format(i + 1, a + b))

# s = '구구단 {0} x {1} = {2}'.format(a, b, a * b)
