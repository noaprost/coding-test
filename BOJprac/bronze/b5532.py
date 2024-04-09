# 방학 숙제
import sys
import math

l = int(sys.stdin.readline())

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
aPage = int(sys.stdin.readline())
bPage = int(sys.stdin.readline())

aL = math.ceil(a / aPage)
bL = math.ceil(b / bPage)

if aL > bL:
    maxL = aL
else:
    maxL = bL

print(l - maxL)
