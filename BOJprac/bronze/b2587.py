import sys

num = [int(sys.stdin.readline()) for _ in range(5)]

num.sort()
print(int(sum(num) / 5))
print(num[2])
