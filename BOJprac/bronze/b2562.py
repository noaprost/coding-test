import sys

num = [int(sys.stdin.readline()) for i in range(9)]

m = max(num)

i = num.index(m)

print(m)
print(i + 1)
