import sys

n = int(sys.stdin.readline())

# 초기화
i = 1
endNum = 666

while n != i:
    endNum += 1
    if "666" in str(endNum):
        i += 1

print(endNum)
