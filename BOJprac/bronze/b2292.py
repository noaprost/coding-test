import sys

n = int(sys.stdin.readline())

# 방의 개수는 1 -> 6을 제외 6개씩 늘어남
# 1
# 6(2~7)
# 12(8~19)
# 18(20~37)
# 24(38~61)

# 찾아야하는것 어느 범위에 있는지 -> 안쪽으로보터 몇번째 방에 있는지

curNum = 1
roomNum = 1
i = 1

while True:
    if n == 1:
        break
    else:
        if n - curNum <= 0:
            break
        else:
            roomNum += 1
            curNum += 6 * i
    i += 1


print(roomNum)
