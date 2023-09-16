# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if (a + b + c) > 180 or (a + b + c) < 180:
    print("Error")
else:
    if len(set([a, b, c])) == 3:
        print("Scalene")
    elif len(set([a, b, c])) == 2:
        print("Isosceles")
    elif len(set([a, b, c])) == 1:
        print("Equilateral")
