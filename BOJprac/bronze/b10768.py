# 특별한 날
import sys

m = int(sys.stdin.readline())
d = int(sys.stdin.readline())

if m < 2:
    exit(print("Before"))
elif m == 2:
    if d < 18:
        exit(print("Before"))
    elif d == 18:
        exit(print("Special"))
    else:
        exit(print("After"))
else:
    exit(print("After"))
