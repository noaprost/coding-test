# 방 번호
import sys
import math

n = sys.stdin.readline().rstrip()

num = [0] * 10
sixCnt = 0
nineCnt = 0

for nn in n:
    num[int(nn)] += 1

sixNineCnt = 0
sixCnt = num[6]
nineCnt = num[9]
num[6] = 0
num[9] = 0
m = max(num)

if sixCnt > m and nineCnt > m:
    sixCnt -= m
    nineCnt -= m
    sixNineCnt = math.ceil((sixCnt + nineCnt) / 2)
elif sixCnt > m:
    sixCnt -= m
    sixNineCnt = math.ceil(sixCnt / 2)
elif nineCnt > m:
    nineCnt -= m
    sixNineCnt = math.ceil(nineCnt / 2)

print(m + sixNineCnt)
