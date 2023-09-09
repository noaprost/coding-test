import sys

n1, n2 = sys.stdin.readline().split()

n1 = n1[::-1]
n2 = n2[::-1]

if int(n1) > int(n2):
    print(int(n1))
else:
    print(int(n2))
