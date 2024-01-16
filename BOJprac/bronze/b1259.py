# 팰린드롬수
import sys

num = sys.stdin.readline().rstrip()


while num != "0":
    length = len(num)
    isP = True

    if length % 2 == 0:
        for i in range((length - 2) // 2+1):
            if num[i] != num[-(i + 1)]:
                isP = False
                break
        if isP:
            print("yes")
        else:
            print("no")
    else:
        for i in range((length - 1) // 2+1):
            if num[i] != num[-(i + 1)]:
                isP = False
                break
        if isP:
            print("yes")
        else:
            print("no")

    num = sys.stdin.readline().rstrip()
