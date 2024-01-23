# 상근 버거
import sys

buger = []
juice = []
for _ in range(3):
    t = int(sys.stdin.readline())
    buger.append(t)
    buger.append(t)

for _ in range(2):
    t = int(sys.stdin.readline())
    juice.append(t)

for i in range(0, 6, 2):
    for j in range(0, 2, 2):
        buger[i] += juice[j] - 50
        buger[i + 1] += juice[j + 1] - 50

print(min(buger))
