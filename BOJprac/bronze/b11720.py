import sys

n = int(sys.stdin.readline())

s = sys.stdin.readline().strip()

sum = 0

for i in range(n):
    sum += int(s[i])

print(sum)
