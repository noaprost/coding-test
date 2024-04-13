import sys
import math

n = sys.stdin.readline().rstrip()

num = [0] * 10

for nn in n:
    num[int(nn)] += 1

sixNineCnt = num[6] + num[9]
num[6] = 0
num[9] = 0
m = max(num)

setNum = max(m, math.ceil(sixNineCnt / 2))

print(setNum)
