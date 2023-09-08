import sys

n = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split()))

m = max(scores)
sum = 0

for i in range(n):
    scores[i] = scores[i] / m * 100
    sum = sum + scores[i]

print(sum / n)
