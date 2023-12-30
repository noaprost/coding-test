import sys

num = 1

for _ in range(3):
    n = int(sys.stdin.readline())
    num *= n

num = str(num)

count = []

for i in range(10):
    count.append(num.count(str(i)))

for c in count:
    print(c)
