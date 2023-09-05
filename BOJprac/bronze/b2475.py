import sys

n, b = sys.stdin.readline().split()
b = int(b)
sum = 0
idx = len(n) - 1

# -55를 해주어야함

for i in range(0, len(n)):
    if ord(n[i]) > 64:
        num = ord(n[i]) - 55
    else:
        num = int(n[i])

    sum = sum + pow(b, idx) * num

    idx = idx - 1
print(sum)
