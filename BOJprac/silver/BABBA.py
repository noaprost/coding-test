import sys

k = int(sys.stdin.readline())
countA = 1
countB = 0

for _ in range(k):
    tmp = countB
    countB += countA
    countA = tmp

print(countA, countB)
